import sys; sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
ps = paginas(sys.argv[1], ate=int(sys.argv[2]))
for i,(W,H,ls) in enumerate(ps):
    t=' '.join(w[4] for l in ls for w in l).lower()
    hits=[k for k in sys.argv[3:] if k in t]
    if hits: print(i, hits)
