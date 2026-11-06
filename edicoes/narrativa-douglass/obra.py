"""Narrativa da vida de Frederick Douglass (1845) — dados para ferramentas/traducoes.py."""

META = {
    'id': 'narrativa-douglass', 'indice': 'nao-ficcao-traducoes', 'autor': 'frederick-douglass',
    'titulo': 'Narrativa da vida de Frederick Douglass',
    'subtitulo': 'um escravo americano, escrita por ele mesmo',
    'ano': 1845, 'genero': 'Autobiografia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'traducao': {'lingua': 'inglês', 'codigo': 'en',
                 'titulo': 'Narrative of the Life of Frederick Douglass, an American Slave. Written by Himself'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O livro.** Frederick Douglass nasceu escravo na Costa Leste de Maryland, por volta de 1818, e fugiu '
            'em 1838, aos vinte anos. Três anos depois, numa reunião abolicionista em Nantucket, falou em público '
            'pela primeira vez e se tornou orador da Sociedade Antiescravista de Massachusetts. Como muitos '
            'duvidavam de que um homem tão eloquente tivesse sido escravo, ele escreveu a própria história, com os '
            'nomes, os lugares e as datas, sabendo que isso o expunha a ser recapturado. A _Narrativa_ saiu em '
            'Boston, em 1845, pelo Escritório Antiescravista, com um prefácio de William Lloyd Garrison e uma carta '
            'de Wendell Phillips; no fim, Douglass pôs um apêndice sobre a religião dos senhores de escravos, que '
            'termina com um poema satírico. Logo depois do livro, ele partiu para a Inglaterra, onde amigos '
            'compraram a sua liberdade (1846). Mais tarde contou a vida de novo, mais longamente, em _My Bondage '
            'and My Freedom_ (1855) e em _Life and Times_ (1881).\n\n'
            '**A tradução.** Do inglês, em português do Brasil, fiel ao sentido e ao tom de Douglass, que passa da '
            'narração seca dos fatos à indignação e à oratória. _Slave_ é «escravo»; _master_, «senhor»; '
            '_overseer_, «feitor»; _slaveholder_, «senhor de escravos». Os títulos _Mr._, _Mrs._ e _Miss_ ficam '
            'como no inglês, para não se confundirem com o «senhor» dos escravos (_Master Hugh_, «o senhor Hugh»). '
            'A palavra injuriosa que os brancos usam nas falas (_nigger_) é «crioulo», para se distinguir de '
            '_negro_, «negro», que é o termo de Douglass. As citações da Bíblia seguem a versão que ele cita, a '
            'inglesa do rei Jaime. Os versos (a cantiga dos escravos do capítulo II, os dois poemas de John '
            'Greenleaf Whittier e a paródia do fim) foram traduzidos em verso, com a medida e as rimas do original.\n\n'
            '**O original.** O inglês, no botão «Inglês», é o da primeira edição (Boston, 1845). A base é o texto '
            'do Projeto Gutenberg, conferido com dois exemplares de 1845 digitalizados no Internet Archive; onde o '
            'Gutenberg se afasta de 1845 (umas quinze palavras, a divisão de dois parágrafos, os versos de Whittier '
            'no apêndice, que ele dá como prosa), segue-se 1845. As notas de rodapé de Douglass vêm no fim de '
            'cada capítulo.'),
        'fontes': [
            {'nome': 'Narrative of the Life of Frederick Douglass (Boston, Anti-Slavery Office, 1845), exemplar do '
                     'Wellesley College no Internet Archive',
             'url': 'https://archive.org/details/narrativeoflife1845doug',
             'nota': 'primeira edição, fac-símile usado para conferir'},
            {'nome': 'A mesma edição, exemplar da Harold B. Lee Library (Brigham Young University)',
             'url': 'https://archive.org/details/narrativeoflifeo1845doug',
             'nota': 'segundo exemplar, para conferir'},
            {'nome': 'Project Gutenberg, eBook nº 23', 'url': 'https://www.gutenberg.org/ebooks/23',
             'nota': 'transcrição de base, corrigida pela edição de 1845'},
        ],
    },
}

PARTES = [
    ('', 'Prefácio de William Lloyd Garrison', ['prefacio.txt']),
    ('', 'Carta de Wendell Phillips', ['carta-de-wendell-phillips.txt']),
] + [(r, '', [f'capitulo-{k}.txt']) for k, r in enumerate('I II III IV V VI VII VIII IX X XI'.split(), 1)] + [
    ('', 'Apêndice', ['apendice.txt']),
]
