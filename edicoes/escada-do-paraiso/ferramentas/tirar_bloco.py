"""tirar_bloco.py <n.k> …: tira o bloco [n.k] do original e da tradução do degrau n e renumera os seguintes."""
import sys, re, os
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for marca in sys.argv[1:]:
    n, k = map(int, marca.split('.'))
    for pasta in ('original', 'traducao'):
        arq = os.path.join(AQUI, pasta, 'degrau-%02d.txt' % n)
        s = open(arq, encoding='utf-8').read()
        partes = s.split('\n\n')
        partes = [p for p in partes if not p.startswith('[%d.%d] ' % (n, k))]
        def ren(m):
            j = int(m.group(2))
            return '[%s.%d]' % (m.group(1), j - 1 if j > k else j)
        partes = [re.sub(r'^\[(%d)\.(\d+)\]' % n, ren, p) for p in partes]
        open(arq, 'w', encoding='utf-8').write('\n\n'.join(partes))
