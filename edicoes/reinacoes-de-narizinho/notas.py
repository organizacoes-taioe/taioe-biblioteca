"""Reinações de Narizinho: o texto da página «Sobre esta edição». Os números ({conferidos}, {corrigidos}) saem de
decisoes.py e de conferencia.tsv na hora de publicar."""
import csv
import os

import decisoes

AQUI = os.path.dirname(os.path.abspath(__file__))

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição de _Reinações de Narizinho_ (São Paulo, Companhia Editora Nacional, 1931; «Bibliotheca Pedagogica Brasileira», série 1, volume I), em que Monteiro Lobato juntou num livro só, refeitas, onze histórias que vinha publicando desde 1920, quando saiu _A Menina do Narizinho Arrebitado_. Na folha de rosto de 1931 o título é «As Reinações de Narizinho»; aqui fica o nome que o livro teve em todas as edições seguintes. Lobato reviu o texto outras vezes, e a última revisão em vida é a das _Obras Completas_ (Brasiliense, 1947), que muda palavras e frases por todo o livro. Dessa não se achou fac-símile gratuito; a de 1931 é a única edição em vida do autor que se pode ler nas imagens, e por isso é a base. As ilustrações de J. G. Villin, que acompanham a edição de 1931, não entram aqui.

**Como foi estabelecido.** O ponto de partida foi a transcrição do Wikisource, feita sobre as fotografias de um exemplar de 1931 do Museu Monteiro Lobato, em Taubaté. Ela foi confrontada palavra por palavra, página por página, com duas leituras automáticas novas (OCR) das mesmas fotografias; os pontos em que as duas leituras concordavam contra a transcrição, e as palavras raras da transcrição, foram conferidos um a um nas imagens ({conferidos} pontos). Assim se corrigiram {corrigidos} leituras da transcrição. Ao exemplar fotografado faltam duas páginas, ambas de «A Pena de Papagaio»: a 249, do começo do capítulo I («A história de Peter Pan, que dona Benta contara aos meninos…» até «…Só Peter Pan, no mundo inteiro, te-»), e a 282, o fim da história («— Vivam! — exclamou o senhor de Lafontaine…» até «…no ponto em que os meninos a haviam interrompido»). Nesses dois trechos o texto é o de uma edição posterior, que o Wikisource usou para completá-los, e não o de 1931; só o nome do fabulista foi posto na forma de 1931 («Lafontaine»).

**Correções.** Corrigiram-se só os erros evidentes da composição de 1931, listados abaixo: letras trocadas, palavras repetidas, a pontuação evidentemente errada, o capítulo VIII do «Sítio do Picapau Amarelo», que saiu numerado XIII. Na página 283 (no começo de «O Pó de Pirlimpimpim»), seis linhas foram montadas fora do lugar («…para virem cor- / e olhou.», «…disse dona Benta ap- / Minutos depois viu lá longe…»); cada uma voltou ao único lugar em que a frase se completa. «O casamento», no «Marquês de Rabicó», vem em 1931 como título sem número entre os capítulos III e IV, e assim ficou, dentro do III. No índice do fim, 1931 traz «Casa de Coruja» por «Cara de Coruja»; o título certo é o do cabeçalho da história.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _annos_ → anos, _sitio_ → sítio, _Picapau Amarello_ → Picapau Amarelo, _vóvó_ → vovó, _accommodal-a_ → acomodá-la, _idéa_ → ideia, _creança_ → criança, _quasi_ → quase, _poude_ → pôde, _porisso_ → por isso, _jaboticaba_ → jabuticaba. Ficaram como Lobato escreveu as palavras e as formas da fala das personagens (_mecê_, _sêo_, _vosmecê_, _inda_, _pra_), as onomatopeias, os nomes que o livro inventa (_Fazdeconta_, _Escavalinho_, _Pantasma_, _pirlimpimpim_) e os estrangeiros (_Pinocchio_, _Lafontaine_, _Peter Pan_, _Tom-Mix_). Três passagens cuja graça é a própria grafia de 1931 ficaram nela: o bilhete de Rabicó, com os erros de propósito («Pesso-vos-lhe perdão da minha kovardia…»); dona Benta, para quem «"elle" toda a vida teve dois "ll"»; e a lição de Narizinho a Emília: «PH é igual a F, como você pode ver nesta caixa de phosphoros». O texto do autor foi respeitado como ele o deixou em 1931, sem cortes nem trocas de palavras.

**Divisão.** Como em 1931, onze histórias, cada uma com os seus capítulos numerados e com título; cada capítulo é uma página desta biblioteca.'''

BASE = 'Edição de 1931'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1931 corrigidos',
              'explica': 'Grafia de 1931 nas duas colunas.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1931, exemplar do Museu Monteiro Lobato (Taubaté)',
     'url': 'https://pt.wikisource.org/wiki/Ficheiro:As_Reina%C3%A7%C3%B5es_de_Narizinho.pdf',
     'nota': 'fotografias do exemplar (sem as pp. 249 e 282); lidas por dois OCRs novos; as imagens decidiram as dúvidas'},
    {'nome': 'Wikisource em português, «As Reinações de Narizinho»',
     'url': 'https://pt.wikisource.org/wiki/As_Reina%C3%A7%C3%B5es_de_Narizinho',
     'nota': 'transcrição da 1ª edição, página a página, sobre o mesmo fac-símile; ponto de partida do texto'},
]

# (lugar, 1931, corrigido): erros de 1931 corrigidos fora de CORRECOES e de conferencia.tsv
ERROS_ANTERIORES = [
    (66, 'O Sítio do Picapau Amarelo, cap. VIII', 'XIII — TOM-MIX', 'VIII — TOM-MIX'),
]


def _conferencia():
    arq = os.path.join(AQUI, 'conferencia.tsv')
    if not os.path.exists(arq):
        return []
    return list(csv.DictReader(open(arq, encoding='utf-8'), delimiter='\t'))


def edicao(lugar_de_pagina=None):
    """lugar_de_pagina: função página do PDF -> «História, cap. N» (montar.py)."""
    lugar = lugar_de_pagina or (lambda p, de=None: f'p. {p}')
    conf = _conferencia()
    erros = [(p, lugar(p, d), d, n) for p, d, n, t in decisoes.CORRECOES if t == 'erro']
    erros += [(int(r['pagina']), lugar(int(r['pagina']), r['de']), r['de'], r['para']) for r in conf if r.get('tipo') == 'erro']
    erros += ERROS_ANTERIORES
    erros = [e[1:] for e in sorted(erros, key=lambda e: e[0])]
    corrigidos = sum(1 for r in conf if r.get('tipo') == 'ws')
    texto = APRESENTACAO.format(conferidos=len(conf), corrigidos=corrigidos)
    return {'base': BASE, 'secoes': SECOES, 'apresentacao': texto, 'fontes': FONTES,
            'erros': [{'cap': c, 'de': d, 'para': p} for c, d, p in erros]}
