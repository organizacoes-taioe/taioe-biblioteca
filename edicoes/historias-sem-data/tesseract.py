"""Histórias sem Data — OCR próprio (Tesseract) do exemplar de Toronto (Internet Archive), um
testemunho independente da camada de texto do PDF.

  python3 edicoes/historias-sem-data/tesseract.py

Cada página do PDF (ferramentas/cache/historias-sem-data/ia_toronto.pdf) vira tess/<nnn>.txt, a
300 dpi, em cinza, `-l por --psm 6`. O Tesseract é o do Ubuntu, extraído sem sudo em
~/.cache/tesseract-local/raiz (variável TESSERACT_RAIZ); ver edicoes/sao-bernardo/tesseract.py.
Threads, não processos: o forkserver do Python 3.14 falha no sandbox.
"""
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', 'historias-sem-data')
PDF = os.path.join(CACHE, 'ia_toronto.pdf')
OUT = os.path.join(CACHE, 'tess')
RAIZ = os.environ.get('TESSERACT_RAIZ', os.path.expanduser('~/.cache/tesseract-local/raiz'))
ENV = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=f'{RAIZ}/usr/lib/x86_64-linux-gnu',
           TESSDATA_PREFIX=f'{RAIZ}/usr/share/tesseract-ocr/5/tessdata')


def pagina(n):
    txt = os.path.join(OUT, f'{n:03d}')
    if os.path.exists(txt + '.txt'):
        return
    png = os.path.join(OUT, f'_{n:03d}')
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', '300', '-gray', '-png', '-singlefile', PDF, png],
                   check=True)
    subprocess.run([f'{RAIZ}/usr/bin/tesseract', png + '.png', txt, '-l', 'por', '--psm', '6'], env=ENV,
                   check=True, stderr=subprocess.DEVNULL)
    os.remove(png + '.png')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    paginas = int(subprocess.run(['pdfinfo', PDF], capture_output=True, text=True).stdout.split('Pages:')[1].split()[0])
    with ThreadPoolExecutor(7) as p:
        list(p.map(pagina, range(1, paginas + 1)))
    print('ok')
