"""Lacunas: trechos da BAE 53 sem par no texto de 1915 (original/), e trechos de 1915 sem par na BAE (sujeira).
Por capítulo, para ser rápido."""
import re, sys, glob, unicodedata, difflib, json
def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-zñ0-9]', '', w.replace('ñ', 'n'))
ORIG = sys.argv[1]
L = open('dl/bae53.txt', encoding='utf-8').read().split('\n')[4627:19279]
t = re.sub(r'-\s*\n\s*', '', '\n'.join(L))
bae = [w for w in (norm(x) for x in t.split()) if w]
bmc = []
for f in sorted(glob.glob(ORIG + '/*.txt')):
    cap = f[-6:-4]
    for b in re.split(r'\n\s*\n', open(f, encoding='utf-8').read()):
        if b.startswith('#'): continue
        m = re.match(r'\[(\d+\.\d+)\]', b); mk = m.group(1) if m else cap
        for w in b.split():
            n = norm(w)
            if n: bmc.append((n, mk, w))
sm = difflib.SequenceMatcher(None, [x[0] for x in bmc], bae, autojunk=False)
out = []
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op in ('insert', 'replace') and j2 - j1 >= 8 and (i2 - i1) < (j2 - j1) / 2:
        mk = bmc[i1][1] if i1 < len(bmc) else 'fim'
        out.append(('FALTA_EM_1915', mk, j2 - j1, ' '.join(bae[j1:j1+12])))
    if op in ('delete', 'replace') and i2 - i1 >= 6 and (j2 - j1) < (i2 - i1) / 2:
        out.append(('SOBRA_EM_1915', bmc[i1][1], i2 - i1, ' '.join(x[2] for x in bmc[i1:i2])[:200]))
json.dump(out, open('dl/lacunas.json', 'w'), ensure_ascii=False, indent=0)
for o in out: print(o[0], o[1], o[2], '|', o[3][:90])
