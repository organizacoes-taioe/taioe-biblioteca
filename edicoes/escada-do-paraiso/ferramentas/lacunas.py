"""Linhas que o Tesseract pulou: em cada coluna, todo vão maior que 1,6 entrelinha é relido sozinho (psm 6) e as
linhas achadas entram no OCR da página. Uso: lacunas.py <pasta de pngs> <pasta de json> [folhas…]"""
import sys, os, json, glob, subprocess, tempfile, statistics
from PIL import Image
R = os.path.expanduser('~/.cache/tesseract-local/raiz')
ENV = dict(os.environ, LD_LIBRARY_PATH=R + '/usr/lib/x86_64-linux-gnu', TESSDATA_PREFIX=R + '/usr/share/tesseract-ocr/5/tessdata', OMP_THREAD_LIMIT='1')
pngs, jsons = sys.argv[1], sys.argv[2]
arqs = sorted(glob.glob(os.path.join(jsons, '*.json')))
if len(sys.argv) > 3: arqs = [os.path.join(jsons, '%s.json' % a) for a in sys.argv[3:]]
novas_total = 0
for f in arqs:
    d = json.load(open(f, encoding='utf-8'))
    if d.get('lacunas') == 2: continue
    b = os.path.basename(f)[:-5]
    png = os.path.join(pngs, b + '.png')
    if not os.path.exists(png): png = os.path.join(pngs, 'u-' + b + '.png')
    im = Image.open(png).convert('L')
    w, h = im.size
    g = d['gutter']
    for ci, col in enumerate(d['cols']):
        col.sort(key=lambda l: l['y'])
        if len(col) < 6: continue
        alt = statistics.median(l['y1'] - l['y'] for l in col)
        pitch = statistics.median(col[i + 1]['y'] - col[i]['y'] for i in range(len(col) - 1))
        a, bb = (0, g) if ci == 0 else (g, w)
        novas = []
        for i in range(len(col) - 1):
            if col[i + 1]['y'] - col[i]['y'] < 1.35 * pitch: continue
            y0, y1 = min(col[i]['y1'], col[i]['y'] + int(alt)) + 2, col[i + 1]['y'] - 2
            if y1 - y0 < alt * .6: continue
            crop = im.crop((a, y0, bb, y1))
            with tempfile.TemporaryDirectory() as td:
                p = os.path.join(td, 'c.png'); crop.save(p)
                subprocess.run([R + '/usr/bin/tesseract', p, os.path.join(td, 'o'), '-l', 'grc', '--psm', '6', 'tsv'], env=ENV, capture_output=True)
                rows = open(os.path.join(td, 'o.tsv'), encoding='utf-8').read().split('\n')[1:]
            lines = {}
            for r in rows:
                q = r.split('\t')
                if len(q) < 12 or q[0] != '5' or not q[11].strip(): continue
                L, T, W, H = map(int, q[6:10])
                lines.setdefault((q[2], q[3], q[4]), []).append([q[11], float(q[10]), L + a, T + y0, L + a + W, T + y0 + H])
            for ws in lines.values():
                if sum(x[1] for x in ws) / len(ws) < 50: continue
                novas.append({'y': min(x[3] for x in ws), 'y1': max(x[5] for x in ws), 'x0': min(x[2] for x in ws),
                              'x1': max(x[4] for x in ws), 'words': ws, 'relida': True})
        if novas:
            col.extend(novas); col.sort(key=lambda l: l['y']); novas_total += len(novas)
    d['lacunas'] = 2
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False)
print('linhas novas', novas_total)
