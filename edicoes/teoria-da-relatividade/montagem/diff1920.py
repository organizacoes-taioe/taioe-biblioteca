"""Compara o Gutenberg (1917) com as duas leituras OCR da 5ª ed. (1920) e lista as diferenças em que
as duas leituras concordam entre si (provável mudança do autor)."""
import re, sys, difflib, unicodedata
D = sys.argv[1]
def norm_ocr(t):
    t = re.sub(r'Digitized\s+by\s+(Google)?', ' ', t)
    t = re.sub(r'(?m)^\s*[-—–]\s*\d+\s*[-—–]?\s*$', ' ', t)
    t = re.sub(r'-\s*\n\s*', '', t)          # hifenização
    return t
def norm_g(t):
    t = t.split('*** START')[1].split('*** END')[0]
    t = re.sub(r'\[\d+\]', ' ', t)
    t = t.replace('+', '').replace('_', '')
    return t
def toks(t):
    out = []
    for w in re.findall(r"[\wÄÖÜäöüß′']+", t):
        w = unicodedata.normalize('NFC', w).lower().replace('ß', 'ss').replace('′', "'").replace('₀','0')
        out.append(w)
    return out
G = toks(norm_g(open(f'{D}/g77850.txt', encoding='utf-8').read()))
A = toks(norm_ocr(open(f'{D}/berdiespezielle00unkngoog.txt', encoding='utf-8').read()))
B = toks(norm_ocr(open(f'{D}/bub_gb_kTdWAAAAMAAJ.txt', encoding='utf-8').read()))
def ops(X):
    sm = difflib.SequenceMatcher(None, G, X, autojunk=False)
    res = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal': res.append((i1, i2, X[j1:j2]))
    return res
oa, ob = ops(A), ops(B)
VOCAB = set(G)
def cobre(lst, i1, i2):
    return [o for o in lst if o[0] <= i2 and o[1] >= i1 and not (o[0] == o[1] == i1 and False)]
n = 0
for i1, i2, xa in oa:
    if i2 - i1 == 0 and len(xa) < 3: continue
    for j1, j2, xb in ob:
        if j1 <= i2 and j2 >= i1:
            sa, sb = ' '.join(xa), ' '.join(xb)
            r = difflib.SequenceMatcher(None, sa, sb).ratio()
            VOC = VOCAB
            ok = sa == sb and all(w in VOC for w in xa)
            novo = (i2 - i1 == 0 and len(xa) >= 3 and r > 0.6)
            if ok or novo or (r > 0.8 and i2 - i1 >= 3):
                n += 1
                print(f'G[{i1}:{i2}] «{" ".join(G[max(0,i1-4):i1])} [{" ".join(G[i1:i2])}] {" ".join(G[i2:i2+4])}» → A «{sa[:200]}» | B «{sb[:200]}»')
            break
print(n, 'diferenças concordes', file=sys.stderr)
