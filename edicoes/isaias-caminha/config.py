"""Recordações do Escrivão Isaías Caminha — fontes.

Edições em vida do autor (morto em 1922): 1ª, Lisboa, A. M. Teixeira, 1909; 2ª, Rio de Janeiro, A. de
Azevedo & Costa, 1917, «revista e augmentada», com a «Breve notícia» (que restabelece o prefácio de
Isaías, cortado em 1909) e uma errata. A 2ª é a última revista pelo autor e está em fac-símile na
Brasiliana USP (BBM 4808): é a edição-base. A Brasiliana tem também a 1ª (BBM 4799), que serve para a
lista das mudanças (mudancas.py).

Testemunhos de 1917 (um exemplar só, duas leituras de programas diferentes):
  t17  OCR próprio (Tesseract, tesseract.py) do BBM 4808. Base do confronto.
  c17  o OCR que vem no PDF do BBM 4808.
Os dois recebem a divisão (partes e parágrafos) da edição moderna de 1917 (bv, abaixo) (ocr.estrutura_como) e são
limpos pelas guias (ocr.limpar: só palavras inexistentes, trocadas pela parecida alinhada). Sem maioria
(dois votos), vale a leitura apoiada pelas edições modernas; sem apoio, a com menos palavras
inexistentes (DESEMPATE_LEXICO), e o ponto vai para a conferência nas imagens (conferencia.json, pela
assinatura do ponto; ver rever()).
Edições modernas (só para a grafia e o desempate; não são texto), as duas no Formulário de 1943:
  bv  a da Biblioteca Virtual do Estudante Brasileiro (USP), da edição da Ática (1995): o texto de 1917
      (traz os trechos acrescentados em 1917), sem a «Breve notícia»; a dela vem do Wikisource.
  ws  a do Wikisource (importada em 2007, de origem não declarada): a «Breve notícia» de 1917, mas o
      romance pelo texto de 1909 (faltam-lhe os acréscimos de 1917: o charadista e o cronista esportivo
      no cap. VIII etc.). Vale como 2ª referência de grafia e para achar as mudanças (mudancas.py).
As duas leem «a compreensão» no começo, onde 1909 e 1917 têm «a compressão».

Divisão: a «Breve notícia» de Lima Barreto (com o prefácio de Isaías dentro) e os capítulos I a XIV,
sem título, como em 1917.
"""
import csv
import glob
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'isaias-caminha'

META = {
    'id': OBRA,
    'autor': 'lima-barreto',
    'titulo': 'Recordações do Escrivão Isaías Caminha',
    'ano': 1909,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1909 e revisto pelo autor na 2ª edição, de 1917.',
}

BASE = 't17'
REFERENCIAS = [('bv', False), ('ws', False)]
DESEMPATE_LEXICO = True

ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV']
PDF17 = 'bbm4808-1917'
PAGS17 = (11, 238)          # da «Breve notícia» ao fim do romance (a p. 239 é a errata)

# dedicatória (1917, p. [7] do PDF 9; conferida no fac-símile)
DEDICATORIA = ['A Benedito de Souza', 'meu compadre e meu amigo']


# ------------------------------------------------------------------ edições modernas

def wikisource_moderno():
    d = json.load(open(fontes.cache(OBRA, 'ws_moderno.json'), encoding='utf-8'))
    pags = {p['title'].split('/', 1)[1]: p['revisions'][0]['slots']['main']['*'] for p in d['query']['pages'].values()}
    obra = []
    for n in ['Breve notícia'] + ROM:
        t = pags[n]
        t = re.sub(r'^\{\{navegar.*?\n\}\}\n', '', t, flags=re.S)
        t = re.sub(r'\[\[Categoria:[^\]]*\]\]', '', t)
        t = re.sub(r'\{\{d\|(.*?)\}\}', r'\1', t, flags=re.S)
        t = t.replace('&mdash;', '—')
        t = re.sub(r'\n*\{\{separador\}\}\n*', lambda m: ' *** ' if not m.group(0).startswith('\n\n') else '\n\n* * *\n\n', t)
        t = re.sub(r'<poem>(.*?)</poem>', lambda m: '\n\n' + VERSO + m.group(1).strip() + '\n\n', t, flags=re.S)
        t = re.sub(r"'''?", '', t)
        t = re.sub(r'<[^>]+>', '', t)
        paras = []
        for b in re.split(r'\n\s*\n', t):
            b = b.strip()
            if not b:
                continue
            if b.startswith(VERSO):
                paras.append(VERSO + '\n'.join(l.strip() for l in b[1:].split('\n') if l.strip()))
            else:
                paras.append(fontes.limpar(b.replace('\n', ' ')))
        obra.append({'n': '' if n == 'Breve notícia' else n, 'titulo': n if n == 'Breve notícia' else '', 'paras': paras})
    return fontes.normalizar(obra)


def bveb():
    s = open(fontes.cache(OBRA, 'bveb.txt'), encoding='utf-8').read()
    s = s[s.index('Lima Barreto\n\n'):]
    obra, parte, par = [], None, ''
    for pag in s.split('\f'):
        for l in pag.split('\n'):
            if not l.strip():
                continue
            m = re.fullmatch(r'\s{20,}([IVX]+)\s*', l)
            if m:
                if parte is not None and par:
                    parte['paras'].append(par)
                par = ''
                parte = {'n': m.group(1), 'titulo': '', 'paras': []}
                obra.append(parte)
                continue
            if parte is None:
                continue
            ind = len(l) - len(l.lstrip())
            l = l.strip()
            if ind >= 6 and par and not re.match(r'^[a-zà-ÿ]', l) or not par:
                if par:
                    parte['paras'].append(par)
                par = l
            elif par.endswith('-') and re.match(r'^[a-zà-ÿ]', l) and not par.endswith(' -'):
                par = par[:-1] + l if not re.search(r'-(me|te|se|lhe|lhes|o|a|os|as|nos|vos|lo|la)$', par) else par + l
            else:
                par += ' ' + l
    if par:
        parte['paras'].append(par)
    for p in obra:
        p['paras'] = [fontes.limpar(x.replace('“', '"').replace('”', '"')) for x in p['paras']]
    return fontes.normalizar(obra)


_MODERNAS = {}


def modernas():
    if not _MODERNAS:
        ws = wikisource_moderno()
        _MODERNAS.update({'bv': [ws[0]] + bveb(), 'ws': ws})
    return _MODERNAS


# ------------------------------------------------------------------ OCRs de 1917

LIXO = re.compile(r'^(BRASILIANA|Digitized by)', re.I)
CABECO = re.compile(r'^[—–\-~_. ]*\d{1,3}[—–\-~_. ]*$|^[—–\-]+$|^[—–\-]\s*\S{1,4}\s*[—–\-]?$|^[IVXLl1]{1,5}\.?$')
# cabeços (RECORDAÇÕES DO ESCRIVÃO, ISAIAS CAMINHA, BREVE NOTICIA) e números dos capítulos: sem minúsculas
TITULO_OCR = re.compile(r'^[^a-zà-ÿ]*[A-ZÀ-Ú]{2}[^a-zà-ÿ]*$')
CABECO_TXT = re.compile(r'^\W*\d*\W*(RECORDA|ISA[IÍ]AS|CAMINHA|DO ESCRIV)', re.I)


def _juntar(linhas):
    s = ''
    for l in linhas:
        l = l.strip()
        if not l:
            continue
        if re.search(r'[A-Za-zÀ-ÿ][-¬]$', s):
            m = re.match(r"[\w']+", l)
            frag = (m.group(0) if m else '').lower()
            s = s[:-1] + ('-' + l if frag in fontes.CLITICOS else l)
        else:
            s = (s + ' ' + l) if s else l
    return s


def _obra_ocr(linhas_por_pagina):
    linhas = []
    for pag in linhas_por_pagina:
        pag = [l.strip().replace('#', '') for l in pag if l.strip() and not LIXO.match(l.strip())]
        pag = [l for l in pag if not TITULO_OCR.match(l)]
        while pag and (CABECO.match(pag[0]) or (CABECO_TXT.match(pag[0]) and len(pag[0]) < 40)):
            pag = pag[1:]
        while pag and CABECO.match(pag[-1]):
            pag = pag[:-1]
        linhas += pag
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto)
    texto = texto.replace('’', "'").replace('E\'', 'É')
    return [{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


def camada():
    s = open(fontes.cache(OBRA, 'c17.txt'), encoding='utf-8').read().split('\f')
    a, b = PAGS17
    return _obra_ocr([p.split('\n') for p in s[a - 1:b]])


def linhas_tesseract(pdf, a, b):
    pasta = fontes.cache(OBRA, 'tess-' + pdf)
    paginas = []
    for n in range(a, b + 1):
        f = os.path.join(pasta, f'{n}.tsv')
        if not os.path.exists(f):
            paginas.append([])
            continue
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            linhas.setdefault(k, []).append((int(r['top']), int(r['left']), r['text'].strip()))
        ls = sorted(linhas.values(), key=lambda ws: sorted(w[0] for w in ws)[len(ws) // 2])
        paginas.append([' '.join(w[2] for w in sorted(ws, key=lambda w: w[1])) for ws in ls])
    return paginas


def tesseract():
    return _obra_ocr(linhas_tesseract(PDF17, *PAGS17))


def transcricoes():
    md = modernas()
    guias = [md['bv'], md['ws']]
    out = {}
    for nome, f in (('t17', tesseract), ('c17', camada)):
        o, n = ocr.limpar(f(), guias)
        print(f'OCR {nome}: palavras corrigidas pelas guias:', n)
        o = ocr.estrutura_como(o, md['bv'])
        for p, b in zip(o, md['bv']):
            p['titulo'] = b['titulo']
        out[nome] = o
    return out


# ------------------------------------------------------------------ publicação

def arrumar(partes):
    """A dedicatória abre a «Breve notícia» (o site não tem página própria para ela)."""
    p0 = partes[0]
    if p0['titulo'] != 'Breve notícia':
        raise SystemExit(f'primeira parte inesperada: {p0["titulo"]!r}')
    p0['paragrafos'] = [{'verso': DEDICATORIA}] + list(p0['paragrafos'])
    return partes


# ------------------------------------------------------------------ revisão das escolhas

def assinatura(x):
    """Chave estável de um ponto de divergência: o contexto na base e a leitura dela."""
    return f"{x['antes'][-30:]}|{x['leituras'].get(BASE)}|{x['depois'][:20]}"


def _toks(s):
    from edicao.tokens import TOK
    out = []
    for parte in re.split(r'(¶|#\S*)', s or ''):
        if parte == '¶' or parte.startswith('#'):
            out.append(parte)
        else:
            out += TOK.findall(parte)
    return out


def rever(tr, md, sitios):
    """Depois do voto, os pontos conferidos no fac-símile (conferencia.json: assinatura -> 't17', 'c17'
    ou o texto) valem sobre tudo."""
    from edicao.tokens import achatar, texto as junta
    conf = {}
    arq = os.path.join(AQUI, 'conferencia.json')
    if os.path.exists(arq):
        conf = json.load(open(arq, encoding='utf-8'))
    B = achatar(tr[BASE])
    usados = set()
    for x in sitios:
        L = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
        a = assinatura(x)
        if a in conf:
            v = conf[a]
            x['escolha'] = L[v] if v in L else _toks(v)
            x['por'] = 'conferido no fac-símile'
            x['duvida'] = False
            usados.add(a)
        x['escolha_txt'] = junta(x['escolha'])
    sobra = set(conf) - usados
    if sobra:
        print('conferência sem ponto correspondente:', len(sobra), list(sobra)[:5])
    E, pos = [], 0
    for x in sitios:
        E.extend(B[pos:x['s']])
        E.extend(x['escolha'])
        pos = x['e']
    E.extend(B[pos:])
    return [t for t in E if t != '*'], sitios
