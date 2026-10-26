"""Angústia — onde estão as anotações à mão nas provas de 1946 (bbm/8482).

  python3 edicoes/angustia/anotacoes.py          (grava relatorios/anotacoes.tsv e ver/anot-<pág>.png)

O OCR lê só o impresso; as correções do autor estão à mão, nas margens e entre as linhas. Para cada
página das provas: a coluna de texto vem das palavras do Tesseract (tess-bbm8482/); conta-se a tinta
nas margens (fora da coluna, sem a borda do papel) e se separam as manchas grandes. As páginas com
manchas saem numa lista e numa imagem reduzida, para ler as correções e conferi-las com 1947.
"""
import csv
import glob
import json
import os
import sys

import numpy as np
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'angustia')
PDF = 'bbm8482'


def coluna(n):
    """(x0, y0, x1, y1) do texto impresso da página, em pixels a 300 dpi."""
    f = os.path.join(CACHE, 'tess-' + PDF, f'{n}.tsv')
    if not os.path.exists(f):
        return None
    dx = json.load(open(f[:-4] + '.json'))['x']
    ws = [(int(r['left']) + dx, int(r['top']), int(r['left']) + dx + int(r['width']), int(r['top']) + int(r['height']))
          for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)
          if r['level'] == '5' and len((r['text'] or '').strip()) >= 3 and float(r['conf']) > 60]
    if len(ws) < 30:
        return None
    xs0 = sorted(w[0] for w in ws)
    xs1 = sorted(w[2] for w in ws)
    ys0 = sorted(w[1] for w in ws)
    ys1 = sorted(w[3] for w in ws)
    k = len(ws) // 50
    return xs0[k], ys0[k], xs1[-1 - k], ys1[-1 - k]


def tinta(n):
    png = os.path.join(CACHE, 'ver', 'pag', f'{PDF}-{n}.png')
    col = coluna(n)
    if col is None or not os.path.exists(png):
        return None
    im = np.array(Image.open(png).convert('L'))
    h, w = im.shape
    escuro = im < 110
    # a borda do papel e a sombra da lombada: 4% de cada lado fora
    bx, by = int(w * 0.04), int(h * 0.03)
    x0, y0, x1, y1 = col
    m = np.zeros_like(escuro)
    m[by:h - by, bx:max(bx, x0 - 25)] = True               # margem esquerda
    m[by:h - by, min(w - bx, x1 + 25):w - bx] = True        # margem direita
    m[by:max(by, y0 - 40), bx:w - bx] = True                # acima do cabeço
    m[min(h - by, y1 + 40):h - by, bx:w - bx] = True        # abaixo da última linha
    return int((escuro & m).sum()), col


def linhas(n):
    """Linhas impressas da página: [(y0, y1, x0, x1, texto)] em pixels a 300 dpi."""
    f = os.path.join(CACHE, 'tess-' + PDF, f'{n}.tsv')
    dx = json.load(open(f[:-4] + '.json'))['x']
    ls = {}
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['level'] == '5' and (r['text'] or '').strip():
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            x, y, w, h = (int(r[c]) for c in ('left', 'top', 'width', 'height'))
            ls.setdefault(k, []).append((x + dx, y, x + dx + w, y + h, r['text']))
    out = []
    for ws in ls.values():
        ws.sort()
        out.append((min(w[1] for w in ws), max(w[3] for w in ws), ws[0][0], ws[-1][2], ' '.join(w[4] for w in ws)))
    return sorted(out)


def marcas(n, largura=330):
    """Linhas com tinta na margem, à direita ou à esquerda: [(y0, y1, lado, tinta, texto)]."""
    col = coluna(n)
    png = os.path.join(CACHE, 'ver', 'pag', f'{PDF}-{n}.png')
    if col is None or not os.path.exists(png):
        return []
    im = np.array(Image.open(png).convert('L')).astype(int)
    x0, y0, x1, y1 = col
    papel = np.median(im[y0:y1, x0:x1])
    escuro = im < papel - 70
    out = []
    for ly0, ly1, lx0, lx1, t in linhas(n):
        if len(t) < 8:
            continue
        a, b = max(0, ly0 - 8), ly1 + 8
        dir_ = escuro[a:b, x1 + 30:x1 + largura].sum()
        esq = escuro[a:b, max(0, x0 - largura):x0 - 30].sum()
        for lado, v in (('d', dir_), ('e', esq)):
            if v > 150:
                out.append((ly0, ly1, lado, int(v), t))
    return out


if __name__ == '__main__' and sys.argv[1:2] == ['linhas']:
    from PIL import ImageDraw
    res = []
    for f in sorted(glob.glob(os.path.join(CACHE, 'ver', 'pag', PDF + '-*.png')),
                    key=lambda f: int(f.rsplit('-', 1)[1][:-4])):
        n = int(f.rsplit('-', 1)[1][:-4])
        for m in marcas(n):
            res.append((n,) + m)
    arq = os.path.join(CACHE, 'relatorios', 'marcas.tsv')
    with open(arq, 'w', encoding='utf-8') as fo:
        for r in res:
            fo.write('\t'.join(str(x) for x in r) + '\n')
    print(len(res), 'linhas com marca na margem em', arq)
    sys.exit()

if __name__ == '__main__':
    res = []
    for f in sorted(glob.glob(os.path.join(CACHE, 'ver', 'pag', PDF + '-*.png')),
                    key=lambda f: int(f.rsplit('-', 1)[1][:-4])):
        n = int(f.rsplit('-', 1)[1][:-4])
        t = tinta(n)
        if t:
            res.append((n, t[0]))
    vals = sorted(v for _, v in res)
    base = vals[len(vals) // 2]
    arq = os.path.join(CACHE, 'relatorios', 'anotacoes.tsv')
    with open(arq, 'w', encoding='utf-8') as fo:
        for n, v in res:
            fo.write(f'{n}\t{v}\t{v / max(base, 1):.1f}\n')
    print(len(res), 'páginas; mediana da tinta nas margens', base)
    print('acima de 3× a mediana:', [n for n, v in res if v > 3 * base])
