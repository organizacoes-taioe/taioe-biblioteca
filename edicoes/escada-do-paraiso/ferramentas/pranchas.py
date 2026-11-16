"""pranchas.py [NN …]: recortes das palavras suspeitas (suspeitas/degrau-NN.tsv) em pranchas de 20, numeradas,
em ~/.cache/claude-pedidos-0511/escada-do-paraiso/pranchas/degrau-NN-<p>.png, com o índice degrau-NN.tsv
(nº, bloco, palavra do OCR, folha:x:y)."""
import sys, os, re
from PIL import Image, ImageDraw
W = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(W, 'pranchas'), exist_ok=True)
def folhas_do_degrau(n):
    s = open(os.path.join(AQUI, 'original', 'degrau-%02d.txt' % n), encoding='utf-8').read()
    cols = [int(c) for c in re.findall(r'PG 88\.(\d+)', s)]
    if not cols: return set()
    return set(range(316 + (min(cols) - 633) // 2 - 1, 316 + (max(cols) - 633) // 2 + 1))
for a in (sys.argv[1:] or [str(n) for n in range(1, 31)]):
    n = int(a); ok = folhas_do_degrau(n)
    linhas = [l.split('\t') for l in open(os.path.join(W, 'suspeitas', 'degrau-%02d.tsv' % n), encoding='utf-8').read().split('\n') if l.strip()]
    idx, crops = [], []
    for i, (bl, w, locs) in enumerate(linhas, 1):
        cand = [tuple(map(int, x.split(':'))) for x in locs.split()] if locs else []
        cand = [c for c in cand if c[0] in ok] or cand
        if not cand: idx.append('%d\t%s\t%s\t-' % (i, bl, w)); continue
        f, x, y = cand[0]
        im = Image.open(os.path.join(W, 'pag', '%04d.png' % f))
        c = im.crop((max(0, x - 260), max(0, y - 14), min(im.width, x + 520), y + 62)).resize((546, 53))
        crops.append((i, c)); idx.append('%d\t%s\t%s\t%d:%d:%d' % (i, bl, w, f, x, y))
    for p in range(0, len(crops), 20):
        lote = crops[p:p + 20]
        o = Image.new('L', (600, 60 * len(lote)), 255); d = ImageDraw.Draw(o)
        for j, (i, c) in enumerate(lote):
            d.text((2, 60 * j + 20), str(i), fill=0); o.paste(c, (50, 60 * j + 3)); d.line((50 + 182, 60 * j + 56, 50 + 260, 60 * j + 56), fill=0)
        o.save(os.path.join(W, 'pranchas', 'degrau-%02d-%d.png' % (n, p // 20 + 1)))
    open(os.path.join(W, 'pranchas', 'degrau-%02d.tsv' % n), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
    print(n, len(crops), 'recortes')
