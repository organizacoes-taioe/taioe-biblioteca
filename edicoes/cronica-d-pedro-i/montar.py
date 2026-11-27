"""Crónica de D. Pedro I — passo 6: junta tudo e grava os textos que vão ao git.

    python3 -I edicoes/cronica-d-pedro-i/montar.py <pasta>

Lê <pasta>/estab.json (estabelecer.py) e <pasta>/pg16633.txt; aplica as correções lidas no fac-símile
(decisoes.CORRECOES), as correções de OCR por tipo (grafia-cauda.tsv), junta as palavras que o OCR
partiu, põe os títulos conferidos (decisoes.TITULOS), moderniza (modernizar.py) e divide os capítulos
em parágrafos pelos da edição de 1895. Grava, na pasta da obra:
  original/parte-NN.txt   o texto de 1816 (NN = 00 prólogo, 01…44 capítulos), um parágrafo por bloco
  atualizado/parte-NN.txt o mesmo na grafia de hoje, com os mesmos parágrafos
  titulos.json            [{n, titulo, original}] na mesma ordem
"""
import collections
import json
import os
import re
import sys
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import decisoes as D  # noqa: E402
import modernizar as M  # noqa: E402
import estabelecer as ES  # noqa: E402

FIM = {'.', '?', '!'}
PONT = {',', ';', ':', '.', '?', '!', '»'}


def corrigir(E):
    erros = []
    for p, k, velho, novo in D.CORRECOES:
        x = E[p]['corpo'][k]
        if x['t'] != velho:
            erros.append(f'parte {p}, {k}: esperava «{velho}», há «{x["t"]}»')
            continue
        x['t'] = novo
        x['conferido'] = True
    if erros:
        sys.exit('\n'.join(erros))
    for p in E:
        novo = []
        for x in p['corpo']:
            if 'p' in x:
                novo.append(x)
                continue
            lw = x['t'].lower()
            if lw in M.LIXO and not x.get('conferido'):
                continue
            if lw in M.OCR and not x.get('conferido'):
                c = M.OCR[lw]
                x['t'] = (c[0].upper() + c[1:]) if x['t'][:1].isupper() else c
            # palavra impressa separada (el Iffamte, de Graada): vira dois itens
            for i, parte in enumerate(x['t'].split(' ')):
                y = dict(x, t=parte)
                if i:
                    y.pop('a95', None), y.pop('op', None)
                novo.append(y)
        p['corpo'] = novo


def juntar(E):
    """Junta as metades de palavra partida no fim da linha que o OCR deixou separadas (mun do, cou sas)."""
    freq = collections.Counter(x['t'].lower() for p in E for x in p['corpo'] if 'p' not in x)
    n = 0
    for p in E:
        out = []
        for x in p['corpo']:
            if out and 'p' not in x and 'p' not in out[-1]:
                a, b = out[-1]['t'], x['t']
                ab = (a.rstrip('-') + b).lower()
                pedaco = lambda w: freq[w.lower()] <= 2 or w.endswith('-')
                if a.endswith('-') or (freq[ab] >= 2 and (pedaco(a) or pedaco(b))) or \
                        (ab in M.CAUDA and pedaco(a) and pedaco(b)):
                    out[-1] = dict(out[-1], t=a.rstrip('-') + b)
                    n += 1
                    continue
            out.append(x)
        p['corpo'] = out
    return n


def titulos(E, p95):
    for p, p9 in zip(E, p95):
        if p['n'] == 0:
            p['titulo'] = []
            continue
        ws = re.findall(r"[A-Za-zÀ-ÿ']+|[,;:.]", D.TITULOS[p['n']])
        w95 = ES.TOK95.findall(p9['titulo'])
        ka = [ES.k16(w) for w in ws]
        kb = [ES.k16(w) for w in w95]
        al = {}
        for op, a0, a1, b0, b1 in SequenceMatcher(None, ka, kb, autojunk=False).get_opcodes():
            if op == 'equal' or (op == 'replace' and a1 - a0 == b1 - b0):
                for d in range(a1 - a0):
                    al[a0 + d] = (w95[b0 + d], op)
        p['titulo'] = [({'t': w, 'p': 1} if w in ',;:.' else
                        {'t': w, **({'a95': al[i][0], 'op': al[i][1]} if i in al else {})}) for i, w in enumerate(ws)]


def frase(itens, campo):
    """Junta os itens num texto: pontuação colada, aspas, maiúscula no começo da frase (no moderno)."""
    out, ini, aberta = [], True, False
    for x in itens:
        t = x[campo]
        if t in ('«', '»'):          # as aspas de 1816 (uma em cada linha das cartas) não vão
            continue
        if t in PONT:
            if out and out[-1] == t:
                continue
            out.append(t)
            if t in FIM:
                ini = True
            continue
        if t == '«':
            out.append(t)
            continue
        if campo == 'm' and ini and t[:1].islower():
            t = t[0].upper() + t[1:]
        elif campo == 'm' and not ini and t[:1].isupper() and not x.get('nome'):
            t = t[0].lower() + t[1:]
        if campo == 't' and ini and t[:1].islower() and out and out[-1] in FIM:
            pass
        out.append(t)
        ini = False
    s = ' '.join(out)
    s = re.sub(r' ([,;:.?!»])', r'\1', s)
    s = re.sub(r'« ', '«', s)
    s = re.sub(r'\b([Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Tt]rezentos|[Qq]uatro|[Dd]uz|[Tt]rez|[Qq]uinhen) (centos|çemtos)\b', r'\1\2', s)
    return s.strip()


CAPS = None
FEM = {'parte', 'mercê', 'reverência', 'gente', 'morte', 'honra', 'hoste', 'fome', 'sede'}
NOMES_COMUNS = {'granada', 'guarda', 'leão', 'castro', 'vermelho', 'porto', 'lobato', 'coroa', 'cruz', 'santa', 'são',
                'evangelhos', 'deus', 'papa', 'senhor', 'cristo', 'bispo'}


def nomes(E):
    """No texto moderno, maiúscula só no começo da frase e nos nomes: o que 1895 escreve com maiúscula,
    o que o dicionário só traz com maiúscula e o que nem está no léxico (Calatayud, Valladolid)."""
    global CAPS
    if CAPS is None:
        baixas, altas = set(), set()
        for w in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore'):
            w = w.strip()
            (altas if w[:1].isupper() else baixas).add(w.lower())
        CAPS = altas - baixas
    lex = M.G.lexico()
    for p in E:
        for campo in ('titulo', 'corpo'):
            ant = '.'
            for x in p[campo]:
                if 'p' in x:
                    ant = x['t']
                    continue
                inicio, ant = ant in FIM or ant == ';', x['t']
                m = x['m']
                a = x.get('a95', '') if x.get('op') in ('equal', 'replace') else ''
                if a and ' ' not in a and a[:1].isupper() and m[:1].islower() and m.lower() in CAPS:
                    x['m'] = m = m[0].upper() + m[1:]
                tab = M.GRAFIA.get(x['t'].lower()) or M.CAUDA.get(x['t'].lower()) or ''
                if tab[:1].isupper():
                    x['m'] = m = m[:1].upper() + m[1:]
                    x['nome'] = True
                    continue
                if not m[:1].isupper():
                    x['nome'] = False
                elif a and ' ' not in a:
                    # 1895 com maiúscula: nome, salvo no começo de frase (Pois, E, Como), onde só vale
                    # se a palavra não for comum (o dicionário só a traz com maiúscula, ou nem a traz)
                    pal = M.G.ao1990(a.lower())
                    x['nome'] = a[:1].isupper() and x['t'][:1].isupper() and (pal in CAPS or pal not in lex or pal in NOMES_COMUNS)
                else:
                    pal = m.split(' ')[0].lower()
                    x['nome'] = pal in CAPS or pal not in lex or pal in ('dom', 'dona', 'deus')


def paragrafos(p, p9):
    """Os limites dos parágrafos de 1895, levados ao texto de 1816 (no fim de frase mais próximo)."""
    wt = len(ES.TOK95.findall(p9['titulo'])) if p['n'] else 0
    lim, c = [], wt
    for par in p9['pars'][:-1]:
        c += len(ES.TOK95.findall(par))
        lim.append(c)
    corpo = p['corpo']
    cortes = []
    for b in lim:
        k = next((i for i, x in enumerate(corpo) if x.get('i95', -1) >= b and 'p' not in x), None)
        if k is None:
            continue
        for j in range(k, max(0, k - 10), -1):
            if corpo[j - 1]['t'] in FIM:
                k = j
                break
        else:
            continue
        if k not in cortes and 0 < k < len(corpo):
            cortes.append(k)
    cortes = sorted(set(cortes))
    return [corpo[a:b] for a, b in zip([0] + cortes, cortes + [len(corpo)])]


def main(pasta):
    E = json.load(open(os.path.join(pasta, 'estab.json'), encoding='utf-8'))
    p95 = ES.partes_1895(os.path.join(pasta, 'pg16633.txt'))
    corrigir(E)
    print(juntar(E), 'palavras juntadas')
    # palavra repetida (de 1816 a 1816 nunca vem dobrada: é o reclamo do pé da página ou o pedaço que o
    # OCR leu duas vezes)
    dup = 0
    for p in E:
        out = []
        for x in p['corpo']:
            if out and 'p' not in x and 'p' not in out[-1] and x['t'].lower() == out[-1]['t'].lower():
                dup += 1
                continue
            out.append(x)
        p['corpo'] = out
    print(dup, 'repetidas tiradas')
    titulos(E, p95)
    rel, trocas = M.modernizar(E)
    nomes(E)
    # vírgula seguida de maiúscula que não é nome (», Este Rei», «, E»): o OCR leu vírgula no lugar do ponto
    for p in E:
        c = p['corpo']
        for i in range(len(c) - 1):
            if c[i].get('t') == ',' and 'p' in c[i] and 'p' not in c[i + 1] and c[i + 1]['t'][:1].isupper() \
                    and not c[i + 1].get('nome'):
                c[i]['t'] = c[i]['m'] = '.'
    os.makedirs(os.path.join(AQUI, 'original'), exist_ok=True)
    os.makedirs(os.path.join(AQUI, 'atualizado'), exist_ok=True)
    tit = []
    palavras = 0
    for p, p9 in zip(E, p95):
        pars = paragrafos(p, p9)
        orig = '\n\n'.join(frase(x, 't') for x in pars) + '\n'
        mod = '\n\n'.join(frase(x, 'm') for x in pars) + '\n'
        mod = re.sub(r'\b(\w+) \1\b', r'\1', mod)       # palavra dobrada pela junção de dois itens
        # «gram» (grande encurtado): grã antes de feminino, grão antes de masculino
        mod = re.sub(r'\b([Gg])rã (\w+)', lambda m: m.group(1) + ('rã ' if re.search(r'(a|as|ção|ções|dade|dades|gem|ez)$', m.group(2)) else 'rão ') + m.group(2), mod)
        for de, para in D.TROCAS_MODERNO.get(p['n'], []) + D.TROCAS_MODERNO.get('*', []):
            if de not in mod and p['n'] in D.TROCAS_MODERNO:
                print('troca não aplicada:', p['n'], de)
            mod = mod.replace(de, para)
        nn = f'{p["n"]:02d}'
        open(os.path.join(AQUI, 'original', f'parte-{nn}.txt'), 'w', encoding='utf-8').write(orig)
        open(os.path.join(AQUI, 'atualizado', f'parte-{nn}.txt'), 'w', encoding='utf-8').write(mod)
        palavras += len(re.findall(r'\w+', mod))
        tit.append({'n': p['n'], 'original': frase(p['titulo'], 't'), 'titulo': frase(p['titulo'], 'm')})
    json.dump(tit, open(os.path.join(AQUI, 'titulos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(pasta, 'sem_par.tsv'), 'w', encoding='utf-8') as f:
        for (w, a), n in rel.most_common():
            f.write(f'{w}\t{a}\t{n}\n')
    with open(os.path.join(pasta, 'trocas.tsv'), 'w', encoding='utf-8') as f:
        for (fo, w, n, a), c in sorted(trocas.items(), key=lambda kv: -kv[1]):
            f.write(f'{fo}\t{w}\t{n}\t{a}\t{c}\n')
    print(len(E), 'partes;', palavras, 'palavras no texto atualizado;', len(rel), 'tipos sem par')


if __name__ == '__main__':
    main(sys.argv[1])
