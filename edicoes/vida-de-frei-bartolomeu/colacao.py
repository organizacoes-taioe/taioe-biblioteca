"""Vida de D. Frei Bertolameu dos Mártires — colação dos testemunhos sobre o de referência (1619, BNP).

  python3 -I edicoes/vida-de-frei-bartolomeu/colacao.py     # grava PASTA/colacao/*.json

Alinhamento: âncoras (quadrigramas de chaves únicos nos dois testemunhos), maior subsequência crescente
das âncoras e, entre âncoras vizinhas, difflib. A chave da palavra é o esqueleto ortográfico
(ferramentas/edicao/grafia.esqueleto) com as trocas típicas do OCR de 1619: ſ/f → s, v → u, j → i.
Blocos de tamanhos diferentes se juntam quando a soma das chaves é a mesma («alemdas» = «alem das»).
"""
import bisect
import difflib
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao.grafia import esqueleto  # noqa: E402
import testemunhos as T  # noqa: E402

ABREV = {'q': 'que', 'q̃': 'que', 'qͥ': 'que', 'cõ': 'com', 'cô': 'com', 'có': 'com', 'cŏ': 'com', 'ẽ': 'em',
         'hũa': 'hua', 'hũ': 'hum', 'ñ': 'não', 'nã': 'não', 'porq': 'porque', 'porq̃': 'porque'}


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def chave(t):
    t = t.lower().replace('ſ', 's')
    t = ABREV.get(t.strip('.,;:!?()'), t)
    t = re.sub(r'[^a-zà-ÿç&]', '', t)
    if t == '&':
        return '&'
    t = sem_acento(t).replace('f', 's').replace('v', 'u').replace('j', 'i')
    t = re.sub(r'[^a-zç]', '', t)
    if not t:
        return ''
    return esqueleto(t)


def ancoras(ka, kb, n=4):
    def grams(k):
        d = {}
        for i in range(len(k) - n + 1):
            g = tuple(k[i:i + n])
            if '' in g:
                continue
            d.setdefault(g, []).append(i)
        return d
    ga, gb = grams(ka), grams(kb)
    pares = sorted((pa[0], gb[g][0]) for g, pa in ga.items() if len(pa) == 1 and len(gb.get(g, ())) == 1)
    # maior subsequência crescente em j
    tails, idx, prev = [], [], [None] * len(pares)
    for k, (i, j) in enumerate(pares):
        p = bisect.bisect_left(tails, j)
        if p == len(tails):
            tails.append(j)
            idx.append(k)
        else:
            tails[p] = j
            idx[p] = k
        prev[k] = idx[p - 1] if p else None
    lis = []
    k = idx[-1] if idx else None
    while k is not None:
        lis.append(pares[k])
        k = prev[k]
    lis.reverse()
    # cada âncora vale n pares (i+d, j+d), sem cruzar
    out = []
    for i, j in lis:
        for d in range(n):
            if not out or (i + d > out[-1][0] and j + d > out[-1][1]):
                out.append((i + d, j + d))
    return out


def alinhar(ka, kb):
    """Lista de blocos (i0, i1, j0, j1, tipo): tipo 'eq' (1:1, mesma chave), 'sub' (1:1, chaves diferentes),
    'grp' (n:m de mesma soma de chaves), 'del' (só em A), 'ins' (só em B)."""
    anc = ancoras(ka, kb)
    blocos = []
    pi, pj = 0, 0
    for (i, j) in anc + [(len(ka), len(kb))]:
        if i > pi or j > pj:
            blocos += _miudo(ka, kb, pi, i, pj, j)
        if i < len(ka):
            blocos.append((i, i + 1, j, j + 1, 'eq'))
        pi, pj = i + 1, j + 1
    return blocos


def _miudo(ka, kb, a0, a1, b0, b1):
    if a1 - a0 > 4000 or b1 - b0 > 4000:
        # trecho grande sem âncora (páginas que faltam num dos testemunhos)
        if a1 - a0 > 3 * (b1 - b0) or b1 - b0 > 3 * (a1 - a0):
            out = []
            if a1 > a0:
                out.append((a0, a1, b0, b0, 'del'))
            if b1 > b0:
                out.append((a1, a1, b0, b1, 'ins'))
            return out
    sa, sb = ka[a0:a1], kb[b0:b1]
    out = []
    for op, i0, i1, j0, j1 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
        i0, i1, j0, j1 = i0 + a0, i1 + a0, j0 + b0, j1 + b0
        if op == 'equal':
            out += [(i0 + d, i0 + d + 1, j0 + d, j0 + d + 1, 'eq') for d in range(i1 - i0)]
        elif op == 'delete':
            out.append((i0, i1, j0, j0, 'del'))
        elif op == 'insert':
            out.append((i0, i0, j0, j1, 'ins'))
        else:
            out += _substituicao(ka, kb, i0, i1, j0, j1)
    return out


def _substituicao(ka, kb, i0, i1, j0, j1):
    """Bloco trocado: junta grupos de mesma soma de chaves; o resto pareia em ordem."""
    out = []
    i, j = i0, j0
    while i < i1 and j < j1:
        achou = False
        for n in range(1, min(4, i1 - i) + 1):
            for m in range(1, min(4, j1 - j) + 1):
                if (n, m) != (1, 1) and ''.join(ka[i:i + n]) == ''.join(kb[j:j + m]) and ''.join(ka[i:i + n]):
                    out.append((i, i + n, j, j + m, 'grp'))
                    i, j = i + n, j + m
                    achou = True
                    break
            if achou:
                break
        if achou:
            continue
        # 1:1, ou palavra a mais de um lado se a seguinte casa melhor
        if j + 1 < j1 and ka[i] == kb[j + 1]:
            out.append((i, i, j, j + 1, 'ins'))
            j += 1
        elif i + 1 < i1 and ka[i + 1] == kb[j]:
            out.append((i, i + 1, j, j, 'del'))
            i += 1
        else:
            out.append((i, i + 1, j, j + 1, 'sub'))
            i, j = i + 1, j + 1
    if i < i1:
        out.append((i, i1, j, j, 'del'))
    if j < j1:
        out.append((i1, i1, j, j1, 'ins'))
    return out


# ------------------------------------------------------------------ testemunhos

TESTEMUNHOS = {
    # nome: (lista de (fonte, de, até)) — as fontes de dois tomos se encadeiam
    'bnp': [('bnp1619', None, None)],
    'ia': [('ia1619', None, None)],
    'ga': [('ga1619', None, None)],
    'r185': [('r1850v1', None, None), ('r1853v2', None, None)],
    'gr185': [('gr1850v1', None, None), ('gr1853v2', None, None)],
    'r1818': [('r1818v1', None, None)],
    'gr1818': [('gr1818v1', None, None)],
}


def carregar(nome):
    seq, notas = [], []
    for fonte, de, ate in TESTEMUNHOS[nome]:
        try:
            s, n = T.sequencia(fonte, de, ate)
        except FileNotFoundError:
            print('falta', fonte, file=sys.stderr)
            continue
        for w in s + n:
            w['f'] = fonte
        seq += s
        notas += n
    return seq, notas


def main():
    dest = os.path.join(T.PASTA, 'colacao')
    os.makedirs(dest, exist_ok=True)
    ref, notas_ref = carregar('bnp')
    ka = [chave(w['t']) for w in ref]
    json.dump({'palavras': ref, 'notas': notas_ref}, open(os.path.join(dest, 'bnp.json'), 'w'), ensure_ascii=False)
    for nome in sys.argv[1:] or [k for k in TESTEMUNHOS if k != 'bnp']:
        seq, notas = carregar(nome)
        if not seq:
            continue
        kb = [chave(w['t']) for w in seq]
        bl = alinhar(ka, kb)
        n_eq = sum(1 for b in bl if b[4] == 'eq')
        print(nome, len(seq), 'palavras;', n_eq, 'iguais', f'({n_eq / max(1, len(ref)):.1%} da referência)')
        json.dump({'palavras': [{'t': w['t'], 'p': w['p'], 'c': w.get('c', ''), 'f': w['f'], 'nl': w.get('nl', False),
                                 'rec': round(w.get('rec', 0), 2)} for w in seq],
                   'notas': [{'t': w['t'], 'p': w['p'], 'f': w['f'], 'nl': w.get('nl', False)} for w in notas],
                   'blocos': bl}, open(os.path.join(dest, nome + '.json'), 'w'), ensure_ascii=False)


if __name__ == '__main__':
    main()
