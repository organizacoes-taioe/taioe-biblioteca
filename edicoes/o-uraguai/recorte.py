"""Pranchas de recortes: python3 recorte.py saida.jpg 1,73 1,85 ... (canto,verso). Para cada verso, a linha de Boston e
a de Toronto (pelas coordenadas do Tesseract), com o texto moderno embaixo."""
import json, sys, os, difflib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import *
import linhas as LN
from PIL import Image, ImageDraw, ImageFont
d = {(x['canto'], x['v']): x for x in json.load(open(D + 'confronto.json'))}
MT = {int(k): v for k, v in json.load(open(D + 'mapa_tor.json')).items()}
def caixa(tsv, alvo):
    ls = LN.tess(tsv)
    best = max(ls, key=lambda l: difflib.SequenceMatcher(None, l[2], alvo).ratio())
    xs = [w[0] for w in best[3]] + [w[2] for w in best[3]]; ys = [w[1] for w in best[3]] + [w[3] for w in best[3]]
    return min(xs), min(ys), max(xs), max(ys)
def recorte(img, tsv, alvo, ctx=0):
    x0, y0, x1, y1 = caixa(tsv, alvo)
    im = Image.open(img)
    h = y1 - y0
    return im.crop((max(0, x0 - 60), max(0, y0 - 15 - ctx * h), min(im.width, x1 + 60), min(im.height, y1 + 15 + ctx * h)))
def prancha(saida, chaves, ctx=0, rotulos=None):
    tiras = []
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    for i, (c, v) in enumerate(chaves):
        x = d[(c, v)]
        p = x['pag']; tp = MT.get(p)
        alvo = (x['leit'].get('TB') or {}).get('linha') or x['mod']
        a = recorte(D + 'bos/tess/%03d.jpg' % p, D + 'bos/tess/%03d.tsv' % p, alvo, ctx)
        alvo2 = (x['leit'].get('TT') or {}).get('linha') or x['mod']
        b = recorte(D + 'tor/tess/%03d.jpg' % tp, D + 'tor/tess/%03d.tsv' % tp, alvo2, ctx) if tp else None
        lab = Image.new('L', (1700, 40), 255); ImageDraw.Draw(lab).text((5, 2), '%d,%d  %s   ⟶ %s' % (c, v, x['mod'], rotulos[i] if rotulos else ''), fill=0, font=fonte)
        tiras += [lab, a] + ([b] if b else [])
    W = max(t.width for t in tiras); H = sum(t.height for t in tiras) + 6 * len(tiras)
    out = Image.new('L', (W, H), 255); y = 0
    for t in tiras: out.paste(t, (0, y)); y += t.height + 6
    if out.width > 1600: out = out.resize((1600, int(out.height * 1600 / out.width)))
    out.save(saida, quality=80)
if __name__ == '__main__':
    ctx = int(os.environ.get('CTX', '0'))
    args = [a.split(':') for a in sys.argv[2:]]
    prancha(sys.argv[1], [tuple(map(int, a[0].split(','))) for a in args], ctx, [a[1] if len(a) > 1 else '' for a in args])
