"""Regra Pastoral, de São Gregório Magno — dados para ferramentas/traducoes.py."""

META = {
    'id': 'regra-pastoral', 'autor': 'sao-gregorio-magno', 'titulo': 'Regra Pastoral',
    'ano': 591, 'datas': 'c. 590–591', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Regula pastoralis'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** Gregório, monge romano, foi eleito papa em 590 contra a vontade, e '
            'escreveu a _Regra Pastoral_ logo no começo do pontificado, por volta de 591, dirigida a João, '
            'bispo de Ravena, que o repreendera por ter querido fugir do cargo. O livro responde a essa '
            'repreensão: diz por que o governo das almas assusta quem o conhece, e como deve ser quem o '
            'assume. Foi o manual dos bispos da Idade Média: o imperador Maurício mandou traduzi-lo para o '
            'grego ainda em vida do autor, o rei Alfredo da Inglaterra o pôs em inglês antigo no século IX, '
            'e os concílios do tempo de Carlos Magno mandavam os bispos conhecê-lo.\n\n'
            '**A divisão.** Gregório anuncia a ordem na carta inicial: como se chega ao governo (parte I), '
            'como vive quem chegou (parte II), como ensina quem vive bem (parte III) e como, depois de tudo, '
            'volta a si mesmo para não se exaltar (parte IV). A parte III, a mais longa, examina em 36 '
            '«admoestações» como falar a cada tipo de ouvinte, sempre aos pares de contrários (homens e '
            'mulheres, alegres e tristes, humildes e altivos…), e termina com a pregação a muitos ao mesmo '
            'tempo. Os títulos dos capítulos são os da edição latina; a pequena marca no começo de cada '
            'capítulo dá a parte e o capítulo, como se cita a obra (III.12).\n\n'
            '**A tradução.** Português do Brasil, feita do latim, fiel ao sentido e ao movimento da prosa de '
            'Gregório — as antíteses, as gradações, as explicações alegóricas da Escritura, que se traduzem '
            'ao pé da letra para que a explicação continue fazendo sentido —, sem acréscimos nem '
            'explicações. Gregório trata João por _tu_. As citações da Escritura são traduzidas do latim '
            'dele (em geral a Vulgata, às vezes a versão latina antiga), não de uma Bíblia moderna; as '
            'referências entre parênteses são as da edição de Migne, passadas às abreviaturas usuais no '
            'Brasil, com os salmos na numeração da Vulgata, a que Gregório usava (Sl 50 = Sl 51 das Bíblias '
            'que seguem o hebraico).\n\n'
            '**O original.** O latim, no botão «Latim», é o da _Patrologia Latina_ de Migne, vol. 77 '
            '(Paris, 1849, col. 13–128), que reproduz a edição dos beneditinos de São Mauro (Paris, 1705), em '
            'domínio público. Partimos da transcrição do Documenta Catholica Omnia e a conferimos palavra por '
            'palavra com o fac-símile do volume; os erros de digitação foram corrigidos pela imagem, e '
            'repusemos um parágrafo inteiro que faltava na transcrição (o começo do capítulo III.33). Os '
            'poucos erros de impressão da própria edição de 1849 ficaram no latim, e a tradução lê a forma '
            'certa. Ficaram de fora as notas e variantes dos editores.'),
        'fontes': [
            {'nome': 'Migne, Patrologia Latina 77 (Paris, 1849), no Internet Archive',
             'url': 'https://archive.org/details/bim_early-english-books-1641-1700_1849_77',
             'nota': 'fac-símile da edição usada no original ao lado (col. 13–128); conferência das correções'},
            {'nome': 'Documenta Catholica Omnia: Regulae Pastoralis Liber',
             'url': 'http://www.documentacatholicaomnia.eu/04z/z_0590-0604__SS_Gregorius_I_Magnus__Regulae_Pastoralis_Liber__LT.pdf.html',
             'nota': 'transcrição do texto de Migne, base do latim'},
            {'nome': 'Migne, Patrologia Latina 77 (Paris, Garnier, 1879), no Internet Archive',
             'url': 'https://archive.org/details/patrologiaecurs06goog',
             'nota': 'outra impressão do mesmo volume, para comparar'},
        ],
    },
}

PARTES = [
    ('I', 'A chegada ao governo', ['parte-1.txt']),
    ('II', 'A vida do pastor', ['parte-2.txt']),
    ('III', 'Como o pastor deve ensinar', ['parte-3.txt']),
    ('IV', 'A volta a si mesmo', ['parte-4.txt']),
]
