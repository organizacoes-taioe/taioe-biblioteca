"""Cartas do Brasil de Nóbrega — grava conteudo/manuel-da-nobrega/cartas-do-brasil.js (chamado por montar.py --publicar).

Uma parte por carta, com o número do volume de 1886 e a data e o lugar no título.
"""
import json
import os
import re


AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'manuel-da-nobrega', 'cartas-do-brasil.js')

APRESENTACAO = """**Texto-base.** Esta edição reproduz as cartas em português de Manuel da Nóbrega (1517–1570) do volume _Cartas do Brasil do padre Manoel da Nobrega (1549–1560)_, organizado e anotado por Alfredo do Valle Cabral (Rio de Janeiro, Imprensa Nacional, 1886; tomo I das _Cartas jesuíticas_), pelo fac-símile da Biblioteca Brasiliana Guita e José Mindlin (USP). Valle Cabral reuniu 21 cartas, impressas antes em separado, e conferiu umas com a cópia manuscrita e o original da Biblioteca Nacional, outras com as cópias de Évora e da Torre do Tombo; as que não têm data ele situou pelo contexto. A seleção traz as 19 cartas que Nóbrega escreveu em português; as duas que o editor traduziu do italiano (a carta de 10 de agosto de 1549 ao doutor Navarro e a de Porto Seguro, de 6 de janeiro de 1550, de que não se conhece o original português) ficaram de fora. As cartas vão na ordem e com a numeração do volume (I a XXI, sem IV e VI). O _Diálogo sobre a conversão do gentio_ e as cartas de 1561 a 1570 não estão neste volume e não entram aqui.

**Como foi estabelecido.** O texto saiu de leituras por OCR do fac-símile (a máscara de texto do PDF a 900 dpi, lida a 450 e a 600 dpi com o Tesseract, mais a camada de texto do próprio PDF, com votação palavra por palavra), e todas as linhas e trechos suspeitos foram conferidos nas imagens das páginas. Ficaram de fora o título, o sumário e as notas de Valle Cabral, que são dele e não de Nóbrega, e o cabeçalho corrente. Onde o exemplar está danificado e a leitura é conjectura, o texto segue a melhor leitura; uma palavra ilegível no fim da carta XX vem como «[…]». A edição crítica moderna (Serafim Leite, _Monumenta Brasiliae_, 1956–1960) é protegida por direitos autorais e não foi usada.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem das frases do impresso: cousa → coisa, sinão → senão, dous → dois, charidade → caridade, similhante → semelhante, deante → diante, hontem → ontem, creança → criança, baptismo → batismo, accrescentar → acrescentar, imigo → inimigo, e assim por diante. Valle Cabral já grafou o texto à maneira de 1886 (Christo, nella, fructo, tambem); a de 1886 é que está atualizada aqui. O «à» do impresso, que ele usa também para a preposição simples, vai como «a» diante de infinitivo, de pronome de tratamento e de palavra masculina («a saber», «a Vossa Alteza»), e como crase nos demais casos. As mesóclises de Nóbrega ficam (far-se-á, fá-lo-á). Ficam como estão os nomes de povos e de lugares indígenas (Tupiniquins, Carijós, Tapariqua, Mirangaoba), e as formas de Nóbrega que ainda se dicionarizam (mantença, dextra, imos, entonces, valhacouto). Os trechos em latim vão em itálico e sem mudança. Chamadas de nota do editor («12)») saíram do texto. A pontuação e as maiúsculas são as do impresso, salvo pontos evidentes de composição."""

FONTES = [
    {'nome': 'Cartas do Brasil do padre Manoel da Nobrega (1549–1560), org. Alfredo do Valle Cabral. Rio de Janeiro: Imprensa Nacional, 1886; exemplar da Biblioteca Brasiliana Guita e José Mindlin (USP, fac-símile)',
     'url': 'https://digital.bbm.usp.br/handle/bbm/8016', 'nota': 'texto-base, pp. 47–176'},
    {'nome': 'O mesmo volume, no Internet Archive (cópia da Biblioteca Nacional)',
     'url': 'https://archive.org/details/cartaaaapdrmnelnobrg', 'nota': 'conferência de leituras'},
]


def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def gravar(cs):
    blocos = []
    for c in cs:
        corpo = list(c['pars_m'])
        blocos.append({'n': c['n'], 'titulo': f'{c["titulo"]} ({c["local"]})', 'texto': '\n\n'.join(corpo)})
    edicao = {'base': '1886', 'apresentacao': APRESENTACAO, 'fontes': FONTES}
    meta = {
        'id': 'cartas-do-brasil', 'autor': 'manuel-da-nobrega', 'titulo': 'Cartas do Brasil (seleção)',
        'ano': 1549, 'genero': 'Cartas',
        'divisao': {'singular': 'carta', 'plural': 'cartas', 'rotulo': 'nome', 'marcas': False},
        'descricao': 'Dezenove cartas do primeiro provincial jesuíta do Brasil, de 1549 a 1560: a chegada à Bahia, os índios, os colonos, São Vicente e Piratininga.',
    }
    linhas = ['/* Cartas do Brasil (seleção) — Manuel da Nóbrega',
              '   Gerado por edicoes/cartas-nobrega/montar.py --publicar a partir de edicoes/cartas-nobrega/1886/.',
              '   Não edite à mão: corrija as decisões em edicoes/cartas-nobrega/ e rode de novo. */',
              'BIBLIOTECA.obra({']
    for chave, v in meta.items():
        linhas.append(f'  {chave}: {json.dumps(v, ensure_ascii=False)},')
    linhas.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    linhas.append('  partes: [')
    for i, b in enumerate(blocos):
        fim = ',' if i + 1 < len(blocos) else ''
        linhas.append(f'    {{ n: {json.dumps(b["n"])}, titulo: {json.dumps(b["titulo"], ensure_ascii=False)}, texto: `{js_texto(b["texto"])}` }}{fim}')
    linhas.append('  ]')
    linhas.append('});')
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ), sum(len(re.findall(r'\w+', b['texto'])) for b in blocos), 'palavras')
    idx = os.path.join(RAIZ, 'index.html')
    h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/manuel-da-nobrega/cartas-do-brasil.js"></script>'
    if linha not in h:
        h = h.replace('</head>', linha + '\n</head>', 1)
        open(idx, 'w', encoding='utf-8').write(h)
