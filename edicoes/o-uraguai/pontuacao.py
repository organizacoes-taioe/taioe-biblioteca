"""Pontuação de 1769 depois de cada palavra, por voto (WS revisado + 4 OCRs). Grava pontuacao.json e lista os empates."""
import json, sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
from confronto import TOK
d = json.load(open(D + 'confronto.json'))
def palavras(s): return [w for w in TOK.findall(s) if re.match(r'[^\W\d_]', w)]
def np(p):
    p = p.replace('..', '.') if p not in ('...', '....') else p
    p = re.sub(r'\.{3,}', '…', p)
    if len(p) > 1:
        for m in '?!…': 
            if m in p: return m
        return p[0]
    return p
OCRS = ('AB', 'TB', 'AT', 'TT')
def decidir(v):
    """Calibrado nas imagens: o Tesseract acha as vírgulas que a camada OCR do PDF perde; o WS revisado
    tem vírgulas a mais e a menos. Vale o par do Tesseract (os dois exemplares) quando concorda."""
    ocr = {f: v[f] for f in OCRS if f in v}
    if not ocr: return v.get('WS', ''), False
    tb, tt, ab, at = (ocr.get(f) for f in ('TB', 'TT', 'AB', 'AT'))
    if tb is not None and tb == tt:
        if tb == '' and ab and ab == at: return ab, True
        return tb, False
    cnt = collections.Counter(x for x in (tb, tt, ab, at, v.get('WS')) if x is not None)
    (top, n), = cnt.most_common(1)
    if n >= 3: return top, False
    return top, True
res = {}; duvidas = []
for x in d:
    ws = palavras(x['mod']); out = []
    for k, w in enumerate(ws):
        v = {}
        for f in ['WS', 'AB', 'TB', 'AT', 'TT']:
            l = x['leit'].get(f)
            if l and l['pal'][k] is not None and not l['pal'][k][0].startswith('∅'):
                v[f] = np(l['pal'][k][1])
        escolha, duv = decidir(v)
        out.append(escolha)
        if duv: duvidas.append((x['canto'], x['v'], k, w, escolha, dict(v)))
    res['%d,%d' % (x['canto'], x['v'])] = out
json.dump(res, open(D + 'pontuacao.json', 'w'), ensure_ascii=False)
for t in duvidas: print('%d,%d [%d] %s → %r %s' % t)
print(len(duvidas), file=sys.stderr)
