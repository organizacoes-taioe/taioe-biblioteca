"""Santa Teresa de Jesus, Livro da Vida — dados para ferramentas/traducoes.py.
Um arquivo por capítulo (00 = prólogo, 41 = epílogo), agrupados nas cinco partes de leitura (sigla «Parte I»…),
como as partes do Heródoto (divisao.agrupar)."""

META = {
    'id': 'livro-da-vida', 'autor': 'santa-teresa-de-jesus', 'titulo': 'Livro da Vida',
    'ano': 1565, 'datas': '1562–1565', 'genero': 'Autobiografia espiritual',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos', 'rotulo': 'nome', 'agrupar': True},
    'traducao': {'lingua': 'castelhano', 'codigo': 'es', 'titulo': 'Libro de la Vida'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O livro.** Teresa de Ahumada nasceu em Ávila em 1515, entrou aos vinte anos no mosteiro carmelita da '
            'Encarnação, na mesma cidade, e em 1562 fundou ali o pequeno mosteiro de São José, o primeiro das '
            'Descalças. Escreveu a _Vida_ por ordem dos confessores, que queriam saber por onde Deus a levava: uma '
            'primeira redação, de 1562, perdeu-se; a que temos foi acabada por volta de 1565 e enviada ao dominicano '
            'García de Toledo, a quem ela trata de _Vossa Mercê_. Não é uma autobiografia comum: Teresa conta a '
            'infância, a entrada no convento, as doenças e os anos de oração tíbia até a conversão diante de uma '
            'imagem de Cristo muito chagado, e depois as mercês de Deus, as visões, as dúvidas dos letrados que a '
            'examinavam e a fundação de São José. No meio da história, entre os capítulos 11 e 22, interrompe-a '
            'para explicar a oração por uma comparação: os quatro modos de regar uma horta, das águas tiradas do '
            'poço com esforço à chuva que vem do céu. O livro passou pela Inquisição, que o reteve por anos, e só '
            'saiu impresso em 1588, seis anos depois da morte dela, na edição de Frei Luis de León.\n\n'
            '**A divisão.** Os 40 capítulos e os seus títulos são os do manuscrito. As cinco partes são desta '
            'edição, para a leitura: I, a vida até a conversão (capítulos 1–10); II, os quatro graus de oração '
            '(11–22); III, a vida nova e as graças (23–31); IV, a fundação de São José (32–36); V, as últimas '
            'mercês (37–40). Antes vem o prólogo, e no fim a carta com que Teresa mandou o livro ao confessor. '
            'As pequenas marcas no texto dão o capítulo e o parágrafo (11.3 é o terceiro parágrafo do capítulo '
            '11); os parágrafos são os da edição de 1915, numerados por nós, e podem não coincidir com a numeração '
            'das edições modernas.\n\n'
            '**A tradução.** Do castelhano, em português do Brasil, fiel ao sentido e ao modo de Teresa, que escreve '
            'como fala: frases longas e emendadas, voltas atrás, desculpas, exclamações a Deus no meio da narração. '
            'Não as cortamos nem as arrumamos. A Deus ela fala por _Vós_; ao confessor, por _Vossa Mercê_. As '
            '_mercês_ são os favores que Deus lhe faz; os _letrados_, os homens de estudo, teólogos, a quem ela '
            'submete tudo. Os termos da oração (recolhimento, quietude, união, arroubo, êxtase) são os da tradição '
            'em português e os mesmos nas outras obras dela na Biblioteca.\n\n'
            '**O original.** O castelhano, no botão «Castelhano», é o da edição do padre Silverio de Santa Teresa '
            '(Burgos, 1915), a primeira grande edição crítica feita sobre o autógrafo, que se guarda no Escorial; '
            'mantém as formas da autora (_ansí_, _mesmo_, _mijor_, _sigún_). Partimos do texto do fac-símile no '
            'Internet Archive, lido por máquina, e o corrigimos com a edição de Vicente de la Fuente na Biblioteca '
            'de Autores Españoles (t. 53, 1861) e com a transcrição do autógrafo da editora Heitz. Ficaram de fora '
            'as notas do editor.'),
        'fontes': [
            {'nome': 'Silverio de Santa Teresa, Obras de Santa Teresa de Jesús, t. I: Libro de la Vida (Burgos, 1915), no Internet Archive',
             'url': 'https://archive.org/details/BMC1ObrasDeSantaTeresaDeJessTomoILibroDeLaVida',
             'nota': 'edição-base do original ao lado'},
            {'nome': 'Vicente de la Fuente, Escritos de Santa Teresa, t. I (Biblioteca de Autores Españoles, 53; Madrid, 1861, reimpr. 1877), no Internet Archive',
             'url': 'https://archive.org/details/bibliotecadeauto53madruoft',
             'nota': 'segundo testemunho, para corrigir a leitura'},
            {'nome': 'La vida de la Madre Teresa de Jesús escrita de su misma mano (Estrasburgo, Heitz, Bibliotheca Romanica), no Internet Archive',
             'url': 'https://archive.org/details/lavidaesentadesu00tere',
             'nota': 'transcrição do autógrafo na grafia original, para desempate'},
        ],
    },
}

PARTES = (
    [('', 'Prólogo', ['00.txt'])]
    + [('Parte I', f'Capítulo {n}', [f'{n:02d}.txt']) for n in range(1, 11)]
    + [('Parte II', f'Capítulo {n}', [f'{n:02d}.txt']) for n in range(11, 23)]
    + [('Parte III', f'Capítulo {n}', [f'{n:02d}.txt']) for n in range(23, 32)]
    + [('Parte IV', f'Capítulo {n}', [f'{n:02d}.txt']) for n in range(32, 37)]
    + [('Parte V', f'Capítulo {n}', [f'{n:02d}.txt']) for n in range(37, 41)]
    + [('', 'Epílogo', ['41.txt'])]
)
