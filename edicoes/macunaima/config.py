"""Macunaíma, o herói sem nenhum caráter — fontes (RASCUNHO: ver FALTA.md).

Mário de Andrade (1893–1945). Edições em vida do autor: 1ª, São Paulo, 1928 (edição do autor, 800
exemplares, «Oficinas Gráficas de Eugenio Cupolo»), e 2ª, Rio, José Olympio, 1937, revista (Mário
tirou nela o capítulo XI de 1928, «As tres Normalistas», e mexeu no texto; a confirmar no fac-símile).
Edição-base: a 1ª (1928), a única com fac-símile digitalizado e transcrição (a de 1937 não está no
Wikisource nem na Brasiliana, até onde se viu em 2026-11-02). Ela tem 18 capítulos e o epílogo.

Testemunhos:
- 'ws': o Wikisource, «Macunaíma (1928).pdf», página a página (o mesmo exemplar da BN). Revisadas
  (nível 3/4) as páginas dos caps. I, XII–XVIII e epílogo; as dos caps. II–XI (pp. 19–165) estão
  no nível 1 (OCR de robô, «Giro bot», não revisado). É a base: guarda a grafia do impresso
  (heroi, tambem, familia), que o ABBYY do IA «corrige» sozinho (herói, também).
- 'ia': a camada de texto (ABBYY) do fac-símile da Biblioteca Nacional no Internet Archive
  (or182096, 1928), com a divisão dada pela base (ocr.estrutura_como).
Sem edição moderna de referência: a grafia de hoje sai de modernizar() (ver CONVENCOES.md).
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao import fontes, ocr  # noqa: E402

OBRA = 'macunaima'

META = {
    'id': OBRA,
    'autor': 'mario-de-andrade',
    'titulo': 'Macunaíma',
    'subtitulo': 'o herói sem nenhum caráter',
    'ano': 1928,
    'genero': 'Rapsódia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'descricao': 'A «rapsódia» de 1928, o herói da nossa gente do Uraricoera a São Paulo e de volta.',
}

REFERENCIAS = []
CORRELACIONADOS = []

ARQUIVO_WS = 'Macunaíma (1928).pdf'
IA = ('or182096', 'or182096_djvu.txt')

# o índice de 1928 (p. 286 do PDF): número, título, página de abertura
CAPITULOS = [('I', 'Macunaíma'), ('II', 'Maioridade'), ('III', 'Ci, Mãi do Mato'), ('IV', 'Boiuna Luna'),
             ('V', 'Piaimã'), ('VI', 'A francesa e o gigante'), ('VII', 'Macumba'), ('VIII', 'Vei, a Sol'),
             ('IX', 'Carta pras Icamiabas'), ('X', 'Pauí-Pódole'), ('XI', 'As tres Normalistas'),
             ('XII', 'A velha Ceiucí'), ('XIII', 'Teque-teque, Chupinzão e a Injustiça dos Homens'),
             ('XIV', 'A piolhenta do Jiguê'), ('XV', 'Muiraquitã'), ('XVI', 'A pacuera de Oibê'),
             ('XVII', 'Uraricoera'), ('XVIII', 'Ursa Maior'), ('Epílogo', '')]

CAB = r'(?s)^(?P<n>[IVXLC]+|EP[IÍ]LOGO)\b.*$'


def _ws():
    """O Wikisource em capítulos. O cabeçalho centrado traz número e título juntos («XII\\n\\nA VELHA
    CEIUCÍ»); o leitor comum pega o número, e o título vem do índice. No XIII o cabeçalho vem noutro
    formato e precisa de conserto (FALTA.md)."""
    o = fontes.wikisource(OBRA, ARQUIVO_WS, 7, 283, rom=CAB)
    titulos = dict(CAPITULOS)
    for i, c in enumerate(list(o)):             # o cabeçalho do XIII passa de 40 letras e fica no XII
        for j, p in enumerate(c['paras']):
            if re.match(r'^\W*XIII\n', p):
                o.insert(o.index(c) + 1, {'n': 'XIII', 'titulo': '', 'paras': c['paras'][j + 1:]})
                del c['paras'][j:]
                break
    for c in o:
        if c['n'].upper().startswith('EP'):
            c['paras'].insert(0, c['titulo'])   # «Acabou-se a história e morreu a vitória.»
            c['n'], c['titulo'] = 'Epílogo', ''
        else:
            if c['titulo']:                     # o leitor tomou a 1ª frase curta por título: devolver
                c['paras'].insert(0, c['titulo'])
            c['titulo'] = titulos.get(c['n'], '')
    return o


_LIXO = re.compile(r'^(?:\d+|MARIO DE ANDRADE|MACUNA[IÍ]MA|[IVXLC]+)$')


def _ia():
    """O OCR do IA como uma parte só, em parágrafos pelas linhas em branco, sem cabeços nem números
    de página; a divisão em capítulos e parágrafos vem da base (ocr.estrutura_como)."""
    s = fontes.internet_archive(OBRA, *IA)
    s = s[s.index('No fundo do mato-virgem'):s.rindex('ESTA EDIÇÃO')]
    titulos = {fontes.nfc(t).upper() for _, t in CAPITULOS if t}
    paras, atual = [], ''
    for bloco in re.split(r'\n\s*\n', s):
        linhas = [l.strip() for l in bloco.split('\n') if l.strip()]
        if not linhas or (len(linhas) == 1 and (_LIXO.match(linhas[0]) or linhas[0].upper() in titulos)):
            continue
        t = ''
        for l in linhas:
            if t.endswith('¬') or (re.search(r'[a-zà-ÿ]-$', t) and re.match(r'[a-zà-ÿ]', l)):
                t = t[:-1] + l                  # palavra partida no fim da linha (A CONFERIR: compostos)
            else:
                t = (t + ' ' + l).strip()
        paras.append(fontes.limpar(t))
    return fontes.normalizar([{'n': 'I', 'titulo': '', 'paras': paras}])


# Capítulos em que o Wikisource ainda está no nível 1: ali o texto dele NÃO é o de 1928 (frecha →
# flecha, tribu → tribo, pra → para, poude → pôde…; parece colado de uma edição posterior, revista e
# modernizada), e o testemunho de 1928 é só o OCR do IA. Ver FALTA.md.
DO_OCR = ['II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
BASE = 'b28'


TESS = os.path.join(AQUI, '..', '..', 'ferramentas', 'cache', OBRA, 'tess')   # <pdf-página>.txt
_RUIDO = re.compile(r'^(?:[^\wÀ-ÿ]{1,3}|[A-ZÀ-Ý0-9][^\w\s]?|[a-zà-ÿ][;:,.]?|\d+)$')


def _tess():
    """O Tesseract (por, --psm 6) das páginas do fac-símile do IA, a 300 dpi (FALTA.md: o comando).
    A lombada e a borda da página viram letras soltas no começo e no fim da linha: saem aqui; o resto
    do ruído perde no voto. Uma parte só; a divisão vem da base (ocr.estrutura_como)."""
    import glob
    linhas = []
    for arq in sorted(glob.glob(os.path.join(TESS, '*.txt'))):
        for l in open(arq, encoding='utf-8'):
            w = l.split()
            while w and _RUIDO.match(w[-1]) and w[-1] not in ('e', 'é', 'a', 'à', 'o', 'E', 'A', 'O', 'É', '—'):
                w.pop()
            while w and _RUIDO.match(w[0]) and w[0] not in ('e', 'é', 'a', 'à', 'o', 'E', 'A', 'O', 'É', '—', '—'):
                w.pop(0)
            l = ' '.join(w)
            if not l or re.fullmatch(r'(?:\d+\s*)?(?:MARIO DE ANDRADE|MACUNA[IÍ]MA)(?:\s*\d+)?', l):
                continue
            linhas.append(l)
    s = '\n'.join(linhas)
    s = s[s.index('No fundo do mato-virgem'):]
    s = s.split('ESTA EDIÇÃO')[0]
    s = re.sub(r'([a-zà-ÿ])[-¬]\n(?=[a-zà-ÿ])', r'\1', s)
    return fontes.normalizar([{'n': 'I', 'titulo': '', 'paras': [fontes.limpar(s.replace('\n', ' '))]}])


def transcricoes():
    """'b28': o texto de 1928 montado capítulo a capítulo (Wikisource revisado onde há; OCR do IA nos
    capítulos de DO_OCR). 'ws': o Wikisource inteiro, só para apontar, nos capítulos do OCR, as
    palavras a conferir no fac-símile (sitios.tsv): no voto de dois, vale sempre a base."""
    ws = _ws()
    ia = ocr.estrutura_como(_ia(), ws)
    b28 = [dict(i, n=w['n'], titulo=w['titulo']) if w['n'] in DO_OCR else w for w, i in zip(ws, ia)]
    out = {'b28': b28, 'ws': ws}
    if os.path.isdir(TESS):
        t = ocr.estrutura_como(_tess(), ws)
        out['t28'] = [dict(x, n=w['n'], titulo=w['titulo']) if w['n'] in DO_OCR else w for w, x in zip(ws, t)]
    return out


def modernas():
    return {}


def modernizar(E, manual):
    """A FAZER (FALTA.md): grafia de 1928 -> Acordo de 1990 só no que não é escolha do autor
    (CONVENCOES.md). Por ora, a palavra fica como está, para os relatórios."""
    from edicao.tokens import e_palavra  # noqa: F401
    out = [manual.get(t, t) for t in E]
    return out, list(range(len(E))), []
