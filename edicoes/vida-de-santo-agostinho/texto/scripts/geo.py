import sys; sys.path.insert(0, sys.argv[0].rsplit('/',1)[0])
from djvu import paginas
ps = paginas(sys.argv[1], ate=int(sys.argv[2])+1)
W,H,ls = ps[int(sys.argv[2])]
print(W,H)
for l in ls:
    x1=min(w[0] for w in l); x2=max(w[2] for w in l); y1=min(w[1] for w in l); y2=max(w[3] for w in l)
    hs=sorted(w[3]-w[1] for w in l); 
    print(x1,x2,y1,y2-y1,hs[len(hs)//2], ' '.join(w[4] for w in l)[:25])
