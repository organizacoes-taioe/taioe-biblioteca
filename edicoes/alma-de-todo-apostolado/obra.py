"""A alma de todo apostolado, de Dom J.-B. Chautard — dados para ferramentas/traducoes.py."""

META = {
    'id': 'alma-de-todo-apostolado', 'autor': 'dom-chautard',
    'titulo': 'A alma de todo apostolado',
    'ano': 1912, 'datas': 'forma definitiva de 1912; texto da 12.ª edição, 1927', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'traducao': {'lingua': 'francês', 'codigo': 'fr', 'titulo': 'L\'Âme de tout apostolat'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Dom Jean-Baptiste Chautard (1858–1935), abade trapista de Sept-Fons, escreveu para os '
            'padres, religiosos e leigos dedicados às obras um livro de uma tese só: o apostolado só dá fruto quando '
            'transborda de uma vida interior, e o homem de ação que deixa de rezar trabalha em vão. Depois de um '
            'Prelúdio em forma de oração, as cinco partes mostram que Deus quer as obras e a vida interior, como as '
            'duas se unem, o perigo da ação sem vida interior, a fecundidade que ela dá às obras e, por fim, '
            'conselhos práticos sobre a oração mental, a vida litúrgica, a guarda do coração e a devoção a Maria. O '
            'livro cresceu de edição em edição; o texto traduzido é o da 12.ª '
            'edição (Sept-Fons, 1927), estabelecido por nós sobre o exemplar digitalizado do Internet Archive e revisto '
            'página por página contra o scan, com as notas do autor.\n\n'
            '**A tradução.** Português do Brasil, fiel ao sentido e ao calor da prosa de Chautard: as exclamações, '
            'as perguntas ao leitor, as palavras grifadas. Deus e Jesus são tratados por _vós_ nas orações, como no '
            'original; quando Jesus fala à alma ou ao padre por _tu_, a tradução acompanha. As citações latinas da '
            'Escritura, da liturgia e dos Padres ficam em latim no corpo do texto, como o autor as deixa, e as '
            'traduções que ele dá nas notas foram vertidas do francês. As notas do autor aparecem no fim de cada '
            'parte. A pequena marca no começo dos capítulos (I.1) dá a parte e o capítulo.\n\n'
            '**O original ao lado.** O botão «Francês», no alto da página de leitura, mostra o texto de 1927 junto da '
            'tradução.'),
        'fontes': [
            {'nome': 'Internet Archive: L\'âme de tout apostolat, 12.ª ed., 1927',
             'url': 'https://archive.org/details/lamedetoutaposto0000unse',
             'nota': 'scan de base'},
            {'nome': 'Internet Archive: L\'âme de tout apostolat, 15.ª ed.',
             'url': 'https://archive.org/details/l-ame-de-tout-apostolat-000001218',
             'nota': 'edição posterior, para conferência'},
        ],
    },
}

PARTES = [
    ('', 'Prelúdio', ['00-preludio.txt']),
    ('I', 'Primeira parte: Deus quer as obras e a vida interior', ['01-primeira-parte.txt']),
    ('II', 'Segunda parte: união da vida ativa e da vida interior', ['02-segunda-parte.txt']),
    ('III', 'Terceira parte: a vida ativa, perigosa sem a vida interior, garante com ela o progresso na virtude',
     ['03-terceira-parte.txt']),
    ('IV', 'Quarta parte: fecundidade das obras pela vida interior',
     ['04-quarta-parte-a.txt', '04-quarta-parte-b.txt']),
    ('V', 'Quinta parte: alguns princípios e conselhos para a vida interior',
     ['05-quinta-parte-a.txt', '05-quinta-parte-b.txt', '05-quinta-parte-c.txt', '05-quinta-parte-d.txt']),
    ('', 'Epílogo', ['06-epilogo.txt']),
]
