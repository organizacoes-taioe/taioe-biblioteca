"""São Bernardo — fontes.

Edições em vida do autor: 1ª, Ariel, 1934; 2ª, José Olympio, 1938; 3ª, José Olympio, 1947 (_Obras_,
vol. 2). A 3ª é a última revista pelo autor que se pode ler em fac-símile (Brasiliana USP, bbm/8421):
é a edição-base. A 2ª impressa não está digitalizada; a Brasiliana tem as provas dela (bbm/8418: a
1ª edição em folhas soltas, com as correções à mão do autor), que servem para conferir dúvidas.
Não há edição moderna gratuita: a grafia de hoje sai de regras (grafia1990.py), e os desempates,
dos dois OCRs da edição-base e do texto de 1934.

Testemunhos de 1947 (os que votam o texto):
- 't47': OCR próprio (Tesseract, tesseract.py) do fac-símile de 1947. Base do confronto.
- 'b47': o OCR que vem no PDF da Brasiliana, do mesmo fac-símile.
Onde os dois concordam, é o texto de 1947. Onde divergem, rever() escolhe pelo texto de 1934 ('a34',
estabelecido antes, posto na grafia de hoje: 'm34') e pelo léxico; as escolhas sem apoio vão para a
conferência nas imagens (relatorios/duvidas.tsv).
Testemunhos de 1934 (estabelecem o 'a34'):
- 'ws34': a 1ª edição no Wikisource (páginas 9–133 revisadas ou validadas; 134–220 só com OCR).
- 't34' e 'b34': o Tesseract e o OCR da Brasiliana do exemplar 1 de 1934 (bbm/8398). Valem um voto
  só; empate com o Wikisource se resolve pelo apoio de 1947.
"""
import csv
import glob
import html
import json
import os
import pickle
import re
import sys
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
sys.path.insert(0, AQUI)
from edicao import estabelecer, fontes, ocr  # noqa: E402
from edicao.grafia import chave, igualar_caixa  # noqa: E402
from edicao.tokens import _mapeador, achatar, alinhar, e_palavra  # noqa: E402

import grafia1990  # noqa: E402
import tesseract  # noqa: E402

OBRA = 'sao-bernardo'

META = {
    'id': OBRA,
    'autor': 'graciliano-ramos',
    'titulo': 'São Bernardo',
    'ano': 1934,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1934, o segundo de Graciliano Ramos.',
}

BASE = 't47'
# Sem edição moderna. Faz as vezes dela, para desempatar, o texto de 1934 posto na grafia de hoje
# ('m34'): onde os três testemunhos divergem, vence a leitura de 1947 que coincide com ele. A grafia
# do texto final vem de modernizar() abaixo, não dele.
REFERENCIAS = [('m34', True)]
M34 = None
NUMEROS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV',
           'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII',
           'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI']

WS34 = ('Graciliano Ramos - S. Bernardo (1934).pdf', 9, 220)
PDF47, PDF34 = 'bbm8421', 'bbm8398'
PAGINAS = {PDF47: (7, 224), PDF34: (17, 230)}     # do capítulo I ao fim, nos PDFs
SITIOS34 = []               # divergências do estabelecimento de 1934 (para conferência)


# ------------------------------------------------------------------ Wikisource (1934)

def _modelos(t):
    t = re.sub(r'<noinclude>.*?</noinclude>', '', t, flags=re.S)
    t = t.replace('{{--}}', '—')
    t = re.sub(r'\{\{(?:nop|NOP)\}\}', '\n\n', t)
    t = re.sub(r'\{\{Modernização automática[^{}]*\}\}', '', t)
    for _ in range(4):
        t = re.sub(r'\{\{(?:sic|SIC)\|([^{}|]*)(?:\|[^{}]*)?\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:sc|Sc|Sc2|Uc|serifa|smaller|x-smaller|x-larger|larger|c)\|([^{}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:lsp|letter-spacing)\|[^{}|]*\|([^{}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:pt)\|[^{}|]*\|([^{}|]*)\}\}', r'\1', t)
    t = re.sub(r'\{\{(?:dhr|rule|page break|RetallaImatge|t2)[^{}]*\}\}', '', t)
    t = re.sub(r'\xad\s*', '', t)
    t = re.sub(r"'''?([^'\n]+?)'''?", r'_\1_', t)
    t = re.sub(r'\bE ?[’\'](?= )', 'É', t)                       # 1934 compõe o É e o À maiúsculos
    t = re.sub(r'\bA ?[’\'](?=\w| )', 'À', t)                    # como E’ e A’ (o OCR: «E '»)
    t = re.sub(r'<p>\s*</p>', '\n\n', t)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    return t


_CABECO_WS = re.compile(r'^(?:\d+|S ?\.? ?BERNARDO|GRACILIANO RAMOS)$', re.I)


def ws34():
    """A 1ª edição no Wikisource, partida nos 36 capítulos pelos títulos ({{t2|IV}} ou «XXVI»)."""
    arquivo, primeira, ultima = WS34
    pags = fontes.wikisource_paginas(f'{OBRA}/ws34', arquivo, 1, ultima + 3)
    obra, atual, corpo = [], None, ''

    def fecha():
        nonlocal corpo
        if atual is not None:
            t = re.sub(r'(\w)-\n(\w)', r'\1\2', corpo)
            for b in re.split(r'\n\s*\n', t):
                b = fontes.limpar(b.replace('\n', ' '))
                if b and not re.fullmatch(r'[\d\W]*', b):
                    atual['paras'].append(b)
        corpo = ''

    for n in range(primeira, ultima + 1):
        v = pags.get(n)
        if not v or not v['qualidade']:
            continue
        cru = v['texto']
        corpo_pag = cru.split('</noinclude>', 1)[-1]
        m = re.match(r'\s*(?:<br\s*/?>\s*)*\{\{t2\|([IVXL]+)[^{}]*\}\}', corpo_pag) or \
            re.match(r'\s*([IVXL]+)\s*<br', corpo_pag)
        t = _modelos(cru)
        linhas = t.strip('\n').split('\n')
        while linhas and (not linhas[0].strip() or _CABECO_WS.match(linhas[0].strip())):   # cabeço das não revisadas
            linhas.pop(0)
        if m:
            fecha()
            atual = {'n': m.group(1), 'titulo': '', 'paras': []}
            obra.append(atual)
            if linhas and linhas[0].strip() == m.group(1):
                linhas.pop(0)
            corpo = '\n'.join(linhas)
            continue
        if atual is None:
            continue
        t = '\n'.join(linhas)
        if re.search(r'\w-$', corpo.rstrip()):
            corpo = corpo.rstrip()[:-1] + t.lstrip()
        elif t.startswith('\n') or cru.split('</noinclude>', 1)[-1].startswith(('\n\n', '<p>')):
            corpo += '\n\n' + t
        else:
            corpo += '\n' + t
    fecha()
    if [p['n'] for p in obra] != NUMEROS:
        raise SystemExit(f'ws34: capítulos {[p["n"] for p in obra]}')
    return fontes.normalizar(obra)


def ws34_revisadas():
    """Páginas do Wikisource revisadas ou validadas (qualidade 3 ou 4)."""
    pags = fontes.wikisource_paginas(f'{OBRA}/ws34', WS34[0], 1, WS34[2] + 3)
    return {n for n, v in pags.items() if (v['qualidade'] or 0) >= 3}


# ------------------------------------------------------------------ linhas dos OCRs

def _linhas_tess(nome):
    """Linhas do Tesseract, por página: (pagina, x, y, texto, altura da página, palavras), em pontos."""
    pasta = fontes.cache(OBRA, 'tess-' + nome)
    alturas = _alturas(nome)
    out = []
    for f in sorted(glob.glob(os.path.join(pasta, '*.tsv')), key=lambda f: int(os.path.basename(f)[:-4])):
        n = int(os.path.basename(f)[:-4])
        corte = json.load(open(f[:-4] + '.json'))
        esc = 72 / corte['dpi']
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            linhas.setdefault(k, []).append(((int(r['left']) + corte['x']) * esc, int(r['top']) * esc,
                                             r['text'].strip(), float(r['conf'])))
        # pedaços da mesma linha física em blocos diferentes viram uma linha só. Junto à lombada a
        # página encurva e a linha sobe para a direita: compara-se a altura das palavras vizinhas
        # (a última de um pedaço e a primeira do outro), não a do começo da linha.
        juntas = [sorted(v) for v in linhas.values()]
        mudou = True
        while mudou:                     # junta pares vizinhos até não sobrar nenhum
            mudou = False
            for a in juntas:
                for b in juntas:
                    # b continua a à direita; ou os dois se entremeiam na mesma altura
                    vizinho = a[-1][0] < b[0][0] and abs(b[0][1] - a[-1][1]) < 9
                    texto_ = lambda g: sum(1 for w in g if re.fullmatch(r'[A-Za-zÀ-ÿ]{3,}[,.;:!?]?', w[2])) >= 2
                    mesmo = abs(sorted(w[1] for w in a)[len(a) // 2] - sorted(w[1] for w in b)[len(b) // 2]) < 6 \
                        and texto_(a) and texto_(b)
                    if a is not b and (vizinho or mesmo):
                        a.extend(b)
                        a.sort()
                        juntas.remove(b)
                        mudou = True
                        break
                if mudou:
                    break
        for ws in sorted(juntas, key=lambda j: j[0][1]):
            out.append((n, ws[0][0], ws[0][1], ' '.join(w[2] for w in ws), alturas[n], [(w[0], w[2]) for w in ws]))
    return out


def _alturas(nome):
    return {k: float(a) for k, a in enumerate(re.findall(r'<page [^>]*height="([\d.]+)"', tesseract.bbox(nome)), 1)}


def _linhas_bbm(nome):
    """Linhas do OCR da Brasiliana (pdftotext -bbox-layout), com os pedaços da mesma linha juntos."""
    out = []
    s = tesseract.bbox(nome)
    for k, (alt, pag) in enumerate(re.findall(r'<page [^>]*height="([\d.]+)"[^>]*>(.*?)</page>', s, re.S), 1):
        pedacos = []
        for l in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>(.*?)</line>', pag, re.S):
            ws = [(float(x), html.unescape(w)) for x, w in re.findall(r'<word xMin="([\d.]+)"[^>]*>([^<]*)</word>', l.group(3))]
            if ws:
                pedacos.append((float(l.group(2)), ws))
        juntas = []
        for y, ws in sorted(pedacos, key=lambda p: p[0]):
            if juntas and abs(y - juntas[-1][0]) < 4:
                juntas[-1] = (juntas[-1][0], sorted(juntas[-1][1] + ws))
            else:
                juntas.append((y, ws))
        for y, ws in juntas:
            out.append((k, ws[0][0], y, ' '.join(w for _, w in ws), float(alt), ws))
    return out


_BOA = re.compile(r'^[A-Za-zÀ-ÿ]{2,}[,.;:!?]?$')
_PALAVRA = re.compile(r'[—–(«“"-]*[A-Za-zÀ-ÿ]{2,}(?:[-’\'][A-Za-zÀ-ÿ]+)*[-,.;:!?…»”")]*|[—–-]?[ÉÓÀAEOÁ][.!?,]?')
_CABECO = re.compile(r'^(?:\d+\s*)?(?:[ÒO0]BRAS\s+DE\s+)?G[RE]AC[IÍl1]L[IÍl1]ANO\s+[RE]AMOS(?:\s*\d+)?$|'
                     r'^(?:\d+\s*)?[S5s]\s*\.?\s*B[EÉ]RNA[RE]?[DO]O?(?:\s*\d+)?$|^\[?\s*\d+\s*\]?$', re.I)


def _e_cabeco(t):
    """Cabeço de página: «6 OBRAS DE GRACILIANO RAMOS», «S. BERNARDO 7», «GRACILIANO RAMOS», o número."""
    t = t.strip()
    u = re.sub(r'[^A-Z0-9]', '', t.upper())
    if _CABECO.match(t) or re.fullmatch(r'\d{1,3}', u):
        return True
    return len(t) < 45 and (('OBRAS' in u or 'RAMOS' in u or 'GRAC' in u) or
                            re.search(r'B[EÉ]R[NJ]', u) and len(u) < 16) and sum(ch.islower() for ch in t) <= 2


def _romano(s):
    s = re.sub(r'[\s.,\'’|]', '', s).replace('l', 'I').replace('1', 'I').replace('Í', 'I').replace('í', 'I')
    return s if re.fullmatch(r'X{0,3}(IX|IV|V?I{0,3})', s) and s else None


def obra_de_linhas(linhas, nome):
    """Linhas (pagina, x, y, texto, altura[, palavras]) -> obra em capítulos e parágrafos.
    Capítulo novo: página cuja primeira linha de texto desce (o «sink» das aberturas) ou que traz o
    número romano isolado; os números são dados em sequência. Parágrafo novo: linha recuada."""
    paginas = {}
    for l in linhas:
        paginas.setdefault(l[0], []).append(l)
    obra, par = [], ''
    relat = []

    def fecha():
        nonlocal par
        if par and obra:
            obra[-1]['paras'].append(par)
        par = ''

    for n in sorted(paginas):
        if not PAGINAS[nome][0] <= n <= PAGINAS[nome][1]:
            continue
        ls = paginas[n]
        cheias = [l[1] for l in ls if sum(bool(_BOA.match(w)) for w in l[3].split()) >= 5]
        if len(cheias) < 2 and not any(_romano(l[3]) for l in ls):
            continue
        # a margem: o menor x em que começam ao menos três linhas cheias (um começo solto é lixo)
        grupos = [x for x in sorted(cheias) if sum(1 for y in cheias if abs(y - x) <= 4) >= min(3, len(cheias))]
        margem = grupos[0] if grupos else (min(cheias) if cheias else min(l[1] for l in ls))
        alt = ls[0][4]
        ls = sorted(ls, key=lambda l: l[2])
        cab = next((i for i, l in enumerate(ls) if l[2] < alt * 0.22 and _e_cabeco(l[3])), None)
        if cab is not None:
            ls = ls[cab + 1:]                                     # o cabeço e o lixo acima dele
        corpo = []
        for l in ls:
            t = l[3].strip()
            rom = _romano(t) and 40 <= l[1] - margem <= 300 and l[2] < alt * 0.4
            if l[1] < margem - 15 and not rom:                    # lixo à esquerda da coluna
                ws = l[5] if len(l) > 5 else None
                if not ws:
                    continue
                ws = [(x, w) for x, w in ws if x >= margem - 15]  # tira só as palavras de fora («|»)
                if not ws:
                    continue
                t = ' '.join(w for _, w in ws)
                l = (l[0], ws[0][0], l[2], t, l[4])
            ws_ = t.split()
            if not rom and not (any(_PALAVRA.fullmatch(w) and sum(ch.isalpha() for ch in w) >= 3 for w in ws_) or
                                ws_[0] in ('—', '–', '-') and len(ws_) <= 3 and any(_PALAVRA.fullmatch(w) for w in ws_[1:]) or
                                len(ws_) <= 2 and any(re.fullmatch(r'[—–-]?[A-Za-zÀ-ÿ]{1,2}[.!?,;:…]+', w) for w in ws_)):
                continue                                          # sem palavra: lixo
            if not corpo and not rom and _e_cabeco(t):
                continue
            corpo.append((l[1], l[2], t, bool(rom)))
        if not corpo:
            continue
        # recuo pela margem local: junto à lombada a página encurva e as linhas de baixo começam mais à
        # direita. A margem de cada linha é o menor começo, entre as linhas vizinhas que não são fala
        # (as falas começam todas recuadas), sem descer da margem da página.
        rel = []
        for x, y, t, r in corpo:
            viz = [x2 for x2, y2, t2, _ in corpo if abs(y2 - y) <= 100 and not t2.startswith(('—', '–', '-'))]
            local = max(margem, min(viz)) if viz else margem
            rel.append((x - local, y, t, r))
        corpo = rel
        boa = next((i for i, c in enumerate(corpo) if sum(bool(_BOA.match(w)) for w in c[2].split()) >= 3), None)
        if boa is None:
            continue
        # abertura de capítulo: o número romano, ou o texto que começa baixo na página; nela, o que vem
        # antes do número (ou do texto) é lixo. Nas outras páginas fica tudo (a 1ª linha pode ser curta).
        rom = next((i for i, c in enumerate(corpo[:boa]) if c[3]), None)
        abre = rom is not None or corpo[boa][1] > alt * 0.27
        if abre:
            corpo = corpo[rom if rom is not None else boa:]
            rom = 0 if rom is not None else None
        if abre:
            fecha()
            k = len(obra)
            achado = _romano(corpo[rom][2]) if rom is not None else None
            relat.append((n, NUMEROS[k] if k < len(NUMEROS) else '?', achado))
            obra.append({'n': NUMEROS[k] if k < len(NUMEROS) else str(k + 1), 'titulo': '', 'paras': []})
            if rom is not None:
                corpo = corpo[rom + 1:]
            primeira = True
        else:
            primeira = False
        if not obra:
            continue
        for i, (recuo, y, t, _) in enumerate(corpo):
            t = re.sub(r'\s{2,}', ' ', t)
            t = re.sub(r'(?<=\w)\s+[-–]$', '-', t)                 # «manifesta -»: hífen solto no fim da linha
            t = re.sub(r'^[|!\[\]{}]+\s*', '', t)                    # lixo da margem no começo («| pes»)
            if re.search(r'\w-$', par):
                t = re.sub(r'^\d\s+(?=[a-zà-ÿ])', '', t)           # «dese-» / «4 jo»
            fala = t.startswith(('—', '–')) and recuo >= 10
            novo = (recuo >= 18 or fala) and not (primeira and i == 1)   # 2ª linha da capitular, também recuada
            if novo and par:
                fecha()
            if par.endswith('\xad'):
                par = par[:-1] + t
            elif re.search(r'\w-$', par) and t.startswith('-'):      # hífen repetido: «construí-» / «-lo»
                par = _juntar_hifen(par, t[1:], repetido=True)
            elif re.search(r'\w[-\xad]$', par):
                par = _juntar_hifen(par, t)
            elif re.search(r'[a-zà-ÿ]\.$', par) and re.match(r'[a-zà-ÿ]', t) and _hifen_lido_ponto(par, t):
                par = par[:-1] + t                                # «escritu.» / «ração»: o hífen lido como ponto
            else:
                par = (par + ' ' + t).strip()
    fecha()
    juntos = []
    for p in obra:                       # parágrafo que começa em minúscula continua o anterior
        ps = []
        for x in p['paras']:
            if ps and re.match(r'[a-zà-ÿ]', x) and not re.search(r'[.!?…:]$', ps[-1]):
                ps[-1] = _juntar_hifen(ps[-1], x) if re.search(r'\w-$', ps[-1]) else ps[-1] + ' ' + x
            else:
                ps.append(x)
        juntos.append(dict(p, paras=[_corrigir_ocr(x) for x in ps]))
    return fontes.normalizar(juntos)


def _juntar_hifen(a, b, repetido=False):
    """Fim de linha hifenizado. Em 1947 o hífen de verdade se repete no começo da linha seguinte
    («construí-» / «-lo»), mas o OCR também lê sujeira como hífen: a palavra junta, se existe, vence
    («con-» / «-tinuam»). Sem o hífen repetido, ele fica só antes de pronome átono depois de palavra
    que existe («Dirigi-» / «me»), e não em «Madale-» / «na», «nenhu-» / «ma»."""
    m = re.match(r"[\w']+", b)
    frag = m.group(0) if m else ''
    tronco = re.search(r'([\wÀ-ÿ]+)[-\xad]$', a).group(1)
    existe = lambda w: grafia1990.atual_parte(w)[1] != 'SEM_PAR'
    junta = existe(tronco + frag) and not (frag.lower() in fontes.CLITICOS and existe(tronco))
    if repetido and not junta:
        return a.rstrip('\xad')[:-1] + '-' + b
    if not repetido and frag.lower() in fontes.CLITICOS and existe(tronco):
        return a.rstrip('\xad')[:-1] + '-' + b
    return a.rstrip('\xad')[:-1] + b.lstrip('-')


def _hifen_lido_ponto(a, b):
    ini = re.search(r'([A-Za-zÀ-ÿ]+)\.$', a).group(1)
    fim = re.match(r'([A-Za-zÀ-ÿ]+)', b).group(1)
    sem = lambda w: grafia1990.atual_parte(w)[1] == 'SEM_PAR'
    return sem(ini) and not sem(ini + fim)


def _corrigir_ocr(p):
    """Erros sistemáticos dos OCRs: «0» por «O», aspas lidas como duas simples, travessão dobrado."""
    p = fontes.limpar(p.replace('\xad', ''))
    p = re.sub(r'(?<=[a-zà-ÿ] )0(?=s? [a-zà-ÿ])', 'o', p)              # «0» no meio da frase é «o»
    p = re.sub(r'(?<![\w,.])0(?=\.?s? [a-zà-ÿ])', 'O', p)
    p = p.replace('0.s ', 'Os ').replace('0s ', 'Os ')
    # artigo em maiúscula logo depois de palavra («tocava O hino»): o Tesseract troca a caixa do «o».
    # Depois de vírgula, não: ali a maiúscula costuma mostrar que a vírgula é um ponto mal lido.
    p = re.sub(r'(?<=[a-zà-ÿ] )(O|Os|A|As)(?= [a-zà-ÿ])', lambda m: m.group(1).lower(), p)
    p = re.sub(r'[‘\'] ?[‘\']', '“', p)
    p = re.sub(r'[’\'] ?[’\']', '”', p)
    p = re.sub(r'^[—–-]{2,}', '—', p)
    p = re.sub(r'(?<!\S)€(?!\S)', 'e', p).replace('€', 'e')        # o Tesseract lê «e» como «€»
    p = re.sub(r'^[-–] ', '— ', p)
    p = re.sub(r'(?<=\w) [-–] ?[,.] ?(?=se\b|lhe\b|o\b|a\b)', '-', p)
    return re.sub(r'[\^■*%=•|]', '', p).strip()


# trocas comuns dos OCRs (o trema lido como «ii», o «q» como «g», «rn» por «m»...)
CONFUSOES = [('gii', 'qü'), ('qii', 'qü'), ('gi', 'qü'), ('qi', 'qü'), ('gú', 'qu'), ('ii', 'ü'), ('ii', 'u'),
             ('rn', 'm'), ('m', 'rn'), ('li', 'h'), ('h', 'li'), ('h', 'b'), ('b', 'h'), ('ri', 'n'), ('n', 'ri'),
             ('u', 'n'), ('n', 'u'), ('e', 'c'), ('c', 'e'), ('e', 'o'), ('o', 'e'), ('i', 'l'), ('l', 'i'),
             ('í', 'i'), ('i', 'í'), ('1', 'l'), ('l', 'I'), ('0', 'o'), ('6', 'ó'), ('ó', 'ô'), ('ô', 'ó'),
             ('é', 'ê'), ('ê', 'é'), ('à', 'â'), ('â', 'à'), ('t', 'f'), ('f', 't'), ('v', 'y'), ('y', 'v'),
             ('ii', 'ü'), ('tl', 'd'), ('cl', 'd'), ('d', 'cl'), ('in', 'm'), ('m', 'in'), ('ni', 'm'), ('1', 'i')]
CONSERTOS = []


def _palavras(obra):
    return {chave(w) for c in obra for p in c['paras'] for w in re.findall(r'[A-Za-zÀ-ÿ0-9]+', p)}


def consertar(obra, nomes=(), atestadas=()):
    """Palavra do OCR fora do léxico trocada pela única forma do léxico a uma troca da lista acima
    (cingiienta → cinqüenta, bihelôs → bibelôs). Ficam os nomes próprios e as palavras atestadas
    (no texto de 1934 ou nos dois OCRs): o léxico não tem muitas palavras do autor (vime, eito)."""
    lex_ok = lambda w: grafia1990.atual_parte(w)[1] == 'lexico'
    cache = {}

    def um(w):
        if w in cache:
            return cache[w]
        if not re.fullmatch(r'[A-Za-zÀ-ÿ0-9]+', w) or w.lower() in nomes or chave(w) in atestadas or lex_ok(w) or len(w) < 3:
            cache[w] = w
            return w
        cands = set()
        for a, b in CONFUSOES:
            for m in re.finditer(re.escape(a), w):
                c = w[:m.start()] + b + w[m.end():]
                if lex_ok(c):
                    cands.add(c)
        cache[w] = cands.pop() if len(cands) == 1 else w
        if cache[w] != w:
            CONSERTOS.append((w, cache[w]))
        return cache[w]

    def junta(m):                       # palavra partida pelo OCR: «sempr e», «carte ira»
        a, b = m.group(1), m.group(2)
        if chave(a) not in atestadas and not lex_ok(a) and lex_ok(a + b) and a.lower() not in nomes:
            CONSERTOS.append((a + ' ' + b, a + b))
            return a + b
        return m.group(0)

    def par(p):
        p = re.sub(r'([A-Za-zÀ-ÿ]{2,}) ([a-zà-ÿ]{1,6})(?![A-Za-zÀ-ÿ])', junta, p)
        return re.sub(r'[A-Za-zÀ-ÿ0-9]+', lambda m: um(m.group(0)), p)
    return [dict(c, paras=[par(p) for p in c['paras']]) for c in obra]


def capitulares(obra, guia):
    """Nas aberturas, a capitular some no OCR e o resto da palavra vem em versalete («ntes de
    iniciar», «ID EPOIS», «M A N H E C I», «D GLÓRIA»). As palavras do começo até a primeira em
    minúsculas são trocadas pelas da guia, quando as letras batem (fora a capitular)."""
    letras = lambda ws: chave(re.sub(r'[^\wÀ-ÿ]', '', ''.join(ws)))
    out = []
    for p, g in zip(obra, guia):
        ps = list(p['paras'])
        if ps and g['paras']:
            ws = ps[0].split(' ')
            k = 0
            while k < min(len(ws), 10) and not re.search(r'[a-zà-ÿ]{2,}', ws[k]):
                k += 1
            if k == 0 and re.match(r'[a-zà-ÿ]', ws[0]):             # «onhecí»: só falta a capitular
                k = 1
            gws = g['paras'][0].split(' ')
            traco = gws[:1] if gws[0] in ('—', '–') else []
            gws = gws[len(traco):]
            if k:
                l = letras(ws[:k])
                gls = {n: letras(gws[:n]) for n in range(1, 5)}
                fortes = [n for n, gl in gls.items() if (l.endswith(gl[1:]) or len(gl) > 4 and l.endswith(gl[2:]))
                          and len(gl) - 2 <= len(l) <= len(gl) + 3]
                fracos = [n for n, gl in gls.items() if abs(len(l) - len(gl)) <= 2 and SequenceMatcher(None, l, gl).ratio() >= 0.75]
                if fortes or fracos:
                    ws = gws[:max(fortes) if fortes else max(fracos, key=lambda n: SequenceMatcher(None, l, gls[n]).ratio())] + ws[k:]
            ps[0] = ' '.join(ws)
        out.append(dict(p, paras=ps))
    return out


# ------------------------------------------------------------------ testemunhos

def _ocr(nome_pdf, leitor, guia):
    """OCR em capítulos e parágrafos; se as aberturas não forem achadas todas, os capítulos vêm do
    alinhamento com a guia."""
    o = obra_de_linhas(leitor(nome_pdf), nome_pdf)
    if [p['n'] for p in o] != NUMEROS:
        print(f'{nome_pdf}: {len(o)} aberturas achadas; capítulos pelo alinhamento')
        o = capitulos_como(o, guia)
    return capitulares(o, guia)


def capitulos_como(obra, base):
    """Põe no OCR a divisão em capítulos da base (as quebras de parágrafo são as do OCR)."""
    T2, quebras = [], set()
    for t in achatar(obra, com_titulos=False):
        if t == '¶':
            quebras.add(len(T2))
        else:
            T2.append(t)
    B = achatar(base)
    B2, marcas, i = [], [], 0
    while i < len(B):
        if B[i].startswith('#'):                      # '#', '¶', título..., '¶'
            j = B.index('¶', i + 2)
            marcas.append((len(B2), B[i:j]))
            i = j
            continue
        if B[i] != '¶':
            B2.append(B[i])
        i += 1
    mp = _mapeador(alinhar([chave(t) for t in B2], [chave(t) for t in T2]))
    onde = {mp(p, True): m for p, m in marcas}
    out = []
    for j, t in enumerate(T2):
        if j in onde:
            out += ['¶'] + onde[j] + ['¶']
        elif j in quebras:
            out.append('¶')
        out.append(t)
    return fontes.normalizar(ocr.obra_de_tokens(out))


ACENTOS = []                # (do t47, do b47, escolha, dúvida, contexto): acentos que os dois OCRs leem diferente


def _marcas(w):
    import unicodedata
    return sum(unicodedata.category(ch) == 'Mn' for ch in unicodedata.normalize('NFD', w))


def acentos(t47, b47, testemunhos34):
    """Onde os dois OCRs de 1947 leem a mesma palavra com acentos diferentes (o alinhamento não os
    vê: a chave ignora acentos), decide-se assim:
    - palavra curta (e/é, a/à, as/às, o/ó, ao/ão...): o Tesseract inventa acentos («É ficámos», «À
      princípio»), e os dois OCRs erram. Votam as cinco leituras, as duas de 1947 e as três de 1934
      (Wikisource e os dois OCRs; o «á» da crase de 1934 vale «à»);
    - palavra longa: se só uma das formas existe hoje, vale ela; se as duas (crédito × credito), a
      acentuada, porque os OCRs perdem acentos mais do que inventam.
    Os empates e os casos com as duas formas possíveis vão para a conferência (ACENTOS, 'duvida')."""
    T, B = achatar(t47), achatar(b47)

    def mapa(outro):
        O = achatar(outro)
        m = {}
        for tp, i1, i2, j1, j2 in alinhar(T, O, chave=chave):
            if tp == 'equal':
                m.update({i1 + k: O[j1 + k] for k in range(i2 - i1)})
        return m
    par = mapa(b47)
    m34 = [mapa(o) for o in testemunhos34]
    crase = {'á': 'à', 'ás': 'às'}
    lex = grafia1990.lexico()
    hoje = lambda w: grafia1990.atual(w)[0].lower()
    existe = lambda w: all(re.sub(r'[òèìù]', lambda m: grafia1990.CAIDOS[m.group(0)], grafia1990.ao1990(p.lower()))
                           in lex for p in w.split('-') if p)
    novo = list(T)
    for i, t in enumerate(T):
        b = par.get(i)
        if b is None or b == t or not e_palavra(t) or t.lower() == b.lower() or hoje(t) == hoje(b):
            continue
        lt, lb = t.lower(), b.lower()
        if len(t) <= 3:
            votos = {lt: 1, lb: 1}
            for m in m34:
                w = m.get(i)
                w = crase.get(w.lower(), w.lower()) if w else None
                if w in votos:
                    votos[w] += 1
            esc = t if votos[lt] > votos[lb] else b if votos[lb] > votos[lt] else (t if _marcas(t) < _marcas(b) else b)
            duvida = abs(votos[lt] - votos[lb]) <= 1
        else:
            et, eb = existe(t), existe(b)
            duvida = et == eb
            if et != eb:
                esc = t if et else b
            elif et:
                esc = b if _marcas(b) > _marcas(t) else t
            else:                                                # nenhuma existe: lixo de OCR (aporrinhaçãô)
                esc = t
        if esc != t:
            novo[i] = igualar_caixa(t, esc)
        ACENTOS.append((t, b, novo[i], duvida, junta_(T[max(0, i - 6):i + 6])))
    return fontes.normalizar(ocr.obra_de_tokens(novo))


def junta_(ts):
    from edicao.tokens import texto
    return texto([t for t in ts if t != '¶' and not t.startswith('#')])


# o que vai em itálico em 1947 (conferido nas imagens): os jornais e os «ss» de d. Marcela. O OCR não
# vê itálico; em 1934 os jornais iam em itálico e entre aspas.
ITALICOS = [r'Correio de Viçosa', r'Gazeta', r'Cruzeiro', r'ss']


def italicos(obra):
    rx = re.compile(r'(?<![\w_])(' + '|'.join(ITALICOS) + r')(?![\w_])')
    return [dict(c, paras=[rx.sub(r'_\1_', p) for p in c['paras']]) for c in obra]


def transcricoes():
    global SITIOS34
    ws = ws34()
    nomes = {w.lower() for p in ws for x in p['paras'] for a, w in zip(x.split(' '), x.split(' ')[1:])
             if w[:1].isupper() and a[-1:].isalpha()}
    nomes = {re.sub(r'\W', '', w) for w in nomes}
    o34 = [_ocr(PDF34, f, ws) for f in (_linhas_tess, _linhas_bbm)]
    o47 = [_ocr(PDF47, f, ws) for f in (_linhas_tess, _linhas_bbm)]
    at34 = _palavras(ws) | (_palavras(o34[0]) & _palavras(o34[1]))
    at47 = _palavras(ws) | (_palavras(o47[0]) & _palavras(o47[1]))
    t34, b34 = (consertar(o, nomes, at34) for o in o34)
    t47, b47 = (consertar(o, nomes, at47) for o in o47)
    E34, SITIOS34 = estabelecer.estabelecer({'ws34': ws, 't34': t34, 'b34': b34}, 'ws34', {'t47': t47, 'b47': b47},
                                            correlacionados=[('t34', 'b34')], um_voto=True)
    global M34
    a34 = fontes.normalizar(ocr.obra_de_tokens(E34))
    t47 = italicos(acentos(t47, b47, (ws, t34, b34)))
    M34 = fontes.normalizar(ocr.obra_de_tokens([de_1934(t) if e_palavra(t) else t for t in achatar(a34)]))
    pickle.dump({'ws34': ws, 't34': t34, 'b34': b34, 'sitios34': SITIOS34, 'a34': a34, 'acentos': ACENTOS},
                open(fontes.cache(OBRA, 'testemunhos34.pkl'), 'wb'))
    return {'t47': t47, 'b47': b47}


def de_1934(t):
    """Uma palavra de 1934 na grafia de hoje (fazel-o → fazê-lo, annos → anos)."""
    t = re.sub(r'(\w)l-(o|a|os|as)$', r'\1-l\2', t)
    crase = {'á': 'à', 'ás': 'às', 'Á': 'À', 'Ás': 'Às'}             # 1934 marca a crase com o agudo
    if t in crase:
        return crase[t]
    return grafia1990.atual(t)[0]


def modernas():
    return {'m34': M34}


DUVIDAS = []


def _nomes(m34):
    """Nomes próprios: palavras em maiúscula no meio da frase, no texto de 1934 e no OCR de 1947."""
    t34 = pickle.load(open(fontes.cache(OBRA, 'testemunhos34.pkl'), 'rb'))
    nomes = set()
    for obra in (t34['ws34'], m34):
        T = achatar(obra)
        for a, b in zip(T, T[1:]):
            if e_palavra(b) and b[:1].isupper() and e_palavra(a):
                nomes.add(b.lower())
    return nomes


def rever(tr, md, sitios):
    """Desempate dos dois OCRs de 1947 onde nenhum coincide com 1934 (m34): vence a leitura com menos
    palavras fora do léxico; empate, a mais parecida com 1934. Se as duas têm palavras desconhecidas e
    1934 não, vale 1934 (na grafia de hoje), marcado para conferir. Devolve (E, sítios)."""
    from edicao.tokens import texto as junta
    lex = grafia1990.lexico()
    nomes = _nomes(md['m34'])
    sem = lambda w: sem_acento_(w)

    def desconhecidas(toks):
        n = 0
        for t in toks:
            if not e_palavra(t) or t.lower() in nomes:
                continue
            for p in t.split('-'):
                if p and grafia1990.atual_parte(p)[1] == 'SEM_PAR' and p.lower() not in nomes:
                    n += 1
        return n

    def parecido(a, b):
        return SequenceMatcher(None, ' '.join(chave(t) for t in a), ' '.join(chave(t) for t in b), autojunk=False).ratio()

    B = achatar(tr[BASE])
    DUVIDAS.clear()
    for x in sitios:
        if x['apoio'] or x['por'].startswith('maioria'):
            continue
        T = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
        m = _toks(x['modernas']['m34'])
        nm = sum(1 for t in m if e_palavra(t))
        falta = lambda ts: abs(sum(1 for t in ts if e_palavra(t)) - nm)     # linha que o OCR perdeu
        cand = sorted(T, key=lambda n: (desconhecidas(T[n]) + falta(T[n]), -parecido(T[n], m), n != BASE))
        esc = cand[0]
        d = {n: desconhecidas(T[n]) for n in T}
        palavras = lambda ts: [chave(t) for t in ts if e_palavra(t)]
        sinais = lambda ts: [t for t in ts if not e_palavra(t) and t != '¶']
        if len({tuple(palavras(v)) for v in list(T.values()) + [m]}) == 1:
            # só a pontuação diverge: a mais perto da de 1934 (o OCR acrescenta pontos e vírgulas de sujeira)
            dist = lambda n: SequenceMatcher(None, sinais(T[n]), sinais(m)).ratio()
            esc = max(T, key=lambda n: (dist(n), n == BASE))
            x['escolha'], x['por'] = T[esc], f'pontuação; {esc}'
            x['escolha_txt'] = junta(x['escolha'])
            DUVIDAS.append(x)
            continue
        if all(v > 0 for v in d.values()) and desconhecidas(m) == 0 and max(parecido(T[n], m) for n in T) >= 0.6:
            x['escolha'], x['por'] = m, 'm34 (os dois OCRs com palavras desconhecidas)'
        else:
            x['escolha'], x['por'] = T[esc], f'léxico; {esc}'
        x['escolha_txt'] = junta(x['escolha'])
        if d[esc] == 0 and sum(1 for v in d.values() if v == 0) > 1 or x['por'].startswith('m34'):
            DUVIDAS.append(x)
    E, pos = [], 0
    for x in sitios:
        E.extend(B[pos:x['s']])
        E.extend(x['escolha'])
        pos = x['e']
    E.extend(B[pos:])
    return [t for t in E if t != '*'], sitios


def _toks(s):
    from edicao.tokens import TOK
    out = []
    for parte in re.split(r'(¶|#\S*)', s):
        if parte == '¶' or parte.startswith('#'):
            out.append(parte)
        else:
            out += TOK.findall(parte)
    return out


def sem_acento_(w):
    import unicodedata
    return ''.join(ch for ch in unicodedata.normalize('NFD', w) if unicodedata.category(ch) != 'Mn')


def modernizar(E, manual):
    """Grafia de 1947 (Formulário de 1943) -> Acordo de 1990, palavra por palavra (grafia1990.py)."""
    return grafia1990.modernizar(E, manual)
