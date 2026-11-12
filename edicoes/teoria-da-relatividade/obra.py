"""Sobre a teoria da relatividade especial e geral, de Albert Einstein — dados para ferramentas/traducoes.py."""

META = {
    'id': 'teoria-da-relatividade', 'indice': 'nao-ficcao-traducoes', 'autor': 'albert-einstein',
    'titulo': 'Sobre a teoria da relatividade especial e geral', 'subtitulo': 'Ao alcance de todos',
    'ano': 1917, 'datas': '1916–1920', 'genero': 'Ciência',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'marcas': False},
    'traducao': {'lingua': 'alemão', 'codigo': 'de',
                 'titulo': 'Über die spezielle und die allgemeine Relativitätstheorie'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Einstein escreveu este livrinho no fim de 1916, um ano depois de concluir a teoria da '
            'relatividade geral, para quem se interessa pela teoria sem dominar a matemática da física. Saiu em 1917, '
            'em Braunschweig, pela editora Vieweg, e foi reeditado muitas vezes em vida do autor, que o ampliou nas '
            'edições seguintes com uma terceira parte, sobre o universo como um todo, e um apêndice com a dedução da '
            'transformação de Lorentz e o mundo de quatro dimensões de Minkowski. Seguimos a 5ª edição (1920), que já '
            'traz essas partes e registra a confirmação do desvio da luz pelo Sol no eclipse de 1919. Os apêndices que '
            'Einstein juntou a edições muito posteriores ficaram de fora.\n\n'
            '**A divisão.** Três partes e um apêndice, com os 32 parágrafos (§§) numerados seguidamente, como no livro; '
            'cada parágrafo é uma página. As figuras foram redesenhadas a partir das da edição de 1920.\n\n'
            '**A tradução.** Do alemão, em português do Brasil, fiel ao tom de conversa de Einstein, que trata o leitor '
            'por “você” e se repete de propósito, “no interesse da clareza”, como diz no prefácio. Os termos da física '
            'são os de uso no Brasil (teoria da relatividade especial, corpo de referência, simultaneidade, massa '
            'inercial e massa gravitacional). As fórmulas vão como no original, em notação simples; as notas são do '
            'autor, numeradas em cada parágrafo.\n\n'
            '**O original.** O alemão, no botão «Alemão», é o da 5ª edição (Braunschweig, Vieweg, 1920). Partimos do '
            'texto da 1ª edição (1917) transcrito e revisado pelo Projeto Gutenberg, e introduzimos nele todas as '
            'mudanças de 1920, achadas pela comparação palavra por palavra com duas leituras do fac-símile de 1920 e '
            'conferidas nas imagens; a terceira parte, o apêndice e as notas novas foram transcritos do fac-símile. '
            'Ortografia e pontuação são as do livro (daß, Entwickelung); só as fórmulas foram passadas para uma notação '
            'em linha.'),
        'fontes': [
            {'nome': 'Über die spezielle und die allgemeine Relativitätstheorie, 5. Auflage (Vieweg, 1920), no Internet Archive',
             'url': 'https://archive.org/details/berdiespezielle00unkngoog',
             'nota': 'fac-símile da edição usada no original ao lado (exemplar da Universidade de Wisconsin)'},
            {'nome': 'O mesmo exemplar, em outra digitalização do Internet Archive',
             'url': 'https://archive.org/details/bub_gb_kTdWAAAAMAAJ',
             'nota': 'segunda leitura do texto de 1920'},
            {'nome': 'Über die spezielle und die allgemeine Relativitätstheorie (1917), no Projeto Gutenberg',
             'url': 'https://www.gutenberg.org/ebooks/77850',
             'nota': 'transcrição revisada da 1ª edição, base das partes I e II'},
        ],
    },
}

PARTES = [
    ('', 'Prefácio', ['prefacio.txt']),
    ('I', 'A teoria da relatividade especial', ['parte-1.txt']),
    ('II', 'A teoria da relatividade geral', ['parte-2.txt']),
    ('III', 'Considerações sobre o universo como um todo', ['parte-3.txt']),
    ('', 'Apêndice', ['apendice.txt']),
]
