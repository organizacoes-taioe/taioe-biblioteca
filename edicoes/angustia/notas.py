"""Angústia — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
ERROS_ANTERIORES = [(d['cap'], d['para'], d['texto'].replace('_', '')) for d in _C if d['cod'] == 'erro']

COMENTARIO = '''Angústia — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/angustia/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a terceira edição de _Angústia_ (Rio de Janeiro, José Olympio, 1947, terceiro volume das _Obras_ de Graciliano Ramos), a última revista pelo autor, digitalizada pela Brasiliana USP. O romance saiu em 1936, pela José Olympio, e teve uma segunda edição em 1941, pela mesma casa; nenhuma das duas está digitalizada.

**As provas de 1946.** A Brasiliana guarda também as provas desta terceira edição, em folhas soltas, com as correções à mão do autor. Elas mostram o livro já composto e cheio de erros de composição: linhas trocadas de lugar ou repetidas (a fala de Julião Tavares sobre o «poeta morto», p. 46 das provas; a conversa com Julião Tavares na p. 71; o fim de uma seção que foi parar na página seguinte, pp. 99–100; a cena na bodega, p. 108), letras trocadas ou caídas, falta do espaço e da vinheta entre as seções («Espaço», «Vinheta», «Favor de colocar as vinhetas equidistantes dos capítulos»). O autor marcou-os na margem, e a edição de 1947 saiu com eles corrigidos. Nas páginas que conferimos, nenhuma correção muda a redação: são todas de composição. As provas serviram aqui para desempatar leituras duvidosas e para mostrar três erros que a edição de 1947 introduziu ao recompor as linhas corrigidas («certeza esquisitas», «pensamento esquesito — Maria despida», onde as provas trazem «certezas» e «esquisito — Marina»).

**Como foi estabelecido.** O texto de 1947 foi lido duas vezes por reconhecimento automático (OCR): uma vez na camada de texto que vem no fac-símile e outra numa leitura nova, feita para esta edição; as provas foram lidas do mesmo modo. As leituras foram confrontadas palavra por palavra, e os parágrafos, decididos pelo voto das quatro. Onde as leituras de 1947 divergiam, valeu a que coincide com as provas. Todo desempate sem apoio, toda palavra fora do dicionário e toda diferença entre as provas e o resultado foram conferidos nas imagens do fac-símile de 1947: uns seiscentos e quarenta pontos, a maior parte erros de leitura das máquinas, corrigidos.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1947 (lista abaixo), como «acabuva de lavar», «cara bolofa» e «tonar-me criança».

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_êle_ → ele, _sôbre_ → sobre, _idéia_ → ideia, _director_ → diretor, _dactilografar_ → datilografar, _quási_ → quase, _à-toa_ → à toa), com _por que_ e _por quê_ nas perguntas e os nomes de lugar compostos sem hífen (Ponta da Terra). O vocabulário e as construções do autor ficaram como estão: _capueiras_, _de mais_, _choramigar_, _caitetu_, _sinha Germana_, _chauffeur_, _smoking_, _bureau_, as mesóclises, a pontuação e os travessões. O itálico é o de 1947: só o jogo de palavras com «Marina» e os versos citados.

**Divisão.** O livro não tem capítulos: o texto corre em quarenta seções sem número nem título, separadas por um espaço e uma vinheta, com as primeiras palavras em versalete. Aqui elas foram numeradas, de 1 a 40, para que cada uma seja uma página desta biblioteca; os números não são do autor.'''

BASE = 'Edição de 1947'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1947 corrigidos',
              'explica': 'Grafia atualizada nas duas colunas.'},
}

FONTES = [
    {'nome': 'Fac-símile da 3ª edição, 1947 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8415',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Provas da 3ª edição, 1946 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8482',
     'nota': 'folhas soltas, com as correções à mão do autor; lidas por dois OCRs, para desempatar as leituras de 1947'},
]

MANTIDAS = []
