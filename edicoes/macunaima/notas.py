"""Macunaíma — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_N_CONF = len(json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8')))

COMENTARIO = '''Macunaíma — Mário de Andrade
   Gerado por ferramentas/texto.py a partir de edicoes/macunaima/.
   Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a primeira edição de _Macunaíma, o herói sem nenhum caráter_ (São Paulo, edição do autor, 1928, oitocentos exemplares impressos nas Oficinas Gráficas de Eugênio Cupolo), pelo fac-símile do exemplar da Biblioteca Nacional. Mário de Andrade reviu o livro para a segunda edição (Rio de Janeiro, José Olympio, 1937) e mexeu nele de novo na terceira (São Paulo, Martins, 1944); essas edições não estão digitalizadas, e o texto daqui é o de 1928 de ponta a ponta.

**O capítulo das normalistas.** Em 1928 o livro tem dezoito capítulos e o epílogo. Para a edição de 1937, Mário cortou o fim do capítulo XI, «As três normalistas», em que o herói propõe às moças da Escola Normal da praça da República que brinquem com ele; o que sobrou do capítulo passou ao começo do seguinte, «A velha Ceiuci», e o livro ficou com dezessete. Aqui o capítulo está inteiro, como saiu em 1928.

**Como foi estabelecido.** Não há edição moderna gratuita da primeira edição. Foram confrontadas palavra por palavra três leituras: a transcrição do Wikisource, revisada sobre as imagens de 1928 no capítulo I e do XII ao epílogo; o reconhecimento automático (OCR) do fac-símile que acompanha a digitalização no Internet Archive; e um OCR novo do mesmo fac-símile, feito para esta edição. Do capítulo II ao XI o Wikisource ainda não foi revisado e traz o texto de uma edição posterior, já modernizada (_flecha_ por _frexa_, _tribo_ por _tribu_, frases e listas diferentes): ali ele só serviu para apontar as dúvidas, e o texto é o dos dois OCRs de 1928. Onde as leituras divergiam sem maioria, e onde a maioria podia esconder um erro, o ponto foi conferido nas imagens do livro: cerca de {_N_CONF + 150} pontos. Assim se recuperou, por exemplo, um parágrafo inteiro da «Carta pras Icamiabas» («Também temos feito muitos discursos de improviso…») que a edição posterior cortou.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1928 (lista abaixo). Ficaram as formas de Mário que podem ser intencionais: _mostro_, _estorcegado de cócegas_, «Vinham médicos veio Assistência», as palavras inventadas e a pontuação do livro, que corta vírgulas de propósito («foi crescendo foi crescendo»).

**Ortografia.** Mário escrevia «à brasileira», de propósito, e essa grafia é parte do livro: ficaram _si_, _sinão_, _siquer_, _mãi_, _milhor_, _guspir_, _enguliu_, _frexa_ e _flexa_, _guela_, _pra_ e _prá_, _inda_, _riba_, _adonde_, as palavras compostas do autor (_arranhacéu_, _boca-da-noite_, _mãi-de-santo_) e a colocação dos pronomes («Me acocorei em riba destas folhas»). Atualizou-se só a ortografia da época que não marca a fala: os acentos (_heroi_ → herói, _tambem_ → também, _porêm_ → porém, _êle_ → ele, _jejú_ → jeju), _quasi_ → quase, _tribu_ → tribo, _poude_ → pôde, _geito_ → jeito, _tezouro_ → tesouro, _gosar_ → gozar, _dansa_ → dança, _cincoenta_ → cinquenta, _milreis_ → mil-réis, e as palavras indígenas e africanas cuja grafia de 1928 caiu (_Ochum_ → Oxum, _macacheira_ → macaxeira, _girau_ → jirau, _sussuarana_ → suçuarana, _guassú_ → guaçu). A «Carta pras Icamiabas», escrita num português de Portugal de propósito empolado, guarda as formas lusitanas do original (_abstémio_, _Polónia_, _assás_, _hemos_). As aspas passaram a angulares.

**Divisão.** O livro tem dezoito capítulos numerados e com título, mais o epílogo; cada um é uma página desta biblioteca.'''

BASE = 'Edição de 1928'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1928 corrigidos',
              'explica': 'Grafia atualizada nas duas colunas.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1928, exemplar da Biblioteca Nacional (Internet Archive)',
     'url': 'https://archive.org/details/or182096',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Wikisource em português, «Macunaíma (1928)»',
     'url': 'https://pt.wikisource.org/wiki/Macuna%C3%ADma_(1928)',
     'nota': 'transcrição revisada no capítulo I e do XII ao epílogo; nos outros, texto de edição posterior, só para apontar dúvidas'},
]

MANTIDAS = []

# (lugar, 1928, corrigido), na grafia de hoje
ERROS_ANTERIORES = [
    ('III', 'E como Jiguê são conseguira moçar', 'E como Jiguê não conseguira moçar'),
    ('IV', 'si a boboiúna aparececesse', 'si a boboiúna aparecesse'),
    ('V', 'a moeda tradicional. Caculou com eles', 'a moeda tradicional. Calculou com eles'),
    ('V', 'duzentorréis quinhentonréis', 'duzentorréis quinhentorréis'),
    ('XI', 'o senhor fez um discursos pros grilos', 'o senhor fez um discurso pros grilos'),
]
