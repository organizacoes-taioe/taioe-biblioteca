"""Memórias de um Sargento de Milícias — texto da página «Sobre esta edição» (RASCUNHO: ver FALTA.md)."""

COMENTARIO = '''Memórias de um Sargento de Milícias — Manuel Antônio de Almeida
   Gerado por ferramentas/texto.py a partir de edicoes/sargento-de-milicias/. Não edite à mão:
   corrija as decisões em edicoes/sargento-de-milicias/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso;
     - «## Capítulo N — título» abre cada capítulo, e «{§ T.c}» marca o seu primeiro parágrafo
       (só para o site dividir as páginas; não aparece no texto).'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição em livro das _Memórias de um Sargento de Milícias_, publicada «por um Brasileiro» no Rio de Janeiro, pela Typographia Brasiliense de Maximiano Gomes Ribeiro, em dois tomos (o primeiro de 1854, o segundo de 1855), a única em vida do autor, morto em 1861. O romance tinha saído antes, sem assinatura, em folhetim na «Pacotilha», o suplemento de domingo do _Correio Mercantil_, entre junho de 1852 e julho de 1853.

**Como foi estabelecido.** Foram confrontadas palavra por palavra duas leituras automáticas (OCR) do exemplar da Brasiliana USP: a que vem no arquivo da biblioteca e uma nova, feita para esta edição. O texto moderno do Wikisource serviu para a divisão em parágrafos e para a grafia; os pontos de dúvida foram conferidos nas imagens do livro.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira (_elle_ → ele, _baptisar_ → batizar, _cousa_ → coisa, _dous_ → dois). O vocabulário e as construções do autor ficaram como estão.

**Divisão.** O romance tem dois tomos, como em 1854–55: o primeiro com 23 capítulos, o segundo com 25, cada um com título; cada capítulo é uma página desta biblioteca.'''

BASE = 'Edição de 1854–55'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1854–55 corrigidos',
              'explica': 'Grafia de 1854–55 nas duas colunas; ¶ marca o começo de um parágrafo.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1854–55, exemplar da Brasiliana USP', 'url': 'https://digital.bbm.usp.br/handle/bbm/4846',
     'nota': 'lido pelo OCR da biblioteca e por um OCR novo (Tesseract); as imagens decidiram as dúvidas'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Mem%C3%B3rias_de_um_Sargento_de_Mil%C3%ADcias',
     'nota': 'texto moderno, posto sobre as páginas do mesmo fac-símile; referência para os parágrafos e a ortografia'},
]

MANTIDAS = []

ERROS_ANTERIORES = []
