"""achar.py <palavra do OCR> : folha, coluna e linha onde está (para ver a imagem)"""
import sys, json, os
L = json.load(open(os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso/linhas.json'), encoding='utf-8'))
for p in L:
    for i, l in enumerate(p['linhas']):
        s = ' '.join(t[0] for t in l['toks'])
        if sys.argv[1] in s:
            print(p['folha'], p['ci'], l['y'], l['x0'], s[:80])
