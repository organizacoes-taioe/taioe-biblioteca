import sys; sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
ps = paginas(sys.argv[1], ate=80)
r=[]
for i,(W,H,ls) in enumerate(ps):
    t=' '.join(w[4] for l in ls for w in l).upper().replace(' ','')
    if 'POSSID' in t or 'AUCTORE' in t: r.append(i)
print(sys.argv[1][3:40], r)
