"""Voto das quatro leituras com limpeza de cada candidato antes do voto."""
import sys, json, collections, re, unicodedata
sys.path.insert(0, sys.argv[1]); base = sys.argv[2]
from tokens import norm
D = json.load(open(f'{base}/alinh.json')); T, OPS = D['T'], D['ops']
ids = list(T); A = ids[0]; TA = T[A]; n = len(TA)
nel = open(f'{base}/../dl/obrasescogidasd00tere.txt', encoding='utf-8').read().split('\n')[13260:21070]
lex = collections.Counter(norm(w) for l in nel for w in l.split())
fq = collections.Counter(norm(w) for t in T.values() for w in t)
def conhecida(w):
    x = norm(w); return bool(x) and (lex[x] >= 1 or fq[x] >= 3 or x.isdigit())
# onde há «!» adiante (na leitura A)
excl = [False] * (n + 1)
prox = None
for i in range(n - 1, -1, -1):
    if TA[i] == '¶': prox = None
    if '!' in TA[i]: prox = i
    excl[i] = prox is not None and prox - i <= 45
PREF = "iljf'‘’(^.)«[¥|!*\"“\\¡"
def limpa(w, i):
    if not w or w == '¶': return w
    w = w.replace('€', 'e').replace('ﬁ', 'fi')
    if w == 'g': return 'y'
    if w in ('!y', 'jj', 'ij'): return 'y'
    if 'fi' in w and not conhecida(w) and conhecida(w.replace('fi', 'ñ')): w = w.replace('fi', 'ñ')
    for _ in range(2):
        if len(w) > 1 and w[0] in PREF and (not conhecida(w) or w[0] in 'ijl¡' and norm(w[0]) and not conhecida(w)) and conhecida(w[1:]):
            c = w[0]; w = w[1:]
            if c in 'ijl¡' and excl[i] and w[0].isalpha(): return '¡' + w
    if w.startswith('¡') and not excl[i]: w = w[1:]
    return w
cand = [[limpa(TA[i], i)] for i in range(n)]
ins = collections.defaultdict(list)
for w, ops in OPS.items():
    tw = T[w]
    for tag, i1, i2, j1, j2 in ops:
        if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1): cand[i1 + k].append(limpa(tw[j1 + k], i1 + k))
        elif tag == 'replace':
            cand[i1].append(' '.join(limpa(x, i1) for x in tw[j1:j2]))
            for k in range(i1 + 1, i2): cand[k].append('')
        elif tag == 'delete':
            for k in range(i1, i2): cand[k].append('')
        else:
            ins[i1].append(' '.join(limpa(x, i1) for x in tw[j1:j2]))
def sem(x): return ''.join(ch for ch in unicodedata.normalize('NFD', x) if unicodedata.category(ch) != 'Mn')
exact = collections.Counter(c for cs in cand for c in cs)
G = collections.Counter()
for cs in cand:
    if len(cs) == 4 and len(set(norm(x) for x in cs)) == 1 and cs[0]: G[norm(cs[0])] += 1
def letras(x): return re.sub(r'[^\wáéíóúüñÁÉÍÓÚÜÑ ]', '', x).lower().strip()
def boa(x): return bool(x) and all(G[norm(y)] for y in x.split() if norm(y))
SENS = {'mi','si','el','tu','mas','que','como','cuan','donde','adonde','quien','cuanto','cuanta','cuantas','cuantos','solo','este','esta','esto','estos','estas','ese','esa','eso','aquel','aquella','aun','de','se','te','cual','cuales','cuando','esté','está'}
out, duv, src = [], [], []
for i in range(n + 1):
    if ins.get(i):
        c = collections.Counter(ins[i]).most_common(1)[0]
        if c[1] >= 3 or (c[1] >= 2 and (c[0] == '¶' or boa(c[0]))):
            out.extend(c[0].split()); src.extend([i] * len(c[0].split()))
            if c[1] < 3: duv.append((len(out) - 1, 'ins', ins[i]))
    if i == n: break
    cs = cand[i]; c = collections.Counter(cs).most_common()
    if len(c) == 1 or c[0][1] >= 3:
        f = c[0][0]
    else:
        ls = {}
        for x in cs:
            ls.setdefault(letras(x), []).append(x)
        if len(ls) == 1:                       # só pontuação: a maioria, ou a do ABBYY
            f = c[0][0] if c[0][1] > c[1][1] else cs[0]
        else:
            # votos por forma em letras
            vl = collections.Counter(letras(x) for x in cs)
            top = vl.most_common()
            boas = [l for l, _ in top if boa(l)]
            rnm = len(set(re.sub('rn', 'm', l) for l, _ in top if l)) < len([l for l, _ in top if l])
            if top[0][1] >= 3:
                l = top[0][0]
            elif rnm:
                l = top[0][0] if top[0][1] > top[1][1] else (cs[2] if len(cs) > 2 and cs[2] else top[0][0])
                l = letras(l); duv.append((len(out), 'rn-m', cs))
            elif len(boas) == 1:
                l = boas[0]
            else:
                ss = set(sem(l) for l, _ in top if l)
                cand_l = [l for l, k in top if k == top[0][1]]
                if len(ss) == 1:
                    l = max(cand_l, key=lambda x: exact.get(x, 0) + sum(exact[y] for y in ls[x]))
                    if sem(l) in SENS and top[0][1] < 3: duv.append((len(out), 'acento', cs))
                else:
                    pool = [l for l in cand_l if boa(l)] or cand_l
                    l = max(pool, key=lambda x: (len(ls[x]), sum(G[norm(y)] for y in x.split())))
                    duv.append((len(out), 'duvida', cs))
            fs = collections.Counter(ls[l]).most_common()
            f = fs[0][0] if len(fs) == 1 or fs[0][1] > fs[1][1] else next((x for x in cs if x in ls[l]), fs[0][0])
    if f: out.extend(f.split()); src.extend([i] * len(f.split()))
# pontuação solta junta à palavra anterior
o2, s2, mapa = [], [], []
for k, w in enumerate(out):
    if o2 and o2[-1] != '¶' and re.fullmatch(r'[,.;:!?)\]»”]+', w): o2[-1] += w
    else: o2.append(w); s2.append(src[k])
    mapa.append(len(o2) - 1)
duv = [(mapa[p] if p < len(mapa) else len(o2) - 1, t, c) for p, t, c in duv]
json.dump({'tok': o2, 'src': s2, 'duv': duv}, open(f'{base}/votado2.json', 'w'), ensure_ascii=False)
print(len(o2), collections.Counter(d[1] for d in duv))
desc = collections.Counter(w for w in o2 if w != '¶' and not conhecida(w))
print('desconhecidas', sum(desc.values()), ' '.join(w for w, _ in desc.most_common(80)))

