"""Diário Íntimo — a pontuação: depois de cada palavra, a da transcrição de 2002 contra a das duas leituras de 1956.

  python3 -I edicoes/diario-intimo/pontuacao.py <ia.txt> <pasta tess> <saída.tsv>

Sai uma linha por palavra em que as duas leituras de 1956 trazem, depois dela, a mesma pontuação e a de 2002 outra
(aspas, apóstrofos e espaços à parte). Colunas: bloco, posição do fim da palavra no bloco, 2002, 1956, contexto, lugar."""
import csv
import difflib
import re
import sys

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import colacao as C  # noqa: E402

PONT = re.compile(r"[0-9A-Za-zÀ-ÿ]+|[^\sA-Za-zÀ-ÿ0-9]+")


def norm_p(s):
    s = re.sub(r'[«»“”"\'‘’()\[\]_*]', '', s)
    s = s.replace('...', '…').replace('. . .', '…')
    s = re.sub(r'[–—-]+', '—', s)
    return s


def seq(texto):
    """(palavra, pontuação depois dela, fim da palavra) para um texto corrido."""
    out = []
    for m in C.PAL.finditer(texto):
        out.append([m.group(0), '', m.end()])
    for k, (w, _, fim) in enumerate(out):
        ini_prox = out[k + 1][2] - len(out[k + 1][0]) if k + 1 < len(out) else len(texto)
        out[k][1] = norm_p(re.sub(r'\s+', '', texto[fim:ini_prox]))
    return out


def main(ia, pasta, saida):
    bl = C.blocos_bn()
    A = []
    for i, b in enumerate(bl):
        corpo = re.sub(r'^(#ANO|##|>>|q:|=|t:|-+|\|)\s', lambda m: ' ' * len(m.group(0)), b)
        for w, p, fim in seq(corpo):
            A.append((w, p, i, fim))
    ia_txt = open(ia, encoding='utf-8').read()
    ia_txt = ia_txt[ia_txt.find('NOTA PREVIA'):]
    ia_txt = '\n'.join(C.sem_cabeco([l for l in ia_txt.split('\n') if l.strip()]))
    ia_txt = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', ia_txt)
    B = seq(ia_txt)
    CT = C.tokens_tess(pasta)
    # a nossa leitura: o texto das palavras do Tesseract (com a pontuação colada) e o lugar de cada uma
    T = []
    for t in C.tokens_tess_brutos(pasta):
        for w, p, _ in seq(t[0]):
            T.append((w, p) + t[1:])
    ka = [C.chave(x[0]).lower() for x in A]
    pb, _ = C.alinhar([x[0] for x in A], [x[0] for x in B])
    pt, _ = C.alinhar([x[0] for x in A], [x[0] for x in T])
    n = 0
    with open(saida, 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        for k, (pal, p, blk, fim) in enumerate(A):
            jb, jt = pb[k], pt[k]
            if jb is None or jt is None:
                continue
            p56, p56t = B[jb][1], T[jt][1]
            if p56 == p56t and p56 != p and C.chave(B[jb][0]).lower() == ka[k]:
                ctx = ' '.join(x[0] + x[1] for x in A[max(0, k - 5):k + 1]) + ' ‖ ' + ' '.join(x[0] for x in A[k + 1:k + 5])
                t = T[jt]
                w.writerow([blk, fim, p, p56, ctx, f'{t[2]}:{t[3]},{t[4]},{t[5]},{t[6]}'])
                n += 1
    print(n, 'linhas em', saida)


if __name__ == '__main__':
    main(*sys.argv[1:4])
