"""Lista do que conferir nas imagens do Knöll e pranchas de recortes.
uso: python3 -I revisar.py <relatorio.json> <pasta-ocr> <pasta-img> <saida-pranchas>"""
import sys, os, re, json, subprocess
from PIL import Image, ImageDraw, ImageFont
REL, OCR, IMG, SAI = sys.argv[1:5]
r = json.load(open(REL, encoding='utf-8'))
def n(t): return re.sub('[^a-z]', '', t.lower()).replace('v', 'u').replace('j', 'i')
ORT = [('inm','imm'),('inp','imp'),('inb','imb'),('conl','coll'),('conm','comm'),('conp','comp'),('conb','comb'),('adp','app'),('adt','att'),('adr','arr'),('adl','all'),('adc','acc'),('adf','aff'),('adg','agg'),('ads','ass'),('inr','irr'),('inl','ill'),('conr','corr'),('k','c'),('ae','e'),('quicq','quidq'),('michi','mihi'),('nil','nihil'),('intellig','intelleg'),('y','i'),('ph','f'),('th','t'),('h','')]
def ort(a):
    a = n(a)
    for x, y in ORT: a = a.replace(x, y)
    return a
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
itens = []
for v in r['variantes']:
    if ort(v['od']) == ort(v['knoll']) or v['n'] == 3: continue
    itens.append({'tipo': 'V', 'livro': v['livro'], 'i': v['i'], 'od': v['od'], 'k': v['knoll'], 'ctx': v['ctx'], 'onde': v['onde']})
for d in r['duvidas']:
    if 'od' not in d: continue
    simples = [x.strip() for x in d['ocr'] if x != 'None' and not x.startswith("('SEG'")]
    if any(ort(x) == ort(d['od']) for x in simples): continue          # regra 1 (no aplicar)
    if simples and len(simples) == len(d['ocr']) and all(lev(n(x), n(d['od'])) <= 2 for x in simples): continue
    if simples and all(lev(n(x), n(d['od'])) <= 1 for x in simples) and len(simples) >= 2: continue
    itens.append({'tipo': 'D', 'livro': d['livro'], 'i': d['i'], 'od': d['od'], 'k': ' / '.join(d['ocr']), 'ctx': d['ctx'], 'onde': d.get('onde') or d.get('perto')})
for a in r['acrescimos']:
    if a['n'] == 3: continue
    itens.append({'tipo': 'A', 'livro': a['livro'], 'i': a['i'], 'od': '', 'k': a['knoll'], 'ctx': a['depois_de'], 'onde': a.get('perto')})
print(len(itens), {t: sum(1 for x in itens if x['tipo'] == t) for t in 'VDA'})
if not os.environ.get('SEL'): json.dump(itens, open(os.path.join(SAI, 'itens.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

def pagina_img(o, p):
    arq = os.path.join(IMG, o, f'{p:04d}.jpg')
    if not os.path.exists(arq):
        os.makedirs(os.path.dirname(arq), exist_ok=True)
        url = f'https://archive.org/download/{o}/{o}_jp2.zip/{o}_jp2%2F{o}_{p:04d}.jp2&ext=jpg'
        subprocess.run(['curl', '-sL', '-o', arq, url], check=True)
    return Image.open(arq)
LARG = {}
def recorte(o, p, bb):
    im = pagina_img(o, p)
    if o not in LARG:
        LARG[o] = {'corpusscriptoru11wiengoog': 3192, 'sanctiaureliaugu33augu': 2438}.get(o)
    w = LARG[o] or im.size[0]
    s = im.size[0] / w
    x0, y0, x1, y1 = bb; h = y1 - y0
    return im.crop((0, int((y0 - 1.6 * h) * s), im.size[0], int((y1 + 1.6 * h) * s))), (int(x0 * s), int(y0 * s) - int((y0 - 1.6 * h) * s), int(x1 * s), int(y1 * s) - int((y0 - 1.6 * h) * s))
PREF = ['sanctiaureliaugu33augu', 'corpusscriptoru11wiengoog', 'corpusscriptorum0033unse']
fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)
os.makedirs(SAI, exist_ok=True)
POR = 10
SEL = json.load(open(os.environ['SEL'])) if os.environ.get('SEL') else list(range(len(itens)))
for f in range(0, len(SEL), POR):
    partes = []
    for k in SEL[f:f + POR]:
        it = itens[k]
        rot = f"#{k} [{it['tipo']}] L{it['livro']}  od={it['od']}  knöll?={it['k'][:70]}"
        ctx = it['ctx'][:150]
        im = None
        for o in PREF:
            if not (it['onde'] and o in it['onde']): continue
            p, bb = it['onde'][o]
            try:
                im, caixa = recorte(o, p, bb); break
            except Exception:
                arq = os.path.join(IMG, o, f'{p:04d}.jpg')
                if os.path.exists(arq) and os.path.getsize(arq) < 20000: os.remove(arq)
        if im is None:
            im = Image.new('RGB', (1200, 40), 'white'); partes.append((rot, ctx, im)); continue
        im = im.convert('RGB')
        if im.size[0] > 1300: im = im.resize((1300, int(im.size[1] * 1300 / im.size[0])))
        partes.append((rot, ctx, im))
    W = 1300; H = sum(60 + im.size[1] + 10 for _, _, im in partes)
    folha = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(folha); y = 0
    for rot, ctx, im in partes:
        d.text((5, y + 4), rot, fill='red', font=fonte); d.text((5, y + 30), ctx, fill='blue', font=fonte)
        folha.paste(im, (0, y + 60)); y += 60 + im.size[1] + 10
    folha.save(os.path.join(SAI, os.environ.get('PREF', 'prancha-') + f'{f // POR:03d}.jpg'), quality=80)
