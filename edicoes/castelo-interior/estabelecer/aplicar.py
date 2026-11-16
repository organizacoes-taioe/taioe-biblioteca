import json, sys
base = sys.argv[1]
L=json.load(open(f'{base}/conferir.json')); D=json.load(open(f'{base}/decisoes-ctx.json'))
V=json.load(open(f'{base}/votado2.json')); tok=V['tok']
cor={}; sem=[]
for x in L:
    antes=x['ctx'].split('[[')[0].strip()
    m=[d for d in D if d['antes'][-25:]==antes[-25:]]
    if m:
        if tok[x['pos']]!=m[0]['forma']: cor[str(x['pos'])]=m[0]['forma']
    elif x['cands'] and set(x['cands']) <= {'¶', ''}: pass
    else: sem.append(x)
for i in range(len(tok)-3):
    if tok[i]=='con' and tok[i+1]=='mucha' and tok[i+2]=='y' and tok[i+3].startswith('ganancia'): cor[str(i+2)]=''
json.dump(cor,open(f'{base}/correcoes.json','w'),ensure_ascii=False,indent=0)
print(len(cor),'correções;',len(sem),'sem decisão')
for x in sem: print(x['n'], x['tipo'][:4], x['cands'], '|', x['ctx'][:110])
