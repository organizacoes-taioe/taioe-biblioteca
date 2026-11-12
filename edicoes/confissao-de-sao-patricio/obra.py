"""Confissão, de São Patrício — dados para ferramentas/traducoes.py."""

META = {
    'id': 'sao-patricio-confissao', 'autor': 'sao-patricio', 'titulo': 'Confissão',
    'ano': 450, 'datas': 'c. 450', 'genero': 'Autobiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Confessio'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Patrício, filho de um diácono e neto de um presbítero da Britânia romana, foi levado '
            'cativo para a Irlanda por piratas aos dezesseis anos, guardou gado ali durante seis anos, fugiu e '
            'voltou para casa. Anos depois, chamado numa visão pela «voz dos irlandeses», voltou à ilha como '
            'bispo e passou nela o resto da vida, entre os que o tinham escravizado. Já velho, acusado por '
            'alguns dos seus superiores na Britânia, que lhe lançavam em rosto um pecado da juventude, escreveu '
            'esta _Confissão_, em latim, por volta de 450: não é uma autobiografia no sentido de hoje, mas uma '
            'confissão no sentido antigo, louvor a Deus pelo que fez num homem sem instrução, e defesa da sua '
            'missão. Com a _Carta aos soldados de Corótico_, é tudo o que temos escrito pelo próprio Patrício, e '
            'o único testemunho seguro sobre a sua vida; as lendas vieram depois.\n\n'
            '**A divisão.** Os 62 parágrafos são os da edição de White (as pequenas marcas no texto), os mesmos '
            'pelos quais a obra se cita. Estão agrupados em sete partes, com títulos desta edição: o cativeiro e a '
            'fé (1–8); por que escreve (9–15); a fuga e as visões (16–25); a acusação (26–33); a missão entre os '
            'irlandeses (34–45); a conduta dele entre os fiéis (46–54); e o fim (55–62).\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos nem '
            'explicações. O latim de Patrício é áspero e às vezes difícil, de quem, como ele mesmo diz, '
            'interrompeu os estudos aos dezesseis anos: frases que mudam de rumo no meio, palavras repetidas, '
            'ligações soltas. A tradução não o embeleza; só torna claro o que no latim é claro, e deixa como está '
            'o que ele deixou suspenso (26; 60). _Hiberio_ é a Irlanda, e os _Scotti_ e _Hiberionaci_ são os '
            'irlandeses. As citações da Escritura são traduzidas do latim de Patrício, que cita muitas vezes de '
            'uma versão anterior à Vulgata; as referências entre parênteses, com os salmos na numeração da '
            'Vulgata seguida da hebraica, foram postas por nós, a partir das notas de White.\n\n'
            '**O original.** O latim ao lado é o da edição de Newport J. D. White, _Libri Sancti Patricii_ '
            '(Londres, 1918), com a grafia dele (_uico_, _Uillulam_, _inperfectus_), sem o aparato. Foi lido por '
            'nós nas imagens do volume, página por página, e conferido com duas leituras automáticas de dois '
            'exemplares e com a primeira edição de White (Dublin, 1905). White segue sobretudo o Livro de Armagh, '
            'do século IX, e outros manuscritos; onde ele corrige todos eles (58: «testemunho fiel», onde os '
            'manuscritos têm «testemunha fiel»), a tradução o segue. Em 49 a tradução lê um «não» que o sentido '
            'pede e que o texto de White não traz.'),
        'fontes': [
            {'nome': 'Newport J. D. White, Libri Sancti Patricii: the Latin writings of St. Patrick (Londres, SPCK, 1918), no Internet Archive',
             'url': 'https://archive.org/details/librisanctipatr00patr',
             'nota': 'fac-símile da edição de base (p. 5–26); texto latino ao lado'},
            {'nome': 'O mesmo, outro exemplar, no Internet Archive',
             'url': 'https://archive.org/details/librisanctipatri0000patr',
             'nota': 'para a conferência'},
            {'nome': 'Newport J. D. White, Libri Sancti Patricii (Proceedings of the Royal Irish Academy 25 C, Dublin, 1905), no Internet Archive',
             'url': 'https://archive.org/details/librisanctipatri00patr',
             'nota': 'primeira edição crítica de White, com o aparato completo'},
        ],
    },
}

PARTES = [
    ('1–8', 'O cativeiro e a fé', ['confessio.txt#1-8']),
    ('9–15', 'Por que escrevo', ['confessio.txt#9-15']),
    ('16–25', 'A fuga e as visões', ['confessio.txt#16-25']),
    ('26–33', 'A acusação', ['confessio.txt#26-33']),
    ('34–45', 'A missão entre os irlandeses', ['confessio.txt#34-45']),
    ('46–54', 'Como vivi entre vós', ['confessio.txt#46-54']),
    ('55–62', 'Até o fim', ['confessio.txt#55-62']),
]
