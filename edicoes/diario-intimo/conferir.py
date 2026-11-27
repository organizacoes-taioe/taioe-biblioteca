"""Diário Íntimo — pranchas para conferir nas imagens de 1956 os pontos da colação.

  python3 -I edicoes/diario-intimo/conferir.py <pontos.tsv> <pasta tess> <pasta de saída> [por prancha]

pontos.tsv: id, página:x,y,largura,altura (da nossa leitura, a 300 dpi), rótulo. Cada ponto vira um recorte de três
linhas da página, com o rótulo em cima; as pranchas saem como p001.png, p002.png…"""
import csv
import os
import sys

from PIL import Image, ImageDraw, ImageFont

FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def main(pontos, pasta, saida, n=8):
    os.makedirs(saida, exist_ok=True)
    fonte = ImageFont.truetype(FONTE, 26) if os.path.exists(FONTE) else ImageFont.load_default()
    linhas = [c for c in csv.reader(open(pontos, encoding='utf-8'), delimiter='\t') if c and not c[0].startswith('#')]
    cache = {}
    for k in range(0, len(linhas), n):
        recortes = []
        for pid, loc, rotulo in linhas[k:k + n]:
            pg, caixa = loc.split(':')
            x, y, w, h = map(int, caixa.split(','))
            if pg not in cache:
                cache.clear()
                cache[pg] = Image.open(os.path.join(pasta, pg + '.png')).convert('L')
            im = cache[pg]
            r = im.crop((max(0, x - 900), max(0, y - 75), min(im.width, x + w + 900), min(im.height, y + h + 75)))
            r = r.resize((r.width // 2, r.height // 2))
            fundo = Image.new('L', (1050, r.height + 40), 255)
            ImageDraw.Draw(fundo).text((5, 5), f'{pid}  p.{pg}  {rotulo}'[:90], font=fonte, fill=0)
            fundo.paste(r, (0, 40))
            d = ImageDraw.Draw(fundo)
            cx = (x - max(0, x - 900)) // 2
            d.rectangle((cx - 3, 40 + (y - max(0, y - 75)) // 2 - 3, cx + w // 2 + 3, 40 + (y - max(0, y - 75) + h) // 2 + 3), outline=0)
            recortes.append(fundo)
        alt = sum(r.height for r in recortes) + 10 * len(recortes)
        pr = Image.new('L', (1050, alt), 200)
        yy = 0
        for r in recortes:
            pr.paste(r, (0, yy))
            yy += r.height + 10
        pr.save(os.path.join(saida, f'p{k // n + 1:03d}.png'))
    print(len(linhas), 'pontos em', (len(linhas) + n - 1) // n, 'pranchas')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 8)
