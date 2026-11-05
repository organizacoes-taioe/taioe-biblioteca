"""Confissão (Исповедь), de Liev Tolstói — dados para ferramentas/traducoes.py."""

ROMANOS = 'I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI'.split()

META = {
    'id': 'confissao', 'indice': 'nao-ficcao-traducoes', 'autor': 'liev-tolstoi', 'titulo': 'Confissão', 'subtitulo': 'Introdução a uma obra não publicada',
    'ano': 1882, 'datas': '1879–1882', 'genero': 'Autobiografia',
    'divisao': {'singular': 'capítulo', 'plural': 'capítulos'},
    'traducao': {'lingua': 'russo', 'codigo': 'ru', 'titulo': 'Исповедь'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto.** Tolstói escreveu a _Confissão_ entre 1879 e 1882, quando já tinha publicado _Guerra e paz_ '
            'e _Anna Kariênina_. Conta como perdeu na juventude a fé em que fora criado, como viveu para a fama, a '
            'família e a literatura, e como, perto dos cinquenta anos, a pergunta pelo sentido da vida o levou à beira '
            'do suicídio. Procura a resposta nas ciências e na filosofia, e não a encontra; encontra-a na fé do povo '
            'simples e volta por algum tempo à Igreja ortodoxa, de que se afasta de novo. O livro termina com um sonho. '
            'O subtítulo, «Introdução a uma obra não publicada», anuncia os estudos de teologia e dos Evangelhos que '
            'Tolstói escreveu em seguida. A censura proibiu o livro na Rússia: a revista _O Pensamento Russo_ chegou a '
            'compô-lo em 1882, mas a tiragem foi recolhida, e a primeira edição saiu em Genebra, em 1884.\n\n'
            '**A divisão.** Os 16 capítulos são os do autor. O último termina com uma nota escrita três anos depois, que '
            'conta o sonho.\n\n'
            '**A tradução.** Do russo, em português do Brasil, fiel ao sentido e ao movimento da prosa de Tolstói, com '
            'as suas frases longas, as repetições de propósito e as perguntas, sem acréscimos. As citações (Salomão, o '
            'Eclesiastes; a lenda de Buda; Sócrates; Schopenhauer) vão como Tolstói as dá, que as resume ou cita de '
            'memória, e não como estão nas traduções correntes.\n\n'
            '**O original.** O russo, no botão «Russo», é o do volume 23 das _Obras completas_ de Tolstói (Moscou, 1957), '
            'na transcrição do Wikisource em russo, conferida com outra transcrição independente e, nos pontos em que '
            'as duas divergem, nas imagens do volume; na ortografia russa de hoje (Бог com maiúscula, onde a edição '
            'soviética imprime «бог»).'),
        'fontes': [
            {'nome': 'Л. Н. Толстой, Полное собрание сочинений, т. 23 (Moscou, 1957), no Wikisource em russo',
             'url': 'https://ru.wikisource.org/wiki/Исповедь_(Толстой)',
             'nota': 'texto russo de base e ao lado, p. 1–59'},
            {'nome': 'O mesmo volume, fac-símile no Wikimedia Commons',
             'url': 'https://commons.wikimedia.org/wiki/File:L._N._Tolstoy._All_in_90_volumes._Volume_23.pdf',
             'nota': 'para conferir as divergências'},
            {'nome': 'Исповедь, na biblioteca Lib.ru/Классика',
             'url': 'http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0440.shtml',
             'nota': 'transcrição de outra edição, usada para conferir'},
        ],
    },
}

PARTES = [(r, '', [f'capitulo-{k:02d}.txt']) for k, r in enumerate(ROMANOS, 1)]
