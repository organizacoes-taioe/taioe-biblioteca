"""Vida do Padre José de Anchieta — OCR próprio (Tesseract) do fac-símile dos Annaes da Bibliotheca
Nacional, vol. XIX (1897), exemplar José Mindlin da Brasiliana USP (bbm/6953), pp. 1–49 (= páginas
5–53 do PDF: página impressa = página do PDF − 4).

  python3 edicoes/vida-de-anchieta/ocr.py [PASTA]

PASTA (padrão ~/.cache/claude-pedidos-0511/vida-de-anchieta) guarda dl/bbm6953.pdf; grava
pag/<n>.png (300 dpi, cinza), tess/<n>.txt (Tesseract, por) e pdf/<n>.txt (camada de texto do PDF).
Tesseract extraído sem sudo em ~/.cache/tesseract-local/raiz (ver edicoes/sao-bernardo/tesseract.py).
"""
import os
import subprocess
import sys
from multiprocessing import Pool

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/vida-de-anchieta')
PDF = os.path.join(PASTA, 'dl', 'bbm6953.pdf')
PAGINAS = range(7, 54)          # pp. 3–49 impressas
RAIZ = os.path.expanduser('~/.cache/tesseract-local/raiz')


def uma(n):
    for d in ('pag', 'tess', 'pdf'):
        os.makedirs(os.path.join(PASTA, d), exist_ok=True)
    png = os.path.join(PASTA, 'pag', str(n))
    if not os.path.exists(png + '.png'):
        subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '300', '-gray', '-png', '-singlefile', PDF, png], check=True)
    txt = os.path.join(PASTA, 'pdf', f'{n}.txt')
    if not os.path.exists(txt):
        subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), '-layout', PDF, txt], check=True)
    out = os.path.join(PASTA, 'tess', str(n))
    if not os.path.exists(out + '.txt'):
        env = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=os.path.join(RAIZ, 'usr/lib/x86_64-linux-gnu'),
                   TESSDATA_PREFIX=os.path.join(RAIZ, 'usr/share/tesseract-ocr/5/tessdata'))
        subprocess.run([os.path.join(RAIZ, 'usr/bin/tesseract'), png + '.png', out, '-l', 'por', '--psm', '4', 'txt', 'tsv'],
                       check=True, env=env, stderr=subprocess.DEVNULL)
    return n


if __name__ == '__main__':
    with Pool(6) as p:
        for n in p.imap_unordered(uma, PAGINAS):
            print(n, end=' ', flush=True)
    print()


def terceira(n):
    """Terceira leitura: 400 dpi, limiarizada (Pillow), --psm 6. Grava tess2/<n>.txt."""
    from PIL import Image
    os.makedirs(os.path.join(PASTA, 'tess2'), exist_ok=True)
    out = os.path.join(PASTA, 'tess2', str(n))
    if os.path.exists(out + '.txt'):
        return n
    png = out + '.png'
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '400', '-gray', '-png', '-singlefile', PDF, out], check=True)
    im = Image.open(png).point(lambda v: 255 if v > 150 else 0)
    im.save(png)
    env = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=os.path.join(RAIZ, 'usr/lib/x86_64-linux-gnu'),
               TESSDATA_PREFIX=os.path.join(RAIZ, 'usr/share/tesseract-ocr/5/tessdata'))
    subprocess.run([os.path.join(RAIZ, 'usr/bin/tesseract'), png, out, '-l', 'por', '--psm', '6', 'txt'],
                   check=True, env=env, stderr=subprocess.DEVNULL)
    os.remove(png)
    return n
