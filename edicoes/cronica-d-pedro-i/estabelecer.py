"""Crónica de D. Pedro I — passo 4: o texto de 1816 a partir da colação (colacao.py) e o alinhamento
com a edição de 1895 (Bibliotheca de Classicos Portuguezes, Project Gutenberg 16633).

    python3 -I edicoes/cronica-d-pedro-i/estabelecer.py <pasta>

Lê <pasta>/slots.json (colacao.py) e <pasta>/pg16633.txt; grava <pasta>/estab.json (por parte: o título
e as palavras de 1816, cada uma com a palavra de 1895 alinhada e o grau de certeza) e
<pasta>/duvidas.tsv (os lugares a conferir no fac-símile).

Em cada lugar: as leituras dos quatro testemunhos se desdobram nas formas que o OCR pode ter
confundido (o s longo ſ lido como f; as ligaduras ſt e ſſ lidas como íl, ít, íf, íT, lT, íF…; os
acentos que o dicionário do OCR põe: necessária, própria, pêra), e ganha a forma com mais apoio;
no empate (sobretudo f × s), a mais próxima da palavra de 1895 e, sem ela, a mais frequente no
resto do texto. Os acentos agudo, grave e circunflexo saem (a edição de 1816 quase não os usa;
os poucos verdadeiros se repõem em decisoes.py); o til e a cedilha ficam.
"""
import collections
import math
import itertools
import json
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher

PESO = {'A': 1.0, 'B': 1.0, 'C': 1.0, 'D': 0.8}
PONT = {',', ';', ':', '.', '?', '!', '«', '»'}
PAL = re.compile(r"^[A-Za-zÀ-ÿẽũĩ'’\-]+$")


def nfc(s):
    return unicodedata.normalize('NFC', s)


def sem_acento(s, til=False):
    out = []
    for c in unicodedata.normalize('NFD', s):
        if unicodedata.combining(c):
            if til and c in '̧̃':
                out.append(c)
            continue
        out.append(c)
    return nfc(''.join(out))


def tira_acentos(s):
    """Tira agudo, grave e circunflexo; fica o til e a cedilha."""
    return sem_acento(s, til=True)


# ---------------------------------------------------------------- 1895
def partes_1895(arq):
    t = open(arq, encoding='utf-8').read()
    t = t[t.index('*PROLOGO*'):t.index('*INDEX*')]
    blocos = re.split(r'\n(?=\*(?:PROLOGO|CAPITULO [IVXL]+)\*)', t)
    out = []
    for b in blocos:
        ps = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', b) if p.strip()]
        cab = ps.pop(0)
        titulo = ''
        if ps and ps[0].startswith('_'):
            titulo = ps.pop(0).strip('_. ')
        out.append({'cab': cab, 'titulo': titulo, 'pars': ps})
    return out


TOK95 = re.compile(r"[A-Za-zÀ-ÿ]+(?:['’\-][A-Za-zÀ-ÿ]+)*")


def k16(w):
    k = sem_acento(w).lower().replace('ſ', 's')
    k = re.sub(r"[^a-z]", '', k)
    k = k.replace('f', 's').replace('h', '').replace('j', 'i').replace('y', 'i').replace('ç', 'c')
    k = re.sub(r'm(?=[^aeiou])', 'n', k)
    k = re.sub(r'(.)\1+', r'\1', k)
    k = k.replace('ph', 'f')
    return k


# ---------------------------------------------------------------- desdobrar as leituras
# (padrão, alternativas, custo da troca): o custo pesa contra as leituras menos óbvias
SUBS = [
    (re.compile(r'(?<=[a-zçãõ])[íÍlI1i]T'), ['ss'], 0),
    (re.compile(r'(?<=[a-zçãõA-Z])(?:[íÍlIi]F|fF)'), ['ff', 'ss'], 0),
    (re.compile(r'íl|íi'), ['st', 'ss'], 0),
    (re.compile(r'ít'), ['st'], 0),
    (re.compile(r'íf'), ['ss', 'ff'], 0),
    (re.compile(r'(?<![A-Za-z])í(?=[aeiouh])'), ['s'], 0),
    (re.compile(r'(?<=[a-z])í(?=[aeiou])'), ['s', 'l', 'i'], 0),
    (re.compile(r'í'), ['i', 's', 'f'], 0),
    (re.compile(r'^b(?=[aeiou])'), ['b', 'h'], 0.3),
    (re.compile(r'^I(?=h)'), ['l'], 0),
    (re.compile(r'^l(?=f[fs]|íF|fF)'), ['I'], 0),
    (re.compile(r'(?<=[a-z])I(?=[a-zR])'), ['l'], 0),
    (re.compile(r'(?<=[a-z])K(?=ei)'), ['R'], 0),
    (re.compile(r'(?<=[aeiou])l(?=[aeiou])'), ['l', 's'], 0.3),
    (re.compile(r'(?<=[aeiou])l(?=t)'), ['l', 's'], 0.3),
    (re.compile(r'(?<=[aeiou])i(?=t)'), ['i', 's'], 0.3),
    (re.compile(r'(?<=[a-z])li(?=[aeo])'), ['li', 'll'], 0.3),
    (re.compile(r'(?<=[a-z])c(?=[ei])'), ['c', 'ç'], 0),
    (re.compile(r'(?<=[a-z])c(?=[a-z])'), ['c', 'e'], 0.5),
    (re.compile(r'(?<=[a-zçãõ])c$'), ['c', 'e'], 0.3),
]


def desdobrar(r):
    """As formas que a leitura do OCR pode representar (no máximo ~64), com o custo de cada uma."""
    if not r:
        return {'': 0.0}
    r = nfc(r)
    formas = {r: 0.0}
    for rx, alts, custo in SUBS:
        novas = {}
        for f, c0 in formas.items():
            partes = rx.split(f)
            achados = rx.findall(f)
            if len(partes) == 1:
                novas[f] = min(novas.get(f, 9), c0)
                continue
            for comb in itertools.product(alts, repeat=len(partes) - 1):
                w = ''.join(x for par in itertools.zip_longest(partes, comb, fillvalue='') for x in par)
                c = c0 + custo * sum(1 for x, y in zip(achados, comb) if x != y)
                novas[w] = min(novas.get(w, 9), c)
            if len(novas) > 96:
                break
        formas = novas
    final = {}
    for f, c0 in formas.items():
        f = tira_acentos(f)
        idx = [i for i, c in enumerate(f) if c == 'f']
        combos = itertools.product('fs', repeat=len(idx)) if len(idx) <= 5 else [tuple('f' * len(idx))]
        for comb in combos:
            l = list(f)
            for i, c in zip(idx, comb):
                l[i] = c
            w = ''.join(l)
            final[w] = min(final.get(w, 9), c0)
    # o f só vem antes de vogal, r, l ou outro f; antes de outra consoante ou no fim é ſ
    boas = {x: c for x, c in final.items() if not re.search(r'f(?![aeiouyrlfAEIOUãõâêôáéíóú])', x)}
    return boas or final


def base(r):
    """A leitura com as ligaduras desfeitas pela primeira alternativa, sem trocar f por s."""
    r = nfc(r)
    for rx, alts, custo in SUBS:
        if custo == 0:
            r = rx.sub(alts[0], r)
    return tira_acentos(r)


def valida(r):
    if not r:
        return ''
    r = r.strip()
    if r in PONT or r in ('&c', '&'):
        return r
    if PAL.match(r):
        return r
    # pontuação colada ou junk
    m = re.match(r"^[A-Za-zÀ-ÿẽũĩ'’\-]+", r)
    if m and len(m.group(0)) >= 2 and not re.search(r'\d', r):
        return m.group(0)
    return ''


def sim(a, b):
    return SequenceMatcher(None, a, b).ratio()


def alvo_norm(t):
    """Palavra de 1895 na forma que se compara à de 1816."""
    return sem_acento(t).lower().replace("'", '').replace('’', '').replace('-', '')


def cmp(w):
    w = sem_acento(w).lower()
    w = w.replace('j', 'i').replace('y', 'i').replace('h', '').replace('ç', 'c').replace('z', 's')
    return re.sub(r'([^fs])\1+', r'\1', w)


TRI = collections.Counter()
BI = collections.Counter()


def treinar(formas):
    TRI.clear(); BI.clear()
    for w, n in formas.items():
        w = '^' + w + '$'
        for i in range(len(w) - 2):
            TRI[w[i:i + 3]] += n
            BI[w[i:i + 2]] += n


def logp(w):
    import math
    w = '^' + w.lower() + '$'
    return sum(math.log((TRI[w[i:i + 3]] + 0.1) / (BI[w[i:i + 2]] + 3)) for i in range(len(w) - 2))


def esqueleto_f(w):
    """A forma com f e s indistintos (o que o OCR deixa em dúvida)."""
    return w.lower().replace('s', 'f')


def escolher(leituras, alvo, freq):
    """Devolve (forma, apoio dos testemunhos, semelhança com 1895, alternativas próximas).

    O apoio se conta por grupo de formas iguais a menos de f × s (o ſ): o OCR não distingue os dois,
    e a escolha entre eles se faz depois, pela palavra de 1895 e pela frequência no resto do texto."""
    leituras = {s: valida(r) for s, r in leituras.items()}
    exp = {s: desdobrar(r) for s, r in leituras.items() if r}
    if not exp:
        return '', 0.0, 0.0, []
    grupo = lambda w: w.lower().replace('f', 's')
    apoio, formas = collections.Counter(), collections.defaultdict(set)
    for s, fs in exp.items():
        melhor = {}
        for f, c in fs.items():
            g = grupo(f)
            formas[g].add(f)
            melhor[g] = max(melhor.get(g, 0), 1 - min(c, 0.9))
        for g, v in melhor.items():
            apoio[g] += PESO[s] * v
    temç = any('ç' in r for r in leituras.values())
    lidas = {tira_acentos(r) for r in leituras.values()} | {base(r) for r in leituras.values() if r}

    def semel(f):
        return sim(cmp(f), cmp(alvo)) if alvo else 0.0

    def nota_g(g):
        return apoio[g] + (2.0 * max(semel(f) for f in formas[g]) if alvo else 0) + \
            0.2 * math.log1p(max(freq.get(f.lower(), 0) for f in formas[g]))

    def nota_f(f):
        n = semel(f) + 0.2 * math.log1p(freq.get(f.lower(), 0))
        if TRI:
            n += 0.002 * logp(f)
        if 'ç' in f and temç:
            n += 0.02
        if f in lidas:
            n += 0.01 if alvo else 0.3
        return n
    gs = sorted(apoio, key=nota_g, reverse=True)
    g = gs[0]
    escolha = max(formas[g], key=nota_f)
    # maiúscula ou minúscula: a dos testemunhos (com peso)
    cx = collections.Counter()
    for s, r in leituras.items():
        if r and r[:1].isalpha():
            cx[r[:1].isupper()] += PESO[s]
    if cx:
        mai = cx[True] > cx[False]
        escolha = (escolha[:1].upper() if mai else escolha[:1].lower()) + escolha[1:]
    s95 = semel(escolha)
    alt = [max(formas[h], key=nota_f) for h in gs[1:3] if nota_g(h) > nota_g(g) - 0.6]
    return escolha, apoio[g], s95, alt


# ---------------------------------------------------------------- pontuação
def pontuacao(le):
    vs = {s: r.strip() for s, r in le.items() if r and r.strip() in PONT | {'&c'}}
    if not vs:
        return ''
    c = collections.Counter()
    for s, r in vs.items():
        c[r] += PESO[s]
    r, n = c.most_common(1)[0]
    return r if n >= 1.0 else ''


def main(pasta):
    slots = json.load(open(os.path.join(pasta, 'slots.json'), encoding='utf-8'))
    p95 = partes_1895(os.path.join(pasta, 'pg16633.txt'))
    # partes de 1816
    partes, atual = [], None
    modo = 'corpo'
    for s in slots:
        if 'm' in s:
            m = s['m']
            if m.startswith('@@'):
                atual = {'titulo': [], 'corpo': []}
                partes.append(atual)
                modo = 'corpo'
            continue
        if atual is not None:
            atual[modo].append(s)
    assert len(partes) == len(p95) == 45, (len(partes), len(p95))
    # frequências: na primeira passada, nenhuma (as do OCR trazem o f do ſ)
    freq = collections.Counter()
    saida = duvidas = None
    for passo in (1, 2):
        saida, duvidas, decisao = rodar(partes, p95, freq)
        # dicionário f × s: para cada esqueleto, a forma escolhida com a ajuda de 1895
        freq = collections.Counter()
        for p in saida:
            for campo in ('titulo', 'corpo'):
                for x in p[campo]:
                    if x.get('op') in ('equal', 'replace') and x.get('s95', 0) >= 0.75:
                        freq[x['t'].lower()] += 1
        treinar(freq)
    json.dump(saida, open(os.path.join(pasta, 'estab.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    with open(os.path.join(pasta, 'duvidas.tsv'), 'w', encoding='utf-8') as fo:
        for d in duvidas:
            n, campo, k, f, ap, le, a = d
            fo.write(f'{n}\t{campo}\t{k}\t{f}\t{ap:.2f}\t' + '\t'.join(le[x] for x in 'ABCD') + f'\t{a}\n')
    print(len(duvidas), 'dúvidas')


def rodar(partes, p95, freq):
    saida, duvidas = [], []
    for n, (p16, p95_) in enumerate(zip(partes, p95)):
        res = {'n': n, 'titulo95': p95_['titulo'], 'pars95': p95_['pars']}
        ss = p16['corpo']                 # título e corpo juntos; separam-se pelo alinhamento com 1895
        primeira = lambda s: s.get('D') or s.get('B') or s.get('A') or s.get('C') or ''
        pal = [i for i, s in enumerate(ss) if valida(primeira(s)) not in PONT | {''}]
        rot = [valida(primeira(ss[i])) for i in pal]
        wt = TOK95.findall(p95_['titulo'])
        w95 = wt + TOK95.findall(' '.join(p95_['pars']))
        ka = [k16(x) for x in rot]
        kb = [k16(x) for x in w95]
        alvo = {}
        sm = SequenceMatcher(None, ka, kb, autojunk=False)
        for op, a0, a1, b0, b1 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and a1 - a0 == b1 - b0):
                for d in range(a1 - a0):
                    alvo[pal[a0 + d]] = (w95[b0 + d], b0 + d, op)
            elif op == 'replace':
                bloco = ' '.join(w95[b0:b1])
                for d in range(a0, a1):
                    alvo[pal[d]] = (bloco, b0, 'bloco')
            elif op == 'delete':
                for d in range(a0, a1):
                    alvo[pal[d]] = ('', b0, 'sobra')
        out = []
        for i, s in enumerate(ss):
            le = {x: s.get(x, '') for x in 'ABCD'}
            a = alvo.get(i)
            if a is None or a[2] == 'sobra':
                if not any(valida(r) and valida(r) not in PONT for r in le.values()):
                    p = pontuacao(le)
                    if p:
                        out.append({'t': p, 'p': 1, 'i95': out[-1]['i95'] if out else 0})
                    continue
            f, ap, s95, emp = escolher(le, alvo_norm(a[0]) if a and a[2] in ('equal', 'replace') else None, freq)
            if f and ((ap < 1.5 and (not a or a[2] == 'sobra')) or (ap < 1.0 and s95 < 0.8)
                      or (s.get('ins') and ap < 2.8 and s95 < 0.9)
                      or (len(f) == 1 and f not in 'eoaEOA' and s95 < 0.95) or "'" in f and len(f) <= 3):
                f = ''          # só um testemunho, sem par em 1895: sujeira (nota de rodapé, reclamo)
            if not f:
                p = pontuacao(le)
                if p:
                    out.append({'t': p, 'p': 1, 'i95': out[-1]['i95'] if out else 0})
                continue
            item = {'t': f, 'ap': round(ap, 2), 'le': le, 's95': round(s95, 2)}
            if a:
                item['a95'] = a[0]
                item['i95'] = a[1]
                item['op'] = a[2]
            else:
                item['i95'] = out[-1]['i95'] if out else 0
            if emp:
                item['emp'] = emp
            out.append(item)
        # o título: até a primeira palavra do corpo, que 1816 imprime com duas maiúsculas
        # (capitular + versal: ELRei, EM, ANdamdo); no cap. I a capitular é a vinheta («Orto»)
        corte = 0
        if n > 0:
            corpo95 = [k16(w) for w in TOK95.findall(' '.join(p95_['pars']))[:4]]
            alvo4 = ''.join(corpo95)
            pals = [k for k, x in enumerate(out) if 'p' not in x]
            melhor, mk = 0.0, None
            for j, k in enumerate(pals[:90]):
                if j < 3:
                    continue
                cand = ''.join(k16(out[q]['t']) for q in pals[j:j + 4])
                r = SequenceMatcher(None, cand, alvo4).ratio()
                if r > melhor + 0.02:
                    melhor, mk = r, k
            versal = [k for k in pals[3:90] if any(re.match(r'^[A-Z][A-Z]', r or '') and r != 'D.' and not re.match(r'^[IVXL]+[.,]?$', r)
                                                    for r in out[k]['le'].values())]
            perto = [k for k in versal if mk is not None and pals.index(mk) - 2 <= pals.index(k) <= pals.index(mk) + 1]
            corte = perto[0] if perto else (mk if mk is not None else (versal[0] if versal else 0))
        res['titulo'], res['corpo'] = out[:corte], out[corte:]
        # a primeira palavra do corpo: capitular perdida pelo OCR («Orto» → «Morto») e versal (ELRei → ElRei)
        c0 = next((x for x in res['corpo'] if 'p' not in x), None)
        if c0:
            t0 = c0['t']
            a0 = c0.get('a95', '') if c0.get('op') in ('equal', 'replace') else ''
            if a0 and len(cmp(a0)) == len(cmp(t0)) + 1 and cmp(a0).endswith(cmp(t0).lower()):
                t0 = a0[0].upper() + t0
            m = re.match(r'^([A-Z])([A-Z]+)(.*)$', t0)
            if m:
                t0 = m.group(1) + m.group(2).lower() + m.group(3)
            c0['t'] = t0
        for campo in ('titulo', 'corpo'):
            for k, x in enumerate(res[campo]):
                if 'p' in x:
                    continue
                ap, s95 = x['ap'], x['s95']
                tem95 = x.get('op') in ('equal', 'replace')
                certo = ap >= 2.8 or (ap >= 2.5 and (not tem95 or s95 >= 0.6)) or (ap >= 1.8 and s95 >= 0.8) or (ap >= 0.8 and s95 >= 0.95)
                x['certo'] = certo
                if not certo:
                    duvidas.append((n, campo, k, x['t'], ap, x['le'], x.get('a95', '')))
        saida.append(res)
    return saida, duvidas, None


if __name__ == '__main__':
    main(sys.argv[1])
