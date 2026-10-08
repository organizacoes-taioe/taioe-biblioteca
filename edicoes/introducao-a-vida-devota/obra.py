"""Introdução à vida devota (Filoteia), de São Francisco de Sales — dados para ferramentas/traducoes.py."""

META = {
    'id': 'introducao-a-vida-devota', 'autor': 'sao-francisco-de-sales',
    'titulo': 'Introdução à vida devota (Filoteia)',
    'ano': 1609, 'datas': '1609; texto definitivo de 1619', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'traducao': {'lingua': 'francês', 'codigo': 'fr', 'titulo': 'Introduction à la vie dévote'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Francisco de Sales, bispo de Genebra com sede em Annecy, escreveu a _Introdução_ a partir '
            'das cartas de direção espiritual que mandava a uma senhora, Madame de Charmoisy, e publicou-a em Lyon em '
            '1609. Dirige-se a Filoteia, «a que ama a Deus», nome de toda alma que quer a devoção no meio do mundo: '
            'na família, na corte, no trabalho, e não só no claustro. As cinco partes levam a alma do primeiro desejo '
            'à resolução firme, à oração e aos sacramentos, ao exercício das virtudes, à luta contra as tentações e à '
            'renovação anual dos propósitos. O autor reviu o livro até a edição de 1619, a última que saiu em vida '
            'dele; é esse o texto traduzido, na edição do abade Fernand Boulenger (Paris, 1909), que o reproduz '
            'inteiro com a ortografia atualizada, conferido com a edição de Annecy das _Obras_ (t. III, 1893).\n\n'
            '**A tradução.** Português do Brasil, fiel ao sentido e ao movimento da prosa de Francisco de Sales: as '
            'comparações tiradas das abelhas, das plantas e dos animais, a doçura do tom, as frases longas e '
            'encadeadas. Filoteia é tratada por _vós_, como no original; o leitor do Prefácio, por _tu_. As palavras '
            'antigas do francês do século XVII foram vertidas pelo sentido, sem arcaísmos artificiais. As citações da '
            'Escritura foram traduzidas do francês do autor, e não copiadas de uma Bíblia portuguesa. A pequena marca '
            'no começo dos capítulos (I.1) dá a parte e o capítulo, como se cita a obra.\n\n'
            '**O original ao lado.** O botão «Francês», no alto da página de leitura, mostra o texto de 1619 junto da '
            'tradução.'),
        'fontes': [
            {'nome': 'Wikisource (fr): Introduction à la vie dévote (Boulenger), texto integral',
             'url': 'https://fr.wikisource.org/wiki/Introduction_%C3%A0_la_vie_d%C3%A9vote_(Boulenger)/Texte_entier',
             'nota': 'texto francês de base (texto de 1619, ed. Boulenger, 1909)'},
            {'nome': 'Œuvres de saint François de Sales, Édition d\'Annecy, t. III (1893), no Internet Archive',
             'url': 'https://archive.org/details/oeuvresdesaintfr03fran',
             'nota': 'edição antiga, para conferência'},
        ],
    },
}

PARTES = [
    ('', 'Oração dedicatória e Prefácio', ['00-oracao-e-prefacio.txt']),
    ('I', 'Primeira parte: do primeiro desejo à resolução de abraçar a vida devota', ['01-primeira-parte.txt']),
    ('II', 'Segunda parte: a oração e os sacramentos', ['02-segunda-parte.txt']),
    ('III', 'Terceira parte: o exercício das virtudes',
     ['03-terceira-parte-a.txt', '03-terceira-parte-b.txt', '03-terceira-parte-c.txt']),
    ('IV', 'Quarta parte: contra as tentações mais comuns', ['04-quarta-parte.txt']),
    ('V', 'Quinta parte: renovar a alma e confirmá-la na devoção', ['05-quinta-parte.txt']),
]
