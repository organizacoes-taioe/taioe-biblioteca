"""Recordações do Escrivão Isaías Caminha — as mudanças de 1917 sobre a 1ª edição (1909), para a «Sobre».

  python3 ferramentas/texto.py isaias-caminha
  python3 edicoes/isaias-caminha/edicao1909.py          (texto de 1909: texto1909.pkl)
  python3 edicoes/isaias-caminha/mudancas.py            (grava edicoes/isaias-caminha/mudancas.json)
  python3 ferramentas/texto.py isaias-caminha --publicar

Compara palavra por palavra o texto de 1917 (antes da grafia de hoje) com o de 1909. Os dois saem de OCR,
e uma diferença entre eles pode ser erro de leitura de um dos lados: por isso só entra na lista a mudança
que as edições modernas confirmam dos dois lados, a do Wikisource (que segue 1909) com a leitura de 1909
e a da Ática (que segue 1917) com a de 1917. Os trechos acrescentados (ou cortados) de mais de 12
palavras vão resumidos, com o número de palavras. A pontuação fica de fora (o OCR não é seguro nela).
"""
import json
import os
import pickle
import re
import sys
from collections import Counter, OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao.fontes import cache  # noqa: E402
from edicao.grafia import chave  # noqa: E402
from edicao.tokens import _mapeador, achatar, alinhar, e_palavra, texto  # noqa: E402

import config  # noqa: E402
from pontos import mesma  # noqa: E402

LONGO = 12


def pal(ts):
    return [t for t in ts if e_palavra(t)]


CRASE = {'a', 'á', 'à', 'A', 'Á', 'À'}


def iguais(x, y):
    from edicao.grafia import esqueleto
    x = [t for t in x if t not in CRASE]          # «á» de 1909 e 1917 (crase ou preposição): o OCR as troca
    y = [t for t in y if t not in CRASE]
    if len(x) == len(y) and all(mesma(a, b) or mesma(b, a) for a, b in zip(x, y)):
        return True
    return bool(x) and bool(y) and esqueleto(''.join(x)) == esqueleto(''.join(y))


def mudancas():
    A = [t for t in pickle.load(open(cache(config.OBRA, 'texto1909.pkl'), 'rb')) if t not in ('_', '*')]
    r = pickle.load(open(cache(config.OBRA, 'resultado.pkl'), 'rb'))
    B = [t for t in r['E'] if t not in ('_', '*')]
    md = config.modernas()
    W = achatar([p for p in md['ws'] if p['n']])
    M = achatar(md['bv'])
    mw = _mapeador(alinhar(A, W, chave=chave))
    mm = _mapeador(alinhar(B, M, chave=chave))
    caps, cap = {}, None
    for i, t in enumerate(B):
        if t.startswith('#'):
            cap = t[1:] or 'Breve notícia'
        caps[i] = cap
    itens, longos = [], []
    ops = [o for o in alinhar(A, B, chave=chave) if o[0] != 'equal']
    for tp, i1, i2, j1, j2 in ops:
        if caps.get(j1) == 'Breve notícia' or any(t.startswith('#') for t in A[i1:i2] + B[j1:j2]):
            continue
        pa, pb = pal(A[i1:i2]), pal(B[j1:j2])
        if not pa and not pb:
            continue                                   # só pontuação
        if iguais(pa, pb):
            continue                                   # só grafia
        pw = pal(W[mw(i1, True):mw(i2, True)])
        pm = pal(M[mm(j1, True):mm(j2, True)])
        if max(len(pa), len(pb)) > LONGO:
            # trecho longo: basta que as modernas tragam quase o mesmo (o OCR erra uma palavra ou outra)
            from difflib import SequenceMatcher
            sim = lambda x, y: SequenceMatcher(None, [chave(t) for t in x], [chave(t) for t in y], autojunk=False).ratio() if x or y else 1.0
            if sim(pa, pw) < 0.8 or sim(pb, pm) < 0.8:
                continue
        elif not (iguais(pa, pw) and iguais(pb, pm)) or iguais(pw, pm):
            continue                                   # sem a confirmação das duas modernas
        if max(len(pa), len(pb)) > LONGO:
            maior, ed = (pb, '1917') if len(pb) >= len(pa) else (pa, '1909')
            resumo = (texto(maior[:8]) + ' […] ' + texto(maior[-6:])) if len(maior) > 16 else texto(maior)
            longos.append({'cap': caps.get(j1), 'de': texto(pa) if len(pa) <= LONGO else f'«{resumo}» ({len(pa)} palavras)',
                           'para': texto(pb) if len(pb) <= LONGO else f'«{resumo}» ({len(pb)} palavras)',
                           'n': len(pb) - len(pa)})
            continue
        # contexto: duas palavras de cada lado
        a0, n = i1, 0
        while a0 > 0 and n < 2 and A[a0 - 1] != '¶' and not A[a0 - 1].startswith('#'):
            a0 -= 1; n += e_palavra(A[a0])
        b0, n = j1, 0
        while b0 > 0 and n < 2 and B[b0 - 1] != '¶' and not B[b0 - 1].startswith('#'):
            b0 -= 1; n += e_palavra(B[b0])
        mostra = lambda ts: re.sub(r'\s*¶\s*', ' ¶ ', texto(ts)).strip()
        itens.append({'cap': caps.get(j1), 'de': mostra(A[a0:i2]), 'para': mostra(B[b0:j2]),
                      'chave': (tuple(chave(t) for t in pa), tuple(chave(t) for t in pb)), 'sa': texto(pa), 'sb': texto(pb)})
    # trocas repetidas (nomes: Michaelowsky → Gregorovitch): um item só, com o número de vezes
    rep = Counter(x['chave'] for x in itens)
    vistos, fim = set(), []
    for x in itens:
        k = x.pop('chave'); sa, sb = x.pop('sa'), x.pop('sb')
        if rep[k] > 2:
            if k in vistos:
                continue
            vistos.add(k)
            x = {'cap': x['cap'], 'de': sa or '—', 'para': (sb or '—') + f' ({rep[k]} vezes)'}
        fim.append(x)
    return fim, longos


def _norm(s):
    from edicao.grafia import chave as ch
    return ' ' + ' '.join(ch(w) for w in re.findall(r"[^\W_]+", s)) + ' '


def _lido(pdf, txt, faixa):
    """Texto corrido de uma leitura (camada do PDF ou Tesseract), normalizado para busca."""
    if txt:
        pags = open(cache(config.OBRA, txt), encoding='utf-8').read().split('\f')[faixa[0] - 1:faixa[1]]
        linhas = [l for p in pags for l in p.split('\n')]
    else:
        linhas = [l for p in config.linhas_tesseract(pdf, *faixa) for l in p]
    return _norm(config._juntar(linhas))


def robustas(itens):
    """Só as mudanças em que as duas leituras de cada edição trazem o trecho: a de 1909 nas duas de 1909
    (camada do PDF e Tesseract) e a de 1917 nas duas de 1917."""
    from edicao1909 import PAGS09, PDF09
    l09 = [_lido(PDF09, None, PAGS09), _lido(None, 'c09.txt', PAGS09)]
    l17 = [_lido(config.PDF17, None, config.PAGS17), _lido(None, 'c17.txt', config.PAGS17)]
    ok = []
    for x in itens:
        de, para = re.sub(r' \(\d+ vezes\)$', '', x['de']), re.sub(r' \(\d+ vezes\)$', '', x['para'])
        if de.count('«') != de.count('»') or para.count('«') != para.count('»'):
            continue                          # aspa solta: leitura duvidosa
        if ' vezes)' in x['para'] and not any(len(w) >= 4 or w == 'Eu' for w in re.findall(r'\w+', de + ' ' + para)):
            continue                          # troca repetida de palavra curta (do → de): o OCR a confunde
        if de in ('—', '') or para in ('—', ''):
            if ' vezes)' in x['para']:
                ok.append(x)                 # palavra tirada ou posta várias vezes (Eu, o): fica
            continue
        if all(_norm(de) in l for l in l09) and all(_norm(para) in l for l in l17):
            ok.append(x)
    return ok


if __name__ == '__main__':
    itens, longos = mudancas()
    n = len(itens)
    itens = robustas(itens)
    print(n, 'diferenças confirmadas pelas modernas;', len(itens), 'também nas duas leituras de cada edição')
    json.dump({'itens': itens, 'longos': longos}, open(os.path.join(AQUI, 'mudancas.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(len(itens), 'mudanças de palavras;', len(longos), 'trechos longos acrescentados ou cortados;',
          sum(x['n'] for x in longos), 'palavras a mais nos longos')
