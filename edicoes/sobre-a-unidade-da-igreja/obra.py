"""Sobre a unidade da Igreja católica, de São Cipriano — dados para ferramentas/traducoes.py."""

META = {
    'id': 'sobre-a-unidade-da-igreja', 'autor': 'sao-cipriano', 'titulo': 'Sobre a unidade da Igreja católica',
    'ano': 251, 'datas': '251', 'genero': 'Tratado',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'De catholicae ecclesiae unitate'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Cipriano, retórico de Cartago convertido já adulto, foi eleito bispo da cidade por volta '
            'de 248. Na perseguição de Décio (250–251) muitos cristãos renegaram a fé para salvar a vida: são os '
            '«caídos». Quando a perseguição cessou, a Igreja se dividiu sobre o modo de recebê-los de volta. Em '
            'Cartago, alguns presbíteros contrários a Cipriano, apoiados por confessores (os que tinham sofrido pela '
            'fé sem renegar), formaram um grupo à parte; em Roma, Novaciano fez-se ordenar bispo contra o papa '
            'Cornélio. Cipriano escreveu este tratado em 251, talvez para ler no concílio de Cartago daquela '
            'primavera: a Igreja é uma só, como um só é Cristo, e quem dela se separa perde a salvação, ainda que '
            'morra mártir. Dele são frases que a Igreja nunca deixou de repetir: «Não pode ter Deus por Pai quem não '
            'tem a Igreja por mãe» (6). Cipriano morreu mártir em 258, sob Valeriano.\n\n'
            '**A divisão.** Os 27 capítulos são os da edição de Hartel (as pequenas marcas no texto), pelos quais a '
            'obra se cita. Estão agrupados em seis partes, com títulos desta edição: as ciladas do inimigo (1–3); a '
            'Igreja una (4–9); os que se separam (10–13); fora da Igreja não há martírio (14–19); os confessores '
            '(20–22); a paz e a vigilância (23–27).\n\n'
            '**As duas redações do capítulo 4.** O capítulo 4, sobre Pedro, chegou até nós em duas formas. A mais '
            'difundida nos manuscritos, que Hartel segue e que vai no texto, diz que o Senhor edifica a Igreja sobre '
            'um só e dá depois a todos os apóstolos igual poder, para que a unidade comece de um. A outra, que só '
            'alguns manuscritos trazem, fala ainda da ordem de apascentar as ovelhas, do «primado dado a Pedro» e da '
            '«cátedra de Pedro»; Hartel a julgou acréscimo posterior e a deixou no aparato, onde a dá pelo códice M. '
            'Desde o século XVI a questão foi discutida entre católicos e protestantes; muitos estudiosos pensam hoje '
            'que as duas redações são do próprio Cipriano, que teria revisto o capítulo. A tradução segue Hartel no '
            'texto e dá a outra redação, como está no códice M, num bloco à parte logo depois do capítulo 4.\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos nem '
            'explicações. Cipriano fala aos fiéis por _vós_ e chama-os «irmãos caríssimos». Chama _sacerdotes_ aos '
            'bispos, como era comum no seu tempo; a tradução mantém a palavra. As citações da Escritura são traduzidas '
            'do latim de Cipriano, que cita uma versão anterior à Vulgata; as referências entre parênteses vêm da '
            'margem de Hartel, nas abreviaturas usuais no Brasil, com os salmos na numeração da Vulgata seguida da '
            'hebraica.\n\n'
            '**O original.** O latim ao lado é o da edição de Wilhelm Hartel, _Corpus Scriptorum Ecclesiasticorum '
            'Latinorum_, vol. 3/1 (Viena, 1868), p. 209–233, com a grafia dele (_adque_, _inmortalitas_), sem o '
            'aparato. Foi lido por nós nas imagens do volume, página por página, e conferido com duas leituras '
            'automáticas de dois exemplares.'),
        'fontes': [
            {'nome': 'Wilhelm Hartel, S. Thasci Caecili Cypriani opera omnia, CSEL 3/1 (Viena, 1868), no Internet Archive',
             'url': 'https://archive.org/details/sthascicaecilic00hartgoog',
             'nota': 'fac-símile da edição de base (p. 209–233; o aparato do cap. 4 nas p. 212–213); texto latino ao lado'},
            {'nome': 'O mesmo volume, outro exemplar, no Internet Archive',
             'url': 'https://archive.org/details/sthascicaecilic03cyprgoog',
             'nota': 'para a conferência'},
            {'nome': 'De unitate ecclesiae (Wikisource latina, texto de Migne, PL 4)',
             'url': 'https://la.wikisource.org/wiki/De_unitate_ecclesiae',
             'nota': 'outra edição (Baluze), só para comparar'},
        ],
    },
}

PARTES = [
    ('1–3', 'As ciladas do inimigo', ['unitate.txt#1-3']),
    ('4–9', 'A Igreja una', ['unitate.txt#4-9']),
    ('10–13', 'Os que se separam', ['unitate.txt#10-13']),
    ('14–19', 'Fora da Igreja não há martírio', ['unitate.txt#14-19']),
    ('20–22', 'Os confessores', ['unitate.txt#20-22']),
    ('23–27', 'A paz e a vigilância', ['unitate.txt#23-27']),
]
