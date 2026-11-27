"""Diário Íntimo — acha o itálico de 1956 que a transcrição de 2002 perdeu, pela inclinação das letras (cópia do
italico.py de Isaías Caminha).

  ~/.venvs/diagramador/bin/python3 -I edicoes/diario-intimo/italico.py <pasta tess> <saída.tsv>     (precisa de numpy)

Para cada palavra da nossa leitura de 1956, o recorte se inclina de volta por vários ângulos, e vale o ângulo em
que as colunas de tinta ficam mais nítidas: letra de pé dá perto de zero; itálico, uns 0,2. Saem as sequências de
palavras inclinadas em 1956 que não estão em itálico na transcrição de 2002: bloco, posição, palavras, ângulo médio,
contexto, lugar."""
import csv
import os
import re
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import colacao as C  # noqa: E402

ANGULOS = np.arange(-0.15, 0.46, 0.05)


def inclinacao(img):
    tinta = img < 128
    ys, xs = np.nonzero(tinta)
    if len(xs) < 40:
        return None
    ym = (ys.min() + ys.max()) / 2
    melhor, nit = None, -1
    for a in ANGULOS:
        xp = np.round(xs + a * (ys - ym)).astype(int)
        h = np.bincount(xp - xp.min())
        n = float((h.astype(float) ** 2).sum())
        if n > nit:
            melhor, nit = a, n
    return float(melhor)


def main(pasta, saida):
    CT = C.tokens_tess(pasta)
    ang, cache = [], {}
    for w, pg, x, y, ww, hh in CT:
        if pg not in cache:
            cache.clear()
            cache[pg] = np.array(Image.open(os.path.join(pasta, f'{pg}.png')).convert('L'))
        im = cache[pg]
        ang.append(inclinacao(im[y:y + hh, x:x + ww]) if sum(ch.isalpha() for ch in w) >= 3 else None)
    bl = C.blocos_bn()
    T = C.tokens_bn(bl)
    ital = []
    for blk, ini, fim, pal in T:
        b = bl[blk]
        ital.append(b[:ini].count('_') % 2 == 1)
    par, _ = C.alinhar([t[3] for t in T], [c[0] for c in CT])
    runs, atual = [], []
    for k, j in enumerate(par):
        a = ang[j] if j is not None else None
        inclinada = a is not None and a >= 0.15
        if inclinada and not ital[k]:
            atual.append(k)
        elif atual and not (a is None and not ital[k] and k + 1 < len(par) and par[k + 1] is not None
                            and (ang[par[k + 1]] or 0) >= 0.15):
            runs.append(atual)
            atual = []
        elif atual:
            atual.append(k)
    if atual:
        runs.append(atual)
    with open(saida, 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        for r in runs:
            k0, k1 = r[0], r[-1]
            ms = [ang[par[k]] for k in r if par[k] is not None and ang[par[k]] is not None]
            ctx = ' '.join(t[3] for t in T[max(0, k0 - 4):k0]) + ' [' + ' '.join(T[k][3] for k in r) + '] ' + \
                ' '.join(t[3] for t in T[k1 + 1:k1 + 4])
            c = CT[par[k0]]
            w.writerow([T[k0][0], T[k0][1], ' '.join(T[k][3] for k in r), f'{sum(ms) / len(ms):.2f}', ctx,
                        f'{c[1]}:{c[2]},{c[3]},{c[4]},{c[5]}'])
    print(len(runs), 'sequências em', saida)


if __name__ == '__main__':
    main(*sys.argv[1:3])
