"""Insônia — acha as palavras em itálico no fac-símile de 1947 pela inclinação das letras.

  python3 edicoes/insonia/italico.py            (grava ferramentas/cache/insonia/relatorios/italico.tsv)

Nenhum testemunho marca itálico (só há OCR). Para cada palavra do Tesseract (tess-bbm8412/), o recorte
da palavra se inclina de volta por vários ângulos, e vale o ângulo em que as colunas de tinta ficam
mais nítidas (a projeção vertical mais concentrada). Letra de pé dá ângulo perto de zero; itálico,
uns 0,2 (12°). Saem as sequências de palavras inclinadas, com o contexto, para conferir nas imagens
(conferir.py) e pôr em config.ITALICOS.
"""
import csv
import glob
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'insonia')
PDF = 'bbm8412'
ANGULOS = np.arange(-0.15, 0.46, 0.05)


def inclinacao(img):
    """img: matriz 0..255 da palavra. Devolve o ângulo (tangente) de maior nitidez."""
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


def paginas():
    out = []
    for f in sorted(glob.glob(os.path.join(CACHE, 'tess-' + PDF, '*.tsv')), key=lambda f: int(os.path.basename(f)[:-4])):
        n = int(os.path.basename(f)[:-4])
        if not os.path.exists(f[:-4] + '.json'):          # página ainda no Tesseract
            continue
        dx = json.load(open(f[:-4] + '.json'))['x']
        ws = []
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] == '5' and (r['text'] or '').strip():
                ws.append((int(r['block_num']), int(r['par_num']), int(r['line_num']), int(r['word_num']),
                           int(r['left']) + dx, int(r['top']), int(r['width']), int(r['height']), r['text']))
        out.append((n, sorted(ws)))
    return out


def pagina(args):
    n, ws = args
    png = os.path.join(CACHE, 'ver', f'_it{n}')
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '300', '-gray', '-png', '-singlefile',
                    os.path.join(CACHE, PDF + '.pdf'), png], check=True)
    im = np.array(Image.open(png + '.png').convert('L'))
    os.remove(png + '.png')
    res = []
    for b, p, l, w, x, y, ww, hh, t in ws:
        letras = sum(ch.isalpha() for ch in t)
        a = inclinacao(im[y:y + hh, x:x + ww]) if letras >= 3 else None
        res.append((n, (b, p, l), t, a))
    return res


if __name__ == '__main__':
    from multiprocessing import Pool
    os.makedirs(os.path.join(CACHE, 'ver'), exist_ok=True)
    with Pool(int(os.environ.get('PROCESSOS', '6'))) as pool:
        todas = [r for rs in pool.map(pagina, paginas()) for r in rs]
    # sequências de palavras inclinadas (as curtas, sem medida, entram se estão entre duas inclinadas)
    LIM = 0.15
    seqs, atual = [], []
    for i, (n, lin, t, a) in enumerate(todas):
        inclinada = a is not None and a >= LIM
        curta_no_meio = a is None and atual and i + 1 < len(todas) and (todas[i + 1][3] or 0) >= LIM
        if inclinada or curta_no_meio:
            atual.append(i)
        elif atual:
            seqs.append(atual); atual = []
    if atual:
        seqs.append(atual)
    arq = os.path.join(CACHE, 'relatorios', 'italico.tsv')
    os.makedirs(os.path.dirname(arq), exist_ok=True)
    with open(arq, 'w', encoding='utf-8') as f:
        for k, s in enumerate(seqs, 1):
            ini, fim = s[0], s[-1]
            ctx = ' '.join(todas[j][2] for j in range(max(0, ini - 3), min(len(todas), fim + 4)))
            italico = ' '.join(todas[j][2] for j in s)
            medias = [todas[j][3] for j in s if todas[j][3] is not None]
            f.write(f"{k}\t{italico}\t{todas[ini][0]}\t{sum(medias) / len(medias):.2f}\t{ctx}\n")
    medidas = [a for *_, a in todas if a is not None]
    print(len(todas), 'palavras;', len(seqs), 'sequências inclinadas em', arq)
    print('distribuição:', {round(float(a), 2): int(c) for a, c in zip(*np.unique(np.round(medidas, 2), return_counts=True))})
