"""Vida de D. Frei Bertolameu dos Mártires — pranchas para a conferência nas imagens de 1619 (BNP).

  python3 -I edicoes/vida-de-frei-bartolomeu/pranchas.py <lista.tsv> <pasta-de-saída> [por-prancha]

lista.tsv: id <TAB> chave da unidade (u123 / v123) <TAB> contexto (texto com a palavra entre ⟦ ⟧) <TAB> leituras.
Grava <saída>/prancha-NNN.png (recortes da linha, com a palavra em vermelho, e o número do item) e
<saída>/prancha-NNN.txt (os itens dessa prancha: número, contexto e leituras).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import testemunhos as T  # noqa: E402

LARG = 1400


def caixa_da_unidade(ref, voto_por_u, chave):
    x = voto_por_u[chave]
    i = x['i']
    ws = [ref[k] for k in range(i, i + max(1, x.get('n', 1))) if k < len(ref)]
    if chave.startswith('v'):                       # vão antes da palavra i: entre a anterior e ela
        ws = [ref[k] for k in (i - 1, i) if 0 <= k < len(ref)]
    w0 = ws[0]
    ws = [w for w in ws if w['p'] == w0['p'] and w.get('c') == w0.get('c')]
    return w0['p'], min(w['x0'] for w in ws), min(w['y0'] for w in ws), max(w['x1'] for w in ws), max(w['y1'] for w in ws)


def main():
    lista, saida = sys.argv[1], sys.argv[2]
    por = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    os.makedirs(saida, exist_ok=True)
    ref = json.load(open(os.path.join(T.PASTA, 'colacao', 'bnp.json')))['palavras']
    voto = json.load(open(os.path.join(T.PASTA, 'voto.json')))
    voto_por_u = {('v' if x.get('vao') else 'u') + str(x['u']): x for x in voto}
    itens = [l.rstrip('\n').split('\t') for l in open(lista, encoding='utf-8') if l.strip() and not l.startswith('#')]
    try:
        fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 34)
    except OSError:
        fonte = ImageFont.load_default()
    cache = {}
    for k0 in range(0, len(itens), por):
        grupo = itens[k0:k0 + por]
        recortes, textos = [], []
        for it in grupo:
            iid, chave = it[0], it[1]
            p, x0, y0, x1, y1 = caixa_da_unidade(ref, voto_por_u, chave)
            if p not in cache:
                if len(cache) > 6:
                    cache.clear()
                cache[p] = Image.open(os.path.join(T.PASTA, 'pag', f'{p}.png')).convert('RGB')
            im = cache[p]
            h = y1 - y0
            cx0 = max(0, x0 - 520)
            cx1 = min(im.size[0], x1 + 520)
            cy0 = max(0, y0 - int(1.6 * h) - 10)
            cy1 = min(im.size[1], y1 + int(1.6 * h) + 10)
            rec = im.crop((cx0, cy0, cx1, cy1)).copy()
            d = ImageDraw.Draw(rec)
            d.rectangle((x0 - cx0 - 4, y0 - cy0 - 4, x1 - cx0 + 4, y1 - cy0 + 4), outline=(220, 0, 0), width=4)
            fundo = Image.new('RGB', (LARG, rec.size[1] + 50), 'white')
            fundo.paste(rec, (0, 46))
            ImageDraw.Draw(fundo).text((6, 4), f'[{iid}]  p. {p}', fill=(0, 0, 200), font=fonte)
            recortes.append(fundo)
            textos.append('\t'.join(it[:1] + it[2:]))
        alt = sum(r.size[1] + 8 for r in recortes)
        prancha = Image.new('RGB', (LARG, alt), (235, 235, 235))
        y = 0
        for r in recortes:
            prancha.paste(r, (0, y))
            y += r.size[1] + 8
        n = k0 // por + 1
        prancha.thumbnail((LARG * 3 // 4, 20000))
        prancha.save(os.path.join(saida, f'prancha-{n:03d}.png'))
        open(os.path.join(saida, f'prancha-{n:03d}.txt'), 'w', encoding='utf-8').write('\n'.join(textos) + '\n')
    print(len(itens), 'itens')


if __name__ == '__main__':
    main()
