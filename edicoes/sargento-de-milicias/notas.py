"""Memórias de um Sargento de Milícias — texto da página «Sobre esta edição»."""
import json
import os
import re
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_AQUI, '..', '..', 'ferramentas'))
from edicao.tokens import TOK, texto as _junta  # noqa: E402

_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))


def _rotulo(cap):
    t, c = cap.split('.')
    return f'tomo {t}, cap. {c}'


def _curto(de, para):
    """Só o que muda, com uma palavra de cada lado."""
    a = [t for t in TOK.findall(de) if t != '_']
    b = [t for t in TOK.findall(para) if t != '_']
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    z = 0
    while z < min(len(a), len(b)) - i and a[-1 - z] == b[-1 - z]:
        z += 1
    i0 = max(0, i - 1)
    return _junta(a[i0:len(a) - max(0, z - 1)]), _junta(b[i0:len(b) - max(0, z - 1)])


ERROS_ANTERIORES = [(_rotulo(d['cap']), *(d.get('sobre') or _curto(d['para'], d['texto']))) for d in _C if d['cod'] == 'erro' and d.get('cap')]
_N_CONF = sum(1 for d in _C if d['cod'] in ('ok', 'fix', 'erro', 'ws') and d['id'] < 3000)
_N_ITAL = sum(1 for d in _C if d['cod'] == 'ital')

COMENTARIO = '''Memórias de um Sargento de Milícias — Manuel Antônio de Almeida
   Gerado por ferramentas/texto.py a partir de edicoes/sargento-de-milicias/. Não edite à mão:
   corrija as decisões em edicoes/sargento-de-milicias/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso;
     - «## Capítulo N — título» abre cada capítulo, e «{§ T.c}» marca o seu primeiro parágrafo
       (só para o site dividir as páginas; não aparece no texto).'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a primeira edição em livro das _Memórias de um Sargento de Milícias_, publicada «por um Brasileiro» no Rio de Janeiro, pela Typographia Brasiliense de Maximiano Gomes Ribeiro, em dois tomos (o primeiro de 1854, o segundo de 1855), a única em vida do autor, morto em 1861. O romance tinha saído antes, sem assinatura, em folhetim na «Pacotilha», o suplemento de domingo do _Correio Mercantil_, entre junho de 1852 e julho de 1853.

**Como foi estabelecido.** Foram confrontadas palavra por palavra três leituras automáticas (OCR) do exemplar da Brasiliana USP: a que vem no PDF da biblioteca, a que vem na cópia do mesmo exemplar no Wikimedia Commons e uma nova, feita para esta edição. O texto moderno do Wikisource serviu para a divisão em parágrafos e para a grafia; onde o texto assim estabelecido diferia do moderno em palavras, a leitura foi conferida nas imagens do livro ({_N_CONF} pontos), e o itálico, que nenhuma das leituras automáticas marca, foi achado pela inclinação das letras e conferido nas imagens. Onde a edição moderna muda o texto do autor («esganava» por «espanava», «havia de custar» por «havia custar», «tampouco» por «tão pouco»), ficou o de 1854–55.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira (_elle_ → ele, _baptisar_ → batizar, _cousa_ → coisa, _dous_ → dois). A 3ª pessoa do plural em _-ão_ dos tempos passados e do presente passou a _-am_ (_chegárão_ → chegaram, _formão_ → formam), e o futuro ficou (_verão_). As formas antigas de palavras de hoje passaram à forma atual (_vestoria_ → vistoria, _couces_ → coices); o vocabulário e as construções do autor ficaram (_intercortada_, _esconjúrio_, _cinteiro_, «havia custar», «o quer que fosse»).

**Divisão.** O romance tem dois tomos, como em 1854–55: o primeiro com 23 capítulos, o segundo com 25, cada um com título; cada capítulo é uma página desta biblioteca. As modinhas e cantigas citadas vão em versos, como no livro.'''

BASE = 'Edição de 1854–55'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1854–55 corrigidos',
              'explica': 'Na grafia de hoje; à esquerda, o que traz o impresso de 1854–55.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1854–55, exemplar da Brasiliana USP', 'url': 'https://digital.bbm.usp.br/handle/bbm/4846',
     'nota': 'lido pelo OCR da biblioteca e por um OCR novo (Tesseract); as imagens decidiram as dúvidas'},
    {'nome': 'O mesmo exemplar no Wikimedia Commons (DjVu)', 'url': 'https://commons.wikimedia.org/wiki/File:Memorias_de_um_sargento_de_milicias.djvu',
     'nota': 'a camada de texto do DjVu, outra leitura automática'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Mem%C3%B3rias_de_um_Sargento_de_Mil%C3%ADcias',
     'nota': 'texto moderno, posto sobre as páginas do mesmo fac-símile; referência para os parágrafos e a ortografia'},
]

MANTIDAS = []

