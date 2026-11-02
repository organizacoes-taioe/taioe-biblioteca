"""Vida de São Martinho, de Sulpício Severo — dados para ferramentas/traducoes.py."""

META = {
    'id': 'vida-de-sao-martinho', 'autor': 'sulpicio-severo', 'titulo': 'Vida de São Martinho',
    'ano': 397, 'datas': 'c. 396–397', 'genero': 'Hagiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Vita Sancti Martini'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Sulpício Severo, advogado da Aquitânia que deixou o mundo para levar vida '
            'ascética, conheceu São Martinho, bispo de Tours, por volta de 393 e escreveu a sua vida ainda '
            'em vida do santo, que morreu em 397. É a primeira vida de um santo do Ocidente que não foi '
            'mártir, e foi um dos livros mais lidos da Idade Média: o soldado que divide o manto com o '
            'pobre de Amiens, o monge de Ligugé e de Marmoutier, o bispo que derruba os templos dos '
            'campos da Gália e não se dobra diante do imperador. O livro vem precedido de uma carta a '
            'Desidério, amigo do autor, a quem ele confia o manuscrito.\n\n'
            '**A divisão.** Os 27 capítulos e as seções são os da edição de Halm (as pequenas marcas no '
            'texto). Estão agrupados em cinco partes, com títulos desta edição: a carta e a juventude '
            'de soldado (1–4); o monge e o bispo (5–10); os templos e os milagres (11–19); os poderosos '
            'e o diabo (20–24); o que o próprio autor viu (25–27).\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos '
            'nem explicações. Severo fala por _tu_ a Desidério e por _nós_ ou _eu_ de si mesmo, como o '
            'original. Os nomes de lugar vão na forma de hoje (Poitiers, Amiens, Tours, Tréveris, Paris, '
            'o Loire); os de pessoa, na forma portuguesa (Hilário, Auxêncio, Máximo, Paulino). As '
            'citações da Escritura são traduzidas do latim de Severo, e não de uma Bíblia moderna.\n\n'
            '**O original.** O latim ao lado é o da edição de Karl Halm (_Corpus Scriptorum '
            'Ecclesiasticorum Latinorum_, vol. 1, Viena, 1866), na digitalização da The Latin Library, '
            'com uns poucos erros de digitação corrigidos.'),
        'fontes': [
            {'nome': 'Sulpicius Severus, Vita Sancti Martini (The Latin Library)',
             'url': 'https://www.thelatinlibrary.com/sulpiciusseverusmartin.html',
             'nota': 'texto latino de base e ao lado, que segue a edição de Halm (CSEL 1, 1866)'},
            {'nome': 'Vita Sancti Martini (Wikisource latina)',
             'url': 'https://la.wikisource.org/wiki/Vita_Sancti_Martini',
             'nota': 'mesma digitação, para consulta'},
        ],
    },
}

PARTES = [
    ('Carta, 1–4', 'O soldado', ['1-o-soldado.txt']),
    ('5–10', 'O monge e o bispo', ['2-o-monge-e-o-bispo.txt']),
    ('11–19', 'Os templos e os milagres', ['3-os-templos-e-os-milagres.txt']),
    ('20–24', 'Os poderosos e o diabo', ['4-os-poderosos-e-o-diabo.txt']),
    ('25–27', 'O homem de Deus', ['5-o-homem-de-deus.txt']),
]
