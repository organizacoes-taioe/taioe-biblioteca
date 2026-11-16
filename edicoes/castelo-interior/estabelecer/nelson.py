import re, glob, difflib, unicodedata, sys
def simp(w):
    w = ''.join(ch for ch in unicodedata.normalize('NFD', w.lower()) if unicodedata.category(ch) != 'Mn')
    w = re.sub(r'[^a-z]', '', w)
    return {'ansi': 'asi', 'mesmo': 'mismo', 'mesma': 'misma', 'mesmos': 'mismos', 'mesmas': 'mismas', 'agora': 'ahora'}.get(w, w)
nos = ' '.join(open(f).read() for f in sorted(glob.glob('trab/original/*.txt')))
nos = re.sub(r'\[[IV]+\.\d+\]', ' ', nos)
A = [w for w in nos.split() if simp(w)]
nel = open('dl/nelson.txt').read()
nel = re.sub(r'-\s*\n\s*', '', nel)
B = [w for w in nel.split() if simp(w)]
a = [simp(w) for w in A]; b = [simp(w) for w in B]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ('insert', 'replace') and (j2 - j1) - (i2 - i1) >= 5:
        print(f'NELSON+ {j2-j1} × {i2-i1} | nós: …{" ".join(A[max(0,i1-5):i2+3])}… | Nelson: {" ".join(B[j1:j2])[:200]}')
