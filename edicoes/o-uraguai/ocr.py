"""uso: ocr.py <pdf> <pasta-saida> [primeira última]: renderiza cada página (pdftoppm, 400 dpi, cinza) e roda o Tesseract (por), 2 processos."""
import os, subprocess, sys
from multiprocessing.pool import ThreadPool as Pool
pdf, out = sys.argv[1], sys.argv[2]
a, b = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1, 999)
os.makedirs(out, exist_ok=True)
R = os.path.expanduser('~/.cache/tesseract-local/raiz')
env = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=R + '/usr/lib/x86_64-linux-gnu', TESSDATA_PREFIX=R + '/usr/share/tesseract-ocr/5/tessdata')
n = int([l for l in subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout.split('\n') if l.startswith('Pages')][0].split()[1])
def um(p):
    img = os.path.join(out, '%03d' % p)
    if os.path.exists(img + '.txt'): return
    subprocess.run(['pdftoppm', '-f', str(p), '-l', str(p), '-r', '400', '-gray', '-singlefile', pdf, img], check=True)
    subprocess.run([R + '/usr/bin/tesseract', img + '.pgm', img, '-l', 'por', '--psm', '4', 'txt', 'tsv'], env=env, capture_output=True)
    from PIL import Image; im = Image.open(img + '.pgm'); im.save(img + '.jpg', quality=85)
    os.remove(img + '.pgm')
with Pool(2) as pool:
    pool.map(um, range(max(1, a), min(n, b) + 1))
