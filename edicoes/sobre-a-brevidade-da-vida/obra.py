"""Sobre a brevidade da vida (De brevitate vitae), de Sêneca — dados para ferramentas/traducoes.py."""

META = {
    'id': 'sobre-a-brevidade-da-vida', 'indice': 'nao-ficcao-traducoes', 'autor': 'seneca', 'titulo': 'Sobre a brevidade da vida',
    'ano': 49, 'datas': 'c. 49–55', 'genero': 'Ensaio',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'De brevitate vitae'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Sêneca escreveu o _Sobre a brevidade da vida_ por volta do ano 49, ou poucos anos '
            'depois (a data é discutida), para Paulino, que cuidava então do abastecimento de trigo de Roma. É o '
            'décimo dos doze livros que os manuscritos chamam _Diálogos_, embora seja uma carta longa, sem '
            'interlocutores. A tese vem logo no começo: a vida não é breve, nós é que a fazemos breve. Os '
            '«ocupados», que a gastam com o dinheiro, a ambição, os prazeres, os deveres sociais e até com '
            'estudos inúteis, nunca têm tempo para si e chegam ao fim sem ter vivido; só vive quem se dá à '
            'sabedoria, e esse junta à sua vida todas as eras. O livro termina com o conselho a Paulino: que '
            'deixe o cargo e guarde para si o resto do tempo.\n\n'
            '**A divisão.** Os 20 capítulos e as seções são os da numeração usual (as pequenas marcas no texto). '
            'Os capítulos estão agrupados em cinco partes, com títulos desta edição: a vida não é breve (1–2); '
            'os ocupados (3–9); o tempo dos ocupados e o falso ócio (10–13); o ócio dos sábios (14–15); a vida '
            'dos ocupados e o conselho a Paulino (16–20).\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao movimento da prosa de '
            'Sêneca, com as suas frases curtas, as antíteses e as perguntas, sem acréscimos. Sêneca fala a '
            'Paulino por _tu_. _Otium_ é sempre «ócio», e _otiosus_, «ocioso», no sentido de Sêneca: o tempo '
            'livre dos negócios e dado a si e à sabedoria, não a preguiça; _occupati_ são «os ocupados». O verso '
            'de Virgílio citado no capítulo 9 foi traduzido em verso. Em duas passagens o texto latino está '
            'corrompido (o sinal † ao lado, em 2.4 e 9.1); a tradução dá o sentido que os editores '
            'reconstituem.\n\n'
            '**O original.** O latim, no botão «Latim», é o da edição de Emil Hermes (Leipzig, Teubner, 1905), em '
            'domínio público, transcrito por nós do fac-símile e conferido nas imagens, com a grafia e os sinais '
            'do editor (_set_, _aput_, _volgus_; ⟨ ⟩ para palavra acrescentada, [ ] para palavra excluída, † '
            'para passagem corrompida). Em alguns pontos Hermes lê diferente das edições mais conhecidas, e a '
            'tradução o segue: em 1.3, por exemplo, _set multum perdimus_ («mas perdemos muito»), onde outras '
            'trazem _perdidimus_; em 13.6, «homens inocentes» (_innoxis_), onde outras trazem «criminosos» '
            '(_noxiis_).'),
        'fontes': [
            {'nome': 'Emil Hermes, L. Annaei Senecae Dialogorum libros XII (Leipzig, Teubner, 1905), no Internet Archive',
             'url': 'https://archive.org/details/dialogorumlibro00senegoog',
             'nota': 'texto latino de base e ao lado, p. 279–309'},
            {'nome': 'A mesma edição, outro exemplar digitalizado',
             'url': 'https://archive.org/details/bub_gb_fC4PAAAAIAAJ',
             'nota': 'para conferir'},
            {'nome': 'De brevitate vitae (The Latin Library)',
             'url': 'https://www.thelatinlibrary.com/sen/sen.brevita.shtml',
             'nota': 'texto de outra edição, usado para conferir e para a numeração das seções'},
        ],
    },
}

PARTES = [
    ('1–2', 'A vida não é breve', ['1-a-vida-nao-e-breve.txt']),
    ('3–9', 'Os ocupados', ['2-os-ocupados.txt']),
    ('10–13', 'O tempo dos ocupados e o falso ócio', ['3-o-tempo-dos-ocupados.txt']),
    ('14–15', 'O ócio dos sábios', ['4-o-ocio-dos-sabios.txt']),
    ('16–20', 'A vida dos ocupados e o conselho a Paulino', ['5-o-conselho-a-paulino.txt']),
]
