"""Escada do Paraíso, de São João Clímaco — dados para ferramentas/traducoes.py."""
import os
import re

META = {
    'id': 'escada-do-paraiso', 'autor': 'sao-joao-climaco', 'titulo': 'Escada do Paraíso',
    'ano': 640, 'datas': 'séc. VII', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'degrau', 'plural': 'degraus'},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Κλῖμαξ'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** João, monge do monte Sinai, foi por muitos anos eremita ao pé da montanha e, já '
            'velho, superior do mosteiro do Sinai; viveu no século VII (as datas mais aceitas vão de cerca de 579 a cerca '
            'de 649, mas a tradição antiga o põe meio século antes). A pedido de outro João, superior do mosteiro de '
            'Raitu, junto ao mar Vermelho, escreveu para os monges um tratado em trinta «degraus», como os trinta anos da '
            'vida escondida de Cristo, que vão da renúncia ao mundo até a caridade. O livro se chamou _Κλῖμαξ_, '
            '«Escada», pela escada que Jacó viu em sonho, e deu ao autor o nome de Clímaco, «o da Escada». Foi, depois '
            'da Escritura, um dos livros mais lidos do Oriente cristão, lido todos os anos nos mosteiros durante a '
            'Quaresma, e chegou cedo ao Ocidente em latim.\n\n'
            '**A divisão.** Cada degrau trata de uma virtude ou de um vício, em sentenças curtas, definições, imagens e '
            'pequenas histórias dos monges que o autor conheceu (as mais longas, no degrau 4, sobre a obediência nos '
            'mosteiros de Alexandria, e no degrau 5, sobre os penitentes do «Cárcere»). Os degraus 23, 26 e 27 têm '
            'seções com título próprio. As marcas no começo dos parágrafos (4.12: degrau 4, parágrafo 12) são desta '
            'edição: seguem os parágrafos do texto grego, divididos nos fins de frase para a leitura e a citação.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e ao andamento das sentenças de Clímaco, '
            'sem acréscimos nem explicações. Os termos da vida espiritual são sempre os mesmos ao longo do livro: '
            '_apátheia_ é «impassibilidade» (a liberdade diante das paixões, não a indiferença), _hesychía_ é '
            '«hesíquia» (o recolhimento, a quietude do corpo e da alma), _pénthos_ é «pranto», _diákrisis_ é '
            '«discernimento», e os _logismoí_ são os «pensamentos» que assaltam a alma. As citações da Escritura são '
            'traduzidas do grego do autor, que cita a Septuaginta, muitas vezes de memória.\n\n'
            '**O original.** O grego, no botão «Grego», é o da _Patrologia Graeca_ de Migne, vol. 88 (Paris, 1860, col. '
            '631–1164), que reproduz a edição do jesuíta Mateus Rader (Paris, 1633), em domínio público. Não havendo '
            'transcrição livre desse texto, fizemos a leitura do fac-símile com reconhecimento de caracteres, comparamos '
            'duas digitalizações do volume e conferimos nas imagens as palavras duvidosas e os trechos em que a leitura '
            'falhou. Os números com que Migne remete aos escólios de Elias de Creta saíram do texto; os escólios, a '
            'tradução latina de Rader (que serviu só para conferir o sentido) e as notas dos editores ficaram de fora. '
            'Onde Rader põe entre colchetes outra lição, ela fica no grego, e a tradução segue a que dá sentido. Em dois '
            'lugares (20.3 e 28.25) falta no grego impresso um pedaço de frase que a tradução latina de Rader traz; '
            'ele vai na tradução entre colchetes.'),
        'fontes': [
            {'nome': 'Migne, Patrologia Graeca 88 (Paris, 1860), no Internet Archive',
             'url': 'https://archive.org/details/bim_early-english-books-1641-1700_1860_88',
             'nota': 'fac-símile do texto grego e do latim de Rader (col. 631–1164); base do original ao lado'},
            {'nome': 'Documenta Catholica Omnia: Joannes Climacus, Scala Paradisi (PG 88, col. 631–1163)',
             'url': 'http://www.documentacatholicaomnia.eu/02g/0525-0606,_Joannes_Climacus,_Scala_Paradisi_(MPG_088_0631_1163),_GM.pdf',
             'nota': 'outra digitalização das mesmas colunas, para a segunda leitura'},
        ],
    },
}

_T = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'traducao')


def _titulo(n):
    s = open(os.path.join(_T, 'degrau-%02d.txt' % n), encoding='utf-8').readline()
    return re.sub(r'^# titulo:\s*', '', s).strip()


PARTES = [(str(n), _titulo(n), ['degrau-%02d.txt' % n]) for n in range(1, 31)]
