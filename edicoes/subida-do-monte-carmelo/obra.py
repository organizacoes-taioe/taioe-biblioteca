"""Subida do Monte Carmelo, de São João da Cruz — dados para ferramentas/traducoes.py."""

META = {
    'id': 'subida-do-monte-carmelo', 'autor': 'sao-joao-da-cruz', 'titulo': 'Subida do Monte Carmelo',
    'ano': 1579, 'datas': 'c. 1578–1585', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'livro', 'plural': 'livros'},
    'traducao': {'lingua': 'espanhol', 'codigo': 'es', 'titulo': 'Subida del Monte Carmelo'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** João da Cruz (Juan de Yepes, 1542–1591), frade carmelita e companheiro de santa '
            'Teresa de Jesus na reforma do Carmelo, escreveu a _Subida do Monte Carmelo_ em prosa como comentário ao '
            'seu poema «Em uma noite escura», cujas oito estrofes abrem o livro. A obra ficou inacabada: o autor '
            'comenta só as duas primeiras estrofes, e o terceiro livro para no meio de um assunto. Não foi publicada '
            'em vida dele; saiu pela primeira vez em Alcalá, em 1618. A _Noite Escura_, também na Biblioteca, é o '
            'outro comentário ao mesmo poema.\n\n'
            '**A divisão.** Um argumento, as canções, um prólogo e três livros: o primeiro trata da noite do sentido; '
            'o segundo, da noite do espírito quanto ao entendimento, pela fé; o terceiro, da memória, pela esperança, '
            'e da vontade, pela caridade. A pequena marca no começo de cada capítulo dá o livro e o capítulo, como se '
            'cita a obra (II.5), e os números dos parágrafos são os da edição usada.\n\n'
            '**A tradução.** Português do Brasil, feita do espanhol, fiel ao sentido e ao movimento da prosa do autor, '
            'que raciocina com distinções e provas da Escritura, sem acréscimos nem explicações. As citações latinas '
            'da Vulgata ficam em latim, com a tradução que o próprio autor dá logo depois. Os versos citados vão em '
            'tradução própria.\n\n'
            '**O original ao lado.** O botão «Espanhol» mostra o texto da edição do P. Silverio de Santa Teresa '
            '(_Obras de San Juan de la Cruz_, t. II, Burgos, 1929), em domínio público, com a acentuação de hoje, '
            'tirado do fac-símile por três leituras automáticas conferidas entre si e com a imagem. Ficaram de fora '
            'as notas e variantes do editor.'),
        'fontes': [
            {'nome': 'Obras de San Juan de la Cruz, ed. Silverio de Santa Teresa, t. II (Burgos, 1929), no Internet Archive',
             'url': 'https://archive.org/details/obrasdesanjuande02john',
             'nota': 'fac-símile da edição usada no original ao lado'},
            {'nome': 'Documenta Catholica Omnia: La subida del Monte Carmelo',
             'url': 'http://www.documentacatholicaomnia.eu/',
             'nota': 'transcrição usada só para limpar a leitura automática do fac-símile'},
        ],
    },
}

PARTES = [
    ('', 'Argumento, canções e prólogo', ['0-argumento-e-prologo.txt']),
    ('I', 'Livro primeiro: a noite do sentido', ['1-livro-primeiro.txt']),
    ('II', 'Livro segundo: a noite do espírito no entendimento',
     ['2-livro-segundo-a.txt', '2-livro-segundo-b.txt', '2-livro-segundo-c.txt']),
    ('III', 'Livro terceiro: a memória e a vontade', ['3-livro-terceiro-a.txt', '3-livro-terceiro-b.txt']),
]
