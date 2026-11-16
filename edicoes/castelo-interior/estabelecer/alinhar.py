import sys, json, difflib, time
sys.path.insert(0, sys.argv[1])
from tokens import tokens, norm
ids = sys.argv[3:]
base = sys.argv[2]
R = {i: [] for i in ids}
T = {i: tokens(f'{base}/{i}.lin', R[i]) for i in ids}
for i in ids: print(i, len(T[i]))
A = ids[0]
an = [norm(w) for w in T[A]]
res = {}
for w in ids[1:]:
    t0 = time.time()
    bn = [norm(x) for x in T[w]]
    sm = difflib.SequenceMatcher(None, an, bn, autojunk=False)
    ops = sm.get_opcodes()
    res[w] = ops
    eq = sum(i2 - i1 for tag, i1, i2, j1, j2 in ops if tag == 'equal')
    print(w, 'igual', eq, 'de', len(an), f'{time.time()-t0:.0f}s')
json.dump({'T': T, 'R': R, 'ops': res}, open(f'{base}/alinh.json', 'w'), ensure_ascii=False)
