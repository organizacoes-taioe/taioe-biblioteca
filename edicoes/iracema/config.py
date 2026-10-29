"""Iracema — fontes.

Edições: 1ª, Rio de Janeiro, Tip. de Viana & Filhos, 1865 (à custa do autor); 2ª, Garnier, 1870,
revista pelo autor e com o «Pós-escrito»; 3ª, Garnier, 1878, revista pelo autor (que morreu em
dezembro de 1877) e base da edição crítica de M. Cavalcanti Proença (1965). A 2ª não está
digitalizada; a 3ª está em fac-símile no Google Livros (exemplar da Biblioteca Real da Bélgica,
YXq66mVeOGAC). Edição-base: a de 1878, a última revista pelo autor que se pode ler em fac-símile.

Testemunhos:
  g78   o texto (OCR do Google) do fac-símile de 1878, lido na visualização de texto do Google Livros,
        página a página (cópia em ferramentas/cache/iracema/g1878/). Bom, mas sem os travessões do
        diálogo, sem itálico e com algumas linhas perdidas nas quebras de página. É o fluxo-base.
  ws65  a 1ª edição no Wikisource (fac-símile da Brasiliana USP, bbm/4660), toda validada. Outra
        edição: onde 1878 não mudou o texto, ela corrige o OCR e dá os travessões e o itálico.
Modernas (só apoio e grafia): 'atica', a edição da Ática (1991) na Biblioteca Virtual do Estudante
(USP), que segue o texto de 1878 da edição crítica; 'luso', o texto do MEC (Biblioteca Digital) na
edição da Luso Livros (2013), que segue a 1ª ou a 2ª edição. Onde g78 e ws65 divergem, vence a leitura
com mais apoio moderno; empate fica com 1878.
"""
import html
import json
import os
import re
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import fontes, rede, modernizar as _mod  # noqa: E402
from edicao.grafia import chave  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'iracema'

META = {
    'id': OBRA,
    'autor': 'jose-de-alencar',
    'titulo': 'Iracema',
    'subtitulo': 'Lenda do Ceará',
    'ano': 1865,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Lenda em prosa poética publicada em 1865, com as notas do autor sobre as palavras tupis.',
}

BASE = 'g78'
REFERENCIAS = [('atica', False), ('luso', False)]

ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV',
           'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII',
           'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII']

DEDICATORIA = 'Dedicatória'
PROLOGO = 'Prólogo (da 1.ª edição)'
ARGUMENTO = 'Argumento histórico'
NOTAS = 'Notas'
CARTA = 'Carta ao Dr. Jaguaribe (da 1.ª edição)'
POS = 'Pós-escrito (à 2.ª edição)'

# começo dos capítulos cujo número o OCR perdeu
SEM_CABECALHO = {'XIII': 'Avança a filha de Araken'}
CABECALHO_OCR = {'XXVIF': 'XXVII'}

G1878 = os.path.join(fontes.RAIZ, 'cache', OBRA, 'g1878')
LIXO = re.compile(r'^(?:[\W\d_]{1,3}|[a-zA-HJ-UWYZ]|كم|ہے|OS|de iden|FIM|IRACEMA|\((?:Da|da|a|á) \d.? ?Edic*ção\))$')


# ------------------------------------------------------------------ vocabulário (para juntar quebras)

_VOC = None


def _vocabulario():
    global _VOC
    if _VOC is None:
        pags = json.load(open(fontes.cache(OBRA, 'ws/wikisource_paginas.json'), encoding='utf-8'))
        t = ' '.join(v['texto'] for v in pags.values())
        _VOC = {chave(w) for w in re.findall(r'[^\W\d_]+', t)}
    return _VOC


def _junta(a, b):
    """Junta dois pedaços de um parágrafo partido na quebra de página: sem espaço quando formam
    uma palavra (o OCR perde o hífen: «affla» + «vam»)."""
    ma, mb = re.search(r'([^\W\d_]+)-?$', a), re.match(r'([^\W\d_]+)', b)
    if ma and mb:
        junto = chave(ma.group(1) + mb.group(1))
        if a.endswith('-') or (junto in _vocabulario() and not (chave(ma.group(1)) in _vocabulario()
                                                                  and chave(mb.group(1)) in _vocabulario())):
            return a.rstrip('-') + b
    return a + ' ' + b


# ------------------------------------------------------------------ 1878 (Google)

def _blocos_g78():
    arqs = sorted(f for f in os.listdir(G1878) if f.endswith('.txt'))
    s = '\n\n'.join(open(os.path.join(G1878, f), encoding='utf-8').read().strip() for f in arqs)
    s = fontes.nfc(s).replace('\xad', '')
    blocos = []
    for b in re.split(r'\n\s*\n', s):
        linhas = [l.strip() for l in b.split('\n') if l.strip()]
        for l in linhas:
            # uma linha nova dentro do bloco é parágrafo novo, salvo quando a anterior não fecha frase
            if blocos and blocos[-1][1] == 'aberto' and not re.search(r'[.!?:;»"…]$', blocos[-1][0]) \
                    and re.match(r'[a-zà-ÿ]', l):
                blocos[-1][0] = _junta(blocos[-1][0], l)
            else:
                blocos.append([l, 'aberto'])
        if blocos:
            blocos[-1][1] = 'fim'
    out = []
    for b, _ in blocos:
        if LIXO.match(b):
            continue
        # parágrafo partido pela quebra de página: o pedaço seguinte começa em minúscula
        if out and re.match(r'[a-zà-ÿ]', b) and not re.search(r'[.!?»"…]$', out[-1]) \
                and not re.fullmatch(r'PAG\. \d+\.?', out[-1]):
            out[-1] = _junta(out[-1], b)
        else:
            out.append(b)
    return out


def _apostrofo(p):
    """«E'» e «A'» são o É e o À maiúsculos da tipografia do tempo."""
    p = re.sub(r"\bE['’] ?(?=[^\W\d_])", 'É ', p)
    return re.sub(r"\bA['’] ?(?=[^\W\d_])", 'À ', p)


def _limpar78(p):
    p = _apostrofo(p)
    p = re.sub(r'\s+([,;:!?.])', r'\1', p)
    p = p.replace('<<', '«').replace('>>>', '»').replace('>>', '»')
    p = re.sub(r'(?<=\w) - (?=\w)', ' — ', p)
    p = re.sub(r'^- ', '— ', p)
    p = p.replace('---', '—').replace('--', '—')
    return fontes.limpar(p)


def g78():
    bl = _blocos_g78()
    obra, atual = [], None

    def nova(n, titulo):
        nonlocal atual
        atual = {'n': n, 'titulo': titulo, 'paras': []}
        obra.append(atual)

    nova('', DEDICATORIA)
    atual['paras'].append(VERSO + 'Á TERRA NATAL\nUM FILHO AUSENTE')
    estado = 'antes'
    for b in bl:
        if estado == 'antes':
            if b == 'PROLOGO':
                nova('', PROLOGO)
                estado = 'prologo'
            continue
        if (re.fullmatch(r'[IVXL]+', b) or b in CABECALHO_OCR) and estado in ('prologo', 'texto'):
            nova(CABECALHO_OCR.get(b, b), '')
            estado = 'texto'
            continue
        for n, ini in SEM_CABECALHO.items():
            if b.startswith(ini) and estado == 'texto' and atual['n'] != n:
                nova(n, '')
        if b == 'NOTAS' and estado == 'texto':
            nova('', ARGUMENTO)
            estado = 'argumento'
            continue
        if estado == 'argumento' and re.fullmatch(r'PAG\. \d+\.?', b):
            nova('', NOTAS)
            estado = 'notas'
        if b == 'CARTA':
            nova('', CARTA)
            estado = 'carta'
            continue
        if b.startswith('POSTCRIPTO'):
            nova('', POS)
            estado = 'pos'
            continue
        if b == 'NOTAS':
            continue
        if estado == 'argumento' and b.startswith('Argumento historico.'):
            b = b[len('Argumento historico.'):].strip()
        atual['paras'].append(_limpar78(b))
    nums = [p['n'] for p in obra if p['n']]
    if nums != ROMANOS:
        raise SystemExit(f'g78: capítulos {nums}')
    # as notas: a leitura do Google as embaralha; vão passadas a limpo à parte (notas1878.txt, na grafia
    # de 1878, e notas.txt, na de hoje) e entram no fim de cada capítulo (arrumar)
    obra = [p for p in obra if p['titulo'] != NOTAS]
    return fontes.normalizar(obra)


def ler_notas(arq='notas.txt'):
    """{capítulo: [parágrafos]} de notas.txt (ou notas1878.txt)."""
    por_cap, cap = {}, None
    for l in open(os.path.join(AQUI, arq), encoding='utf-8'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        if l.startswith('@ '):
            cap = l[2:].strip()
            continue
        por_cap.setdefault(cap, []).append(l)
    return por_cap


def arrumar(partes):
    """Cada nota do autor vai para o fim do seu capítulo (parágrafos «¤ »)."""
    por_cap = {c: ['¤ ' + x for x in v] for c, v in ler_notas().items()}
    notas = None
    def miudos(x):
        if not isinstance(x, str):
            return x
        x = re.sub(r'(\d)\. ?ª', r'\1.ª', x)                          # 1.ª (o tokenizador separa)
        x = re.sub(r'\b(\d)a (página|edição)', r'\1.ª \2', x)          # «2a pagina» de 1878
        x = re.sub(r'(^|[.;:,!?—] )([Aa])s vezes', lambda m: m.group(1) + ('À' if m.group(2) == 'A' else 'à') + 's vezes', x)
        x = x.replace('à-margem', 'à margem').replace('«< ', '«')
        return x.replace('mestre-de-campo', 'mestre de campo')
    def juntar_orfas(ps):
        """A última linha curta de um parágrafo, que a leitura do Google perdeu e veio da 1ª edição
        («cruel?», «fiel.»), às vezes fica num parágrafo à parte: volta ao seu."""
        out = []
        for k, x in enumerate(ps):
            if (isinstance(x, str) and re.fullmatch(r'\{ ?\{[^}]*\} ?\}', x)):
                continue                                         # resto de modelo do Wikisource
            prox = ps[k + 1] if k + 1 < len(ps) else None
            if (isinstance(x, str) and len(re.findall(r'\w+', x)) <= 3 and not x.startswith(('—', '¤', '#'))
                    and isinstance(prox, str) and prox.endswith(' ' + x)):
                continue                                         # a mesma linha, já no seu lugar
            if (out and isinstance(x, str) and isinstance(out[-1], str) and len(re.findall(r'\w+', x)) <= 3
                    and not x.startswith(('—', '¤', '#')) and not re.search(r'[.!?:;…»]$', out[-1])):
                out[-1] = out[-1] + ' ' + x
                continue
            out.append(x)
        return out
    saida = []
    for p in partes:
        p = dict(p, paragrafos=juntar_orfas([miudos(x) for x in p['paragrafos']]))
        if p['titulo'] == DEDICATORIA:
            p['paragrafos'] = [{'verso': ['À TERRA NATAL', 'UM FILHO AUSENTE']}]
        if p['titulo'] == PROLOGO and p['paragrafos'][0] == 'Meu Amigo.':
            p['paragrafos'][0] = 'Meu amigo.'
        if p['titulo'] == POS:                 # os números das seções do pós-escrito: título de seção
            p = dict(p, paragrafos=['## ' + x if isinstance(x, str) and re.fullmatch(r'[IV]+\.', x) else x
                                    for x in p['paragrafos']])
        if p['n'] in por_cap:
            p = dict(p, paragrafos=p['paragrafos'] + por_cap.pop(p['n']))
        saida.append(p)
    if por_cap:
        raise SystemExit(f'notas sem capítulo: {list(por_cap)}')
    return saida


# ------------------------------------------------------------------ 1865 (Wikisource)

def _ws_texto(pags, a, b):
    corpo = ''
    for n in range(a, b + 1):
        v = pags.get(str(n))
        if not v or not v['qualidade']:
            continue
        cab = re.search(r'<noinclude>.*?\{\{cabeçalho\|\|([IVXL]+)\}\}.*?</noinclude>', v['texto'], flags=re.S)
        t = re.sub(r'<noinclude>.*?</noinclude>', '', v['texto'], flags=re.S)
        if cab:
            t = '\n\n' + cab.group(1) + '\n\n' + t
        t = re.sub(r'<section[^>]*/>', '', t)
        t = re.sub(r'\{\{Iracema ref\|[^{}]*\}\}', '', t)
        t = re.sub(r'\{\{âncora\|[^{}]*\}\}', '', t)
        t = re.sub(r'\{\{pl\|([^|{}]*)\|[^{}]*\}\}', r'\1', t)
        t = re.sub(r'\{\{sic\|([^|{}]*)\|[^{}]*\}\}', r'\1', t)
        t = re.sub(r'\{\{(?:término|começo) de palavra hifenizada\|([^|{}]*)(?:\|[^{}]*)?\}\}',
                   lambda m: '\u0006' + m.group(1) if 'término' in m.group(0) else m.group(1) + '\u0007', t)
        t = re.sub(r'\{\{(?:Quebra de linha|separador|traço|NOP|nop)\}\}', '\n\n', t)
        t = re.sub(r'\{\{(?:d|direita)\|([^{}]*)\}\}', r'\n\n\1\n\n', t)
        t = re.sub(r"\{\{(?:t2|c)\|(?:<big>)?(?:''')?([^{}|']*?)(?:''')?(?:</big>)?(?:\|[^{}]*)?\}\}", r'\n\n\1\n\n', t)
        t = re.sub(r'\{\{(?:dhr|espaçamento vertical|linha horizontal|Ouça)[^{}]*\}\}', '\n\n', t)
        t = t.replace('{{--}}', '—')
        par_novo = t.startswith('\n')
        t = t.strip()
        if '\u0006' in t:                          # o fim da palavra começada na página anterior
            corpo = re.sub(r'\S*\u0007$', '', corpo.rstrip())
            t = t.replace('\u0006', '')
        elif re.search(r'\w-$', corpo):
            corpo = corpo[:-1]
        else:
            corpo += '\n\n' if par_novo else ' '
        corpo += t
    corpo = corpo.replace('\u0007', '')
    t = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', corpo)
    t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    t = t.replace("'''", '')
    t = re.sub(r"''(.*?)''", r'_\1_', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return [_apostrofo(fontes.limpar(x.replace('\n', ' '))) for x in re.split(r'\n\s*\n', t) if x.strip()]


def ws65():
    arq = 'Iracema - lenda do Ceará.djvu'
    fontes.wikisource_paginas(f'{OBRA}/ws', arq, 1, 240)
    pags = json.load(open(fontes.cache(OBRA, 'ws/wikisource_paginas.json'), encoding='utf-8'))
    obra = [{'n': '', 'titulo': DEDICATORIA, 'paras': [VERSO + 'A’ TERRA NATAL\nUM FILHO AUSENTE.']},
            {'n': '', 'titulo': PROLOGO, 'paras': _ws_texto(pags, 13, 18)}]
    paras = _ws_texto(pags, 21, 176)
    for p in paras:
        if re.fullmatch(r'[IVXL]+', p):
            obra.append({'n': p, 'titulo': '', 'paras': []})
        else:
            obra[-1]['paras'].append(p)
    caps = [p for p in obra if p['n']]
    if len(caps) != 33:
        raise SystemExit(f'ws65: {len(caps)} capítulos')
    for p, r in zip(caps, ROMANOS):          # a 1ª edição numera mal alguns (XVIII por XXVIII, XXIX duas vezes)
        p['n'] = r
    notas = [p for p in _ws_texto(pags, 179, 210) if p != 'NOTAS']   # só o argumento histórico conta
    arg, resto = [], []
    for p in notas:
        (arg if not resto and not re.match(r'Pag\. 1\. — _Onde', p) else resto).append(p)
    arg[0] = re.sub(r'^Pag\. 1\. – _Argumento historico_\. – ', '', arg[0])
    obra.append({'n': '', 'titulo': ARGUMENTO, 'paras': arg})
    carta = [p for p in _ws_texto(pags, 211, 222) if p not in ('CARTA', 'AO DR. JAGUARIBE.')]
    obra.append({'n': '', 'titulo': CARTA, 'paras': carta})
    obra.append({'n': '', 'titulo': POS, 'paras': []})
    return fontes.normalizar(obra)


def _travessoes(obra, outras):
    """O OCR de 1878 perdeu o travessão que abre as falas: volta onde a mesma fala (pelas três
    primeiras palavras) abre com travessão na Ática (texto de 1878) ou na 1ª edição."""
    def k(p):
        return tuple(chave(w) for w in re.findall(r'[^\W\d_]+', p)[:3])
    com = {}
    for o in outras:
        for parte in o:
            for p in parte['paras']:
                if p.startswith(('—', '-')):
                    com.setdefault((parte['n'], parte['titulo']), set()).add(k(p))
    n = 0
    for parte in obra:
        chaves = com.get((parte['n'], parte['titulo']), set())
        for i, p in enumerate(parte['paras']):
            if parte['n'] and not p.startswith('—') and k(p) in chaves:
                parte['paras'][i] = '— ' + p
                n += 1
    return n


def transcricoes():
    g, w = g78(), ws65()
    _travessoes(g, [w, atica()])
    return {'g78': g, 'ws65': w}


# ------------------------------------------------------------------ modernas

def atica():
    """Ática, 1991 (BVEB/USP). O PDF põe a Carta logo depois do prólogo: volta ao fim."""
    s = fontes.pdf_texto(OBRA, 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/'
                               'jose-de-alencar/iracema.pdf', 'atica')
    s = s.replace('\f', '\n')
    s = re.sub(r'(?m)^(Prólogo da 1ª Edição|Carta ao Dr\. Jaguaribe)\s*$', r'@@\1', s)
    s = re.sub(r'(?m)^([IVXL]+)\s*$', r'@@\1', s)
    s = re.sub(r'(?<=\w)\?"', '', s)                     # chamadas de nota («Ipu?"»)
    obra = fontes.texto_por_linhas(s, [r'^@@(?P<n>[IVXL]+)$', r'^@@(?P<t>Prólogo da 1ª Edição|Carta ao Dr\. Jaguaribe)$'])
    pro = [p for p in obra if p['titulo'].startswith('Prólogo')]
    carta = [p for p in obra if p['titulo'].startswith('Carta')]
    caps = [p for p in obra if p['n']]
    for p in pro + carta:
        p['titulo'] = PROLOGO if p in pro else CARTA
    return pro + caps + carta


def luso():
    """Texto do MEC (Biblioteca Digital) na edição «versão original» da Luso Livros: as notas do autor
    vêm entre colchetes no meio do texto (saem) e reordenadas no fim (não entram)."""
    arq = fontes.cache(OBRA, 'luso.epub')
    rede.baixar('https://archive.org/download/iracema-jose-de-alencar-original-lusolivros/Iracema-Jose-de-Alencar.epub', arq)
    z = zipfile.ZipFile(arq)
    obra = []
    for n in sorted(x for x in z.namelist() if x.endswith('.htm')):
        s = z.read(n).decode('utf-8')
        paras = []
        for m in re.finditer(r'<p[^>]*>(.*?)</p>', s, re.S):
            p = re.sub(r'<[^>]+>', '', m.group(1))
            p = html.unescape(p).replace('\xa0', ' ').strip()
            if p:
                paras.append(p)
        if not paras:
            continue
        cab = paras[0]
        m = re.fullmatch(r'CAPÍTULO (\d+)', cab)
        if m:
            corpo = [re.sub(r'\(\*+\)', '', p) for p in paras[1:] if not p.startswith('[(')]
            obra.append({'n': ROMANOS[int(m.group(1)) - 1], 'titulo': '', 'paras': corpo})
        elif cab == 'Contexto Histórico':
            obra.append({'n': '', 'titulo': ARGUMENTO, 'paras': paras[1:]})
        elif cab.startswith('Carta'):
            obra.append({'n': '', 'titulo': CARTA, 'paras': paras[1:]})
        elif cab.upper().startswith('MEU AMIGO') or 'Meu amigo' in cab:
            obra.insert(0, {'n': '', 'titulo': PROLOGO, 'paras': paras})
    return fontes.normalizar([dict(p, paras=[fontes.limpar(x) for x in p['paras']]) for p in obra])


def modernas():
    return {'atica': atica(), 'luso': luso()}


# ------------------------------------------------------------------ grafia

PREP_SI = {'para', 'contra', 'de', 'em', 'por', 'sobre', 'entre', 'a', 'á', 'sob', 'ante', 'perante', 'consigo'}
FEMININOS_NAO = {'esmo', 'medo', 'jorro', 'respeito', 'proposito', 'propósito', 'fazer', 'ser', 'ver', 'cada', 'toda',
                 'qualquer', 'esta', 'essa', 'aquela', 'uma', 'ela', 'elas', 'vossa', 'sua', 'minha', 'nossa', 'tua',
                 'pena', 'guisa'}


def feminino(w):
    """Palavra que, depois do «á» de 1878, pede crase hoje (substantivo feminino): heurística das terminações."""
    lw = w.lower()
    if lw in FEMININOS_NAO or not lw.isalpha():
        return False
    if lw in ('moderna', 'antiga', 'francesa', 'portuguesa', 'brasileira', 'vontade', 'noite', 'tarde', 'margem', 'beira',
              'mão', 'mãos', 'luz', 'semelhança', 'índole', 'parte', 'força', 'imitação', 'proporção', 'maneira', 'medida',
              'censura', 'mesa', 'gramática', 'língua', 'regra', 'preposição', 'escuta', 'sombra', 'foz', 'flor', 'proa'):
        return True
    return bool(re.search(r'(ção|ções|dade|dades|gem|gens|ância|ência|ura|uras|eza|ezas)$', lw))


def secao_ortografia(E):
    """Índices [a, b) em E da seção I do pós-escrito (do primeiro parágrafo depois de «I.» até «II.»)."""
    try:
        k = next(i for i, t in enumerate(E) if t == '#' and E[i + 2] == 'Pós-escrito')
    except StopIteration:
        return None, None
    seq = lambda r: next(i for i in range(k, len(E) - 3) if E[i:i + 4] == ['¶', r, '.', '¶'])
    return seq('I') + 4, seq('II') + 1


def modernizar(E, manual):
    """A grafia das modernas; o que elas não cobrem (notas, pós-escrito) pelo léxico (como em São Bernardo)."""
    sys.path.insert(0, os.path.join(AQUI, '..', 'sao-bernardo'))
    import grafia1990
    import pickle
    _, md = pickle.load(open(fontes.cache(OBRA, 'fontes.pkl'), 'rb'))
    refs = [(n, md[n], pos) for n, pos in REFERENCIAS]
    out, origem, rel = _mod.modernizar(E, refs, manual)
    pos = {}                                   # índice em E -> posição em out
    for j, o in enumerate(origem):
        pos.setdefault(o, j)
    novo_rel = []
    for velho, novo, fonte, i in rel:
        if fonte == 'SEM_PAR':
            n2, f2 = grafia1990.atual(velho, manual)
            if f2 != 'SEM_PAR' or n2 != velho:
                fonte = 'lexico:' + f2
                if i in pos:
                    out[pos[i]] = n2
                novo = n2
        # nos trechos sem edição moderna (notas, pós-escrito): o «si» conjunção e a crase do «á» de 1878
        if fonte.startswith('lexico') and i in pos:
            j = pos[i]
            ant = out[j - 1].lower() if j else ''
            seg = next((t for t in out[j + 1:j + 3] if t[:1].isalpha()), '')
            if velho in ('si', 'Si') and ant not in PREP_SI and not (seg == 'por' and out[j - 1] == 'conjunção'):
                out[j] = novo = 'se' if velho == 'si' else 'Se'
            elif velho in ('á', 'Á', 'ás', 'Ás') and seg and feminino(seg):
                out[j] = novo = {'á': 'à', 'Á': 'À', 'ás': 'às', 'Ás': 'Às'}[velho]
        novo_rel.append((velho, novo, fonte, i))
    # a seção I do pós-escrito discute a ortografia do tempo (acentos, «si», «ão» e «am»): fica na de 1878
    a, b = secao_ortografia(E)
    if a is not None:
        ja = next(j for j, o in enumerate(origem) if o >= a)
        jb = next(j for j, o in enumerate(origem) if o >= b)
        out = out[:ja] + list(E[a:b]) + out[jb:]
        origem = origem[:ja] + list(range(a, b)) + origem[jb:]
        novo_rel = [r for r in novo_rel if not a <= r[3] < b]
    return out, origem, novo_rel


# ------------------------------------------------------------------ desempate

DUVIDAS = []        # sítios para conferir no fac-símile (relatorios/duvidas.tsv)

# leituras de 1878 com grafia que o léxico não conhece (e que a regra do erro de OCR trocaria pela de 1865):
# (leitura g78, leitura ws65) -> testemunho que vale. As modernas que seguem 1878 (Ática) confirmam.
CONFERIDOS = {
    ('múrmuros', 'múrmures'): 'g78', ('murmuros', 'murmures'): 'g78', ('Mecejana', 'Mocejana'): 'g78',
    ('cope', 'copou'): 'g78', ('enflore', 'enflorou'): 'g78', ('remordeu', 'remorde'): 'g78',
    ('confrangia', 'roia'): 'g78', ("no intimo d'alma", 'das almas desnudas'): 'g78', ('rio Tahiba', 'Rio Pacoty'): 'g78',
    ('Cauipe', 'Iguape'): 'g78', ('barra da Piroquara', 'tribu dos pescadores'): 'g78', (', receioso', 'com receio'): 'g78',
    ('autochtones', 'autoctnes'): 'g78', ('este asserto', 'essa asserção'): 'g78', ('amargurava', 'amargava'): 'g78',
    ('Ainda sorpreso', 'Martim ainda surpreso'): 'g78', ('afastavase', 'afastou-se'): 'g78',
    ('apojaram afinal', 'apojarão a final'): 'g78', ('Veiu', ''): 'g78', ('Araracú', 'Acaraú'): 'g78',
    ('- Dispede', '¶ — Saia'): 'g78', ('moviame á', 'me deleitada na'): 'g78', ('abriram inda', 'abrirão ainda'): 'g78',
    ('percebaram', 'perceberão'): 'g78', ('murmu raram', 'murmurarão'): 'g78', ('pégracil', 'pé gracile'): 'g78',
    ('Poty veiu só', 'com suas armas'): 'g78',
}


def rever(tr, md, sitios):
    """g78 × ws65, sem maioria possível. As modernas não são testemunhas puras de 1878 (a Ática segue em
    muitos pontos a 1ª edição; o texto do MEC, ora uma, ora outra), por isso 1878 vale sempre, salvo erro
    do OCR: palavra que não existe onde 1865 traz uma que existe; palavra parecida (uma ou duas letras)
    onde todas as modernas que têm o trecho seguem 1865; pontuação ou parágrafo onde todas as modernas
    seguem 1865. Os casos de palavra que ficam com 1865, e os trechos que faltam em 1878, vão para
    DUVIDAS (relatorios/duvidas.tsv). Devolve (E, sítios)."""
    from difflib import SequenceMatcher
    from edicao.grafia import esqueleto
    from edicao.tokens import achatar, e_palavra, texto as junta, TOK
    sys.path.insert(0, os.path.join(AQUI, '..', 'sao-bernardo'))
    import grafia1990
    voc = _vocabulario()

    def toks(s):
        return TOK.findall(s) if s and s != '(lacuna)' else []

    def pals(ts):
        return [esqueleto(t) for t in ts if e_palavra(t)]

    def sinais(ts):
        return [t if t != '-' else '—' for t in ts if not e_palavra(t)]

    def sim(x, y):
        return SequenceMatcher(None, x, y, autojunk=False).ratio() if (x or y) else 1.0

    def desconhecidas(ts):
        n = 0
        for t in ts:
            if e_palavra(t) and chave(t) not in voc and \
                    any(p and grafia1990.atual_parte(p)[1] == 'SEM_PAR' for p in t.split('-')):
                n += 1
        return n

    B = achatar(tr[BASE])
    partes_B = {i: t[1:] or B[i + 2] for i, t in enumerate(B) if t.startswith('#')}
    partes_B[0] = partes_B.get(0, '-')
    tem = {n: {p['n'] or p['titulo'].split()[0] for p in md[n]} for n in md}
    partes_B = {i: (v if v in ROMANOS else v.split()[0]) for i, v in partes_B.items()}
    DUVIDAS.clear()
    for x in sitios:
        g = x['tokens'].get('g78', [])
        w = x['tokens'].get('ws65', [])
        ga, wa = pals(g), pals(w)
        mods = {n: toks(v) for n, v in x['modernas'].items()}
        # moderna que não tem o trecho (a Ática não tem as notas; o MEC, o prólogo) não opina
        parte = partes_B[max(k for k in partes_B if k <= x['s'])]
        presentes = {n: m for n, m in mods.items() if parte in tem[n]}
        if ga == wa:                                            # só pontuação ou parágrafo
            vota_w = [n for n, m in presentes.items() if sim(sinais(w), sinais(m)) > sim(sinais(g), sinais(m))]
            so_par = [t for t in g if t != '¶'] == [t for t in w if t != '¶']
            # a leitura do Google junta parágrafos (linha que acaba na margem): basta uma moderna com 1865
            esc = 'ws65' if presentes and (len(vota_w) == len(presentes) or (so_par and vota_w)) else 'g78'
            por = f'pontuação; {esc}'
        else:
            dg, dw = desconhecidas(g), desconhecidas(w)
            sup = lambda r: [n for n, m in presentes.items() if pals(m) == r]
            perto = sim(' '.join(ga), ' '.join(wa)) >= 0.6
            chave_x = (x['leituras'].get('g78'), x['leituras'].get('ws65'))
            ini_par = x['antes'].rstrip().endswith('¶') or (w[:1] == ['¶'])
            fim_par = x['depois'].lstrip().startswith('¶') or (w[-1:] == ['¶'])
            # a visualização de texto do Google perde as linhas curtas: a última linha de um parágrafo
            # («cruel?», «fiel.») e as falas de uma linha só («— Bebe!»)
            fim_par = fim_par or g == ['¶']
            fala = not ga and wa and (('¶' in w and '—' in w) or ('—' in w and len(wa) <= 4)
                                      or (fim_par and len(wa) <= 3) or (ini_par and fim_par))
            if chave_x in CONFERIDOS:
                esc, por = CONFERIDOS[chave_x], 'lição de 1878 de grafia antiga; ' + CONFERIDOS[chave_x]
            elif dg > dw and (perto or not ga or abs(len(ga) - len(wa)) <= 1):
                esc, por = 'ws65', 'erro do OCR; ws65'
            elif fala:
                esc, por = 'ws65', 'linha curta perdida pelo OCR; ws65'
            elif not ga or (len(ga) < len(wa) and set(ga) <= set(wa)):
                esc, por = 'g78', 'falta em 1878; g78'
                if 'atica' in presentes and set(wa) - set(ga) <= set(pals(presentes['atica'])):
                    DUVIDAS.append(x)                 # a Ática traz o que falta: o OCR perdeu?
            else:
                esc, por = 'g78', 'lição de 1878; g78'
                if perto and presentes and len(sup(wa)) == len(presentes) and not sup(ga):
                    DUVIDAS.append(x)                 # palavra parecida; as modernas seguem 1865
        x['escolha'] = list(g if esc == 'g78' else w)
        # parágrafo que a leitura do Google juntou: volta se 1865 e alguma moderna o têm
        if esc == 'g78' and '¶' in w and '¶' not in g and any('¶' in m for m in presentes.values()):
            if w[-1] == '¶':
                x['escolha'] = x['escolha'] + ['¶']
            elif w[0] == '¶':
                x['escolha'] = ['¶'] + x['escolha']
        x['escolha_txt'], x['por'] = junta(x['escolha']), por
    E, pos = [], 0
    for x in sitios:
        E.extend(B[pos:x['s']])
        E.extend(x['escolha'])
        pos = x['e']
    E.extend(B[pos:])
    E = [t for t in E if t != '*']
    import csv
    with open(fontes.cache(OBRA, 'relatorios/duvidas.tsv'), 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t')
        wr.writerow(['decisão', 'antes', 'g78', 'ws65', 'atica', 'luso', 'depois'])
        for x in DUVIDAS:
            wr.writerow([x['por'], x['antes'], x['leituras'].get('g78'), x['leituras'].get('ws65'),
                         x['modernas'].get('atica'), x['modernas'].get('luso'), x['depois']])
    return E, sitios

