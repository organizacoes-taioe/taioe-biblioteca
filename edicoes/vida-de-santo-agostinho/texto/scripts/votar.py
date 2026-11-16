"""Vota cada palavra: leituras do PL (A 1845, B 1841 t.1-2, C 1841 t.1, G 1844) contra Weiskotten (W, W2)."""
import sys, json, re, difflib, collections
r = json.load(open(sys.argv[1]))
W = r['W']; n = len(W)
SRC = [k for k in ('A','B','C','G') if k in r]
PESO = {'A':1.0,'B':1.0,'C':1.0,'G':0.6}

def base(t):
    t = t.lower().replace('æ','ae').replace('œ','oe').replace('ﬀ','ff').replace('ﬁ','fi').replace('ﬂ','fl')
    t = re.sub(r'[^a-zà-ÿſ]', '', t)
    return t.translate(str.maketrans('jvàáâèéêìíîòóôùúûë', 'iuaaaeeeiiiooouuue'))
def chaves(t):
    """conjunto de chaves possíveis: ſ pode ser s ou f (o OCR troca)"""
    b = base(t)
    if 'ſ' not in b: return {b}
    out = {''}
    for ch in b:
        out = {o+c for o in out for c in (('s','f') if ch=='ſ' else (ch,))}
        if len(out) > 16: break
    return out
def junta(x): return '|'.join(t['t'] for t in x) if x else None

saida = []
cont = collections.Counter()
for i in range(n):
    wf = W[i]['t']; wk = base(wf)
    w2 = junta(r['W2']['slot'][i]) if 'W2' in r else None
    leit = {k: junta(r[k]['slot'][i]) for k in SRC}
    sup = collections.Counter(); forma = {}
    for k,v in leit.items():
        if not v: continue
        for c in chaves(v):
            sup[c] += PESO[k]; forma.setdefault(c, (k, v))
    pres = [k for k,v in leit.items() if v]
    if not pres:
        cls = 'sem'; esc = None
    else:
        melhor, sm = sup.most_common(1)[0]
        if w2 and base(w2) != wk and sup.get(base(w2),0) > sup.get(wk,0):
            wk = base(w2); wf = w2          # a outra leitura de Weiskotten acerta
        if sup.get(wk, 0) >= 1 and (melhor == wk or sm < 2):
            cls = 'ok'; esc = wk
        elif sm >= 2 and melhor != wk:
            cls = 'pl'; esc = melhor          # variante do PL (duas leituras concordam)
        elif sup.get(wk,0) > 0:
            cls = 'fraco'; esc = wk           # só a G apoia W
        else:
            # ninguém concorda; ver se alguma leitura é quase W
            sims = [difflib.SequenceMatcher(None, base(v), wk).ratio() for v in leit.values() if v]
            cls = 'dub' if max(sims) >= 0.6 else 'ruido'
            esc = wk
    cont[cls] += 1
    item = {'i': i, 'w': wf, 'wk': wk, 'w2': w2, 'cls': cls, 'k': esc, 'leit': leit}
    if esc in forma: item['de'] = forma[esc][0]; item['forma'] = forma[esc][1]
    saida.append(item)
print(dict(cont))
json.dump(saida, open(sys.argv[2],'w'), ensure_ascii=False)
