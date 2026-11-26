"""Reinações de Narizinho: recortes do fac-símile para conferir leituras.

    python3 -I edicoes/reinacoes-de-narizinho/conferir.py <saida.png> <pagina>:<palavra> [<pagina>:<palavra> …]

Acha na página (PDF) a linha do Tesseract (tess/<n>.tsv) cuja palavra mais se parece com <palavra> e empilha
os recortes (a linha e as vizinhas), com o rótulo, num PNG.
"""
import os
import sys
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from comparar import IMG, TESS, TESS2, k, tess_palavras  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402


def achar(n, palavra):
    melhor = (0, None)
    for pasta in (TESS, TESS2):
        for w, cx, linha in tess_palavras(n, pasta) or []:
            r = SequenceMatcher(None, k(w), k(palavra)).ratio()
            if r > melhor[0]:
                melhor = (r, linha)
    return melhor[1]


def main():
    saida, pedidos = sys.argv[1], sys.argv[2:]
    fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
    recs = []
    for p in pedidos:
        n, w = p.split(':', 1)
        n = int(n)
        im = Image.open(os.path.join(IMG, f'{n:03d}.jpg')).convert('L')
        cx = achar(n, w)
        if cx:
            rec = im.crop((0, max(0, cx[1] - 110), im.size[0], min(im.size[1], cx[3] + 110)))
        else:
            rec = im.resize((im.size[0] // 3, im.size[1] // 3))
        rec = rec.resize((rec.size[0] * 2 // 3, rec.size[1] * 2 // 3))
        cab = Image.new('L', (rec.size[0], 36), 255)
        ImageDraw.Draw(cab).text((8, 4), f'p{n}: {w}', font=fonte, fill=0)
        recs += [cab, rec]
    W = max(r.size[0] for r in recs)
    tela = Image.new('L', (W, sum(r.size[1] + 4 for r in recs)), 200)
    y = 0
    for r in recs:
        tela.paste(r, (0, y)); y += r.size[1] + 4
    tela.save(saida)


if __name__ == '__main__':
    main()
