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
        'apresentacao': 'A ESCREVER no fim (ver FALTA.md).',
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
