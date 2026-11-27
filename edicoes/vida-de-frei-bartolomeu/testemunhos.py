"""Vida de D. Frei Bertolameu dos Mártires — leitura dos testemunhos (OCRs) em sequências de palavras.

Cada testemunho vira uma lista de palavras na ordem de leitura, sem cabeço, reclamo, assinatura e
notas (as notas à margem de 1619 e as de rodapé das edições de Lisboa vão à parte):

  bnp1619   Tesseract nosso do exemplar da BNP (res-33-a), por coluna (ocr.py); é o testemunho de
            referência: tem a ordem e a completude de 1619 e as coordenadas para a conferência nas imagens
  ia1619    Tesseract nosso do exemplar do Internet Archive (bub_gb_ejJfgR_PmtQC, Biblioteca Nacional de Roma)
  ga1619    OCR do Internet Archive do mesmo exemplar (djvu.xml)
  r1850v1, r1853v2, r1818v1   Tesseract nosso das edições de Lisboa, Tipografia Rolandiana (tomos I e II)
  gr1850v1, gr1853v2, gr1818v1   OCR do Internet Archive das mesmas

Palavra: dict(t=texto, p=página do PDF, c=coluna ('a', 'b' ou ''), x0, y0, x1, y1 (pixels da imagem do
OCR), nl=True se começa linha, par=True se começa parágrafo (recuo), m=marca (cabeçalho de capítulo…)).
"""
import csv
import html
import os
import re
import statistics

PASTA = os.environ.get('VIDA_PASTA', '/mnt/arquivos/claude-tmp/pedidos-2711b/vida-de-frei-bartolomeu')
IA = {'ga1619': 'bub_gb_ejJfgR_PmtQC', 'gr1850v1': 'vidadedfrbertol00luisgoog',
      'gr1853v2': 'vidadedfrbertol01luisgoog', 'gr1818v1': 'vidadedfrbertol00sousgoog'}

CABECO = re.compile(r'(?i)(liuro|livro|liv\.|vida|arcebi|primas|hefpan|hespan|espan|bert|mart|braga|tomo)')


# ------------------------------------------------------------------ leitura bruta

def _linhas_tsv(f):
    L = {}
    with open(f, encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            x, y, w, h = int(r['left']), int(r['top']), int(r['width']), int(r['height'])
            L.setdefault(k, []).append({'t': r['text'].strip(), 'x0': x, 'y0': y, 'x1': x + w, 'y1': y + h,
                                        'cf': float(r['conf'])})
    linhas = []
    for k, ws in L.items():
        linhas.append(ws)
    # linhas pela altura do meio; Tesseract às vezes quebra uma linha em dois blocos
    linhas.sort(key=lambda ws: statistics.median((w['y0'] + w['y1']) / 2 for w in ws))
    return _fundir(linhas)


def _fundir(linhas):
    """Junta pedaços da mesma linha (mesma altura) que o OCR separou em blocos."""
    out = []
    for ws in linhas:
        ym = statistics.median((w['y0'] + w['y1']) / 2 for w in ws)
        h = statistics.median(w['y1'] - w['y0'] for w in ws)
        if out:
            ws0 = out[-1]
            ym0 = statistics.median((w['y0'] + w['y1']) / 2 for w in ws0)
            if abs(ym - ym0) < 0.45 * h:
                out[-1] = sorted(ws0 + ws, key=lambda w: w['x0'])
                continue
        out.append(sorted(ws, key=lambda w: w['x0']))
    return out


def _linhas_xml(nome_ia):
    """{página (1…): [linhas de palavras]} do djvu.xml do Internet Archive."""
    x = open(os.path.join(PASTA, 'ia', nome_ia + '.xml'), encoding='utf-8').read()
    paginas = {}
    for n, obj in enumerate(x.split('<OBJECT')[1:], 1):
        linhas = []
        for l in re.findall(r'<LINE>(.*?)</LINE>', obj, re.S):
            ws = []
            for c, t in re.findall(r'coords="([\d,]+)"[^>]*>([^<]*)<', l):
                x0, y1, x1, y0 = map(int, c.split(',')[:4])
                t = html.unescape(t).strip()
                if t:
                    ws.append({'t': t, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'cf': 0})
            if ws:
                linhas.append(ws)
        linhas.sort(key=lambda ws: statistics.median((w['y0'] + w['y1']) / 2 for w in ws))
        paginas[n] = _fundir(linhas)
    return paginas


# ------------------------------------------------------------------ limpeza da página

def _e_palavra(t):
    return re.search(r'[A-Za-zÀ-ÿſ]', t) is not None


MODELOS_CABECO = ['liuro i da vida de d fr bert dos mart', 'arcebispo de braga primas das hespanhas',
                  'vida de d fr bertolameu', 'dos martyres liv i', 'livro primeiro da vida de']


def _trigramas(s):
    s = re.sub(r'[^a-z]+', ' ', s.lower())
    return {s[i:i + 3] for i in range(len(s) - 2)}


def cara_de_cabeco(txt):
    t = _trigramas(txt)
    if not t:
        return True
    return max(len(t & _trigramas(m)) / len(t | _trigramas(m)) for m in MODELOS_CABECO) > 0.18


def _sem_cabeco(linhas, alto):
    """Tira o cabeço (título corrido e número da página): a 1ª linha, se está no alto e tem cara de cabeço
    (parecida com os títulos corridos, ou só números)."""
    while linhas:
        txt = ' '.join(w['t'] for w in linhas[0])
        y = min(w['y0'] for w in linhas[0])
        if y < alto and (cara_de_cabeco(txt) or re.fullmatch(r'[\d\s.,]+', txt) or len(txt) < 4):
            linhas = linhas[1:]
            continue
        break
    return linhas


def _espaco(linhas):
    ys = [statistics.median(w['y0'] for w in l) for l in linhas]
    d = [b - a for a, b in zip(ys, ys[1:]) if b > a]
    return statistics.median(d) if d else 80


def limpar_r(linhas, altura):
    """Edições de Lisboa (1 coluna): (corpo, notas de rodapé). Rodapé: linhas abaixo de um vão grande no
    fim, ou que começam por «(1)»; assinatura do caderno («TOMO I. F»): linha curta no fim."""
    linhas = _sem_cabeco(linhas, altura * 0.12)
    if not linhas:
        return [], []
    esp = _espaco(linhas)
    ys = [min(w['y0'] for w in l) for l in linhas]
    notas = []
    # assinatura / reclamo: última linha curta e recuada
    while linhas:
        ult = linhas[-1]
        txt = ' '.join(w['t'] for w in ult)
        if len(ult) <= 3 and (re.search(r'(?i)tom', txt) or len(txt) <= 12) and ys[len(linhas) - 1] > altura * 0.8 \
                and not re.match(r'\(\s*\d', txt):
            linhas = linhas[:-1]
            continue
        break
    # rodapé: a partir do primeiro vão > 1,5 espaço, na metade de baixo, seguido de linha com «(n)»
    corte = len(linhas)
    for i in range(1, len(linhas)):
        y0, y1 = min(w['y0'] for w in linhas[i - 1]), min(w['y0'] for w in linhas[i])
        txt = ' '.join(w['t'] for w in linhas[i])
        if y1 - y0 > 1.45 * esp and y1 > altura * 0.5 and re.match(r'\s*[(\[{]?\s*[\dlIi]\s*[)\]}]', txt):
            corte = i
            break
    notas = linhas[corte:]
    return linhas[:corte], notas


def limpar_1619(linhas, largura, altura, coluna):
    """Uma coluna de 1619: (corpo, notas à margem). Tira cabeço, reclamo e assinatura; as palavras fora da
    mancha do texto (à esquerda na coluna a, à direita na b) são as notas à margem."""
    linhas = _sem_cabeco(linhas, altura * 0.07)
    if len(linhas) > 3:
        esp = _espaco(linhas)
        y0, y1 = min(w['y0'] for w in linhas[0]), min(w['y0'] for w in linhas[1])
        if y0 < altura * 0.03 or (y0 < altura * 0.07 and y1 - y0 > 1.2 * esp):
            linhas = linhas[1:]
    if not linhas:
        return [], []
    # reclamo / assinatura: última linha com até 2 palavras e começando depois do meio da coluna
    while linhas and len(linhas[-1]) <= 2 and max(w['x0'] for w in linhas[-1]) > largura * 0.5:
        linhas = linhas[:-1]
    if not linhas:
        return [], []
    esq = [l[0]['x0'] for l in linhas if len(l) >= 3]
    dir_ = [max(w['x1'] for w in l if _e_palavra(w['t']) or True) for l in linhas if len(l) >= 3]
    margem = []
    corpo = []
    for i, l in enumerate(linhas):
        viz = [k for k in range(max(0, i - 6), min(len(linhas), i + 7)) if len(linhas[k]) >= 3]
        if coluna == 'a':
            le = sorted(linhas[k][0]['x0'] for k in viz)
            limite = le[len(le) // 2] if le else 0
            fora = [w for w in l if w['x1'] < limite - 12]
        else:
            ri = sorted(max(w['x1'] for w in linhas[k] if _e_palavra(w['t'])) if any(_e_palavra(w['t']) for w in linhas[k]) else 0 for k in viz)
            limite = ri[len(ri) // 2] if ri else largura
            fora = [w for w in l if w['x0'] > limite + 12]
        dentro = [w for w in l if w not in fora]
        if fora:
            margem.append(fora)
        if dentro:
            corpo.append(dentro)
    return corpo, margem


# ------------------------------------------------------------------ sequências

def _paragrafos(corpo):
    """Marca o começo de parágrafo pelo recuo da 1ª palavra em relação às linhas vizinhas."""
    for i, l in enumerate(corpo):
        viz = [corpo[k][0]['x0'] for k in range(max(0, i - 5), min(len(corpo), i + 6)) if k != i and len(corpo[k]) >= 3]
        base = sorted(viz)[len(viz) // 2] if viz else l[0]['x0']
        alt = statistics.median(w['y1'] - w['y0'] for w in l)
        l[0]['rec'] = (l[0]['x0'] - base) / max(alt, 1)


def palavras_pagina(nome, n):
    """(corpo, notas) de uma página de um testemunho, como listas de palavras."""
    import json
    if nome in IA:
        if nome not in _CACHE_XML:
            _CACHE_XML[nome] = _linhas_xml(IA[nome])
        linhas = _CACHE_XML[nome].get(n, [])
        xs = [w['x1'] for l in linhas for w in l] or [1]
        ys = [w['y1'] for l in linhas for w in l] or [1]
        largura, altura = max(xs), max(ys)
        if nome.endswith('1619'):
            corpo, notas = _limpar_ia1619(linhas, largura, altura)
        else:
            corpo, notas = limpar_r(linhas, altura)
        cols = [('', corpo, notas)]
    else:
        pasta = os.path.join(PASTA, 'tess-' + nome)
        info = json.load(open(os.path.join(pasta, f'{n}.json')))
        cols = []
        if nome.endswith('1619') and len(info['caixas']) == 2:
            for k, suf in enumerate('ab'):
                f = os.path.join(pasta, f'{n}{suf}.tsv')
                cx = info['caixas'][k]
                linhas = _linhas_tsv(f)
                corpo, notas = limpar_1619(linhas, cx[2] - cx[0], cx[3] - cx[1], suf)
                for l in corpo + notas:
                    for w in l:
                        w['x0'] += cx[0]
                        w['x1'] += cx[0]
                cols.append((suf, corpo, notas))
        else:
            linhas = _linhas_tsv(os.path.join(pasta, f'{n}.tsv'))
            corpo, notas = limpar_r(linhas, info['tamanho'][1])
            cols.append(('', corpo, notas))
    out, notas_out = [], []
    for suf, corpo, notas in cols:
        _paragrafos(corpo)
        for l in corpo:
            for j, w in enumerate(l):
                w.update(p=n, c=suf, nl=(j == 0))
                out.append(w)
        for l in notas:
            l = [w for w in l if re.search(r'[A-Za-z0-9]', w['t'])]
            for j, w in enumerate(l):
                w.update(p=n, c=suf, nl=(j == 0))
                notas_out.append(w)
    return out, notas_out


_CACHE_XML = {}


def _limpar_ia1619(linhas, largura, altura):
    """OCR do IA de 1619: as colunas vêm misturadas por linha; separa pelo meio da página e lê a esquerda
    e depois a direita. Notas à margem não se separam (é testemunho fraco: só vota)."""
    linhas = _sem_cabeco(linhas, altura * 0.08)
    meio = largura / 2
    a, b = [], []
    for l in linhas:
        la = [w for w in l if (w['x0'] + w['x1']) / 2 < meio]
        lb = [w for w in l if (w['x0'] + w['x1']) / 2 >= meio]
        if la:
            a.append(la)
        if lb:
            b.append(lb)
    return a + b, []


def paginas(nome):
    import json
    if nome in IA:
        if nome not in _CACHE_XML:
            _CACHE_XML[nome] = _linhas_xml(IA[nome])
        return sorted(_CACHE_XML[nome])
    pasta = os.path.join(PASTA, 'tess-' + nome)
    return sorted(int(f[:-5]) for f in os.listdir(pasta) if f.endswith('.json'))


def sequencia(nome, de=None, ate=None):
    """Todas as palavras do testemunho (corpo), com a hifenização do fim da linha desfeita: a palavra
    partida vira uma só, com as coordenadas da 1ª parte e 'parte2' com as da 2ª."""
    seq, notas = [], []
    for n in paginas(nome):
        if (de and n < de) or (ate and n > ate):
            continue
        c, nt = palavras_pagina(nome, n)
        seq += c
        notas += nt
    return dehifenar(seq), notas


HIFEN = re.compile(r'[-‐‑–—=¬]$')


def dehifenar(seq):
    out = []
    i = 0
    while i < len(seq):
        w = dict(seq[i])
        if i + 1 < len(seq) and seq[i + 1].get('nl') and HIFEN.search(w['t']) and len(w['t']) > 1 \
                and re.search(r'[A-Za-zÀ-ÿſ]', w['t'][-2]) and _e_palavra(seq[i + 1]['t']):
            prox = seq[i + 1]
            w['t'] = w['t'][:-1] + prox['t']
            w['parte2'] = {k: prox[k] for k in ('p', 'c', 'x0', 'y0', 'x1', 'y1')}
            i += 2
        else:
            i += 1
        out.append(w)
    return out
