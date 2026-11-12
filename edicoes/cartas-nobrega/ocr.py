"""Cartas do Brasil de Nóbrega — OCR próprio (Tesseract) do fac-símile da edição de 1886 (Imprensa Nacional,
Cartas Jesuíticas I), exemplar da Brasiliana USP (bbm/8016). O PDF tem camada de texto em máscara
JBIG2 de 900 dpi: extraímos a máscara (pdfimages) e lemos a 450 dpi (A, psm 4, com TSV) e a 600 dpi (B, psm 6).
Página impressa = página do PDF − 16. Letras: PDF 62–200.

  python3 -I edicoes/cartas-nobrega/ocr.py [PASTA]

Grava pag/<n>.png (máscara 450 dpi), tess/<n>.txt+tsv (A), tess2/<n>.txt (B) e pdf/<n>.txt (camada de texto do PDF, C).
Tesseract extraído sem sudo em ~/.cache/tesseract-local/raiz (ver edicoes/sao-bernardo/tesseract.py).
"""
import os
import subprocess
import sys
import tempfile
from multiprocessing import Pool

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-nobrega')
PDF = os.path.join(PASTA, 'dl', 'bbm8016.pdf')
PAGINAS = range(62, 201)
RAIZ = os.path.expanduser('~/.cache/tesseract-local/raiz')
ENV = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=os.path.join(RAIZ, 'usr/lib/x86_64-linux-gnu'),
           TESSDATA_PREFIX=os.path.join(RAIZ, 'usr/share/tesseract-ocr/5/tessdata'))
TESS = os.path.join(RAIZ, 'usr/bin/tesseract')


def uma(n):
    for d in ('pag', 'tess', 'tess2', 'pdf'):
        os.makedirs(os.path.join(PASTA, d), exist_ok=True)
    png = os.path.join(PASTA, 'pag', f'{n}.png')
    if not os.path.exists(png):
        with tempfile.TemporaryDirectory() as t:
            subprocess.run(['pdfimages', '-png', '-f', str(n), '-l', str(n), PDF, os.path.join(t, 'x')],
                           check=True, stderr=subprocess.DEVNULL)
            m = max((os.path.join(t, f) for f in os.listdir(t)), key=os.path.getsize)
            # a máscara é a imagem de 1 bit, a maior em pixels
            cand = [os.path.join(t, f) for f in os.listdir(t)]
            m = max(cand, key=lambda f: Image.open(f).size[0])
            im = Image.open(m).convert('L')
            im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(png)
            im.resize((im.width * 2 // 3, im.height * 2 // 3), Image.LANCZOS).save(png.replace('.png', '_600.png'))
    txt = os.path.join(PASTA, 'pdf', f'{n}.txt')
    if not os.path.exists(txt):
        subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), '-layout', PDF, txt], check=True, stderr=subprocess.DEVNULL)
    out = os.path.join(PASTA, 'tess', str(n))
    if not os.path.exists(out + '.txt'):
        subprocess.run([TESS, png, out, '-l', 'por', '--psm', '4', 'txt', 'tsv'], check=True, env=ENV, stderr=subprocess.DEVNULL)
    out2 = os.path.join(PASTA, 'tess2', str(n))
    if not os.path.exists(out2 + '.txt'):
        subprocess.run([TESS, png.replace('.png', '_600.png'), out2, '-l', 'por', '--psm', '6', 'txt'], check=True, env=ENV, stderr=subprocess.DEVNULL)
    return n


if __name__ == '__main__':
    with Pool(7) as p:
        for n in p.imap_unordered(uma, PAGINAS):
            print(n, end=' ', flush=True)
    print()
