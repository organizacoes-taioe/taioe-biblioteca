import json
a = json.load(open('alinhado.json')); e = json.load(open('alinhado_ep.json'))
va = json.load(open('votos.json')); ve = json.load(open('votos_ep.json'))
I0, I1 = 10111, 11053
m = {'W': a['W']}
for k in ('W2','A','B','C','G'):
    if k not in a: continue
    sl = a[k]['slot'][:I0] + (e[k]['slot'] if k in e else [None]*(I1-I0)) + a[k]['slot'][I1:]
    gp = {g:t for g,t in a[k]['gap'].items() if not (I0-1 <= int(g) < I1)}
    if k in e:
        for g,t in e[k]['gap'].items(): gp[str(int(g)+I0)] = t
    m[k] = {'slot': sl, 'gap': gp}
json.dump(m, open('alinhado_m.json','w'), ensure_ascii=False)
vv = va[:I0]
for x in ve:
    x = dict(x); x['i'] += I0; x['leit'].setdefault('C', None); x['leit'].setdefault('G', None); x['ep'] = True; vv.append(x)
vv += va[I1:]
assert len(vv) == len(va)
json.dump(vv, open('votos_m.json','w'), ensure_ascii=False)
print(len(vv))
