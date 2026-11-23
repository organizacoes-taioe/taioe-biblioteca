"""Linhas de texto de uma página: da camada do PDF (pdftotext -bbox) ou do TSV do Tesseract.
Cada linha: (y, x0, texto). Agrupa palavras por altura."""
import os, re, subprocess, html, csv
def _agrupar(pals, tol):
    pals.sort(key=lambda w: (w[1] + w[3]) / 2)
    linhas = []
    for w in pals:
        yc = (w[1] + w[3]) / 2
        if linhas and abs(linhas[-1]['yc'] - yc) < tol:
            linhas[-1]['w'].append(w); n = len(linhas[-1]['w']); linhas[-1]['yc'] += (yc - linhas[-1]['yc']) / n
        else:
            linhas.append({'yc': yc, 'w': [w]})
    out = []
    xs = sorted(min(w[0] for w in l['w']) for l in linhas)
    xmed = xs[len(xs) // 2] if xs else 0
    for l in linhas:
        ws = sorted(l['w'], key=lambda w: w[0])
        txt = ' '.join(w[4] for w in ws)
        if out and ws[0][0] > 2 * xmed and re.match(r'[a-zà-ÿ]', txt) and l['yc'] - out[-1][0] < 5 * tol:
            p = out[-1]; out[-1] = (p[0], p[1], p[2] + ' ' + txt, p[3] + ws); continue
        out.append((l['yc'], ws[0][0], txt, ws))
    return out
    for l in linhas:
        ws = sorted(l['w'], key=lambda w: w[0])
        out.append((l['yc'], ws[0][0], ' '.join(w[4] for w in ws), [w for w in ws]))
    return out
def pdf(pdfpath, pag):
    xml = subprocess.run(['pdftotext', '-f', str(pag), '-l', str(pag), '-bbox', pdfpath, '-'], capture_output=True, text=True).stdout
    pals = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in
            re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', xml)]
    return _agrupar(pals, 5)
def tess(tsvpath):
    pals = []
    for r in csv.DictReader(open(tsvpath), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['level'] == '5' and r['text'].strip():
            x, y, w, h = int(r['left']), int(r['top']), int(r['width']), int(r['height'])
            pals.append((x, y, x + w, y + h, r['text']))
    return _agrupar(pals, 25)
if __name__ == '__main__':
    import sys
    if sys.argv[1].endswith('.tsv'):
        ls = tess(sys.argv[1])
    else:
        ls = pdf(sys.argv[1], int(sys.argv[2]))
    for l in ls: print('%6.0f %5.0f | %s' % (l[0], l[1], l[2]))
