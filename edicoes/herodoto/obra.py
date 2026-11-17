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
            'a conquista da Jônia, Babilônia e a guerra contra os masságetas. O livro II, _Euterpe_, é o do Egito, que Cambises, '
            'filho de Ciro, vai conquistar: a terra e o Nilo, os costumes, os deuses e os animais sagrados dos egípcios, e a '
            'história dos seus reis, das pirâmides até Amásis, contada pelo que Heródoto viu e ouviu dos sacerdotes.\n\n'
            '**Em partes.** Por enquanto estão aqui os livros I e II; os outros sete vêm depois, um a um, com as mesmas '
            'convenções.\n\n'
            '**A divisão.** Os capítulos e as seções são os da numeração usual (as pequenas marcas no texto: 5.2 é o '
            'capítulo 5, seção 2, do livro; 1.0 é o proêmio), 216 capítulos no livro I e 182 no II (no II, a história '
            'de Rampsinito, o capítulo 121, se divide em 121α a 121ζ). Os grupos de capítulos e os títulos '
            'deles são desta edição, para a leitura em partes.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e à ordem das ideias, sem acréscimos, com o '
            'andamento de quem conta em voz alta, que é o de Heródoto: as fórmulas que abrem e fecham cada história, o «dizem» '
            'e o «pelo que eu soube» com que ele separa o que viu, o que ouviu e o que pensa. Os nomes estão na forma '
            'portuguesa usual. Os oráculos em verso vão em verso livre, linha por linha. O que Godley imprime entre colchetes, '
            'por julgar acréscimo de copista, vai entre colchetes também na tradução (no livro I, 148.2, 167.1, 180.4, 196.5; '
            'no II, 116.2, 143.4, 148.4); onde o texto se perdeu, «…» (I 92.2, 180.4, 193.2; II 40.1, 86.2, 175.4).\n\n'
            '**O original.** O grego, no botão «Grego», é o da edição de A. D. Godley (_Herodotus_, vol. I, coleção Loeb, '
            '1920), em domínio público. Partimos da transcrição da Perseus Digital Library e a comparamos, palavra por '
            'palavra, com duas leituras do fac-símile da edição (a impressão de 1921 e uma reimpressão das mesmas chapas); '
            'corrigimos pela imagem, no livro I, uns 40 erros de digitação (letras trocadas, palavras juntas ou partidas, uma '
            'oração repetida em 153.1) e cerca de 280 acentos; no livro II, 16 palavras com letras trocadas, duas palavras '
            'que faltavam (47.1, 113.3) e 21 acentos. Ficaram de fora as notas críticas de Godley, e a tradução inglesa dele, '
            'ao lado do grego na edição Loeb, serviu só para conferir o sentido.'),
        'fontes': [
            {'nome': 'A. D. Godley, Herodotus, vol. I (Loeb, 1920), impressão de 1921, no Internet Archive',
             'url': 'https://archive.org/details/herodotud0000adgo',
             'nota': 'fac-símile do texto grego (livros I e II nas páginas pares); conferência das correções'},
            {'nome': 'Perseus Digital Library: Heródoto, Histórias (texto de Godley, CC BY-SA 4.0)',
             'url': 'https://github.com/PerseusDL/canonical-greekLit/tree/master/data/tlg0016/tlg001',
             'nota': 'transcrição do grego de Godley, base do texto ao lado'},
        ],
    },
}

L1 = 'Livro I'
L2 = 'Livro II'
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
    # livro II (Euterpe)
    (L2, 'Psamético e os homens mais antigos (1–4)', ['livro2-1-4.txt']),
    (L2, 'A terra do Egito (5–18)', ['livro2-5-18.txt']),
    (L2, 'As cheias do Nilo (19–27)', ['livro2-19-27.txt']),
    (L2, 'As fontes do Nilo (28–34)', ['livro2-28-34.txt']),
    (L2, 'Os costumes dos egípcios (35–41)', ['livro2-35-41.txt']),
    (L2, 'Héracles e os deuses dos gregos (42–53)', ['livro2-42-53.txt']),
    (L2, 'Dodona e as festas dos egípcios (54–64)', ['livro2-54-64.txt']),
    (L2, 'Os animais sagrados (65–76)', ['livro2-65-76.txt']),
    (L2, 'A vida dos egípcios e os embalsamamentos (77–90)', ['livro2-77-90.txt']),
    (L2, 'Perseu, os pântanos e o caminho do rio (91–98)', ['livro2-91-98.txt']),
    (L2, 'Min, Nitócris, Méris e Sesóstris (99–110)', ['livro2-99-110.txt']),
    (L2, 'Feros, Proteu e Helena (111–120)', ['livro2-111-120.txt']),
    (L2, 'Rampsinito e o ladrão (121–123)', ['livro2-121-123.txt']),
    (L2, 'Quéops, Quéfren e Miquerino (124–136)', ['livro2-124-136.txt']),
    (L2, 'Sabacos, Setos e as gerações dos reis (137–146)', ['livro2-137-146.txt']),
    (L2, 'Os doze reis e Psamético (147–157)', ['livro2-147-157.txt']),
    (L2, 'Neco, Psâmis e Apríes (158–171)', ['livro2-158-171.txt']),
    (L2, 'Amásis (172–182)', ['livro2-172-182.txt']),
]
