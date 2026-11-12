"""A democracia na América (De la démocratie en Amérique), de Alexis de Tocqueville, seleção — dados para
ferramentas/traducoes.py."""

META = {
    'id': 'democracia-na-america', 'indice': 'nao-ficcao-traducoes', 'autor': 'alexis-de-tocqueville',
    'titulo': 'A democracia na América', 'subtitulo': 'Seleção',
    'ano': 1835, 'datas': '1835–1840', 'genero': 'Política',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos', 'marcas': False},
    'traducao': {'lingua': 'francês', 'codigo': 'fr', 'titulo': 'De la démocratie en Amérique'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O livro.** Alexis de Tocqueville tinha vinte e cinco anos quando partiu para os Estados Unidos, em 1831, '
            'com o amigo Gustave de Beaumont, para estudar o sistema penitenciário americano. Voltou com o material de '
            'outro livro: _A democracia na América_, publicado em duas partes, a primeira em 1835 (as instituições e a '
            'vida política) e a segunda em 1840 (a influência da igualdade sobre as ideias, os sentimentos e os costumes). '
            'A pergunta que atravessa a obra está na Introdução: a igualdade de condições avança em todo o mundo cristão '
            'como um «fato providencial»; o que fazer para que ela leve à liberdade e não a uma nova servidão?\n\n'
            '**A seleção.** O livro inteiro tem perto de trezentas mil palavras. Aqui estão a Introdução e treze capítulos '
            'inteiros, os mais lidos e citados, cerca de 45 mil palavras: da primeira parte, o ponto de partida dos '
            'puritanos, o estado social dos anglo-americanos, a onipotência e a tirania da maioria e, do longo capítulo '
            'sobre as causas que mantêm a república democrática, só as seções sobre os costumes e a religião (as causas '
            'acidentais, as leis, as luzes e a comparação com a Europa ficam de fora); da segunda parte, a fonte das '
            'crenças nos povos democráticos e a religião diante dos instintos democráticos, os capítulos sobre o '
            'individualismo e a doutrina do interesse bem compreendido, «Que espécie de despotismo as nações democráticas '
            'devem temer» e a «Visão geral do assunto», com que o livro termina. A escolha dá mais lugar à religião e aos '
            'costumes, que para Tocqueville sustentam a liberdade mais que as leis. O título de cada capítulo diz o seu '
            'lugar no livro.\n\n'
            '**A tradução.** Do francês, em português do Brasil, fiel ao sentido e ao movimento da prosa de Tocqueville, '
            'com os seus períodos longos e as suas antíteses, sem acréscimos. Os termos que ele usa como conceitos têm '
            'sempre a mesma tradução: «igualdade de condições», «estado social», «costumes» (_mœurs_, no sentido largo '
            'que ele define numa nota: os hábitos, as noções e as opiniões), «luzes» (_lumières_, a instrução difundida), '
            '«interesse bem compreendido», «tirania da maioria», «despotismo administrativo». Os sumários em itálico no '
            'começo dos capítulos e das seções são do próprio Tocqueville, e as notas do fim de cada capítulo também; as '
            'citações em inglês dessas notas vão traduzidas. As notas que ele pôs no fim de cada tomo ficam de fora.\n\n'
            '**O original.** O francês, no botão «Francês», é o da 12ª edição (Paris, Pagnerre, 1848, 4 tomos), «revista '
            'e corrigida», a última preparada pelo autor, na grafia da época. Foi tomado da transcrição do Project '
            'Gutenberg e comparado palavra por palavra com a do Wikisource e com a das _Obras completas_ de 1864–1866; os '
            '91 pontos em que divergem foram decididos nas imagens da edição de 1848.'),
        'fontes': [
            {'nome': 'De la démocratie en Amérique, 12e éd., Paris, Pagnerre, 1848, no Project Gutenberg (ebooks 30513–30516)',
             'url': 'https://www.gutenberg.org/ebooks/30513',
             'nota': 'texto francês de base e ao lado'},
            {'nome': 'A mesma edição, fac-símile no Wikimedia Commons (via Wikisource em francês)',
             'url': 'https://fr.wikisource.org/wiki/De_la_d%C3%A9mocratie_en_Am%C3%A9rique/%C3%89dition_1848',
             'nota': 'para decidir as divergências'},
            {'nome': 'Œuvres complètes, t. 1–3 (Paris, Michel Lévy, 1864–1866), no Wikisource em francês',
             'url': 'https://fr.wikisource.org/wiki/De_la_d%C3%A9mocratie_en_Am%C3%A9rique/%C3%89dition_1866',
             'nota': 'para achar divergências; dela vem a emenda «chefe do Estado» (I, 2ª parte, cap. IX)'},
        ],
    },
}

PARTES = [
    ('', 'Introdução (vol. I)', ['01-introducao.txt']),
    ('', 'Do ponto de partida e da sua importância para o futuro dos anglo-americanos (vol. I, 1ª parte, cap. II)',
     ['02-ponto-de-partida.txt']),
    ('', 'Estado social dos anglo-americanos (vol. I, 1ª parte, cap. III)', ['03-estado-social.txt']),
    ('', 'Da onipotência da maioria nos Estados Unidos e dos seus efeitos (vol. I, 2ª parte, cap. VII)',
     ['04-onipotencia-da-maioria.txt']),
    ('', 'Os costumes e a religião (vol. I, 2ª parte, cap. IX, em parte)', ['05-religiao.txt']),
    ('', 'Da fonte principal das crenças nos povos democráticos (vol. II, 1ª parte, cap. II)', ['06-fonte-das-crencas.txt']),
    ('', 'Como, nos Estados Unidos, a religião sabe servir-se dos instintos democráticos (vol. II, 1ª parte, cap. V)',
     ['07-religiao-e-instintos-democraticos.txt']),
    ('', 'Do individualismo nos países democráticos (vol. II, 2ª parte, cap. II)', ['08-individualismo.txt']),
    ('', 'Como o individualismo é maior ao sair de uma revolução democrática do que em outra época (vol. II, 2ª parte, '
         'cap. III)', ['09-individualismo-e-revolucao.txt']),
    ('', 'Como os americanos combatem o individualismo com instituições livres (vol. II, 2ª parte, cap. IV)',
     ['10-instituicoes-livres.txt']),
    ('', 'Como os americanos combatem o individualismo pela doutrina do interesse bem compreendido (vol. II, 2ª parte, '
         'cap. VIII)', ['11-interesse-bem-compreendido.txt']),
    ('', 'Como os americanos aplicam a doutrina do interesse bem compreendido em matéria de religião (vol. II, 2ª parte, '
         'cap. IX)', ['12-interesse-e-religiao.txt']),
    ('', 'Que espécie de despotismo as nações democráticas devem temer (vol. II, 4ª parte, cap. VI)', ['13-despotismo.txt']),
    ('', 'Visão geral do assunto (vol. II, 4ª parte, cap. VIII)', ['14-visao-geral.txt']),
]
