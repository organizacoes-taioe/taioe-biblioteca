"""Caetés — recortes do fac-símile para conferir leituras duvidosas.

  python3 edicoes/caetes/conferir.py <arquivo.tsv> [bbm8819|bbm8374]

O arquivo tem uma linha por ponto: número, trecho a procurar (umas quatro palavras do texto, na
grafia de 1947 ou de hoje) e, opcional, uma nota. Os recortes (a linha achada, com as vizinhas)
saem numerados, empilhados de 8 em 8, em ferramentas/cache/caetes/ver/<arquivo>-<n>.png.
O trecho é achado pelas palavras do Tesseract (tess-<pdf>/), sem acentos nem maiúsculas.
"""
import csv
import glob
import json
import os
import re
import subprocess
import sys
import unicodedata

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'caetes')


def _k(w):
    w = unicodedata.normalize('NFD', w.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(ch for ch in w if unicodedata.category(ch) != 'Mn'))


_PAL = {}
_IDX = {}


def palavras(nome):
    """[(chave, pagina, x0, y0, x1, y1)] em pixels da página inteira a 300 dpi, na ordem de leitura."""
    if nome in _PAL:
        return _PAL[nome]
    out = []
    pasta = os.path.join(CACHE, 'tess-' + nome)
    for f in sorted(glob.glob(os.path.join(pasta, '*.tsv')), key=lambda f: int(os.path.basename(f)[:-4])):
        n = int(os.path.basename(f)[:-4])
        dx = json.load(open(f[:-4] + '.json'))['x']
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] == '5' and (r['text'] or '').strip():
                k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
                x, y, w, h = (int(r[c]) for c in ('left', 'top', 'width', 'height'))
                linhas.setdefault(k, []).append((x + dx, y, x + dx + w, y + h, r['text']))
        for k in sorted(linhas, key=lambda k: min(p[1] for p in linhas[k])):
            for x0, y0, x1, y1, t in sorted(linhas[k]):
                for parte in re.split(r'[-—]', t):
                    if _k(parte):
                        out.append((_k(parte), n, x0, y0, x1, y1, dx))
    _PAL[nome] = out
    return out


def achar(nome, trecho):
    """(pagina, caixa) do trecho; a correspondência mais longa a partir do começo do trecho."""
    alvo = [_k(p) for p in re.split(r'[\s\-—]+', trecho) if _k(p)]
    P = palavras(nome)
    chaves = [p[0] for p in P]
    if nome not in _IDX:
        idx = {}
        for i, c in enumerate(chaves):
            idx.setdefault(c, []).append(i)
        _IDX[nome] = idx
    idx = _IDX[nome]
    melhor = None
    for n in range(len(alvo), 1, -1):
        for ini in range(0, len(alvo) - n + 1):
            sub = alvo[ini:ini + n]
            achados = [i for i in idx.get(sub[0], []) if chaves[i:i + n] == sub]
            if len(achados) == 1:
                melhor = (achados[0], n)
                break
        if melhor:
            break
    if not melhor:
        return None
    i, n = melhor
    ws = [p for p in P[i:i + n] if p[1] == P[i][1]]
    return P[i][1], (min(p[2] for p in ws), min(p[3] for p in ws), max(p[4] for p in ws), max(p[5] for p in ws)), P[i][6]


def pagina_png(nome, pagina):
    """A página inteira a 300 dpi, em cinza, renderizada uma vez só (ver/pag/)."""
    pasta = os.path.join(CACHE, 'ver', 'pag')
    os.makedirs(pasta, exist_ok=True)
    png = os.path.join(pasta, f'{nome}-{pagina}')
    if not os.path.exists(png + '.png'):
        subprocess.run(['pdftoppm', '-f', str(pagina), '-l', str(pagina), '-r', '300', '-gray', '-png', '-singlefile',
                        os.path.join(CACHE, nome + '.pdf'), png], check=True)
    return png + '.png'


def recorte(nome, pagina, caixa, dx=0, acima=110, abaixo=110):
    x0, y0, x1, y1 = caixa
    pag = Image.open(pagina_png(nome, pagina)).convert('L')
    X0 = max(0, dx - 40)
    oy = max(0, y0 - acima)
    im = pag.crop((X0, oy, X0 + 1850, y1 + abaixo))
    # sublinha o trecho achado
    d = ImageDraw.Draw(im)
    d.rectangle([x0 - X0 - 4, y0 - oy - 4, x1 - X0 + 4, y1 - oy + 6], outline=0, width=3)
    return im


def montar(itens, nome, saida):
    """itens: [(rótulo, trecho)]. Grava as pranchas e devolve [(rótulo, página ou None)]."""
    res, pranchas, atual = [], [], []
    for rot, trecho in itens:
        a = achar(nome, trecho)
        res.append((rot, a[0] if a else None))
        if not a:
            continue
        im = recorte(nome, *a)
        im = im.resize((im.width // 2, im.height // 2))
        atual.append((rot, a[0], im))
        if len(atual) == 10:
            pranchas.append(atual); atual = []
    if atual:
        pranchas.append(atual)
    arquivos = []
    for k, pr in enumerate(pranchas, 1):
        w = max(im.width for _, _, im in pr) + 90
        h = sum(im.height + 8 for _, _, im in pr)
        folha = Image.new('L', (w, h), 255)
        d = ImageDraw.Draw(folha)
        y = 0
        for rot, pag, im in pr:
            folha.paste(im, (90, y))
            d.text((4, y + im.height // 2 - 12), f'{rot}', fill=0, font_size=26)
            d.text((4, y + im.height // 2 + 16), f'p{pag}', fill=90, font_size=16)
            d.line([0, y + im.height + 4, w, y + im.height + 4], fill=160, width=1)
            y += im.height + 8
        arq = f'{saida}-{k}.png'
        folha.save(arq)
        arquivos.append(arq)
    return res, arquivos


if __name__ == '__main__':
    entrada = sys.argv[1]
    nome = sys.argv[2] if len(sys.argv) > 2 else 'bbm8819'
    itens = [(l[0], l[1]) for l in csv.reader(open(entrada, encoding='utf-8'), delimiter='\t') if len(l) >= 2]
    base = os.path.join(CACHE, 'ver', os.path.splitext(os.path.basename(entrada))[0] + '-' + nome[-4:])
    res, arqs = montar(itens, nome, base)
    for rot, pag in res:
        if pag is None:
            print('não achado:', rot)
    print('\n'.join(arqs))
