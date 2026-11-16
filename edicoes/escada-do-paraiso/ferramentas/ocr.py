"""OCR das duas colunas de uma página da PG 88 com o Tesseract grc. Uso: ocr.py <png> <saida.json>
Grava {'gutter': x, 'cols': [ [linha…], [linha…] ]}, linha = {'y','x0','x1','h','words':[[texto,conf,x0,y0,x1,y1]]}"""
import sys, os, json, subprocess, tempfile
from PIL import Image
R = os.path.expanduser('~/.cache/tesseract-local/raiz')
ENV = dict(os.environ, LD_LIBRARY_PATH=R + '/usr/lib/x86_64-linux-gnu', TESSDATA_PREFIX=R + '/usr/share/tesseract-ocr/5/tessdata', OMP_THREAD_LIMIT='1')
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
px = im.load()
# calha: coluna de menor tinta entre 40% e 60% da largura, nas linhas 10%–90%
y0, y1 = int(h * .10), int(h * .90)
small = im.resize((w // 4, h // 4))
sp = small.load(); sw, sh = small.size
dens = []
for x in range(int(sw * .40), int(sw * .60)):
    dens.append((sum(1 for y in range(sh // 10, sh * 9 // 10, 2) if sp[x, y] < 110), x))
# suaviza
best = min((sum(d for d, _ in dens[i:i + 5]), dens[i + 2][1]) for i in range(len(dens) - 5))
g = best[1] * 4
out = {'gutter': g, 'size': [w, h], 'cols': []}
for (a, b) in ((0, g), (g, w)):
    crop = im.crop((a, 0, b, h))
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'c.png'); crop.save(p)
        r = subprocess.run([R + '/usr/bin/tesseract', p, os.path.join(td, 'o'), '-l', 'grc', '--psm', '4', 'tsv'], env=ENV, capture_output=True)
        rows = open(os.path.join(td, 'o.tsv'), encoding='utf-8').read().split('\n')[1:]
    lines = {}
    for r in rows:
        f = r.split('\t')
        if len(f) < 12 or f[0] != '5' or not f[11].strip(): continue
        key = (int(f[2]), int(f[3]), int(f[4]))
        L, T, W, H = map(int, f[6:10])
        lines.setdefault(key, []).append([f[11], float(f[10]), L + a, T, L + a + W, T + H])
    col = []
    for k in sorted(lines, key=lambda k: min(wd[3] for wd in lines[k])):
        ws = lines[k]
        col.append({'y': min(x[3] for x in ws), 'y1': max(x[5] for x in ws), 'x0': min(x[2] for x in ws), 'x1': max(x[4] for x in ws), 'words': ws})
    out['cols'].append(col)
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
