"""Vida de D. Frei Bertolameu dos Mártires — grafia de hoje (Acordo de 1990, forma brasileira), palavra por
palavra, sem trocar palavra (o método da _Vida de Anchieta_, edicoes/vida-de-anchieta/montar.py).

Léxico: o dicionário do Brasil do sistema, as palavras dos textos publicados de Machado e Graciliano e as do
dicionário português do sistema sem forma do mesmo esqueleto no do Brasil (sao-bernardo/grafia1990.py).
Para cada palavra: decisões à mão (decisoes.MANUAL), crase, ênclise antiga, ambíguas pelo contexto e, por
fim, a forma do léxico de mesmo esqueleto (grafia1990.atual). Relatórios: PASTA/relatorios/grafia-*.tsv.
"""
import collections
import glob
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, AQUI)
import grafia1990 as G  # noqa: E402
import decisoes as D  # noqa: E402
from edicao.grafia import esqueleto, ao1990  # noqa: E402
from edicao.tokens import TOK as TOKS, e_palavra  # noqa: E402


def nfc(s):
    return unicodedata.normalize('NFC', s)


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def _lexico_ampliado():
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
    lex |= set(D.LEXICO_EXTRA)
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


_lexico_ampliado()

TOK = re.compile(r"[A-Za-zÀ-ÿºª0-9]+(?:['’\-][A-Za-zÀ-ÿºª0-9]+)*\.?|\.\.\.|[^\sA-Za-zÀ-ÿ0-9]")
_IA = None


def _idx_acentos():
    global _IA
    if _IA is None:
        _IA = collections.defaultdict(set)
        for w in G.lexico():
            _IA[sem_acento(w)].add(w)
    return _IA


def ambiguo(w):
    lw = w.lower()
    if lw != sem_acento(lw):
        return None
    formas = _idx_acentos().get(lw, set())
    if lw in formas and len(formas) > 1:
        return sorted(formas)
    return None


def enclise_antiga(t):
    """1619 junta o pronome ao verbo sem hífen (fezlhes, dandonos, levantarse): separa pelo léxico."""
    lw = t.lower()
    for pron in D.PRONOMES_JUNTOS:
        if lw.endswith(pron) and len(lw) > len(pron) + 2:
            base = lw[:-len(pron)]
            if D.verbo_valido(base, pron):
                return base, pron
    return None


REL = {'SEM_PAR': collections.Counter(), 'esqueleto': collections.Counter(), 'regra': collections.Counter(), 'ambiguos': collections.defaultdict(list),
       'enclise': collections.Counter(), 'manual': collections.Counter()}


def uma(t, ant, seg):
    """Forma de hoje de uma palavra (sem pontuação) no contexto."""
    lw = t.lower()
    if f'{lw}|{seg.lower()}' in D.CONTEXTO:
        return G.igualar_caixa(t, D.CONTEXTO[f'{lw}|{seg.lower()}'])
    if t in D.MANUAL_EXATO:
        return D.MANUAL_EXATO[t]
    if lw in D.MANUAL:
        REL['manual'][lw] += 1
        return G.igualar_caixa(t, D.MANUAL[lw])
    if lw in D.LATIM_PALAVRAS:
        return t
    enc = enclise_antiga(t)
    if enc:
        base, pron = enc
        nb = uma(base, ant, pron)
        np_ = D.PRONOME_FORMA.get(pron, pron)
        nb = D.antes_de_clitico(nb, np_)
        REL['enclise'][(t, nb + '-' + np_)] += 1
        return nb + '-' + np_
    amb = ambiguo(t)
    if amb:
        novo = D.desambiguar(lw, ant.lower(), seg.lower(), amb)
        REL['ambiguos'][(lw, '|'.join(amb), novo)].append(f'{ant} {t} {seg}')
        return G.igualar_caixa(t, novo)
    t0 = t
    if re.search(r'[áéíó](ra|ras|ram)$', lw) and len(re.findall(r'[áéíóúâêôãõ]', lw)) == 1:
        t0 = re.sub(r'[áéíó](?=(ra|ras|ram|ramos)$)', lambda m: G.CAIDOS[m.group(0)], t)   # obrára: mais-que-perfeito
    novo, fonte = G.atual(t0)
    if fonte == 'SEM_PAR':
        n2 = regras(t0.lower())
        if n2:
            novo, fonte = G.igualar_caixa(t0, n2), 'regra'
            REL['regra'][(t, novo)] += 1
    novo = G.composto(novo)
    if fonte in ('SEM_PAR', 'esqueleto'):
        REL[fonte][(t, novo)] += 1
    return novo


def _no_lexico(w):
    lex = G.lexico()
    for v in G._variantes(w):
        a = ao1990(v)
        if a in lex:
            return a
    return None


def regras(lw):
    """Grafias antigas regulares que o esqueleto não resolve: -ão átono dos verbos (erão → eram), -eo/-io do
    pretérito (respondeo → respondeu, vio → viu), h inicial (avendo → havendo, hir → ir), e, por fim, a forma
    do léxico de mesmo esqueleto mesmo com vogal diferente (sintia → sentia, minino → menino), conferida no
    relatório grafia-regra.tsv."""
    cands = []
    if lw.endswith('ão'):
        cands.append(lw[:-2] + 'am')
    if lw.endswith('ões') is False and re.search(r'eo$', lw):
        cands.append(lw[:-2] + 'eu')
    if re.search(r'io$', lw):
        cands.append(lw[:-2] + 'iu')
    if lw.startswith('h'):
        cands.append(lw[1:])
    elif re.match(r'[aeiouáéíóú]', lw):
        cands.append('h' + lw)
    for c in list(cands):
        if c.endswith('ão'):
            cands.append(c[:-2] + 'am')
    for c in cands:
        a = _no_lexico(c)
        if a:
            return a
    from difflib import SequenceMatcher
    if len(lw) >= 4:
        for c in [lw] + cands:
            ops = G._IDX.get(esqueleto(c), [])
            if ops:
                o = max(ops, key=lambda o: (SequenceMatcher(None, c, o).ratio(), o))
                if SequenceMatcher(None, c, o).ratio() >= 0.8:
                    return o
    return None


def modernizar(texto):
    """Um parágrafo (texto de 1619 já estabelecido, na grafia das edições de Lisboa) → grafia de hoje.
    Respeita _itálico_ (latim: sem mudança) e as marcas {…}."""
    guardados = []

    def guardar(m):
        guardados.append(m.group(0))
        return f'QQGUARDA{len(guardados) - 1}QQ'
    texto = re.sub(r'\{[^}]*\}', guardar, texto)
    texto = re.sub(r'_[^_]+_', guardar, texto)
    for rx, sub in D.PRE:
        texto = re.sub(rx, sub, texto)
    toks = TOK.findall(texto)
    out = []
    for i, t in enumerate(toks):
        if not re.match(r'[A-Za-zÀ-ÿ]', t) or t.startswith('QQGUARDA'):
            out.append(t)
            continue
        ponto = ''
        if t.endswith('.') and t[:-1].lower() not in D.ABREVIATURAS:
            t, ponto = t[:-1], '.'
        ant = next((x for x in reversed(toks[:i]) if re.match(r'[A-Za-zÀ-ÿ]', x)), '')
        seg = toks[i + 1] if i + 1 < len(toks) else ''
        if '-' in t and not re.match(r'(?i)^(d|el|ante|sub|vice|sem|bem|mal)-', t):
            partes = t.split('-')
            novo = '-'.join(uma(p, ant, partes[k + 1] if k + 1 < len(partes) else seg) if k == 0 or p.lower() not in D.CLITICOS
                            else p.lower() for k, p in enumerate(partes))
        else:
            novo = uma(t, ant, seg.rstrip('.'))
        out.append(novo + ponto)
    s = ' '.join(out)
    s = re.sub(r' ([,.;:!?)])', r'\1', s)
    s = re.sub(r'\( ', '(', s)
    s = re.sub(r'QQGUARDA(\d+)QQ', lambda m: guardados[int(m.group(1))], s)
    for rx, sub in D.DEPOIS:
        s = re.sub(rx, sub, s)
    return s


def relatorios(pasta):
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, 'grafia-sem_par.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(REL['SEM_PAR'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(pasta, 'grafia-esqueleto.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(REL['esqueleto'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(pasta, 'grafia-regra.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(REL['regra'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(pasta, 'grafia-ambiguos.tsv'), 'w', encoding='utf-8') as f:
        for (lw, fs, esc), ctx in sorted(REL['ambiguos'].items(), key=lambda x: -len(x[1])):
            f.write(f'{lw}\t{fs}\t{esc}\t{len(ctx)}\t{" / ".join(ctx[:4])}\n')
    with open(os.path.join(pasta, 'grafia-enclise.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(REL['enclise'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
