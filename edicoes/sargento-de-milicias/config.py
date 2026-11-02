"""Memórias de um Sargento de Milícias — fontes (EM ANDAMENTO: ver FALTA.md nesta pasta).

Edição-base: a 1ª edição em livro, «por um Brasileiro» (Rio de Janeiro, Typographia Brasiliense de
Maximiano Gomes Ribeiro, rua do Sabão n. 114; tomo I de 1854, tomo II de 1855), a única em vida do
autor (o romance saíra antes em folhetim, sem assinatura, na «Pacotilha» do Correio Mercantil, de
27/06/1852 a 31/07/1853). Não há transcrição humana da 1ª edição; os testemunhos dela são:
  pdf  a camada de texto (OCR da Brasiliana) do fac-símile da Brasiliana USP, BBM 4846
       (https://digital.bbm.usp.br/handle/bbm/4846, os dois tomos num volume; a página do PDF é a do
       DjVu do Commons, que é o mesmo exemplar);
  bt   OCR próprio (Tesseract) do mesmo PDF: edicoes/sargento-de-milicias/tesseract.py bbm4846:9-309.
Os dois são do mesmo exemplar, mas de programas diferentes; valem um voto cada (modelo: Caetés e
São Bernardo, ver o README das ferramentas, «Sem edição moderna»).
Edição moderna (só para a estrutura, a grafia e o desempate; não é texto): a do Wikisource
(«ws»), que está posta sobre as páginas do DjVu de 1854 (Index:Memorias de um sargento de milicias.djvu,
páginas de qualidade 1, «Phe-bot»), mas é um texto moderno no Formulário de 1943 (idéia), da linhagem
das edições escolares; dá os parágrafos e a divisão. Falta uma segunda moderna (Domínio Público/BVEB).

Divisão: dois tomos, como em 1854–55: o I com 23 capítulos, o II com 25 (numeração recomeçada).
No fluxo, cada capítulo é uma parte «I.I» … «I.XXIII», «II.I» … «II.XXV»; a publicação refaz os
dois tomos (como agrupar() de Policarpo Quaresma). Os títulos são os de 1854–55 (o Wikisource os
moderniza ou troca: «batismo», «Despedidas»), na grafia de hoje.
"""
import csv
import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402,F401
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'sargento-de-milicias'

META = {
    'id': OBRA,
    'autor': 'manuel-antonio-de-almeida',
    'titulo': 'Memórias de um Sargento de Milícias',
    'ano': 1854,
    'genero': 'Romance',
    'divisao': {'singular': 'tomo', 'plural': 'tomos', 'rotulo': 'nome', 'marcas': False},
    'descricao': 'Romance publicado em folhetim em 1852–53 e em livro em 1854–55, em dois tomos, '
                 'a única edição em vida do autor.',
}

ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV',
       'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV']
TOMOS = ['Tomo I', 'Tomo II']

# capítulo -> (primeira, última página do PDF/DjVu) e título de 1854–55 na grafia de hoje (lidos no
# cabeçalho de cada capítulo da camada do PDF; conferir nas imagens os marcados com «?»)
CAPITULOS = [
    ('I.I', 9, 14, 'Origem, nascimento e batizado'),
    ('I.II', 15, 23, 'Primeiros infortúnios'),
    ('I.III', 25, 30, 'Despedida às travessuras'),
    ('I.IV', 31, 34, 'Fortuna'),
    ('I.V', 35, 39, 'O Vidigal'),
    ('I.VI', 41, 46, 'Primeira noite fora de casa'),
    ('I.VII', 47, 51, 'A comadre'),
    ('I.VIII', 53, 56, 'O pátio dos bichos'),
    ('I.IX', 57, 61, 'O «arranjei-me» do compadre'),
    ('I.X', 63, 69, 'Explicações'),
    ('I.XI', 71, 76, 'Progresso e atraso'),
    ('I.XII', 77, 81, 'Entrada para a escola'),
    ('I.XIII', 83, 88, 'Mudança de vida'),
    ('I.XIV', 89, 95, 'Nova vingança e seu resultado'),
    ('I.XV', 97, 103, 'Estralada'),
    ('I.XVI', 105, 108, 'Sucesso do plano'),
    ('I.XVII', 109, 117, 'D. Maria'),
    ('I.XVIII', 119, 122, 'Amores'),
    ('I.XIX', 123, 126, 'Domingo do Espírito Santo'),
    ('I.XX', 127, 131, 'O fogo no campo'),
    ('I.XXI', 133, 137, 'Contrariedades'),
    ('I.XXII', 139, 142, 'Aliança'),
    ('I.XXIII', 143, 146, 'Declaração'),
    ('II.I', 151, 156, 'A comadre em exercício'),
    ('II.II', 157, 162, 'Trama'),
    ('II.III', 163, 168, 'Derrota'),
    ('II.IV', 169, 173, 'O mestre de reza'),
    ('II.V', 175, 181, 'Transtorno'),
    ('II.VI', 183, 188, 'Pior transtorno'),
    ('II.VII', 189, 193, 'Remédio aos males'),
    ('II.VIII', 195, 199, 'Novos amores'),
    ('II.IX', 201, 208, 'José Manuel triunfa'),
    ('II.X', 209, 214, 'O agregado'),
    ('II.XI', 215, 219, 'Malsinação'),
    ('II.XII', 221, 225, 'Triunfo completo de José Manuel'),
    ('II.XIII', 227, 231, 'Escápula'),          # ? 1855: ESCAPULA (sem acento nas maiúsculas)
    ('II.XIV', 233, 237, 'O Vidigal desapontado'),
    ('II.XV', 239, 242, 'Caldo entornado'),
    ('II.XVI', 243, 247, 'Ciúmes'),
    ('II.XVII', 249, 252, 'Fogo de palha'),
    ('II.XVIII', 253, 259, 'Represálias'),
    ('II.XIX', 261, 266, 'O granadeiro'),
    ('II.XX', 267, 276, 'Novas diabruras'),
    ('II.XXI', 277, 281, 'Descoberta'),
    ('II.XXII', 283, 287, 'Empenhos'),
    ('II.XXIII', 289, 294, 'As três em comissão'),
    ('II.XXIV', 295, 300, 'A morte é juiz'),
    ('II.XXV', 301, 305, 'Conclusão feliz'),
]
TITULOS = {c[0]: c[3] for c in CAPITULOS}
PDF = 'https://digital.bbm.usp.br/bitstream/bbm/4846/1/000284_COMPLETO.pdf'


# ------------------------------------------------------------------ edição moderna (estrutura)

_MODERNAS = {}


def wikisource_moderno():
    """O texto moderno do Wikisource, capítulo a capítulo pelas páginas do DjVu (CAPITULOS)."""
    pags = fontes.wikisource_paginas(OBRA, 'Memorias de um sargento de milicias.djvu', 1, 308)
    obra = []
    for n, a, b, tit in CAPITULOS:
        corpo = ''
        for k in range(a, b + 1):
            v = pags.get(k)
            if not v:
                continue
            t = re.sub(r'<noinclude>.*?</noinclude>', '', v['texto'], flags=re.S).strip('\n').rstrip()
            t = re.sub(r'<poem>(.*?)</poem>', lambda m: '\n\n' + VERSO + m.group(1).strip() + '\n\n', t, flags=re.S)
            if corpo and v['texto'].split('</noinclude>', 1)[-1].startswith('\n\n'):
                corpo += '\n\n' + t
            else:
                corpo += ('\n' if corpo else '') + t      # parágrafo que continua na página seguinte
        corpo = re.sub(r"'''?", '', corpo)
        corpo = re.sub(r'<[^>]+>', '', corpo)
        paras = []
        for bl in re.split(r'\n\s*\n', corpo):
            bl = bl.strip()
            if not bl:
                continue
            if bl.startswith(VERSO):
                paras.append(VERSO + '\n'.join(x.strip().lstrip(':').strip() for x in bl[1:].split('\n') if x.strip()))
            else:
                paras.append(fontes.limpar(bl.replace('\n', ' ')))
        obra.append({'n': n, 'titulo': tit, 'paras': paras})
    return fontes.normalizar(obra)


def modernas():
    if not _MODERNAS:
        _MODERNAS.update({'ws': wikisource_moderno()})
    return _MODERNAS


# ------------------------------------------------------------------ OCRs da 1ª edição

CABECO = re.compile(r'^[—–\-~_. ]*\d{1,3}[—–\-~_. ]*$|^[—–\-]+$')
# cabeçalhos do livro (MEMÓRIAS DE UM SARGENTO…, CAPITULO N., títulos): linhas sem minúsculas
TITULO_OCR = re.compile(r'^[^a-zà-ÿ]*[A-ZÀ-Ú]{2}[^a-zà-ÿ]*$')


def _juntar(linhas):
    s = ''
    for l in linhas:
        l = l.strip()
        if not l:
            continue
        if re.search(r'[A-Za-zÀ-ÿ][-¬]$', s):
            m = re.match(r"[\w']+", l)
            frag = (m.group(0) if m else '').lower()
            s = (s[:-1] + '-' + l) if frag in fontes.CLITICOS else (s[:-1] + l)
        else:
            s = (s + ' ' + l) if s else l
    return s


def _capitulo_ocr(n, linhas_por_pagina):
    linhas = []
    for pag in linhas_por_pagina:
        pag = [l.strip() for l in pag if l.strip()]
        while pag and CABECO.match(pag[0]):            # número da página no alto
            pag = pag[1:]
        while pag and CABECO.match(pag[-1]):
            pag = pag[:-1]
        pag = [l for l in pag if not TITULO_OCR.match(l)]
        linhas += pag
    texto = _juntar(linhas)
    texto = re.sub(r'\s+([,.;:!?])', r'\1', texto).replace('’', "'")
    return {'n': n, 'titulo': '', 'paras': [fontes.limpar(texto)]}


def _pdf():
    p = fontes.cache(OBRA, 'bbm4846.pdf')
    if not os.path.exists(p):
        from edicao import rede
        rede.baixar(PDF, p, cabecalhos={'User-Agent': 'Mozilla/5.0'})
    return p


def camada():
    """A camada de texto do PDF da Brasiliana, um capítulo por parte (um parágrafo só por capítulo)."""
    txt = fontes.cache(OBRA, 'camada.txt')
    if not os.path.exists(txt):
        subprocess.run(['pdftotext', '-enc', 'UTF-8', _pdf(), txt], check=True)
    pags = open(txt, encoding='utf-8').read().split('\f')          # pags[0] = página 1
    return [_capitulo_ocr(n, [pags[k - 1].split('\n') for k in range(a, b + 1)]) for n, a, b, _ in CAPITULOS]


def djvu():
    """A camada de texto do DjVu do Commons (mesma digitalização da Brasiliana, OCR diferente do do PDF).
    commons.txt: djvutxt --page=N para cada página, separadas por \\f (djvulibre extraído sem sudo em
    ~/.cache/djvu-local/raiz, como o Tesseract)."""
    pags = open(fontes.cache(OBRA, 'commons.txt'), encoding='utf-8').read().split('\f')
    return [_capitulo_ocr(n, [pags[k - 1].split('\n') for k in range(a, b + 1)]) for n, a, b, _ in CAPITULOS]


def tesseract():
    pasta = fontes.cache(OBRA, 'tess-bbm4846')
    por_pagina = {}
    for f in glob.glob(os.path.join(pasta, '*.tsv')):
        linhas = {}
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['level'] != '5' or not (r['text'] or '').strip():
                continue
            k = (int(r['block_num']), int(r['par_num']), int(r['line_num']))
            linhas.setdefault(k, []).append((int(r['top']), int(r['left']), r['text'].strip()))
        ls = sorted(linhas.values(), key=lambda ws: sorted(w[0] for w in ws)[len(ws) // 2])
        por_pagina[int(os.path.basename(f)[:-4])] = [' '.join(w[2] for w in sorted(ws, key=lambda w: w[1])) for ws in ls]
    return [_capitulo_ocr(n, [por_pagina.get(k, []) for k in range(a, b + 1)]) for n, a, b, _ in CAPITULOS]


# ------------------------------------------------------------------ confronto

BASE = 'pdf'
REFERENCIAS = [('ws', False)]
DESEMPATE_LEXICO = True
# as duas camadas (PDF e DjVu) são do mesmo tipo de OCR e erram juntas («linha» por «tinha», «ler» por
# «ter», «eslava», «c» por «e»): correlacionadas, a maioria delas perde para a minoria (o Tesseract) que tem o
# apoio da moderna. Com UM_VOTO = True quase tudo virava empate (3.907 divergências, 2.458 sem maioria)
CORRELACIONADOS = [('pdf', 'dj')]
UM_VOTO = False


def transcricoes():
    """Os dois OCRs de 1854–55, limpos pela edição moderna (só palavras inexistentes) e com a
    divisão dela (parágrafos, versos)."""
    ws = modernas()['ws']
    brutos = {'pdf': camada(), 'dj': djvu(), 'bt': tesseract()}
    # léxico de 1854–55: palavras que os dois programas leram iguais em algum lugar. Sem ele, a guia
    # moderna «corrigia» as formas da época («passavão» -> «passavam», «baptisado» -> «batizado»)
    palavras = [{w for p in o for x in p['paras'] for w in re.findall(r"[A-Za-zÀ-ÿ'-]+", x)} for o in brutos.values()]
    lexico = (palavras[0] & palavras[2]) | (palavras[1] & palavras[2])     # um ABBYY e o Tesseract
    out = {}
    for nome, bruto in brutos.items():
        o, n = ocr.limpar(bruto, [ws], lexico)
        print(f'OCR {nome}: palavras corrigidas pela guia:', n)
        o = ocr.estrutura_como(o, ws)
        for p, b in zip(o, ws):
            p['n'], p['titulo'] = b['n'], b['titulo']
        out[nome] = o
    return out


# ------------------------------------------------------------------ publicação

def agrupar(partes):
    """48 capítulos -> 2 tomos, cada capítulo com «## Capítulo N — título» + «{§ T.c}» no 1º parágrafo."""
    out = []
    for k, nome in enumerate(TOMOS):
        pr = ROM[k]
        caps = [p for p in partes if p['n'].split('.')[0] == pr]
        paras = []
        for c, cap in enumerate(caps, 1):
            rc = cap['n'].split('.')[1]
            paras.append(f'## Capítulo {rc} — {cap["titulo"]}')
            corpo = list(cap['paragrafos'])
            if isinstance(corpo[0], dict):
                raise SystemExit(f'capítulo {cap["n"]} abre com versos')
            corpo[0] = f'{{§ {pr}.{c}}} ' + corpo[0]
            paras += corpo
        out.append({'n': pr, 'titulo': nome, 'paragrafos': paras})
    return out


def rotulos(partes):
    """Lugar de cada correção na página «Sobre»: «tomo I, cap. III»."""
    return ['tomo ' + p['n'].replace('.', ', cap. ', 1) for p in partes]


# ------------------------------------------------------------------ grafia

def modernizar(E, manual):
    """A grafia pela edição moderna (como nas outras obras), com um passo antes: a 3ª pessoa do plural
    em -ão de 1854 («formão», «fechavão», «chegarão» no pretérito) passa a -am onde a moderna, alinhada
    no mesmo ponto, traz a mesma palavra em -am; onde ela traz -ão (o futuro, «chegarão»), fica."""
    from edicao import modernizar as mz
    from edicao.grafia import chave
    from edicao.tokens import achatar, alinhar
    ws = modernas()['ws']
    G = achatar(ws)
    E = list(E)
    # palavras coladas pelos OCRs (o tipo de 1854 é espaçado de modo irregular): «Tinhãoesses»,
    # «emquantoella», «logarvou». Onde a moderna, no mesmo ponto, traz duas ou mais palavras que juntas
    # dão a mesma chave, a palavra se parte nos mesmos comprimentos
    novo, mapa = [], []          # mapa: índice na lista nova -> índice em E (o itálico é indexado por E)
    ops = alinhar(E, G, chave=chave)
    for tp, i1, i2, j1, j2 in ops:
        if tp == 'replace' and i2 - i1 == 1 and 2 <= j2 - j1 <= 6 and isinstance(E[i1], str):
            o, ns = E[i1], G[j1:j2]
            ko = chave(o)
            kn = chave(''.join(ns))
            if all(n[:1].isalpha() for n in ns) and (ko == kn or ko.replace('ao', 'am') == kn.replace('ao', 'am')):
                partes, pos = [], 0
                for n in ns[:-1]:
                    partes.append(o[pos:pos + len(n)]); pos += len(n)
                partes.append(o[pos:])
                if all(partes) and [chave(x) for x in partes][:-1] == [chave(x) for x in ns][:-1]:
                    novo += partes
                    mapa += [i1] * len(partes)
                    continue
        novo += E[i1:i2]
        mapa += list(range(i1, i2))
    print('palavras coladas partidas:', len(novo) - len(E))
    E = novo
    trocas = 0
    for tp, i1, i2, j1, j2 in alinhar(E, G, chave=chave):
        if tp != 'replace' or i2 - i1 != j2 - j1:
            continue
        for k in range(i2 - i1):
            o, n = E[i1 + k], G[j1 + k]
            if not isinstance(o, str):
                continue
            mo = re.match(r'(.+)ão(-\w+)?$', o)          # «formão», «enfurecião-se»
            mn = re.match(r'(.+)am(-\w+)?$', n)
            if mo and mn and len(o) >= 3 and chave(mo.group(1)) == chave(mn.group(1)) and mo.group(2) == mn.group(2):
                E[i1 + k] = mo.group(1) + 'am' + (mo.group(2) or '')
                trocas += 1
    print('3ª do plural em -ão -> -am:', trocas)
    # letras que os três OCRs confundem do mesmo jeito (tipo gasto de 1854): onde todos leem «linha», «ler»,
    # «eslava», «c», «ó» e a moderna traz, no mesmo ponto, a palavra com a letra certa («tinha», «ter»,
    # «estava», «e», «é»), vale a da moderna, na grafia de 1854. A lista vai para relatorios/letras.tsv
    # (conferir uma amostra nas imagens).
    pares = {('l', 't'), ('c', 'e'), ('ó', 'é'), ('b', 'h'), ('o', 'e'), ('i', 't'), ('f', 't'), ('n', 'u'), ('u', 'n')}
    reg = []
    for tp, i1, i2, j1, j2 in alinhar(E, G, chave=chave):
        if tp != 'replace' or i2 - i1 != j2 - j1:
            continue
        for k in range(i2 - i1):
            o, n = E[i1 + k], G[j1 + k]
            if not isinstance(o, str) or not o[:1].isalpha():
                continue
            cands = [o[:x] + b + o[x + 1:] for x in range(len(o)) for a, b in pares if o[x] == a]
            certa = next((c for c in cands if chave(c) == chave(n)), None)
            if certa and (len(o) > 1 or (o, n) in (('c', 'e'), ('ó', 'é'), ('o', 'e'))):
                reg.append((E[max(0, i1 + k - 6):i1 + k], o, certa, E[i1 + k + 1:i1 + k + 6]))
                E[i1 + k] = certa
    print('letras confundidas pelos OCRs, trocadas pela moderna:', len(reg))
    with open(fontes.cache(OBRA, 'relatorios/letras.tsv'), 'w', encoding='utf-8') as f:
        f.write('antes\tOCR\ttroca\tdepois\n')
        for a, o, c, d in reg:
            f.write(f"{' '.join(a)}\t{o}\t{c}\t{' '.join(d)}\n")
    out, origem, rel = mz.modernizar(E, [(n, modernas()[n], pos) for n, pos in REFERENCIAS], manual)
    return out, [mapa[o] for o in origem], rel


if __name__ == '__main__':          # conferência rápida das fontes: palavras por capítulo
    ws, pd, bt = modernas()['ws'], camada(), tesseract()
    tot = [0, 0, 0]
    for a, b, c in zip(ws, pd, bt):
        nums = [sum(len(p.split()) for p in x['paras']) for x in (a, b, c)]
        tot = [t + k for t, k in zip(tot, nums)]
        print(a['n'], len(a['paras']), nums, a['titulo'])
    print('total ws, pdf, bt:', tot)
