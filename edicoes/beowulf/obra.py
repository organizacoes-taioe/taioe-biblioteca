"""Beowulf — dados para ferramentas/traducoes.py."""

META = {
    'id': 'beowulf', 'autor': 'anonimo-anglo-saxao', 'titulo': 'Beowulf',
    'genero': 'Poesia', 'poema': True, 'indice': 'literatura',
    'divisao': {'singular': 'canto', 'plural': 'cantos'},
    'traducao': {'lingua': 'inglês antigo', 'codigo': 'ang', 'titulo': 'Bēowulf'},
    'original_ao_lado': True,
    'descricao': ('O poema heroico do inglês antigo: Beowulf, príncipe dos geatas, livra o salão de Hrothgar de '
                  'Grendel e da mãe dele e, já velho e rei, morre matando o dragão. Tradução verso a verso, com '
                  'a cesura e a aliteração do original, que pode ser lido ao lado.'),
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O poema.** _Beowulf_ é o mais longo e o maior dos poemas do inglês antigo: 3.182 versos (3.184 na '
            'numeração da edição usada aqui), de autor desconhecido, composto na Inglaterra anglo-saxã entre o '
            'século VIII e o começo do XI e conservado num só manuscrito, copiado por volta do ano 1000 (Londres, '
            'British Library, Cotton Vitellius A.xv), que o incêndio da biblioteca Cotton, em 1731, chamuscou nas '
            'bordas. A ação se passa na Escandinávia do século VI, entre dinamarqueses, geatas e suecos; o poeta é '
            'cristão e conta a vida de heróis pagãos. Beowulf atravessa o mar para livrar o salão Heorot, do rei '
            'Hrothgar, de Grendel, o monstro da linhagem de Caim, e depois da mãe dele; cinquenta anos mais tarde, '
            'rei dos geatas, enfrenta o dragão que guarda um tesouro e morre na vitória.\n\n'
            '**O texto.** A tradução segue a edição de James A. Harrison e Robert Sharp (4.ª edição, Boston, '
            '1894), feita sobre a de Moritz Heyne, na transcrição revista do Projeto Gutenberg. A divisão em 43 '
            'seções e os títulos delas (aqui traduzidos) são dos editores; o manuscrito numera as seções, mas não '
            'lhes dá título. Onde o manuscrito queimado perdeu letras ou palavras, a edição e a tradução marcam a '
            'lacuna com pontos, sem completá-la. O volume de Harrison e Sharp traz em apêndice o fragmento de '
            '_Finnsburh_, que conta a luta de que o poeta de _Beowulf_ canta o desfecho nos cantos XVII e XVIII; ele vem '
            'aqui também, no fim.\n\n'
            '**A tradução.** Verso a verso, do inglês antigo, em português do Brasil. O verso do _Beowulf_ não '
            'tem rima nem conta sílabas: cada verso tem duas metades separadas por uma pausa, cada metade dois '
            'tempos fortes, e a aliteração (palavras que começam pelo mesmo som) amarra as duas metades. A '
            'tradução guarda essa medida, como o método do Versificador manda guardar a do original: a pausa '
            'no meio do verso, os dois tempos de cada metade e, sempre que o sentido deixa, a aliteração. Guarda '
            'também o que faz o estilo do poema: as aposições (o mesmo herói nomeado duas e três vezes no mesmo '
            'fôlego), os compostos e as metáforas condensadas, os _kennings_ (o mar é o «caminho da baleia», o '
            'corpo, a «casa dos ossos»), e as fórmulas, traduzidas sempre do mesmo modo. Os nomes ficam na forma do '
            'inglês antigo, sem os acentos de quantidade, com _th_ no lugar de _þ_ e _ð_.\n\n'
            '**O original ao lado.** O botão «Inglês antigo», no alto da página de leitura, mostra o texto da '
            'edição junto da tradução, verso com verso.'),
        'fontes': [
            {'nome': 'Project Gutenberg, eBook nº 9701 (Harrison e Sharp, 4.ª ed., versão revista)',
             'url': 'https://www.gutenberg.org/ebooks/9701', 'nota': 'texto de base'},
            {'nome': 'Project Gutenberg, eBook nº 9700 (a mesma edição, com a acentuação do impresso)',
             'url': 'https://www.gutenberg.org/ebooks/9700', 'nota': 'para conferência'},
        ],
    },
}

TITULOS = [
    'A partida de Scyld', 'O salão Heorot', 'As visitas de Grendel', 'O vassalo de Hygelac', 'A missão',
    'A fala de Beowulf', 'As boas-vindas de Hrothgar', 'Hrothgar fala de Grendel', 'Unferth provoca Beowulf',
    'A disputa de Beowulf com Breca. O banquete', 'A vigília à espera de Grendel', 'O ataque de Grendel',
    'Beowulf arranca o braço de Grendel', 'A alegria em Heorot', 'O louvor de Hrothgar', 'O banquete e os presentes',
    'O canto do poeta de Hrothgar: a balada de Hnæf e Hengest', 'Termina a história do menestrel',
    'O colar de Beowulf. Os heróis repousam', 'A mãe de Grendel ataca os dinamarqueses dos anéis',
    'Luto em Heorot: a morte de Æschere', 'Beowulf busca o monstro no covil das feras das águas',
    'A batalha com o dragão das águas', 'Beowulf mata o espectro', 'A gratidão de Hrothgar. O discurso do rei',
    'Fim do discurso. Beowulf se prepara para partir', 'As palavras de despedida',
    'Beowulf volta à terra dos geatas. As rainhas Hygd e Thryth', 'A chegada. Hygelac recebe Beowulf',
    'Beowulf conta os combates', 'Os presentes a Hygelac. A recompensa. A morte de Hygelac. Beowulf reina',
    'O dragão de fogo. O tesouro', 'Beowulf decide matar o dragão de fogo',
    'Beowulf relembra. A guerra entre suecos e geatas', 'Memórias do passado. O combate com o dragão de fogo',
    'Wiglaf socorre Beowulf no combate', 'Beowulf ferido de morte', 'O tesouro de joias. A partida de Beowulf',
    'Os vassalos covardes', 'O lamento e a profecia do mensageiro', 'O relato dos suecos e dos geatas',
    'Wiglaf fala. A construção da pira', 'A pira de Beowulf',
]

ROMANOS = ('I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XXIV XXV XXVI '
           'XXVII XXVIII XXIX XXX XXXI XXXII XXXIII XXXIV XXXV XXXVI XXXVII XXXVIII XXXIX XL XLI XLII XLIII').split()

PARTES = [(r, t, [f'{k:02d}.txt']) for k, (r, t) in enumerate(zip(ROMANOS, TITULOS), 1)] + [
    ('', 'Apêndice: o combate em Finnsburh', ['finnsburh.txt'])]
