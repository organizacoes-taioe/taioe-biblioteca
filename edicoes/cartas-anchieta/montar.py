"""Cartas de Anchieta — da transcrição de 1933 (1933/<folha>.txt, conferida nas imagens) ao texto na grafia
de hoje. Adaptado da Vida de Anchieta (mesma grafia: São Bernardo + decisoes.py).

  python3 edicoes/cartas-anchieta/montar.py              # grava atual/ e relatorios/ (fora do git: relatorios)
  python3 edicoes/cartas-anchieta/montar.py --publicar   # e conteudo/jose-de-anchieta/cartas-anchieta.js

Formato de 1933/<folha>.txt: uma linha por linha impressa, «¶ » no começo de parágrafo, palavra partida no
fim da linha com hífen; só o texto de Anchieta (sem cabeço, número de página, título, sumário de 1933 e notas);
as chamadas de nota de 1933, «(89)», ficam e saem aqui; itálico entre «_».
"""
import collections
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'))
sys.path.insert(0, AQUI)
import grafia1990 as G  # noqa: E402
import decisoes as D  # noqa: E402
from edicao.grafia import esqueleto  # noqa: E402


def _lexico_ampliado():
    """O léxico da São Bernardo, refeito: o dicionário do Brasil do sistema, as palavras do texto (só os
    `texto:` das partes) das obras em prosa publicadas de Machado e Graciliano (a lista da São Bernardo lia
    também as páginas «Sobre», com grafias antigas: annos, elle) e as do dicionário português do sistema
    (Acordo de 1990, norma europeia) sem forma do mesmo esqueleto no do Brasil (entra virgindade, aquietou;
    ficam de fora facto, contacto)."""
    import glob
    from edicao.grafia import ao1990
    from edicao.tokens import TOK as TOKS, e_palavra
    lex = set()
    for w in open(G.DICIONARIO, encoding='utf-8'):
        w = nfc(w.strip())
        if w:
            lex.add(ao1990(w).lower())
    for f in glob.glob(os.path.join(RAIZ, 'conteudo', 'machado-de-assis', '*.js')) + \
            glob.glob(os.path.join(RAIZ, 'conteudo', 'graciliano-ramos', '*.js')):
        corpo = nfc(open(f, encoding='utf-8').read())
        for m in re.finditer(r'texto: `(.*?)`', corpo, re.S):
            for w in TOKS.findall(m.group(1)):
                if e_palavra(w) and '-' not in w:
                    lex.add(w.lower())
    idx = {}
    for w in lex:
        idx.setdefault(esqueleto(w), []).append(w)
    for w in open('/usr/share/dict/portuguese', encoding='utf-8'):
        w = nfc(w.strip()).lower()
        if w and w not in lex and "'" not in w:
            e = esqueleto(w)
            if e not in idx:
                lex.add(w)
                idx.setdefault(e, []).append(w)
    G._LEX, G._IDX = lex, idx


def nfc(s):
    return unicodedata.normalize('NFC', s)


_lexico_ampliado()

CLITICOS = {'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas', 'me', 'te', 'se', 'lhe', 'lhes', 'vos',
            'o', 'a', 'os', 'as', 'mo', 'ma', 'lho', 'lha'}
TOK = re.compile(r"[A-Za-zÀ-ÿºª0-9]+(?:['’\-][A-Za-zÀ-ÿºª0-9]+)*\.?|\.\.\.|[^\sA-Za-zÀ-ÿ0-9]")
import pecas  # noqa: E402


def nfc(s):
    return unicodedata.normalize('NFC', s)


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


# ------------------------------------------------------------------ leitura da transcrição de 1897

def linhas_peca(peca):
    """(folha, linha, texto) de uma peça."""
    out = []
    for f in pecas.folhas_de(peca):
        for k, l in enumerate(open(os.path.join(AQUI, '1933', f'{f}.txt'), encoding='utf-8').read().splitlines(), 1):
            if l.strip():
                out.append((f, k, nfc(l.rstrip())))
    return hifens_perdidos(out)


def hifens_perdidos(out):
    """A leitura às vezes perde o hífen do fim da linha («al» / «deia»): junta as duas metades quando juntas
    fazem palavra e uma delas, sozinha, não faz."""
    import lexico
    lex, lexsa, _ = lexico._carregar()

    def perto(w):
        novo, fonte = G.atual(w.lower())
        return fonte == 'lexico' or fonte == 'esqueleto' and lexico.sem_acento(novo) == lexico.sem_acento(w)

    def boa(w):
        lw = w.lower()
        return lw in lex or lw in lexico.ANTIGAS or lexico.sem_acento(lw) in lexsa
    for i in range(len(out) - 1):                 # palavra inteira numa linha e o seu fim repetido na seguinte
        a = re.search(r'([A-Za-zÀ-ÿ]+)[,.;:]?$', out[i][2])
        b = re.match(r'^((?:¶ )?)([a-zà-ÿ]+)([,.;:]?) ', out[i + 1][2])
        if a and b and len(a.group(1)) >= len(b.group(2)) + 2 and a.group(1).lower().endswith(b.group(2)) \
                and (b.group(2) not in lex or b.group(2) == 'mente'):
            f, k, l = out[i + 1]
            out[i + 1] = (f, k, b.group(1) + l[b.end():])
    for i in range(len(out) - 1):
        f, k, l = out[i]
        a = re.search(r'([A-Za-zÀ-ÿ]+)$', l)
        b = re.match(r'^(?:¶ )?([a-zà-ÿ]+)', out[i + 1][2])
        if not a or not b or out[i + 1][2].startswith('¶ '):
            continue
        a, b = a.group(1), b.group(1)
        ab = a + b
        if (not boa(a) and not boa(b)) or ((not boa(a) or not boa(b)) and (boa(ab) or perto(ab))):
            out[i] = (f, k, l + '-')
    return out


NOTA = re.compile(r' ?\((\d{1,3}(?:[-:]\d{1,2})?)\)')


def palavras_conhecidas(linhas):
    return {sem_acento(w).lower() for _, _, l in linhas for w in re.findall(r'[A-Za-zÀ-ÿ]+', l)}


def juntar(linhas):
    """Blocos: ('titulo', nivel, texto, onde) e ('par', texto, onde). Desfaz a hifenização do fim da linha."""
    conhecidas = palavras_conhecidas(linhas)
    lex = G.lexico()
    blocos = []
    atual = None
    for p, k, l in linhas:
        m = re.match(r'^(#{1,3}) (.*)$', l)
        if m:
            atual = None
            blocos.append(['titulo', len(m.group(1)), m.group(2).strip(), (p, k)])
            continue
        if l.startswith('> '):
            l = l[2:]
            if atual is None or atual[0] != 'pre':
                atual = ['pre', '', (p, k)]
                blocos.append(atual)
        elif l.startswith('¶ ') or atual is None or atual[0] != 'par':
            l = l[2:] if l.startswith('¶ ') else l
            atual = ['par', '', (p, k)]
            blocos.append(atual)
        t = atual[1]
        if t.endswith('-'):
            ant = re.search(r'([A-Za-zÀ-ÿ]+)-$', t)
            seg = re.match(r'([A-Za-zÀ-ÿ]+)', l)
            a = ant.group(1) if ant else ''
            b = seg.group(1) if seg else ''
            hifen = b.lower() in CLITICOS and (sem_acento(a).lower() in conhecidas and a.lower() in lex or
                                               a.lower() in D.HIFEN_ANTES) and (a + b).lower() not in D.JUNTAR
            if (a + '-' + b).lower() in D.JUNTAR:
                hifen = False
            atual[1] = t + l if hifen else t[:-1] + l
        else:
            atual[1] = (t + ' ' + l) if t else l
    return blocos


# ------------------------------------------------------------------ grafia

def tokens(s):
    return TOK.findall(s)


def ambiguo(w):
    """Formas do léxico com a mesma chave sem acento: {pratica, prática}."""
    lex = G.lexico()
    lw = w.lower()
    if lw != sem_acento(lw):
        return None
    idx = _idx_acentos()
    formas = idx.get(lw, set())
    if lw in formas and len(formas) > 1:
        return sorted(formas)
    return None


_IA = None


def _idx_acentos():
    global _IA
    if _IA is None:
        _IA = collections.defaultdict(set)
        for w in G.lexico():
            _IA[sem_acento(w)].add(w)
    return _IA


def enclise(t):
    """copial-o → copiá-lo, fazel-o → fazê-lo, reduzil-os → reduzi-los (a forma de 1897 com «l-»)."""
    m = re.match(r'^(.*?)([aeiouô])l-(o|a|os|as)$', t)
    if not m:
        return None
    base, v, pron = m.groups()
    nv = {'a': 'á', 'e': 'ê', 'i': 'i', 'o': 'ô', 'ô': 'ô', 'u': 'u'}[v]
    return G.atual(base + v + 'r')[0][:-2] + nv + '-l' + pron


def modernizar_bloco(texto, onde, rel):
    guardados = []

    def guardar(m):
        guardados.append(m.group(0))
        return f'LATIMXX{len(guardados) - 1}XX'
    for frase in D.LATIM:
        texto = re.sub(r'(?<![A-Za-zÀ-ÿ])' + re.escape(frase) + r'(?![A-Za-zÀ-ÿ])', guardar, texto)
    texto = re.sub(r'_[^_]+_', guardar, texto)          # o que já está em itálico (espanhol)
    out = []
    toks = tokens(texto)
    for i, t in enumerate(toks):
        if not re.match(r'[A-Za-zÀ-ÿ]', t) or t.startswith('LATIMXX'):
            out.append(t)
            continue
        ponto = ''
        if t.endswith('.') and t[:-1].lower() not in D.ABREVIATURAS:
            t, ponto = t[:-1], '.'
        ant = toks[i - 1] if i else ''
        seg = toks[i + 1] if i + 1 < len(toks) else ''
        chave_ctx = f'{t}|{seg.rstrip(".")}'
        lw = t.lower()
        if chave_ctx in D.CONTEXTO:
            novo, fonte = D.CONTEXTO[chave_ctx], 'contexto'
        elif t in D.MANUAL_EXATO:
            novo, fonte = D.MANUAL_EXATO[t], 'manual'
        elif lw in D.MANUAL:
            novo, fonte = G.igualar_caixa(t, D.MANUAL[lw]), 'manual'
        elif lw in ('á', 'ás', 'áquele', 'áquela', 'áqueles', 'áquelas', 'áquilo'):
            novo, fonte = D.crase(t, seg, ant), 'crase'
            rel['crase'].append((onde, ant, t, seg, novo))
        elif enclise(lw):
            novo, fonte = G.igualar_caixa(t, enclise(lw)), 'enclise'
            rel['enclise'][(t, novo)] += 1
        else:
            amb = ambiguo(t)
            if amb:
                novo = D.desambiguar(t, ant, seg, amb)
                fonte = 'ambiguo'
                rel['ambiguos'][(lw, '|'.join(amb), novo.lower())].append(f'{ant} {t} {seg}')
                novo = G.igualar_caixa(t, novo)
            else:
                t0 = t
                if re.search(r'[áéíó](ra|ras|ram)$', lw) and len(re.findall(r'[áéíóúâêôãõ]', lw)) == 1:
                    t0 = re.sub(r'[áéíó](?=(ra|ras|ram|ramos)$)', lambda m: G.CAIDOS[m.group(0)], t)   # fallára, obrára: mais-que-perfeito
                novo, fonte = G.atual(t0)
                if t0 != t:                     # o esqueleto pode dar o futuro (quebrantará): fica o mais-que-perfeito
                    novo = re.sub(r'[áéíó](?=(ra|ras|ram)$)', lambda m: G.CAIDOS[m.group(0)], novo)
                    if sem_acento(novo).lower() == sem_acento(t0).lower():
                        novo = G.igualar_caixa(t0, t0.lower())
                novo = G.composto(novo)
        if fonte in ('SEM_PAR', 'esqueleto'):
            rel[fonte][(t, novo)] += 1
        elif novo.lower() == t.lower() and re.search(r'([bcdfglmnprt])\1|ph|th|y|ae$|aes$|eo$|eos$|^h[aeiou]|sc[ei]|ct|pt|mn|z$|oe$|ue$', t.lower()):
            rel['suspeitas'][t] += 1
        out.append(novo + ponto)
    s = ' '.join(out)
    s = re.sub(r' ([,.;:!?)])', r'\1', s)
    s = re.sub(r'\( ', '(', s)
    s = re.sub(r'(\d)\. (\d{3})', r'\1.\2', s)
    s = re.sub(r'_ (.*?) _', r'_\1_', s)
    for k in reversed(range(len(guardados))):
        g = guardados[k]
        s = s.replace(f'LATIMXX{k}XX', g if g.startswith('_') or '_LATIMXX' in s else '_' + g + '_')
    return s


def preparar(texto, onde, peca, rel):
    """As decisões sobre o texto de 1933, antes da grafia: chamadas de nota, erros, emendas."""
    texto = NOTA.sub('', texto)
    texto = D.italicos(texto)
    for p, de, para, _ in D.ERROS:
        if p == peca and de in texto:
            texto = texto.replace(de, para, 1); rel['usadas'].add(('erro', p, de))
    for p, de, para in D.COMPOSICAO + D.EMENDAS:
        if p == peca and de in texto:
            texto = texto.replace(de, para, 1); rel['usadas'].add(('comp', p, de))
    for rx, sub in D.PRE:
        texto = re.sub(rx, sub, texto)
    return texto


def modernizado():
    rel = {'SEM_PAR': collections.Counter(), 'esqueleto': collections.Counter(), 'crase': [],
           'ambiguos': collections.defaultdict(list), 'enclise': collections.Counter(), 'usadas': set(), 'suspeitas': collections.Counter()}
    pecas_m = []
    for p in pecas.PECAS:
        blocos = juntar(linhas_peca(p))
        pars = []
        for b in blocos:
            if b[0] == 'titulo':
                pars.append('## ' + modernizar_bloco(b[2], b[3], rel))
                continue
            texto, onde = b[1], b[2]
            pars.append(D.depois(modernizar_bloco(preparar(texto, onde, p[0], rel), onde, rel)))
        pecas_m.append({'n': p[0], 'titulo': p[4], 'lingua': p[3], 'pars': pars,
                        'pars_1933': [preparar(b[1], b[2], p[0], {'usadas': set()}) for b in blocos if b[0] != 'titulo']})
    return pecas_m, rel


def relatorios(rel):
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    with open(os.path.join(AQUI, 'relatorios', 'sem_par.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['SEM_PAR'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'esqueleto.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['esqueleto'].items()):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'ambiguos.tsv'), 'w', encoding='utf-8') as f:
        for (lw, fs, esc), ctx in sorted(rel['ambiguos'].items()):
            f.write(f'{lw}\t{fs}\t{esc}\t{len(ctx)}\t{" / ".join(ctx[:4])}\n')
    with open(os.path.join(AQUI, 'relatorios', 'crase.tsv'), 'w', encoding='utf-8') as f:
        for x in rel['crase']:
            f.write('\t'.join(map(str, x)) + '\n')
    with open(os.path.join(AQUI, 'relatorios', 'suspeitas.tsv'), 'w', encoding='utf-8') as f:
        for a, n in sorted(rel['suspeitas'].items()):
            f.write(f'{a}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'enclise.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['enclise'].items()):
            f.write(f'{a}\t{b}\t{n}\n')


def gravar_atual(pecas_m):
    os.makedirs(os.path.join(AQUI, 'atual'), exist_ok=True)
    for p in pecas_m:
        corpo = f'## {p["n"]}. {p["titulo"]}\n\n' + '\n\n'.join(p['pars'])
        open(os.path.join(AQUI, 'atual', f'{p["n"]}.txt'), 'w', encoding='utf-8').write(corpo + '\n')


if __name__ == '__main__':
    partes, rel = modernizado()
    relatorios(rel)
    faltam = [x for x in [('erro', a, b) for a, b, _, _ in D.ERROS] +
              [('comp', a, b) for a, b, _ in D.COMPOSICAO + D.EMENDAS] if x not in rel['usadas']]
    if faltam:
        print('NÃO APLICADAS:', faltam)
    gravar_atual(partes)
    print('sem par:', sum(rel['SEM_PAR'].values()), len(rel['SEM_PAR']), '| esqueleto:', len(rel['esqueleto']),
          '| ambíguos:', len(rel['ambiguos']), '| crase:', len(rel['crase']))
    if '--publicar' in sys.argv:
        import publicar
        publicar.gravar(partes)
