"""Os Maias — fontes.

Edição-base: a 1ª edição (Porto, Livraria Internacional de Ernesto Chardron — Lugan & Genelioux,
1888, 2 volumes), a única publicada em vida do autor. Três transcrições dela:
  pg    Projeto Gutenberg nº 40409 (2012), sobre as imagens da Biblioteca Nacional de Portugal;
  ws    Wikisource, páginas sobre o fac-símile do Commons (vol. 1 em DjVu, vol. 2 em PDF), quase todas
        revisadas («Giro bot»); o texto veio do Gutenberg (as mesmas correções, marcadas com {{corr}}),
        por isso os dois são aparentados;
  bveb  Biblioteca Virtual do Estudante Brasileiro (USP), «texto-base digitalizado pela Biblioteca
        Nacional de Portugal», sem itálico nem parágrafos confiáveis (recebe os do Gutenberg).
Edições modernas (só para a grafia e o desempate; não são texto): a da Luso Livros (2012, Acordo de
1990 na norma de Portugal) e a da eBooksFrance (2000, grafia portuguesa de 1945), da mesma linhagem.
Nenhuma está na grafia brasileira: `modernizar` (abaixo) leva a forma portuguesa à brasileira.

Divisão: a 1ª edição numera os capítulos por volume (I a X e I a VIII, com dois «VII» no vol. 1 e um
salto de IV para VII no vol. 2); aqui eles vão de I a XVIII, como nas edições modernas.
"""
import html
import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes, modernizar as _mod, ocr  # noqa: E402
from edicao.tokens import VERSO, achatar  # noqa: E402
from edicao.grafia import chave, esqueleto, mesma_palavra  # noqa: E402
from collections import Counter  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import brasil  # noqa: E402

OBRA = 'os-maias'

META = {
    'id': OBRA,
    'autor': 'eca-de-queiros',
    'titulo': 'Os Maias',
    'subtitulo': 'Episódios da vida romântica',
    'ano': 1888,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1888, em dois volumes, o mais longo de Eça de Queirós.',
}

BASE = 'pg'
# o Wikisource veio do Gutenberg (vol. 1 quase sem revisão; vol. 2 revisto nas imagens), e o Gutenberg
# partilha com a BVEB muitos erros (a BVEB é anterior: provável ponto de partida do Gutenberg)
CORRELACIONADOS = [('pg', 'ws'), ('pg', 'bveb')]
REFERENCIAS = [('luso', True), ('ebf', False)]

ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
           'XV', 'XVI', 'XVII', 'XVIII']

# capítulos no Wikisource: (volume, primeira página, última página)
WS_ARQ = {1: 'Os Maias - Volume 1.djvu', 2: 'Os Maias - Volume 2.pdf'}
WS_CAPS = [(1, 11, 47), (1, 49, 77), (1, 79, 124), (1, 125, 158), (1, 159, 201), (1, 203, 256),
           (1, 257, 298), (1, 299, 343), (1, 345, 408), (1, 409, 468),
           (2, 11, 62), (2, 63, 118), (2, 119, 156), (2, 157, 236), (2, 237, 350), (2, 351, 412),
           (2, 413, 500), (2, 501, 542)]

# abreviaturas com letras sobrescritas: uma forma só em todos os testemunhos
# (impressas em linha, sem espaço: sr.ª, S.ta, M.me, ex.as; ver decisoes.corrigir)
SOBRESCRITOS = [('^{ta}', 'ta'), ('.{ta}', '.ta'), ('^{me}', 'me'), ('^{as}', 'as'), ('^{mo}', 'mo'), ('^{os}', 'os'),
                ('^ta', 'ta'), ('^t', 't'), ('^a', 'ª'), ('^o', 'º'), ('[oe]', 'œ'), ('[~e]', 'ẽ')]


def numerar(obra):
    """Só os capítulos (partes com texto), numerados de I a XVIII."""
    caps = [p for p in obra if p['paras']]
    if len(caps) != 18:
        raise SystemExit(f'{len(caps)} capítulos (esperados 18): {[p["n"] for p in caps]}')
    return [dict(p, n=r, titulo='') for p, r in zip(caps, ROMANOS)]


def _limpar_para(p):
    p = p.replace('\xad', '')
    p = re.sub(r"(?<![\w_])([dD]['’])_", r"_\1", p)          # d'_Ophelia_ -> _d'Ophelia_
    p = re.sub(r'\s+([,;:!?])', r'\1', p) if not p.startswith(VERSO) else p
    return p


def gutenberg():
    obra = fontes.gutenberg(OBRA, 40409, [r'^(?P<n>[IVXL]+)$'], fim='FIM DO SEGUNDO VOLUME',
                            titulo_seguinte=False, trocar=SOBRESCRITOS)
    for p in obra:                       # o rosto do 2º volume fica no fim do capítulo X
        if 'FIM DO PRIMEIRO VOLUME' in p['paras']:
            p['paras'] = p['paras'][:p['paras'].index('FIM DO PRIMEIRO VOLUME')]
        p['paras'] = [_limpar_para(x) for x in p['paras']]
    return numerar(obra)


def _ws_preparar(vol):
    """Cópia das páginas com os modelos que o leitor geral não conhece já resolvidos."""
    origem = fontes.cache(OBRA, f'ws{vol}/wikisource_paginas.json')
    destino = fontes.cache(OBRA, f'ws{vol}x/wikisource_paginas.json')
    if not os.path.exists(origem):
        fontes.wikisource_paginas(f'{OBRA}/ws{vol}', WS_ARQ[vol], 1, 478 if vol == 1 else 560)
    pags = json.load(open(origem, encoding='utf-8'))
    for v in pags.values():
        t = v['texto']
        t = re.sub(r'\{\{hífen\|[^|}]*\|([^|}]*)\}\}', r'\1', t)          # palavra partida entre páginas
        t = re.sub(r'\{\{hífen-fim\|[^}]*\}\}', '', t)
        t = re.sub(r'\{\{espaço vertical[^}]*\}\}', '', t)
        t = re.sub(r'\{\{corr\|[^|}]*\|([^|}]*)\}\}', r'\1', t)
        t = re.sub(r'\{\{Quote\|(.*?)\}\}', lambda m: '<poem>' + m.group(1) + '</poem>', t, flags=re.S)

        def poema(m):
            linhas = [l.strip().lstrip(':').strip() for l in m.group(1).split('\n')]
            return '\n\n' + '<br>'.join(l for l in linhas if l) + '\n\n'
        t = re.sub(r'(?:<blockquote>)?<poem[^>]*>(.*?)</poem>(?:</blockquote>)?', poema, t, flags=re.S)
        t = re.sub(r'\n\s*<br ?/?>\s*\n', '\n\n', t)                       # quebra de seção
        t = t.replace('\xad', '')
        t = re.sub(r'<sup>(\w+)</sup>', r'\1', t)
        for a, b in SOBRESCRITOS:
            t = t.replace(a, b)
        v['texto'] = t
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    json.dump(pags, open(destino, 'w', encoding='utf-8'), ensure_ascii=False)


def wikisource():
    obra = []
    for vol in (1, 2):
        _ws_preparar(vol)
    for vol, a, b in WS_CAPS:
        partes = fontes.wikisource(f'{OBRA}/ws{vol}x', WS_ARQ[vol], a, b, rom=r'^(?P<n>[IVXL]+)$', titulos=False)
        paras = [_limpar_para(x) for p in partes for x in p['paras']]
        paras = [x for x in paras if x not in ('FIM DO SEGUNDO VOLUME', 'OS MAIAS')]
        obra.append({'n': '', 'titulo': '', 'paras': paras})
    return numerar(fontes.normalizar(obra))


def bveb(base):
    """PDF da BVEB: as linhas não marcam parágrafo; cada capítulo vira um bloco, e os parágrafos
    vêm do Gutenberg (ocr.paragrafos_como)."""
    s = fontes.pdf_texto(OBRA, 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/'
                         'eca-de-queiros/os-maias.pdf', 'bveb')
    s = s.replace('\f', '\n')
    s = s[s.index('Livro Primeiro'):s.rindex('FIM')]
    obra, atual = [], None
    for l in s.split('\n'):
        l = l.strip()
        if not l or l in ('Livro Primeiro', 'Livro Segundo'):
            continue
        if re.fullmatch(r'[IVXL]+', l):
            atual = {'n': '', 'titulo': '', 'paras': ['']}
            obra.append(atual)
            continue
        par = atual['paras'][-1]
        if par.endswith('-') and not par.endswith(' -') and re.match(r'[a-zà-ÿ]', l):
            atual['paras'][-1] = par[:-1] + l
        else:
            atual['paras'][-1] = (par + ' ' + l).strip()
    obra = numerar(fontes.normalizar([dict(p, paras=[fontes.limpar(x) for x in p['paras']]) for p in obra]))
    obra = ocr.paragrafos_como(obra, base)
    return versos_como(obra, base)


def versos_como(obra, base):
    """A BVEB não separa os versos: cada parágrafo que tem as mesmas palavras de um bloco de versos
    da base é partido nos mesmos pontos (as palavras continuam as da BVEB)."""
    from edicao.grafia import chave
    from edicao.tokens import TOK, texto
    palavras = lambda s: [t for t in TOK.findall(s) if t[:1].isalnum()]
    for pb, po in zip(base, obra):
        versos = {tuple(chave(w) for w in palavras(x)): x for x in pb['paras'] if x.startswith(VERSO)}
        novos = []
        for x in po['paras']:
            v = versos.get(tuple(chave(w) for w in palavras(x)))
            if v and not x.startswith(VERSO):
                toks = TOK.findall(x)
                linhas, i = [], 0
                for l in v[1:].split('\n'):
                    n = len(palavras(l))
                    j, c = i, 0
                    while j < len(toks) and (c < n or not toks[j][:1].isalnum()):
                        c += toks[j][:1].isalnum()
                        j += 1
                    linhas.append(texto(toks[i:j]))
                    i = j
                if toks[i:]:
                    linhas[-1] += ' ' + texto(toks[i:])
                x = VERSO + '\n'.join(linhas)
            novos.append(x)
        po['paras'] = novos
    return obra


def transcricoes():
    pg = gutenberg()
    return {'pg': pg, 'ws': wikisource(), 'bveb': bveb(pg)}


def luso():
    """Luso Livros (2012), Acordo de 1990 (norma de Portugal); epub do Internet Archive."""
    arq = fontes.cache(OBRA, 'lusolivros.epub')
    if not os.path.exists(arq):
        from edicao import rede
        rede.baixar('https://archive.org/download/os-maias_lusolivros/Os-Maias-Eca-de-Queiros.epub', arq)
    z = zipfile.ZipFile(arq)
    obra = []
    for n in sorted(x for x in z.namelist() if re.search(r'split_0*(\d+)\.htm$', x)):
        t = z.read(n).decode('utf-8')
        paras = []
        for m in re.finditer(r'<p[^>]*>(.*?)</p>', t, re.S):
            p = re.sub(r'<span class="calibre9">(.*?)</span>', r'_\1_', m.group(1), flags=re.S)
            p = html.unescape(re.sub(r'<[^>]+>', '', p)).replace('\xa0', ' ')
            p = fontes.limpar(p.replace('\n', ' '))
            if p:
                paras.append(p)
        if paras and re.fullmatch(r'CAPÍTULO [IVXL]+', paras[0]):
            obra.append({'n': paras[0].split()[1], 'titulo': '', 'paras': paras[1:]})
    return fontes.normalizar(obra)


def ebooksfrance():
    """eBooksFrance (2000), na edição do eBooksBrasil (2006): grafia portuguesa de 1945."""
    from edicao import rede
    b = rede.baixar('http://www.ebooksbrasil.org/eLibris/maias.html', fontes.cache(OBRA, 'ebooksbrasil_maias.html'),
                    cabecalhos={'User-Agent': 'Mozilla/5.0'})
    s = b.decode('latin-1')
    s = s[s.index('<h3>Capítulo I</h3>'):s.rindex('éditions eBooksFrance<br />')]
    obra = []
    for m in re.finditer(r'<h3>Capítulo ([IVXL]+)</h3>|<p[^>]*>(.*?)</p>', s, re.S):
        if m.group(1):
            obra.append({'n': m.group(1), 'titulo': '', 'paras': []})
            continue
        p = re.sub(r'</?i>', '_', m.group(2))
        p = re.sub(r'<br ?/?>', '\n', p)
        p = html.unescape(re.sub(r'<[^>]+>', '', p)).replace('\xa0', ' ')
        p = re.sub(r'(\w)-\n(\w)', r'\1\2', p)
        p = fontes.limpar(p.replace('\n', ' '))
        p = p.replace('_ _', ' ').replace('__', '')
        if p and obra:
            obra[-1]['paras'].append(p)
    return fontes.normalizar(obra)


def modernas():
    return {'luso': luso(), 'ebf': ebooksfrance()}


# «d'» + palavra: a grafia de hoje separa (d'um -> de um, d'agua -> de água), salvo nas contrações que
# viraram uma palavra só (d'elle -> dele, d'ahi -> daí: o alinhamento com as modernas resolve), nos
# nomes e expressões francesas e nos versos (a elisão conta na medida)
FUNDIDAS = re.compile(r"(?i)(ell?[ae]s?|éll?e|est[ae]s?|ess[ae]s?|aquell?[ae]s?|aquill?o|isso|isto|ahi|aqui|"
                      r"all?i|onde|entre|antes|outr'ora|ora)$")
FRANCESAS = {'Or', 'Albe', 'Escompte', 'abord', 'Arc', 'Orsay', 'Artagnan', 'Amanda'}


# formas do autor que o léxico moderno confundiria com outra palavra (dize ~ disse, traz ~ trás)
NAO_AUTO = {'traz', 'Traz', 'dize', 'Dize', 'dize-me', 'Dize-me', 'Dize-lhe', 'faze', 'faze-me', 'traze-me', 'Traze'}


def separar_elisoes(E):
    E2, mapa = [], []
    verso = False
    for i, t in enumerate(E):
        if t == '¶':
            # parágrafo de versos: tem '/' antes do próximo '¶'
            j = i + 1
            while j < len(E) and E[j] != '¶':
                j += 1
            verso = '/' in E[i + 1:j]
        m = re.match(r"([dD])['’](.+)$", t)
        if m and not verso and m.group(2) not in FRANCESAS and not FUNDIDAS.match(m.group(2)):
            E2 += [m.group(1) + 'e', m.group(2)]
            mapa += [i, i]
            continue
        E2.append(t)
        mapa.append(i)
    return E2, mapa


def modernizar(E, manual):
    """Grafia das edições modernas (portuguesas) e, depois, a brasileira (brasil.py)."""
    from edicao.fontes import cache
    import pickle
    tr, md = pickle.load(open(cache(OBRA, 'fontes.pkl'), 'rb'))
    refs = [(n, md[n], pos) for n, pos in REFERENCIAS]
    E2, mapa = separar_elisoes(E)
    out, origem, rel = _mod.modernizar(E2, refs, {})
    # palavras que o alinhamento não emparelhou: a forma moderna da mesma palavra em outro ponto
    # das edições modernas (approximava -> aproximava), quando só há uma
    lexico = {}
    for n, obra, pos in refs:
        for t in achatar(obra):
            if t[:1].isalpha():
                lexico.setdefault(esqueleto(t), Counter())[t if t[1:] != t[1:].lower() else t.lower()] += 1
    auto = {}
    for velho, novo, fonte, i in rel:
        if fonte != 'SEM_PAR' or not velho[:1].isalpha() or velho in manual or velho in auto:
            continue
        cand = lexico.get(esqueleto(velho))
        if cand:
            forma = cand.most_common(1)[0][0]
            if (forma.lower() != velho.lower() and len(velho) > 2 and mesma_palavra(velho, forma)
                    and chave(velho) == chave(forma) and velho not in NAO_AUTO):
                auto[velho] = forma
    with open(fontes.cache(OBRA, 'relatorios/auto.tsv'), 'w', encoding='utf-8') as f:
        f.writelines(f'{a}\t{b}\n' for a, b in sorted(auto.items()) if a not in manual)
    manual = dict(auto, **manual)
    out = [brasil.converter(t, E2[o]) for t, o in zip(out, origem)]
    rel = [(velho, brasil.converter_frase(novo, velho), fonte, i) for velho, novo, fonte, i in rel]
    out, origem, rel = aplicar_manual(E2, out, origem, rel, manual)
    return out, [mapa[o] for o in origem], [(v, n, f, mapa[i]) for v, n, f, i in rel]


def aplicar_manual(E, out, origem, rel, manual, converter=()):
    """MANUAL: {forma antiga: forma final}; troca a saída de cada palavra antiga listada."""
    if not manual:
        return out, origem, rel
    novo_out, novo_or = [], []
    i = 0
    while i < len(out):
        o = origem[i]
        j = i
        while j < len(out) and origem[j] == o:
            j += 1
        velho = E[o]
        if velho in manual and any(c.isalpha() for c in velho):
            from edicao.grafia import igualar_caixa, forma_atual
            troca = manual[velho].split(' ')
            if velho in converter:                         # forma das edições modernas: ainda portuguesa
                troca = [brasil.converter(forma_atual(x), velho) for x in troca]
            troca = [igualar_caixa(velho, troca[0])] + troca[1:]
            novo_out += troca
            novo_or += [o] * len(troca)
        else:
            novo_out += out[i:j]
            novo_or += origem[i:j]
        i = j
    rel = [(v, manual[v] if v in manual else n, 'manual' if v in manual else f, k) for v, n, f, k in rel]
    return novo_out, novo_or, rel
