"""Diz em que página (do livro e do PDF a) está cada frase. Uso: pagina.py 'frase' ..."""
import re, sys
D = '/home/geremias/.cache/claude-pedidos-0511/teoria-da-relatividade/dl/berdiespezielle00unkngoog.txt'
pg, linhas = 0, []
for l in open(D, encoding='utf-8'):
    m = re.match(r'^\s*[-—–]\s*(\d+)\s*[-—–]', l)
    if m: pg = int(m.group(1)) - 1
    linhas.append((pg, l))
txt = ''.join(re.sub(r'\s+', ' ', l) for _, l in linhas)
pos, acc = [], 0
for p, l in linhas:
    n = len(re.sub(r'\s+', ' ', l)); pos.append((acc, p)); acc += n
for f in sys.argv[1:]:
    i = txt.find(f)
    if i < 0: print(f, '-> ?'); continue
    p = max(pp for a, pp in pos if a <= i) + 1
    print(f, '-> livro', p, 'pdf', p + 9)
