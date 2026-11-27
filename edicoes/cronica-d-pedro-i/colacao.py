"""Crónica de D. Pedro I — passo 3: colação dos quatro testemunhos do texto de 1816.

    python3 -I edicoes/cronica-d-pedro-i/colacao.py <pasta>      # lê <pasta>/A.txt … D.txt (limpar.py)

A, B, C: três exemplares da edição da Academia (Colecção de livros inéditos, t. IV, 1816) no Internet
Archive; D: a 2ª edição do mesmo tomo (Imprensa Nacional, 1925), recomposta página a página. Todos
com OCR do próprio Archive, que lê o s longo (ſ) ora como f, ora como s, e as ligaduras ſt, ſſ, ſi
de muitas maneiras (ft, íl, íT, lT, fF…). D é o pivô: o OCR da reimpressão de 1925 separa melhor as aspas, as chamadas das notas e as palavras partidas.

Alinha A, C e D a B (âncoras de 4 palavras únicas + SequenceMatcher nos intervalos) e escolhe, em
cada lugar, a leitura com mais apoio (A, B, C pesam 1; D, 0,8), contando f = s. Grava <pasta>/voto.tsv
(uma linha por palavra: B, A, C, D, escolhida, apoio) e <pasta>/voto.txt (o texto escolhido).
"""
import collections
import json
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher

TOK = re.compile(r"@@ [A-Z]+(?: \d+)?|@T|@F|@CAP \S+|[A-Za-zÀ-ÿẽũĩõãç'’\-\^0-9]+|[^\sA-Za-zÀ-ÿ0-9]")
PESO = {'A': 1.0, 'B': 1.0, 'C': 1.0, 'D': 0.8}


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))


def chave(t):
    """Chave grosseira para alinhar: minúsculas, sem acento, f = s, só letras."""
    if t.startswith('@'):
        return t
    k = sem_acento(t).lower()
    k = re.sub(r'[^a-z]', '', k)
    k = k.replace('f', 's').replace('l', 'i').replace('t', 'i')
    return k or t


def tokens(arq):
    s = open(arq, encoding='utf-8').read()
    s = re.sub(r'^@P\n', '', s, flags=re.M)
    out = []
    for linha in s.split('\n'):
        if linha.startswith('@T '):
            out.append('@T')
            out += TOK.findall(linha[3:])
            out.append('@F')
        elif linha.startswith('@'):
            out.append(linha.strip())
        else:
            out += TOK.findall(linha)
    return out


def ancoras(ka, kb, n=4):
    def grams(k):
        c = collections.defaultdict(list)
        for i in range(len(k) - n + 1):
            g = tuple(k[i:i + n])
            if all(len(x) > 1 for x in g):
                c[g].append(i)
        return {g: v[0] for g, v in c.items() if len(v) == 1}
    ga, gb = grams(ka), grams(kb)
    pares = sorted((ga[g], gb[g]) for g in ga.keys() & gb.keys())
    # maior subsequência crescente em b
    import bisect
    tails, idx, prev = [], [], [None] * len(pares)
    for k, (i, j) in enumerate(pares):
        p = bisect.bisect_left([pares[t][1] for t in tails], j) if tails else 0
        if p > 0:
            prev[k] = tails[p - 1]
        if p == len(tails):
            tails.append(k)
        else:
            tails[p] = k
    seq, k = [], tails[-1] if tails else None
    while k is not None:
        seq.append(pares[k])
        k = prev[k]
    return seq[::-1]


def alinhar(ta, tb):
    """Para cada posição de ta (o pivô), a leitura de tb (string, '' se faltar), e as inserções."""
    ka, kb = [chave(t) for t in ta], [chave(t) for t in tb]
    anc = ancoras(ka, kb)
    leit = [''] * len(ta)
    ins = collections.defaultdict(list)          # posição do pivô antes da qual entra
    pontos = [(0, 0)] + [(i, j) for i, j in anc] + [(len(ta), len(tb))]
    for (i0, j0), (i1, j1) in zip(pontos, pontos[1:]):
        if i1 < i0 or j1 < j0:
            continue
        sm = SequenceMatcher(None, ka[i0:i1], kb[j0:j1], autojunk=False)
        for op, a0, a1, b0, b1 in sm.get_opcodes():
            a0 += i0; a1 += i0; b0 += j0; b1 += j0
            if op == 'equal' or (op == 'replace' and a1 - a0 == b1 - b0):
                for d in range(a1 - a0):
                    leit[a0 + d] = tb[b0 + d]
            elif op == 'replace':
                # emparelha pela semelhança, em ordem
                bs = list(range(b0, b1))
                usados = 0
                for a in range(a0, a1):
                    melhor, mj = 0.0, None
                    for j in bs[usados:usados + 3]:
                        r = SequenceMatcher(None, ka[a], kb[j]).ratio()
                        if r > melhor:
                            melhor, mj = r, j
                    if mj is not None and melhor >= 0.5:
                        for j in range(bs[usados], mj):
                            ins[a].append(tb[j])
                        leit[a] = tb[mj]
                        usados = bs.index(mj) + 1 - 0
                        usados = mj - b0 + 1
                for j in range(b0 + usados, b1):
                    ins[a1].append(tb[j])
            elif op == 'insert':
                ins[a0] += tb[b0:b1]
    return leit, ins


LIMPA = re.compile(r"^[A-Za-zÀ-ÿçãõẽũ'’\-]+$")


def plausivel(t):
    """Penalidade para formas que o OCR inventa."""
    if not t or t.startswith('@'):
        return 0
    p = 0
    if not LIMPA.match(t) and len(t) > 1:
        p += 1.0
    if re.search(r'[íìî](?=[lLTtFfI])|[a-zç][TFIL]|[a-z][A-Z](?!ei)', t) and not re.match(r"^(el|del|dal|ael|al)Rei", t):
        p += 0.6
    if re.search(r'[0-9^]', t):
        p += 1.0
    return p


def norm(t):
    return sem_acento(t).replace('f', 's').replace('ſ', 's')


def escolher(leituras):
    """leituras: {sigla: forma}. Devolve (forma, apoio)."""
    cands = {f for f in leituras.values()}
    melhor, mp = None, -9
    for c in cands:
        ap = 0.0
        for s, f in leituras.items():
            if f == c:
                ap += PESO[s]
            elif norm(f) == norm(c):
                ap += PESO[s] * 0.95
            elif f and c:
                ap += PESO[s] * 0.6 * max(0, SequenceMatcher(None, norm(f).lower(), norm(c).lower()).ratio() - 0.5) * 2
        ap -= plausivel(c)
        if c == '':
            ap -= 0.3
        if ap > mp:
            melhor, mp = c, ap
    return melhor, mp


def main(pasta):
    T = {s: tokens(os.path.join(pasta, s + '.txt')) for s in 'ABCD'}
    PIV = 'D'
    OUT = [x for x in 'ABCD' if x != PIV]
    piv = T[PIV]
    L = {PIV: piv}
    INS = {}
    for s in OUT:
        L[s], INS[s] = alinhar(piv, T[s])
        # palavra partida no fim da linha sem hífen: o pedaço que sobrou junta-se ao vizinho
        for i in list(INS[s]):
            ins = INS[s][i]
            if ins and i > 0 and L[s][i - 1] and SequenceMatcher(None, chave(L[s][i - 1] + ins[0]), chave(piv[i - 1])).ratio() > \
                    SequenceMatcher(None, chave(L[s][i - 1]), chave(piv[i - 1])).ratio() + 0.05:
                L[s][i - 1] += ins.pop(0)
            if ins and i < len(piv) and L[s][i] and SequenceMatcher(None, chave(ins[-1] + L[s][i]), chave(piv[i])).ratio() > \
                    SequenceMatcher(None, chave(L[s][i]), chave(piv[i])).ratio() + 0.05:
                L[s][i] = ins.pop() + L[s][i]
    saida, linhas, slots = [], [], []
    for i, b in enumerate(piv):
        # inserções que dois testemunhos ou mais trazem antes desta posição
        cand = [tuple(x for x in INS[s].get(i, []) if re.match(r"^[A-Za-zÀ-ÿçãõẽũ]{2,}$", x)) for s in OUT]
        cnt = collections.Counter(tuple(chave(x) for x in c) for c in cand if c)
        if cnt:
            k, n = cnt.most_common(1)[0]
            if n >= 2:
                forma = next(c for c in cand if tuple(chave(x) for x in c) == k)
                for k, x in enumerate(forma):
                    lx = {s: (c[k] if len(c) == len(forma) else '') for s, c in zip(OUT, cand)}
                    slots.append({PIV: '', **lx, 'ins': True})
                    saida.append(x)
                    linhas.append(f'+\t\t\t\t{x}\tins')
        if b.startswith('@'):
            slots.append({'m': b})
            saida.append(b)
            linhas.append(f'{b}\t\t\t\t{b}\t')
            continue
        le = {s: L[s][i] for s in 'ABCD'}
        slots.append(dict(le))
        f, ap = escolher(le)
        if f:
            saida.append(f)
        linhas.append('\t'.join([le['B'], le['A'], le['C'], le['D'], f, f'{ap:.2f}']))
    json.dump(slots, open(os.path.join(pasta, 'slots.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    open(os.path.join(pasta, 'voto.tsv'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    txt = ' '.join(saida)
    txt = re.sub(r' ?(@@ [A-Z]+(?: \d+)?|@T|@F|@CAP \S+) ?', r'\n\1\n', txt)
    open(os.path.join(pasta, 'voto.txt'), 'w', encoding='utf-8').write(txt)


if __name__ == '__main__':
    main(sys.argv[1])
