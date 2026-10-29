"""Histórias sem Data — fontes.

Coletânea de contos (Rio de Janeiro, B. L. Garnier, 1884; impressa por Lombaerts), única edição
em vida do autor. Testemunhos de 1884: Projeto Gutenberg 33056 (transcrição de Pedro Saborano; o
Wikisource tem o mesmo texto, posto lá por robô, e não conta como testemunho) e dois OCRs do
exemplar da Universidade de Toronto no Internet Archive (historiassemdata00machuoft): a camada de
texto do PDF (ABBYY antigo, sem acentos) e um Tesseract nosso (`tesseract.py`). Os dois OCRs leem
as mesmas imagens com programas diferentes: cada um vota. Modernas: machadodeassis.net (conto a
conto), Aguilar (MEC / Domínio Público), Objetivo (outra digitação do Aguilar).

Como em Papéis Avulsos, a coletânea é estabelecida inteira e publicada conto a conto (CONTOS). O
livro não tem notas do autor (NOTAS = None). Traz uma errata, aplicada em decisoes.EMENDAS.
"""
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao import fontes, rede  # noqa: E402
from edicao.ocr import estrutura_como, limpar as limpar_ocr  # noqa: E402
from edicao.tokens import VERSO  # noqa: E402

OBRA = 'historias-sem-data'

META = {
    'id': OBRA,
    'autor': 'machado-de-assis',
    'titulo': 'Histórias sem Data',
    'ano': 1884,
    'genero': 'Contos',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
}

# Na ordem do livro. 'pg': título no Gutenberg; 'mdn': (slug, id) no machadodeassis.net;
# 'publicacao': primeira publicação, pelos dados do machadodeassis.net. «A Igreja do Diabo»: lá,
# 12 de fevereiro de 1883; Daniela Magalhães da Silveira (Fábrica de contos, 2010, e ANPUH 2011),
# que leu a Gazeta, e a Wikipédia dão 17 de fevereiro, que fica.
CONTOS = [
    {'id': 'historias-sem-data-advertencia', 'titulo': 'Advertência', 'pg': 'ADVERTENCIA', 'paratexto': True,
     'mdn': ('historias-sem-data', 28928), 'publicacao': ''},
    {'id': 'a-igreja-do-diabo', 'titulo': 'A Igreja do Diabo', 'pg': 'A EGREJA DO DIABO',
     'mdn': ('a-igreja-do-diabo', 28933), 'capitulos': True,
     'publicacao': '_Gazeta de Notícias_, 17 de fevereiro de 1883'},
    {'id': 'o-lapso', 'titulo': 'O Lapso', 'pg': 'O LAPSO', 'mdn': ('o-lapso', 29028),
     'publicacao': '_Gazeta de Notícias_, 17 de abril de 1883'},
    {'id': 'ultimo-capitulo', 'titulo': 'Último Capítulo', 'pg': 'ULTIMO CAPITULO', 'mdn': ('ultimo-capitulo', 29108),
     'publicacao': '_Gazeta de Notícias_, 20 de junho de 1883'},
    {'id': 'cantiga-de-esponsais', 'titulo': 'Cantiga de Esponsais', 'pg': 'CANTIGA DE ESPONSAES',
     'mdn': ('cantiga-de-esponsais', 29145), 'publicacao': '_A Estação_, 15 de maio de 1883'},
    {'id': 'singular-ocorrencia', 'titulo': 'Singular Ocorrência', 'pg': 'SINGULAR OCCURRENCIA',
     'mdn': ('singular-ocorrencia', 29187), 'publicacao': '_Gazeta de Notícias_, 30 de maio de 1883'},
    {'id': 'galeria-postuma', 'titulo': 'Galeria Póstuma', 'pg': 'GALERIA POSTHUMA', 'mdn': ('galeria-postuma', 29278),
     'capitulos': True, 'publicacao': '_Gazeta de Notícias_, 2 de agosto de 1883'},
    {'id': 'capitulo-dos-chapeus', 'titulo': 'Capítulo dos Chapéus', 'pg': 'CAPITULO DOS CHAPÉOS',
     'mdn': ('capitulo-dos-chapeus', 29341),
     'publicacao': '_A Estação_, 15 e 31 de agosto e 15 de setembro de 1883'},
    {'id': 'conto-alexandrino', 'titulo': 'Conto Alexandrino', 'pg': 'CONTO ALEXANDRINO',
     'mdn': ('conto-alexandrino', 29481), 'capitulos': True, 'publicacao': '_Gazeta de Notícias_, 13 de maio de 1883'},
    {'id': 'primas-de-sapucaia', 'titulo': 'Primas de Sapucaia!', 'pg': 'PRIMAS DE SAPUCAIA!',
     'mdn': ('primas-de-sapucaia', 29577), 'publicacao': '_Gazeta de Notícias_, 24 de outubro de 1883'},
    {'id': 'uma-senhora', 'titulo': 'Uma Senhora', 'pg': 'UMA SENHORA.', 'mdn': ('uma-senhora', 29661),
     'publicacao': '_Gazeta de Notícias_, 27 de novembro de 1883'},
    {'id': 'anedota-pecuniaria', 'titulo': 'Anedota Pecuniária', 'pg': 'ANECDOTA PECUNIARIA',
     'mdn': ('anedota-pecuniaria', 29712), 'publicacao': '_Gazeta de Notícias_, 6 de outubro de 1883'},
    {'id': 'fulano', 'titulo': 'Fulano', 'pg': 'FULANO', 'mdn': ('fulano', 29803),
     'publicacao': '_Gazeta de Notícias_, 4 de janeiro de 1884'},
    {'id': 'a-segunda-vida', 'titulo': 'A Segunda Vida', 'pg': 'A SEGUNDA VIDA', 'mdn': ('a-segunda-vida', 29867),
     'publicacao': '_Gazeta Literária_, 15 de janeiro de 1884'},
    {'id': 'noite-de-almirante', 'titulo': 'Noite de Almirante', 'pg': 'NOITE DE ALMIRANTE',
     'mdn': ('noite-de-almirante', 29931), 'publicacao': '_Gazeta de Notícias_, 10 de fevereiro de 1884'},
    {'id': 'manuscrito-de-um-sacristao', 'titulo': 'Manuscrito de um Sacristão', 'pg': 'MANUSCRITO DE UM SACHRISTÃO',
     'mdn': ('manuscrito-de-um-sacristao', 30015), 'capitulos': True,
     'publicacao': '_Gazeta de Notícias_, 17 de fevereiro de 1884'},
    {'id': 'ex-cathedra', 'titulo': 'Ex Cathedra', 'pg': 'EX CATHEDRA', 'mdn': ('ex-cathedra', 30104),
     'publicacao': '_Gazeta de Notícias_, 8 de abril de 1884'},
    {'id': 'a-senhora-do-galvao', 'titulo': 'A Senhora do Galvão', 'pg': 'A SENHORA DO GALVÃO',
     'mdn': ('a-senhora-do-galvao', 30179), 'publicacao': '_Gazeta de Notícias_, 14 de maio de 1884'},
    {'id': 'as-academias-de-siao', 'titulo': 'As Academias de Sião', 'pg': 'AS ACADEMIAS DE SIÃO',
     'mdn': ('as-academias-de-siao', 30261), 'capitulos': True,
     'publicacao': '_Gazeta de Notícias_, 6 de junho de 1884'},
]
NOTAS = None

BASE = 'pg'
CORRELACIONADOS = [('pg', 'ocr')]   # o Gutenberg saiu da camada de texto do Internet Archive (erros comuns: telus, tornados, via)
UM_VOTO = True
DESEMPATE_LEXICO = True
REFERENCIAS = [('mdn', True), ('mec', False)]

PDF_TORONTO = 'https://archive.org/download/historiassemdata00machuoft/historiassemdata00machuoft.pdf'
CAPITULO = re.compile(r'^(?:CAPITULO )?(?P<n>[IVXL]+)\.?$')
FIM = re.compile(r'^FIM D[AEO]S? ')


# Lugares em que o Gutenberg emendou o impresso sem dizer (as três primeiras emendas da errata do
# livro e erros evidentes, todos conferidos no fac-símile): volta a leitura de 1884, para que a
# correção se registre em decisoes.EMENDAS e apareça na página «Sobre».
IMPRESSO = [
    ('mandei-lhe coser as mais', 'mandei-lhe coser-lhe as mais'),           # errata, p. 43
    ('estar a contar-lhe tudo', 'estar-lhe a contar tudo'),                 # errata, p. 182
    ('que lhe deram a força', 'que deram a força'),                         # errata, p. 211
    ('e as boas acções', 'e ao boas acções'),
    ('dois mezes na côrte', 'dois mezes no côrte'),
    ('os que não a conheciam', 'os que não e conheciam'),
    ('Foi fallar ás duas', 'Foi fallar á duas'),
    ('Desde esse dia começou', 'Desse esse dia começou'),
    ('tal era o motivo', 'tal era o o motivo'),
]


def pg():
    """Unidades do livro no Gutenberg. As epígrafes (blocos recuados) viram um bloco de linhas."""
    bruto = rede.baixar('https://www.gutenberg.org/cache/epub/33056/pg33056.txt',
                        fontes.cache(OBRA, 'pg33056.txt')).decode('utf-8').replace('\r', '')
    s = bruto.split('*** START OF THE PROJECT GUTENBERG EBOOK', 1)[1].split('*** END OF THE PROJECT')[0]
    s = s[s.index('\nADVERTENCIA\n'):].replace('--', '—').replace('\xad', '')
    titulos = {c['pg']: c for c in CONTOS}
    obra, atual, unidade, espera_tit, epigrafe, usados = [], None, None, False, [], set()

    def fecha_epigrafe():
        if epigrafe:
            atual['paras'].append(VERSO + '\n'.join(epigrafe))
            epigrafe.clear()

    for bloco in re.split(r'\n\s*\n', s):
        b = bloco.strip()
        if not b:
            continue
        if b in titulos:
            atual = {'n': '', 'titulo': b.rstrip('.'), 'paras': []}   # o título alinha com o dos OCRs
            obra.append(atual)
            unidade, espera_tit = titulos[b], False
            continue
        if FIM.match(b):
            continue
        linhas = [l for l in bloco.split('\n') if l.strip()]
        if unidade['id'] != 'historias-sem-data-advertencia' and all(l.startswith('    ') for l in linhas):
            epigrafe.append(' '.join(l.strip() for l in linhas))
            continue
        fecha_epigrafe()
        m = CAPITULO.match(b) if unidade.get('capitulos') else None
        if m:
            atual = {'n': m.group('n'), 'titulo': '', 'paras': []}
            obra.append(atual)
            espera_tit = True
            continue
        if espera_tit and b == b.upper() and len(b) < 90:
            atual['titulo'] = b
            espera_tit = False
            continue
        espera_tit = False
        par = fontes.limpar(' '.join(l.strip() for l in linhas))
        for a, b in IMPRESSO:
            if a in par:
                par = par.replace(a, b)
                usados.add(a)
        atual['paras'].append(par)
    fecha_epigrafe()
    falta = [a for a, _ in IMPRESSO if a not in usados]
    if falta:
        raise SystemExit(f'IMPRESSO sem efeito: {falta}')
    return fontes.normalizar(obra)


def _corrido(texto_):
    return [{'n': '0', 'titulo': '', 'paras': [p for p in re.split(r'\n\s*\n', texto_) if p.strip()]}]


CABECO = re.compile(r'^\W*(\d+\W*)?[A-ZÀ-Ý0-9 .,\'!’:;—-]{6,}?(\W*\d+)?\W*$')


def _paginas_corridas(paginas):
    """Páginas de OCR -> texto corrido: tira o cabeço (título corrente com o número da página) e
    os números soltos, desfaz a divisão silábica do fim da linha."""
    linhas = []
    for pag in paginas:
        ls = [l.strip() for l in pag.split('\n') if l.strip()]
        if ls and re.search(r'\d', ls[0]) and CABECO.match(ls[0]) and len(ls[0]) < 50:
            ls = ls[1:]
        elif ls and ls[0].replace(' ', '').upper() == 'HISTORIASSEMDATA':
            ls = ls[1:]
        ls = [l for l in ls if not re.fullmatch(r'[\divxlcIVXLC.,\'’ ]{1,8}', l)]
        # «FIM DA ...» e «CAPITULO II»: a base não os tem (o capítulo é marca de parte)
        ls = [l for l in ls if not re.match(r'^\W*[FP]I[MN]\s+(D|1\))', l) and not re.match(r'^CAP[I1l]T[UV][LI1][O0]\W*\s*\S{0,6}$', l)]
        if sum(len(re.findall(r'[A-Za-zÀ-ÿ]{3,}', l)) >= 3 for l in ls) < 2:     # página em branco: só sujeira
            continue
        linhas += ls
    t = ''
    for l in linhas:
        if re.search(r'\w[-¬]$', t) and not t.endswith('--'):
            t = fontes._juntar_hifen(t, l)
        else:
            t += (' ' if t else '') + l
    t = re.sub(r'\s+', ' ', t)
    fim = t.rfind('Changai, China')           # as últimas palavras do livro; depois, só a ficha da biblioteca
    return t[:fim + 15] if fim > 0 else t


def _corte_inicio(t, marca):
    i = t.find(marca)
    return t[i:] if i >= 0 else t


def ocr_abbyy(base, guias):
    pdf = fontes.cache(OBRA, 'ia_toronto.pdf')
    txt = fontes.cache(OBRA, 'ia_toronto_raw.txt')
    if not os.path.exists(txt):
        rede.baixar(PDF_TORONTO, pdf)
        subprocess.run(['pdftotext', '-raw', '-enc', 'UTF-8', pdf, txt], check=True)   # sem -raw, a ordem das palavras se embaralha
    pags = open(txt, encoding='utf-8').read().split('\f')
    t = _paginas_corridas(pags)
    t = t[t.index('ADVERTENCIA De'):] if 'ADVERTENCIA De' in t else _corte_inicio(t, 'ADVERTENCIA')
    obra, n = limpar_ocr([{'n': '0', 'titulo': '', 'paras': [t]}], guias)
    print('OCR ABBYY (Toronto): palavras corrigidas pelas guias:', n)
    return estrutura_como(obra, base)


def ocr_tesseract(base, guias):
    arqs = sorted(glob.glob(fontes.cache(OBRA, os.path.join('tess', '*.txt'))))
    if not arqs:
        raise SystemExit('rode antes: python3 edicoes/historias-sem-data/tesseract.py')
    t = _paginas_corridas(open(a, encoding='utf-8').read() for a in arqs)
    i = t.find('ADVERTENCIA', t.find('ERRATA'))
    t = t[i:]
    obra, n = limpar_ocr([{'n': '0', 'titulo': '', 'paras': [t]}], guias)
    print('OCR Tesseract (Toronto): palavras corrigidas pelas guias:', n)
    return estrutura_como(obra, base)


def _mec_corrido():
    mec = open(fontes.cache(OBRA, 'ia_historiasSemData.txt'), encoding='utf-8').read() \
        if os.path.exists(fontes.cache(OBRA, 'ia_historiasSemData.txt')) else \
        fontes.internet_archive(OBRA, 'historiasSemData', 'historiasSemData.pdf')
    mec = mec.replace('\f', '\n')
    i = mec.index('ADVERTÊNCIA DA 1', mec.index('ADVERTÊNCIA DA 1') + 5)
    return _corrido(mec[i:].replace('\n', '\n\n'))


def _mdn_corrido():
    paras = []
    for c in CONTOS:
        for p in fontes.machadodeassis_net(OBRA, *c['mdn']):
            for x in (p['n'], p['titulo']):
                x = re.sub(r'^CAPÍTULO\s+', '', x or '', flags=re.I).strip()
                if x and not re.fullmatch(r'b\d+-s\d+-c\d+', x):
                    paras.append(x)
            paras += p['paras']
    return [{'n': '0', 'titulo': '', 'paras': paras}]


def transcricoes():
    base = pg()
    guias = [base, _mdn_corrido()]
    return {'pg': base, 'ocr': ocr_abbyy(base, guias), 'tess': ocr_tesseract(base, guias)}


def modernas():
    base = pg()
    nup = fontes.pdf_texto(OBRA, 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/'
                           'machado-de-assis/historias-sem-data.pdf', 'nupill').replace('\f', '\n')
    nup = nup[nup.index('ADVERTÊNCIA DA 1'):]
    return {
        'mdn': estrutura_como(_mdn_corrido(), base),
        'mec': estrutura_como(_mec_corrido(), base),
        'nup': estrutura_como(_corrido(nup.replace('\n', '\n\n')), base),
    }
