"""Paixão de Perpétua e Felicidade (Santa Perpétua, Sáturo e um anônimo) — dados para ferramentas/traducoes.py."""

META = {
    'id': 'paixao-de-perpetua', 'autor': 'anonimo', 'titulo': 'Paixão de Perpétua e Felicidade',
    'ano': 203, 'datas': 'c. 203', 'genero': 'Hagiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Passio Sanctarum Perpetuae et Felicitatis'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** A _Paixão de Perpétua e Felicidade_ conta o martírio de um grupo de catecúmenos '
            'presos em Cartago, na África romana, e mortos nas feras do anfiteatro no aniversário do César '
            'Geta, em 7 de março de 203, sob o imperador Sétimo Severo. É um dos textos cristãos mais antigos '
            'escritos em latim e tem três vozes. Um redator anônimo escreve o prefácio, a apresentação dos '
            'presos e, depois, o relato do martírio (1–2 e 14–21). No meio, ele transcreve o diário da própria '
            'Perpétua, uma jovem matrona de 22 anos, mãe de um menino de peito, que conta a prisão, as súplicas '
            'do pai e quatro visões (3–10); e a visão escrita por Sáturo, o catequista do grupo (11–13). É, '
            'portanto, um dos raros textos antigos escritos por uma mulher. Santo Agostinho pregou sobre as '
            'mártires na festa delas, e os nomes de Felicidade e Perpétua estão no Cânon Romano da Missa; a '
            'festa é a 7 de março. O redator é desconhecido; já se pensou em Tertuliano, sem prova.\n\n'
            '**A divisão.** Os 21 capítulos e os parágrafos são os da numeração usual (as pequenas marcas no '
            'texto). Os capítulos estão agrupados em quatro partes, com títulos desta edição: o prefácio e os '
            'presos (1–2), o relato de Perpétua (3–10), a visão de Sáturo (11–13) e o martírio (14–21).\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. O '
            'latim de Perpétua é simples, de frases curtas ligadas por «e», com palavras da língua falada; a '
            'tradução guarda esse andamento, que contrasta com o estilo mais trabalhado do redator. As palavras '
            'gregas do texto latino ficam em grego transcrito (_tégnon_, «filho», em 4,9; _ágios_, «santo», em '
            '12,2). As citações da Escritura vêm em itálico, traduzidas do latim da obra. Onde Robinson adota '
            'conjecturas próprias, a tradução o segue: em 11,6, as folhas das árvores «cantavam» (os manuscritos '
            'dizem «caíam»); em 11,8, «um estádio coberto de violetas» (outros leem «por um caminho largo»).\n\n'
            '**O original.** O latim ao lado é o da edição de J. Armitage Robinson (Cambridge, 1891), feita '
            'sobre os manuscritos latinos e a versão grega antiga. O texto grego, que Robinson imprime ao lado '
            'do latim, não está aqui.'),
        'fontes': [
            {'nome': 'J. Armitage Robinson, The Passion of S. Perpetua (Texts and Studies I,2, Cambridge, 1891), no Internet Archive',
             'url': 'https://archive.org/details/MN5140ucmf_2',
             'nota': 'texto latino de base e ao lado (p. 60–95)'},
            {'nome': 'Passio Sanctarum Perpetuae et Felicitatis (The Latin Library)',
             'url': 'https://www.thelatinlibrary.com/perp.html',
             'nota': 'transcrição digital usada como ponto de partida e corrigida pela edição de Robinson'},
        ],
    },
}

PARTES = [
    ('1–2', 'O prefácio e os presos', ['1-o-prefacio-e-os-presos.txt']),
    ('3–10', 'O relato de Perpétua', ['2-o-relato-de-perpetua.txt']),
    ('11–13', 'A visão de Sáturo', ['3-a-visao-de-saturo.txt']),
    ('14–21', 'O martírio', ['4-o-martirio.txt']),
]
