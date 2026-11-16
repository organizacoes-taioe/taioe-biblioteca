#!/usr/bin/env python3
"""Monta o texto espanhol da Subida e da Noite pela edição de Silverio de Santa Teresa (Burgos, 1929, t. II),
a partir de três leituras (OCR) do mesmo fac-símile do Internet Archive.

Testemunhos (todos baixados em --fontes; ver original/LEIAME.md):
  silv.json  OCR do Internet Archive de «obrasdesanjuande02john» (_djvu.xml, lido por paginas.py)
  bmc.json   OCR do mesmo fac-símile reprocessado em «BMC11ObrasDeSanJuanDeLaCruzTomoIISubidaYNocheOscura»
  tess/      Tesseract 5 (spa, tessdata_best) sobre as imagens jp2 de «obrasdesanjuande02john»
  es_full.txt lista de frequência do espanhol (FrequencyWords), para desempate e acentuação

Método:
  1. em cada página, as linhas do OCR do IA são classificadas: cabeço (sai), nota de rodapé (sai: letra menor,
     medida pela largura por caractere e pela altura da linha), título em maiúsculas, verso (recuado), prosa;
  2. as palavras das três leituras são alinhadas (difflib) e decididas por maioria; sem maioria, pela lista
     de frequência, e a dúvida vai para o relatório (--duvidas), com página e caixa da linha, para conferir
     na imagem;
  3. sai o que é de Silverio e não do autor: as chamadas de nota «(1)», os números de página, os cabeços;
  4. parágrafos pelos números de Silverio («1.», «2.» …), que viram as marcas [L.1] (primeiro parágrafo do
     capítulo) e [n]; versos com «| »; títulos internos em itálico;
  5. acentuação de hoje: palavra sem acento que só existe acentuada (asi → así, mia → mía, habia → había),
     «fué/dió/vió» → «fue/dio/vio»; as formas do autor (aprovecharme he, esotro, aquesta, substancia) ficam;
  6. emendas à mão, conferidas na imagem: EMENDAS abaixo (por obra), aplicadas por último.

Uso:
  python3 -I montar.py --fontes ~/.cache/claude-pedidos-1611/tmp-subida-noite-escura --obra subida --livro 1
  (--livro 0 = argumento, canções e prólogo; --duvidas arq.tsv grava as dúvidas; --bruto mostra o texto sem
  dividir em arquivos)
O resultado vai para o arquivo do livro (ver ARQUIVOS); o cabeçalho «# » de cada arquivo vem de CABECALHO.
"""
import argparse
import collections
import difflib
import glob
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- páginas de cada livro (índices do djvu)
# (obra, livro): (primeira, última) página, inclusive; conferidas à mão no djvu.
PAGINAS = {
    ('subida', 0): (16, 24),
    ('subida', 1): (25, 78),
    ('subida', 2): (79, 251),
    ('subida', 3): (252, 371),
    ('noche', 0): (372, 376),
    ('noche', 1): (377, 426),
    ('noche', 2): (427, 523),   # 524: fe de erratas (aplicada nas EMENDAS)
}
INDICE = (526, 541)

ROMANOS = {1: 'I', 2: 'II', 3: 'III'}
LIVRO_NOME = {'PRIMERO': 1, 'SEGUNDO': 2, 'TERCERO': 3}


def ler_tess(arq):
    linhas = collections.OrderedDict()
    if not os.path.exists(arq):
        return []
    for ln in open(arq, encoding='utf-8'):
        c = ln.rstrip('\n').split('\t')
        if len(c) < 12 or c[0] != '5':
            continue
        if not c[11].strip():
            continue
        linhas.setdefault((c[2], c[3], c[4]), []).append(c[11])
    return [w for ws in linhas.values() for w in ws]


def letras(s):
    return [ch for ch in s if ch.isalpha()]


def maiusc(s):
    ls = letras(s)
    return len(ls) >= 3 and sum(ch.isupper() for ch in ls) >= 0.8 * len(ls)


# ---------------------------------------------------------------- classificação das linhas
def pequena(l, W):
    """Linha longa em letra de nota (corpo menor): largura por caractere e altura."""
    x0, y0, x1, y1, t = l[:5]
    if len(t) < 30 or maiusc(t):
        return False
    r = (x1 - x0) / len(t) / W
    h = (y1 - y0) / W
    return r < 0.0101 or (r < 0.0106 and h < 0.0170)


def classificar(pag, ipag=None):
    W, H = pag['W'], pag['H']
    L = pag['linhas']
    longas = [l for l in L if len(l[4]) >= 30 and not maiusc(l[4])]
    xs = sorted(l[0] for l in longas)
    margem = xs[len(xs) // 4] if xs else 0.1 * W
    out = []
    pe = False
    abre_livro = False   # entre «LIBRO …» e «CAPITULO I»: o sumário vem em letra pequena e não é nota
    for k, l in enumerate(L):
        x0, y0, x1, y1, t, pid = l
        r = (x1 - x0) / max(1, len(t)) / W
        h = (y1 - y0) / W
        if k < 3 and y0 / H < 0.1 and (maiusc(t) or re.fullmatch(r'[\dIl\W]+', t.strip())
                                       or (sum(c.isupper() for c in t) >= 0.5 * max(1, len(letras(t)))
                                           and re.search(r'L.?I.?B.?R.?O|N.?O.?C.?H|SUBIDA|C.?A.?P\b|\bCAP|IMERO|IMFRO|EGUNDO|ERCERO',
                                                         t.upper()))):
            out.append('cabeco')
            continue
        if (k < 3 and y0 / H < 0.075 and len(t) < 32 and x0 - margem > 0.12 * W
                and all(L[j][1] - y0 > 0.03 * H for j in range(k + 1, min(k + 2, len(L))) if L[j][1] > y0 + 5)):
            out.append('cabeco')   # cabeço centrado que o OCR leu como minúsculas («kochf oscrsA»)
            continue
        if (ipag, k) in CLASSE_FORCADA:
            out.append(CLASSE_FORCADA[(ipag, k)])
            continue
        if maiusc(t) and re.match(r'^\[?L\s?I\s?B\s?R\s?O\s', t.strip()) and k < 4:
            abre_livro = True
            out.append('maiusc')
            continue
        if abre_livro:
            if maiusc(t):
                abre_livro = False   # CAPITULO ou CANCION: daqui em diante, a classificação de sempre
            else:
                out.append('prosa')
                continue
        if ipag in NOTAS_DESDE:
            pe = k >= NOTAS_DESDE[ipag]
        elif not pe:
            if pequena(l, W) and k + 1 < len(L) and pequena(L[k + 1], W):
                pe = True
            elif re.match(r'^\d{1,2}\s+[^\s\.,]', t) and h < 0.0175 and k > 0:
                pe = True
            elif (re.match(r'^[\dIl]{1,2}\s+\S', t) and not re.match(r'^[\dIl]{1,2}\s?[\dIl]?\s?\.', t)
                  and y0 / H > 0.6 and r < 0.0116 and k > 0):
                pe = True
            elif (re.match(r'^[\dIl]{1,2}\s+\S', t) and y0 / H > 0.6 and k > 0
                  and re.search(r'\b[eE]\.\s?p\.|C[óo]dice|\bAlc\.|\bAle\.', t)):
                pe = True   # nota de variante em negrito (largura de corpo)
        if pe:
            out.append('nota')
            continue
        if maiusc(t):
            out.append('maiusc')
        elif x0 - margem > 0.15 * W and len(t) < 60:
            out.append('verso')
        else:
            out.append('prosa')
    return out, margem


# ---------------------------------------------------------------- votação das três leituras
def chave(w):
    return w


class Vocab:
    def __init__(self, arq):
        self.f = {}
        for ln in open(arq, encoding='utf-8'):
            p = ln.split()
            if len(p) == 2:
                self.f[p[0]] = int(p[1])

    def freq(self, w):
        w = re.sub(r'[^\w]', '', w).lower()
        if not w:
            return 10 ** 6
        if w.isdigit():
            return 1000
        return self.f.get(w, 0)

    def nota(self, span):
        ws = span.split()
        if not ws:
            return 0
        return min(self.freq(w) for w in ws)


def mapear(a, b):
    """Para cada índice de a, o índice correspondente de b (ou None), e os trechos não iguais."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sm.get_opcodes()


def votar_pagina(ta, tb, tc, vocab, duvidas, info, importa=None, dono=None):
    """ta: tokens do IA (pivô); devolve lista do mesmo tamanho com a escolha para cada token de ta
    (string, pode ser vazia ou com espaço), decidida por maioria entre ta, tb, tc."""
    escolha = list(ta)
    na = [unicodedata.normalize('NFC', w) for w in ta]
    ops_b = mapear(na, tb)
    ops_c = mapear(na, tc)

    def fatia(ops, i1, i2, outro):
        """Texto de 'outro' que corresponde a na[i1:i2] (aproximado nos trechos desiguais)."""
        partes = []
        for op, a1, a2, b1, b2 in ops:
            if a2 <= i1 and not (a1 == a2 == i1):
                continue
            if a1 >= i2 and not (a1 == a2 == i2 and False):
                break
            if op == 'equal':
                lo, hi = max(a1, i1), min(a2, i2)
                partes += outro[b1 + lo - a1:b1 + hi - a1]
            elif op == 'insert':
                if i1 < a1 < i2:
                    partes += outro[b1:b2]
            else:
                if a1 >= i1 and a2 <= i2:
                    partes += outro[b1:b2]
                elif a2 - a1 == b2 - b1:
                    lo, hi = max(a1, i1), min(a2, i2)
                    partes += outro[b1 + lo - a1:b1 + hi - a1]
                else:
                    return None
        return ' '.join(partes)

    for op, a1, a2, b1, b2 in ops_b:
        if op == 'equal':
            # pode haver diferença que o Tesseract desfaz? a igualdade de dois basta
            continue
        if op == 'insert':
            # B tem palavras a mais: só entram se o Tesseract também as tiver
            ins = ' '.join(tb[b1:b2])
            ref = fatia(ops_c, a1, a1, tc) if a1 > 0 else None
            # verifica no Tesseract o vizinho: texto entre na[a1-1] e na[a1]
            ctx = fatia(ops_c, max(0, a1 - 1), min(len(na), a1 + 1), tc) or ''
            viz = ' '.join(na[max(0, a1 - 1):a1 + 1])
            if ins and ins in ctx and ins not in viz and a1 > 0:
                escolha[a1 - 1] = escolha[a1 - 1] + ' ' + ins
                if importa is None or importa[a1 - 1]:
                    duvidas.append((info, dono[a1 - 1] if dono else '', viz, ins, '', 'acrescentado (B=C)'))
            continue
        # replace ou delete: trecho a1:a2
        if a2 - a1 == b2 - b1 and op == 'replace':
            pares = [(i, tb[b1 + i - a1]) for i in range(a1, a2)]
        else:
            pares = [((a1, a2), ' '.join(tb[b1:b2]))]
        for idx, cand_b in pares:
            i1, i2 = (idx, idx + 1) if isinstance(idx, int) else idx
            cand_a = ' '.join(na[i1:i2])
            cand_c = fatia(ops_c, i1, i2, tc)
            if cand_c is not None and cand_c == cand_b:
                ganha, motivo = cand_b, 'B=C'
            elif cand_c is not None and cand_c == cand_a:
                ganha, motivo = cand_a, 'A=C'
            else:
                fa, fb = vocab.nota(cand_a), vocab.nota(cand_b)
                if fb > fa:
                    ganha = cand_b
                elif fa > fb:
                    ganha = cand_a
                else:
                    ganha = cand_b if cand_b else cand_a
                motivo = 'sem maioria'
                if importa is None or any(importa[i1:max(i2, i1 + 1)]):
                    duvidas.append((info, dono[i1] if dono else '', cand_a, cand_b, cand_c, ganha))
            escolha[i1] = ganha
            for j in range(i1 + 1, i2):
                escolha[j] = ''
    return escolha


# ---------------------------------------------------------------- montagem
NUM = re.compile(r'^([\dIlO|]{1,3})[\.,]$')


def limpar_chamadas(s):
    s = re.sub(r'\s*\((?:\d{1,2}|[íilIoOsSí]|\d[íil]|[íil]\d|\d\s?\d)\)', '', s)
    s = re.sub(r'\s*\(\s?(?:\d{1,2})\s?\)', '', s)
    return s


def juntar_linhas(linhas):
    """Junta linhas de prosa, desfazendo a hifenização."""
    out = ''
    for t in linhas:
        t = t.strip()
        if not t:
            continue
        if out.endswith('-') and not out.endswith('--') and t[:1].isalpha() and not out.endswith(' -'):
            out = out[:-1] + t
        elif out:
            out += ' ' + t
        else:
            out = t
    return out


VOGAIS = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú'}
SEM_ACENTO = str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
OBSOLETOS = {'hán': 'han', 'fué': 'fue', 'fuí': 'fui', 'dió': 'dio', 'vió': 'vio', 'pié': 'pie', 'ví': 'vi', 'dí': 'di',
             'fuése': 'fuese', 'Fué': 'Fue', 'Dió': 'Dio', 'Vió': 'Vio'}
# palavras válidas sem acento que não se tocam (o contexto decide; ficam como Silverio imprimiu)
AMBIGUAS = set('''si sí mi mí tu tú el él que qué como cómo cuan cuán cuanto cuánto donde dónde esta está ésta
este éste ese ése solo sólo mas más aun aún de dé se sé te té seria sería perdida pérdida cual cuál quien quién
cuando cuándo ultimo continuo continúo practica práctica publico público animo ánimo sabia sabía habito hábito
deposito depósito termino término intimo íntimo limite límite medico médico vario varío varia varía envio envío
estas estás estos éstos esos ésos aquel aquél aquella aquélla aquellos aquéllos esa ésa esas ésas ejercito ejército
transito tránsito animas ánimas hacia hacía cuántos cuántas cuánta cuánto dónde cómo cuál cuáles quiénes
adónde qué'''.split())


DEMONST = set('''solo este esta estos estas ese esa esos esas aquel aquella aquellos aquellas aquello esto eso
'''.split())
VOG = 'aeiouáéíóúü'


def grupos_depois(w, i):
    """Quantos grupos de vogais há depois da posição i."""
    n = 0
    for g in re.findall(r'[aeiouáéíóúü]+', w[i + 1:].lower()):
        n += max(1, sum(ch in 'aeoáéóíú' for ch in g))
    return n


def acentuar(texto, vocab, log):
    def troca(m):
        w = m.group(0)
        if w in OBSOLETOS:
            log[(w, OBSOLETOS[w])] += 1
            return OBSOLETOS[w]
        lw = w.lower()
        if lw in AMBIGUAS or len(lw) < 2 or w in LATIM_PROTEGIDO:
            return w
        base = lw.translate(SEM_ACENTO)
        if base != lw:
            # já acentuada: só tira o acento que a regra de hoje não quer (quedéme → quedeme, dióle → diole):
            # palavra grave terminada em vogal, n ou s, com o acento numa vogal seguida de consoante
            if base in DEMONST:
                return w
            k = next(i for i, ch in enumerate(lw) if ch in 'áéíóú')
            if lw[k] in 'íú' and ((k > 0 and lw[k - 1] in VOG) or (k + 1 < len(lw) and lw[k + 1] in VOG)):
                return w   # hiato (poseída, oíros)
            if (grupos_depois(lw, k) == 1 and lw[-1] in 'aeiouns' and k + 1 < len(lw)
                    and lw[k + 1] not in VOG):
                novo = w[:k] + w[k].translate(SEM_ACENTO) + w[k + 1:]
                log[(w, novo)] += 1
                return novo
            return w
        f0 = vocab.f.get(lw, 0)
        if re.search(r'(re|res|ren)$', lw):
            return w   # futuro do subjuntivo (juzgare, pidiere): nunca leva acento
        cands = {}
        for i, ch in enumerate(base):
            if ch in VOGAIS:
                v = base[:i] + VOGAIS[ch] + base[i + 1:]
                cands[v] = vocab.f.get(v, 0)
        if not cands:
            return w
        melhor = max(cands, key=cands.get)
        if cands[melhor] > max(50, 20 * f0) and melhor not in AMBIGUAS:
            novo = melhor
            if w[0].isupper():
                novo = novo[0].upper() + novo[1:]
            if w.isupper():
                novo = novo.upper()
            log[(w, novo)] += 1
            return novo
        return w
    return re.sub(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+', troca, texto)


def carregar(fontes):
    A = json.load(open(os.path.join(fontes, 'silv.json'), encoding='utf-8'))
    B = json.load(open(os.path.join(fontes, 'bmc.json'), encoding='utf-8'))
    return A, B


# número de parágrafo de Silverio mal lido pelas três leituras, conferido na imagem:
# (página djvu, linha): (número, True = troca o primeiro token lido; False = o número faltava)
NUMERO_FORCADO = {
    (84, 5): (1, True), (104, 15): (5, True), (185, 19): (1, True), (217, 23): (1, True),
    (297, 19): (3, True), (316, 15): (5, True), (354, 18): (3, True), (366, 21): (4, True),
    (382, 23): (6, True), (427, 5): (1, True), (507, 24): (5, True), (513, 23): (4, False), (400, 2): (2, False),
}

# classe de linha corrigida à mão (título que o classificador tomou por nota)
CLASSE_FORCADA = {(217, 22): 'maiusc'}
# páginas em que o classificador tomou o corpo por nota (número de parágrafo sem ponto): notas só desta linha em diante
NOTAS_DESDE = {242: 34, 400: 32}


def linhas_votadas(A, B, fontes, ini, fim, vocab, duvidas):
    """Devolve a lista de linhas [(classe, texto, pagina, y0, x0, margem, W)] das páginas ini..fim."""
    saida = []
    for i in range(ini, fim + 1):
        pa, pb = A[i], B[i]
        classes, margem = classificar(pa, i)
        ta, dono = [], []
        for k, l in enumerate(pa['linhas']):
            for w in l[4].split():
                ta.append(w)
                dono.append(k)
        tb = [unicodedata.normalize('NFC', w) for l in pb['linhas'] for w in l[4].split()]
        nome = pa['pag'].replace('.djvu', '')
        tc = [unicodedata.normalize('NFC', w) for w in ler_tess(os.path.join(fontes, 'tess', nome + '.tsv'))]
        info = f'p{i}'
        importa = [classes[k] in ('prosa', 'verso', 'maiusc') for k in dono]
        esc = votar_pagina(ta, tb, tc, vocab, duvidas, info, importa, dono)
        por_linha = collections.defaultdict(list)
        for w, k in zip(esc, dono):
            if w:
                por_linha[k].append(w)
        for k, l in enumerate(pa['linhas']):
            txt = ' '.join(por_linha[k])
            m = re.match(r'^([\dIl|]{1,2})\s?\.\s', l[4])
            if m and classes[k] == 'prosa' and not re.match(r'^[\dIl|]{1,2}\s?\.', txt):
                txt = m.group(1) + '. ' + re.sub(r'^\S{1,2}\.\s', '', txt)   # o voto apagou o número do parágrafo (as outras leituras não o tinham)
            if (i, k) in NUMERO_FORCADO:
                n, apaga = NUMERO_FORCADO[(i, k)]
                txt = f'{n}. ' + (txt.split(' ', 1)[1] if apaga else txt)
            saida.append((classes[k], txt, i, l[1], l[0], margem, pa['W'], l[3]))
    return saida


def montar_livro(linhas, livro, obra):
    """Linhas classificadas → lista de blocos: ('livro', n), ('sumario', txt), ('cap', n, titulo_maiusc),
    ('sub', txt), ('par', num, txt), ('verso', [linhas])."""
    blocos = []
    estado = None
    prosa = []
    versos = []
    ultimo_y = None
    cancoes = False

    num_atual = None
    esperado = 1
    avisos = []

    def fecha():
        nonlocal prosa, versos, num_atual
        if prosa:
            blocos.append(['par', num_atual, juntar_linhas(prosa)])
            prosa = []
            num_atual = None
        if versos:
            blocos.append(['verso', versos])
            versos = []

    def numero(t):
        """Número de parágrafo de Silverio no começo da linha («12.», «1 1 .», «2 Digo»): (n, resto) ou None."""
        m = re.match(r'^([\dIl|]{1,2}(?:\s?[\dIl|])?)\s?([\.,]?)\s*(\S.*)$', t)
        if not m:
            return None
        d = re.sub(r'\s', '', m.group(1)).replace('I', '1').replace('l', '1').replace('|', '1')
        if not d.isdigit():
            return None
        if not m.group(2) and not m.group(3)[:1].isupper() and m.group(3)[:1] not in '¡¿«"':
            return None
        return int(d), m.group(3), bool(m.group(2))

    for cl, t, pag, y0, x0, margem, W, y1 in linhas:
        if cl in ('cabeco', 'nota') or not t.strip():
            continue
        if cl == 'maiusc':
            fecha()
            tt = t.strip()
            if re.match(r'^\[?L\s?I\s?B\s?R\s?O\s', tt) and any(k in tt for k in LIVRO_NOME):
                blocos.append(['livro', tt])
                estado = 'sumario'
            elif re.match(r'^CAP[IÍ]TULO', tt):
                blocos.append(['cap', tt, []])
                esperado = 1
                estado = 'titcap'
            elif estado == 'titcap' and not re.match(r'^(CANCI[OÓ]N|DECLARACI)', tt):
                blocos[-1][2].append(tt)
            else:
                if blocos and blocos[-1][0] == 'sub' and not re.match(r'^(ARGUMENTO|PR[OÓ]LOGO|CANCIONES)\b', tt) \
                        and not re.match(r'^(ARGUMENTO|PR[OÓ]LOGO|CANCIONES)\b', blocos[-1][1]):
                    blocos[-1][1] += ' ' + tt
                else:
                    blocos.append(['sub', tt])
                estado = None
                if re.match(r'^CANCIONES', tt) and livro == 0:
                    cancoes = True
                elif cancoes and any(x[0] == 'verso' for x in blocos):
                    cancoes = False
                elif re.match(r'^(PR[OÓ]LOGO|ARGUMENTO)', tt):
                    cancoes = False
                    esperado = 1
            ultimo_y = None
            continue
        if cancoes and cl == 'prosa':
            cl = 'verso'
        if estado == 'sumario':
            blocos.append(['sumario', t])
            continue
        if estado == 'titcap':
            estado = None
        if cl == 'verso' and prosa and not versos and not re.search(r'[:\.;!?»\)]\s*$', prosa[-1]):
            cl = 'prosa'   # linha de prosa com caixa torta no OCR (continua a frase de cima)
        if cl == 'verso':
            if prosa:
                fecha()
            # estrofe nova: número «2.—» ou salto grande
            if versos and (re.match(r'^[\dJIl]{1,2}\.\s?[—-]', t) or (ultimo_y is not None and y0 - ultimo_y > 0.07 * W)):
                blocos.append(['verso', versos])
                versos = []
            versos.append(t)
            ultimo_y = y0
            continue
        # prosa
        if versos:
            fecha()
        nn = numero(t)
        if nn and (nn[0] == esperado or (nn[2] and nn[0] == esperado + 1)
                   or (nn[2] and esperado == 1 and nn[0] in (10, 11))):
            if nn[0] != esperado:
                avisos.append(f'p{pag}: parágrafo {nn[0]} lido, esperado {esperado}')
                if nn[0] in (10, 11) and esperado == 1:
                    nn = (1,) + nn[1:]
            fecha()
            num_atual = nn[0]
            esperado = nn[0] + 1
            t = nn[1]
        prosa.append(t)
        ultimo_y = y0
    fecha()
    for a_ in avisos:
        print('aviso:', a_, file=sys.stderr)
    return blocos


ROM = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
       'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
       'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII',
       'XLIII', 'XLIV', 'XLV']


def romano(s):
    """Lê o número romano de um título de capítulo do OCR (tolerante: Vil, VIH, Xfl, X1J11…)."""
    s = s.upper().replace('PRIMERO', 'I')
    s = s.replace('1', 'I').replace('L', 'L').replace('H', 'II').replace('J', 'I').replace('U', 'II')
    s = s.replace('N', 'II').replace('D', 'II').replace('Ü', 'II').replace('F', 'I').replace('Í', 'I')
    s = re.sub(r'[^IVXL]', '', s)
    if s not in ROM and s.replace('L', 'I') in ROM:
        s = s.replace('L', 'I')
    return ROM.index(s) if s in ROM else None


def titulos_indice(A, B, fontes, vocab):
    """{(obra, livro, cap): título} lidos do índice do volume (pp. 513 ss.), que tem os títulos em caixa baixa."""
    d = []
    linhas = linhas_votadas(A, B, fontes, INDICE[0], INDICE[1], vocab, d)
    obra, livro = 'subida', 0
    ents = []
    for cl, t, *_ in linhas:
        t = t.strip()
        if not t or re.fullmatch(r'[\dIl\W]+', t) or t in ('ÍNDICE', 'INDICE.', 'Página', 'DE CAPITULOS', 'INDICE'):
            continue
        if t.startswith('SUBIDA DEL MONTE'):
            continue
        if t.startswith('NOCHE OSCURA'):
            obra, livro = 'noche', 0
            continue
        m = re.match(r'^LIBRO\s+(PRIMERO|SEGUNDO|TERCERO)', t)
        if m:
            livro = LIVRO_NOME[m.group(1)]
            continue
        if re.match(r'^(ARGUMENTO|PROLOGO|PRÓLOGO)', t):
            continue
        m = re.match(r'^CAP[IÍ]TULO\s+([A-Z0-9ÜÍ]+)\s*[\.\-—–]*\s*(.*)$', t)
        if m:
            ents.append([obra, livro, romano(m.group(1)), m.group(2)])
        elif ents:
            ents[-1][3] = juntar_linhas([ents[-1][3], t])
    out = {}
    for obra, livro, cap, tit in ents:
        tit = re.sub(r'[\s\.]*[\dIlHl\\]{1,3}\s*$', '', tit).strip(' .—-')
        tit = re.sub(r'\s*[\.,]?—\s*', '. — ', tit) if '—' in tit else tit
        tit = re.sub(r'\.\s*\.\s*—', '. —', tit)
        out[(obra, livro, cap)] = acentuar(tit, vocab, collections.Counter())
    return out


def frase(t, vocab):
    """Título em maiúsculas → caixa baixa com acentos (DECLARACION DE LA CANCION → Declaración de la canción)."""
    t = limpar_chamadas(t).strip(' .')
    t = t[:1].upper() + t[1:].lower()
    for nome in ('Dios', 'Amado', 'Esposo'):
        t = re.sub(r'\b' + nome.lower() + r'\b', nome, t)
    return acentuar(t, vocab, collections.Counter())


def limpar_par(t):
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'(^|(?<=[\s«"(]))[ijlI1]\s?(?=(Oh|Qué|Cuán|Cuánto|Cuánta|Ay|Ah|Oh,)\b)', '¡', t)
    t = re.sub(r'\s+([,;:\.\)!?»])', r'\1', t)
    t = re.sub(r'([?!])\.(?=\s|$)', r'\1', t)   # «?.» que sobra da chamada de nota tirada
    t = re.sub(r'([\(«¡¿])\s+', r'\1', t)
    return t


def render(blocos, obra, livro, titulos, vocab):
    livro = livro
    """Blocos → texto no formato da Biblioteca (sem o cabeçalho «# »)."""
    out = []
    cap = 0
    primeiro = False
    R = ROMANOS.get(livro, '')
    pendente = None   # marca a pôr no próximo bloco (número de Silverio num parágrafo que só abre versos)
    i = 0
    while i < len(blocos):
        b = blocos[i]
        tipo = b[0]
        if tipo == 'livro':
            pass
        elif tipo == 'sumario':
            txt = ' '.join(x[1] for x in blocos[i:] if x[0] == 'sumario')
            n = sum(1 for x in blocos[i:] if x[0] == 'sumario')
            # só os sumários seguidos
            j = i
            partes = []
            while j < len(blocos) and blocos[j][0] == 'sumario':
                partes.append(blocos[j][1])
                j += 1
            txt = limpar_par(juntar_linhas(partes)).strip('[]{}() .')
            txt = re.sub(r'[\]\}]\s*\.?$', '', txt)
            out.append('_' + txt.rstrip('.') + '._')
            i = j
            continue
        elif tipo == 'cap':
            n = romano(b[1].replace('CAPITULO', '').replace('CAPÍTULO', ''))
            if n and cap < n <= cap + 2:
                if n != cap + 1:
                    print(f'aviso: falta o título do capítulo {cap + 1} (veio junto do anterior)', file=sys.stderr)
                cap = n
            else:
                cap += 1
                if n != cap:
                    print(f'aviso: capítulo lido {n}, esperado {cap}', file=sys.stderr)
            tit = titulos.get((obra, livro, cap)) or frase(' '.join(b[2]), vocab)
            corpo = frase(' '.join(b[2]), vocab) if b[2] else ''
            if corpo and (obra, livro, cap) not in ((('subida', 3, 40),)) and difflib.SequenceMatcher(None, _norm(tit), _norm(corpo)).ratio() < 0.6:
                print(f'aviso: título do índice não bate com o do corpo no capítulo {cap}; fica o do corpo', file=sys.stderr)
                tit = corpo
            out.append(f'## {cap}. {tit}'.rstrip(' .') if tit else f'## {cap}.')
            primeiro = True
        elif tipo == 'sub':
            t = b[1]
            if livro == 0 and (t.startswith('SUBIDA DEL MONTE') or t.startswith('NOCHE OSCURA')):
                pass
            elif re.match(r'^(ARGUMENTO|PR[OÓ]LOGO|CANCIONES)$', t.strip(' .')):
                out.append('## ' + frase(t, vocab).replace('Prologo', 'Prólogo'))
            elif t.startswith('FIN DEL LIBRO'):
                out.append('_' + frase(t, vocab) + '._')
            else:
                marca = f'[{pendente}] ' if pendente else ''
                pendente = None
                out.append(marca + '_' + frase(t, vocab) + '_')
        elif tipo == 'par':
            num, txt = b[1], limpar_par(b[2])
            # parágrafo curto que só abre uma série de versos («12. —Cuando reparas en algo,»)
            if txt.startswith('—') and len(txt) < 70 and i + 1 < len(blocos) and blocos[i + 1][0] == 'verso':
                blocos[i + 1][1].insert(0, txt)
                if num:
                    if out and out[-1].startswith('_') and not out[-1].startswith('['):
                        out[-1] = f'[{num}] ' + out[-1]
                    else:
                        pendente = num
                i += 1
                continue
            if livro == 0 and not num and not any(x.startswith('## ') for x in out):
                out.append('_' + txt + '_')
                i += 1
                continue
            if num and primeiro and R:
                marca = f'[{R}.{cap}] '
                primeiro = False
            elif num:
                marca = f'[{num}] '
            else:
                marca = ''
            out.append(marca + txt)
        elif tipo == 'verso':
            estrofes = [[]]
            for v in b[1]:
                v = limpar_par(v)
                v = re.sub(r'^[\dJIl]{1,2}\.\s*[—-]\s*', '', v)
                v = re.sub(r'\s*[»\*]$', '', v) if v.endswith(' »') or v.endswith(' *') else v
                if v.startswith('—') and estrofes[-1]:
                    estrofes.append([])
                v = v.lstrip('— ').strip()
                if v:
                    estrofes[-1].append(v)
            for e in estrofes:
                if e:
                    out.append('\n'.join('| ' + v for v in e))
        i += 1
    return '\n\n'.join(out) + '\n'


# ---------------------------------------------------------------- arquivos de saída
EDICOES = os.path.normpath(os.path.join(AQUI, '..', '..'))
PASTA = {'subida': 'subida-do-monte-carmelo', 'noche': 'noite-escura'}
# (obra, livro): [(arquivo, primeiro capítulo, último capítulo)]; None = livro inteiro num arquivo
ARQUIVOS = {
    ('subida', 0): [('0-argumento-e-prologo.txt', None, None)],
    ('subida', 1): [('1-livro-primeiro.txt', None, None)],
    ('subida', 2): [('2-livro-segundo-a.txt', 1, 12), ('2-livro-segundo-b.txt', 13, 21), ('2-livro-segundo-c.txt', 22, 32)],
    ('subida', 3): [('3-livro-terceiro-a.txt', 1, 23), ('3-livro-terceiro-b.txt', 24, 45)],
    ('noche', 0): [('0-prologo-e-cancoes.txt', None, None)],
    ('noche', 1): [('1-livro-primeiro.txt', None, None)],
    ('noche', 2): [('2-livro-segundo-a.txt', 1, 12), ('2-livro-segundo-b.txt', 13, 25)],
}
TITULO_OBRA = {'subida': 'Subida del Monte Carmelo', 'noche': 'Noche oscura'}
TITULO_LIVRO = {0: None, 1: 'Libro primero', 2: 'Libro segundo', 3: 'Libro tercero'}
TITULO_0 = {'subida': 'Argumento, canciones y prólogo', 'noche': 'Prólogo y canciones'}
PAGS_IMPRESSAS = {   # páginas do volume de 1929 (para o cabeçalho)
    ('subida', 0): '3–11', ('subida', 1): '12–66', ('subida', 2): '66–238', ('subida', 3): '239–362',
    ('noche', 0): '363–368', ('noche', 1): '368–413', ('noche', 2): '413–512',
}


def cabecalho(obra, livro, faixa, arq):
    tit = TITULO_LIVRO[livro] or TITULO_0[obra]
    if faixa[0]:
        tit += f', capítulos {faixa[0]}–{faixa[1]}'
    return '\n'.join([
        f'# titulo: {tit}',
        f'# obra: San Juan de la Cruz, {TITULO_OBRA[obra]}',
        '# fonte: Internet Archive, «Obras de San Juan de la Cruz, t. II» (obrasdesanjuande02john; outra digitalização do '
        'mesmo exemplar em BMC11ObrasDeSanJuanDeLaCruzTomoIISubidaYNocheOscura), três leituras (OCR) do fac-símile '
        'votadas por original/montar.py' + (' na pasta subida-do-monte-carmelo' if obra == 'noche' else '')
        + ('; palavras ilegíveis limpas pela transcrição do Documenta Catholica Omnia (só para o OCR)' if obra == 'subida' and livro >= 2 else ''),
        '# edicao: Obras de San Juan de la Cruz, Doctor de la Iglesia, editadas y anotadas por el P. Silverio de Santa '
        'Teresa, C. D., t. II, Subida y Noche oscura (Burgos, Tipografía de «El Monte Carmelo», 1929; Biblioteca '
        f'Mística Carmelitana, 11), pp. {PAGS_IMPRESSAS[(obra, livro)]}',
        '# nota: «## n. título» abre cada capítulo, com o título de Silverio (tirado do índice do volume); '
        '«[I.1]» = livro e capítulo, no primeiro parágrafo numerado; «[n]» = número de parágrafo de Silverio; '
        'títulos internos e sumários em itálico; versos com «| »; fora as notas e variantes de Silverio, as chamadas '
        'de nota, os cabeços e os números de página; acentuação de hoje; ver LEIAME.md',
    ]) + '\n\n'


def dividir(texto, faixa):
    """Corta o texto do livro nos capítulos faixa[0]..faixa[1] (o que vem antes do 1º «##» vai com o 1º arquivo)."""
    if not faixa[0]:
        return texto
    pedacos = re.split(r'(?m)^(?=## \d+\. )', texto)
    out = []
    for p in pedacos:
        m = re.match(r'## (\d+)\. ', p)
        n = int(m.group(1)) if m else 0
        if (n == 0 and faixa[0] == 1) or faixa[0] <= n <= faixa[1]:
            out.append(p)
    return ''.join(out).rstrip() + '\n'


CAPITAIS = {'Angel': 'Ángel', 'Angeles': 'Ángeles', 'Angeles,': 'Ángeles,', 'Ultimo': 'Último', 'Unico': 'Único',
            'Africa': 'África', 'Asia': 'Asia', 'Ambrosio': 'Ambrosio', 'Exodo': 'Éxodo', 'Indice': 'Índice'}


# palavras que o OCR ou a grafia de 1929 dão sem acento e que, neste texto, são sempre a forma acentuada
SEMPRE = {'capitulo': 'capítulo', 'capitulos': 'capítulos', 'vacio': 'vacío', 'vacios': 'vacíos',
          'oido': 'oído', 'oidos': 'oídos', 'oir': 'oír', 'tenia': 'tenía', 'tenian': 'tenían', 'decia': 'decía',
          'hacia': 'hacia', 'mas': 'mas', 'guia': 'guía', 'guias': 'guías', 'sabia': 'sabia', 'fatigase': 'fatígase',
          'sigúese': 'síguese', 'cuan': 'cuan', 'airan': 'aíran', 'siguense': 'síguense', 'lamparas': 'lámparas',
          'oleo': 'óleo'}
# latim que a acentuação do espanhol estragaria (ómnibus, réquiem)
LATIM_PROTEGIDO = {'omnibus', 'requiem', 'Domine', 'omnia', 'anima', 'animae', 'vide', 'lucis', 'caeli', 'coeli',
                   'Deus', 'unus', 'luci', 'dare', 'omnes', 'gratia', 'mihi', 'tibi', 'sibi', 'nobis', 'vobis', 'filii', 'opera', 'vita', 'via'}


def normalizar(texto):
    """Acentuação de hoje que depende do contexto, aplicada ao texto pronto."""
    texto = re.sub(r'\b[A-Z][a-z]+\b', lambda m: CAPITAIS.get(m.group(0), m.group(0)), texto)
    # «El» pronome (Deus, Cristo) no meio da frase: Él
    texto = re.sub(r'(?<=[a-záéíóúñ,;] )El\b(?! [A-Z])', 'Él', texto)
    texto = re.sub(r'\b[a-z]+\b', lambda m: SEMPRE.get(m.group(0), m.group(0)), texto)
    texto = re.sub(r'\b([Hh])abernos (?=\w+(?:ado|ido|cho|sto|to|ito)\b)', r'\1abemos ', texto)
    texto = re.sub(r'(?<=[a-záéíóúñ,;:] \()El\b', 'Él', texto)
    # «sí» reflexivo depois de preposição
    texto = re.sub(r'\b(de|en|por|para|sobre|entre|contra|hacia|tras|sin|a|consigo) si\b'
                   r'(?=\s*[,;:\.\)]|\s+mism|\s+propi|\s+sól|\s+solo|\s+sola|\s+y\b|\s+o\b|\s+que\b)',
                   r'\1 sí', texto)
    return texto


# ---------------------------------------------------------------- segundo testemunho (só a Subida)
# dco-subida.txt: transcrição da Subida no Documenta Catholica Omnia (texto de Silverio, sem as notas). Serve só
# para limpar o OCR: troca uma palavra do texto votado apenas quando ela é suspeita (sinal estranho no meio, ou
# palavra que não existe na lista de frequência) e o testemunho, alinhado no mesmo capítulo, traz no mesmo lugar
# uma palavra parecida que existe. Nada mais se muda por ele.
LETRA = 'A-Za-zÁÉÍÓÚÜÑáéíóúüñ'
DCO_LIVROS = {1: 'LIBRO PRIMERO', 2: 'LIBRO SEGUNDO', 3: 'LIBRO TERCERO'}


def _norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(ch for ch in w if not unicodedata.combining(ch) or ch == '\u0303')
    return re.sub(r'[^a-zñ\u0303]', '', unicodedata.normalize('NFC', w))


def capitulos_dco(arq, livro):
    linhas = [l for l in open(arq, encoding='utf-8').read().split('\n')
              if 'file:///' not in l and 'S. Juan De La Cruz' not in l]
    # o corpo começa no segundo «LIBRO PRIMERO» (o primeiro é o índice)
    idx = [i for i, l in enumerate(linhas) if l.strip() == DCO_LIVROS[livro]]
    ini = idx[-1]
    fim = len(linhas)
    if livro + 1 in DCO_LIVROS:
        prox = [i for i, l in enumerate(linhas) if l.strip() == DCO_LIVROS[livro + 1] and i > ini]
        fim = prox[0] if prox else fim
    caps = collections.OrderedDict()
    atual = 0 if livro == 3 else None
    buf = []
    for l in linhas[ini + 1:fim]:
        m = re.match(r'^\s*CAP[ÍI]TULO (\d+)\.?', l)
        if m:
            if atual is not None:
                caps[atual] = ' '.join(buf)
            atual, buf = int(m.group(1)), [l[m.end():]]
            continue
        buf.append(l)
    caps[atual] = ' '.join(buf)
    if livro == 3 and 0 in caps:
        caps[1] = caps.pop(0)
    return caps


def limpar_com_testemunho(texto, livro, arq, vocab, log):
    caps = capitulos_dco(arq, livro)
    pedacos = re.split(r'(?m)^(?=## \d+\.)', texto)
    out = []
    for ped in pedacos:
        m = re.match(r'## (\d+)\.', ped)
        n = int(m.group(1)) if m else (1 if livro == 3 else None)
        w_txt = caps.get(n)
        if not w_txt:
            out.append(ped)
            continue
        cru = [x for x in w_txt.split() if re.search('[' + LETRA + ']', x)]
        wt = [re.sub(r'^[^' + LETRA + r']+|[^' + LETRA + r']+$', '', x) for x in cru]
        wn = [_norm(w) for w in wt]
        toks = [mm for mm in re.finditer(r'\S+', ped)]
        tn = [_norm(mm.group(0)) for mm in toks]
        sm = difflib.SequenceMatcher(None, tn, wn, autojunk=False)
        trocas = {}
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op != 'replace' or a2 - a1 > 8 or b2 - b1 > 8:
                continue
            if a2 - a1 != b2 - b1:
                # trecho embaralhado pelo OCR («a idad • Líos» por «caridad de Dios»): troca o trecho inteiro,
                # se a maior parte das palavras é suspeita e os dois trechos se parecem
                raws = [toks[i].group(0) for i in range(a1, a2)]
                if any(r.startswith(('[', '#', '|', '_')) or r.endswith('_') for r in raws):
                    continue
                cores = [re.sub(r'^[^' + LETRA + r']+|[^' + LETRA + r']+$', '', r) for r in raws]
                susp = [bool(re.search(r'[^' + LETRA + r'\-]', c)) or vocab.freq(c) < 2 for c in cores]
                if sum(susp) * 2 < len(susp) or not any(re.search(r'[^' + LETRA + r'\-]', c) for c in cores):
                    continue
                ca, cb = ''.join(tn[a1:a2]), ''.join(wn[b1:b2])
                if not ca or not 0.7 <= len(cb) / len(ca) <= 1.4 or difflib.SequenceMatcher(None, ca, cb).ratio() < 0.6:
                    continue
                if any(vocab.freq(w) < 2 for w in wt[b1:b2]) or any(re.search(r'[\(\)\[\]]', x) for x in cru[b1:b2]):
                    continue
                novo = acentuar(' '.join(cru[b1:b2]), vocab, collections.Counter())
                pre = re.match(r'^[«\(¡¿"]*', raws[0]).group(0)
                pos = re.search(r'[,\.;:!\?»\)]*$', raws[-1]).group(0)
                novo = pre + novo.lstrip('«(¡¿"') if pre else novo
                novo = novo.rstrip(',.;:!?»)') + pos if pos else novo
                trocas[a1] = novo
                for i in range(a1 + 1, a2):
                    trocas[i] = ''
                log.append((n, ' '.join(raws), novo))
                continue
            for i, j in zip(range(a1, a2), range(b1, b2)):
                raw = toks[i].group(0)
                if raw.startswith('[') or raw.startswith('#') or raw == '|':
                    continue
                mm = re.match(r'^([«\(¡¿"_]*)(.*?)([,\.;:!\?»\)_]*)$', raw)
                pre, core, pos = mm.groups()
                w = wt[j]
                suspeita = (re.search(r'[^' + LETRA + r'\-]', core) or vocab.freq(core) < 2)
                if not suspeita or vocab.freq(w) < 2 or not core:
                    continue
                if difflib.SequenceMatcher(None, tn[i], wn[j]).ratio() < 0.5:
                    continue
                if not re.search(r'[^' + LETRA + r'\-]', core):
                    # palavra só de letras, mas rara: pode ser forma do autor, nome ou latim de Silverio
                    # (Balaán, Apocalipsi, coelo); só se troca erro de uma ou duas letras por palavra comum
                    if (core[:1].isupper() or len(core) != len(w) or vocab.freq(w) < 20
                            or sum(x != y for x, y in zip(_norm(core), _norm(w))) > 1):
                        continue
                novo = w[0].upper() + w[1:] if core[:1].isupper() else w
                novo = acentuar(novo, vocab, collections.Counter())
                trocas[i] = pre + novo + pos
                log.append((n, raw, trocas[i]))
        if trocas:
            partes, ult = [], 0
            for i, mm in enumerate(toks):
                if i in trocas:
                    if trocas[i] == '':
                        ult = mm.end()
                        continue
                    partes.append(ped[ult:mm.start()])
                    partes.append(trocas[i])
                    ult = mm.end()
            partes.append(ped[ult:])
            ped = ''.join(partes)
        out.append(ped)
    return ''.join(out)



def tirar_sujeira(texto, vocab, log):
    """Sinais soltos que o OCR grudou numa palavra («mismo*», «Dios'», «^digo»): saem quando o que sobra é
    palavra comum."""
    def troca(m):
        w = m.group(0)
        if w.startswith('[') or w in ('|', '##'):
            return w
        jj = re.fullmatch('([' + LETRA + ']+)(,?)\\.([' + LETRA + ']+)([,\\.;:]?)', w)
        if jj and vocab.freq(jj.group(1)) >= 20 and vocab.freq(jj.group(3)) >= 20:
            a_, v_, b_, p_ = jj.groups()
            novo = (a_ + v_ + ' ' + b_ if b_[0].islower() else a_ + '. ' + b_) + p_
            log.append(('-', w, novo))
            return novo
        mm = re.match(r"^([«\(¡¿_]*)([\'\*\"~\^\\{}<>|`’]*)(.*?)([\'\*\"~\^\\{}<>|`’]*)([,\.;:!\?»\)_]*)$", w)
        if not mm or not (mm.group(2) or mm.group(4)):
            return w
        core = mm.group(3)
        if re.fullmatch('[' + LETRA + ']+', core) and vocab.freq(core) >= 20:
            novo = mm.group(1) + core + mm.group(5)
            log.append(('-', w, novo))
            return novo
        return w
    return '\n'.join(l if l.startswith('#') else re.sub(r'\S+', troca, l) for l in texto.split('\n'))


def aplicar_emendas(texto, obra, livro):
    """EMENDAS (emendas.py, ao lado): trocas exatas, cada uma tem de bater o número de vezes indicado."""
    arq = os.path.join(AQUI, 'emendas.py')
    if not os.path.exists(arq):
        return texto, []
    ns = {}
    exec(open(arq, encoding='utf-8').read(), ns)
    falhas = []
    for e in ns['EMENDAS'].get((obra, livro), []):
        velho, novo = e[0], e[1]
        vezes = e[2] if len(e) > 2 else 1
        n = texto.count(velho)
        if n != vezes:
            falhas.append(f'{velho!r}: {n} vez(es), esperado {vezes}')
            continue
        texto = texto.replace(velho, novo)
    return texto, falhas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fontes', required=True)
    ap.add_argument('--obra', choices=['subida', 'noche'], required=True)
    ap.add_argument('--livro', type=int, required=True)
    ap.add_argument('--duvidas')
    ap.add_argument('--gravar', action='store_true', help='grava os arquivos em original/ (ARQUIVOS)')
    ap.add_argument('--json', help='grava os blocos em JSON (para revisar e montar o arquivo)')
    a = ap.parse_args()
    fontes = os.path.expanduser(a.fontes)
    vocab = Vocab(os.path.join(fontes, 'es_full.txt'))
    A, B = carregar(fontes)
    ini, fim = PAGINAS[(a.obra, a.livro)]
    duvidas = []
    linhas = linhas_votadas(A, B, fontes, ini, fim, vocab, duvidas)
    blocos = montar_livro(linhas, a.livro, a.obra)
    log = collections.Counter()
    for b in blocos:
        if b[0] in ('par', 'sumario'):
            b[-1] = acentuar(limpar_chamadas(b[-1]), vocab, log)
        elif b[0] == 'verso':
            b[1] = [acentuar(limpar_chamadas(v), vocab, log) for v in b[1]]
        elif b[0] == 'sub':
            b[1] = limpar_chamadas(b[1])
    titulos = titulos_indice(A, B, fontes, vocab)
    texto = render(blocos, a.obra, a.livro, titulos, vocab)
    texto = normalizar(texto)
    trocas_t = []
    arq_t = os.path.join(fontes, 'dco-subida.txt')
    if a.obra == 'subida' and a.livro >= 2 and os.path.exists(arq_t):
        texto = limpar_com_testemunho(texto, a.livro, arq_t, vocab, trocas_t)
        print(f'{len(trocas_t)} palavras limpas pelo segundo testemunho', file=sys.stderr)
    texto, falhas = aplicar_emendas(texto, a.obra, a.livro)
    if a.livro >= 2 or a.obra == 'noche':
        texto = tirar_sujeira(texto, vocab, trocas_t)
    for f in falhas:
        print('emenda não aplicada:', f, file=sys.stderr)
    if a.gravar:
        pasta = os.path.join(EDICOES, PASTA[a.obra], 'original')
        os.makedirs(pasta, exist_ok=True)
        for arq, c1, c2 in ARQUIVOS[(a.obra, a.livro)]:
            with open(os.path.join(pasta, arq), 'w', encoding='utf-8') as f:
                f.write(cabecalho(a.obra, a.livro, (c1, c2), arq) + dividir(texto, (c1, c2)))
            print('gravado', os.path.join(PASTA[a.obra], 'original', arq), file=sys.stderr)
    elif not a.json:
        sys.stdout.write(texto)
    if a.json:
        json.dump({'blocos': blocos, 'acentos': [[k[0], k[1], v] for k, v in log.most_common()]},
                  open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    if a.duvidas:
        with open(a.duvidas, 'w', encoding='utf-8') as f:
            for d in duvidas:
                f.write('\t'.join(str(x) for x in d) + '\n')
        if trocas_t:
            with open(a.duvidas.replace('.tsv', '-testemunho.tsv'), 'w', encoding='utf-8') as f:
                for d in trocas_t:
                    f.write('\t'.join(str(x) for x in d) + '\n')
    print(f'{len(blocos)} blocos, {len(duvidas)} dúvidas, {sum(log.values())} acentos', file=sys.stderr)


if __name__ == '__main__':
    main()
