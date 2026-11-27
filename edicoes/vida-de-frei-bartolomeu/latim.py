"""Vida de D. Frei Bertolameu dos Mártires — os trechos em latim (citações da Escritura e dos Padres), que
1619 compõe em itálico: vão em itálico e sem mudança de grafia.

Vocabulário latino: as palavras dos originais latinos já na Biblioteca (Confissões, Regra Pastoral, Vida de
Santo Agostinho, de São Martinho, de São Bento, de São Paulo eremita, São Cipriano, São Patrício, Perpétua).
Trecho latino: sequência de palavras que são latinas e não portuguesas, ou de ambas (in, a, non…), com pelo
menos duas só latinas (ou uma longa, de 7 letras ou mais), a partir da primeira e até a última só latina.
"""
import glob
import os
import re
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
OBRAS = ['confissoes', 'regra-pastoral', 'vida-de-santo-agostinho', 'vida-de-sao-martinho', 'vida-de-sao-bento',
         'sobre-a-unidade-da-igreja', 'confissao-de-sao-patricio', 'paixao-de-perpetua', 'vida-de-sao-paulo-eremita']
_LA = None
# formas que 1619 escreve à portuguesa mas são latinas nas citações (u por v, j por i)
EXTRA = {'iustitiam', 'iudicate', 'utiq', 'vtique', 'ergo', 'filii', 'hominum', 'dominus', 'domine', 'deus', 'dei',
         'eius', 'ejus', 'quia', 'quod', 'enim', 'sicut', 'super', 'autem', 'etiam', 'nobis', 'vobis', 'tibi', 'mihi'}


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def vocabulario():
    global _LA
    if _LA is None:
        la = set(EXTRA)
        for o in OBRAS:
            for f in glob.glob(os.path.join(RAIZ, 'edicoes', o, 'original', '*.txt')):
                for w in re.findall(r'[A-Za-zæœ]+', open(f, encoding='utf-8').read()):
                    w = w.lower().replace('æ', 'ae').replace('œ', 'oe')
                    la.add(w)
                    la.add(w.replace('v', 'u'))
                    la.add(w.replace('j', 'i'))
        _LA = la
    return _LA


def norm(t):
    return sem_acento(re.sub(r'[^A-Za-zÀ-ÿ]', '', t)).lower()


def trechos(palavras, e_portuguesa):
    """palavras: lista de tokens (com pontuação); e_portuguesa(w) → bool. Devolve [(início, fim)] (fim incluso)."""
    la = vocabulario()
    tipo = []
    for t in palavras:
        w = norm(t)
        if not w:
            tipo.append('x')
            continue
        L = w in la or w.replace('v', 'u') in la
        P = e_portuguesa(t)
        tipo.append('L' if L and not P else ('A' if L and P else 'P'))
    out = []
    i = 0
    while i < len(tipo):
        if tipo[i] != 'L':
            i += 1
            continue
        j = i
        while j + 1 < len(tipo) and tipo[j + 1] in 'LAx':
            j += 1
        while j > i and tipo[j] != 'L':
            j -= 1
        n_l = sum(1 for k in range(i, j + 1) if tipo[k] == 'L')
        longa = any(len(norm(palavras[k])) >= 7 for k in range(i, j + 1) if tipo[k] == 'L')
        if n_l >= 2 or (n_l == 1 and longa and j == i):
            # inclui palavras ambíguas logo antes (In principio…), se começam com maiúscula
            while i > 0 and tipo[i - 1] == 'A' and palavras[i - 1][:1].isupper():
                i -= 1
            out.append((i, j))
        i = j + 1
    return out
