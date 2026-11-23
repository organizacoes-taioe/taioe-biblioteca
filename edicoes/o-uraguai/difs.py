"""Diferenças de palavra entre o texto moderno e as leituras de 1769 (confronto.json).
Uma variante só conta se aparece nos dois exemplares (Boston: AB/TB; Toronto: AT/TT) ou no WS revisado + um exemplar.
Erros típicos do OCR com o ſ (ſſ → íT, fl, íl; ſt → íl, ft, lt) não contam."""
import json, sys, os, re, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
from confronto import L, TOK
d = json.load(open(D + 'confronto.json'))
def palavras(s): return [w for w in TOK.findall(s) if re.match(r'[^\W\d_]', w)]
def igual(r, m):
    a, b = L(r), L(m)
    if a == b: return True
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal': continue
        x, y = a[i1:i2], b[j1:j2]
        if op == 'replace' and set(x) <= set('iltsfbjí') and set(y) <= set('st') and abs(len(x) - len(y)) <= 1: continue
        if op == 'delete' and set(x) <= set('ilf') and len(x) <= 1 and ('s' in a[max(0, i1 - 1):i2 + 1]): continue
        return False
    return True
def variantes(x, k, w):
    lido = {}
    for f in ['WS', 'AB', 'TB', 'AT', 'TT']:
        l = x['leit'].get(f)
        if l and l['pal'][k] is not None: lido[f] = l['pal'][k][0]
    grupos = []  # [(rep, set(fontes))]
    for f, r in lido.items():
        if not r.startswith('∅') and igual(r, w): continue
        for g in grupos:
            if (r.startswith('∅') and g[0].startswith('∅')) or (not r.startswith('∅') and not g[0].startswith('∅') and (igual(r, g[0]) or igual(g[0], r))):
                g[1].add(f); break
        else:
            grupos.append((r, {f}))
    fortes = []
    for rep, fs in grupos:
        b = fs & {'AB', 'TB'}; t = fs & {'AT', 'TT'}
        if (b and t) or ('WS' in fs and (b or t)):
            fortes.append((rep, sorted(fs)))
    return lido, fortes
if __name__ == '__main__':
    n = 0
    for x in d:
        ws = palavras(x['mod'])
        for k, w in enumerate(ws):
            lido, fortes = variantes(x, k, w)
            if fortes:
                n += 1
                print('%s,%d [%d] %-14s → %s   | %s' % (x['canto'], x['v'], k, w, ' ; '.join('%s(%s)' % (r, ''.join(f[0] + f[1].lower() for f in fs)) for r, fs in fortes),
                                                 ' '.join('%s:%s' % kv for kv in lido.items())))
    print(n, file=sys.stderr)
