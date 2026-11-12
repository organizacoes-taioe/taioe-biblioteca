"""Cartas de Anchieta — OCR próprio (Tesseract) do fac-símile de 1933 (Internet Archive, ver pecas.py).

  python3 edicoes/cartas-anchieta/ocr.py [PASTA]

PASTA (padrão ~/.cache/claude-pedidos-0511/cartas-anchieta) guarda dl/jp2/<item>_jp2/<item>_NNNN.jp2 (o
`_jp2.zip` do item, descompactado) e dl/ia_djvu.xml (a leitura do próprio IA). Grava, por folha:
png/<f>.png (2×, cinza), tess/<f>.tsv e .txt (psm 4) e tess2/<f>.txt (2×, limiarizada, psm 6).
Tesseract extraído sem sudo em ~/.cache/tesseract-local/raiz (ver edicoes/sao-bernardo/tesseract.py).
"""
import os
import subprocess
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pecas  # noqa: E402

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-anchieta')
RAIZ = os.path.expanduser('~/.cache/tesseract-local/raiz')
ENV = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=os.path.join(RAIZ, 'usr/lib/x86_64-linux-gnu'),
           TESSDATA_PREFIX=os.path.join(RAIZ, 'usr/share/tesseract-ocr/5/tessdata'))


def jp2(f):
    return os.path.join(PASTA, 'dl', 'jp2', pecas.ITEM + '_jp2', f'{pecas.ITEM}_{f:04d}.jp2')


def uma(f):
    from PIL import Image
    for d in ('png', 'tess', 'tess2'):
        os.makedirs(os.path.join(PASTA, d), exist_ok=True)
    png = os.path.join(PASTA, 'png', f'{f}.png')
    if not os.path.exists(png):
        im = Image.open(jp2(f)).convert('L')
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
        im.save(png)
    out = os.path.join(PASTA, 'tess', str(f))
    if not os.path.exists(out + '.tsv'):
        subprocess.run([os.path.join(RAIZ, 'usr/bin/tesseract'), png, out, '-l', 'por', '--psm', '4', 'txt', 'tsv'],
                       check=True, env=ENV, stderr=subprocess.DEVNULL)
    out2 = os.path.join(PASTA, 'tess2', str(f))
    if not os.path.exists(out2 + '.txt'):
        b = out2 + '.png'
        Image.open(png).point(lambda v: 255 if v > 140 else 0).save(b)
        subprocess.run([os.path.join(RAIZ, 'usr/bin/tesseract'), b, out2, '-l', 'por', '--psm', '6', 'txt'],
                       check=True, env=ENV, stderr=subprocess.DEVNULL)
        os.remove(b)
    return f


def ia():
    """A leitura do IA (Tesseract 5.3 deles), uma folha por arquivo: ia/<f>.txt."""
    import xml.etree.ElementTree as ET
    os.makedirs(os.path.join(PASTA, 'ia'), exist_ok=True)
    root = ET.parse(os.path.join(PASTA, 'dl', 'ia_djvu.xml')).getroot()
    for i, obj in enumerate(root.iter('OBJECT')):
        linhas = [' '.join((w.text or '') for w in line.iter('WORD')) for line in obj.iter('LINE')]
        open(os.path.join(PASTA, 'ia', f'{i}.txt'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')


if __name__ == '__main__':
    ia()
    with Pool(7) as p:
        for f in p.imap_unordered(uma, list(pecas.folhas())):
            print(f, end=' ', flush=True)
    print()
