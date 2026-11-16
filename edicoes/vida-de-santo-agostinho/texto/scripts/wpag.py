import sys,re; sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
ps = paginas(sys.argv[1])
EN = set('the and of that he his to was which in with for they by as were had not is it'.split())
for i,(W,H,ls) in enumerate(ps):
    ws=[w[4].lower() for l in ls for w in l]
    if not ws: continue
    en=sum(w in EN for w in ws)/len(ws)
    t=' '.join(w[4] for w in ls[0])[:50] if ls else ''
    print(i,len(ws),round(en,2),t)
