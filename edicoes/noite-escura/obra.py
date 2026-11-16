"""Noite Escura, de São João da Cruz — dados para ferramentas/traducoes.py.
Convenções da tradução: edicoes/subida-do-monte-carmelo/CONVENCOES.md (valem para as duas obras)."""

META = {
    'id': 'noite-escura', 'autor': 'sao-joao-da-cruz', 'titulo': 'Noite Escura',
    'ano': 1585, 'datas': 'c. 1578–1585', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'livro', 'plural': 'livros'},
    'traducao': {'lingua': 'espanhol', 'codigo': 'es', 'titulo': 'Noche oscura'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** João da Cruz (Juan de Yepes, 1542–1591), frade carmelita e companheiro de santa '
            'Teresa de Jesus na reforma do Carmelo, escreveu a _Noite Escura_ como comentário ao seu poema «Em uma '
            'noite escura», o mesmo da _Subida do Monte Carmelo_, também na Biblioteca. Se a _Subida_ ensina o que a '
            'alma deve fazer para se despojar, a _Noite_ trata do que Deus faz nela, nas purificações que ela padece. '
            'A obra ficou inacabada: o comentário para no começo da terceira estrofe. Saiu pela primeira vez em '
            'Alcalá, em 1618.\n\n'
            '**A divisão.** Um prólogo, as canções e dois livros: o primeiro, da noite do sentido; o segundo, da noite '
            'do espírito. A pequena marca no começo de cada capítulo dá o livro e o capítulo (II.5), e os números dos '
            'parágrafos são os da edição usada.\n\n'
            '**A tradução.** Português do Brasil, feita do espanhol, fiel ao sentido e ao movimento da prosa do autor, '
            'sem acréscimos nem explicações. As citações latinas da Vulgata ficam em latim, com a tradução que o '
            'próprio autor dá. Os versos citados vão em tradução própria.\n\n'
            '**O original ao lado.** O botão «Espanhol» mostra o texto da edição do P. Silverio de Santa Teresa '
            '(_Obras de San Juan de la Cruz_, t. II, Burgos, 1929), em domínio público, com a acentuação de hoje, '
            'tirado do fac-símile por três leituras automáticas conferidas entre si e com a imagem. Ficaram de fora '
            'as notas e variantes do editor.'),
        'fontes': [
            {'nome': 'Obras de San Juan de la Cruz, ed. Silverio de Santa Teresa, t. II (Burgos, 1929), no Internet Archive',
             'url': 'https://archive.org/details/obrasdesanjuande02john',
             'nota': 'fac-símile da edição usada no original ao lado'},
        ],
    },
}

PARTES = [
    ('', 'Prólogo e canções', ['0-prologo-e-cancoes.txt']),
    ('I', 'Livro primeiro: a noite do sentido', ['1-livro-primeiro.txt']),
    ('II', 'Livro segundo: a noite do espírito', ['2-livro-segundo-a.txt', '2-livro-segundo-b.txt']),
]
