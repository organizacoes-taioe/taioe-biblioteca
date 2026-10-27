"""Carta a Diogneto, anônimo — dados para ferramentas/traducoes.py."""

META = {
    'id': 'carta-a-diogneto', 'autor': 'anonimo', 'titulo': 'Carta a Diogneto',
    'ano': 200, 'datas': 'séc. II ou III', 'genero': 'Padres apostólicos',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Ἐπιστολὴ πρὸς Διόγνητον'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** A _Carta a Diogneto_ é uma defesa da fé cristã escrita em grego por um autor '
            'desconhecido a um pagão culto, Diogneto, que lhe perguntara em que Deus os cristãos creem, por '
            'que desprezam a morte, por que não seguem nem os deuses dos gregos nem o culto dos judeus, por que '
            'se amam tanto e por que essa raça nova só apareceu agora. A data é discutida, entre o século II e o '
            'III. Os Padres não a citam, e o texto chegou até nós num único manuscrito grego, do século XIII ou '
            'XIV, achado em Constantinopla no século XV entre obras atribuídas a São Justino. Publicado em 1592 '
            'por Henri Estienne, o manuscrito se perdeu no incêndio da biblioteca de Estrasburgo, em 1870, '
            'durante a guerra franco-prussiana; o texto depende das cópias e colações feitas antes. É dela a '
            'página mais conhecida sobre os cristãos no mundo: «o que a alma é no corpo, isso são os cristãos '
            'no mundo» (6,1).\n\n'
            '**A divisão.** Os 12 capítulos e os versículos são os da numeração usual (as pequenas marcas no '
            'texto). Os capítulos estão agrupados em quatro partes, com títulos desta edição: a dedicatória, os '
            'ídolos e os judeus (1–4); os cristãos no mundo (5–6); a revelação e o plano de Deus (7–10); o Verbo '
            'e o paraíso (11–12). O manuscrito tem lacunas, marcadas com reticências (7,6–7 e 10,1), e depois de '
            '10,8 o copista anotou outra falha no modelo que copiava. Muitos estudiosos julgam que os capítulos '
            '11 e 12 são de outro autor, talvez o fim de uma homilia, porque ali mudam o tom, o assunto e o '
            'destinatário (o autor se diz «mestre dos gentios» e fala a vários ouvintes); outros os leem como '
            'o fecho da própria carta.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos. O autor '
            'fala a Diogneto por _tu_ e passa a _vós_ quando se dirige aos pagãos em geral (cap. 2) e aos '
            'ouvintes do final; a tradução segue essas mudanças. _Logos_ é «o Verbo» quando designa o Filho. As '
            'citações e alusões à Escritura são traduzidas do grego da carta, e não de uma Bíblia moderna. '
            'Segue-se o texto de Lake também onde ele adota correções antigas do manuscrito: em 5,7, «põem a '
            'mesa em comum, mas não o leito» (o manuscrito repetia «comum»); em 12,9, «os tempos se reúnem» (o '
            'manuscrito trazia «os círios»).\n\n'
            '**O original.** O grego ao lado é o da edição de Kirsopp Lake (1913), na digitalização do projeto '
            'First1KGreek, com uma dezena de erros de digitalização corrigidos pela edição impressa.'),
        'fontes': [
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 2 (Loeb, 1913), no First1KGreek (CC BY-SA 4.0)',
             'url': 'https://github.com/OpenGreekAndLatin/First1KGreek/blob/master/data/tlg0646/tlg004/tlg0646.tlg004.1st1K-grc1.xml',
             'nota': 'texto grego de base e ao lado'},
            {'nome': 'Kirsopp Lake, The Apostolic Fathers, vol. 2 (fac-símile no Internet Archive)',
             'url': 'https://archive.org/details/TheApostolicFathersV2',
             'nota': 'para conferir a digitalização (p. 350–378)'},
            {'nome': 'Ἐπιστολὴ πρὸς Διόγνητον (Wikisource grega)',
             'url': 'https://el.wikisource.org/wiki/%CE%95%CF%80%CE%B9%CF%83%CF%84%CE%BF%CE%BB%CE%AE_%CF%80%CF%81%CE%BF%CF%82_%CE%94%CE%B9%CF%8C%CE%B3%CE%BD%CE%B7%CF%84%CE%BF%CE%BD',
             'nota': 'para conferir a digitalização'},
        ],
    },
}

PARTES = [
    ('1–4', 'A dedicatória, os ídolos e os judeus', ['1-os-idolos-e-os-judeus.txt']),
    ('5–6', 'Os cristãos no mundo', ['2-os-cristaos-no-mundo.txt']),
    ('7–10', 'A revelação e o plano de Deus', ['3-o-plano-de-deus.txt']),
    ('11–12', 'O Verbo e o paraíso', ['4-o-verbo-e-o-paraiso.txt']),
]
