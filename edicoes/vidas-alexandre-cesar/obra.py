"""Plutarco, Vidas paralelas: Alexandre e César — dados para ferramentas/traducoes.py."""

META = {
    'id': 'vidas-alexandre-cesar', 'indice': 'nao-ficcao-traducoes', 'autor': 'plutarco',
    'titulo': 'Vidas paralelas: Alexandre e César',
    'ano': 110, 'datas': 'c. 100–120', 'genero': 'Biografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'agrupar': True},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Βίοι Παράλληλοι: Ἀλέξανδρος καὶ Καῖσαρ'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** Plutarco nasceu por volta do ano 46 em Queroneia, na Beócia, onde passou quase '
            'toda a vida; foi sacerdote de Apolo em Delfos e morreu depois de 119. Das suas _Vidas paralelas_, '
            'escritas nos últimos vinte anos da vida, restam 23 pares: em cada um, um grego e um romano, contados '
            'lado a lado e, em geral, comparados no fim. Este é o mais célebre, Alexandre, rei da Macedônia (356–323 '
            'a.C.), e Caio Júlio César (100–44 a.C.). Plutarco avisa logo no começo que não escreve história, mas '
            'vidas: busca o caráter, que muitas vezes se mostra melhor num dito ou numa brincadeira do que nas '
            'grandes batalhas, e por isso resume as guerras e se demora nas anedotas. A comparação que costuma '
            'fechar cada par perdeu-se neste, e muitos estudiosos acham que se perdeu também o começo da _Vida de '
            'César_, que abre de repente, já no casamento dele com Cornélia.\n\n'
            '**A divisão.** Os capítulos e as seções são os da numeração usual (as pequenas marcas no texto: 1.1 é o '
            'capítulo 1, seção 1), 77 capítulos na _Vida de Alexandre_ e 69 na de César. Os grupos de capítulos e os '
            'títulos deles são desta edição, para a leitura em partes.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e à ordem das ideias, sem acréscimos; '
            'as frases longas de Plutarco foram desdobradas onde o português pedia. Os nomes estão na forma '
            'portuguesa usual, e os romanos voltam à forma latina (Pompeu, Cipião, Lúculo). Os cargos de Roma, que '
            'Plutarco dá com palavras gregas, levam o nome romano: cônsul, pretor, questor, edil, tribuno da plebe, '
            'pontífice máximo. Os versos citados vão em verso livre. Em duas passagens o texto dos manuscritos se '
            'perdeu (os «…» em Alexandre 35.6 e César 42.1).\n\n'
            '**O original.** O grego, no botão «Grego», é o da edição de Bernadotte Perrin (_Plutarch\'s Lives_, vol. '
            'VII, coleção Loeb, 1919), em domínio público, que segue em geral o texto de Sintenis (Teubner, 1873–1875). '
            'Partimos da transcrição da Perseus Digital Library e a comparamos, palavra por palavra, com o fac-símile '
            'da edição de 1919; corrigimos pela imagem uns 60 erros de digitação (sílabas perdidas, palavras '
            'trocadas, restos soltos, uma oração repetida) e 355 acentos. Ficaram de fora as notas críticas de Perrin, '
            'e a tradução inglesa dele, ao lado do grego na edição Loeb, serviu só para conferir o sentido.'),
        'fontes': [
            {'nome': 'Bernadotte Perrin, Plutarch\'s Lives, vol. VII (Loeb, 1919), no Internet Archive',
             'url': 'https://archive.org/details/plutarchslives07plut',
             'nota': 'fac-símile da edição do texto grego ao lado (p. 224–609); conferência das correções'},
            {'nome': 'Perseus Digital Library: Plutarco, Alexandre e César (texto de Perrin, CC BY-SA 4.0)',
             'url': 'https://github.com/PerseusDL/canonical-greekLit/tree/master/data/tlg0007',
             'nota': 'transcrição do grego de Perrin, base do texto ao lado (tlg047 e tlg048)'},
        ],
    },
}

PARTES = [
    ('Alexandre', 'Origem, infância e educação (1–8)', ['alexandre-1-8.txt']),
    ('Alexandre', 'A subida ao trono (9–14)', ['alexandre-9-14.txt']),
    ('Alexandre', 'Do Grânico a Isso (15–21)', ['alexandre-15-21.txt']),
    ('Alexandre', 'Tiro, o Egito e Amon (22–30)', ['alexandre-22-30.txt']),
    ('Alexandre', 'Gaugamela, Babilônia e Persépolis (31–38)', ['alexandre-31-38.txt']),
    ('Alexandre', 'A morte de Dario (39–47)', ['alexandre-39-47.txt']),
    ('Alexandre', 'Filotas, Clito e Calístenes (48–55)', ['alexandre-48-55.txt']),
    ('Alexandre', 'A Índia (56–67)', ['alexandre-56-67.txt']),
    ('Alexandre', 'A volta e a morte (68–77)', ['alexandre-68-77.txt']),
    ('César', 'A juventude (1–4)', ['cesar-1-4.txt']),
    ('César', 'A carreira em Roma (5–14)', ['cesar-5-14.txt']),
    ('César', 'A Gália (15–21)', ['cesar-15-21.txt']),
    ('César', 'Germanos, bretões e Vercingetórix (22–27)', ['cesar-22-27.txt']),
    ('César', 'O Rubicão (28–35)', ['cesar-28-35.txt']),
    ('César', 'De Dirráquio a Farsália (36–46)', ['cesar-36-46.txt']),
    ('César', 'Egito, Ásia, África e Hispânia (47–56)', ['cesar-47-56.txt']),
    ('César', 'O ditador (57–61)', ['cesar-57-61.txt']),
    ('César', 'Os Idos de Março (62–69)', ['cesar-62-69.txt']),
]
