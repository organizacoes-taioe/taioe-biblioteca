"""Vida de São Bento (Diálogos, livro II), de São Gregório Magno — dados para ferramentas/traducoes.py."""

META = {
    'id': 'vida-de-sao-bento', 'autor': 'sao-gregorio-magno', 'titulo': 'Vida de São Bento',
    'ano': 594, 'datas': 'c. 593–594', 'genero': 'Hagiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes'},
    'traducao': {'lingua': 'latim', 'codigo': 'la', 'titulo': 'Dialogorum liber II'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** Por volta de 593–594, já papa, Gregório escreveu os _Diálogos sobre a '
            'vida e os milagres dos Padres da Itália_, quatro livros em forma de conversa com o seu diácono '
            'Pedro, para mostrar que a Itália, devastada pela guerra e pelos lombardos, também tivera os seus '
            'santos. O livro II é todo dedicado a Bento de Núrsia (c. 480–547), o pai dos monges do Ocidente, '
            'e é praticamente tudo o que sabemos da sua vida: a fuga de Roma, os três anos na gruta de '
            'Subiaco, os mosteiros, a mudança para Monte Cassino, os milagres, a irmã Escolástica, a visão do '
            'mundo inteiro num raio de luz, a Regra e a morte de pé no oratório. Gregório diz de onde tirou '
            'o que conta: de quatro discípulos de Bento, que nomeia no prólogo. O livro foi lido em todos os '
            'mosteiros da Idade Média e deu à arte cristã quase todas as cenas da vida do santo.\n\n'
            '**A divisão.** Um prólogo e 38 capítulos, com os títulos da edição latina, traduzidos; a pequena '
            'marca no começo de cada capítulo dá o livro e o capítulo, como se cita a obra (II.35). As quatro '
            'partes são desta edição, só para facilitar a leitura: Subiaco (prólogo e cap. 1–8), Monte '
            'Cassino (9–21), os milagres (22–32) e Escolástica e a morte de Bento (33–38). O livro é um '
            'diálogo: as falas de Pedro, que pergunta, e de Gregório, que responde e explica, vêm marcadas '
            'com o nome de quem fala.\n\n'
            '**A tradução.** Português do Brasil, feita do latim, fiel ao sentido e ao tom simples da '
            'narração, sem acréscimos nem explicações. Gregório trata Pedro por _tu_. As citações da '
            'Escritura são traduzidas do latim dele (a Vulgata), não de uma Bíblia moderna; as referências '
            'entre parênteses são as da edição de Migne, passadas às abreviaturas usuais no Brasil, com os '
            'salmos na numeração da Vulgata (Sl 118 = Sl 119 das Bíblias que seguem o hebraico) e os livros '
            'dos Reis e de Samuel com os nomes de hoje (o «IV Reg.» de Migne é 2Rs). Os nomes próprios '
            'seguem a forma portuguesa tradicional (Bento, Escolástica, Mauro, Plácido, Enfide, Subiaco, '
            'Cassino).\n\n'
            '**O original.** O latim, no botão «Latim», é o da _Patrologia Latina_ de Migne, vol. 66 '
            '(Paris, Migne, col. 126–204), que reproduz a edição dos beneditinos de São Mauro (Paris, 1705), '
            'em domínio público, na transcrição da Bibliotheca Augustana. Ficaram de fora as notas e '
            'variantes dos editores e os números das colunas. Corrigimos pelo sentido uma dúzia de '
            'falhas evidentes da transcrição (letras trocadas, pontos que faltavam); a conferência com o '
            'fac-símile da edição ainda está por fazer.'),
        'fontes': [
            {'nome': 'Bibliotheca Augustana: Gregorius Magnus, Dialogi, Liber II (texto da PL 66)',
             'url': 'https://www.hs-augsburg.de/~harsch/Chronologia/Lspost06/GregoriusMagnus/gre_d200.html',
             'nota': 'transcrição do texto de Migne, base do latim ao lado'},
            {'nome': 'Dialogi (Gregorius Magnus)/Liber II, no Wikisource latino',
             'url': 'https://la.wikisource.org/wiki/Dialogi_(Gregorius_Magnus)/Liber_II',
             'nota': 'outro texto antigo (dos Bolandistas, com outra divisão em capítulos), para comparar'},
        ],
    },
}

PARTES = [
    ('1–8', 'Subiaco', ['parte-1.txt']),
    ('9–21', 'Monte Cassino', ['parte-2.txt']),
    ('22–32', 'Os milagres', ['parte-3.txt']),
    ('33–38', 'Escolástica e a morte de Bento', ['parte-4.txt']),
]
