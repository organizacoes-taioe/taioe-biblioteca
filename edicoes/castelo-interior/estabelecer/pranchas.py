import sys, json, os, subprocess, collections, re
sys.path.insert(0, sys.argv[1]); base = sys.argv[2]
from tokens import norm
from PIL import Image, ImageDraw, ImageFont
V = json.load(open(f'{base}/votado2.json')); tok, src = V['tok'], V['src']
AL = json.load(open(f'{base}/alinh.json')); A = list(AL['T'])[0]; R = AL['R'][A]
T = AL['T']
fq = collections.Counter(norm(w) for t in T.values() for w in t)
nel = open(f'{base}/../dl/nelson.txt', encoding='utf-8').read()
lex = collections.Counter(norm(w) for w in nel.split())
itens = []
vistos = set()
for pos, tipo, cs in V['duv']:
    if pos in vistos: continue
    vistos.add(pos); itens.append((pos, tipo, cs))
for pos, w in enumerate(tok):
    x = norm(w)
    if w != '¶' and x and not (lex[x] >= 1 or fq[x] >= 3 or x.isdigit()) and pos not in vistos:
        vistos.add(pos); itens.append((pos, 'desconhecida', [w]))
itens.sort()
os.makedirs(f'{base}/../img/pag', exist_ok=True)
def pagina(p):
    arq = f'{base}/../img/pag/n{p}.jpg'
    if not os.path.exists(arq):
        subprocess.run(['curl', '-sL', '-A', 'TaioeBiblioteca/1.0', '-o', arq, f'https://archive.org/download/{A}/page/n{p}.jpg'], check=True)
    return Image.open(arq)
lista = []
crops = []
for k, (pos, tipo, cs) in enumerate(itens, 1):
    ref = R[src[pos]] if src[pos] < len(R) else None
    ctx = ' '.join(tok[max(0, pos - 6):pos]) + ' [[' + tok[pos] + ']] ' + ' '.join(tok[pos + 1:pos + 6])
    lista.append({'n': k, 'pos': pos, 'tipo': tipo, 'cands': cs, 'atual': tok[pos], 'ctx': ctx, 'ref': ref})
    if ref:
        im = pagina(ref[0])
        h = ref[2] - ref[1]
        c = im.crop((0, max(0, ref[1] - int(1.4 * h)), im.size[0], min(im.size[1], ref[2] + int(1.4 * h))))
        c = c.resize((c.size[0] * 2 // 3, c.size[1] * 2 // 3))
        crops.append((k, c))
json.dump(lista, open(f'{base}/conferir.json', 'w'), ensure_ascii=False, indent=0)
os.makedirs(f'{base}/../img/pr', exist_ok=True)
fonte = ImageFont.load_default(size=36) if hasattr(ImageFont, 'load_default') else None
for g in range(0, len(crops), 8):
    grupo = crops[g:g + 8]
    W = max(c.size[0] for _, c in grupo) + 90; H = sum(c.size[1] + 10 for _, c in grupo)
    pr = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(pr); y = 0
    for k, c in grupo:
        pr.paste(c, (90, y)); d.text((5, y + c.size[1] // 3), str(k), fill='red', font=fonte); y += c.size[1] + 10
        d.line((0, y - 5, W, y - 5), fill='blue', width=2)
    pr.save(f'{base}/../img/pr/pr{g // 8 + 1:02d}.jpg', quality=80)
print(len(itens), 'itens', len(crops), 'recortes')
