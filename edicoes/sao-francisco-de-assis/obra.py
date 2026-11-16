"""São Francisco de Assis, de G. K. Chesterton — dados para ferramentas/traducoes.py."""

META = {
    'id': 'sao-francisco-de-assis', 'autor': 'g-k-chesterton', 'titulo': 'São Francisco de Assis',
    'ano': 1923, 'genero': 'Hagiografia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'traducao': {'lingua': 'inglês', 'codigo': 'en', 'titulo': 'St. Francis of Assisi'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** _St. Francis of Assisi_ saiu em Londres, pela Hodder and Stoughton, em 1923, numa '
            'coleção de livros curtos de divulgação, a «People\'s Library». Chesterton o escreveu logo depois de '
            'entrar na Igreja Católica (1922). Não é uma biografia completa, e ele o diz no primeiro capítulo: é '
            'um ensaio que tenta explicar ao leitor moderno, de fora para dentro, o santo que ele admira mas não '
            'entende, a começar pelo mundo em que Francisco nasceu e pelo que nele parece mais estranho.\n\n'
            '**A tradução.** Do inglês, em português do Brasil, fiel ao sentido e ao humor de Chesterton, com os '
            'termos e o tom já fixados na nossa tradução da _Ortodoxia_: o paradoxo tem de funcionar em '
            'português, com a mesma secura. Os nomes de pessoas e lugares vão na forma portuguesa usual (Assis, '
            'a Porciúncula, o Alverne, frei Junípero), e as criaturas do _Cântico_ com maiúscula, como no '
            'poema (Irmão Sol, Irmã Lua). Os versos de Belloc foram traduzidos em verso, com a medida e as '
            'rimas do original.\n\n'
            '**O original ao lado.** O botão «Inglês», no alto da página de leitura, mostra o texto de '
            'Chesterton junto da tradução: o da 1ª edição, de 1923, na transcrição do Project Gutenberg, '
            'conferida palavra por palavra com três exemplares dessa edição. Onde a transcrição se afastava da '
            'impressão, ficou a impressão (cinco lugares, como _firelight_ e _lingering_); os erros evidentes '
            'de composição de 1923 (um _pyschological_ e alguns pontos caídos) ficaram corrigidos.'),
        'fontes': [
            {'nome': 'St. Francis of Assisi (London, Hodder and Stoughton, 1923), no Internet Archive',
             'url': 'https://archive.org/details/stfrancisofassis00chesuoft',
             'nota': 'edição-base; com os exemplares francisofassisi00chesuoft e stfrancisofassis01ches'},
            {'nome': 'Project Gutenberg, eBook nº 63084', 'url': 'https://www.gutenberg.org/ebooks/63084',
             'nota': 'transcrição de trabalho, conferida com a edição de 1923'},
        ],
    },
}

PARTES = [
    (r, t, [f'capitulo-{k}.txt']) for k, (r, t) in enumerate([
        ('I', 'O problema de São Francisco'), ('II', 'O mundo que São Francisco encontrou'),
        ('III', 'Francisco, o combatente'), ('IV', 'Francisco, o construtor'), ('V', 'O jogral de Deus'),
        ('VI', 'O Pobrezinho'), ('VII', 'As três ordens'), ('VIII', 'O espelho de Cristo'),
        ('IX', 'Milagres e morte'), ('X', 'O testamento de São Francisco'),
    ], 1)]
