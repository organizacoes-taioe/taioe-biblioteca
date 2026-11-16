"""Carta de São Clemente aos Coríntios (1 Clemente) — dados para ferramentas/traducoes.py."""

META = {
    'id': 'primeira-carta-de-clemente', 'autor': 'sao-clemente-romano', 'titulo': 'Carta aos Coríntios',
    'ano': 96, 'datas': 'c. 96', 'genero': 'Padres apostólicos',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Κλήμεντος πρὸς Κορινθίους Αʹ'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** No fim do século I, alguns membros da igreja de Corinto se levantaram contra os seus '
            'presbíteros e os tiraram do ministério. A igreja de Roma escreveu então esta carta, para pedir a paz '
            'e a volta à ordem. A carta não traz nome de autor: fala sempre a igreja de Roma, em «nós». A '
            'tradição mais antiga (Dionísio de Corinto, por volta de 170, Hegesipo, Ireneu) a atribui a '
            'Clemente, bispo de Roma, o terceiro depois de Pedro na lista de Ireneu. Costuma ser datada do fim do '
            'reinado de Domiciano, por volta do ano 96, o que a faz contemporânea dos últimos escritos do Novo '
            'Testamento. É o testemunho mais antigo do martírio de Pedro e de Paulo em Roma (capítulo 5), fala '
            'da ordem do culto e da sucessão dos apóstolos (capítulos 40 a 44) e termina com uma longa oração '
            '(capítulos 59 a 61), a mais antiga da igreja de Roma que se conserva. Foi lida por muito tempo '
            'nas assembleias de Corinto e de outras igrejas, e alguns a tiveram por Escritura.\n\n'
            '**Primeira carta.** Os manuscritos trazem, depois desta, uma «segunda carta de Clemente», que é '
            'uma homilia de outro autor, do século II. Por isso esta é chamada a primeira.\n\n'
            '**A divisão.** Os 65 capítulos e os versículos são os da numeração usual (as pequenas marcas no '
            'texto). As doze partes e os seus títulos são nossos, só para a leitura: a carta não tem divisão '
            'própria.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. A igreja '
            'de Roma fala à de Corinto por _vós_. As muitas citações da Escritura são traduzidas do grego da '
            'carta, que segue a Septuaginta e cita muitas vezes de memória, e por isso nem sempre coincidem com '
            'as Bíblias de hoje; algumas não se acham em nenhum livro conhecido. Deus é chamado na carta por '
            'dois títulos, traduzidos sempre do mesmo modo: _Senhor_ (_kýrios_) e _Soberano_ (_despótēs_). '
            'A palavra _zêlos_, a paixão que a carta acusa de ter dividido Corinto, vai por «ciúme».\n\n'
            '**O original.** O grego ao lado é o da edição de Kirsopp Lake (1912), na digitalização do projeto '
            'First1KGreek, com 91 erros de digitalização corrigidos pelo fac-símile. Em 59,3 o texto de Lake '
            'marca uma lacuna («…»): faltam ali algumas palavras, e a carta passa de repente a falar a Deus.'),
        'fontes': [
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 1 (Loeb, 1912), no First1KGreek (CC BY-SA 4.0)',
             'url': 'https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg1271/tlg001/tlg1271.tlg001.1st1K-grc1.xml',
             'nota': 'texto grego de base e ao lado'},
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 1 (fac-símile no Internet Archive)',
             'url': 'https://archive.org/details/apostolicfathers01lake',
             'nota': 'reimpressão de 1919, para conferir a digitalização (p. 8–121)'},
        ],
    },
}

PARTES = [
    ('1–3', 'A igreja de Corinto, antes e agora', ['01-corinto.txt']),
    ('4–6', 'O ciúme e os seus males', ['02-ciume.txt']),
    ('7–12', 'O arrependimento, a obediência, a fé e a hospitalidade', ['03-arrependimento.txt']),
    ('13–18', 'A humildade', ['04-humildade.txt']),
    ('19–23', 'A paz e a ordem da criação', ['05-paz.txt']),
    ('24–28', 'A ressurreição', ['06-ressurreicao.txt']),
    ('29–36', 'O caminho da santidade', ['07-santidade.txt']),
    ('37–44', 'A ordem na Igreja e a sucessão dos apóstolos', ['08-ordem.txt']),
    ('45–50', 'A discórdia de Corinto e o louvor do amor', ['09-discordia.txt']),
    ('51–58', 'O apelo aos autores da sedição', ['10-apelo.txt']),
    ('59–61', 'A grande oração', ['11-oracao.txt']),
    ('62–65', 'Conclusão', ['12-conclusao.txt']),
]
