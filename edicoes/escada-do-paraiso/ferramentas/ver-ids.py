"""ver-ids.py <trecho> [n palavras]: mostra as palavras com id em volta de cada ocorrência do trecho no texto montado"""
import sys, json, os
b = json.load(open(os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso/blocos.json'), encoding='utf-8'))
plano = [(w, t, bi) for bi, x in enumerate(b) for w, t in x['pal']]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
for k, (w, t, bi) in enumerate(plano):
    if sys.argv[1] in w:
        print('---', bi)
        for w2, t2, b2 in plano[max(0, k - n):k + n]: print('  ', b2, t2, w2)
