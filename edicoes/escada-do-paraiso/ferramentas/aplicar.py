"""aplicar.py NN: aplica ~/.cache/claude-pedidos-0511/escada-do-paraiso/decisoes/degrau-NN.tsv (nº<TAB>forma certa,
só as que mudam) ao original/degrau-NN.txt: troca a palavra do OCR, no bloco dela, pela forma certa (a pontuação em
volta fica). Grava o que não achou em decisoes/degrau-NN-nao.tsv."""
import sys, os, re
W = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for a in sys.argv[1:]:
    n = int(a)
    idx = {}
    for l in open(os.path.join(W, 'pranchas', 'degrau-%02d.tsv' % n), encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3: idx[p[0]] = (p[1], p[2])
    arq = os.path.join(AQUI, 'original', 'degrau-%02d.txt' % n)
    blocos = open(arq, encoding='utf-8').read().split('\n\n')
    dec = os.path.join(W, 'decisoes', 'degrau-%02d.tsv' % n)
    nao, feitas = [], 0
    for l in open(dec, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 2 or p[0] not in idx or p[1].strip() in ('', '='): continue
        bl, w = idx[p[0]]; novo = p[1].strip()
        for i, b in enumerate(blocos):
            if b.startswith('[%s] ' % bl):
                b2, k = re.subn(r'(?<![\w])' + re.escape(w) + r'(?![\w])', novo, b, count=1)
                if k: blocos[i] = b2; feitas += 1
                else: nao.append(l)
                break
        else: nao.append(l)
    open(arq, 'w', encoding='utf-8').write('\n\n'.join(blocos))
    open(os.path.join(W, 'decisoes', 'degrau-%02d-nao.tsv' % n), 'w', encoding='utf-8').write(''.join(nao))
    print(n, 'aplicadas', feitas, 'não achadas', len(nao))
