"""A arte de aproveitar as próprias faltas, de Joseph Tissot — dados para ferramentas/traducoes.py."""

META = {
    'id': 'arte-de-aproveitar-as-faltas', 'autor': 'joseph-tissot',
    'titulo': 'A arte de aproveitar as próprias faltas',
    'subtitulo': 'segundo São Francisco de Sales',
    'ano': 1879, 'datas': '1879; texto da 6.ª edição, 1894', 'genero': 'Espiritualidade',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'traducao': {'lingua': 'francês', 'codigo': 'fr',
                 'titulo': 'L\'Art d\'utiliser ses fautes d\'après saint François de Sales'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** O padre Joseph Tissot (1840–1894), dos Missionários de São Francisco de Sales, de Annecy, '
            'reuniu neste livro, publicado em 1879, o que o santo bispo de Genebra ensina sobre as próprias faltas: '
            'não se espantar com elas, não se perturbar, não desanimar; e, mais ainda, tirar delas humildade, amor '
            'da própria pequenez, confiança na misericórdia de Deus, perseverança e fervor. Quase tudo é dito com as '
            'palavras do próprio Francisco de Sales, tiradas das cartas, dos sermões, da _Filoteia_ e do _Tratado do '
            'amor de Deus_. O texto traduzido é o da sexta edição (1894), a última revista pelo autor, que acrescentou '
            'citações e numerou os parágrafos; foi estabelecido por nós sobre o exemplar digitalizado pela Biblioteca '
            'Municipal de Lyon e revisto página por página contra o scan, com as notas do autor. Os poucos erros de '
            'impressão foram corrigidos; as referências bíblicas que o impresso dá erradas ficaram como estão. A epígrafe '
            'da página de rosto, _Misericordias Domini in æternum cantabo_, abre o livro, antes da Advertência.\n\n'
            '**A tradução.** Português do Brasil, fiel ao sentido e ao tom afetuoso do livro. As citações de são '
            'Francisco de Sales foram traduzidas do francês em que Tissot as dá, guardando o sabor da língua do '
            'século XVII sem arcaísmos artificiais; as que vêm da _Filoteia_ seguem a nossa tradução da _Introdução à '
            'vida devota_, ajustada onde Tissot cita de outro modo. O tratamento do original foi mantido: _vós_ nas cartas '
            'do santo, nos apelos ao leitor e nas orações; _tu_ quando Deus fala à alma ou a alma a si mesma. As notas do '
            'autor aparecem no fim de cada parte. A pequena marca no começo dos capítulos (I.1) dá a parte e o capítulo.\n\n'
            '**O original ao lado.** O botão «Francês», no alto da página de leitura, mostra o texto de 1894 junto da '
            'tradução.'),
        'fontes': [
            {'nome': 'Bibliothèque municipale de Lyon (Numelyo), 6.ª ed., 1894',
             'url': 'https://numelyo.bm-lyon.fr/f_view/BML:BML_00GOO0100137001103793597',
             'nota': 'scan de base, domínio público (Licence Ouverte)'},
            {'nome': 'Bibliothèque municipale de Lyon (Numelyo), 1.ª ed., 1879',
             'url': 'https://numelyo.bm-lyon.fr/f_view/BML:BML_00GOO0100137001103793555',
             'nota': 'primeira edição, para conferência'},
        ],
    },
}

PARTES = [
    ('', 'Advertência', ['00-avant-propos.txt']),
    ('I', 'Primeira parte: não se espantar, não se perturbar, não desanimar', ['01-primeira-parte.txt']),
    ('II', 'Segunda parte: aproveitar as faltas', ['02-segunda-parte-a.txt', '02-segunda-parte-b.txt']),
]
