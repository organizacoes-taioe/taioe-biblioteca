"""recorte.py <saida.png> 'trecho 1' 'trecho 2' ... : recorta do fac-símile de Toronto (ia.pdf) as linhas
de cada trecho (achado pelas palavras do OCR do Internet Archive) e empilha os recortes numa imagem."""
import re, sys, unicodedata, html, subprocess, os
from PIL import Image, ImageDraw
C = '/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas/cache/minha-formacao/'
TMP = '/home/geremias/.cache/claude-pedidos-0511/minha-formacao/pag/'
os.makedirs(TMP, exist_ok=True)
def k(w):
    w = unicodedata.normalize('NFD', w.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in w if unicodedata.category(c) != 'Mn'))
s = open(C + 'ia_djvu.xml', encoding='utf-8').read()
P = []   # (chave, pag, x0, y0, x1, y1, W, H)
for n, obj in enumerate(re.findall(r'<OBJECT.*?</OBJECT>', s, re.S)):
    W = int(re.search(r'width="(\d+)"', obj).group(1)); H = int(re.search(r'height="(\d+)"', obj).group(1))
    for w in re.finditer(r'<WORD coords="(\d+),(\d+),(\d+),(\d+)[^"]*"[^>]*>(.*?)</WORD>', obj):
        x0, y1, x1, y0 = map(int, w.groups()[:4])
        for parte in re.split(r'[-—]', html.unescape(w.group(5))):
            if k(parte):
                P.append((k(parte), n, x0, y0, x1, y1, W, H))
chaves = [p[0] for p in P]
def achar(trecho):
    alvo = [k(x) for x in re.split(r'[\s\-—]+', trecho) if k(x)]
    for n in range(len(alvo), 1, -1):
        for ini in range(0, len(alvo) - n + 1):
            sub = alvo[ini:ini + n]
            ach = [i for i in range(len(chaves) - n) if chaves[i:i + n] == sub]
            if len(ach) == 1:
                return ach[0], n
    return None
def pagina(n):
    f = TMP + f'p{n + 1:03d}'
    if not os.path.exists(f + '.png'):
        subprocess.run(['pdftoppm', '-r', '200', '-f', str(n + 1), '-l', str(n + 1), '-png', '-singlefile',
                        C + 'ia.pdf', f], check=True)
    return Image.open(f + '.png')
saida, trechos = sys.argv[1], sys.argv[2:]
recs = []
for t in trechos:
    r = achar(t)
    if not r:
        im = Image.new('RGB', (900, 40), 'white'); ImageDraw.Draw(im).text((5, 10), 'NÃO ACHADO: ' + t, fill='red')
        recs.append(im); continue
    i, n = r
    ws = P[i:i + n]
    pg = ws[0][1]
    img = pagina(pg)
    sx = img.width / ws[0][6]; sy = img.height / ws[0][7]
    y0 = min(w[3] for w in ws if w[1] == pg); y1 = max(w[5] for w in ws if w[1] == pg)
    h = y1 - y0
    box = (0, max(0, int((y0 - 1.3 * h if h < 80 else y0 - 40) * sy)), img.width, min(img.height, int((y1 + 60) * sy)))
    c = img.crop(box)
    lab = Image.new('RGB', (c.width, 24), 'white'); ImageDraw.Draw(lab).text((5, 5), f'[{len(recs)+1}] p.{pg} {t}', fill='blue')
    recs.append(lab); recs.append(c)
W = max(r.width for r in recs); H = sum(r.height for r in recs)
out = Image.new('RGB', (W, H), 'white'); y = 0
for r in recs:
    out.paste(r, (0, y)); y += r.height
out.save(saida)
print(saida, W, H)
