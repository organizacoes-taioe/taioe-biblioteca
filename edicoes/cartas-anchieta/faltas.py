"""Cartas de Anchieta — linhas que a leitura-base (Tesseract psm 4) não viu e que o OCR do Internet Archive viu.

  python3 edicoes/cartas-anchieta/faltas.py [PASTA]

Para cada folha, cada linha do OCR do IA (dl/ia_djvu.xml) é procurada na transcrição (1933/<folha>.txt):
a que não tem par parecido (razão < 0,75) é candidata a linha perdida. Grava PASTA/pranchas7/ (recorte da
linha no fac-símile, com a de cima e a de baixo) e o .txt com «k<TAB>folha<TAB>k+<TAB>texto do IA», onde k é a
linha do rascunho depois da qual ela entra. A conferência grava «folha<TAB>k+<TAB>texto» em conferencia.tsv
(texto «-» = não falta nada), que o rascunho.py --aplicar insere.
"""
import difflib
import json
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import pecas  # noqa: E402

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-anchieta')


def norm(t):
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn').lower()
    return ''.join(re.findall(r'[a-z]+', t))


def linhas_ia():
    root = ET.parse(os.path.join(PASTA, 'dl', 'ia_djvu.xml')).getroot()
    out = {}
    for i, obj in enumerate(root.iter('OBJECT')):
        w, h = int(obj.get('width')), int(obj.get('height'))
        ls = []
        for line in obj.iter('LINE'):
            ws = list(line.iter('WORD'))
            cs = [list(map(int, x.get('coords').split(',')[:4])) for x in ws]
            box = [min(c[0] for c in cs), min(c[3] for c in cs), max(c[2] for c in cs), max(c[1] for c in cs)]
            ls.append((' '.join(x.text or '' for x in ws), box, (w, h)))
        out[i] = ls
    return out


def main():
    conf = {}
    for l in open(os.path.join(AQUI, 'conferencia.tsv'), encoding='utf-8'):
        if l.strip() and not l.startswith('#'):
            f, k, t = l.rstrip('\n').split('\t', 2)
            conf[(int(f), k)] = t
    ia = linhas_ia()
    lista = []
    for f in pecas.folhas():
        rasc = open(os.path.join(PASTA, 'rascunho', f'{f}.txt'), encoding='utf-8').read().splitlines()
        nossas = [conf.get((f, str(k)), l) for k, l in enumerate(rasc)]
        nn = [norm(l) for l in nossas]
        texto = ''.join(nn)
        ultimo = -1
        t2 = norm(open(os.path.join(PASTA, 'tess2', f'{f}.txt'), encoding='utf-8').read())
        p = next(x for x in pecas.PECAS if f in pecas.folhas_de(x))
        linhas = ia[f]
        if f == pecas.folhas_de(p)[-1]:             # as notas de 1933 não contam
            corte = next((i for i, x in enumerate(linhas) if re.match(r'^\W*NOTAS?\b', x[0])), len(linhas))
            linhas = linhas[:corte]
        for t, box, dim in linhas:
            n = norm(t)
            if len(n) < 12 or re.search(r'JOSEP|CARTA D|INFORMA|SERM[ÃA]O', t) or sum(c.isupper() for c in t) > len(t) / 3:
                continue
            if f == pecas.folhas_de(p)[0] and ultimo < 0 and not any(norm(pecas.INICIO[p[0]]) in norm(x) for x in nossas[:1]):
                pass
            # confirmada pela outra leitura (tess2): sem isso é sujeira do OCR do IA
            if len(re.findall(r'[a-zà-ÿ]{3,}', t)) < 3:        # sujeira do OCR do IA
                continue
            # melhor linha nossa (ou par de linhas, pela hifenização)
            melhor, km = 0, None
            for k in range(len(nn)):
                for cand in (nn[k], nn[k] + (nn[k + 1] if k + 1 < len(nn) else '')):
                    r = difflib.SequenceMatcher(None, n, cand, autojunk=False).find_longest_match(0, len(n), 0, len(cand)).size / len(n)
                    if r > melhor:
                        melhor, km = r, k
            if melhor >= 0.6 or n in texto:
                ultimo = max(ultimo, km)
                continue
            if ultimo < 0 and f == pecas.folhas_de(p)[0]:       # título e sumário de 1933, antes do texto
                continue
            lista.append((f, ultimo, t, box, dim))
    os.makedirs(os.path.join(PASTA, 'pranchas7'), exist_ok=True)
    jp2 = lambda f: os.path.join(PASTA, 'dl', 'jp2', pecas.ITEM + '_jp2', f'{pecas.ITEM}_{f:04d}.jp2')
    n = 0
    for i in range(0, len(lista), 8):
        grupo = lista[i:i + 8]
        recs = []
        for f, k, t, (x0, y0, x1, y1), (w, h) in grupo:
            im = Image.open(jp2(f)).convert('L')
            sx, sy = im.width / w, im.height / h
            r = im.crop((max(0, int(x0 * sx) - 20), max(0, int(y0 * sy) - 30), min(im.width, int(x1 * sx) + 20),
                         min(im.height, int(y1 * sy) + 30)))
            recs.append(r.resize((r.width * 2, r.height * 2)))
        larg = max(r.width for r in recs) + 70
        pr = Image.new('L', (larg, sum(r.height + 12 for r in recs)), 255)
        d = ImageDraw.Draw(pr)
        y = 0
        txt = []
        for j, (r, (f, k, t, _, _)) in enumerate(zip(recs, grupo), 1):
            pr.paste(r, (70, y))
            d.text((8, y + r.height // 2 - 8), str(j), fill=0)
            d.line((0, y + r.height + 6, larg, y + r.height + 6), fill=120)
            y += r.height + 12
            antes = open(os.path.join(PASTA, 'rascunho', f'{f}.txt'), encoding='utf-8').read().splitlines()
            ctx = conf.get((f, str(k)), antes[k]) if k >= 0 else '(começo da folha)'
            txt.append(f'{j}\t{f}\t{k}+\t{t}\t(depois de: {ctx})')
        n += 1
        pr.save(os.path.join(PASTA, 'pranchas7', f'{n:03d}.png'))
        open(os.path.join(PASTA, 'pranchas7', f'{n:03d}.txt'), 'w', encoding='utf-8').write('\n'.join(txt) + '\n')
    print(len(lista), 'linhas candidatas em', n, 'pranchas')


if __name__ == '__main__':
    main()
