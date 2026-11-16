import sys; sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
ps = paginas(sys.argv[1], ate=90)
for i,(W,H,ls) in enumerate(ps):
    t = ' '.join(w[4] for l in ls[:3] for w in l)
    if 'POSSID' in ' '.join(w[4] for l in ls for w in l).upper() or 'CAPUT' in t:
        print(i, W, H, len(ls), t[:80])
