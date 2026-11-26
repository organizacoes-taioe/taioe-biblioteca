"""Reinações de Narizinho: o texto de 1931 (Wikisource, 1931/paginas.json) contra o OCR próprio (Tesseract) das
mesmas páginas, página a página, e os recortes do fac-símile para conferir as divergências.

    python3 -I edicoes/reinacoes-de-narizinho/comparar.py [--pranchas]

Lê o Tesseract de TESS (<pdf>.tsv, palavras com coordenadas) e grava em REL:
  pontos.tsv   uma linha por divergência de palavra em que as DUAS leituras concordam entre si contra o
               Wikisource (e leem palavra conhecida); as já decididas em conferencia.tsv saem marcadas;
  raras.tsv    palavras do Wikisource fora do léxico que aparecem uma vez só, com as duas leituras no mesmo
               lugar e o tipo: '1931' (as duas leem o mesmo que o Wikisource: é o impresso), 'OCR' (as duas
               leem outra coisa: erro da transcrição?), '?';
  com --pranchas, ver/prancha-NNN.png: os recortes da linha de cada ponto ainda sem decisão, 8 por prancha.
"""
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao.grafia import chave  # noqa: E402

TRAB = os.path.expanduser('~/.cache/claude-pedidos-2611/reinacoes-de-narizinho')
TESS = os.path.join(TRAB, 'tess')
TESS2 = os.path.join(TRAB, 'tess2')     # segunda leitura: imagem original, --psm 6
IMG = os.path.join(TRAB, 'dl', 'pag')
REL = os.path.join(TRAB, 'rel')
PAL = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*", re.U)


def k(w):
    return chave(w.replace('´', "'").replace('’', "'"))


def ws_tokens(texto):
    t = re.sub(r'(?m)^#+ .*$', ' ', texto)      # cabeçalhos: fora da comparação (o OCR os lê mal)
    t = t.replace('_', ' ').replace('|', ' ')
    return PAL.findall(t)


def tess_palavras(n, pasta=TESS):
    """[(palavra, (x0, y0, x1, y1), (linha x0, y0, x1, y1))] da página, na ordem de leitura."""
    arq = os.path.join(pasta, f'{n:03d}.tsv')
    if not os.path.exists(arq):
        return None
    linhas = {}
    for r in csv.DictReader(open(arq, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if r['level'] != '5' or not (r['text'] or '').strip():
            continue
        kk = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
        x, y, w, h = (int(r[c]) for c in ('left', 'top', 'width', 'height'))
        linhas.setdefault(kk, []).append((x, y, x + w, y + h, r['text']))
    out = []
    for kk in sorted(linhas, key=lambda kk: kk):
        ws = sorted(linhas[kk])
        txt = ' '.join(w[4] for w in ws)
        if not re.search(r'[a-zà-ÿ]', txt) or re.fullmatch(r'\W*\d+\W*.*|.*\W\d+\W*', txt) and len(txt) < 40:
            continue                      # cabeço (MONTEIRO LOBATO, título da história) e número da página
        caixa = (min(w[0] for w in ws), min(w[1] for w in ws), max(w[2] for w in ws), max(w[3] for w in ws))
        for x0, y0, x1, y1, t in ws:
            for p in PAL.findall(t):
                out.append((p, (x0, y0, x1, y1), caixa))
    return out


def lexico(paginas):
    lex = set()
    for l in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore'):
        lex.add(k(l.strip()))
    cont = Counter()
    for v in paginas.values():
        cont.update(k(w) for w in ws_tokens(v['texto']))
    return lex, cont


def conferidos():
    arq = os.path.join(AQUI, 'conferencia.tsv')
    out = {}
    if os.path.exists(arq):
        for r in csv.DictReader(open(arq, encoding='utf-8'), delimiter='\t'):
            out[(r['pagina'], r['ws'], r['antes'])] = r
    return out


def leituras(W, T):
    """Alinha as palavras da transcrição (W) com as de um OCR (T): {(i1, i2): (leitura, caixa)} nos trechos
    curtos que diferem, e {i: leitura} palavra a palavra nos trechos iguais ou trocados um por um."""
    a = [k(w) for w in W]
    b = [k(t[0]) for t in T]
    sm = SequenceMatcher(None, a, b, autojunk=False)
    dif, por = {}, {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('equal',) or (op == 'replace' and i2 - i1 == j2 - j1):
            for d in range(i2 - i1):
                por[i1 + d] = (T[j1 + d][0], T[j1 + d][2])
        if op == 'equal':
            continue
        if i2 - i1 > 3 or j2 - j1 > 3:
            continue
        if ''.join(a[i1:i2]).replace('-', '') == ''.join(b[j1:j2]).replace('-', ''):
            continue
        caixa = T[j1][2] if j1 < j2 else (T[j1 - 1][2] if j1 else (T[0][2] if T else None))
        dif[(i1, i2)] = (' '.join(t[0] for t in T[j1:j2]), caixa)
    return dif, por


def main():
    paginas = json.load(open(os.path.join(AQUI, '1931', 'paginas.json'), encoding='utf-8'))
    lex, cont = lexico(paginas)
    conh = lambda w: k(w) in lex or cont[k(w)] >= 2
    conf = conferidos()
    os.makedirs(REL, exist_ok=True)
    pontos, raras = [], []
    for ns, v in sorted(paginas.items(), key=lambda x: int(x[0])):
        n = int(ns)
        T1 = tess_palavras(n)
        T2 = tess_palavras(n, TESS2)
        if T1 is None or T2 is None:
            continue
        W = ws_tokens(v['texto'])
        d1, p1 = leituras(W, T1)
        d2, p2 = leituras(W, T2)
        for (i1, i2), (r1, cx) in d1.items():
            if (i1, i2) not in d2:
                continue
            r2 = d2[(i1, i2)][0]
            if [k(x) for x in r1.split()] != [k(x) for x in r2.split()]:
                continue                  # os dois OCRs não concordam: ruído de um deles
            if r1 and not all(conh(x) for x in r1.split()):
                continue
            pontos.append({'pagina': n, 'ws': ' '.join(W[i1:i2]), 'ocr': r1, 'antes': ' '.join(W[max(0, i1 - 4):i1]),
                           'depois': ' '.join(W[i2:i2 + 4]), 'caixa': cx})
        for i, w in enumerate(W):
            partes = [p for p in w.split('-') if p]
            if cont[k(w)] != 1 or w[:1].isupper() or all(k(p) in lex or cont[k(p)] >= 2 for p in partes):
                continue
            r1, r2 = p1.get(i), p2.get(i)
            o1, o2 = (r1[0] if r1 else ''), (r2[0] if r2 else '')
            if k(o1) == k(w) and k(o2) == k(w):
                tipo = '1931'                 # os dois OCRs leem o mesmo: é o impresso (erro de 1931?)
            elif o1 and k(o1) == k(o2):
                tipo = 'OCR'                  # os dois OCRs leem outra coisa: erro da transcrição?
            else:
                tipo = '?'
            raras.append({'pagina': n, 'ws': w, 'ocr': f'{o1} / {o2}', 'tipo': tipo,
                          'antes': ' '.join(W[max(0, i - 4):i]), 'depois': ' '.join(W[i + 1:i + 4]),
                          'caixa': (r1 or r2 or (None, None))[1]})
    for lista, nome in ((pontos, 'pontos'), (raras, 'raras')):
        with open(os.path.join(REL, nome + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('id\tpagina\tws\tocr\tantes\tdepois\ttipo\tdecidido\n')
            for i, p in enumerate(lista, 1):
                p['id'] = i
                d = conf.get((str(p['pagina']), p['ws'], p['antes']))
                p['decidido'] = d['leitura'] if d else ''
                f.write(f"{i}\t{p['pagina']}\t{p['ws']}\t{p['ocr']}\t{p['antes']}\t{p['depois']}\t{p.get('tipo', '')}\t{p['decidido']}\n")
        json.dump(lista, open(os.path.join(REL, nome + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    from collections import Counter
    print('pontos:', len(pontos), 'sem decisão:', sum(1 for p in pontos if not p['decidido']), '; raras:', len(raras),
          dict(Counter(p['tipo'] for p in raras)))
    if '--pranchas' in sys.argv:
        pranchas([p for p in pontos if not p['decidido']], 'prancha')
        pranchas([p for p in raras if not p['decidido'] and p['tipo'] != '1931'], 'rara')


def pranchas(lista, nome, por=8):
    from PIL import Image, ImageDraw, ImageFont
    pasta = os.path.join(TRAB, 'ver')
    os.makedirs(pasta, exist_ok=True)
    try:
        fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
    except OSError:
        fonte = ImageFont.load_default()
    for g in range(0, len(lista), por):
        recs = []
        for p in lista[g:g + por]:
            im = Image.open(os.path.join(IMG, f"{p['pagina']:03d}.jpg")).convert('L')
            if p['caixa']:
                x0, y0, x1, y1 = p['caixa']
                y0 = max(0, y0 - 60); y1 = min(im.size[1], y1 + 60)
                rec = im.crop((0, y0, im.size[0], y1))
            else:
                rec = im.resize((im.size[0] // 4, im.size[1] // 4))
            rec = rec.resize((rec.size[0] * 2 // 3, rec.size[1] * 2 // 3))
            cab = Image.new('L', (rec.size[0], 40), 255)
            ImageDraw.Draw(cab).text((8, 4), f"#{p['id']} p{p['pagina']}  WS: {p['ws']}  |  OCR: {p['ocr']}", font=fonte, fill=0)
            recs.append(cab); recs.append(rec)
        W = max(r.size[0] for r in recs); H = sum(r.size[1] for r in recs) + 4 * len(recs)
        tela = Image.new('L', (W, H), 200)
        y = 0
        for r in recs:
            tela.paste(r, (0, y)); y += r.size[1] + 4
        tela.save(os.path.join(pasta, f'{nome}-{g // por + 1:03d}.png'))
    print(nome, ':', (len(lista) + por - 1) // por, 'pranchas em', pasta)


if __name__ == '__main__':
    main()
