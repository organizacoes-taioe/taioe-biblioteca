"""Angústia — fontes.

Edições em vida do autor: 1ª, José Olympio, 1936; 2ª, José Olympio, 1941; 3ª, José Olympio, 1947
(_Obras_, vol. 3). A 1ª e a 2ª não estão digitalizadas. A 3ª é a última revista pelo autor e está em
fac-símile na Brasiliana USP (bbm/8415): é a edição-base. A Brasiliana tem também as provas dela
(bbm/8482, 1946: folhas soltas, com as correções à mão do autor). Não há edição moderna gratuita: a
grafia de hoje sai de regras (grafia1990.py), e os desempates, dos OCRs.

Testemunhos de 1947 (os que votam o texto):
- 't47': OCR próprio (Tesseract, tesseract.py) do fac-símile de 1947. Base do confronto.
- 'b47': o OCR que vem no PDF da Brasiliana, do mesmo fac-símile.
Onde os dois concordam, é o texto de 1947. Onde divergem, rever() escolhe pelo texto impresso das
provas ('p46') e pelo léxico; as escolhas sem apoio vão para a conferência nas imagens.
Testemunhos das provas (estabelecem o 'p46', o texto impresso antes das correções à mão):
- 't46' e 'b46': o Tesseract e o OCR da Brasiliana das provas (só as páginas ímpares do PDF; as
  pares são o verso das folhas, em branco). Empate entre os dois se resolve pelo apoio de 1947.

O livro não tem capítulos: o texto corre em seções separadas por uma vinheta, com a primeira palavra
(ou as primeiras) em versalete. Aqui as seções são numeradas em sequência (1, 2, 3…), decisão do Gere
de 2026-10-26. A abertura de seção se reconhece pelo espaço em branco: um vão grande entre duas linhas
(o da vinheta) ou a primeira linha da página que começa baixa.
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

OBRA = 'angustia'

META = {
    'id': OBRA,
    'autor': 'graciliano-ramos',
    'titulo': 'Angústia',
    'ano': 1936,
    'genero': 'Romance',
    'divisao': {'singular': 'seção', 'plural': 'seções'},
    'descricao': 'Romance publicado em 1936, o terceiro de Graciliano Ramos.',
}

BASE = 't47'
# Sem edição moderna. Faz as vezes dela, para desempatar, o texto impresso das provas de 1946 ('p46'),
# na mesma grafia de 1947: onde os dois OCRs de 1947 divergem, vence a leitura que coincide com ele.
# A grafia do texto final vem de modernizar() abaixo.
REFERENCIAS = [('p46', True)]
P46 = None

PDF47, PDF46 = 'bbm8415', 'bbm8482'
PAGINAS = {PDF47: (7, 225), PDF46: (9, 427)}      # da primeira à última página de texto, nos PDFs
SITIOS46 = []               # divergências do estabelecimento das provas (para conferência)
SECOES = {}                 # nome do OCR -> [(página, primeiras palavras)] das aberturas achadas


def _pagina_util(nome, n):
    """As provas têm o verso de cada folha em branco: só as páginas ímpares do PDF."""
    a, b = PAGINAS[nome]
    return a <= n <= b and (nome != PDF46 or n % 2 == 1)


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
        # pedaços da mesma linha física em blocos diferentes viram uma linha só (ver São Bernardo)
        juntas = [sorted(v) for v in linhas.values()]
        mudou = True
        while mudou:
            mudou = False
            for a in juntas:
                for b in juntas:
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
        for ws in sorted(juntas, key=lambda j: sorted(w[1] for w in j)[len(j) // 2]):
            y = sorted(w[1] for w in ws)[len(ws) // 2]
            out.append((n, ws[0][0], y, ' '.join(w[2] for w in ws), alturas[n], [(w[0], w[2]) for w in ws]))
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
                     r'^(?:\d+\s*)?A\s*N\s*G\s*[UÚ]\s*S\s*T\s*[IÍl1]\s*A(?:\s*\d+)?$|^\[?\s*\d+\s*\]?$', re.I)


def _e_cabeco(t):
    """Cabeço de página: «6 OBRAS DE GRACILIANO RAMOS», «ANGÚSTIA 7», «GRACILIANO RAMOS», o número."""
    t = t.strip()
    u = re.sub(r'[^A-Z0-9]', '', t.upper())
    if _CABECO.match(t) or re.fullmatch(r'\d{1,3}', u):
        return True
    return len(t) < 45 and (('OBRAS' in u or 'RAMOS' in u or 'GRAC' in u) or
                            re.search(r'NG[UÚ]?ST', u) and len(u) < 16) and sum(ch.islower() for ch in t) <= 2


def _limpar_corpo(ls, margem):
    """Tira das linhas da página (já sem o cabeço) o lixo: palavras à esquerda da coluna, linhas sem palavra."""
    corpo = []
    for l in ls:
        t = l[3].strip()
        # sujeira solta no começo da linha (a sombra da lombada lida como «|», «!», «4»): sai, e a linha
        # começa na palavra seguinte (senão o recuo dos parágrafos se perde)
        ws0 = l[5] if len(l) > 5 else None
        while ws0 and len(ws0) > 2 and re.fullmatch(r'[|!¡?\[\](){}0-9\'"‘’“”.,:;*]{1,2}', ws0[0][1]) \
                and ws0[1][0] - ws0[0][0] > 4:
            ws0 = ws0[1:]
            l = (l[0], ws0[0][0], l[2], ' '.join(w for _, w in ws0), l[4], ws0)
            t = l[3].strip()
        if l[1] < margem - 15:                                # lixo à esquerda da coluna
            ws = l[5] if len(l) > 5 else None
            if not ws:
                continue
            # fica o que está na coluna e, até 45 pontos antes dela, as palavras de verdade: em página de
            # diálogo quase toda linha começa recuada, a margem calculada sai do recuo, e a linha que
            # começa na margem real («inferno.») parecia sujeira
            ws = [(x, w) for x, w in ws if x >= margem - 15 or x >= margem - 45 and
                  re.fullmatch(r'[—–«“"(]*[A-Za-zÀ-ÿ]{3,}[-A-Za-zÀ-ÿ]*[.,;:!?…»”")]*', w)]
            if not ws:
                continue
            t = ' '.join(w for _, w in ws)
            l = (l[0], ws[0][0], l[2], t, l[4])
        ws_ = t.split()
        if not (any(_PALAVRA.fullmatch(w) and sum(ch.isalpha() for ch in w) >= 3 for w in ws_) or
                ws_[0] in ('—', '–', '-') and len(ws_) <= 3 and any(_PALAVRA.fullmatch(w) for w in ws_[1:]) or
                len(ws_) <= 2 and any(re.fullmatch(r'[—–-]?[A-Za-zÀ-ÿ]{1,2}[.!?,;:…]+', w) for w in ws_)):
            continue                                          # sem palavra: lixo (a vinheta, sujeira)
        if not corpo and _e_cabeco(t):
            continue
        corpo.append((l[1], l[2], t))
    return corpo


def paginas_de(linhas, nome):
    """{página: (corpo [(x, y, texto)], margem, altura, linhas depois de vinheta)} das páginas de texto."""
    paginas = {}
    for l in linhas:
        paginas.setdefault(l[0], []).append(l)
    # o pé normal do texto (a mediana da última linha cheia): abaixo dele, a assinatura do caderno e a
    # sujeira da margem, que o OCR lê como linhas
    pes = sorted(max(l[2] for l in ls if sum(bool(_BOA.match(w)) for w in l[3].split()) >= 5)
                 for n, ls in paginas.items() if _pagina_util(nome, n)
                 and sum(1 for l in ls if sum(bool(_BOA.match(w)) for w in l[3].split()) >= 5) >= 10)
    pe = pes[len(pes) // 2] if pes else 10 ** 6
    out = {}
    for n in sorted(paginas):
        if not _pagina_util(nome, n):
            continue
        ls = paginas[n]
        cheias = [l[1] for l in ls if sum(bool(_BOA.match(w)) for w in l[3].split()) >= 5]
        if len(cheias) < 2:
            continue
        grupos = [x for x in sorted(cheias) if sum(1 for y in cheias if abs(y - x) <= 4) >= min(3, len(cheias))]
        margem = grupos[0] if grupos else min(cheias)
        alt = ls[0][4]
        ls = sorted((l for l in ls if l[2] <= pe + 60), key=lambda l: l[2])
        cab = next((i for i, l in enumerate(ls) if l[2] < alt * 0.22 and _e_cabeco(l[3])), None)
        if cab is not None:
            ls = ls[cab + 1:]                                     # o cabeço e o lixo acima dele
        # a vinheta entre as seções: linha curta (o OCR a lê como «Cm,», «Sa,», «e AME = a») bem
        # recuada, no meio da coluna; sai do texto, e a linha seguinte abre seção
        base = sorted(cheias)[len(cheias) // 2]                  # o começo típico das linhas cheias
        vinheta = lambda l: l[1] - base > 90 and sum(ch.isalpha() for ch in l[3]) <= 12 \
            and not l[3].strip().startswith(('—', '–', '-'))
        vys = [l[2] for l in ls if vinheta(l)]
        corpo = _limpar_corpo([l for l in ls if not vinheta(l)], margem)
        if corpo:
            depois = {next((i for i, c in enumerate(corpo) if c[1] > vy), None) for vy in vys} - {None}
            out[n] = (corpo, margem, alt, depois)
    return out


def aberturas(paginas):
    """Onde começam as seções: {(página, índice da linha)}. Mede-se a entrelinha de cada página (a
    mediana dos vãos) e o topo normal do texto (a mediana, entre as páginas, da primeira linha). Abre
    seção a linha depois de um vão de mais de 2,2 entrelinhas (a vinheta) e a primeira linha da página
    que começa mais de 2,2 entrelinhas abaixo do topo normal."""
    topos = sorted(c[0][1] for c, *_ in paginas.values())
    topo = topos[len(topos) // 2]
    abre = set()
    for n, (corpo, *_) in paginas.items():
        ys = [y for _, y, _ in corpo]
        vaos = sorted(b - a for a, b in zip(ys, ys[1:]))
        if not vaos:
            continue
        passo = vaos[len(vaos) // 2]
        if ys[0] - topo > 2.2 * passo:
            abre.add((n, 0))
        for i in range(1, len(ys)):
            if ys[i] - ys[i - 1] > 2.2 * passo:
                abre.add((n, i))
    return abre


REJEITADAS = {}             # nome do OCR -> vãos sem versalete (versos, sujeira): para conferir


def _versalete(t):
    """A linha começa em versalete? Letra maiúscula solta do resto («L evantei-me», «D. R o s») ou
    palavra toda em maiúsculas («ÊSTE MÊS», «— MARINA,», «No OUTRO dia») nas três primeiras palavras,
    ou a primeira com maiúsculas no meio («JuLiÃo»)."""
    t = re.sub(r'^[—–-]\S*\s*', '', t.strip())
    if re.match(r'(?:[A-ZÀ-Ú]\.\s*)?[A-ZÀ-Ú] [a-zà-úA-ZÀ-Ú]', t):
        return True
    ws = t.split()
    return bool(ws) and (any(re.fullmatch(r'[A-ZÀ-Ú]{2,}[,.;:!?]?', w) for w in ws[:3]) or
                         bool(re.search(r'[a-zà-ú][A-ZÀ-Ú]', ws[0])))      # «JuLiÃo»: versalete mal lido


def _versalete_forte(t):
    """Versalete sem vão antes (seção que começa no alto da página, a vinheta no pé da anterior):
    uma das duas primeiras palavras com três maiúsculas ou mais («ALGUNS DIAS», «DescoBrI»)."""
    ws = re.sub(r'^[—–-]\S*\s*', '', t.strip()).split()
    if len(ws) < 4:                                       # linha curta: sujeira da margem («ITeWY Já.»)
        return False
    return any(sum(ch.isupper() for ch in w) >= 3 and sum(ch.isalpha() for ch in w) >= 3 for w in ws[:2])


def obra_de_linhas(linhas, nome):
    """Linhas (pagina, x, y, texto, altura[, palavras]) -> obra em seções e parágrafos. Seção nova:
    a linha depois de um vão (aberturas()) que tem a vinheta ou cuja linha está em versalete, ou o
    parágrafo que abre em versalete forte (_versalete_forte: a seção no alto da página); os vãos sem
    versalete (os versos, que vêm entre espaços) ficam em REJEITADAS. Parágrafo novo: linha recuada (pela margem local, como em
    São Bernardo) ou abertura de seção."""
    paginas = paginas_de(linhas, nome)
    abre = aberturas(paginas)
    obra, par = [], ''
    SECOES[nome], REJEITADAS[nome] = [], []

    def fecha():
        nonlocal par
        if par and obra:
            obra[-1]['paras'].append(par)
        par = ''

    for n in sorted(paginas):
        corpo, margem, alt, vinhetas = paginas[n]
        rel = []
        for x, y, t in corpo:
            viz = [x2 for x2, y2, t2 in corpo if abs(y2 - y) <= 100 and not t2.startswith(('—', '–', '-'))]
            local = max(margem, min(viz)) if viz else margem
            # página de diálogo: todas as linhas vizinhas recuadas, e a margem local sobe até o recuo. O
            # travessão das falas marca o recuo: a margem fica ao menos 22 pontos à esquerda dele
            falas = [x2 for x2, y2, t2 in corpo if abs(y2 - y) <= 100 and t2.startswith(('—', '–'))]
            if falas:
                local = max(margem, min(local, min(falas) - 22))
            rel.append((x - local, y, t))
        for i, (recuo, y, t) in enumerate(rel):
            t = re.sub(r'\s{2,}', ' ', t)
            t = re.sub(r'(?<=\w)\s+[-–]$', '-', t)
            t = re.sub(r'^[|!\[\]{}]+\s*', '', t)
            if re.search(r'\w-$', par):
                t = re.sub(r'^\d\s+(?=[a-zà-ÿ])', '', t)
            secao = (n, i) in abre and (i in vinhetas or _versalete(t)) or recuo >= 18 and _versalete_forte(t)
            if (n, i) in abre and obra and not secao:
                REJEITADAS[nome].append((n, ' '.join(t.split()[:4])))
            if secao or not obra:
                fecha()
                obra.append({'n': str(len(obra) + 1), 'titulo': '', 'paras': []})
                SECOES[nome].append((n, ' '.join(t.split()[:4])))
                par = t
                continue
            fala = t.startswith(('—', '–')) and recuo >= 10
            # o hífen repetido no começo da linha («Sentia-» / «-me») não é travessão de fala
            continua = re.search(r'\w[-\xad]$', par) and re.match(r'[-–—]\s*[a-zà-ÿ]', t)
            novo = (recuo >= 18 or fala) and not continua
            if novo and par:
                fecha()
            if par.endswith('\xad'):
                par = par[:-1] + t
            elif continua:                                          # hífen repetido: «construí-» / «-lo»
                par = _juntar_hifen(par, re.sub(r'^[-–—]\s*', '', t), repetido=True)
            elif re.search(r'\w[-\xad]$', par):
                par = _juntar_hifen(par, t)
            elif re.search(r'[a-zà-ÿ]\.$', par) and re.match(r'[a-zà-ÿ]', t) and _hifen_lido_ponto(par, t):
                par = par[:-1] + t
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
    """Fim de linha hifenizado (ver São Bernardo): o hífen de verdade se repete no começo da linha
    seguinte («construí-» / «-lo»); a palavra junta, se existe, vence («con-» / «-tinuam»)."""
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
    """«ou.» / «tra»: o hífen do fim da linha lido como ponto. Depois de ponto a frase começa em
    maiúscula; se a linha seguinte começa em minúscula e a palavra junta existe (ou é um nome), junta-se."""
    ini = re.search(r'([A-Za-zÀ-ÿ]+)\.$', a).group(1)
    fim = re.match(r'([A-Za-zÀ-ÿ]+)', b).group(1)
    if ini.lower() in ABREVIATURAS:
        return False
    junta = ini + fim
    return grafia1990.atual_parte(junta)[1] != 'SEM_PAR' or junta.lower() in NOMES


def _corrigir_ocr(p):
    """Erros sistemáticos dos OCRs: «0» por «O», aspas lidas como duas simples, travessão dobrado. O
    «_» sai: o OCR não marca itálico, e os sublinhados à mão do exemplar de 1947 viram «_»; o itálico
    vem de decisoes.ITALICOS e VERSOS_ITALICOS, conferidos nas imagens."""
    p = fontes.limpar(p.replace('\xad', '').replace('_', ' '))
    p = re.sub(r'(?<=[a-zà-ÿ] )0(?=s? [a-zà-ÿ])', 'o', p)
    p = re.sub(r'(?<![\w,.])0(?=\.?s? [a-zà-ÿ])', 'O', p)
    p = p.replace('0.s ', 'Os ').replace('0s ', 'Os ')
    p = re.sub(r'(?<=[a-zà-ÿ] )(O|Os|A|As)(?= [a-zà-ÿ])', lambda m: m.group(1).lower(), p)
    p = re.sub(r'[‘\'] ?[‘\']', '“', p)
    p = re.sub(r'[’\'] ?[’\']', '”', p)
    p = re.sub(r'^[—–-]{2,}', '—', p)
    p = re.sub(r'(?<!\S)€(?!\S)', 'e', p).replace('€', 'e')
    p = re.sub(r'^[-–] ', '— ', p)
    p = re.sub(r'(?<=\w) [-–] ?[,.] ?(?=se\b|lhe\b|o\b|a\b)', '-', p)
    p = _parenteses(p)
    p = re.sub(r'(?:(?<=\s)|^)[\[\]{}]+(?=\s|$)', '', p)              # colchete solto: sujeira
    p = p.replace('/', ' ')                     # o livro não tem barra; para o montar, «/» separa versos
    return re.sub(r'[\^■*%=•|]', '', p).strip()


def _parenteses(p):
    """O vão largo depois do ponto, com alguma sujeira, sai como «(» («nomes. (Quando»): parêntese
    sem par no parágrafo é lixo."""
    abertos, fora = [], set()
    for m in re.finditer(r'[()]', p):
        if m.group(0) == '(':
            abertos.append(m.start())
        elif abertos:
            abertos.pop()
        else:
            fora.add(m.start())
    fora |= set(abertos)
    return ''.join(ch for k, ch in enumerate(p) if k not in fora).replace('  ', ' ')


# trocas comuns dos OCRs (o trema lido como «ii», o «q» como «g», «rn» por «m»...)
CONFUSOES = [('giii', 'qüi'), ('gii', 'qüi'), ('qii', 'qüi'), ('gjiii', 'qüi'), ('giú', 'qüi'), ('gii', 'qü'), ('qii', 'qü'), ('gi', 'qü'), ('qi', 'qü'), ('gú', 'qu'), ('ii', 'ü'), ('ii', 'u'),
             ('rn', 'm'), ('m', 'rn'), ('li', 'h'), ('h', 'li'), ('h', 'b'), ('b', 'h'), ('ri', 'n'), ('n', 'ri'),
             ('u', 'n'), ('n', 'u'), ('e', 'c'), ('c', 'e'), ('e', 'o'), ('o', 'e'), ('i', 'l'), ('l', 'i'),
             ('í', 'i'), ('i', 'í'), ('1', 'l'), ('l', 'I'), ('0', 'o'), ('6', 'ó'), ('ó', 'ô'), ('ô', 'ó'),
             ('é', 'ê'), ('ê', 'é'), ('à', 'â'), ('â', 'à'), ('t', 'f'), ('f', 't'), ('v', 'y'), ('y', 'v'),
             ('ii', 'ü'), ('tl', 'd'), ('cl', 'd'), ('d', 'cl'), ('in', 'm'), ('m', 'in'), ('ni', 'm'), ('1', 'i')]
CONSERTOS = []


def _palavras(obra):
    return {chave(w) for c in obra for p in c['paras'] for w in re.findall(r'[A-Za-zÀ-ÿ0-9]+', p)}


def consertar(obra, nomes=(), atestadas=()):
    """Palavra do OCR fora do léxico trocada pela única forma do léxico a uma troca da lista acima.
    Ficam os nomes próprios e as palavras atestadas (lidas igual em dois OCRs)."""
    lex_ok = lambda w: grafia1990.atual_parte(w)[1] == 'lexico'
    cache = {}

    def um(w):
        if w in cache:
            return cache[w]
        # «ii» não existe em português: é o trema mal lido, ainda que os dois OCRs o leiam (cinqiienta)
        atestada = chave(w) in atestadas and 'ii' not in w
        if not re.fullmatch(r'[A-Za-zÀ-ÿ0-9]+', w) or w.lower() in nomes or atestada or lex_ok(w) or len(w) < 3:
            cache[w] = w
            return w
        cands = set()
        for a, b in CONFUSOES:
            for m in re.finditer(re.escape(a), w):
                c = w[:m.start()] + b + w[m.end():]
                if lex_ok(c):
                    cands.add(c)
        # várias trocas que dão a mesma palavra de hoje (cinqiienta → cinqüenta ou cinquenta): a de 1947
        if len({grafia1990.atual(c)[0].lower() for c in cands}) == 1:
            cands = {max(cands, key=lambda c: (_marcas(c), c))}
        cache[w] = cands.pop() if len(cands) == 1 else w
        if cache[w] != w:
            CONSERTOS.append((w, cache[w]))
        return cache[w]

    def junta(p):                       # palavra partida pelo OCR: «sempr e», «desespe rada», «pren — dera»
        ws = p.split(' ')
        out = []
        k = 0
        while k < len(ws):
            a = ws[k]
            tra = k + 2 < len(ws) and ws[k + 1] in ('—', '–', '-')
            b = ws[k + 2] if tra else (ws[k + 1] if k + 1 < len(ws) else '')
            ma = re.fullmatch(r'([A-Za-zÀ-ÿ]{2,})', a)
            mb = re.fullmatch(r'([a-zà-ÿ]{1,12})([^A-Za-zÀ-ÿ]*)', b)
            junta_ = ma and mb and lex_ok(a + mb.group(1)) and a.lower() not in nomes and (
                not lex_ok(a) and (chave(a) not in atestadas or not lex_ok(mb.group(1)))
                or tra and not lex_ok(mb.group(1)))          # «conta - ria»: o hífen da linha, solto
            if junta_:
                CONSERTOS.append((' '.join(ws[k:k + (3 if tra else 2)]), a + b))
                out.append(a + b)
                k += 3 if tra else 2
                continue
            out.append(a)
            k += 1
        return ' '.join(out)

    def par(p):
        p = junta(p)
        return re.sub(r'[A-Za-zÀ-ÿ0-9]+', lambda m: um(m.group(0)), p)
    return [dict(c, paras=[par(p) for p in c['paras']]) for c in obra]


# as palavras em versalete de cada abertura, na caixa normal (conferidas nas imagens de 1947, na grafia
# de 1947): substituem no OCR o mesmo número de letras do começo da seção
VERSALETE = {
    '1': 'Levantei-me', '2': 'Se pudesse,', '3': 'Uma chuvinha', '4': 'Penso', '5': 'Seu Ivo,',
    '6': 'Êste mês', '7': 'A minha', '8': 'Em janeiro', '9': 'Ainda', '10': 'Foi', '11': '— Que diabo',
    '12': '— Boa tarde,', '13': 'Como era', '14': 'Defronte da', '15': '— Marina,', '16': 'No outro',
    '17': 'Alguns dias', '18': 'Marina', '19': 'Porque foi', '20': 'Pouco a pouco', '21': 'Aos domingos',
    '22': 'D. Rosália', '23': 'Há nas minhas', '24': 'À noite', '25': 'Quando', '26': 'O último dia',
    '27': 'Introduzi', '28': 'As visitas', '29': 'Algumas horas', '30': 'Alguns dias', '31': 'É estranho',
    '32': 'Seu Ivo', '33': 'Julião Tavares', '34': 'Nas horas', '35': 'Marina', '36': 'Descobri',
    '37': 'A casa', '38': 'Fui até', '39': '— Ó Vitória,', '40': 'A réstia',
}


def _letras(s):
    return re.sub(r'[^0-9a-zà-ÿ]', '', s.lower())


def versalete(obra):
    """Na abertura de seção as primeiras palavras vêm em versalete, que o OCR lê com a primeira letra
    solta, em maiúsculas ou misturado («L evantei - me», «DEFRONTE DA», «P ou co A POUCO»). Troca-se
    o começo da seção, até somar as letras da forma de VERSALETE, por ela."""
    out = []
    for c in obra:
        ps = list(c['paras'])
        v = VERSALETE.get(c['n'])
        if ps and v:
            alvo = len(_letras(v))
            ws = ps[0].split(' ')
            k, n = 0, 0
            while k < len(ws) and n < alvo:
                n += len(_letras(ws[k]))
                k += 1
            if alvo <= n <= alvo + 2:                        # o OCR às vezes dobra uma letra
                ps[0] = ' '.join([v] + ws[k:])
            else:
                print(f'versalete: seção {c["n"]}: {" ".join(ws[:k])!r} não bate com {v!r}')
        out.append(dict(c, paras=ps))
    return out


# ------------------------------------------------------------------ testemunhos

def _ocr(nome_pdf, leitor, guia=None):
    """OCR em seções e parágrafos; com guia, se as aberturas não baterem, as seções vêm do
    alinhamento com ela."""
    o = obra_de_linhas(leitor(nome_pdf), nome_pdf)
    if guia is not None and len(o) != len(guia):
        print(f'{nome_pdf}/{leitor.__name__}: {len(o)} seções achadas, {len(guia)} na guia; seções pelo alinhamento')
        o = capitulos_como(o, guia)
    return versalete(o)


def capitulos_como(obra, base):
    """Põe no OCR a divisão em seções da base (as quebras de parágrafo são as do OCR)."""
    T2, quebras = [], set()
    for t in achatar(obra, com_titulos=False):
        if t == '¶':
            quebras.add(len(T2))
        else:
            T2.append(t)
    B = achatar(base)
    B2, marcas, i = [], [], 0
    while i < len(B):
        if B[i].startswith('#'):
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


def acentos(t47, b47, testemunhos46):
    """Onde os dois OCRs de 1947 leem a mesma palavra com acentos diferentes (ver São Bernardo):
    palavra curta, votam as quatro leituras (as duas de 1947 e as duas das provas); palavra longa, a
    forma que existe hoje, ou a acentuada. Empates e dúvidas vão para a conferência (ACENTOS)."""
    T, B = achatar(t47), achatar(b47)

    def mapa(outro):
        O = achatar(outro)
        m = {}
        for tp, i1, i2, j1, j2 in alinhar(T, O, chave=chave):
            if tp == 'equal':
                m.update({i1 + k: O[j1 + k] for k in range(i2 - i1)})
        return m
    par = mapa(b47)
    m46 = [mapa(o) for o in testemunhos46]
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
            for m in m46:
                w = m.get(i)
                w = w.lower() if w else None
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
            else:
                esc = t
        if esc != t:
            novo[i] = igualar_caixa(t, esc)
        ACENTOS.append((t, b, novo[i], duvida, junta_(T[max(0, i - 6):i + 6])))
    return fontes.normalizar(ocr.obra_de_tokens(novo))


PARAGRAFOS = []             # (o que mudou, contexto): quebras de parágrafo do t47 mudadas pelo voto


def paragrafos_por_voto(base, outros):
    """As quebras de parágrafo da base (t47) por voto com os outros OCRs (b47, t46, b46): antes de
    cada palavra, cada testemunho diz se ali começa parágrafo. Muda-se a base quando os outros três
    concordam entre si contra ela (onde o testemunho tem a palavra alinhada)."""
    B = achatar(base)
    pal = [i for i, t in enumerate(B) if e_palavra(t)]

    def comeca(T, i):
        """Há ¶ entre a palavra anterior e a de índice i?"""
        k = i - 1
        while k >= 0 and not e_palavra(T[k]) and not T[k].startswith('#'):
            if T[k] == '¶':
                return True
            k -= 1
        return k >= 0 and T[k].startswith('#')
    votos = []
    for o in outros:
        O = achatar(o)
        op = [j for j, t in enumerate(O) if e_palavra(t)]
        m = {}
        for tp, i1, i2, j1, j2 in alinhar([chave(B[i]) for i in pal], [chave(O[j]) for j in op]):
            if tp == 'equal':
                for k in range(i2 - i1):
                    m[i1 + k] = comeca(O, op[j1 + k])
        votos.append(m)
    novo, k = [], 0
    for idx, i in enumerate(pal + [len(B)]):
        trecho = B[k:i]
        if idx < len(pal):
            vs = [v[idx] for v in votos if idx in v]
            atual = comeca(B, i)
            if len(vs) == len(outros) and len(set(vs)) == 1 and vs[0] != atual and not any(t.startswith('#') for t in trecho):
                if vs[0]:                                   # falta ¶: antes do travessão, se houver
                    j = len(trecho)
                    while j > 0 and trecho[j - 1] in ('—', '–', '-', '«', '“', '"'):
                        j -= 1
                    trecho = trecho[:j] + ['¶'] + trecho[j:]
                else:
                    trecho = [t for t in trecho if t != '¶']
                PARAGRAFOS.append(('+¶' if vs[0] else '-¶', junta_(B[max(0, i - 6):i + 6])))
        novo += trecho
        if idx < len(pal):
            novo.append(B[i])
        k = i + 1
    return fontes.normalizar(ocr.obra_de_tokens(novo))


def junta_(ts):
    from edicao.tokens import texto
    return texto([t for t in ts if t != '¶' and not t.startswith('#')])


# o que vai em itálico em 1947 (achado pela inclinação das letras, italico.py, e conferido nas imagens)
ITALICOS = []


def italicos(obra):
    if not ITALICOS:
        return obra
    rx = re.compile(r'(?<![\w_])(' + '|'.join(ITALICOS) + r')(?![\w_])')
    return [dict(c, paras=[rx.sub(r'_\1_', p) for p in c['paras']]) for c in obra]


NOMES = set()


def _nomes_de(obras):
    """Nomes próprios: palavras em maiúscula no meio da frase, em todos os OCRs dados."""
    conj = None
    for obra in obras:
        T = achatar(obra)
        s = {b.lower() for a, b in zip(T, T[1:]) if e_palavra(b) and b[:1].isupper() and e_palavra(a)}
        conj = s if conj is None else conj & s
    return {re.sub(r'\W', '', w) for w in conj or ()}


def transcricoes():
    global SITIOS46, P46
    if os.path.exists(fontes.cache(OBRA, 'testemunhos46.pkl')):      # os nomes da rodada anterior (hífens)
        _nomes()
    t47 = _ocr(PDF47, _linhas_tess)
    b47 = _ocr(PDF47, _linhas_bbm, t47)
    t46 = _ocr(PDF46, _linhas_tess, t47)
    b46 = _ocr(PDF46, _linhas_bbm, t47)
    NOMES.clear()
    NOMES.update(_nomes_de([t47, b47]) | _nomes_de([t46, b46]) | _nomes_de([t47, t46]))
    todas = [_palavras(o) for o in (t47, b47, t46, b46)]
    atest = {w for w in set().union(*todas) if sum(w in s for s in todas) >= 2}
    t47, b47, t46, b46 = (consertar(o, NOMES, atest) for o in (t47, b47, t46, b46))
    E46, SITIOS46 = estabelecer.estabelecer({'t46': t46, 'b46': b46}, 't46', {'t47': t47, 'b47': b47})
    P46 = fontes.normalizar(ocr.obra_de_tokens(E46))
    t47 = paragrafos_por_voto(t47, (b47, t46, b46))
    t47 = italicos(acentos(t47, b47, (t46, b46)))
    pickle.dump({'t46': t46, 'b46': b46, 'sitios46': SITIOS46, 'p46': P46, 'acentos': ACENTOS,
                 'nomes': NOMES, 'secoes': SECOES, 'consertos': CONSERTOS, 'paragrafos': PARAGRAFOS},
                open(fontes.cache(OBRA, 'testemunhos46.pkl'), 'wb'))
    return {'t47': t47, 'b47': b47}


def modernas():
    return {'p46': P46}


DUVIDAS = []


def _nomes():
    if not NOMES:
        NOMES.update(pickle.load(open(fontes.cache(OBRA, 'testemunhos46.pkl'), 'rb'))['nomes'])
    return NOMES


def rever(tr, md, sitios):
    """Desempate dos dois OCRs de 1947 onde nenhum coincide com as provas (p46): vence a leitura com
    menos palavras fora do léxico; empate, a mais parecida com as provas. Se as duas têm palavras
    desconhecidas e as provas não, valem as provas, marcado para conferir. Devolve (E, sítios)."""
    from edicao.tokens import texto as junta
    nomes = _nomes()

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
        m = _toks(x['modernas']['p46'])
        # vírgula × ponto (o Tesseract lê muito ponto como vírgula): decide a palavra seguinte; em
        # maiúscula, e não nome próprio, é ponto
        if sorted(tuple(v) for v in T.values()) == [(',',), ('.',)]:
            seg = next((t for t in B[x['e']:x['e'] + 3] if t not in ('¶', '—', '«', '“', '"')), '')
            ponto = e_palavra(seg) and seg[:1].isupper() and seg.lower() not in nomes or seg in ('¶',)
            x['escolha'], x['por'] = ['.'] if ponto else [','], 'vírgula × ponto'
            x['escolha_txt'] = junta(x['escolha'])
            continue
        nm = sum(1 for t in m if e_palavra(t))
        falta = lambda ts: abs(sum(1 for t in ts if e_palavra(t)) - nm)     # linha que o OCR perdeu
        cand = sorted(T, key=lambda n: (desconhecidas(T[n]) + falta(T[n]), -parecido(T[n], m), n != BASE))
        esc = cand[0]
        d = {n: desconhecidas(T[n]) for n in T}
        palavras = lambda ts: [chave(t) for t in ts if e_palavra(t)]
        sinais = lambda ts: [t for t in ts if not e_palavra(t) and t != '¶']
        if len({tuple(palavras(v)) for v in list(T.values()) + [m]}) == 1:
            dist = lambda n: SequenceMatcher(None, sinais(T[n]), sinais(m)).ratio()
            esc = max(T, key=lambda n: (dist(n), n == BASE))
            x['escolha'], x['por'] = T[esc], f'pontuação; {esc}'
            x['escolha_txt'] = junta(x['escolha'])
            DUVIDAS.append(x)
            continue
        if all(v > 0 for v in d.values()) and desconhecidas(m) == 0 and max(parecido(T[n], m) for n in T) >= 0.6:
            x['escolha'], x['por'] = m, 'p46 (os dois OCRs com palavras desconhecidas)'
        else:
            x['escolha'], x['por'] = T[esc], f'léxico; {esc}'
        x['escolha_txt'] = junta(x['escolha'])
        if d[esc] == 0 and sum(1 for v in d.values() if v == 0) > 1 or x['por'].startswith('p46'):
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


def modernizar(E, manual):
    """Grafia de 1947 (Formulário de 1943) -> Acordo de 1990, palavra por palavra (grafia1990.py)."""
    return grafia1990.modernizar(E, manual)
