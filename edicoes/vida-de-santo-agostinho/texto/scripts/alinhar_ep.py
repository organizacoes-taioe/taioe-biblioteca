"""Alinha as leituras do PL 32 (A,B,G,H) ao esqueleto de Weiskotten (W) e vota palavra a palavra."""
import sys, json, re, difflib, collections
r = json.load(open(sys.argv[1]))
LET = re.compile(r'[A-Za-zÀ-ÿſæœÆŒ]')

def chave(t):
    t = t.lower().replace('ſ','s').replace('f','s').replace('æ','ae').replace('œ','oe').replace('ﬀ','ff').replace('ﬁ','fi').replace('ﬂ','fl')
    t = re.sub(r'[^a-zà-ÿ]', '', t)
    t = t.translate(str.maketrans('jvàáâèéêìíîòóôùúûë', 'iuaaaeeeiiiooouuue'))
    t = t.replace('ae','e').replace('oe','e')
    return t

def preparar(toks):
    """Junta hífens de fim de linha; pontuação solta vira sufixo do anterior."""
    out = []
    i = 0
    while i < len(toks):
        t = dict(toks[i]); s = t['t']
        while (s.endswith('-') or s.endswith('—') and len(s)>1) and i+1 < len(toks) and LET.search(s) and re.match(r'[a-zſæœ]', toks[i+1]['t']):
            s = s.rstrip('-—') + toks[i+1]['t']; i += 1
        t['t'] = s
        if not chave(s) and out and not re.search(r'[0-9]', s):
            out[-1]['t'] += s if s[0] not in '(' else ''
        elif chave(s):
            out.append(t)
        i += 1
    return out

W = preparar(r['W'])
ini = next(i for i,x in enumerate(W) if x['t']=='PRAEFATIO')
fim = max(i for i,x in enumerate(W) if x['p'] <= 149)
W = W[ini:fim+1][10111:11053]
wk = [chave(x['t']) for x in W]

def sim(a, b):
    if not a or not b: return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()

def bloco(ws, ps):
    """DP para emparelhar um bloco desigual. Devolve lista de (i_w|None, [j_p...])."""
    m, n = len(ws), len(ps)
    INF = 1e9
    D = [[INF]*(n+1) for _ in range(m+1)]; B = [[None]*(n+1) for _ in range(m+1)]
    D[0][0] = 0
    for i in range(m+1):
        for j in range(n+1):
            d = D[i][j]
            if d >= INF: continue
            movs = []
            if i<m and j<n: movs.append((1,1, 1-sim(ws[i],ps[j])))
            if i<m: movs.append((1,0, 0.9))
            if j<n: movs.append((0,1, 0.9))
            if i<m and j+1<n: movs.append((1,2, 1-sim(ws[i],ps[j]+ps[j+1]) + 0.05))
            if i+1<m and j<n: movs.append((2,1, 1-sim(ws[i]+ws[i+1],ps[j]) + 0.05))
            for di,dj,c in movs:
                if d+c < D[i+di][j+dj]:
                    D[i+di][j+dj] = d+c; B[i+di][j+dj] = (di,dj)
    i,j = m,n; pares = []
    while i or j:
        di,dj = B[i][j]
        pares.append((i-di, di, j-dj, dj)); i-=di; j-=dj
    return pares[::-1]

def alinhar(fonte):
    P = preparar(r[fonte]); pk = [chave(x['t']) for x in P]
    sm = difflib.SequenceMatcher(None, wk, pk, autojunk=False)
    slot = [None]*len(wk); gap = collections.defaultdict(list)
    ops = sm.get_opcodes()
    for tag,i1,i2,j1,j2 in ops:
        if tag == 'equal':
            for k in range(i2-i1): slot[i1+k] = [P[j1+k]]
        elif tag == 'replace' or tag == 'insert' or tag == 'delete':
            if tag == 'insert' and j2-j1 > 6:   # nota, cabeçalho, sumário: fora
                continue
            if tag == 'delete': continue
            if (i2-i1) > 1200 or (j2-j1) > 1500:
                continue
            for (i,di,j,dj) in bloco(wk[i1:i2], pk[j1:j2]):
                if di and dj and di == 1 and dj == 1 and sim(wk[i1+i], pk[j1+j]) < 0.4:
                    gap[i1+i-1].append(P[j1+j])
                elif di and dj:
                    slot[i1+i] = [P[j1+j+q] for q in range(dj)]
                    if di == 2: slot[i1+i+1] = []   # absorvido
                elif dj:
                    gap[i1+i-1].append(P[j1+j])
    return slot, gap

res = {'W': W}
for f in [k for k in ('W2','A','B') if k in r]:
    s,g = alinhar(f)
    res[f] = {'slot': s, 'gap': {str(k):v for k,v in g.items()}}
    ok = sum(1 for i,x in enumerate(s) if x and chave(''.join(t['t'] for t in x))==wk[i])
    print(f, 'slots', sum(1 for x in s if x is not None), 'iguais a W', ok, 'de', len(wk))
json.dump(res, open(sys.argv[2],'w'), ensure_ascii=False)
