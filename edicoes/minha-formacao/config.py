"""Minha Formação — fontes.

Edição-base: a 1ª edição em livro (Rio de Janeiro e Paris, H. Garnier, 1900), a única em vida do
autor (morto em 1910). A maior parte saíra antes no Commercio de S. Paulo (1895) e na Revista
Brazileira (1895–99), e o prefácio diz que na revisão para o livro «foram feitas emendas e
variantes». Três leituras dessa edição, de dois exemplares:
  pg  Projeto Gutenberg nº 76030 (2025), transcrição humana (Distributed Proofreaders) sobre as
      imagens do exemplar de Toronto (Robarts Library) no Internet Archive (minhaformao00nabuuoft);
  ia  OCR do mesmo exemplar de Toronto (ABBYY, camada _djvu.xml do Internet Archive);
  hv  OCR do exemplar de Harvard (digitalização do Google pela HathiTrust, hvd.hwt4ru), camada de
      texto do DjVu do Wikimedia Commons (djvutxt página a página; cache harvard.txt).
Os dois OCRs são de programas e de exemplares diferentes: valem um voto cada. Recebem a divisão
(capítulos, parágrafos) do Gutenberg (ocr.estrutura_como) e são limpos pelas guias (ocr.limpar).
As notas de rodapé do autor (quatro) saem do fluxo e voltam no fim do capítulo (arrumar; texto em
notas-autor.txt, conferido no fac-símile).
Edições modernas (só para a grafia e o desempate; não são texto):
  ws    o texto moderno que um robô (Giro bot) pôs nas páginas do Wikisource sobre o DjVu de Harvard
        (304 das 338 páginas, «não revistas»; ortografia de 1971, com idéia, conseqüência);
  ob    as Obras Completas, vol. 1 (Instituto Progresso Editorial, São Paulo, 1949), PDF da Brasiliana
        USP (bbm/4743), ortografia de 1943 (êle, idéia).
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402
from edicao.grafia import chave  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'minha-formacao'

META = {
    'id': OBRA,
    'autor': 'joaquim-nabuco',
    'titulo': 'Minha Formação',
    'ano': 1900,
    'genero': 'Autobiografia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Memórias da formação política e intelectual do autor, publicadas em jornal e revista de 1895 '
                 'a 1899 e reunidas em livro em 1900.',
}

BASE = 'pg'
REFERENCIAS = [('ws', False), ('ob', False)]
DESEMPATE_LEXICO = True

ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
       'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI']
PREFACIO = 'Prefácio'
# títulos na grafia de hoje, como no corpo do livro de 1900 (que os compõe em maiúsculas; a caixa
# segue o índice do próprio livro)
TITULOS = {
    'I': 'Colégio e Academia', 'II': 'Bagehot', 'III': '1871-1873. A _Reforma_', 'IV': 'Atração do mundo',
    'V': 'Primeira viagem à Europa', 'VI': 'A França de 1873-74', 'VII': 'Ernest Renan', 'VIII': 'A crise poética',
    'IX': 'Adido de legação', 'X': 'Londres', 'XI': '_32, Grosvenor Gardens_', 'XII': 'Influência inglesa',
    'XIII': 'O espírito inglês', 'XIV': 'Nova York (1876-77)', 'XV': 'O meu diário de 1877',
    'XVI': 'Traços americanos', 'XVII': 'Influência dos Estados Unidos', 'XVIII': 'Meu pai',
    'XIX': 'Eleição de deputado', 'XX': 'Massangana', 'XXI': 'A abolição',
    'XXII': 'Caráter do movimento. A parte da dinastia', 'XXIII': 'Passagem pela política', 'XXIV': 'No Vaticano',
    'XXV': 'O barão de Tautphoeus', 'XXVI': 'Os últimos dez anos (1889-1899)',
}

NOTA = re.compile(r'^\[(\d)\] ')


# ------------------------------------------------------------------ Gutenberg

def _pg_bruto():
    s = open(fontes.cache(OBRA, 'pg76030.txt'), encoding='utf-8').read().replace('\r', '')
    s = s.split('*** START OF THE PROJECT GUTENBERG EBOOK', 1)[1].split('\n', 1)[1]
    s = s.split('*** END OF THE PROJECT GUTENBERG EBOOK')[0]
    s = s[s.index('                               PREFACIO\n'):]
    s = s[:s.index('\n                                  FIM\n')]
    s = s.replace('--', '—')
    return fontes.nfc(s)


def separadores():
    """As linhas de asteriscos do livro (separação de seções dentro do capítulo): as primeiras
    palavras do parágrafo que cada uma abre. O fluxo descarta os asteriscos; arrumar() os repõe."""
    blocos = [b.strip() for b in re.split(r'\n\s*\n', _pg_bruto())]
    out = []
    for k, b in enumerate(blocos):
        if re.fullmatch(r'[*\s]+', b) and k + 1 < len(blocos):
            out.append(' '.join(blocos[k + 1].split()[:5]))
    return out


def gutenberg():
    s = _pg_bruto()
    s = s.replace('\n                            MINHA FORMAÇÃO\n', '\n')
    blocos, notas = [], []
    for b in re.split(r'\n\s*\n', s):
        if NOTA.match(b.strip()):
            notas.append(b.strip())
            continue
        b = re.sub(r'\[\d\]', '', b)
        if re.fullmatch(r'[*\s]+', b.strip()):
            continue
        blocos.append(b)
    obra = fontes.partir_por_cabecalhos(blocos, [r'^(?P<n>[IVXL]+)$', r'^(?P<t>PREFACIO)$'])
    obra = fontes.normalizar(obra)
    nums = [p['n'] for p in obra if p['n']]
    if nums != ROM or obra[0]['titulo'] != 'PREFACIO' or len(notas) != 4:
        raise SystemExit(f'pg: {nums} {obra[0]["titulo"]} {len(notas)} notas')
    obra[0]['titulo'] = PREFACIO
    for p in obra[1:]:
        p['titulo'] = TITULOS[p['n']]
    return obra


# ------------------------------------------------------------------ OCRs

CABECO = re.compile(r'^[—–\-~_.\s]*[\dIVXLlio]{1,4}[—–\-~_.\s]*$|^[—–\-]+$')
# cabeços e títulos do livro (MINHA FORMAÇÃO, PREFACIO, os títulos dos capítulos): linhas sem minúsculas
TITULO_OCR = re.compile(r'^[^a-zà-ÿ]*[A-ZÀ-Ú]{2}[^a-zà-ÿ]*$')
_NOTAS_PAL = None
# marcas d'água do Google no exemplar de Harvard
LIXO = re.compile(r'^(Digitized by|Original from|HARVARD UNIVERSITY|Goo?gle$)', re.I)


def _palavras_notas():
    """As palavras (de 4 letras ou mais) das notas de rodapé do autor, pelo Gutenberg."""
    global _NOTAS_PAL
    if _NOTAS_PAL is None:
        s = _pg_bruto()
        notas = [b for b in re.split(r'\n\s*\n', s) if NOTA.match(b.strip())]
        _NOTAS_PAL = {chave(w) for b in notas for w in re.findall(r'[^\W\d_]{4,}', b)}
    return _NOTAS_PAL


def _e_nota(l, minimo=0.7):
    ws = [chave(w) for w in re.findall(r'[^\W\d_]{4,}', l)]
    return bool(ws) and sum(w in _palavras_notas() for w in ws) >= minimo * len(ws) - 1e-9


RETIRADAS = []


CHAMADA = re.compile(r"^[\(\[']?\s?[1iIl]?\s?[\)\].']\s|^[\(\[]?[1iIl][\)\].]?\s")
_PENDENTE = [False]


def _sem_rodape(pag):
    """Tira do pé da página a nota de rodapé do autor: da linha da chamada («1.», «i.», «'») até o
    fim, se a linha é da nota; e, se a nota da página anterior ficou aberta, as últimas linhas da
    página que são da nota (de baixo para cima)."""
    k = len(pag)
    for i in range(len(pag) - 1, max(len(pag) - 25, -1), -1):
        if CHAMADA.match(pag[i]) and _e_nota(pag[i]):
            k = i
            break
    if k == len(pag) and _PENDENTE[0]:
        while k > 0 and _e_nota(pag[k - 1], 0.4) and len(pag) - k < 12:
            k -= 1
    if k < len(pag):
        RETIRADAS.append(pag[k:])
        fim = pag[-1].rstrip()
        _PENDENTE[0] = not re.search(r'[.»]$', fim)
    else:
        _PENDENTE[0] = False
    return pag[:k]


def _juntar(linhas):
    """Linhas do livro -> texto corrido, com as palavras partidas juntas."""
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


def _obra_ocr(paginas):
    linhas = []
    for pag in paginas:
        pag = [l.strip().replace('#', '').replace('¶', '') for l in pag if l.strip() and not LIXO.match(l.strip())]
        pag = [l for l in pag if not TITULO_OCR.match(l)]
        while pag and CABECO.match(pag[0]):            # número da página no alto
            pag = pag[1:]
        while pag and CABECO.match(pag[-1]):
            pag = pag[:-1]
        linhas += _sem_rodape(pag)
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto)
    texto = texto.replace('’', "'").replace("E'", 'É')
    return [{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


def _de_ate(paginas, ini, fim):
    """As páginas do começo do prefácio ao fim do livro (pelas palavras do começo e do fim)."""
    a = next(i for i, p in enumerate(paginas) if any(ini in l for l in p))
    b = next(i for i, p in enumerate(paginas) if any(fim in l for l in p))
    return paginas[a:b + 1]


def toronto():
    s = open(fontes.cache(OBRA, 'ia_djvu.xml'), encoding='utf-8').read()
    paginas = []
    for obj in re.findall(r'<OBJECT.*?</OBJECT>', s, re.S):
        ls = [' '.join(w.strip() for w in re.findall(r'<WORD[^>]*>(.*?)</WORD>', l))
              for l in re.findall(r'<LINE>(.*?)</LINE>', obj, re.S)]
        paginas.append([fontes.nfc(__import__('html').unescape(l)) for l in ls])
    return _obra_ocr(_de_ate(paginas, 'A maior parte de', 'espero ainda'))


def harvard():
    s = open(fontes.cache(OBRA, 'harvard.txt'), encoding='utf-8').read()
    paginas = [fontes.nfc(p).split('\n')[1:] for p in re.split(r'(?m)^@@PAGINA \d+@@$', s)[1:]]
    return _obra_ocr(_de_ate(paginas, 'A maior parte de', 'espero ainda'))


def transcricoes():
    pg = gutenberg()
    md = modernas()
    # as modernas primeiro (com o Gutenberg à frente, o OCR copiava os erros dele); o Gutenberg entra
    # no léxico, para que as grafias de 1900 fiquem como estão
    guias = [md['ws'], md['ob'], pg]
    out = {'pg': pg}
    for nome, f in (('ia', toronto), ('hv', harvard)):
        RETIRADAS.clear()
        o, n = ocr.limpar(f(), guias)
        print(f'OCR {nome}: palavras corrigidas pelas guias: {n}; linhas de rodapé tiradas: '
              f'{sum(len(r) for r in RETIRADAS)}')
        with open(fontes.cache(OBRA, f'rodape-{nome}.txt'), 'w', encoding='utf-8') as f2:
            f2.write('\n\n'.join('\n'.join(r) for r in RETIRADAS))
        o = ocr.estrutura_como(o, pg)
        for p, b in zip(o, pg):
            p['titulo'] = b['titulo']
        out[nome] = o
    return out


# ------------------------------------------------------------------ edições modernas

_MODERNAS = {}


def _ws_moderno():
    """O texto moderno das páginas «não revistas» do Wikisource (17 a 322), corrido."""
    pags = json.load(open(fontes.cache(OBRA, 'ws/wikisource_paginas.json'), encoding='utf-8'))
    partes = []
    for n in range(17, 323):
        v = pags.get(str(n))
        if not v or v['qualidade'] != 1:
            continue
        t = re.sub(r'<noinclude>.*?</noinclude>', '', v['texto'], flags=re.S)
        t = re.sub(r'<[^>]+>', ' ', t)
        t = re.sub(r'\{\{[^{}]*\}\}', ' ', t)
        t = t.replace("'''", '').replace("''", '')
        partes.append(t.strip())
    t = ' '.join(partes)
    t = __import__('html').unescape(t).replace('“', '«').replace('”', '»')
    t = t.replace('#', '').replace('¶', '')
    return [{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(t.replace('\n', ' '))]}]


def _obras_1949():
    """Obras Completas, 1949 (PDF da Brasiliana): sem cabeços, números de página nem títulos."""
    s = fontes.pdf_texto(OBRA, 'https://digital.bbm.usp.br/bitstream/bbm/4743/1/024049-1_COMPLETO.pdf', 'ob1949')
    paginas = [p.split('\n') for p in s.split('\f')]
    paginas = _de_ate(paginas, 'A maior parte de', 'espero ainda')
    linhas = []
    for pag in paginas:
        pag = [l.strip() for l in pag if l.strip()]
        pag = [l for l in pag if not TITULO_OCR.match(l) and not re.match(r'^\d+\s+MINHA FORMA|.*[A-Z]{3,}\s+\d+$', l)]
        linhas += pag
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto).replace('“', '«').replace('”', '»')
    texto = texto.replace('#', '').replace('¶', '')
    return [{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


def modernas():
    if not _MODERNAS:
        pg = gutenberg()
        for nome, f in (('ws', _ws_moderno), ('ob', _obras_1949)):
            o = ocr.estrutura_como(f(), pg)
            for p, b in zip(o, pg):
                p['titulo'] = b['titulo']
            _MODERNAS[nome] = fontes.normalizar(o)
    return _MODERNAS


# ------------------------------------------------------------------ grafia

def modernizar(E, manual):
    """A grafia das modernas (o texto do Wikisource primeiro, as Obras de 1949 onde ele falta), mas a
    crase como em 1900: o livro a marca («á», «ás», «áquelle»), e o texto do Wikisource às vezes a põe
    ou a tira por engano («uma boa fortuna à noite que passei»)."""
    import pickle
    from edicao import modernizar as _mod
    _, md = pickle.load(open(fontes.cache(OBRA, 'fontes.pkl'), 'rb'))
    out, origem, rel = _mod.modernizar(E, [(n, md[n], pos) for n, pos in REFERENCIAS], manual)
    pos = {}
    for j, o in enumerate(origem):
        pos.setdefault(o, j)
    novo_rel = []
    for velho, novo, fonte, i in rel:
        j = pos.get(i)
        if j is not None and fonte != 'manual' and ' ' not in velho:
            v, n = velho, out[j]
            if v[:1] in 'áÁ' and n[:1] in 'aA' and chave(v) == chave(n):
                out[j] = novo = ('À' if n[0] == 'A' else 'à') + n[1:]
            elif v[:1] in 'aA' and n[:1] in 'àÀ':
                out[j] = novo = ('A' if n[0] == 'À' else 'a') + n[1:]
        novo_rel.append((velho, novo, fonte, i))
    return out, origem, novo_rel


# ------------------------------------------------------------------ publicação

DEDICATORIA = 'A meus filhos'


def ler_notas(arq='notas-autor.txt'):
    """{capítulo: (âncora, [parágrafos])} de notas-autor.txt (na grafia de hoje)."""
    por_cap, cap = {}, None
    for l in open(os.path.join(AQUI, arq), encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip() or l.startswith('#'):
            continue
        m = re.match(r'^@ (\S+) (.*)$', l)
        if m:
            cap = m.group(1)
            por_cap[cap] = (m.group(2).strip(), [])
            continue
        por_cap[cap][1].append(l.strip())
    return por_cap


def arrumar(partes):
    """A dedicatória abre o prefácio; as linhas de asteriscos voltam ao seu lugar; cada nota do autor
    vai para o fim do seu capítulo (parágrafos «¤ »), com a chamada [1] depois da âncora."""
    seps = separadores()
    notas = ler_notas()
    usados = set()

    def abre(x, s):
        a = [chave(w) for w in re.findall(r'[^\W_]+', x)[:len(s.split())]]
        return a == [chave(w) for w in re.findall(r'[^\W_]+', s)]
    saida = []
    for p in partes:
        novos = []
        for x in p['paragrafos']:
            if isinstance(x, str):
                for s in seps:
                    if s not in usados and abre(x, s):
                        novos.append('* * *')
                        usados.add(s)
                        break
            novos.append(x)
        if p['titulo'] == PREFACIO:
            novos = [{'verso': [DEDICATORIA]}] + novos
        if p['n'] in notas:
            ancora, corpo = notas[p['n']]
            if ancora != '-':
                k = [i for i, x in enumerate(novos) if isinstance(x, str) and ancora in x]
                if len(k) != 1:
                    print(f'AVISO: nota do cap. {p["n"]}: âncora «{ancora}» achada {len(k)} vezes')
                    k = k or [len(novos) - 1]
                novos[k[0]] = novos[k[0]].replace(ancora, ancora + '[1]', 1)
                corpo = ['[1] ' + corpo[0]] + corpo[1:]
            novos += ['¤ ' + c for c in corpo]
        saida.append(dict(p, paragrafos=novos))
    falta = [s for s in seps if s not in usados]
    if falta:
        print(f'AVISO: separadores sem lugar: {falta}')
    return saida


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
    """Depois do voto: (1) onde só a pontuação difere, vale a do Gutenberg (os OCRs perdem vírgulas e
    pontos finos); (2) os pontos conferidos no fac-símile (conferencia.json: assinatura -> 'pg', 'ia',
    'hv' ou o texto) valem sobre tudo."""
    from edicao.tokens import achatar, e_palavra, texto as junta
    conf = {}
    arq = os.path.join(AQUI, 'conferencia.json')
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
