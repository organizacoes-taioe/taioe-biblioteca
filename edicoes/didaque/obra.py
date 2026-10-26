"""Didaqué (Ensinamento dos doze apóstolos), anônimo — dados para ferramentas/traducoes.py."""

META = {
    'id': 'didaque', 'autor': 'anonimo', 'titulo': 'Didaqué', 'subtitulo': 'Ensinamento dos doze apóstolos',
    'ano': 100, 'datas': 'c. 50–120', 'genero': 'Padres apostólicos',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Διδαχὴ τῶν δώδεκα ἀποστόλων'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** A _Didaqué_ é o mais antigo catecismo cristão que se conserva: uma instrução para quem se '
            'prepara para o batismo (os dois caminhos, o da vida e o da morte), seguida das normas de uma comunidade '
            'antiga sobre o batismo, o jejum, a oração, a Eucaristia, a acolhida de apóstolos e profetas, o dia do '
            'Senhor e a escolha de bispos e diáconos, e de uma exortação final à vigilância. O autor é desconhecido; '
            'a data é discutida, entre o fim do século I e o começo do II. Os Padres a conheciam e a citavam, mas o '
            'texto se perdeu e só reapareceu em 1873, num manuscrito grego de 1056 achado em Constantinopla e '
            'publicado por Filoteu Bryennios em 1883.\n\n'
            '**A divisão.** Os 16 capítulos e os versículos são os da numeração usual (as pequenas marcas no texto). '
            'Os capítulos estão agrupados em quatro partes, com títulos desta edição: os dois caminhos (1–6); o '
            'batismo, o jejum, a oração e a Eucaristia (7–10); os apóstolos, os profetas e a vida da comunidade '
            '(11–15); a vigilância e a vinda do Senhor (16).\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. O texto '
            'fala por _tu_ nos dois caminhos e por _vós_ nas normas da comunidade, como o original. As citações da '
            'Escritura, o Pai-Nosso entre elas, são traduzidas do grego da _Didaqué_, e não de uma Bíblia moderna. '
            'Onde o manuscrito é duvidoso, segue-se o texto de Lake: em 4,3, «não desejarás a divisão» (outros '
            'editores corrigem para «não farás divisão»); em 4,6, «darás um resgate pelos teus pecados».\n\n'
            '**O original.** O grego ao lado é o da edição de Kirsopp Lake (1912), na digitalização do projeto '
            'First1KGreek, com uns vinte erros de digitalização corrigidos pela edição impressa.'),
        'fontes': [
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 1 (Loeb, 1912), no First1KGreek (CC BY-SA 4.0)',
             'url': 'https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg1311/tlg001/tlg1311.tlg001.1st1K-grc1.xml',
             'nota': 'texto grego de base e ao lado'},
            {'nome': 'Διδαχή των Δώδεκα Αποστόλων (Wikisource grega)',
             'url': 'https://el.wikisource.org/wiki/%CE%94%CE%B9%CE%B4%CE%B1%CF%87%CE%AE_%CF%84%CF%89%CE%BD_%CE%94%CF%8E%CE%B4%CE%B5%CE%BA%CE%B1_%CE%91%CF%80%CE%BF%CF%83%CF%84%CF%8C%CE%BB%CF%89%CE%BD',
             'nota': 'para conferir a digitalização'},
        ],
    },
}

PARTES = [
    ('1–6', 'Os dois caminhos', ['1-os-dois-caminhos.txt']),
    ('7–10', 'O batismo, o jejum, a oração e a Eucaristia', ['2-batismo-jejum-eucaristia.txt']),
    ('11–15', 'Os apóstolos, os profetas e a vida da comunidade', ['3-a-comunidade.txt']),
    ('16', 'A vigilância e a vinda do Senhor', ['4-a-vigilancia.txt']),
]
