"""Heródoto, Histórias — dados para ferramentas/traducoes.py. A obra cresce por livros: cada livro novo acrescenta
as suas partes em PARTES (sigla «Livro II» etc.) e conta na «Sobre»."""

META = {
    'id': 'herodoto-historias', 'indice': 'nao-ficcao-traducoes', 'autor': 'herodoto',
    'titulo': 'Histórias',
    'datas': 'c. 430–425 a.C.', 'genero': 'História',
    'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'agrupar': True},
    'traducao': {'lingua': 'grego', 'codigo': 'grc', 'titulo': 'Ἱστορίαι'},
    'original_ao_lado': True,
    'edicao': {
        'titulo': 'Sobre esta tradução',
        'apresentacao': (
            '**O texto e o autor.** Heródoto nasceu por volta de 484 a.C. em Halicarnasso, cidade grega da Cária, na costa da '
            'Ásia Menor, então sujeita aos persas; viajou pelo Egito, pela Fenícia, pela Babilônia e pelas terras do mar Negro, '
            'viveu em Atenas e morreu por volta de 425 a.C., talvez em Túrio, no sul da Itália. As suas _Histórias_ contam a '
            'guerra entre gregos e persas e, para explicá-la, a formação do império persa e os povos que ele conquistou: por '
            'isso Cícero o chamou «pai da história». A divisão em nove livros, cada um com o nome de uma Musa, é dos '
            'estudiosos de Alexandria. O livro I, _Clio_, vai das origens da inimizade entre a Europa e a Ásia até a morte de '
            'Ciro: Creso e a Lídia, Sólon, os oráculos, Atenas e Esparta, os medos, a infância de Ciro, os costumes dos persas, '
            'a conquista da Jônia, Babilônia e a guerra contra os masságetas.\n\n'
            '**Em partes.** Por enquanto está aqui só o livro I; os outros oito vêm depois, um a um, com as mesmas '
            'convenções.\n\n'
            '**A divisão.** Os capítulos e as seções são os da numeração usual (as pequenas marcas no texto: 5.2 é o '
            'capítulo 5, seção 2, do livro; 1.0 é o proêmio), 216 capítulos no livro I. Os grupos de capítulos e os títulos '
            'deles são desta edição, para a leitura em partes.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e à ordem das ideias, sem acréscimos, com o '
            'andamento de quem conta em voz alta, que é o de Heródoto: as fórmulas que abrem e fecham cada história, o «dizem» '
            'e o «pelo que eu soube» com que ele separa o que viu, o que ouviu e o que pensa. Os nomes estão na forma '
            'portuguesa usual. Os oráculos em verso vão em verso livre, linha por linha. O que Godley imprime entre colchetes, '
            'por julgar acréscimo de copista, vai entre colchetes também na tradução (148.2, 167.1, 180.4, 196.5); onde o '
            'texto se perdeu, «…» (92.2, 180.4, 193.2).\n\n'
            '**O original.** O grego, no botão «Grego», é o da edição de A. D. Godley (_Herodotus_, vol. I, coleção Loeb, '
            '1920), em domínio público. Partimos da transcrição da Perseus Digital Library e a comparamos, palavra por '
            'palavra, com duas leituras do fac-símile da edição (a impressão de 1921 e uma reimpressão das mesmas chapas); '
            'corrigimos pela imagem uns 40 erros de digitação (letras trocadas, palavras juntas ou partidas, uma oração '
            'repetida em 153.1) e cerca de 280 acentos. Ficaram de fora as notas críticas de Godley, e a tradução inglesa dele, '
            'ao lado do grego na edição Loeb, serviu só para conferir o sentido.'),
        'fontes': [
            {'nome': 'A. D. Godley, Herodotus, vol. I (Loeb, 1920), impressão de 1921, no Internet Archive',
             'url': 'https://archive.org/details/herodotud0000adgo',
             'nota': 'fac-símile do texto grego (livro I nas páginas pares, p. 2–270 da edição); conferência das correções'},
            {'nome': 'Perseus Digital Library: Heródoto, Histórias (texto de Godley, CC BY-SA 4.0)',
             'url': 'https://github.com/PerseusDL/canonical-greekLit/tree/master/data/tlg0016/tlg001',
             'nota': 'transcrição do grego de Godley, base do texto ao lado'},
        ],
    },
}

L1 = 'Livro I'
PARTES = [
    (L1, 'Proêmio: os raptos (1–5)', ['livro1-1-5.txt']),
    (L1, 'Candaules e Giges (6–14)', ['livro1-6-14.txt']),
    (L1, 'Os reis da Lídia e Árion (15–25)', ['livro1-15-25.txt']),
    (L1, 'Creso, Sólon e Átis (26–45)', ['livro1-26-45.txt']),
    (L1, 'Creso consulta os oráculos (46–58)', ['livro1-46-58.txt']),
    (L1, 'Atenas e Esparta (59–70)', ['livro1-59-70.txt']),
    (L1, 'A guerra com Ciro e a tomada de Sardes (71–84)', ['livro1-71-84.txt']),
    (L1, 'Creso na fogueira; os lídios (85–94)', ['livro1-85-94.txt']),
    (L1, 'Os medos (95–106)', ['livro1-95-106.txt']),
    (L1, 'O nascimento de Ciro (107–122)', ['livro1-107-122.txt']),
    (L1, 'Ciro contra Astíages (123–130)', ['livro1-123-130.txt']),
    (L1, 'Os costumes dos persas (131–140)', ['livro1-131-140.txt']),
    (L1, 'Os jônios e Pactias (141–161)', ['livro1-141-161.txt']),
    (L1, 'Hárpago na Jônia, na Cária e na Lícia (162–176)', ['livro1-162-176.txt']),
    (L1, 'Babilônia e as suas rainhas (177–187)', ['livro1-177-187.txt']),
    (L1, 'Ciro toma Babilônia; os costumes dos babilônios (188–200)', ['livro1-188-200.txt']),
    (L1, 'Tômiris e a morte de Ciro (201–216)', ['livro1-201-216.txt']),
]
