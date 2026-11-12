"""Prepara a conferência nas imagens: ver/<p>.png (texto escuro em fundo claro, recortado, ~1500 px de largura) e
lotes de páginas com as linhas a conferir (relatorios/conferir.json) em ver/lote-NN.md (fora do git: ~/.cache)."""
import json
import os
import sys

from PIL import Image, ImageOps

Image.MAX_IMAGE_PIXELS = None
AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.expanduser('~/.cache/claude-pedidos-0511/cartas-nobrega')
POR_LOTE = int(sys.argv[1]) if len(sys.argv) > 1 else 14


def recorte(p):
    xs, ys, xe, ye = 10 ** 9, 10 ** 9, 0, 0
    for l in open(os.path.join(PASTA, 'tess', f'{p}.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c = l.split('\t')
        if len(c) >= 12 and c[0] == '5' and c[11].strip() and float(c[10]) > 30:
            x, y, w, h = map(int, c[6:10])
            xs, ys, xe, ye = min(xs, x), min(ys, y), max(xe, x + w), max(ye, y + h)
    return xs, ys, xe, ye


def main():
    conf = json.load(open(os.path.join(AQUI, 'relatorios', 'conferir.json')))
    os.makedirs(os.path.join(PASTA, 'ver'), exist_ok=True)
    pags = sorted(int(p) for p in conf)
    for p in pags:
        out = os.path.join(PASTA, 'ver', f'{p}.png')
        if os.path.exists(out):
            continue
        im = ImageOps.invert(Image.open(os.path.join(PASTA, 'pag', f'{p}.png')).convert('L'))
        xs, ys, xe, ye = recorte(p)
        im = im.crop((max(xs - 60, 0), max(ys - 60, 0), min(xe + 60, im.width), min(ye + 60, im.height)))
        w = 1500
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
        im.save(out)
    lotes = [pags[i:i + POR_LOTE] for i in range(0, len(pags), POR_LOTE)]
    for n, lote in enumerate(lotes, 1):
        linhas = []
        for p in lote:
            linhas.append(f'## página {p}  (imagem: {PASTA}/ver/{p}.png)')
            for x in conf[str(p)]:
                linhas.append(f'- k={x["k"]} | {x["linha"]} | suspeitas: {"; ".join(x["motivos"])}')
            linhas.append('')
        open(os.path.join(PASTA, 'ver', f'lote-{n:02d}.md'), 'w', encoding='utf-8').write('\n'.join(linhas))
    print(len(pags), 'páginas;', len(lotes), 'lotes')


main()
