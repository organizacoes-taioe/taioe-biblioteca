"""Pranchas para a conferência linha a linha: cada uma é um trecho da coluna grega (até 10 linhas do OCR), com o
número de cada linha lida à esquerda, e um .txt com as palavras do nosso texto em cada linha (folha:idx<TAB>palavras).
Grava pranchas/<parte>-NNN.png e .txt. Uso: pranchas2.py"""
import os, json, re
from PIL import Image, ImageDraw, ImageFont
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-2')
os.makedirs(os.path.join(AQUI, 'pranchas'), exist_ok=True)
try: FONTE = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
except Exception: FONTE = None
ESC = 0.75
for parte in ('inicio', 'pastor'):
    linhas = json.load(open(os.path.join(AQUI, 'linhas-%s.json' % parte), encoding='utf-8'))
    blocos = json.load(open(os.path.join(AQUI, 'blocos-%s.json' % parte), encoding='utf-8'))
    pal_de = {}
    for b in blocos:
        for w, tid in b['pal']:
            if tid: pal_de[tid] = w
    n = 0
    for p in linhas:
        f = p['folha']
        ocr = json.load(open(os.path.join(AQUI, 'ocr', '%04d.json' % f)))
        im = Image.open(os.path.join(AQUI, 'pag', '%04d.png' % f)).convert('L')
        W, H = im.size; g = ocr['gutter']
        a, b = (0, g + 20) if p['ci'] == 0 else (g - 20, W)
        reais = [l for l in p['linhas'] if l.get('id')]
        # grupos de linhas seguidas (um título no meio corta o grupo)
        grupos, cur = [], []
        for l in p['linhas']:
            if not l.get('id'):
                if cur: grupos.append(cur); cur = []
                continue
            if cur and int(l['id'].split(':')[1]) != int(cur[-1]['id'].split(':')[1]) + 1 and l['y'] - cur[-1]['y'] > 200:
                grupos.append(cur); cur = []
            cur.append(l)
        if cur: grupos.append(cur)
        for gr in grupos:
            for k in range(0, len(gr), 10):
                lote = gr[k:k + 10]
                y0 = lote[0]['y'] - (110 if k == 0 else 12)
                ult = lote[-1]
                y1 = (gr[k + 10]['y'] - 8) if k + 10 < len(gr) else ult['y1'] + 110
                y0, y1 = max(0, y0), min(H, y1)
                c = im.crop((a, y0, b, y1))
                c = c.resize((int(c.width * ESC), int(c.height * ESC)))
                o = Image.new('L', (c.width + 110, c.height), 255); o.paste(c, (110, 0))
                d = ImageDraw.Draw(o)
                txt = []
                for l in lote:
                    yy = int((l['y'] - y0) * ESC); yy1 = int((l['y1'] - y0) * ESC)
                    d.line((100, yy, 100, yy1), fill=0, width=4)
                    d.text((4, yy), l['id'].split(':')[1], fill=0, font=FONTE)
                    ws = []
                    for t in l['toks']:
                        tid = '%d:%d:%d' % (f, t[2], t[3])
                        if tid in pal_de: ws.append(pal_de[tid])
                    txt.append('%s\t%s' % (l['id'], ' '.join(ws)))
                n += 1
                nome = '%s-%03d' % (parte, n)
                o.save(os.path.join(AQUI, 'pranchas', nome + '.png'))
                open(os.path.join(AQUI, 'pranchas', nome + '.txt'), 'w', encoding='utf-8').write('\n'.join(txt) + '\n')
    print(parte, n, 'pranchas')
