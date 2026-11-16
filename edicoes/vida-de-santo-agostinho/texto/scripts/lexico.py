import os, re, sys, json, collections
raizes = sys.argv[2:]
c = collections.Counter()
def norm(w):
    w = w.lower().replace('æ','ae').replace('œ','oe')
    return w.translate(str.maketrans('jvàáâèéêìíîòóôùúûëäöü', 'iuaaaeeeiiiooouuueaou'))
for r in raizes:
    for dp, dn, fn in os.walk(r):
        for f in fn:
            if not f.endswith(('.txt','.xml','.json','.jsonl','.tsv','.html')): continue
            try: t = open(os.path.join(dp,f), encoding='utf-8', errors='ignore').read()
            except: continue
            for w in re.findall(r"[A-Za-zÀ-ÿæœÆŒ]+", t):
                c[norm(w)] += 1
json.dump(c, open(sys.argv[1],'w'))
print(len(c))
