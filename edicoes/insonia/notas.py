"""Insônia — texto da página «Sobre esta edição» (a mesma para todos os contos)."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
ERROS_ANTERIORES = [(d['cap'], d['para'], d['texto'].replace('_', '')) for d in _C if d['cod'] == 'erro']
_N_CONF = sum(1 for d in _C if d['cod'] != 'ver')

COMENTARIO = '''Insônia — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/insonia/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.'''

APRESENTACAO = f'''**Texto-base.** Os contos de _Insônia_ saíram em livro em 1947 (Rio de Janeiro, José Olympio, quinto volume das _Obras_ de Graciliano Ramos), a única edição publicada em vida do autor. Este texto a reproduz, pelos dois exemplares digitalizados pela Brasiliana USP. Alguns contos tinham saído antes em jornais e revistas, e alguns em _Dois dedos_ (1945); aqui vale o texto do livro.

**Como foi estabelecido.** Não há edição moderna gratuita do livro. O texto foi lido quatro vezes por reconhecimento automático (OCR): as camadas de texto que vêm nos dois exemplares digitalizados e duas leituras novas, feitas para esta edição. As quatro leituras foram confrontadas palavra por palavra, e valeu a maioria. Os pontos em que não houve maioria, ou em que a leitura podia esconder um erro (acentos, palavras raras), foram conferidos um a um nas imagens do livro: {_N_CONF} pontos.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1947 (lista abaixo). Em «Dois dedos» (p. 117 da edição) faltam duas linhas impressas; o exemplar 2 da Brasiliana as traz escritas à mão na margem, junto com outras marcas de revisão, e o trecho foi completado por elas.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_êle_ → ele, _sôbre_ → sobre, _idéia_ → ideia, _quási_ → quase), com _por que_ e _por quê_ nas perguntas. O vocabulário, a pontuação e as formas do autor ficaram como estão.

**Divisão.** O livro reúne treze contos, na ordem do índice de 1947; cada um é uma página desta biblioteca.'''

BASE = 'Edição de 1947'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1947 corrigidos',
              'explica': '¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.'},
}

FONTES = [
    {'nome': 'Fac-símile da edição de 1947, exemplar 1 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8412',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da edição de 1947, exemplar 2 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8393',
     'nota': 'lido por dois OCRs'},
]

MANTIDAS = []
