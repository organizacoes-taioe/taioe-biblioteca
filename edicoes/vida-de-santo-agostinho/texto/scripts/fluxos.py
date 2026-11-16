"""Gera os fluxos de palavras: Weiskotten (latim) e as 4 leituras do PL 32. Grava JSON."""
import sys, json, re, statistics
sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
D = sys.argv[1]  # pasta dl
EN = set('the and of that he his to was which in with for they by as were had not is it'.split())

def wstream(path):
    ps = paginas(path)
    out = []
    for i,(W,H,ls) in enumerate(ps):
        ws=[w[4].lower() for l in ls for w in l]
        if len(ws) < 30: continue
        if sum(w in EN for w in ws)/len(ws) > 0.15: continue
        hs = [statistics.median([w[3]-w[1] for w in l]) for l in ls]
        med = statistics.median(hs)
        lefts = [min(w[0] for w in l) for l in ls]
        margem = statistics.median(lefts)
        for j,(l,h) in enumerate(zip(ls,hs)):
            if j > 3 and h < 0.9*med and all(x < 0.9*med for x in hs[j:j+3]): break       # aparato
            t=' '.join(w[4] for w in l)
            if j == 0 and re.search(r'VITA|AUGUST', t): continue
            for w in l:
                tok = w[4]
                if w[0] < margem - 40 and re.fullmatch(r'[0-9IlOo]+', tok): continue
                out.append({'t': tok, 'p': i})
    return out

def plstream(path, a, b):
    ps = paginas(path, ate=b+1)
    out = []
    for i in range(a, b+1):
        W,H,ls = ps[i]
        cols = [[],[]]
        for l in ls:
            cx = (min(w[0] for w in l)+max(w[2] for w in l))/2
            # linha que atravessa as duas colunas: separar pelas palavras
            if min(w[0] for w in l) < W/2 < max(w[2] for w in l) and max(w[2] for w in l)-min(w[0] for w in l) > 0.6*W:
                e=[w for w in l if (w[0]+w[2])/2 < W/2]; d=[w for w in l if (w[0]+w[2])/2 >= W/2]
                if e: cols[0].append(e)
                if d: cols[1].append(d)
            else:
                cols[0 if cx < W/2 else 1].append(l)
        for c,col in enumerate(cols):
            col.sort(key=lambda l: min(w[1] for w in l))
            for l in col:
                for w in l:
                    out.append({'t': w[4], 'p': i, 'c': c, 'b': [w[0],w[1],w[2],w[3]]})
    return out

fontes = {
 'W': ('sanctiaugustiniv00possrich.djvu.xml', None),
 'W2': ('cu31924029266513.djvu.xml', None),
 'A': ('bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_32.djvu.xml', (14, 40)),
 'B': ('sanctiaureliiau1v2augu.djvu.xml', (14, 45)),
 'C': ('sanctiaureliiau01augu.djvu.xml', (20, 50)),
 'G': ('patrologiaecurs157unkngoog.djvu.xml', (19, 44)),
}
import os
res = {}
for k,(f,r) in fontes.items():
    if not os.path.exists(f'{D}/{f}') or os.path.getsize(f'{D}/{f}') < 100000: continue
    p = f'{D}/{f}'
    res[k] = wstream(p) if r is None else plstream(p, *r)
    print(k, len(res[k]))
json.dump(res, open(sys.argv[2],'w'), ensure_ascii=False)
