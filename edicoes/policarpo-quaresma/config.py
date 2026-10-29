"""Triste Fim de Policarpo Quaresma — fontes.

Edição-base: a 1ª edição em livro (Rio de Janeiro, Typ. «Revista dos Tribunaes», 1915), a única em
vida do autor (o romance saíra antes em folhetim no Jornal do Commercio, ago.–out. de 1911). O
volume traz depois do romance sete contos, que ficam fora daqui. Três testemunhos dessa edição, de
três exemplares diferentes:
  pg  Projeto Gutenberg nº 67535 (2022), transcrição humana sobre as imagens da Biblioteca Nacional;
  pr  OCR do exemplar da Universidade de Princeton (camada de texto do DjVu do Wikimedia Commons,
      digitalização do Google pela HathiTrust);
  bt  OCR próprio (Tesseract) do exemplar da Brasiliana USP (BBM 4361): edicoes/policarpo-quaresma/tesseract.py.
Os dois OCRs são de programas e de exemplares diferentes: valem um voto cada. Recebem a divisão
(partes, capítulos, parágrafos) do Gutenberg (ocr.estrutura_como) e são limpos pelas guias
(ocr.limpar: só palavras inexistentes, trocadas pela parecida alinhada); as modernas vêm à frente do
Gutenberg nas guias, senão o OCR copiava os erros dele e o voto os confirmava («cra» -> «ora»).
Depois do voto, rever() aplica os pontos conferidos nas imagens (conferencia.json, pela assinatura
do ponto: contexto e leitura do Gutenberg) e, onde só a pontuação difere, fica a do Gutenberg
(os OCRs perdem vírgulas e pontos finos). Recortes para conferir: conferir.py (cópia do de Caetés).
Edições modernas (só para a grafia e o desempate; não são texto): a da Biblioteca Virtual do
Estudante Brasileiro (USP), OCR da edição da Ática (17ª ed.), e a do Wikisource, da mesma linhagem;
as duas no Formulário de 1943 (idéia, conseqüência) e com as horas por extenso («às quatro e
quinze», onde 1915 tem «ás 4 e 15»): o texto segue 1915.

Divisão: três partes, cada uma com cinco capítulos numerados (I a V) e com título, como em 1915.
No fluxo, cada capítulo é uma parte numerada «I.I» … «III.V»; agrupar() refaz as três partes na
publicação, com os capítulos marcados para o site («## Capítulo I — …» e «{§ I.1}»).
"""
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'policarpo-quaresma'

META = {
    'id': OBRA,
    'autor': 'lima-barreto',
    'titulo': 'Triste Fim de Policarpo Quaresma',
    'ano': 1915,
    'genero': 'Romance',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'marcas': False},
    'descricao': 'Romance publicado em folhetim em 1911 e em livro em 1915, a única edição em vida do autor.',
}

BASE = 'pg'
REFERENCIAS = [('ws', False), ('bv', False)]
DESEMPATE_LEXICO = True

ROM = ['I', 'II', 'III', 'IV', 'V']
PARTES = ['Primeira parte', 'Segunda parte', 'Terceira parte']
# títulos dos capítulos na grafia de hoje, como em 1915 (só a caixa muda: 1915 os compõe em maiúsculas)
TITULOS = {
    'I.I': 'A lição de violão', 'I.II': 'Reformas radicais', 'I.III': 'A notícia do Genelício',
    'I.IV': 'Desastrosas consequências de um requerimento', 'I.V': 'O bibelot',
    'II.I': 'No «Sossego»', 'II.II': 'Espinhos e flores', 'II.III': 'Golias',
    'II.IV': '«Peço energia, sigo já»', 'II.V': 'O trovador',
    'III.I': 'Patriotas', 'III.II': 'Você, Quaresma, é um visionário',
    'III.III': '...E tornaram logo silenciosos...', 'III.IV': 'O Boqueirão', 'III.V': 'A afilhada',
}
# rosto do livro: dedicatória e epígrafe (1915, p. [3] e [5]; conferidas no fac-símile)
DEDICATORIA = 'A\nJoão Luís Ferreira\nEngenheiro Civil'
EPIGRAFE = ("Le grand inconvénient de la vie réelle et ce qui la rend insupportable à l'homme supérieur, "
            "c'est que, si l'on y transporte les principes de l'idéal, les qualités deviennent des défauts, "
            "si bien que fort souvent l'homme accompli y réussit moins bien que celui qui a pour mobiles "
            "l'égoïsme ou la routine vulgaire.")
EPIGRAFE_AUTOR = '**Renan**, Marc-Aurèle'
# linha de pontos que separa a carta de Quaresma da narração (1915, p. 217; o Gutenberg a dá com asteriscos,
# e o fluxo descarta os asteriscos): volta na publicação, antes do parágrafo que ela abre
SEPARADORES = {'Como Quaresma dizia na carta': '. . . . . . . . . . .'}


def numerar(obra):
    """15 capítulos, na ordem: I.I … III.V."""
    caps = [p for p in obra if p['paras']]
    if len(caps) != 15:
        raise SystemExit(f'{len(caps)} capítulos (esperados 15): {[(p["n"], p["titulo"]) for p in caps]}')
    nomes = [f'{p}.{c}' for p in ('I', 'II', 'III') for c in ROM]
    return [dict(p, n=n, titulo=TITULOS[n]) for p, n in zip(caps, nomes)]


FIM_PARTE = re.compile(r'^(PRIMEIRA|SEGUNDA|TERCEIRA) PARTE$')


def gutenberg():
    obra = fontes.gutenberg(OBRA, 67535, [r'^(?P<n>[IVX]+)$'], inicio='PRIMEIRA PARTE')
    for p in obra:
        paras = []
        for x in p['paras']:
            if FIM_PARTE.match(x):
                continue
            if re.fullmatch(VERSO + r'[*\s]+', x):          # «* * *» do Gutenberg (ver decisoes.py)
                x = '* * *'
            paras.append(x)
        p['paras'] = paras
    return numerar(obra)


# ------------------------------------------------------------------ OCRs

LIXO = re.compile(r'^(Digitized by|Original from|.{0,12}R[I1]NCET[O0]N UNIVERS|.*PRINCETON)', re.I)
CABECO = re.compile(r'^[—–\-~_. ]*\d{1,3}[—–\-~_. ]*$|^[—–\-]+$|^[—–\-]\s*\S{1,4}\s*[—–\-]?$')
# cabeçalhos do livro (PRIMEIRA PARTE, números e títulos dos capítulos): linhas sem minúsculas
TITULO_OCR = re.compile(r'^[^a-zà-ÿ]*[A-ZÀ-Ú]{2}[^a-zà-ÿ]*$')


def _juntar(linhas):
    """Linhas de uma página ou do livro -> texto corrido, com as palavras partidas juntas."""
    s = ''
    for l in linhas:
        l = l.strip()
        if not l:
            continue
        if re.search(r'[A-Za-zÀ-ÿ][-¬]$', s):
            m = re.match(r"[\w']+", l)
            frag = (m.group(0) if m else '').lower()
            if frag in fontes.CLITICOS:
                s = s[:-1] + '-' + l
            else:
                s = s[:-1] + l
        else:
            s = (s + ' ' + l) if s else l
    return s


def _obra_ocr(linhas_por_pagina):
    linhas = []
    for pag in linhas_por_pagina:
        pag = [l.strip().replace('#', '') for l in pag if l.strip() and not LIXO.match(l.strip())]
        pag = [l for l in pag if not TITULO_OCR.match(l) and not re.fullmatch(r'[IVXl1]{1,4}\.?', l)]
        while pag and CABECO.match(pag[0]):            # número da página no alto
            pag = pag[1:]
        while pag and CABECO.match(pag[-1]):
            pag = pag[:-1]
        linhas += pag
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto)
    texto = texto.replace('’', "'").replace('E\'', 'É')
    return [{'n': 'I.I', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


def princeton():
    s = open(fontes.cache(OBRA, 'commons.txt'), encoding='utf-8').read().split('\f')
    return _obra_ocr([p.split('\n') for p in s[11:243]])        # páginas 12–243 do DjVu


def tesseract():
    pasta = fontes.cache(OBRA, 'tess-bbm4361')
    paginas = []
    for f in sorted(glob.glob(os.path.join(pasta, '*.tsv')), key=lambda f: int(os.path.basename(f)[:-4])):
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            linhas.setdefault(k, []).append((int(r['top']), int(r['left']), r['text'].strip()))
        ls = sorted(linhas.values(), key=lambda ws: sorted(w[0] for w in ws)[len(ws) // 2])
        paginas.append([' '.join(w[2] for w in sorted(ws, key=lambda w: w[1])) for ws in ls])
    return _obra_ocr(paginas)


def transcricoes():
    pg = gutenberg()
    md = modernas()
    # as modernas primeiro: com o Gutenberg à frente, o OCR copiava os erros dele («cra» -> «ora»);
    # o Gutenberg entra no léxico, para que as grafias de 1915 fiquem como estão
    guias = [md['ws'], md['bv'], pg]
    out = {'pg': pg}
    for nome, f in (('pr', princeton), ('bt', tesseract)):
        o, n = ocr.limpar(f(), guias)
        print(f'OCR {nome}: palavras corrigidas pelas guias:', n)
        o = ocr.estrutura_como(o, pg)
        for p, b in zip(o, pg):                     # títulos: os do Gutenberg (decisoes.TITULOS os fixa)
            p['titulo'] = b['titulo']
        out[nome] = o
    return out


# ------------------------------------------------------------------ edições modernas

_MODERNAS = {}


def wikisource_moderno():
    d = json.load(open(fontes.cache(OBRA, 'ws_moderno.json'), encoding='utf-8'))
    pags = {p['title'].split('/', 1)[1]: p['revisions'][0]['slots']['main']['*'] for p in d['query']['pages'].values()}
    obra = []
    for parte in ('I', 'II', 'III'):
        for c in ROM:
            t = pags[f'{parte}/{c}']
            t = re.sub(r'^\{\{navegar.*?\n\}\}\}?\}?\n', '', t, flags=re.S)
            t = re.sub(r'\[\[Categoria:[^\]]*\]\]', '', t)
            t = re.sub(r'<poem>(.*?)</poem>', lambda m: '\n\n' + VERSO + m.group(1).strip() + '\n\n', t, flags=re.S)
            t = re.sub(r"'''?", '', t).replace("''", '')
            t = re.sub(r'<[^>]+>', '', t)
            paras = []
            for b in re.split(r'\n\s*\n', t):
                b = b.strip()
                if not b:
                    continue
                if b.startswith(VERSO):
                    paras.append(VERSO + '\n'.join(l.strip().lstrip(':').strip() for l in b[1:].split('\n') if l.strip()))
                else:
                    paras.append(fontes.limpar(b.replace('\n', ' ')))
            obra.append({'n': f'{parte}.{c}', 'titulo': TITULOS[f'{parte}.{c}'], 'paras': paras})
    return fontes.normalizar(obra)


def bveb():
    s = fontes.pdf_texto(OBRA, 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/'
                         'lima-barreto/policarpo-quaresma.pdf', 'bveb')
    s = s[s.index('I A LIÇÃO DE VIOLÃO'):]
    s = re.sub(r'(?m)^Virtual Bookstore.*$', '', s)
    s = re.sub(r'(?m)^(PRIMEIRA|SEGUNDA|TERCEIRA) PARTE$', '', s)
    s = re.sub(r'(\w)- (\w)', r'\1\2', s)                       # «subsecretá- rio»
    obra = fontes.texto_por_linhas(s, [r'^(?P<n>I{1,3}|IV|V) (?P<t>[A-ZÀ-Ú."«“ ][^a-z]+)$'])
    obra = [p for p in obra if p['paras']]
    for p, n in zip(obra, [f'{a}.{c}' for a in ('I', 'II', 'III') for c in ROM]):
        p['n'], p['titulo'] = n, TITULOS[n]
        while p['paras'] and re.fullmatch(r'[^a-z]+', p['paras'][0]):    # resto do título em outra linha
            p['paras'].pop(0)
    return fontes.normalizar(obra)


def modernas():
    if not _MODERNAS:
        _MODERNAS.update({'ws': wikisource_moderno(), 'bv': bveb()})
    return _MODERNAS


# ------------------------------------------------------------------ publicação

def agrupar(partes):
    """15 capítulos -> 3 partes, cada uma com «## Capítulo N — título» + «{§ P.c}» no 1º parágrafo
    (o gerador do site faz de cada capítulo uma página; META['divisao']['marcas'] = False esconde a
    marca). A dedicatória e a epígrafe abrem a primeira parte."""
    out = []
    for k, nome in enumerate(PARTES):
        pr = ROM[k]
        paras = []
        if k == 0:
            paras += [{'verso': DEDICATORIA.split('\n')}, EPIGRAFE, EPIGRAFE_AUTOR]
        for c, rc in enumerate(ROM, 1):
            cap = next(p for p in partes if p['n'] == f'{pr}.{rc}')
            paras.append(f'## Capítulo {rc} — {cap["titulo"]}')
            corpo = list(cap['paragrafos'])
            if isinstance(corpo[0], dict):
                raise SystemExit(f'capítulo {cap["n"]} abre com versos')
            corpo[0] = f'{{§ {pr}.{c}}} ' + corpo[0]
            for x in corpo:
                if isinstance(x, str) and any(x.startswith(k) for k in SEPARADORES):
                    paras.append(next(v for k, v in SEPARADORES.items() if x.startswith(k)))
                paras.append(x)
        out.append({'n': pr, 'titulo': nome, 'paragrafos': paras})
    return out


def rotulos(partes):
    """Lugar de cada correção na página «Sobre»: «I, cap. III»."""
    return [p['n'].replace('.', ', cap. ', 1) for p in partes]


# ------------------------------------------------------------------ revisão das escolhas

def assinatura(x):
    """Chave estável de um ponto de divergência: o contexto no Gutenberg e a leitura dele."""
    return f"{x['antes'][-30:]}|{x['leituras'].get('pg')}|{x['depois'][:20]}"


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
    """Depois do voto: (1) onde só a pontuação difere, vale a do Gutenberg (os dois OCRs perdem
    vírgulas e pontos finos; conferido nas imagens, ver conferencia.json); (2) os pontos conferidos
    no fac-símile (conferencia.json: assinatura -> 'pg', 'pr', 'bt' ou o texto) valem sobre tudo."""
    from edicao.tokens import achatar, e_palavra, texto as junta
    from edicao.grafia import chave
    conf = {}
    arq = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conferencia.json')
    if os.path.exists(arq):
        conf = json.load(open(arq, encoding='utf-8'))
    B = achatar(tr[BASE])
    pal = lambda ts: [chave(t) for t in ts if e_palavra(t)]
    usados = set()
    for x in sitios:
        L = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
        a = assinatura(x)
        if a in conf:
            v = conf[a]
            x['escolha'] = L[v] if v in L else _toks(v)
            x['por'] = 'conferido no fac-símile'
            usados.add(a)
        elif len({tuple(pal(v)) for v in L.values()}) == 1 and x['escolha'] != L[BASE]:
            x['escolha'], x['por'] = L[BASE], 'pontuação do pg'
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
