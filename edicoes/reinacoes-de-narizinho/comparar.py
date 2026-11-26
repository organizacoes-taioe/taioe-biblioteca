"""Reinações de Narizinho: o texto de 1931 (Wikisource, 1931/paginas.json) contra o OCR próprio (Tesseract) das
mesmas páginas, página a página, e os recortes do fac-símile para conferir as divergências.

    python3 -I edicoes/reinacoes-de-narizinho/comparar.py [--pranchas]

Lê o Tesseract de TESS (<pdf>.tsv, palavras com coordenadas) e grava em REL:
  pontos.tsv   uma linha por divergência de palavra (id, página, leitura do Wikisource, do OCR, contexto),
               só onde a leitura do OCR é palavra conhecida (léxico do sistema ou do próprio livro) e difere
               da do Wikisource em mais do que grafia miúda; as já decididas em conferencia.tsv saem marcadas;
  raras.tsv    palavras do Wikisource que não estão no léxico e aparecem uma vez só (erro de 1931 ou da
               transcrição?), com a leitura do OCR no mesmo lugar;
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
IMG = os.path.join(TRAB, 'dl', 'pag')
REL = os.path.join(TRAB, 'rel')
PAL = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*", re.U)


def k(w):
    return chave(w.replace('´', "'").replace('’', "'"))


def ws_tokens(texto):
    t = re.sub(r'(?m)^#+ .*$', ' ', texto)      # cabeçalhos: fora da comparação (o OCR os lê mal)
    t = t.replace('_', ' ').replace('|', ' ')
    return PAL.findall(t)


def tess_palavras(n):
    """[(palavra, (x0, y0, x1, y1), (linha x0, y0, x1, y1))] da página, na ordem de leitura."""
    arq = os.path.join(TESS, f'{n:03d}.tsv')
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


def main():
    paginas = json.load(open(os.path.join(AQUI, '1931', 'paginas.json'), encoding='utf-8'))
    lex, cont = lexico(paginas)
    conh = lambda w: k(w) in lex or cont[k(w)] >= 2
    conf = conferidos()
    os.makedirs(REL, exist_ok=True)
    pontos, raras = [], []
    for ns, v in sorted(paginas.items(), key=lambda x: int(x[0])):
        n = int(ns)
        T = tess_palavras(n)
        if T is None:
            continue
        W = ws_tokens(v['texto'])
        a = [k(w) for w in W]
        b = [k(t[0]) for t in T]
        sm = SequenceMatcher(None, a, b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                continue
            wsr = ' '.join(W[i1:i2]); tr = ' '.join(t[0] for t in T[j1:j2])
            antes = ' '.join(W[max(0, i1 - 4):i1]); depois = ' '.join(W[i2:i2 + 4])
            caixa = T[j1][2] if j1 < j2 else (T[j1 - 1][2] if j1 else None)
            if ''.join(a[i1:i2]).replace('-', '') == ''.join(b[j1:j2]).replace('-', ''):
                continue                  # só a separação ou o hífen mudam («Chama-se» / «Chama se»)
            if op == 'replace' and (j2 - j1) != (i2 - i1):
                continue                  # o OCR partiu ou juntou palavras («a cura» / «altura»): ruído
            if op in ('replace', 'insert') and j2 - j1 <= 3 and all(conh(t[0]) for t in T[j1:j2]) and (i2 - i1) <= 3:
                # o OCR lê palavra(s) conhecida(s) onde a transcrição tem outra coisa (ou nada)
                if op == 'insert' and all(len(t[0]) <= 2 for t in T[j1:j2]):
                    continue              # letras soltas do OCR (borda da página, ilustração)
                if ''.join(a[i1:i2]) == ''.join(b[j1:j2]):
                    continue              # só a separação muda («dum» / «d um»)
                pontos.append({'pagina': n, 'ws': wsr, 'ocr': tr, 'antes': antes, 'depois': depois, 'caixa': caixa})
            elif op == 'delete' and i2 - i1 <= 2 and all(conh(w) for w in W[i1:i2]):
                # palavra da transcrição que o OCR não tem: só se o OCR está limpo em volta (não é ruído)
                viz = T[max(0, j1 - 3):j1 + 3]
                if len(viz) >= 4 and all(conh(t[0]) for t in viz):
                    pontos.append({'pagina': n, 'ws': wsr, 'ocr': '', 'antes': antes, 'depois': depois,
                                   'caixa': caixa})
        for i, w in enumerate(W):
            if cont[k(w)] == 1 and k(w) not in lex and not w[:1].isupper():
                j = None
                for op, i1, i2, j1, j2 in sm.get_opcodes():
                    if i1 <= i < i2:
                        j = j1 + (i - i1) if op in ('equal', 'replace') and j1 + (i - i1) < j2 else None
                        break
                raras.append({'pagina': n, 'ws': w, 'ocr': T[j][0] if j is not None else '',
                              'antes': ' '.join(W[max(0, i - 4):i]), 'depois': ' '.join(W[i + 1:i + 4]),
                              'caixa': T[j][2] if j is not None else None})
    for lista, nome in ((pontos, 'pontos'), (raras, 'raras')):
        with open(os.path.join(REL, nome + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('id\tpagina\tws\tocr\tantes\tdepois\tdecidido\n')
            for i, p in enumerate(lista, 1):
                p['id'] = i
                d = conf.get((str(p['pagina']), p['ws'], p['antes']))
                p['decidido'] = d['leitura'] if d else ''
                f.write(f"{i}\t{p['pagina']}\t{p['ws']}\t{p['ocr']}\t{p['antes']}\t{p['depois']}\t{p['decidido']}\n")
        json.dump(lista, open(os.path.join(REL, nome + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('pontos:', len(pontos), 'sem decisão:', sum(1 for p in pontos if not p['decidido']), '; raras:', len(raras))
    if '--pranchas' in sys.argv:
        pranchas([p for p in pontos if not p['decidido']], 'prancha')
        pranchas([p for p in raras if not p['decidido']], 'rara')


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
