"""Infância — fontes.

Memórias, publicadas em 1945 (José Olympio), a única edição em vida do autor. A Brasiliana USP tem dois
exemplares (bbm/8871 e bbm/8394): é a edição-base. Não há edição moderna gratuita: a grafia de hoje sai de
regras (grafia1990.py), e o texto, do voto das quatro leituras dos dois exemplares.

Testemunhos (todos votam, um voto cada):
- 't47' e 'b47': o Tesseract (tesseract.py) e o OCR do PDF do exemplar 1 (bbm/8871). 't47' é a base
  (o nome vem do método de Caetés e Insônia, de 1947).
- 'u47' e 'c47': o mesmo no exemplar 2 (bbm/8394).
Sem maioria, rever() escolhe pelo léxico, e as escolhas sem apoio vão para a conferência nas imagens.

Cada capítulo abre página nova, com o título no alto e a primeira palavra com capitular: as páginas de
abertura estão em INICIOS (do exemplar 1; no 2, DESLOCAMENTO páginas depois), e as primeiras palavras, em
PRIMEIRAS. Os capítulos têm título e não têm número (como em Vidas Secas).
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

OBRA = 'infancia'

META = {
    'id': OBRA,
    'autor': 'graciliano-ramos',
    'titulo': 'Infância',
    'ano': 1945,
    'genero': 'Memórias',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Memórias publicadas em 1945.',
}

BASE = 't47'
REFERENCIAS = []            # sem edição moderna: a grafia vem de modernizar(), abaixo
CORRELACIONADOS = []
UM_VOTO = False

PDF1, PDF2 = 'bbm8871', 'bbm8394'
PAGINAS = {PDF1: (7, 281), PDF2: (19, 293)}
DESLOCAMENTO = {PDF1: 0, PDF2: 12}
INICIOS = [7, 20, 27, 33, 39, 46, 52, 61, 67, 75, 82, 87, 95, 103, 112, 119, 126, 136, 142, 151, 160, 167, 172, 181,
           184, 188, 196, 203, 208, 215, 221, 227, 233, 239, 247, 255, 262, 267, 273]   # páginas do índice + 2 (exemplar 1)
TITULOS = ['Nuvens', 'Manhã', 'Verão', 'Um cinturão', 'Uma bebedeira', 'Chegada à vila', 'A vila', 'Vida nova',
           'Padre João Inácio', 'O fim do mundo', 'O inferno', 'O moleque José', 'Um incêndio', 'José da Luz',
           'Leitura', 'Escola', 'D. Maria', 'O barão de Macaúbas', 'Meu avô', 'Cegueira', 'Chico Brabo',
           'José Leonardo', 'Minha irmã natural', 'Antônio Vale', 'Mudança', 'Adelaide', 'Um enterro',
           'Um novo professor', 'Um intervalo', 'Os astrônomos', 'Samuel Smiles',
           'O menino da mata e o seu cão Piloto', 'Fernando', 'Jerônimo Barreto', 'Venta-Romba',
           'Mário Venâncio', 'Seu Ramiro', 'A criança infeliz', 'Laura']


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
                     r'^(?:\d+\s*)?[IJ]?\s*N\s*F\s*[AÂ]\s*N\s*[CO]\s*[IlÍ]\s*A\s*\.?(?:\s*\d+)?$|^\[?\s*\d+\s*\]?$', re.I)

def _e_cabeco(t):
    """Cabeço de página: «6 OBRAS DE GRACILIANO RAMOS», «INFÂNCIA 7», «GRACILIANO RAMOS», o número."""
    t = t.strip()
    u = re.sub(r'[^A-Z0-9]', '', t.upper())
    if _CABECO.match(t) or re.fullmatch(r'\d{1,3}', u):
        return True
    return len(t) < 45 and (('OBRAS' in u or 'RAMOS' in u or 'GRAC' in u) or
                            re.search(r'NF[AÂ]N', u) and len(u) < 16) and sum(ch.islower() for ch in t) <= 2

def _romano(s):
    s = s.upper() if re.fullmatch(r'[\Wvx]*[vx][\Wvxi]*', s) else s       # «v» minúsculo do Tesseract
    s = re.sub(r'[\s.,\'’|]', '', s).replace('l', 'I').replace('1', 'I').replace('Í', 'I').replace('í', 'I')
    return s if re.fullmatch(r'X{0,3}(IX|IV|V?I{0,3})', s) and s else None

ABERTURAS = {}              # nome do PDF -> [(página, número dado, número lido)]


def obra_de_linhas(linhas, nome, dadas=None):
    """Linhas (pagina, x, y, texto, altura[, palavras]) -> obra em capítulos e parágrafos.
    Capítulo novo: o número romano isolado, centrado na coluna (os números são dados em
    sequência); o capítulo I abre a primeira página. Parágrafo novo: linha recuada."""
    paginas = {}
    for l in linhas:
        paginas.setdefault(l[0], []).append(l)
    obra, par = [], ''
    relat = ABERTURAS.setdefault(nome, [])
    relat.clear()
    _CANDIDATOS[nome] = []

    def fecha():
        nonlocal par
        if par and obra:
            obra[-1]['paras'].append(par)
        par = ''

    prox = 0
    for n in sorted(paginas):
        if not PAGINAS[nome][0] <= n <= PAGINAS[nome][1]:
            continue
        while prox < len(INICIOS) and INICIOS[prox] + DESLOCAMENTO[nome] <= n:  # o conto abre na página dele, mesmo se a
            fecha()                                          # leitura dela falhou
            relat.append((INICIOS[prox] + DESLOCAMENTO[nome], TITULOS[prox], None))
            obra.append({'n': '', 'titulo': TITULOS[prox], 'paras': []})
            prox += 1
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
            xr = l[1]
            if not _romano(t) and len(l) > 5 and len(t) <= 10:   # sujeira antes do número («\\ XXI»)
                rs = [(x, w) for x, w in l[5] if _romano(w)]
                if len(rs) == 1 and len(re.sub(r'\W', '', t)) - len(rs[0][1]) <= 1:
                    xr, t = rs[0]
            rom = False                     # os contos não têm números
            if rom and dadas is None:
                _CANDIDATOS[nome].append((n, l[2], _romano(t)))
            if dadas is not None:           # as aberturas já achadas (achar_aberturas): marcadas adiante
                rom = any(p == n and abs(y0 - l[2]) < 16 for p, y0, _ in dadas) and len(t) <= 8
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
        if n - DESLOCAMENTO[nome] in INICIOS and boa is not None:     # abertura do conto: o lixo acima do texto sai
            corpo = corpo[boa:]
        if boa is None:
            continue
        # abertura de capítulo: o número romano centrado na coluna, em qualquer altura da página (os
        # capítulos correm um depois do outro); o primeiro capítulo abre a primeira página.
        if not obra:
            continue
        faltam = []
        if dadas is not None:           # cada abertura dada marca uma linha só: a do número, ou a mais perto
            corpo = [(a, y, t, False) for a, y, t, _ in corpo]
            for p, y0, _ in dadas:
                if p != n:
                    continue
                perto = [i for i, (_, y, t, _) in enumerate(corpo) if abs(y - y0) < 16 and len(t) <= 8]
                if perto:
                    i = min(perto, key=lambda i: (not _romano(corpo[i][2]), abs(corpo[i][1] - y0)))
                    corpo[i] = corpo[i][:3] + (True,)
                else:
                    faltam.append(y0)
        for i, (recuo, y, t, r) in enumerate(corpo):
            if faltam and y > faltam[0]:   # o número que esta leitura perdeu: o capítulo abre na linha seguinte
                faltam.pop(0)
                r, t = True, ''
            if r:
                fecha()
                k = len(obra)
                relat.append((n, NUMEROS[k] if k < len(NUMEROS) else '?', _romano(t) if t else None))
                obra.append({'n': NUMEROS[k] if k < len(NUMEROS) else str(k + 1), 'titulo': '', 'paras': []})
                if t or _romano(corpo[i][2]):
                    continue
                t = corpo[i][2]
            t = re.sub(r'\s{2,}', ' ', t)
            t = re.sub(r'(?<=\w)\s+[-–]$', '-', t)                 # «manifesta -»: hífen solto no fim da linha
            t = re.sub(r'^[|!\[\]{}]+\s*', '', t)                    # lixo da margem no começo («| pes»)
            if re.search(r'\w-$', par):
                t = re.sub(r'^\d\s+(?=[a-zà-ÿ])', '', t)           # «dese-» / «4 jo»
            fala = t.startswith(('—', '–')) and recuo >= 10
            novo = recuo >= 18 or fala
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

ABREVIATURAS = {'d', 'dr', 'sr', 'sra', 'srs', 's', 'v', 'exa', 'excia', 'etc', 'n', 'cia'}


def _hifen_lido_ponto(a, b):
    ini = re.search(r'([A-Za-zÀ-ÿ]+)\.$', a).group(1)
    fim = re.match(r'([A-Za-zÀ-ÿ]+)', b).group(1)
    sem = lambda w: grafia1990.atual_parte(w)[1] == 'SEM_PAR'
    return sem(ini) and not sem(ini + fim)

def _corrigir_ocr(p):
    """Erros sistemáticos dos OCRs: «0» por «O», aspas lidas como duas simples, travessão dobrado."""
    p = fontes.limpar(p.replace('\xad', '').replace('_', ' '))     # o OCR não marca itálico: ITALICOS
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
    return re.sub(r'[\^■*%=•|#]', '', p).strip()

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
    (lidas iguais em três OCRs): o léxico não tem muitas palavras do autor (vime, eito)."""
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
        # palavra partida no fim da linha sem o hífen: junta-se, mesmo atestada nas leituras (o hífen se
        # perde em todas), quando a primeira parte não existe sozinha e a palavra inteira sim
        if not lex_ok(a) and lex_ok(a + b) and a.lower() not in nomes and len(a + b) >= 6:
            CONSERTOS.append((a + ' ' + b, a + b))
            return a + b
        return m.group(0)

    def par(p):
        # o hífen do fim da linha lido como «:» ou «;» («im: pelido», «con: tar»)
        p = re.sub(r'(?<![A-Za-zÀ-ÿ])([A-Za-zÀ-ÿ]{1,})[:;] ([a-zà-ÿ]{2,})(?![A-Za-zÀ-ÿ])',
                   lambda m: (CONSERTOS.append((m.group(0), m.group(1) + m.group(2))) or m.group(1) + m.group(2))
                   if lex_ok(m.group(1) + m.group(2)) and not lex_ok(m.group(2)) else m.group(0), p)
        p = re.sub(r'([A-Za-zÀ-ÿ]{2,}) ([a-zà-ÿ]{1,9})(?![A-Za-zÀ-ÿ])', junta, p)
        return re.sub(r'[A-Za-zÀ-ÿ0-9]+', lambda m: um(m.group(0)), p)
    return [dict(c, paras=[par(p) for p in c['paras']]) for c in obra]

def versalete(obra, caixa):
    """A primeira palavra (ou as primeiras) de cada capítulo vem em versalete: o OCR a lê em maiúsculas
    («ADRIÃO,», «À NOITE», «RECOSTEI-ME», «O DR. LIBERATO»). Elas vão para minúsculas, com a inicial
    maiúscula na primeira; as outras levam maiúscula só se, no resto do livro, aparecem mais vezes com
    maiúscula do que sem ela no meio da frase (caixa: palavra -> [com maiúscula, sem])."""
    out = []
    for c in obra:
        ps = list(c['paras'])
        while ps and sum(ch.isalpha() for ch in ps[0]) < 3:     # sujeira no lugar do número («I», «.»)
            ps.pop(0)
        if ps:
            ps[0] = re.sub(r'^([«“"—–-]*\s*)0(?=[\s.,])', r'\1O', ps[0])
            ws = ps[0].split(' ')
            k = 0
            caps = lambda w: re.fullmatch(r'[^a-zà-ÿ]*[A-ZÀ-Ý0][A-ZÀ-Ý0-]*[^a-zà-ÿ]*', w) and re.search(r'[A-ZÀ-Ý]', w)
            while k < min(len(ws), 4) and caps(ws[k]) and (len(re.sub(r'\W', '', ws[k])) > 1 or k + 1 < len(ws) and caps(ws[k + 1])):
                w = re.sub(r'^([^\w]*)0', r'\1O', ws[k])
                miud = w.lower()
                m = re.search(r'[a-zà-ÿ]', miud)
                chave_ = re.sub(r'\W', '', miud)
                com, sem = caixa.get(chave_, (0, 0))
                if m and (k == 0 or com > sem and len(chave_) > 2):
                    miud = miud[:m.start()] + miud[m.start()].upper() + miud[m.start() + 1:]
                ws[k] = miud
                k += 1
            ps[0] = ' '.join(ws)
        out.append(dict(c, paras=ps))
    return out


def caixa_das_palavras(obra):
    """palavra -> [vezes com maiúscula, vezes sem] no meio da frase (depois de outra palavra)."""
    T = achatar(obra)
    conta = {}
    for k in range(1, len(T)):
        a, b = T[k - 1], T[k]
        depois_de_abrev = a == '.' and k > 1 and T[k - 2].lower() in ('d', 'dr', 'sr', 'sra', 's')
        if (e_palavra(a) or depois_de_abrev) and e_palavra(b) and re.search(r'[a-zà-ÿ]', b[1:] or 'x'):
            par = conta.setdefault(b.lower(), [0, 0])
            par[0 if b[:1].isupper() else 1] += 1
    return conta


NOMES = set()               # nomes próprios (minúsculas), achados nos OCRs: transcricoes()

# ------------------------------------------------------------------ testemunhos

_CANDIDATOS = {}            # nome do PDF -> [(página, y, número lido)] da última leitura (obra_de_linhas)


def _ocr(nome_pdf, leitor):
    """OCR em contos e parágrafos (os contos abrem nas páginas de INICIOS)."""
    return obra_de_linhas(leitor(nome_pdf), nome_pdf)


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

def acentos(t47, b47, outros):
    """Onde os dois OCRs de 1947 leem a mesma palavra com acentos diferentes (o alinhamento não os
    vê: a chave ignora acentos), decide-se assim:
    - palavra curta (e/é, a/à, as/às, o/ó, ao/ão...): o Tesseract inventa acentos («É ficámos», «À
      princípio»), e os dois OCRs erram. Votam as cinco leituras de 1947;
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
    m34 = [mapa(o) for o in outros]
    crase = {}
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

# o que vai em itálico em 1947 (conferido nas imagens; italico.py acha os candidatos)
ITALICOS = []

def italicos(obra):
    if not ITALICOS:
        return obra
    rx = re.compile(r'(?<![\w_])(' + '|'.join(ITALICOS) + r')(?![\w_])')
    return [dict(c, paras=[rx.sub(r'_\1_', p) for p in c['paras']]) for c in obra]

LEITURAS = {'t47': (PDF1, '_linhas_tess'), 'b47': (PDF1, '_linhas_bbm'), 'u47': (PDF2, '_linhas_tess'),
            'c47': (PDF2, '_linhas_bbm')}
CAPITULOS = {}              # nome -> capítulos achados pelas aberturas (antes do alinhamento)

def transcricoes():
    """As cinco leituras de 1947, em capítulos e parágrafos. A guia dos capítulos é a primeira leitura
    em que as aberturas foram achadas todas; as outras, se faltar alguma, pelo alinhamento com ela."""
    brutas = {n: _ocr(pdf, globals()[f]) for n, (pdf, f) in LEITURAS.items()}
    for n, o in brutas.items():
        CAPITULOS[n] = [p['titulo'] for p in o]
        print(n, len(o), 'aberturas')
    titulos = list(TITULOS)
    for n, o in brutas.items():
        if [p['titulo'] for p in o] != titulos:
            raise SystemExit(f'{n}: os contos não bateram: ' + str([p['titulo'] for p in o]))
    obras = brutas
    # nomes próprios: em maiúscula no meio da frase, em duas leituras ou mais
    conta = {}
    for o in obras.values():
        T = achatar(o)
        vistos = {b.lower() for a, b in zip(T, T[1:]) if e_palavra(b) and b[:1].isupper() and e_palavra(a)
                  and re.search(r'[a-zà-ÿ]', b[1:])}         # o versalete (UMA TARDE) não é nome
        for w in vistos:
            conta[w] = conta.get(w, 0) + 1
    NOMES.clear()
    NOMES.update(w for w, k in conta.items() if k >= 2)
    caixa = caixa_das_palavras(obras['t47'])
    obras = {n: versalete(o, caixa) for n, o in obras.items()}
    # palavras atestadas: lidas iguais em três leituras ou mais (o léxico não tem muitas do autor)
    conta = {}
    for o in obras.values():
        for w in _palavras(o):
            conta[w] = conta.get(w, 0) + 1
    atestadas = {w for w, k in conta.items() if k >= 3}
    obras = {n: consertar(o, NOMES, atestadas) for n, o in obras.items()}
    obras = {n: primeiras(sem_titulo(o)) for n, o in obras.items()}
    obras['t47'] = italicos(acentos(obras['t47'], obras['b47'], (obras['u47'], obras['c47'])))
    pickle.dump({'capitulos': CAPITULOS, 'acentos': ACENTOS, 'nomes': sorted(NOMES)},
                open(fontes.cache(OBRA, 'testemunhos.pkl'), 'wb'))
    return obras

PRIMEIRAS = {              # índice do capítulo -> as primeiras palavras certas (a capitular engana o OCR)
    0: 'A primeira', 1: 'Mergulhei', 2: 'Dêsse antigo', 3: 'As minhas', 4: 'Andámos',
    5: 'Era uma', 6: 'Buíque tinha', 7: 'A nossa', 8: 'O ponto', 9: 'Minha mãe',
    10: 'Às vezes', 11: 'A preta', 12: 'Numa das', 13: 'Para reduzir-me', 14: 'Achava-me',
    15: 'A preguiça,', 16: 'A mulher', 17: 'Um grosso', 18: 'Minha mãe', 19: 'Afastou-me',
    20: 'O que', 21: 'Aparecia', 22: 'Tínhamos', 23: 'Tínhamos', 24: 'Uma caminhada',
    25: 'A sociedade', 26: 'Naquele dia', 27: 'Tiraram-me', 28: 'Seu Nuno', 29: 'Aos nove',
    30: 'Eu tinha', 31: 'Descobri', 32: 'É uma', 33: 'Apareceu', 34: 'Ofereceram a',
    35: 'Organizou-se uma', 36: 'Naquele tempo', 37: 'No colégio', 38: 'Aos onze',
}


def sem_titulo(obra):
    """Tira do começo do capítulo o título, quando a leitura o juntou ao texto («Padre João Inácio Padre…»)."""
    letras = lambda t: re.sub(r'[^a-z]', '', sem_acento_(t).lower())
    out = []
    for k, c in enumerate(obra):
        ps = list(c['paras'])
        T = letras(TITULOS[k])
        while ps:
            ws = ps[0].split(' ')
            n = next((j for j in range(1, min(len(ws), 12) + 1) if len(letras(' '.join(ws[:j]))) >= len(T)), None)
            if n and SequenceMatcher(None, letras(' '.join(ws[:n])), T).ratio() >= 0.8:
                resto = ' '.join(ws[n:]).strip()
                if resto:
                    ps[0] = resto
                else:
                    ps.pop(0)
                continue
            break
        out.append(dict(c, paras=ps))
    return out


def primeiras(obra):
    """Troca, no começo de cada conto, as palavras que o OCR leu da capitular e do versalete pelas de
    PRIMEIRAS: as primeiras k palavras cujas letras mais se parecem com as do começo certo."""
    letras = lambda ws: re.sub(r'[^a-z]', '', sem_acento_(' '.join(ws)).lower())
    out = []
    for k, c in enumerate(obra):
        ps = list(c['paras'])
        certo = PRIMEIRAS.get(k)
        if certo and ps:
            ws = ps[0].split(' ')
            T = letras([certo])
            notas = [(SequenceMatcher(None, letras(ws[:k]), T).ratio(), k) for k in range(1, min(8, len(ws)) + 1)]
            r, k = max(notas)
            if r >= 0.6:
                ps[0] = ' '.join([certo] + ws[k:])
            elif re.match(r'[a-zà-ÿ]', ps[0]):        # a leitura perdeu as primeiras palavras
                ps[0] = certo + ' ' + ps[0]
        out.append(dict(c, paras=ps))
    return out


def modernas():
    return {}

DUVIDAS = []

def rever(tr, md, sitios):
    """Desempate onde não houve maioria: vence a leitura com menos palavras fora do léxico (e que não
    perde nem ganha palavras em relação às outras); empate, a do t47. As escolhas em que mais de uma
    leitura é toda de palavras que existem vão para a conferência (DUVIDAS). Devolve (E, sítios)."""
    from edicao.tokens import texto as junta
    nomes = set(pickle.load(open(fontes.cache(OBRA, 'testemunhos.pkl'), 'rb'))['nomes'])

    def desconhecidas(toks):
        n = 0
        for t in toks:
            if not e_palavra(t) or t.lower() in nomes:
                continue
            for p in t.split('-'):
                if p and grafia1990.atual_parte(p)[1] == 'SEM_PAR' and p.lower() not in nomes:
                    n += 1
        return n

    B = achatar(tr[BASE])
    DUVIDAS.clear()
    for x in sitios:
        if x['por'].startswith('maioria'):
            continue
        T = {n: _toks(v) for n, v in x['leituras'].items() if v != '(lacuna)'}
        npal = sorted(sum(1 for t in v if e_palavra(t)) for v in T.values())
        med = npal[len(npal) // 2]
        falta = lambda ts: abs(sum(1 for t in ts if e_palavra(t)) - med)
        d = {n: desconhecidas(T[n]) for n in T}
        esc = min(T, key=lambda n: (d[n] + falta(T[n]), n != BASE, list(LEITURAS).index(n)))
        x['escolha'], x['por'] = T[esc], f'léxico; {esc}'
        x['escolha_txt'] = junta(x['escolha'])
        boas = {tuple(chave(t) for t in T[n] if e_palavra(t)) for n in T if d[n] == 0 and falta(T[n]) == 0}
        if len(boas) > 1 or d[esc] > 0:
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
