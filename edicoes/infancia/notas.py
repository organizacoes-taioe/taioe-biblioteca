"""Infância — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
ERROS_ANTERIORES = [(d['cap'], d['para'], d['texto'].replace('_', '')) for d in _C if d['cod'] == 'erro']
_N_CONF = sum(1 for d in _C if d['cod'] != 'ver')

COMENTARIO = '''Infância — Graciliano Ramos
   Gerado por ferramentas/texto.py a partir de edicoes/infancia/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados.'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a primeira edição de _Infância_ (Rio de Janeiro, José Olympio, 1945), a única publicada em vida do autor, pelos dois exemplares digitalizados pela Brasiliana USP. Alguns capítulos tinham saído antes em jornais e revistas; aqui vale o texto do livro.

**Como foi estabelecido.** Não há edição moderna gratuita do livro. O texto foi lido quatro vezes por reconhecimento automático (OCR): as camadas de texto que vêm nos dois exemplares digitalizados e duas leituras novas, feitas para esta edição. As quatro leituras foram confrontadas palavra por palavra, e valeu a maioria. Os pontos em que não houve maioria, ou em que a leitura podia esconder um erro (acentos, palavras raras), foram conferidos um a um nas imagens do livro: {_N_CONF} pontos.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1945 (lista abaixo).

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_êle_ → ele, _sôbre_ → sobre, _idéia_ → ideia, _quási_ → quase), com _por que_ e _por quê_ nas perguntas. O vocabulário, a pontuação e as formas do autor ficaram como estão.

**Divisão.** O livro tem trinta e nove capítulos com título, sem número; cada um é uma página desta biblioteca.'''

BASE = 'Edição de 1945'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1945 corrigidos',
              'explica': '¶ marca o começo de um parágrafo. Grafia atualizada nas duas colunas.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1945, exemplar 1 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8871',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da 1ª edição, 1945, exemplar 2 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/8394',
     'nota': 'lido por dois OCRs'},
]

MANTIDAS = []
