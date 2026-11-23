"""Catecismo Maior de São Pio X (Compendio della dottrina cristiana, Catechismo maggiore, Roma, 1905) —
dados para ferramentas/traducoes.py. O original sai de montar.py; a divisão em capítulos, de «## n. título»
com a marca «[parte.n]» no primeiro bloco de cada capítulo, que não aparece (divisao.marcas = False)."""

META = {
    'id': 'catecismo-pio-x', 'autor': 'igreja-catolica', 'titulo': 'Catecismo Maior de São Pio X',
    'subtitulo': 'Compêndio da doutrina cristã',
    'ano': 1905, 'datas': 'São Pio X, 1905', 'genero': 'Magistério', 'grupo': 'São Pio X',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'marcas': False},
    'traducao': {'lingua': 'italiano', 'codigo': 'it', 'titulo': 'Catechismo maggiore'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Em 14 de junho de 1905, São Pio X, numa carta ao cardeal Pietro Respighi, seu vigário '
            'geral, prescreveu às dioceses da província eclesiástica de Roma um _Compêndio da doutrina cristã_, '
            'tirado, com pequenos retoques, dos catecismos já usados na Itália, e disse esperar que as outras '
            'dioceses o adotassem, para se chegar a um texto único. O volume, impresso em Roma pela Tipografia '
            'Vaticana no mesmo ano, tem as primeiras noções para as crianças pequenas, o catecismo pequeno, o '
            'catecismo maior, uma instrução sobre as festas e uma breve história da religião. O _Catecismo '
            'maior_, a parte principal, destinado aos jovens que já sabiam o pequeno, é o que se chama até hoje '
            '_Catecismo de São Pio X_. É só ele que está aqui. (Em 1912 o Papa prescreveu para Roma outro '
            'catecismo, mais curto, que é outro livro.)\n\n'
            '**A divisão.** Uma lição preliminar e cinco partes: o Credo, a oração, os mandamentos de Deus e os '
            'preceitos da Igreja, os sacramentos, e as virtudes com as outras coisas que o cristão precisa '
            'saber. As partes se dividem em capítulos e, muitos deles, em parágrafos (§), com os títulos da '
            'edição. São 993 perguntas, cada uma com a sua resposta. A edição de 1905 não numera as perguntas; '
            'a numeração contínua, de 1 a 993, foi posta por nós, para facilitar a citação. O «D.» e o «R.» da '
            'edição (_domanda_ e _risposta_) viraram a pergunta em negrito, seguida da resposta.\n\n'
            '**A tradução.** Nossa, feita do italiano, em português do Brasil simples, como o de um catecismo '
            'para o povo, fiel ao texto e sem acréscimos. O catequista trata quem aprende por «você». As '
            'orações e as fórmulas que o catecismo manda recitar (o Credo, o Pai-Nosso, a Ave-Maria, os '
            'sacramentos, as virtudes, os dons do Espírito Santo, as obras de misericórdia, os pecados '
            'capitais) estão na forma rezada no Brasil, salvo onde o próprio catecismo explica as palavras da '
            'sua forma: por isso o Credo diz «desceu aos infernos» e o Pai-Nosso «perdoai-nos as nossas '
            'dívidas», e os mandamentos de Deus e os preceitos da Igreja seguem as palavras do catecismo. As '
            'citações da Escritura foram traduzidas como o catecismo as dá.\n\n'
            '**O original.** O italiano, no botão «Italiano», é o da edição de Roma, Tipografia Vaticana, 1905 '
            '(pp. 75-287), na transcrição do Wikisource italiano, validada página por página contra o fac-símile '
            'do volume, e conferida de novo por nós, palavra por palavra, com uma leitura própria das imagens; os '
            'erros de transcrição que isso apontou (uns trinta, quase todos de acento ou de palavra partida) '
            'foram corrigidos pela imagem. A grafia é a da edição (_perchè_, _imagine_, _divozione_).'),
        'fontes': [
            {'nome': 'Compendio della dottrina cristiana, Roma, Tipografia Vaticana, 1905, fac-símile no Wikimedia Commons',
             'url': 'https://commons.wikimedia.org/wiki/File:Compendio_della_dottrina_cristiana,_Roma,_1905.djvu',
             'nota': 'a edição usada no original ao lado (pp. 75-287), digitalizada pelo Google Livros'},
            {'nome': 'Wikisource italiano: Compendio della dottrina cristiana / Catechismo maggiore',
             'url': 'https://it.wikisource.org/wiki/Compendio_della_dottrina_cristiana/Catechismo_maggiore',
             'nota': 'transcrição validada da mesma edição, base do texto italiano'},
            {'nome': 'Carta de São Pio X ao cardeal Respighi, 14 de junho de 1905, no site da Santa Sé',
             'url': 'https://www.vatican.va/content/pius-x/it/letters/documents/hf_p-x_let_19050614_compendio-catechismo.pdf',
             'nota': 'a carta que prescreve o Compêndio (também no começo do volume)'},
        ],
    },
}

P1 = ['p1-c%02d.txt' % n for n in range(1, 14)]
P2 = ['p2-c%02d.txt' % n for n in range(1, 5)]
P3 = ['p3-c%02d.txt' % n for n in range(1, 6)]
P4 = ['p4-c01.txt', 'p4-c02.txt', 'p4-c03.txt', 'p4-c04.txt', 'p4-c05.txt', 'p4-c06a.txt', 'p4-c06b.txt',
      'p4-c07.txt', 'p4-c08.txt', 'p4-c09.txt']
P5 = ['p5-c%02d.txt' % n for n in range(1, 9)]

PARTES = [
    ('', 'Lição preliminar', ['p0-licao-preliminare.txt']),
    ('I', 'Do Símbolo dos Apóstolos, chamado comumente o «Credo»', P1),
    ('II', 'Da oração', P2),
    ('III', 'Dos mandamentos de Deus e da Igreja', P3),
    ('IV', 'Dos sacramentos', P4),
    ('V', 'Das virtudes principais e de outras coisas que o cristão precisa saber', P5),
]
