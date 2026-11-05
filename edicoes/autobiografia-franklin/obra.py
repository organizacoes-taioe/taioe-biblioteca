"""Autobiografia de Benjamin Franklin — dados para ferramentas/traducoes.py."""

META = {
    'id': 'autobiografia', 'indice': 'nao-ficcao-traducoes', 'autor': 'benjamin-franklin', 'titulo': 'Autobiografia',
    'ano': 1771, 'datas': '1771–1790', 'genero': 'Autobiografia',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'marcas': False},
    'traducao': {'lingua': 'inglês', 'codigo': 'en', 'titulo': 'The Autobiography of Benjamin Franklin'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Franklin começou as memórias em 1771, aos 65 anos, numa semana de folga em Twyford, '
            'na casa de campo do seu amigo Jonathan Shipley, bispo de St. Asaph, em forma de carta ao filho '
            'William, e as levou até 1730. A Revolução interrompeu o trabalho; os papéis se perderam e foram '
            'achados por um velho amigo quacre, Abel James, que lhe mandou uma cópia e uma carta pedindo que '
            'continuasse. Com essa carta e outra de Benjamin Vaughan, Franklin retomou o texto em Passy, perto '
            'de Paris, em 1784, agora para o público: são as páginas sobre a biblioteca, a religião e o projeto '
            'de perfeição moral, com as treze virtudes. Em agosto de 1788, já em Filadélfia, escreveu a terceira '
            'parte, a mais longa, até a chegada a Londres em 1757; a quarta, poucas páginas, é do último ano de '
            'vida, já doente. Morreu em 1790 sem terminar o livro, que para em 1758.\n\n'
            '**A divisão.** As quatro partes são as de Franklin, com o lugar e o ano em que cada uma foi escrita. '
            'Franklin não dividiu o texto em capítulos: os capítulos e os seus títulos são desta edição, em '
            'trechos de tamanho de leitura, nos cortes naturais da história. As notas que Franklin pôs à margem '
            'do manuscrito vêm logo depois do parágrafo, entre colchetes.\n\n'
            '**A tradução.** Do inglês, em português do Brasil, fiel ao sentido e ao tom de conversa de Franklin, '
            'claro e concreto, com o seu humor seco, sem acréscimos. Franklin trata o filho por _tu_; os quacres, '
            'que tratavam todo mundo por _thee_, também falam por _tu_. Moedas e medidas ficam as do original '
            '(libras, xelins e pence; milhas, pés e polegadas). Os _proprietários_ são os Penn, donos hereditários '
            'da Pensilvânia, que nomeavam o governador. Franklin, tipógrafo, chama os seus erros de _erratas_, '
            'e assim ficaram. Os versos citados foram traduzidos em verso.\n\n'
            '**O original.** O inglês, no botão «Inglês», é o da edição de John Bigelow (Filadélfia, Lippincott, '
            '1868), a primeira feita sobre o manuscrito, que Bigelow tinha comprado na França no ano anterior: '
            'antes dela se lia a versão do neto, William Temple Franklin, com mais de mil e duzentas mudanças no '
            'texto e sem a quarta parte. Partimos da transcrição do Project Gutenberg (Harvard Classics, 1909), '
            'que segue Bigelow, e a conferimos palavra por palavra com três exemplares da edição de 1868; onde '
            'a transcrição se afastava de 1868, ficou a lição de 1868 (umas setenta, como _above fifty years_, '
            '_sweat plentifully_, _those actions_). Mantém-se a grafia do manuscrito (_receiv\'d_, _compleat_, '
            '_extreamly_). As notas de Bigelow ficaram de fora; a tabela do livrinho de exame vai descrita entre '
            'colchetes.'),
        'fontes': [
            {'nome': 'John Bigelow, Autobiography of Benjamin Franklin, edited from his manuscript (Philadelphia, 1868), no Internet Archive',
             'url': 'https://archive.org/details/autobiographyofb1868fran',
             'nota': 'edição-base; com os exemplares benjaminfrautobio00franrich e autobiographyofb00fran2'},
            {'nome': 'The Autobiography of Benjamin Franklin (Harvard Classics, 1909), Project Gutenberg',
             'url': 'https://www.gutenberg.org/ebooks/148',
             'nota': 'transcrição de trabalho, conferida com a edição de 1868'},
        ],
    },
}

PARTES = [
    ('I', 'Twyford, 1771', ['parte-1.txt']),
    ('II', 'Passy, 1784', ['parte-2.txt']),
    ('III', 'Filadélfia, 1788', ['parte-3.txt']),
    ('IV', 'Filadélfia, 1789–1790', ['parte-4.txt']),
]
