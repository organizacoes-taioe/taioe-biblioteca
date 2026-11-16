"""Vida de Santo Agostinho, de São Possídio — dados para ferramentas/traducoes.py."""

META = {
    'id': 'vida-de-santo-agostinho', 'autor': 'sao-possidio', 'titulo': 'Vida de Santo Agostinho',
    'ano': 432, 'datas': 'c. 432', 'genero': 'Hagiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Vita Sancti Augustini'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Possídio foi um dos primeiros monges do mosteiro que Agostinho fundou em Hipona, e '
            'depois bispo de Calama, na Numídia; viveu perto dele quase quarenta anos e estava junto do seu leito '
            'quando ele morreu, em agosto de 430, na cidade cercada pelos vândalos. Escreveu esta vida pouco '
            'depois, por volta de 432: é a primeira biografia de Agostinho e a única de quem o conheceu. Não repete '
            'as _Confissões_, que cita ao começar: conta o que veio depois delas, o presbítero e o bispo, as '
            'disputas com maniqueus, donatistas, arianos e pelagianos, e sobretudo o modo de vida de Agostinho, a '
            'mesa, a casa, o dinheiro da Igreja, as visitas e a morte. No capítulo 30 Possídio copia inteira a carta '
            'em que Agostinho responde ao bispo Honorato se os clérigos deviam fugir diante dos invasores.\n\n'
            '**A divisão.** Os 31 capítulos e o prefácio são os de todas as edições (as pequenas marcas no texto). '
            'Estão agrupados em seis partes, com títulos desta edição: da conversão ao sacerdócio (prefácio e 1–5); '
            'o bispo de Hipona (6–11); as controvérsias (12–18); como vivia (19–27); os vândalos e a carta a '
            'Honorato (28–30); a morte (31). No fim do capítulo 18 Possídio promete juntar ao livro a lista das obras '
            'de Agostinho, o _Indiculus_; ela não está aqui: é só uma relação de títulos, que a edição de base '
            'imprime à parte.\n\n'
            '**A tradução.** Do latim, em português do Brasil, fiel ao sentido e ao tom, sem acréscimos nem '
            'explicações. Possídio escreve frases longas, cheias de pares de palavras quase sinônimas («exorta e '
            'admoesta», «pede e suplica»), que a tradução conserva quando dão o tom e encurta quando são só '
            'enchimento. Chama Agostinho muitas vezes de _sacerdos_, que no latim do tempo dizia sobretudo o bispo: '
            'fica «sacerdote» quando fala dele, e «bispos» onde o sentido é claramente esse (os concílios, as '
            'ordenações). Os nomes vão na forma portuguesa (Agostinho, Valério, Ambrósio, Megálio, Crispino, '
            'Emérito, Pascêncio, Maximino, Honorato, Bonifácio) e os lugares na forma de hoje (Tagaste, Hipona, '
            'Cartago, Milão, Calama, Cirta, Cesareia da Mauritânia). As citações da Escritura são traduzidas do '
            'latim de Possídio e de Agostinho; as referências entre parênteses, com os salmos na numeração da '
            'Vulgata seguida da hebraica, foram postas por nós. Os dois dísticos latinos, a inscrição da mesa de '
            'Agostinho e o epitáfio de um poeta, vão em verso livre.\n\n'
            '**O original.** O latim ao lado é o dos beneditinos de São Mauro (Paris, 1679–1700), na _Patrologia '
            'Latina_ de Migne, vol. 32 (Paris, 1841), col. 33–66, sem as notas e sem as referências bíblicas que os '
            'editores puseram no texto. Foi estabelecido por nós a partir de quatro leituras automáticas de três '
            'tiragens (1841, 1844 e 1845), comparadas palavra por palavra, e conferido, coluna por coluna, nas '
            'imagens da tiragem de 1845. A grafia é a da edição (_ejus_, _charitas_, _lacrymas_). No capítulo 30 '
            'a edição de Migne copia só o começo da carta a Honorato e manda o leitor à carta 228 das obras de '
            'Agostinho; o resto da carta (§§ 10–14) foi completado aqui pela mesma edição, vol. 33 (col. '
            '1017–1019), conferida da mesma maneira. A edição crítica de Herbert T. Weiskotten (Princeton, 1919) '
            'serviu só para comparar.'),
        'fontes': [
            {'nome': 'Sancti Aurelii Augustini Opera omnia, t. 1 (Patrologia Latina 32; Paris, Migne, 1841), no Internet Archive',
             'url': 'https://archive.org/details/sanctiaureliiau01augu',
             'nota': 'edição de base, col. 33–66'},
            {'nome': 'Patrologia Latina 32 (Paris, Migne, 1845), no Internet Archive',
             'url': 'https://archive.org/details/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_32',
             'nota': 'fac-símile em que o texto foi conferido'},
            {'nome': 'Patrologia Latina 33 (Paris, Migne, 1845), no Internet Archive',
             'url': 'https://archive.org/details/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1845_33',
             'nota': 'Epístola 228, §§ 10–14 (col. 1017–1019): o fim da carta a Honorato, no cap. 30'},
            {'nome': 'Herbert T. Weiskotten, Sancti Augustini vita scripta a Possidio episcopo (Princeton, 1919), no Internet Archive',
             'url': 'https://archive.org/details/sanctiaugustiniv00possrich',
             'nota': 'edição crítica, só para comparar'},
        ],
    },
}

PARTES = [
    ('Pref., 1–5', 'Da conversão ao sacerdócio', ['prefacio.txt', 'vita.txt#1-5']),
    ('6–11', 'O bispo de Hipona', ['vita.txt#6-11']),
    ('12–18', 'As controvérsias', ['vita.txt#12-18']),
    ('19–27', 'Como vivia', ['vita.txt#19-27']),
    ('28–30', 'Os vândalos e a carta a Honorato', ['vita.txt#28-30']),
    ('31', 'A morte', ['vita.txt#31-31']),
]
