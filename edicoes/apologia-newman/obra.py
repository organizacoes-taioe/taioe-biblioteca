"""Apologia pro Vita Sua, de São John Henry Newman — dados para ferramentas/traducoes.py."""

META = {
    'id': 'apologia-newman', 'autor': 'sao-john-henry-newman', 'titulo': 'Apologia pro Vita Sua',
    'ano': 1864, 'datas': '1864; forma final, 1873', 'genero': 'Autobiografia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos', 'rotulo': 'nome', 'agrupar': True},
    'traducao': {'lingua': 'inglês', 'codigo': 'en', 'titulo': 'Apologia pro Vita Sua'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Em janeiro de 1864, Charles Kingsley escreveu, numa resenha da _Macmillan’s Magazine_, '
            'que a verdade, por si mesma, nunca fora uma virtude do clero romano, e citou Newman como prova. '
            'Depois de uma troca de cartas e de um panfleto de Kingsley, Newman respondeu contando a história das '
            'suas opiniões religiosas, de menino até a entrada na Igreja católica, em 1845. A _Apologia_ saiu em '
            'Londres em sete fascículos semanais, entre 21 de abril e 2 de junho de 1864, seguidos de um apêndice. '
            'Em 1865 Newman refez o livro: tirou a polêmica direta com Kingsley e reduziu o apêndice a notas; em '
            '1873 o título _Apologia pro Vita Sua_ voltou à frente. É essa forma final que traduzimos.\n\n'
            '**A divisão.** O prefácio de 1865 conta a ocasião do livro e traz os trechos da primeira edição que '
            'Newman conservou. Seguem os cinco capítulos da história (até 1833; 1833 a 1839; 1839 a 1841; 1841 a '
            '1845; e a posição do autor desde 1845), as sete notas sobre pontos discutidos (o liberalismo, os '
            'milagres, a mentira…), a carta do bispo de Birmingham e as mensagens de apoio do clero e dos leigos, '
            'e as notas que Newman acrescentou depois. Os capítulos mais longos vão em duas ou três partes, '
            'cortadas numa pausa do próprio autor. Ficaram de fora duas listas do fim do volume: a das cartas '
            'citadas, com as páginas da edição inglesa, e a das obras do autor.\n\n'
            '**A tradução.** Português do Brasil, feita do inglês, fiel ao sentido e ao movimento da prosa de '
            'Newman, de períodos longos e exatos, sem acréscimos nem explicações. Os nomes de pessoas, de '
            'colégios e de cargos de Oxford ficam como são; o latim que Newman cita fica em latim, traduzido só '
            'quando ele o traduz. As notas de rodapé do autor vêm no fim de cada página. As remissões a páginas '
            'são as da edição inglesa.\n\n'
            '**O original.** O inglês, no botão «Inglês», é o da edição de Londres, Longmans, Green, and Co., '
            '1890, na transcrição do Projeto Gutenberg.'),
        'fontes': [
            {'nome': 'Project Gutenberg, eBook nº 22088', 'url': 'https://www.gutenberg.org/ebooks/22088',
             'nota': 'texto inglês de base (Longmans, 1890), com as imagens das páginas'},
        ],
    },
}

_H = 'História das minhas opiniões religiosas'
PARTES = [
    ('', 'Prefácio', ['00-prefacio.txt']),
    ('I', f'{_H} até o ano de 1833', ['01-capitulo-1.txt']),
    ('II', f'{_H} de 1833 a 1839 (1ª parte)', ['02-capitulo-2a.txt']),
    ('II', f'{_H} de 1833 a 1839 (2ª parte)', ['03-capitulo-2b.txt']),
    ('III', f'{_H} de 1839 a 1841 (1ª parte)', ['04-capitulo-3a.txt']),
    ('III', f'{_H} de 1839 a 1841 (2ª parte)', ['05-capitulo-3b.txt']),
    ('IV', f'{_H} de 1841 a 1845 (1ª parte)', ['06-capitulo-4a.txt']),
    ('IV', f'{_H} de 1841 a 1845 (2ª parte)', ['07-capitulo-4b.txt']),
    ('IV', f'{_H} de 1841 a 1845 (3ª parte)', ['08-capitulo-4c.txt']),
    ('V', 'A posição do meu espírito desde 1845 (1ª parte)', ['09-capitulo-5a.txt']),
    ('V', 'A posição do meu espírito desde 1845 (2ª parte)', ['10-capitulo-5b.txt']),
    ('Nota A', 'O liberalismo', ['11-nota-a.txt']),
    ('Nota B', 'Os milagres eclesiásticos', ['12-nota-b.txt']),
    ('Nota C', 'O sermão sobre a sabedoria e a inocência', ['13-nota-c.txt']),
    ('Nota D', 'A série de vidas de santos de 1843-1844', ['14-nota-d.txt']),
    ('Nota E', 'A Igreja anglicana', ['15-nota-e.txt']),
    ('Nota F', 'A economia', ['16-nota-f.txt']),
    ('Nota G', 'A mentira e o equívoco', ['17-nota-g.txt']),
    ('', 'Carta do bispo de Birmingham', ['18-carta-do-bispo.txt']),
    ('', 'Mensagens do clero e dos leigos', ['19-cartas-do-clero-e-leigos.txt']),
    ('', 'Notas adicionais', ['20-notas-adicionais.txt']),
]
