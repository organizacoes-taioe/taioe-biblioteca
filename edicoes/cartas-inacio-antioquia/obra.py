"""Cartas de Santo Inácio de Antioquia (as sete da recensão média) — dados para ferramentas/traducoes.py."""

META = {
    'id': 'cartas-inacio-antioquia', 'autor': 'santo-inacio-de-antioquia', 'titulo': 'Cartas',
    'subtitulo': 'As sete cartas a caminho do martírio',
    'ano': 107, 'datas': 'c. 107–110', 'genero': 'Padres apostólicos',
    'divisao': {'singular': 'carta', 'plural': 'cartas', 'rotulo': 'nome'},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Ἰγνατίου ἐπιστολαί'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Inácio, bispo de Antioquia da Síria, foi preso no tempo do imperador Trajano e levado '
            'a Roma, sob a guarda de soldados, para morrer nas feras. No caminho escreveu sete cartas: em '
            'Esmirna, aos Efésios, aos Magnésios, aos Tralianos e aos Romanos; em Trôade, aos Filadélfios, aos '
            'Esmirnenses e ao bispo deles, Policarpo. São os escritos cristãos mais antigos depois do Novo '
            'Testamento a falar com tanta clareza do bispo, dos presbíteros e dos diáconos, da Eucaristia, da '
            'unidade da Igreja e da verdade da carne de Cristo contra os que diziam que ele sofrera só em '
            'aparência. É dele a primeira menção conhecida da «Igreja católica» (Esmirnenses 8,2) e a página '
            'mais citada sobre o martírio: «Sou trigo de Deus, e sou moído pelos dentes das feras» (Romanos '
            '4,1). A data tradicional é por volta de 107; muitos estudiosos preferem os anos de 110 a 117.\n\n'
            '**As sete cartas.** As cartas de Inácio circularam em três formas: uma longa, com seis cartas '
            'falsas acrescentadas e as verdadeiras interpoladas no século IV; uma curta, em siríaco, só com três '
            'cartas resumidas; e a média, que é a que se lê aqui, com as sete cartas que Eusébio de Cesareia já '
            'conhecia, e que a maior parte dos estudiosos, desde Zahn e Lightfoot, tem por autêntica.\n\n'
            '**A divisão.** Uma página por carta, na ordem de Eusébio e das edições. Os capítulos e os '
            'versículos são os da numeração usual (as pequenas marcas no texto); a saudação que abre cada carta '
            'vem sem número.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. A frase '
            'de Inácio é densa e às vezes se interrompe, e a tradução não a completa nem a alisa. Ele fala às '
            'igrejas por _vós_ e a Policarpo por _tu_. As citações da Escritura são traduzidas do grego das '
            'cartas, e não de uma Bíblia moderna. Onde os manuscritos divergem, segue-se o texto de Lake: em '
            'Efésios 7,2, «gerado e não gerado».\n\n'
            '**O original.** O grego ao lado é o da edição de Kirsopp Lake (1912), na digitalização do projeto '
            'First1KGreek, com uns cento e vinte erros de digitalização corrigidos e quatro números de '
            'versículo repostos.'),
        'fontes': [
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 1 (Loeb, 1912), no First1KGreek (CC BY-SA 4.0)',
             'url': 'https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg1443/tlg001/tlg1443.tlg001.1st1K-grc1.xml',
             'nota': 'texto grego de base e ao lado'},
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 1 (fac-símile no Internet Archive)',
             'url': 'https://archive.org/details/apostolicfathers01lake',
             'nota': 'reimpressão de 1919, para conferir a digitalização (p. 172–277)'},
        ],
    },
}

PARTES = [
    ('Ef', 'Aos Efésios', ['1-efesios.txt']),
    ('Mg', 'Aos Magnésios', ['2-magnesios.txt']),
    ('Tr', 'Aos Tralianos', ['3-tralianos.txt']),
    ('Rm', 'Aos Romanos', ['4-romanos.txt']),
    ('Fld', 'Aos Filadélfios', ['5-filadelfios.txt']),
    ('Esm', 'Aos Esmirnenses', ['6-esmirnenses.txt']),
    ('Pol', 'A Policarpo', ['7-policarpo.txt']),
]
