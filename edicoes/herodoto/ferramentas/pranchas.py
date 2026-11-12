"""Pranchas de recortes do fac-símile de 1921 para conferir pontos da colação.
Uso: pranchas.py <pasta-trabalho> <lista.tsv> <saida-prefixo> [por_prancha=10]
A lista tem, por linha: id \t ref \t perseus \t leitura \t pag \t x0,y0,x1,y1 (caixa da palavra no PNG de 300 dpi).
Cada recorte é a linha inteira, com a palavra num retângulo vermelho e o número do item à esquerda."""
import sys, os
from PIL import Image, ImageDraw, ImageFont
B, lista, saida = sys.argv[1], sys.argv[2], sys.argv[3]
N = int(sys.argv[4]) if len(sys.argv) > 4 else 10
itens = [l.rstrip('\n').split('\t') for l in open(lista, encoding='utf-8') if l.strip()]
try:
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
except Exception:
    fonte = ImageFont.load_default()
cache = {}
def pagina(p):
    if p not in cache:
        cache.clear(); cache[p] = Image.open(f'{B}/pag/p{p}-{p}.png').convert('RGB')
    return cache[p]
recs = []
for it in itens:
    iid, ref, pers, leit, pag, bb = it[:6]
    if not pag or not bb: continue
    x0, y0, x1, y1 = map(int, bb.split(','))
    img = pagina(pag)
    W = img.width
    cx0, cx1 = max(0, x0 - 420), min(W, x1 + 420)
    c = img.crop((cx0, max(0, y0 - 55), cx1, min(img.height, y1 + 55))).copy()
    d = ImageDraw.Draw(c)
    d.rectangle((x0 - cx0 - 4, 55 - 4 if y0 >= 55 else y0 - 4, x1 - cx0 + 4, (55 if y0 >= 55 else y0) + (y1 - y0) + 4), outline=(220, 0, 0), width=3)
    rot = Image.new('RGB', (c.width + 90, c.height), 'white'); rot.paste(c, (90, 0))
    ImageDraw.Draw(rot).text((5, c.height // 2 - 14), iid, fill=(0, 0, 200), font=fonte)
    recs.append(rot)
for k in range(0, len(recs), N):
    grupo = recs[k:k + N]
    W = max(r.width for r in grupo); H = sum(r.height + 8 for r in grupo)
    p = Image.new('RGB', (W, H), (200, 200, 200)); y = 0
    for r in grupo:
        p.paste(r, (0, y)); y += r.height + 8
    p.save(f'{saida}-{k // N + 1:02d}.png')
print(len(recs), 'recortes,', (len(recs) + N - 1) // N, 'pranchas')
