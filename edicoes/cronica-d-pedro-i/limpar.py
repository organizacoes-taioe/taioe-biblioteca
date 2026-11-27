"""Crónica de D. Pedro I — passo 2: das linhas do hOCR (linhas.py) ao texto corrido de um testemunho.

    python3 -I edicoes/cronica-d-pedro-i/limpar.py <linhas.tsv> <saida.txt>

Tira o cabeçalho da página, as notas de rodapé (as variantes dos códices B e T), o reclamo e a
assinatura do caderno; junta as linhas, desfaz a palavra partida no fim da linha e marca o começo de
cada parte: «@@ PROLOGO» e «@@ CAPITULO N», o título do capítulo em «@T …». Começa no prólogo e
para na «Tavoada» (1816) ou no começo da crónica de D. Fernando.
"""
import re
import statistics
import sys

ROMANO = {'I': 1, 'V': 5, 'X': 10, 'L': 50}


def romano(s):
    s = s.upper().replace('1', 'I').replace('l', 'I').replace('U', 'II')
    s = re.sub(r'[^IVXL]', '', s)
    t = 0
    for i, c in enumerate(s):
        v = ROMANO[c]
        t += -v if i + 1 < len(s) and ROMANO[s[i + 1]] > v else v
    return t


def paginas(arq):
    pp = {}
    for l in open(arq, encoding='utf-8'):
        p, y0, y1, x0, x1, xs, t = l.rstrip('\n').split('\t')
        pp.setdefault(int(p), []).append(dict(y0=int(y0), y1=int(y1), x0=int(x0), x1=int(x1), xs=int(xs), t=t))
    return pp


CAB = re.compile(r'chronica|chr[o0]n|d.?el ?r[ec]i|pedro|prologo|^\W*\d+\W*$|^\W*\d+\W|\W\d+\W*$', re.I)
NOTA = re.compile(r'^\W{0,3}[\(\[{]\s?[0-9iIlzOoSj]{1,2}\s?[\)\]}^]\s?\S.*\s[TB][.,]')
CAB2 = re.compile(r'P\s?E\s?D\s?R\s?[oO0]|E\s?L\s?R\s?E\s?I|C\s?H\s?R\s?O\s?N\s?I\s?C\s?A')
CAPIT = re.compile(r'^\W*C\s?A\s?P\s?I\s?T\s?U\s?L\s?O\s*([IVXLlJíÍ1Unr\]]+[.,]?\s*[IVXLlJ1r\]]*)\W*$')


def limpar_pagina(ls):
    ls = sorted(ls, key=lambda d: d['y0'])
    corpo = [d for d in ls if len(d['t'].split()) >= 5]
    if not corpo:
        return ls
    tam = statistics.median(d['xs'] for d in corpo)
    marg = statistics.median(d['x0'] for d in corpo)
    larg = statistics.median(d['x1'] for d in corpo) - marg
    alto = max(d['y1'] for d in ls)
    # cabeçalho: a primeira linha, se for o título corrente ou o número da página
    for _ in range(2):
        if not ls or CAPIT.match(ls[0]['t']):
            break
        t0 = ls[0]['t']
        letras = re.sub(r'[^A-Za-z]', '', t0)
        espacada = len(t0.split()) >= 4 and sum(len(w) <= 2 for w in t0.split()) >= 0.6 * len(t0.split())
        if (CAB.search(t0) and len(t0.split()) <= 4) or (CAB2.search(t0) and (espacada or len(t0.split()) <= 5)) \
                or re.match(r'^\W*\d+\W*$', t0) or (espacada and ls[0]['y1'] < (corpo[0]['y0'] if corpo else 0)):
            ls = ls[1:]
        else:
            break
    # notas de rodapé: as linhas com as siglas dos códices, e as de letra menor no pé da página
    fim_corpo = max((d['y1'] for d in ls if d['xs'] >= 0.88 * tam and len(d['t'].split()) >= 4 and not NOTA.match(d['t'])), default=alto)
    ls = [d for d in ls if not NOTA.match(d['t']) and not re.match(r'^\s*Tom[.,]\s', d['t'])
          and not (d['xs'] < 0.88 * tam and d['y0'] >= fim_corpo - 5)]
    # o reclamo (e a assinatura do caderno): a última linha curta, fora da margem
    if ls:
        d = ls[-1]
        if len(d['t'].split()) <= 3 and (d['x0'] > marg + 0.3 * larg or re.search(r'\^\s*$', d['t'])):
            ls = ls[:-1]
    return ls


QINI = re.compile(r'^\s*(?:«|»|„|"|99|55|3[jJ>]|5[jJ>^]|>j|j\)|\)j|í>|9>|95|\?>|€|•|■)\s*')


def main(arq, saida):
    pp = paginas(arq)
    nums = sorted(pp)
    ini = next(p for p in nums if any(re.match(r'\W*L?E\s?[iI][xX]', d['t']) for d in pp[p]))
    fim = next(p for p in nums if p > ini and any(re.search(r'T\s?A\s?V\s?O\s?A\s?D\s?A|D\.\s?FERNANDO|NONO REI', d['t']) for d in pp[p]))
    linhas = []                     # (tipo, texto, centrada)
    # páginas escaneadas duas vezes (na 2ª edição, 121–122 = 123–124)
    from difflib import SequenceMatcher
    txt = {p: re.sub(r'\W', '', ' '.join(d['t'] for d in sorted(pp[p], key=lambda d: d['y0'])))[:1500] for p in nums}
    repetidas = {q for p in range(ini, fim) for q in range(p + 1, p + 5)
                 if p in txt and q in txt and len(txt[p]) > 300
                 and SequenceMatcher(None, txt[p], txt[q], autojunk=False).ratio() > 0.9}
    for p in range(ini, fim):
        if p not in pp or p in repetidas:
            continue
        ls = limpar_pagina(pp[p])
        if p == ini:
            ls = [d for d in ls if d['y0'] >= next(d2['y0'] for d2 in ls if re.match(r'\W*L?E\s?[iI][xX]', d2['t']))]
            linhas.append(('@@', '@@ PROLOGO', False))
        corpo = [d for d in ls if len(d['t'].split()) >= 5]
        tam = statistics.median([d['xs'] for d in corpo] or [0])
        marg = statistics.median([d['x0'] for d in corpo] or [0])
        dir_ = statistics.median([d['x1'] for d in corpo] or [0])
        larg = (dir_ - marg) or 1
        for d in ls:
            t = d['t']
            m = CAPIT.match(t)
            if m:
                linhas.append(('@@', f'@@ CAPITULO {romano(m.group(1))}', False))
                continue
            if len(t) <= 2 and d['xs'] > 1.5 * tam:      # capitular
                continue
            centrada = d['x0'] > marg + 0.04 * larg and d['x1'] < dir_ - 0.04 * larg
            linhas.append(('l', t, centrada))
    # títulos: a 1ª linha depois de «@@ CAPITULO» e as seguintes, centradas, até a que termina em ponto
    out, i = [], 0
    while i < len(linhas):
        tipo, l, c = linhas[i]
        if tipo == '@@':
            out.append(l)
            i += 1
            if l.startswith('@@ CAPITULO'):
                n = 0
                while i < len(linhas) and linhas[i][0] == 'l' and n < 5:
                    if n > 0 and (not linhas[i][2] or re.search(r'[.»]\s*$', out[-1])):
                        break
                    out.append('@T ' + linhas[i][1])
                    n += 1
                    i += 1
            continue
        out.append(l)
        i += 1
    # aspas: a marca no começo de cada linha citada sai; a primeira linha de cada citação ganha «
    res, antes = [], False
    for l in out:
        if l.startswith('@'):
            res.append(l)
            antes = False
            continue
        m = QINI.match(l)
        if m:
            l = l[m.end():]
            if not antes and res and '«' not in res[-1]:
                l = '« ' + l
            antes = True
        else:
            antes = False
        res.append(l)
    # juntar: palavra partida no fim da linha
    txt = []
    for l in res:
        if l.startswith('@'):
            txt.append('\n' + l + '\n')
        else:
            txt.append(l + '\n')
    s = ''.join(txt)
    s = re.sub(r'(\w)[-¬]\s*\n(?!@)\s*', r'\1', s)
    open(saida, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
