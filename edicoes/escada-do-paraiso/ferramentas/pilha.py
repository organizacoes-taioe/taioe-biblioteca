"""pilha.py saida.png escala folha:y0:y1[:lado] ... : recortes da coluna grega empilhados (lado e/d; padrão: pelo OCR)"""
import sys, json
from PIL import Image, ImageDraw
A = '/home/geremias/.cache/claude-pedidos-0511/escada-do-paraiso/'
L = {(p['folha']): p['ci'] for p in json.load(open(A + 'linhas.json', encoding='utf-8'))}
out, e = sys.argv[1], float(sys.argv[2])
ims = []
for arg in sys.argv[3:]:
    p = arg.split(':'); f, y0, y1 = int(p[0]), int(p[1]), int(p[2])
    d = json.load(open(A + 'ocr/%04d.json' % f)); g = d['gutter']
    im = Image.open(A + 'pag/%04d.png' % f)
    ci = {'e': 0, 'd': 1}[p[3]] if len(p) > 3 else L.get(f, 0)
    box = (0, y0, g + 40, y1) if ci == 0 else (g - 40, y0, im.width, y1)
    c = im.crop(box); c = c.resize((int(c.width * e), int(c.height * e)))
    ims.append((arg, c))
W = max(c.width for _, c in ims); H = sum(c.height + 22 for _, c in ims)
o = Image.new('L', (W, H), 255); dr = ImageDraw.Draw(o); y = 0
for a, c in ims:
    dr.text((4, y + 4), a, fill=0); o.paste(c, (0, y + 20)); y += c.height + 22
o.save(out)
