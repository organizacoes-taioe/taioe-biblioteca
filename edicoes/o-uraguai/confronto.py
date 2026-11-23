"""Confronto dos versos: o texto moderno do Wikisource (WS-mod, grafia de hoje, 1380 versos) como esqueleto;
para cada palavra, as leituras de 1769: WS1769 (só páginas revisadas), camada OCR de Boston (AB), Tesseract de
Boston (TB), camada OCR de Toronto (AT), Tesseract de Toronto (TT). Grava confronto.json."""
import json, os, re, sys, difflib, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
import linhas as LN
TOK = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*|⟦\d+⟧|[^\s\w]|\d+")
def L(w):
    w = w.lower().replace('ç', 's').replace('ſ', 's')
    w = sem_acento(w)
    pecas = []
    for w in w.split('-'):
        w = w.replace('ph', 'f').replace('th', 't').replace('y', 'i').replace('z', 's').replace('f', 's')
        w = w.replace('h', '')
        w = re.sub(r'[^a-z]', '', w)
        w = re.sub(r'(.)\1', r'\1', w)
        w = re.sub(r'mp(?=t)', 'n', w); w = re.sub(r'[cp](?=t)', '', w); w = re.sub(r'm(?=[^aeiou]|$)', 'n', w)
        w = re.sub(r'c(?=[ei])', 's', w); w = re.sub(r'(.)\1', r'\1', w)
        w = re.sub(r'aos?$', 'an', w); w = re.sub(r'an$', 'an', w)
        w = re.sub(r'eos$', 'eus', w); w = re.sub(r'eo$', 'eu', w); w = re.sub(r'io$', 'iu', w); w = re.sub(r'ae(s?)$', r'ai\1', w); w = re.sub(r'oes$', 'ois', w)
        w = re.sub(r'oe(s?)$', r'oi\1', w)
        pecas.append(w)
    return ''.join(pecas)
JUNTAR = [('em', 'tanto'), ('em', 'fim'), ('em', 'quanto'), ('entre', 'tanto'), ('de', 'balde')]
PONT = set(',.;:!?')
def norm_pont(t):
    return {'5': ',', '>': ',', '»': ',', '‚': ',', '·': '.', '¡': '!', ';': ';'}.get(t, t)
def toks_ocr(s):
    s = s.replace('’', "'")
    out = []
    for t in TOK.findall(s):
        if re.match(r'[^\W\d_]', t): out.append(('w', t))
        else:
            t = norm_pont(t)
            if t in PONT: out.append(('p', t))
    i = 0; res = []
    while i < len(out):
        if i + 1 < len(out) and out[i][0] == 'w' and out[i + 1][0] == 'w' and (out[i][1].lower(), out[i + 1][1].lower()) in JUNTAR:
            res.append(('w', out[i][1] + out[i + 1][1])); i += 2; continue
        res.append(out[i]); i += 1
    return res
def leitura(mod_ws, ocr_t):
    """mod_ws: palavras modernas; ocr_t: tokens da linha OCR. -> por palavra moderna: (palavra lida, pontuação seguinte)"""
    ow = [i for i, t in enumerate(ocr_t) if t[0] == 'w']
    A = [L(w) for w in mod_ws]; B = [L(ocr_t[i][1]) for i in ow]
    res = [None] * len(mod_ws)
    def pont(k):  # pontuação depois da palavra ocr k
        i = ow[k]; p = ''
        j = i + 1
        while j < len(ocr_t) and ocr_t[j][0] == 'p': p += ocr_t[j][1]; j += 1
        return p
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
        if op == 'equal' or (op == 'replace' and a2 - a1 == b2 - b1):
            for k in range(a2 - a1): res[a1 + k] = (ocr_t[ow[b1 + k]][1], pont(b1 + k))
        elif op == 'replace':
            # emparelha pela semelhança
            usados = set()
            for k in range(a1, a2):
                best, bj = 0, None
                for j in range(b1, b2):
                    if j in usados: continue
                    r = difflib.SequenceMatcher(None, A[k], B[j]).ratio()
                    if r > best: best, bj = r, j
                if bj is not None and best >= 0.5:
                    usados.add(bj); res[k] = (ocr_t[ow[bj]][1], pont(bj))
                else:
                    res[k] = ('∅' + ' '.join(ocr_t[ow[j]][1] for j in range(b1, b2) if j not in usados), '')
        elif op == 'delete':
            for k in range(a1, a2): res[k] = ('∅', '')
        # insert: palavras a mais no OCR -> anexadas à anterior
        if op in ('insert', 'replace') and b2 - b1 > a2 - a1 and a1 > 0 and res[a1 - 1] and op == 'insert':
            res[a1 - 1] = (res[a1 - 1][0] + ' +' + ' '.join(ocr_t[ow[j]][1] for j in range(b1, b2)), res[a1 - 1][1])
    return res
def casar(versos, linhas_ocr):
    """versos (texto moderno) -> índice da linha OCR, em ordem (programação dinâmica simples)."""
    K = [L(v.replace(' ', '|')) for v in versos]
    def kk(s): return ''.join(L(w) for w in re.findall(r"[^\W\d_]+", s))
    Kv = [''.join(L(w) for w in re.findall(r"[^\W\d_]+", v)) for v in versos]
    Ko = [kk(l[2]) for l in linhas_ocr]
    n, m = len(versos), len(linhas_ocr)
    S = [[difflib.SequenceMatcher(None, Kv[i], Ko[j], autojunk=False).ratio() for j in range(m)] for i in range(n)]
    # DP monótono
    best = [[(-1e9, None)] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1): best[0][j] = (0, None)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cand = [(best[i][j - 1][0], (i, j - 1, None)), (best[i - 1][j - 1][0] + (S[i - 1][j - 1] if S[i - 1][j - 1] > 0.45 else -1), (i - 1, j - 1, j - 1)),
                    (best[i - 1][j][0] - 1, (i - 1, j, None))]
            best[i][j] = max(cand, key=lambda x: x[0])
    res = [None] * n
    i, j = n, m
    while i > 0 and j >= 0:
        sc, prev = best[i][j]
        if prev is None: break
        pi, pj, lin = prev
        if lin is not None and pi == i - 1: res[i - 1] = (lin, S[i - 1][lin])
        i, j = pi, pj
    return res
def tor_pag(p):
    return MAPA_TOR.get(p)
MAPA_TOR = {}
def main():
    mod = wsmod()
    v69 = versos1769()
    ws = {p['pag']: p for p in ws1769()}
    tor = D + 'tor/ouraguaypoema00gama.pdf'
    bos = D + 'bos/ouruaguaypoema00gama.pdf'
    global MAPA_TOR
    MAPA_TOR = json.load(open(D + 'mapa_tor.json')) if os.path.exists(D + 'mapa_tor.json') else {}
    MAPA_TOR = {int(k): v for k, v in MAPA_TOR.items()}
    saida = []
    for c in CANTOS:
        v = [x for x in v69[c] if not re.match(r'^Fim do', x[2])]
        assert len(v) == len(mod[c]), (c, len(v), len(mod[c]))
        porpag = {}
        for i, (pag, nivel, t) in enumerate(v): porpag.setdefault(pag, []).append(i)
        for pag, idx in porpag.items():
            nivel = ws[pag]['nivel']
            fontes = {'AB': LN.pdf(bos, pag), 'TB': LN.tess(D + 'bos/tess/%03d.tsv' % pag)}
            tp = tor_pag(pag)
            if tp:
                fontes['AT'] = LN.pdf(tor, tp)
                if os.path.exists(D + 'tor/tess/%03d.tsv' % tp): fontes['TT'] = LN.tess(D + 'tor/tess/%03d.tsv' % tp)
            versos_mod = [mod[c][i] for i in idx]
            leit = {}
            for f, ls in fontes.items():
                cas = casar(versos_mod, ls)
                leit[f] = []
                for k, i in enumerate(idx):
                    words = [w for w in TOK.findall(versos_mod[k]) if re.match(r'[^\W\d_]', w)]
                    if cas[k] is None: leit[f].append(None); continue
                    leit[f].append({'linha': ls[cas[k][0]][2], 'sim': round(cas[k][1], 2), 'pal': leitura(words, toks_ocr(ls[cas[k][0]][2]))})
            if nivel >= 3:
                leit['WS'] = []
                for k, i in enumerate(idx):
                    words = [w for w in TOK.findall(versos_mod[k]) if re.match(r'[^\W\d_]', w)]
                    t = re.sub(r'⟦\d+⟧', '', v[i][2]).replace('_', '')
                    leit['WS'].append({'linha': t, 'sim': 1, 'pal': leitura(words, toks_ocr(t))})
            for k, i in enumerate(idx):
                saida.append({'canto': c, 'v': i + 1, 'pag': pag, 'nivel': nivel, 'mod': mod[c][i], 'ws69': v[i][2],
                              'leit': {f: leit[f][k] for f in leit}})
    json.dump(saida, open(D + 'confronto.json', 'w'), ensure_ascii=False, indent=0)
    print(len(saida), 'versos')
if __name__ == '__main__':
    main()
