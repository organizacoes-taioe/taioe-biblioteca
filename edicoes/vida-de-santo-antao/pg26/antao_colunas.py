"""Recorta a coluna grega de cada folha da PG 26 (Vita Antonii) e a reconhece de novo com o Tesseract.
Usa o hOCR da página inteira (primeira passada) só para achar a geometria.
uso: python3 -I antao_colunas.py <pasta-folhas> <pasta-ocr> <saida>"""
import sys, os, re, html, subprocess
from PIL import Image
FOL, OCR, SAI = sys.argv[1:4]
R = os.path.expanduser('~/.cache/tesseract-local/raiz')
env = dict(os.environ, LD_LIBRARY_PATH=R + '/usr/lib/x86_64-linux-gnu', TESSDATA_PREFIX=R + '/usr/share/tesseract-ocr/5/tessdata', OMP_THREAD_LIMIT='2')
GREGO = re.compile(r'[Ͱ-Ͽἀ-῿]')
LAT = re.compile(r'[A-Za-z]')
os.makedirs(SAI, exist_ok=True)
def linhas_de(arq):
    s = open(arq, encoding='utf-8').read()
    out = []
    for lm in re.finditer(r"<span class='ocr_line'[^>]*title=\"bbox (\d+) (\d+) (\d+) (\d+);[^>]*>(.*?)</span>\s*</span>", s, re.S):
        ws = [html.unescape(re.sub(r'<[^>]+>', '', w)).strip() for w in re.findall(r"<span class='ocrx_word'[^>]*>(.*?)</span>", lm.group(5), re.S)]
        ws = [w for w in ws if w]
        if ws: out.append((tuple(map(int, lm.groups()[:4])), ws))
    return sorted(out, key=lambda x: x[0][1])
def razao_grego(ws):
    g = sum(1 for w in ws if GREGO.search(w)); l = sum(1 for w in ws if LAT.search(w) and not GREGO.search(w))
    return g / max(1, g + l)
def ocr(im, nome, psm):
    p = os.path.join(SAI, nome + '.png'); im.save(p)
    subprocess.run([R + '/usr/bin/tesseract', p, os.path.join(SAI, nome), '-l', 'grc', '--psm', str(psm)], env=env, capture_output=True)
    return open(os.path.join(SAI, nome + '.txt'), encoding='utf-8').read()
for arq in sorted(f for f in os.listdir(OCR) if f.endswith('.hocr')):
    b = arq[:4]
    if os.path.exists(os.path.join(SAI, b + '.grego.txt')): continue
    im = Image.open(os.path.join(FOL, b + '.jp2')).convert('L'); W, H = im.size; meio = W / 2
    ls = linhas_de(os.path.join(OCR, arq))
    corpo = [l for l in ls if l[0][1] > H * 0.07]
    # fim da zona de cima: a primeira linha larga em latim (Evágrio ou as notas)
    fim = H
    for bb, ws in corpo:
        if bb[2] - bb[0] > W * 0.7 and razao_grego(ws) < 0.3 and len(ws) >= 6: fim = bb[1]; break
    zona = [l for l in corpo if l[0][3] <= fim + 5]
    esq = sum(sum(1 for w in ws if GREGO.search(w)) for bb, ws in zona if bb[2] < meio + W * 0.05)
    dir_ = sum(sum(1 for w in ws if GREGO.search(w)) for bb, ws in zona if bb[0] > meio - W * 0.05)
    lado = 'e' if esq >= dir_ else 'd'
    largas = [l for l in zona if l[0][2] - l[0][0] > W * 0.7 and razao_grego(l[1]) >= 0.6]
    topo = min((bb[1] for bb, ws in zona), default=int(H * 0.07)) - 8
    x0, x1 = (int(W * 0.04), int(meio + 8)) if lado == 'e' else (int(meio - 8), int(W * 0.97))
    pedacos = []
    y = topo
    for bb, ws in largas:
        if bb[1] > y + 10:
            pedacos.append(('col', (x0, y, x1, bb[1] - 2)))
        pedacos.append(('larga', (int(W * 0.03), bb[1] - 6, int(W * 0.98), bb[3] + 6)))
        y = bb[3] + 6
    if fim > y + 10: pedacos.append(('col', (x0, y, x1, fim - 2)))
    txt = []
    for k, (tipo, cx) in enumerate(pedacos):
        txt.append(ocr(im.crop(cx), f'{b}-{k}', 6 if tipo == 'col' else 7))
    open(os.path.join(SAI, b + '.grego.txt'), 'w', encoding='utf-8').write('\n'.join(txt))
    print(b, lado, len(pedacos), 'fim', fim, flush=True)
