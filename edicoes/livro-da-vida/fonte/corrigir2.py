"""2.ª passada de OCR, direto nos original/*.txt: «g» por «y» em palavra que não existe nos outros testemunhos,
«i» solto = «¡», cabeços de página. Registro em dl/correcoes2.tsv."""
import re, glob, sys, unicodedata
from collections import Counter
D = sys.argv[1]
def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-zñ0-9]', '', w.replace('ñ', 'n'))
def txt_norms(arq, a, b):
    t = '\n'.join(open(arq, encoding='utf-8').read().split('\n')[a-1:b])
    t = re.sub(r'-\s*\n\s*', '', t)
    return Counter(norm(w) for w in t.split())
bae = txt_norms('dl/bae53.txt', 4628, 19279); hei = txt_norms('dl/heitz.txt', 1489, 17131)
outros = bae + hei
arqs = sorted(glob.glob(D + '/*.txt'))
cont = Counter()
for f in arqs:
    for w in re.findall(r'[^\W\d_]+', open(f, encoding='utf-8').read()): cont[w.lower()] += 1
reg = []
PAL = re.compile(r'[^\W\d_]+')
def fix_word(m):
    w = m.group(0); n = norm(w)
    if 'g' in w.lower() and outros[n] == 0:
        for cand in {w.replace('g', 'y'), w.replace('G', 'Y')} | {w[:k] + 'y' + w[k+1:] for k, c in enumerate(w) if c == 'g'}:
            if outros[norm(cand)] >= 2 and cand != w:
                reg.append((w, cand)); return cand
    return w
for f in arqs:
    s = open(f, encoding='utf-8').read()
    cab, _, corpo = s.partition('\n\n')
    c2 = PAL.sub(fix_word, corpo)
    c3 = re.sub(r'(?<![\w¡¿])i (?=[A-ZÁÉÍÓÚ]|oh\b|qu[eé]\b|cu[aá]n|c[oó]mo\b)', lambda m: (reg.append(('i ', '¡')), '¡')[1], c2)
    c3 = re.sub(r'\s*\b\d{1,3} VIDA DE SANTA TERESA DE JESUS\b\s*', lambda m: (reg.append((m.group(0).strip(), '')), ' ')[1], c3)
    if c3 != corpo:
        open(f, 'w', encoding='utf-8').write(cab + '\n\n' + c3)
open('dl/correcoes2.tsv', 'w').write('\n'.join(a + '\t' + b for a, b in reg) + '\n')
print(len(reg)); print(Counter(reg).most_common(40))
