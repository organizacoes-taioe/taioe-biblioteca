"""Caetés — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
_ARQ_M = os.path.join(_AQUI, 'mudancas.json')
_M = json.load(open(_ARQ_M, encoding='utf-8')) if os.path.exists(_ARQ_M) else {'itens': [], 'contracoes': 0, 'exemplos': ''}
ERROS_ANTERIORES = [(d['cap'], d['para'], d['texto'].replace('_', '')) for d in _C if d['cod'] == 'erro']
_N_CONF = sum(1 for d in _C if d['cod'] != 'ver')

COMENTARIO = '''Caetés — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/caetes/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a segunda edição de _Caetés_ (Rio de Janeiro, José Olympio, 1947, primeiro volume das _Obras_ de Graciliano Ramos), a última publicada em vida do autor, digitalizada pela Brasiliana USP em três exemplares. O romance, o primeiro de Graciliano, saiu em 1933, pela Schmidt, com o título _Cahetés_. O volume de 1947 abre com um ensaio de Floriano Gonçalves, que não é do autor e fica de fora.

**Como foi estabelecido.** Não há edição moderna gratuita do livro. O texto de 1947 foi lido cinco vezes por reconhecimento automático (OCR): as camadas de texto que vêm nos três exemplares digitalizados e duas leituras novas, feitas para esta edição. As cinco leituras foram confrontadas palavra por palavra, e valeu a maioria. Os pontos em que não houve maioria, ou em que a leitura podia esconder um erro (acentos, palavras raras), foram conferidos um a um nas imagens do livro: {_N_CONF} pontos.

**As mudanças de 1947.** O romance saiu em 1933 como _Cahetés_; em 1947 o título passou a _Caetés_, e o texto mudou pouco e em detalhes. Há cortes («que escândalo! Misericórdia!» → «que escândalo!»; «Tem razão, é claro, tem toda a razão» → «Tem razão»; «eu experimentava um grande» → «eu experimentava grande»), o «Oh» das falas virou «Ó» («Oh Pinheiro» → «Ó Pinheiro»), «quatorze» virou «catorze», e algumas palavras foram trocadas («Brava rapariga!» → «Corajosa.»; «Eu também não sabia» → «Eu também ignorava»; «montanhas circumdam» → «montanhas circulam»). A lista abaixo traz as {len(_M["itens"])} mudanças de palavras em que as três leituras de 1933 (dois exemplares, dois programas de OCR) concordam; as de pontuação e de parágrafos ficaram de fora, porque nesses pontos a leitura automática de 1933 não é segura, e também os erros tipográficos de 1933 que 1947 corrigiu.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1947 (lista abaixo).

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_êle_ → ele, _sôbre_ → sobre, _idéia_ → ideia, _quási_ → quase), com _por que_ e _por quê_ nas perguntas. O vocabulário, a pontuação e as formas do autor ficaram como estão.

**Divisão.** O livro tem trinta e um capítulos numerados, sem título; cada um é uma página desta biblioteca.'''

BASE = 'Edição de 1947'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1947 corrigidos',
              'explica': '¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.'},
    'tradicao': {'titulo': 'Mudanças da edição de 1947 sobre a de 1933',
                 'explica': 'Os pontos em que o texto de 1947 difere do de 1933, fora a grafia'
                            + (f' e as {_M["contracoes"]} contrações desfeitas (dum → de um, num → em um)' if _M['contracoes'] else '')
                            + '. ¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.',
                 'de': '1ª edição (1933)', 'para': '2ª edição (1947)'},
}

FONTES = [
    {'nome': 'Fac-símile da 2ª edição, 1947, exemplar 3 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8819',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da 2ª edição, 1947, exemplar 1 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8374',
     'nota': 'lido por dois OCRs'},
    {'nome': 'Fac-símile da 2ª edição, 1947, exemplar 2 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8485',
     'nota': 'a camada de texto do fac-símile'},
    {'nome': 'Fac-símile da 1ª edição, 1933, _Cahetés_ (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8400',
     'nota': 'lido por OCR, para a comparação com 1947'},
]

MANTIDAS = []

TRADICAO_EXTRA = [(x['cap'], x['de'], x['para']) for x in _M['itens']]
