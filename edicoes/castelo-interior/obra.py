"""Castelo interior (As moradas), de Santa Teresa de Jesus — dados para ferramentas/traducoes.py."""

META = {
    'id': 'castelo-interior', 'autor': 'santa-teresa-de-jesus',
    'titulo': 'Castelo interior (As moradas)',
    'ano': 1577, 'datas': '1577', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'morada', 'plural': 'moradas', 'rotulo': 'nome'},
    'traducao': {'lingua': 'castelhano', 'codigo': 'es', 'titulo': 'Castillo interior o Las moradas'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Teresa de Jesus escreveu o _Castelo interior_ por ordem do padre Jerônimo Gracián, '
            'o seu superior, e do seu confessor, o doutor Alonso Velázquez, para as monjas dos mosteiros '
            'carmelitas descalços que tinha fundado. Começou-o em Toledo, no dia da Santíssima Trindade, 2 de junho '
            'de 1577, e acabou-o em Ávila, no mosteiro de São José, na véspera de Santo André, 29 de novembro do '
            'mesmo ano, com uma longa interrupção no meio. Tinha sessenta e dois anos e escrevia doente, «com a '
            'cabeça», diz ela, «com um ruído e fraqueza tão grande». A imagem que organiza o livro lhe ocorreu '
            'logo no começo: a alma é um castelo de diamante ou de cristal muito claro, com muitos aposentos, e '
            'no centro dele mora o Rei; a porta é a oração. As sete moradas são os graus do caminho que vai do '
            'conhecimento próprio, nas primeiras, às mercês da oração de quietude e de união, ao desposório '
            'espiritual e, nas sétimas, ao matrimônio espiritual. O livro saiu pela primeira vez em 1588, na '
            'edição das obras de Teresa preparada por frei Luís de León em Salamanca.\n\n'
            '**A divisão.** As sete moradas e os seus capítulos são os de Teresa; cada capítulo leva uma ementa '
            '(«Em que trata…»), que serve de título; o prólogo vem antes das primeiras moradas, e o epílogo depois das '
            'sétimas. A pequena marca no começo de cada capítulo (I.1) dá a morada e o capítulo, como se cita a '
            'obra.\n\n'
            '**A tradução.** Do castelhano, em português do Brasil, fiel ao sentido e ao modo de Teresa, que '
            'escreve como fala: frases longas que mudam de rumo, parênteses, voltas ao assunto, desculpas por não '
            'saber dizer, exclamações. A sintaxe foi arrumada só o necessário para ficar clara. Teresa fala às '
            'irmãs por _vós_, e assim ficou; quando fala com Deus, «Vós», com maiúscula. Os termos da oração '
            'seguem o uso dela, sempre do mesmo modo: oração de recolhimento, de quietude, de união; '
            'contentamentos e gostos (a diferença que ela mesma explica nas quartas moradas); arroubamento, voo '
            'do espírito, desposório e matrimônio espiritual. As formas antigas do castelhano dela (_ansí_, '
            '_mesmo_, _terná_, _dinidad_) saem em português de hoje. As citações da Escritura foram traduzidas '
            'como ela as faz, de memória; o latim que ela escreve ficou em latim.\n\n'
            '**O original.** O castelhano, no botão «Castelhano», é o da edição do padre Silverio de Santa '
            'Teresa, carmelita descalço (_Obras de Santa Teresa de Jesús_, t. IV, Burgos, 1917), feita sobre o '
            'autógrafo, que se guarda no convento das carmelitas descalças de Sevilha. Silverio atualiza a '
            'ortografia, mas guarda as formas da língua de Teresa (_ansí_, _mesmo_, _inorancia_, _relisión_, '
            '_terná_) e deixa de fora as emendas que outras mãos puseram no autógrafo; os colchetes são dele '
            '(letras e palavras que faltam no autógrafo). Partimos de quatro exemplares digitalizados dessa '
            'edição, lidos por dois programas de OCR e comparados palavra por palavra; as divergências foram '
            'conferidas nas imagens. As notas de Silverio ficaram de fora.'),
        'fontes': [
            {'nome': 'Silverio de Santa Teresa (ed.), Obras de Santa Teresa de Jesús, t. IV (Burgos, El Monte Carmelo, 1917), no Internet Archive',
             'url': 'https://archive.org/details/obrasdestateresa04tere',
             'nota': 'edição-base; com os exemplares obrasdesantatere04tere, bwb_Y0-AAF-301 e bwb_C0-ANN-573'},
            {'nome': 'El castillo interior ó Tratado de las moradas, edição autografada do manuscrito (Sevilha, 1882), no Internet Archive',
             'url': 'https://archive.org/details/elcastillointeri00tere',
             'nota': 'fac-símile do autógrafo'},
        ],
    },
}

PARTES = [
    ('', 'Prólogo', ['00-prologo.txt']),
    ('I', 'Primeiras moradas', ['01-primeiras-moradas.txt']),
    ('II', 'Segundas moradas', ['02-segundas-moradas.txt']),
    ('III', 'Terceiras moradas', ['03-terceiras-moradas.txt']),
    ('IV', 'Quartas moradas', ['04-quartas-moradas.txt']),
    ('V', 'Quintas moradas', ['05-quintas-moradas.txt']),
    ('VI', 'Sextas moradas', ['06-sextas-moradas.txt']),
    ('VII', 'Sétimas moradas', ['07-setimas-moradas.txt']),
    ('', 'Epílogo', ['08-epilogo.txt']),
]
