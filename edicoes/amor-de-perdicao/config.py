"""Amor de Perdição — fontes.

Edição-base: a 1ª edição (Porto, em casa de N. Moré, 1862). O autor reviu o livro na 2ª (1864) e na
5ª (1879, com o «Prefácio da quinta edição»), mas essas duas só estão digitalizadas em imagem
(Wikisource/Commons, sem transcrição); a 1ª é a única com transcrição feita sobre as imagens:
  pg    Projeto Gutenberg nº 16425 (2005), sobre as imagens da Biblioteca Nacional Digital (Portugal),
        revisto pelo Distributed Proofreaders.
O Wikisource tem a 1ª edição página a página, mas ainda sem revisão (nível 1) e vinda da mesma
linhagem; não entra no confronto.
Edições modernas (só para a grafia; não são texto, porque seguem a edição revista):
  bveb  Biblioteca Virtual do Estudante Brasileiro (USP), texto da 5ª edição na grafia brasileira de
        1943, com os prefácios da 2ª e da 5ª;
  luso  Luso Livros (2012), Acordo de 1990 na norma de Portugal, em parte adaptado.

Divisão: dedicatória, prefácio, os vinte capítulos (a 1ª edição numera I a X em cada uma das duas
partes; aqui vão de I a XX, como no Wikisource) e a conclusão. As seis notas do autor, no fim do
volume em 1862, vão para o fim do capítulo em que estão as chamadas.
"""
import html
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import brasil  # noqa: E402
from edicao import modernizar as _mod  # noqa: E402
from edicao.tokens import achatar  # noqa: E402
from edicao.grafia import chave, esqueleto, mesma_palavra  # noqa: E402
from collections import Counter  # noqa: E402

OBRA = 'amor-de-perdicao'

META = {
    'id': OBRA,
    'autor': 'camilo-castelo-branco',
    'titulo': 'Amor de Perdição',
    'subtitulo': 'Memórias de uma família',
    'ano': 1862,
    'genero': 'Romance',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'Romance publicado em 1862, escrito na cadeia da Relação do Porto: o amor de Simão e Teresa.',
}

BASE = 'pg'
REFERENCIAS = [('bveb', False), ('luso', True)]

ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
           'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

SOBRESCRITOS = [('^mo', 'mo'), ('^or', 'or'), ('^as', 'as'), ('^ce', 'ce'), ('^a', 'ª'), ('^o', 'º')]


def gutenberg():
    bruto = open(fontes.cache(OBRA, 'pg16425.txt'), encoding='utf-8').read() if os.path.exists(
        fontes.cache(OBRA, 'pg16425.txt')) else None
    if bruto is None:
        from edicao import rede
        bruto = rede.baixar('https://www.gutenberg.org/cache/epub/16425/pg16425.txt',
                            fontes.cache(OBRA, 'pg16425.txt')).decode('utf-8')
    s = bruto.replace('\r', '')
    s = s.split('*** START OF THE PROJECT GUTENBERG EBOOK', 1)[1].split('\n', 1)[1]
    s = s.split('*** END OF THE PROJECT GUTENBERG EBOOK')[0]
    s = s[s.index('AO ILLUSTRISSIMO'):s.index('Encadernação N.')]
    corpo, notas = s.split('\nFIM.\n')
    corpo = corpo.replace('AO ILLUSTRISSIMO', 'DEDICATORIA.\n\nAO ILLUSTRISSIMO', 1)
    corpo = re.sub(r'\n(PRIMEIRA|SEGUNDA) PARTE\.\n', '\n', corpo)
    corpo = corpo.replace('\nAMOR DE PERDIÇÃO.\n', '\n')
    corpo = re.sub(r'\n\s*\*(\s+\*){4}\s*\n', '\n\n', corpo)
    corpo = re.sub(r'(?m)^ {3,}', '', corpo)                 # citações recuadas (não são versos)
    notas = re.sub(r'\n\s*\*(\s+\*){4}\s*\n', '\n\n', notas)
    s = corpo + '\n\nNOTAS.\n\n' + notas
    s = s.replace('--', '—')
    for a, b in SOBRESCRITOS:
        s = s.replace(a, b)
    obra = fontes.partir_por_cabecalhos(re.split(r'\n\s*\n', s),
                                        [r'^(?P<n>[IVXL]+)\.?$', r'^(?P<t>DEDICATORIA|PREFACIO|CONCLUSÃO|NOTAS)\.$'],
                                        titulo_seguinte=False, verso_indentado=False)
    obra = fontes.normalizar(obra)
    k = 0
    for p in obra:
        if p['titulo'] == '':
            p['n'] = ROMANOS[k]
            k += 1
        else:
            p['titulo'] = {'DEDICATORIA': 'Dedicatória', 'PREFACIO': 'Prefácio', 'CONCLUSÃO': 'Conclusão',
                           'NOTAS': 'Notas'}[p['titulo']]
        p['paras'] = [re.sub(r'\s+([,;:!?])', r'\1', x.replace('\xad', '')) for x in p['paras']]
    if k != 20 or len(obra) != 24:
        raise SystemExit(f'{k} capítulos e {len(obra)} partes (esperados 20 e 24)')
    return obra


def _ws_preparar():
    """Cópia das páginas com cada nota do autor (<ref>) trocada pela chamada «[n]», como no Gutenberg,
    e sem a nota da 5ª edição (p. 246), que não é da 1ª; letras sobrescritas na linha."""
    import json
    origem = fontes.cache(OBRA, 'ws/wikisource_paginas.json')
    if not os.path.exists(origem):
        fontes.wikisource_paginas(f'{OBRA}/ws', 'Amor de Perdição (1862).pdf', 1, 272)
    pags = json.load(open(origem, encoding='utf-8'))
    k = 0
    for n in sorted(pags, key=int):
        t = pags[n]['texto']

        def nota(m):
            nonlocal k
            if 'follow=' in m.group(0)[:40] or 'Nota da 5' in m.group(0):
                return ''
            k += 1
            return f'[{k}]'
        t = re.sub(r'<ref[^>]*>.*?</ref>', nota, t, flags=re.S)
        t = re.sub(r'<sup>(\w+)</sup>', lambda m: 'ª' if m.group(1) == 'a' else m.group(1), t)
        pags[n]['texto'] = t
    destino = fontes.cache(OBRA, 'wsx/wikisource_paginas.json')
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    json.dump(pags, open(destino, 'w', encoding='utf-8'), ensure_ascii=False)


def wikisource(base):
    """Wikisource, 1ª edição página a página: um terço revisto sobre as imagens (Giro720), o resto em
    OCR cru, de outra leitura que a do Gutenberg. Sem a dedicatória (misturada à folha de rosto) nem as
    notas: ali não vota (LACUNA). Os parágrafos vêm do Gutenberg (o OCR parte as linhas)."""
    from edicao import ocr
    from edicao.tokens import LACUNA
    _ws_preparar()
    o = fontes.wikisource(f'{OBRA}/wsx', 'Amor de Perdição (1862).pdf', 1, 272,
                          rom=r'^(?P<n>[IVXL]+)\.?$|^(?P<t>DEDICATORIA|PREFACIO|CONCLUSÃO|NOTAS)\.?$', titulos=False)
    o = fontes.normalizar(o)
    if len(o) != 23:
        raise SystemExit(f'Wikisource: {len(o)} partes (esperadas 23)')
    o[0] = dict(o[0], paras=[LACUNA])
    conc = o[-1]['paras']
    if conc and conc[-1].startswith('FIM'):
        conc.pop()
    o.append({'n': '', 'titulo': 'Notas', 'paras': [LACUNA]})
    for p, b in zip(o, base):
        p['n'], p['titulo'] = b['n'], b['titulo']
        p['paras'] = [x.replace('’', "'").replace('\x04', ' ') for x in p['paras']]
    return ocr.paragrafos_como(o, base)


def transcricoes():
    pg = gutenberg()
    return {'pg': pg, 'ws': wikisource(pg)}


def luso():
    """Luso Livros (2012), Acordo de 1990 (norma de Portugal); epub do Internet Archive."""
    arq = fontes.cache(OBRA, 'lusolivros.epub')
    if not os.path.exists(arq):
        from edicao import rede
        rede.baixar('https://archive.org/download/branco-camilo-castelo-amor-de-perdicao-lusolivros/'
                    'Branco%2C%20Camilo%20Castelo%20-%20Amor%20de%20Perdi%C3%A7%C3%A3o.epub', arq)
    z = zipfile.ZipFile(arq)
    obra = []
    for n in sorted(x for x in z.namelist() if re.search(r'split_0*(\d+)\.htm$', x)):
        t = z.read(n).decode('utf-8')
        for m in re.finditer(r'<p[^>]*>(.*?)</p>', t, re.S):
            p = re.sub(r'<span class="calibre9">(.*?)</span>', r'_\1_', m.group(1), flags=re.S)
            p = html.unescape(re.sub(r'<[^>]+>', '', p)).replace('\xa0', ' ')
            p = fontes.limpar(p.replace('\n', ' '))
            if not p:
                continue
            if re.fullmatch(r'CAPÍTULO [IVXL]+|Introdução|CONCLUSÃO|Conclusão', p):
                obra.append({'n': '', 'titulo': p, 'paras': []})
            elif obra:
                obra[-1]['paras'].append(p)
    return fontes.normalizar(obra)


def bveb():
    """BVEB (USP): texto da 5ª edição, grafia brasileira de 1943; usado inteiro, num bloco só (a
    modernização alinha o livro todo de uma vez; os cabeçalhos de vários capítulos se perderam no PDF)."""
    s = fontes.pdf_texto(OBRA, 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/'
                         'camilo-castelo-branco/amor-de-perdicao.pdf', 'bveb')
    s = s.replace('\f', '\n')
    s = s[:s.index('PREFÁCIO DA SEGUNDA EDIÇÃO')]
    linhas = [l.strip() for l in s.split('\n')]
    texto = ''
    for l in linhas:
        if not l or re.fullmatch(r'\d+|[IVXL]+', l):
            continue
        if texto.endswith('-') and not texto.endswith(' -') and re.match(r'[a-zà-ÿ]', l):
            texto = texto[:-1] + l
        else:
            texto = (texto + ' ' + l).strip()
    texto = texto.replace('"', '')
    return [{'n': '', 'titulo': '', 'paras': [fontes.limpar(texto)]}]


def modernas():
    return {'bveb': bveb(), 'luso': luso()}


def arrumar(partes):
    """Cada nota do autor vai para o fim do capítulo da sua chamada («[1]»), como «¤ » (o site a
    mostra no fim da página); a quebra de seção da conclusão volta como «* * *»."""
    notas = next(p for p in partes if p['titulo'] == 'Notas')
    por_n = {}
    for x in notas['paragrafos']:
        m = re.match(r'\[ ?(\d) ?\] ?(.*)$', x, re.S) if isinstance(x, str) else None
        if m:
            por_n[m.group(1)] = [m.group(2)]
        elif por_n:
            por_n[list(por_n)[-1]].append(x)
    saida = []
    for p in partes:
        if p is notas:
            continue
        novos, fim = [], []
        for x in p['paragrafos']:
            if isinstance(x, str):
                x = re.sub(r' ?\[ ?(\d) ?\]', r'[\1]', x)
                for n in re.findall(r'\[(\d)\]', x):
                    corpo = por_n.pop(n)
                    fim.append(f'¤ [{n}] ' + corpo[0])
                    fim += ['¤ ' + c for c in corpo[1:]]
                if p['titulo'] == 'Conclusão' and x.startswith('Da família de Simão Botelho'):
                    novos.append('* * *')
            novos.append(x)
        saida.append(dict(p, paragrafos=novos + fim))
    if por_n:
        print(f'AVISO: notas sem chamada: {sorted(por_n)}')
    return saida


# «d'» + palavra: a grafia de hoje separa (d'um -> de um, d'agua -> de água), salvo nas contrações que
# viraram uma palavra só (d'elle -> dele, d'ahi -> daí: o alinhamento com as modernas resolve), nos
# nomes e expressões francesas e nos versos (a elisão conta na medida)
FUNDIDAS = re.compile(r"(?i)(ell?[ae]s?|éll?e|est[ae]s?|ess[ae]s?|aquell?[ae]s?|aquill?o|isso|isto|ahi|aqui|"
                      r"all?i|onde|entre|antes|outr'ora|ora)$")
FRANCESAS = set()


# formas do autor que o léxico moderno confundiria com outra palavra (dize ~ disse, traz ~ trás)
NAO_AUTO = {'Morrerá', 'morrerá', "p'ra", 'traz', 'Traz', 'dize', 'Dize', 'dize-me', 'Dize-me', 'Dize-lhe', 'faze', 'faze-me', 'traze-me', 'Traze'}


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
