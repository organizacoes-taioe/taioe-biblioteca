"""Diálogo da Divina Providência, de Santa Catarina de Sena — dados para ferramentas/traducoes.py."""

META = {
    'id': 'dialogo', 'autor': 'santa-catarina-de-sena', 'titulo': 'Diálogo da Divina Providência',
    'subtitulo': 'ou Livro da Divina Doutrina',
    'ano': 1378, 'datas': '1377–1378', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'marcas': False},
    'traducao': {'lingua': 'italiano', 'codigo': 'it', 'titulo': 'Libro della divina dottrina'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e a autora.** Catarina Benincasa, filha de um tintureiro de Sena, terciária dominicana '
            '(uma _mantelata_, das que vestiam o manto da ordem e viviam em casa), não aprendeu a escrever senão '
            'tarde, e ditava. Ditou este livro em 1377 e 1378, nos últimos anos de vida, em parte, segundo os '
            'discípulos, em êxtase; o códice de Sena diz que foi terminado em outubro de 1378. Os discípulos o '
            'chamaram _Libro della divina dottrina_; o nome de _Diálogo_, com que ficou conhecido, vem da forma: '
            'uma alma (a própria Catarina, que fala de si na terceira pessoa) faz quatro pedidos a Deus Pai, e '
            'ele responde, longamente, a cada um, com as orações dela de permeio. Catarina morreu em Roma em '
            '1380, aos 33 anos; foi canonizada em 1461 e declarada doutora da Igreja em 1970.\n\n'
            '**A divisão.** Os 167 capítulos e os seus títulos (rubricas) são os do códice, na numeração de '
            'Gigli (1707) e de Fiorilli (1912). Os capítulos se agrupam, como nessas edições, num prólogo (1–8) '
            'e em quatro tratados: da discrição (9–64), onde está a imagem de Cristo como Ponte entre o céu e a '
            'terra; da oração (65–134), com os estados das lágrimas e os ministros da Igreja; da providência '
            '(135–153); e da obediência (154–167).\n\n'
            '**A tradução.** Do italiano do século XIV, em português do Brasil, fiel ao sentido e ao movimento da '
            'prosa ditada de Catarina, com os seus períodos longos, as retomadas e as repetições de propósito, sem '
            'acréscimos. Deus Pai trata a alma por _tu_, e ela a ele; aos homens em geral ele fala por _vós_. '
            'Mantêm-se os termos dela: a _discrição_ (o discernimento que dá a cada um o que lhe é devido), o '
            '_conhecimento de si_, o _afeto_ (o movimento do amor na vontade), a _sensualidade_ (a parte sensitiva '
            'da alma e o amor desordenado a ela), o _lume_ da fé e do intelecto. _Verdade_, com maiúscula, é Deus '
            'ou o Filho, «a minha Verdade», como Catarina escreve. As citações da Escritura são traduzidas como '
            'ela as cita, de memória, sem referências, que ela não dá.\n\n'
            '**O original.** O italiano, no botão «Italiano», é o da edição de Matilde Fiorilli (_Libro della '
            'divina dottrina, volgarmente detto Dialogo della divina provvidenza_, Bari, Laterza, 1912, coleção '
            '«Scrittori d\'Italia»), feita sobre o códice T.II.9 da Biblioteca Comunal de Sena, do século XIV, '
            'com a grafia do códice (_virtú_, _caritá_, _sancto_, _cognoscimento_). Partimos da transcrição do '
            'Wikisource italiano, revista duas vezes sobre o fac-símile da edição. A «Nota» de Fiorilli sobre os '
            'códices ficou de fora.'),
        'fontes': [
            {'nome': 'Libro della divina dottrina (Caterina da Siena - Fiorilli), Wikisource em italiano',
             'url': 'https://it.wikisource.org/wiki/Libro_della_divina_dottrina_(Caterina_da_Siena_-_Fiorilli)',
             'nota': 'transcrição da edição de 1912, revista sobre o fac-símile; base do italiano'},
            {'nome': 'Caterina da Siena, Libro della divina dottrina (Bari, Laterza, 1912), fac-símile da BEIC no Wikimedia Commons',
             'url': 'https://commons.wikimedia.org/wiki/File:Caterina_da_Siena_%E2%80%93_Libro_della_divina_dottrina,_1912_%E2%80%93_BEIC_1785736.djvu',
             'nota': 'edição usada no original ao lado'},
        ],
    },
}

PARTES = [
    ('I', 'Prólogo', ['prologo.txt']),
    ('II', 'Tratado da discrição', ['discricao.txt']),
    ('III', 'Tratado da oração', ['oracao.txt']),
    ('IV', 'Tratado da providência', ['providencia.txt']),
    ('V', 'Tratado da obediência', ['obediencia.txt']),
]
