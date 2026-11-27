"""Diário Íntimo (Lima Barreto) — OCR próprio (Tesseract) do fac-símile da edição de 1956 (Brasiliense, Obras de
Lima Barreto, vol. XIV), uma segunda leitura de 1956, independente da do Internet Archive.

  PROCESSOS=2 python3 edicoes/diario-intimo/tesseract.py <1956.pdf> <pasta de saída> [primeira-última]

Cada página vira <pasta>/<n>.tsv (palavras com coordenadas a 300 dpi) e <n>.png (a página em cinza, a 300 dpi,
que o italico.py e o conferir.py usam). Tesseract: o do Ubuntu, extraído em ~/.cache/tesseract-local/raiz
(variável TESSERACT_RAIZ). Rodar com teto: systemd-run --user --scope --slice=pesado.slice -q -- ...
"""
import os
import subprocess
import sys
from multiprocessing import Pool

DPI = 300


def _ambiente():
    raiz = os.environ.get('TESSERACT_RAIZ', os.path.expanduser('~/.cache/tesseract-local/raiz'))
    env = dict(os.environ, OMP_THREAD_LIMIT='1')
    exe = 'tesseract'
    if os.path.isdir(raiz):
        exe = os.path.join(raiz, 'usr', 'bin', 'tesseract')
        env['LD_LIBRARY_PATH'] = os.path.join(raiz, 'usr', 'lib', 'x86_64-linux-gnu')
        env['TESSDATA_PREFIX'] = os.path.join(raiz, 'usr', 'share', 'tesseract-ocr', '5', 'tessdata')
    return exe, env


def pagina(args):
    pdf, n, pasta = args
    tsv = os.path.join(pasta, f'{n}.tsv')
    png = os.path.join(pasta, f'{n}')
    if os.path.exists(tsv):
        return n
    exe, env = _ambiente()
    if not os.path.exists(png + '.png'):
        subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-r', str(DPI), '-gray', '-png', '-singlefile', pdf, png],
                       check=True)
    subprocess.run([exe, png + '.png', os.path.join(pasta, str(n)), '-l', 'por', '--psm', os.environ.get('PSM', '6'), 'tsv'],
                   check=True, env=env, capture_output=True)
    return n


if __name__ == '__main__':
    pdf, pasta = sys.argv[1], sys.argv[2]
    a, b = map(int, (sys.argv[3] if len(sys.argv) > 3 else '1-310').split('-'))
    os.makedirs(pasta, exist_ok=True)
    tarefas = [(pdf, n, pasta) for n in range(a, b + 1)]
    with Pool(int(os.environ.get('PROCESSOS', '2'))) as p:
        for k, n in enumerate(p.imap_unordered(pagina, tarefas), 1):
            if k % 20 == 0:
                print(k, '/', len(tarefas), flush=True)
