"""São Bernardo — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
_M = json.load(open(os.path.join(_AQUI, 'mudancas.json'), encoding='utf-8'))
ERROS_ANTERIORES = [(d['cap'], d['para'], d['texto'].replace('_', '')) for d in _C if d['cod'] == 'erro']

COMENTARIO = '''São Bernardo — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/sao-bernardo/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a terceira edição de _São Bernardo_ (Rio de Janeiro, José Olympio, 1947, segundo volume das _Obras_ de Graciliano Ramos), a última revista pelo autor que hoje se pode ler em fac-símile, digitalizada pela Brasiliana USP. O romance saiu em 1934, pela Ariel, e teve uma segunda edição em 1938, pela José Olympio. Esta não está digitalizada, mas a Brasiliana guarda as provas dela, já na paginação nova, com as correções e anotações à mão do autor.

**O título.** As edições em vida do autor trazem «S. Bernardo», na capa e no texto. Aqui o nome da fazenda vai por extenso, «São Bernardo», como nas edições de hoje; as outras abreviaturas («S. Pedro», «S. João», «d. Glória») ficaram como estão.

**Como foi estabelecido.** O texto de 1947 foi lido duas vezes por reconhecimento automático (OCR): uma vez na camada de texto que vem no fac-símile e outra numa leitura nova, feita para esta edição. As duas leituras foram confrontadas palavra por palavra. Onde divergiam, valeu a que coincide com a primeira edição (1934), estabelecida antes pelo mesmo método, com a transcrição do Wikisource e duas leituras do fac-símile de 1934. Todo ponto em que o resultado diferia de 1934, e todo desempate que 1934 não resolvia, foi conferido nas imagens do fac-símile de 1947: uns quatrocentos e cinquenta pontos, a maior parte erros de leitura das máquinas, corrigidos.

**As mudanças de 1947.** Entre 1934 e 1947 o texto mudou em {len(_M["itens"])} pontos. Há cortes («com um cesto de cajus e uma garrafa» → «com uma garrafa»; «Conforme declarei no princípio do capítulo anterior» → «Conforme declarei»), palavras trocadas («Entretanto em desarticular» → «Entretido em desarticular»; «tinha razão de confiar» → «tinha razão para confiar»), frases refeitas («Naturalmente pede para mandar algum dinheiro» → «Pede-me naturalmente que mande algum dinheiro»), um parágrafo mudado de lugar no capítulo XXX, parágrafos abertos e juntados, travessões e pontuação. Há também formas da época que a edição de 1947 adotou: «Ó» nos vocativos («Oh Padilha» → «Ó Padilha»), «hem» por «hein», «catorze» por «quatorze», «tique-taque», «futebol», «vagão», e as contrações desfeitas (_dum_ → de um, _num_ → em um). A lista completa vai abaixo; ela junta as mudanças de 1938 e as de 1947, porque a segunda edição impressa não está digitalizada. As provas de 1938 mostram que parte delas já estava lá (os cortes «com um cesto de cajus» e «no princípio do capítulo anterior», «Entretido», «lindas mãos»), e que outras só vieram em 1947 (os vocativos com «Ó», «hem», «catorze», «vagão»).

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1947 (lista abaixo), como «padre Sivestre», «Pouco o pouco» e «comer da banda pobre».

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_êle_ → ele, _sôbre_ → sobre, _idéia_ → ideia, _pèssimamente_ → pessimamente, _despedí-lo_ → despedi-lo, _contra-senso_ → contrassenso, _ante-ontem_ → anteontem), com _por que_ e _por quê_ nas perguntas e os nomes de lugar compostos sem hífen (Bom Sucesso, Pão de Açúcar, Ponta da Terra). O vocabulário e as construções do autor ficaram como estão: _capueira_, _de mais_, _choramigar_, _pexote_, _toitiço_, _mil-réis_, as mesóclises, a pontuação e os travessões.

**Divisão.** O livro tem trinta e seis capítulos numerados, sem título; cada um é uma página desta biblioteca.'''

BASE = 'Edição de 1947'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1947 corrigidos',
              'explica': '¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.'},
    'tradicao': {'titulo': 'Mudanças da edição de 1947 sobre a de 1934',
                 'explica': 'Todos os pontos em que o texto de 1947 difere do de 1934, fora a grafia e as '
                            f'{_M["contracoes"]} contrações desfeitas (dum → de um, num → em um). Inclui as mudanças '
                            'da segunda edição (1938). ¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.',
                 'de': '1ª edição (1934)', 'para': '3ª edição (1947)'},
}

FONTES = [
    {'nome': 'Fac-símile da 3ª edição, 1947 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8421',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da 1ª edição, 1934 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8398',
     'nota': 'lido por dois OCRs, para a comparação com 1947'},
    {'nome': 'Wikisource em português: a 1ª edição, 1934', 'url': 'https://pt.wikisource.org/wiki/S._Bernardo_(1934)',
     'nota': 'transcrição página a página, revista até o capítulo XXII'},
    {'nome': 'Provas da 2ª edição, 1938 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8418',
     'nota': 'folhas soltas, com as correções e anotações do autor; lidas por OCR para ver quais mudanças já estavam em 1938'},
]

MANTIDAS = []

TRADICAO_EXTRA = [(x['cap'], x['de'], x['para']) for x in _M['itens']]
