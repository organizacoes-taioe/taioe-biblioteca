"""Confere as linhas de base/<id>.txt (ou 1901/<id>.txt) com as do OCR de 1901: lista as que não batem.
    python3 edicoes/poesias-completas-machado/linhas.py [base|1901] [id ...]"""
import json, os, re, sys
from difflib import SequenceMatcher
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rascunho as R  # noqa
def n(l):
    return ' '.join(R.norm(w) for w in R.TOK.findall(l) if re.match(r'[^\W_]', w))
pasta = sys.argv[1]
so = set(sys.argv[2:])
P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
tot = 0
for p in P:
    f = os.path.join(AQUI, pasta, p['id'] + '.txt')
    if not os.path.exists(f) or (so and p['id'] not in so):
        continue
    base = [l for l in open(f, encoding='utf-8').read().split('\n') if l.strip() and not l.startswith('#')]
    ocr = [l for l in R.tess_texto(*p['pdf']).split('\n') if len(n(l)) > 3]
    on = [n(l) for l in ocr]
    bn = [n(l) for l in base]
    ruins = []
    for l, x in zip(base, bn):
        if not x: continue
        r = max((SequenceMatcher(None, x, y).ratio() for y in on), default=0)
        if r < 0.8 or '⟦' in l: ruins.append('  B %.2f %s' % (r, l))
    for l, y in zip(ocr, on):
        r = max((SequenceMatcher(None, y, x).ratio() for x in bn), default=0)
        if r < 0.6: ruins.append('  O %.2f %s' % (r, l))
    if ruins:
        print('==', p['id'], len(ruins)); print('\n'.join(ruins))
    tot += len(ruins)
print('total', tot)
