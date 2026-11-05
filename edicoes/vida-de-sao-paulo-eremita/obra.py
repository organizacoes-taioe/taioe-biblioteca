"""Vida de São Paulo, primeiro eremita, de São Jerônimo — dados para ferramentas/traducoes.py."""

META = {
    'id': 'vida-de-sao-paulo-eremita', 'autor': 'sao-jeronimo', 'titulo': 'Vida de São Paulo, primeiro eremita',
    'ano': 376, 'datas': 'c. 375–376', 'genero': 'Hagiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Vita S. Pauli primi eremitae'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** São Jerônimo escreveu esta vida por volta de 375–376, jovem ainda, quando vivia como '
            'eremita no deserto de Cálcis, na Síria; é a sua primeira obra. Conta o começo e o fim de Paulo de '
            'Tebas, que fugiu para o deserto do Egito na perseguição de Décio, por volta de 250, e lá viveu '
            'escondido quase cem anos, numa caverna com uma fonte e uma palmeira, até que Santo Antão, avisado '
            'em sonho, foi procurá-lo e o achou pouco antes da sua morte. Jerônimo quer mostrar que o primeiro '
            'eremita não foi Antão, cuja vida Santo Atanásio tinha escrito, mas Paulo. Do meio da vida de Paulo '
            'ele não diz nada, porque, como avisa, ninguém sabe. O livro, curto e cheio de cenas que a pintura '
            'guardou (o corvo que traz o pão, os leões que cavam a sepultura), foi muito lido na Idade Média. '
            'A festa de São Paulo, primeiro eremita, é a 15 de janeiro.\n\n'
            '**A divisão.** Os 18 capítulos são os da _Patrologia Latina_ (as pequenas marcas no texto). Estão '
            'agrupados em quatro partes, com títulos desta edição: Paulo no deserto (1–6), a viagem de Antão '
            '(7–9), o encontro (10–13) e a morte de Paulo (14–18).\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. As '
            'citações da Escritura vêm em itálico, traduzidas do latim de Jerônimo; os dois versos da _Eneida_ '
            'que ele adapta no cap. 9 vão em verso livre. Os títulos de capítulo da _Patrologia_ são do editor '
            'e ficaram de fora.\n\n'
            '**O original.** O latim ao lado é o da _Patrologia Latina_, vol. 23, que reproduz a edição de '
            'Domenico Vallarsi (Verona, 1734–1742), transcrito por nós das imagens das páginas, com a grafia '
            'dela. As variantes que o editor põe entre colchetes no meio do texto ficaram de fora; oito defeitos '
            'de impressão foram corrigidos. No fim, a _Patrologia_ lê «com os seus castigos», onde outros '
            'manuscritos leem «com os seus reinos».'),
        'fontes': [
            {'nome': 'Patrologia Latina 23 (Migne), col. 17–30, no Internet Archive',
             'url': 'https://archive.org/details/patrologiaecurs01goog',
             'nota': 'texto latino de base e ao lado (p. 16–22 do fac-símile)'},
            {'nome': 'Patrologia Latina 23 (Migne, 1845), outro exemplar, no Internet Archive',
             'url': 'https://archive.org/details/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_23',
             'nota': 'para conferir a transcrição'},
        ],
    },
}

PARTES = [
    ('1–6', 'Paulo no deserto', ['1-paulo-no-deserto.txt']),
    ('7–9', 'A viagem de Antão', ['2-a-viagem-de-antao.txt']),
    ('10–13', 'O encontro', ['3-o-encontro.txt']),
    ('14–18', 'A morte de Paulo', ['4-a-morte-de-paulo.txt']),
]
