"""Vidas Secas — fontes.

Edições em vida do autor (todas José Olympio): 1ª, 1938; 2ª, 1947; 3ª, 1952. A 2ª é a última
revista pelo autor que se pode ler em fac-símile (Brasiliana USP, bbm/8480); a 3ª não está
digitalizada. Edição-base: a de 1947.

Testemunhos (o esquema de Brás Cubas: transcrição limpa de outra edição + OCR da edição-base):
- 'ws38': a 1ª edição (1938) no Wikisource, página a página, toda validada. É o fluxo-base do
  confronto, porque é a única transcrição inteira e revista; as mudanças de 1947 entram por
  cima dela.
- 'ws47': a 2ª edição no Wikisource, só nas páginas revisadas (capítulos 1 a 3); nos outros
  capítulos é lacuna e não vota. Os parágrafos dele são os do OCR (o transcritor juntou vários).
- 'ocr47': a camada de texto (OCR) do fac-símile de 1947, em parágrafos pelo recuo da primeira
  linha, dividida em capítulos pelo alinhamento com 1938 e limpa do ruído com a ajuda das
  transcrições (ocr.limpar só troca palavras que não existem).
Moderna: 'cps', a edição digital gratuita de 2024 (distribuída pelo Centro Paula Souza), já no
Acordo de 1990. Segue as lições de 1947 (aió, de uma, toicinho...), que chegam a ela pelas
edições da Record, feitas sobre a 2ª edição. Onde 1938 e o OCR de 1947 divergem, ela desempata;
onde só ela diverge, não conta. É também a referência para a grafia.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes  # noqa: E402
from edicao import ocr  # noqa: E402
from edicao.grafia import chave, sem_acento  # noqa: E402
from edicao.tokens import LACUNA, _mapeador, achatar, alinhar, e_palavra  # noqa: E402

OBRA = 'vidas-secas'

META = {
    'id': OBRA,
    'autor': 'graciliano-ramos',
    'titulo': 'Vidas Secas',
    'ano': 1938,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1938, o último de Graciliano Ramos.',
}

TROCAS_OCR = []          # o que limpar_ocr trocou no OCR (para conferência)

BASE = 'ws38'
RUIDOSO = 'ocr47'
REFERENCIAS = [('cps', True)]

CAPITULOS = ['Mudança', 'Fabiano', 'Cadeia', 'Sinha Vitória', 'O menino mais novo', 'O menino mais velho',
             'Inverno', 'Festa', 'Baleia', 'Contas', 'O soldado amarelo', 'O mundo coberto de penas', 'Fuga']

# (arquivo, primeira e última página do corpo, páginas a saltar): na digitalização de 1938, a folha de
# rosto interna e a lista «Do autor» (pp. 9–10) ficaram entre o título do 1º capítulo e o texto.
WS38 = ('Vidas seccas.pdf', 7, 201, {9, 10})
WS47 = ('Vidas Sêcas 2nd edition.pdf', 7, 196, set())
PDF47 = 'https://digital.bbm.usp.br/bitstream/bbm/8480/1/45000022931_Output.o.pdf'
PDF_CPS = 'https://bkpsitecpsnew.blob.core.windows.net/uploadsitecps/sites/255/2025/04/vidas-secas.pdf'


def _modelos(t):
    """Modelos do Wikisource usados nestas duas transcrições."""
    t = re.sub(r'<noinclude>.*?</noinclude>', '', t, flags=re.S)
    t = t.replace('{{--}}', '—')
    t = re.sub(r'\{\{nop\}\}', '\n\n', t)
    t = re.sub(r'\{\{Capitular\|([^{}|]*)\}\}', r'\1', t)
    for _ in range(4):
        t = re.sub(r'\{\{(?:sic|SIC)\|([^{}|]*)(?:\|[^{}]*)?\}\}', r'\1', t)      # o impresso é o 1º argumento
        t = re.sub(r'\{\{(?:sc|Sc|Uc|serifa|smaller|x-smaller|fine|larger|big|left|d1|cursivo2)\|([^{}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:lsp|letter-spacing)\|[^{}|]*\|([^{}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{cor\|[^{}|]*\|([^{}]*)\}\}', r'\1', t)
    t = re.sub(r'\xad\s*', '', t)                                # hífen de divisão silábica
    t = re.sub(r"'''?([^'\n]+?)'''?", r'_\1_', t)                # o «chapchap» de 1938 vem em negrito
    t = re.sub(r'\bE’(?= )', 'É', t)                             # 1938 compõe o É e o À maiúsculos
    t = re.sub(r'\bA’(?=\w| )', 'À', t)                          # como E’ e A’ (A’s vezes, A’quella)
    t = re.sub(r'<p>\s*</p>', '\n\n', t)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    return t


def _titulo(pagina):
    """Texto de uma página de abertura de capítulo: só o título, dentro de modelos de formatação."""
    t = re.sub(r'<noinclude>.*?</noinclude>', '', pagina, flags=re.S)
    for _ in range(6):
        t = re.sub(r'\{\{[^{}|]*\|(?:[^{}|]*\|)*([^{}|=]*)(?:\|[^{}|]*=[^{}|]*)*\}\}', r'\1', t)
    t = re.sub(r'<[^>]+>', ' ', t).strip()
    return t if t and '\n' not in t else None


def _chave_titulo(s):
    s = sem_acento(fontes.nfc(s)).lower()
    return re.sub(r'\W', '', s).replace('ct', 't').replace('ll', 'l').replace('nn', 'n')


def wikisource(sub, arquivo, primeira, ultima, saltar=(), so_revisadas=False):
    """Texto corrido das páginas, partido nos 13 capítulos pelos títulos (que casam com CAPITULOS)."""
    pags = fontes.wikisource_paginas(f'{OBRA}/{sub}', arquivo, 1, ultima + 10)
    chaves = {_chave_titulo(c): c for c in CAPITULOS}
    obra, atual, corpo = [], None, ''

    def fecha():
        nonlocal corpo
        if atual is not None:
            t = re.sub(r'(\w)-\n(\w)', r'\1\2', corpo)          # palavra hifenizada no fim da linha
            for b in re.split(r'\n\s*\n', t):
                b = fontes.limpar(b.replace('\n', ' '))
                if b and not re.fullmatch(r'[\d\W]*', b):
                    atual['paras'].append(b)
        corpo = ''

    for n in range(primeira, ultima + 1):
        v = pags.get(n)
        if n in saltar or not v or not v['qualidade'] or (so_revisadas and v['qualidade'] < 3):
            continue
        cru = v['texto']
        t = _modelos(cru)
        tit = _titulo(cru)
        if tit is not None and _chave_titulo(tit) in chaves:
            fecha()
            atual = {'n': '', 'titulo': chaves[_chave_titulo(tit)], 'paras': []}
            obra.append(atual)
            continue
        if atual is None:
            continue
        t = t.strip('\n')
        if re.search(r'\w-$', corpo.rstrip()):
            corpo = corpo.rstrip()[:-1] + t.lstrip()
        elif cru.split('</noinclude>', 1)[-1].startswith(('\n\n', '<p>')):
            corpo += '\n\n' + t
        else:
            corpo += '\n' + t
    fecha()
    return fontes.normalizar(obra)


def _linhas_ocr47():
    """Linhas do OCR de 1947 (pdftotext -bbox-layout), na ordem da página, cada uma com o recuo
    (em pontos) em relação à margem do texto; sem cabeços, números de página nem o lixo da
    margem interna (sombras da encadernação que o OCR lê como letras)."""
    import html
    pdf = fontes.cache(OBRA, 'bbm47.pdf')
    xml = fontes.cache(OBRA, 'bbm47-bbox.html')
    if not os.path.exists(xml):
        fontes.pdf_texto(OBRA, PDF47, 'bbm47')                     # baixa o PDF
        subprocess.run(['pdftotext', '-bbox-layout', '-enc', 'UTF-8', pdf, xml], check=True)
    s = open(xml, encoding='utf-8').read()
    cabeco = re.compile(r'^(?:[ÒO0]BRAS DE GRAC.*|VIDAS S[EÊ]CAS|\[ ?\d+ ?\]|\d+)$')
    out = []
    for k, pag in enumerate(re.findall(r'<page [^>]*>(.*?)</page>', s, re.S), 1):
        linhas = []
        for l in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>(.*?)</line>', pag, re.S):
            ws = [(float(x), html.unescape(w)) for x, w in re.findall(r'<word xMin="([\d.]+)"[^>]*>([^<]*)</word>', l.group(3))]
            if ws:
                linhas.append((float(l.group(2)), ws))
        boa = re.compile(r'^[A-Za-zÀ-ÿ]{2,}[,.;:!?]?$')
        cheias = [ws[0][0] for _, ws in linhas if sum(bool(boa.match(w)) for _, w in ws) >= 5]
        if not cheias:
            continue
        margem = sorted(cheias)[len(cheias) // 2] - 3             # a margem esquerda do texto
        juntas = []                                               # pedaços da mesma linha (justificação larga)
        for y, ws in sorted(linhas, key=lambda x: x[0]):
            if juntas and abs(y - juntas[-1][0]) < 4:
                juntas[-1] = (juntas[-1][0], sorted(juntas[-1][1] + ws))
            else:
                juntas.append((y, ws))
        texto = []
        for y, ws in juntas:
            ws = [(x, w) for x, w in ws if x >= margem - 12]       # sem o lixo da margem interna
            if not ws:
                continue
            l = ' '.join(w for _, w in ws)
            junto = re.sub(r'\s', '', l).upper()
            if (cabeco.match(re.sub(r'\s+', ' ', l)) or junto in ('OBRASDEGRACILIANORAMOS', 'VIDASSÊCAS', 'VIDASSECAS')
                    or (y < 80 and re.fullmatch(r'[A-ZÀ-Ü ]+', l))):
                continue
            texto.append((k, ws[0][0] - margem, l))
        out += texto
    return out


def ocr47(primeira=9, ultima=195):
    """OCR do fac-símile de 1947 em parágrafos (linha recuada abre parágrafo), num bloco só: a
    divisão em capítulos vem depois, por alinhamento com a 1ª edição (segunda.capitulos_como)."""
    paras, par = [], ''
    for k, recuo, l in _linhas_ocr47():
        if not primeira <= k <= ultima or sum(ch.isalpha() for ch in l) < 2 or recuo > 100:
            continue
        l = re.sub(r'\s{2,}', ' ', l)
        if recuo >= 25 and par:
            paras.append(par); par = ''
        if par.endswith('\xad'):
            par = par[:-1] + l
        elif re.search(r'\w-$', par) and l.startswith('-'):            # gritou- / -lhe
            par = par + l[1:]
        elif re.search(r'\w-$', par):
            par = fontes._juntar_hifen(par, l)                           # deitou- / se; ou pala- / vra
        else:
            par = (par + ' ' + l).strip()
    if par:
        paras.append(par)
    juntos = []                                 # parágrafo que começa em minúscula continua o anterior
    for p in paras:                             # (a capitular dos inícios de capítulo desloca a 1ª linha)
        if juntos and re.match(r'[a-zà-ÿ]', p) and not re.search(r'[.!?…]$', juntos[-1]):
            juntos[-1] += ' ' + p
        else:
            juntos.append(p)
    return fontes.normalizar([{'n': '', 'titulo': '', 'paras': [_corrigir_ocr(p) for p in juntos]}])


def _corrigir_ocr(p):
    """Erros sistemáticos deste OCR: «0» por «O», aspas curvas lidas como duas simples."""
    p = fontes.limpar(p.replace('\xad', ''))
    p = re.sub(r'(?<![\w,.])0(?=\.?s? [a-zà-ÿ])', 'O', p)
    p = p.replace('0.s ', 'Os ').replace('0s ', 'Os ')
    p = re.sub(r'[‘\'] ?[‘\']', '“', p)
    p = re.sub(r'[’\'] ?[’\']', '”', p)
    p = re.sub(r'(?<=\w) [-–] ?[,.] ?(?=se\b|lhe\b|o\b|a\b)', '-', p)         # acocorou -, se
    return re.sub(r'[\^■*%=•]', '', p).strip()


def capitulos_como(obra, base):
    """Põe no OCR (um bloco só, com os parágrafos dele) a divisão em capítulos da base."""
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
    return ocr.obra_de_tokens(out)


def _dist(a, b):
    return ocr._dist(a, b)


def limpar_ocr(obra, guias, lexico):
    """Como ocr.limpar, mas alinhando só as palavras (o OCR põe parágrafos e pontuação a mais, que
    desfazem os blocos de uma palavra por uma). Troca só palavras que não existem por uma parecida,
    alinhada no mesmo ponto, da primeira guia que a tiver; junta palavra partida pelo OCR. Devolve
    (obra, trocas), trocas = [(do OCR, para, guia)]."""
    T = achatar(obra)
    idx = [i for i, t in enumerate(T) if e_palavra(t)]
    W = [T[i] for i in idx]
    lex = {chave(w) for w in lexico} | {chave(w) for _, g in guias for w in achatar(g) if e_palavra(w)}
    trocas, reg = {}, []
    for nome, g in guias:
        G = [t for t in achatar(g) if e_palavra(t)]
        for tp, i1, i2, j1, j2 in alinhar(W, G, chave=chave):
            if tp != 'replace':
                continue
            if i2 - i1 == j2 - j1:
                for k in range(i2 - i1):
                    o, n = W[i1 + k], G[j1 + k]
                    ko = chave(o)
                    if i1 + k in trocas or ko in lex or _dist(ko, chave(n)) > ocr._limite(ko):
                        continue
                    trocas[i1 + k] = (idx[i1 + k], idx[i1 + k], n)
                    reg.append((o, n, nome))
            for k in range(i1, i2 - 1):                 # palavra partida: «li vrou-se», «acocorou se»
                a, b = W[k], W[k + 1]
                if k in trocas or k + 1 in trocas or (chave(a) in lex and chave(b) in lex):
                    continue
                for n in G[j1:j2]:
                    if chave(n).replace('-', '') == chave(a + b).replace('-', ''):
                        trocas[k] = (idx[k], idx[k + 1], n)
                        trocas[k + 1] = None
                        reg.append((a + ' ' + b, n, nome))
                        break
    novo, i = [], 0
    por_inicio = {v[0]: v for v in trocas.values() if v}
    while i < len(T):
        if i in por_inicio:
            a, b, n = por_inicio[i]
            novo.append(n)
            i = b + 1
            continue
        novo.append(T[i])
        i += 1
    return ocr.obra_de_tokens(novo), reg


def com_lacunas(parcial, base):
    """Os 13 capítulos, com lacuna (não vota) nos que a transcrição parcial não tem."""
    tem = {p['titulo']: p for p in parcial}
    return [tem.get(p['titulo']) or {'n': '', 'titulo': p['titulo'], 'paras': [LACUNA]} for p in base]


def transcricoes():
    ws38 = wikisource('ws38', *WS38)
    cps = modernas()['cps']
    lexico = [t for t in achatar(cps) if e_palavra(t)]
    o = capitulos_como(ocr47(), ws38)
    ws47 = wikisource('ws47', *WS47, so_revisadas=True)
    o, trocas = limpar_ocr(o, [('ws47', ws47), ('cps', cps), ('ws38', ws38)], lexico)
    o = fontes.normalizar(o)
    global TROCAS_OCR
    TROCAS_OCR = trocas
    feitos = [p['titulo'] for p in ws47]
    ws47 = ocr.paragrafos_como(ws47, [p for p in o if p['titulo'] in feitos])
    return {'ws38': ws38, 'ws47': fontes.normalizar(com_lacunas(ws47, ws38)), 'ocr47': o}


def _juntar_moderna(a, b, corpo):
    """Junta o fim de linha hifenizado da edição moderna: «Fabia-» + «no» é Fabiano, não Fabia-no
    (vale a forma que aparece inteira noutro ponto do texto); sem isso, a regra dos pronomes."""
    if b.startswith('-'):                                        # enjoou- / -os
        return a + b[1:]
    m = re.match(r"[\w']+", b)
    resto = m.group(0) if m else ''
    ultimo = re.search(r'(\w+)-$', a).group(1)
    if re.search(r'(?<![\w-])' + re.escape(ultimo + resto) + r'(?![\w-])', corpo):
        return a[:-1] + b
    if re.search(r'(?<![\w-])' + re.escape(ultimo + '-' + resto) + r'(?![\w-])', corpo):
        return a + b
    return fontes._juntar_hifen(a, b)


def modernas():
    """A edição moderna em parágrafos pelo recuo (pdftotext -layout); o «Depoimento» do autor,
    que ela traz antes do texto, fica de fora."""
    pdf = fontes.cache(OBRA, 'cps.pdf')
    txt = fontes.cache(OBRA, 'cps-layout.txt')
    if not os.path.exists(txt):
        fontes.pdf_texto(OBRA, PDF_CPS, 'cps')
        subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, txt], check=True)
    titulos = {sem_acento(c).upper(): c for c in CAPITULOS}
    titulos['SINHA VITORIA'] = 'Sinha Vitória'
    obra, atual, par, capitular = [], None, '', ''
    palavras_cps = open(txt, encoding='utf-8').read() + '\n'.join(   # e as palavras de 1938, para os hífens
        x for parte in wikisource('ws38', *WS38) for x in parte['paras'])

    def fecha():
        nonlocal par
        if par and atual is not None:
            atual['paras'].append(fontes.limpar(par))
        par = ''

    linhas = []                                          # (recuo em relação à margem da página, linha)
    for pag in open(txt, encoding='utf-8').read().split('\f'):
        ls = [l.rstrip() for l in pag.split('\n') if l.strip() and not re.fullmatch(r'\s*(\d+|Distribuição Gratuita)\s*', l)]
        cheias = [len(l) - len(l.lstrip()) for l in ls if len(l.strip()) > 45]
        margem = min(cheias) if cheias else 0
        linhas += [(len(l) - len(l.lstrip()) - margem, l.strip()) for l in ls]
    k = 0
    while k < len(linhas):
        recuo, tl = linhas[k]
        k += 1
        if tl == 'O MUNDO COBERTO' and k < len(linhas):          # título em duas linhas
            tl += ' ' + linhas[k][1]
            k += 1
        if sem_acento(tl) in titulos:
            fecha()
            atual = {'n': '', 'titulo': titulos[sem_acento(tl)], 'paras': []}
            obra.append(atual)
            continue
        if atual is None:
            continue
        if re.fullmatch(r'[A-ZÀ-Ü]', tl):                  # letra capitular, solta numa linha
            fecha()
            capitular = tl
            continue
        if capitular:                                    # «N» + «a planície»; «A» + «família»
            primeira = tl.split()[0]
            junta = capitular + primeira
            par = (junta + tl[len(primeira):]) if re.search(r'(?<!\w)' + junta + r'\b', palavras_cps) else capitular + ' ' + tl
            capitular = ''
            continue
        if 3 <= recuo <= 6 and par:
            fecha()
            par = tl
        elif re.search(r'\w-$', par):
            par = _juntar_moderna(par, tl, palavras_cps)
        else:
            par = (par + ' ' + tl).strip()
    fecha()
    return {'cps': fontes.normalizar(obra)}
