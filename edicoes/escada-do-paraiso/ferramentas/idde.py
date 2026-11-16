"""idde.py <bloco> [palavra]: id da 1ª palavra do bloco (ou da 1ª palavra que contém o trecho); mostra o começo"""
import sys, json, os
b = json.load(open(os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso/blocos.json'), encoding='utf-8'))
x = b[int(sys.argv[1])]['pal']
ws = [(w, t) for w, t in x if t]
k = 0
if len(sys.argv) > 2:
    k = next(i for i, (w, t) in enumerate(ws) if sys.argv[2] in w)
print(ws[k][1], ' '.join(w for w, t in ws[max(0, k - 3):k + 8]))
