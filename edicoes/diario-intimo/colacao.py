"""Diário Íntimo — confronta a transcrição da Biblioteca Nacional (2002; fontes/bn2002.txt) com as duas leituras por
OCR do fac-símile de 1956: a do Internet Archive (ia.txt, o _djvu.txt do item) e a nossa (Tesseract, tess/<n>.tsv).

  python3 -I edicoes/diario-intimo/colacao.py <ia.txt> <pasta tess> <saída.tsv>

Para cada palavra da transcrição de 2002, a palavra que cada leitura de 1956 põe no mesmo lugar. Sai uma linha por
divergência em que as duas leituras de 1956 concordam entre si e discordam da de 2002 (acentos à parte; maiúscula
conta), e uma por trecho que as duas leituras de 1956 têm a mais (até 40 palavras; os maiores são as notas do
organizador, que não entram). Colunas: tipo, bloco, posição da palavra no bloco, 2002, 1956, contexto."""
import csv
import difflib
import glob
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
PAL = re.compile(r"[0-9A-Za-zÀ-ÿ]+")


def chave(w):
    w = unicodedata.normalize('NFD', w)
    return ''.join(c for c in w if not unicodedata.combining(c))


def blocos_bn():
    texto = open(os.path.join(AQUI, 'fontes', 'bn2002.txt'), encoding='utf-8').read()
    return texto.split('\n\n')


def tokens_bn(bl):
    out = []                       # (bloco, início, fim, palavra)
    for i, b in enumerate(bl):
        for m in PAL.finditer(b):
            if b.startswith(('#ANO', '## ', '>> ', 'q: ', '= ', 't: ')) and m.start() < 3:
                continue
            out.append((i, m.start(), m.end(), m.group(0)))
    return out


CABECO = re.compile(r'LIMA BARRETO|CLARA DOS ANJ|D[IL1]?[AÁ]R[IL1]?O\s+[IÍ]?\w?NT[IL1]?MO')


def sem_cabeco(linhas):
    return [l for l in linhas if not (len(l) < 45 and CABECO.search(l))]


def tokens_ocr(texto):
    texto = '\n'.join(sem_cabeco([l for l in texto.split('\n') if l.strip()]))
    texto = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', texto)
    return [m.group(0) for m in PAL.finditer(texto)]


def tokens_tess(pasta):
    """As palavras da nossa leitura, na ordem, com o lugar de cada uma: (palavra, página, x, y, largura, altura)."""
    out = []
    for t in tokens_tess_brutos(pasta):
        for m in PAL.finditer(t[0]):
            out.append((m.group(0),) + t[1:])
    return out


def tokens_tess_brutos(pasta):
    """As palavras do Tesseract como saem (com a pontuação colada), sem os cabeços e com o hífen de fim de linha
    desfeito: (texto, página, x, y, largura, altura)."""
    out = []
    arqs = sorted(glob.glob(os.path.join(pasta, '*.tsv')), key=lambda f: int(os.path.basename(f)[:-4]))
    for f in arqs:
        pg = int(os.path.basename(f)[:-4])
        ws = []
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            ws.append((r['text'], pg, int(r['left']), int(r['top']), int(r['width']), int(r['height']), (r['block_num'], r['par_num'], r['line_num'])))
        linhas = {}
        for t in ws:
            linhas.setdefault(t[6], []).append(t)
        fora = {k for k, v in linhas.items() if len(' '.join(x[0] for x in v)) < 45 and CABECO.search(' '.join(x[0] for x in v))}
        ws = [t[:6] for t in ws if t[6] not in fora]
        # hífen de fim de linha: junta com a primeira palavra da linha seguinte
        k = 0
        while k < len(ws):
            t = ws[k]
            if t[0].endswith('-') and len(t[0]) > 1 and k + 1 < len(ws) and ws[k + 1][3] > t[3] + t[5] // 2:
                n = ws[k + 1]
                ws[k] = (t[0][:-1] + n[0],) + t[1:]
                del ws[k + 1]
            k += 1
        out += ws
    return out


def alinhar(a, b):
    """Para cada índice de a, o índice de b alinhado (None: sem par). Trechos trocados ou a mais em b:
    {i: (i2, j1, j2)}, o trecho a[i:i2] corresponde a b[j1:j2]."""
    sm = difflib.SequenceMatcher(None, [chave(x).lower() for x in a], [chave(x).lower() for x in b], autojunk=False)
    par, trechos = [None] * len(a), {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                par[i1 + k] = j1 + k
        elif op in ('insert', 'replace', 'delete'):
            trechos[i1] = (i2, j1, j2)
    return par, trechos


def lugar(CT, j):
    t = CT[min(j, len(CT) - 1)]
    return f'{t[1]}:{t[2]},{t[3]},{t[4]},{t[5]}'


def main(ia, pasta, saida):
    bl = blocos_bn()
    T = tokens_bn(bl)
    a = [t[3] for t in T]
    ia_txt = open(ia, encoding='utf-8').read()
    ia_txt = ia_txt[ia_txt.find('NOTA PREVIA'):]
    B = tokens_ocr(ia_txt)
    CT = tokens_tess(pasta)
    C = [t[0] for t in CT]
    pb, tb = alinhar(a, B)
    pc, tc = alinhar(a, C)
    norm = lambda xs: ' '.join(chave(x).lower() for x in xs)
    n = 0
    with open(saida, 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        for i, (blk, ini, fim, pal) in enumerate(T):
            ctx = ' '.join(a[max(0, i - 6):i]) + ' [' + pal + '] ' + ' '.join(a[i + 1:i + 7])
            jb, jc = pb[i], pc[i]
            if jb is not None and jc is not None:
                xb, xc = B[jb], C[jc]
                if chave(xb) == chave(xc) and chave(xb) != chave(pal):
                    w.writerow(['palavra', blk, ini, pal, xb, ctx, lugar(CT, jc)]); n += 1
            if i in tb and i in tc:
                (i2b, j1b, j2b), (i2c, j1c, j2c) = tb[i], tc[i]
                sb, sc = B[j1b:j2b], C[j1c:j2c]
                if len(sb) > 40 or len(sc) > 40:
                    if len(sb) > 40 and len(sc) > 40:
                        w.writerow(['grande', blk, ini, ' '.join(a[i:max(i2b, i2c)]), ' '.join(sb[:25]) + ' …', ctx]); n += 1
                    continue
                if norm(sb) == norm(sc) or difflib.SequenceMatcher(None, norm(sb), norm(sc)).ratio() > 0.85:
                    w.writerow(['trecho', blk, ini, ' '.join(a[i:i2b]), ' '.join(sb) + ' ‖ ' + ' '.join(sc), ctx, lugar(CT, j1c if j2c > j1c else max(0, j1c - 1))]); n += 1
    print(n, 'linhas em', saida)


if __name__ == '__main__':
    main(*sys.argv[1:4])
