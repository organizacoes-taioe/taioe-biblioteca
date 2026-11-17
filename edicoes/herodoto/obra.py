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
            'história dos seus reis, das pirâmides até Amásis, contada pelo que Heródoto viu e ouviu dos sacerdotes. O livro III, _Tália_, é o de Cambises e de Dario: a '
            'conquista do Egito e a loucura de Cambises, Polícrates de Samos, o mago que tomou o trono, os sete persas e o '
            'debate sobre a melhor forma de governo, as satrapias e os tributos do império, os confins da terra (a Índia e a '
            'Arábia), o médico Democedes e a revolta de Babilônia. O livro IV, _Melpômene_, é o dos citas e o da Líbia: a origem, a terra, os rios e os '
            'costumes dos citas e dos povos vizinhos (as amazonas entre eles), a expedição de Dario contra eles, que volta pela ponte do '
            'Istro, e, do outro lado do mundo, a fundação de Cirene, os povos da Líbia e o cerco de Barca. O livro V, _Terpsícore_, é o da '
            'revolta jônica: Megabazo na Trácia, Histieu e Aristágoras de Mileto, Aristágoras em Esparta e em Atenas, a história de '
            'Atenas depois dos tiranos (Clístenes e as tribos, as guerras com Tebas, Cálcis e Egina), o discurso do coríntio '
            'Sosícles contra a tirania, com Cípselo e Periandro, o incêndio de Sardes e a guerra em Chipre e na Cária. O livro VI, _Érato_, é o do fim da '
            'revolta e de Maratona: a batalha de Lade e a queda de Mileto, a morte de Histieu, os Milcíades no Quersoneso, '
            'os reis de Esparta e a queda de Demarato, a loucura de Cleômenes, a expedição de Dátis e Artafernes, a batalha de '
            'Maratona, os alcmeônidas e o casamento de Agariste, e o fim de Milcíades. O livro VII, _Polímnia_, é o da expedição de '
            'Xerxes: o conselho e os sonhos que o levam à guerra, o canal do Atos e as pontes do Helesponto, a marcha, o '
            'catálogo dos povos do exército e da frota, a conversa com Demarato, os gregos que tomaram o partido dos medos, o '
            'oráculo do muro de madeira, Gelão de Siracusa, o Artemísio e a batalha das Termópilas. O livro VIII, _Urânia_, é o '
            'de Salamina: as batalhas do Artemísio, o ataque a Delfos, Atenas abandonada e a acrópole tomada, os conselhos dos '
            'gregos e de Xerxes, a batalha de Salamina, a volta de Xerxes, Temístocles em Andros, e Alexandre da Macedônia, '
            'que leva aos atenienses a proposta de Mardônio, e a resposta deles.\n\n'
            '**Em partes.** Por enquanto estão aqui os livros I a VIII; o IX vem depois, um a um, com as mesmas '
            'convenções.\n\n'
            '**A divisão.** Os capítulos e as seções são os da numeração usual (as pequenas marcas no texto: 5.2 é o '
            'capítulo 5, seção 2, do livro; 1.0 é o proêmio), 216 capítulos no livro I, 182 no II, 160 no III, 205 no IV, 126 no V, 140 no VI, 239 no VII e 144 no VIII (no II, a história '
            'de Rampsinito, o capítulo 121, se divide em 121α a 121ζ; no V, o discurso de Sosícles, o capítulo 92, em 92α a 92η; no VI, a história de Glauco, o capítulo 86, em 86α a 86δ; no VII, os discursos do conselho de Xerxes, em 8α a 8δ, 9α a 9γ e 10α a 10θ, e a resposta de Artabano, em 16α a 16γ; no VIII, o discurso de Temístocles, em 60α a 60γ, o conselho de Artemísia, em 68α a 68γ, e a mensagem de Mardônio e o discurso de Alexandre, em 140α e 140β). Os grupos de capítulos e os títulos '
            'deles são desta edição, para a leitura em partes.\n\n'
            '**A tradução.** Do grego, em português do Brasil, fiel ao sentido e à ordem das ideias, sem acréscimos, com o '
            'andamento de quem conta em voz alta, que é o de Heródoto: as fórmulas que abrem e fecham cada história, o «dizem» '
            'e o «pelo que eu soube» com que ele separa o que viu, o que ouviu e o que pensa. Os nomes estão na forma '
            'portuguesa usual. Os oráculos em verso vão em verso livre, linha por linha. O que Godley imprime entre colchetes, '
            'por julgar acréscimo de copista, vai entre colchetes também na tradução (no livro I, 148.2, 167.1, 180.4, 196.5; '
            'no II, 116.2, 143.4, 148.4; no III, 14.11, 51.2, 59.2, 91.3, 97.2, 149.1; o IV e o V não têm; no VI, 111.2 e o capítulo 122 inteiro; o VII não tem; no VIII, 104.1 a 105.1); onde o texto se perdeu, «…» (I 92.2, '
            '180.4, 193.2; II 40.1, 86.2, 175.4; III 39.2, 49.1; IV 47.2, 149.2; o V não tem; VI 64.1; VII 61.1, 76.1, 154.1; VIII 124.2).\n\n'
            '**O original.** O grego, no botão «Grego», é o da edição de A. D. Godley (_Herodotus_, coleção Loeb: vol. I, '
            '1920, com os livros I e II; vol. II, 1921, com o III e o IV; vol. III, 1922, com o V, o VI e o VII; vol. IV, 1924, com o VIII e o IX), em domínio público. Partimos da transcrição da Perseus Digital Library e a comparamos, palavra por '
            'palavra, com duas leituras do fac-símile da edição (a primeira impressão de cada volume e uma reimpressão das mesmas chapas); '
            'corrigimos pela imagem, no livro I, uns 40 erros de digitação (letras trocadas, palavras juntas ou partidas, uma '
            'oração repetida em 153.1) e cerca de 280 acentos; no livro II, 16 palavras com letras trocadas, duas palavras '
            'que faltavam (47.1, 113.3) e 21 acentos; no livro III, 10 palavras com letras trocadas (quase todas formas jônicas, '
            'como ἐκέετο e τράπουσι), uma palavra que faltava (21.2) e uns 40 acentos; no livro IV, 20 palavras com letras trocadas, uma que faltava (119.4), os parênteses de 34.2 e 35.3 e uns 116 '
            'acentos; no livro V, 13 palavras com letras trocadas, juntas ou partidas, uma que faltava (29.2), os parênteses de 67.3 e uns 25 acentos; no livro VI, 15 palavras com letras trocadas, duas que faltavam (53.2, 138.2), '
            'os parênteses de 69.4 e 109 e uns 35 acentos; no livro VII, 16 palavras com letras trocadas (uma delas, Κάδμος em '
            '164.1, erro tipográfico do próprio Godley), seis que faltavam (8γ.2, 16γ.1, 19.2, 111.2, 176.4, 219.1), os '
            'parênteses de 205.1 e uns 40 acentos; no livro VIII, 9 palavras com letras trocadas, uma que faltava (74.2) e '
            'uma a mais (2.1), os parênteses de 67.1 e 75.2 e uns 15 acentos. Ficaram de fora as notas críticas de Godley, e a tradução inglesa dele, '
            'ao lado do grego na edição Loeb, serviu só para conferir o sentido.'),
        'fontes': [
            {'nome': 'A. D. Godley, Herodotus, vol. I (Loeb, 1920), impressão de 1921, no Internet Archive',
             'url': 'https://archive.org/details/herodotud0000adgo',
             'nota': 'fac-símile do texto grego (livros I e II nas páginas pares); conferência das correções'},
            {'nome': 'A. D. Godley, Herodotus, vol. II (Loeb, 1921), impressão de 1921, no Internet Archive',
             'url': 'https://archive.org/details/herodotus0002adgo_j1l1',
             'nota': 'fac-símile do texto grego (livros III e IV nas páginas pares); conferência das correções'},
            {'nome': 'A. D. Godley, Herodotus, vol. III (Loeb, 1922), impressão de 1922, no Internet Archive',
             'url': 'https://archive.org/details/in.ernet.dli.2015.183370',
             'nota': 'fac-símile do texto grego (livros V, VI e VII nas páginas pares); conferência das correções'},
            {'nome': 'A. D. Godley, Herodotus, vol. IV (Loeb, 1924), impressão de 1924, no Internet Archive',
             'url': 'https://archive.org/details/bwb_Y0-DUM-764',
             'nota': 'fac-símile do texto grego (livros VIII e IX nas páginas pares); conferência das correções'},
            {'nome': 'Perseus Digital Library: Heródoto, Histórias (texto de Godley, CC BY-SA 4.0)',
             'url': 'https://github.com/PerseusDL/canonical-greekLit/tree/master/data/tlg0016/tlg001',
             'nota': 'transcrição do grego de Godley, base do texto ao lado'},
        ],
    },
}

L1 = 'Livro I'
L2 = 'Livro II'
L3 = 'Livro III'
L4 = 'Livro IV'
L5 = 'Livro V'
L6 = 'Livro VI'
L7 = 'Livro VII'
L8 = 'Livro VIII'
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
    # livro III (Tália)
    (L3, 'Cambises marcha contra o Egito (1–9)', ['livro3-1-9.txt']),
    (L3, 'Psamenito e a conquista do Egito (10–16)', ['livro3-10-16.txt']),
    (L3, 'A expedição contra os etíopes (17–26)', ['livro3-17-26.txt']),
    (L3, 'A loucura de Cambises (27–38)', ['livro3-27-38.txt']),
    (L3, 'Polícrates e o anel (39–47)', ['livro3-39-47.txt']),
    (L3, 'Periandro e Licofron; o cerco de Samos (48–60)', ['livro3-48-60.txt']),
    (L3, 'O mago e a morte de Cambises (61–66)', ['livro3-61-66.txt']),
    (L3, 'Os sete contra os magos (67–79)', ['livro3-67-79.txt']),
    (L3, 'O debate sobre o governo; Dario rei (80–88)', ['livro3-80-88.txt']),
    (L3, 'As satrapias e os tributos (89–97)', ['livro3-89-97.txt']),
    (L3, 'A Índia e as formigas do ouro (98–106)', ['livro3-98-106.txt']),
    (L3, 'A Arábia e os confins da terra (107–117)', ['livro3-107-117.txt']),
    (L3, 'Intafernes; Oretes e a morte de Polícrates (118–128)', ['livro3-118-128.txt']),
    (L3, 'Democedes (129–138)', ['livro3-129-138.txt']),
    (L3, 'Silosonte e Samos (139–149)', ['livro3-139-149.txt']),
    (L3, 'A revolta de Babilônia e Zópiro (150–160)', ['livro3-150-160.txt']),
    # livro IV (Melpômene)
    (L4, 'Dario contra os citas; as origens dos citas (1–12)', ['livro4-1-12.txt']),
    (L4, 'Aristeas e os povos do norte (13–27)', ['livro4-13-27.txt']),
    (L4, 'O inverno da Cítia e os hiperbóreos (28–36)', ['livro4-28-36.txt']),
    (L4, 'As partes da terra (37–45)', ['livro4-37-45.txt']),
    (L4, 'Os rios da Cítia (46–58)', ['livro4-46-58.txt']),
    (L4, 'Os deuses e a guerra dos citas (59–66)', ['livro4-59-66.txt']),
    (L4, 'Adivinhos, juramentos e funerais dos citas (67–75)', ['livro4-67-75.txt']),
    (L4, 'Anacársis e Cíles (76–82)', ['livro4-76-82.txt']),
    (L4, 'A ponte do Bósforo e a marcha pela Trácia (83–92)', ['livro4-83-92.txt']),
    (L4, 'Os getas e Zalmóxis; a ponte do Istro (93–98)', ['livro4-93-98.txt']),
    (L4, 'A Cítia e os seus vizinhos (99–109)', ['livro4-99-109.txt']),
    (L4, 'As amazonas e os saurômatas (110–117)', ['livro4-110-117.txt']),
    (L4, 'Os citas recuam diante de Dario (118–125)', ['livro4-118-125.txt']),
    (L4, 'Idantirso e os presentes dos citas (126–135)', ['livro4-126-135.txt']),
    (L4, 'Os jônios na ponte e a volta de Dario (136–144)', ['livro4-136-144.txt']),
    (L4, 'Os mínios e Tera (145–149)', ['livro4-145-149.txt']),
    (L4, 'Bato e a fundação de Cirene (150–158)', ['livro4-150-158.txt']),
    (L4, 'Os reis de Cirene e Feretima (159–167)', ['livro4-159-167.txt']),
    (L4, 'Os povos da Líbia (168–180)', ['livro4-168-180.txt']),
    (L4, 'As colinas de sal e os povos do deserto (181–190)', ['livro4-181-190.txt']),
    (L4, 'A Líbia ocidental (191–199)', ['livro4-191-199.txt']),
    (L4, 'O cerco de Barca e o fim de Feretima (200–205)', ['livro4-200-205.txt']),
    # livro V (Terpsícore)
    (L5, 'Os perintios, os peônios e os trácios (1–10)', ['livro5-1-10.txt']),
    (L5, 'Histieu, Côes e os peônios levados para a Ásia (11–16)', ['livro5-11-16.txt']),
    (L5, 'Os macedônios e os enviados persas; Histieu em Susa (17–27)', ['livro5-17-27.txt']),
    (L5, 'Naxos e o começo da revolta jônica (28–38)', ['livro5-28-38.txt']),
    (L5, 'Cleômenes e Dorieu (39–48)', ['livro5-39-48.txt']),
    (L5, 'Aristágoras em Esparta (49–54)', ['livro5-49-54.txt']),
    (L5, 'Hiparco, os gefireus e a queda dos Pisistrátidas (55–65)', ['livro5-55-65.txt']),
    (L5, 'Clístenes, Iságoras e as vitórias de Atenas (66–78)', ['livro5-66-78.txt']),
    (L5, 'Tebas, Egina e as estátuas de Dâmia e Auxésia (79–89)', ['livro5-79-89.txt']),
    (L5, 'Hípias e o discurso de Sosícles (90–96)', ['livro5-90-96.txt']),
    (L5, 'Aristágoras em Atenas e o incêndio de Sardes (97–103)', ['livro5-97-103.txt']),
    (L5, 'A revolta de Chipre (104–115)', ['livro5-104-115.txt']),
    (L5, 'A Cária, o Helesponto e a morte de Aristágoras (116–126)', ['livro5-116-126.txt']),
    # livro VI (Érato)
    (L6, 'Histieu e a frota jônica em Lade (1–10)', ['livro6-1-10.txt']),
    (L6, 'A batalha de Lade e a queda de Mileto (11–21)', ['livro6-11-21.txt']),
    (L6, 'Os sâmios em Zancle; a morte de Histieu (22–33)', ['livro6-22-33.txt']),
    (L6, 'Os Milcíades no Quersoneso (34–41)', ['livro6-34-41.txt']),
    (L6, 'Mardônio, Tasos e os arautos de Dario (42–50)', ['livro6-42-50.txt']),
    (L6, 'Os reis de Esparta (51–60)', ['livro6-51-60.txt']),
    (L6, 'Demarato e Leotíquides (61–72)', ['livro6-61-72.txt']),
    (L6, 'A loucura e a morte de Cleômenes (73–84)', ['livro6-73-84.txt']),
    (L6, 'Glauco e a guerra com Egina (85–93)', ['livro6-85-93.txt']),
    (L6, 'Dátis e Artafernes; a tomada de Erétria (94–101)', ['livro6-94-101.txt']),
    (L6, 'Antes de Maratona (102–110)', ['livro6-102-110.txt']),
    (L6, 'A batalha de Maratona (111–120)', ['livro6-111-120.txt']),
    (L6, 'Os alcmeônidas e o casamento de Agariste (121–131)', ['livro6-121-131.txt']),
    (L6, 'Milcíades em Paros; os pelasgos de Lemnos (132–140)', ['livro6-132-140.txt']),
    # livro VII (Polímnia)
    (L7, 'A morte de Dario; Xerxes decide a guerra (1–7)', ['livro7-1-7.txt']),
    (L7, 'O conselho de Xerxes (8–11)', ['livro7-8-11.txt']),
    (L7, 'Os sonhos de Xerxes e de Artabano (12–19)', ['livro7-12-19.txt']),
    (L7, 'O canal do Atos e as pontes (20–25)', ['livro7-20-25.txt']),
    (L7, 'Pítio, o lídio, e a marcha até Sardes (26–32)', ['livro7-26-32.txt']),
    (L7, 'As pontes do Helesponto e a marcha até Ílion (33–43)', ['livro7-33-43.txt']),
    (L7, 'Xerxes em Ábido: a conversa com Artabano (44–53)', ['livro7-44-53.txt']),
    (L7, 'A travessia e a contagem em Dorisco (54–60)', ['livro7-54-60.txt']),
    (L7, 'O exército: os povos e as armas (61–80)', ['livro7-61-80.txt']),
    (L7, 'Os comandantes, os Imortais e a cavalaria (81–88)', ['livro7-81-88.txt']),
    (L7, 'A frota e Artemísia (89–99)', ['livro7-89-99.txt']),
    (L7, 'A revista e a conversa com Demarato (100–105)', ['livro7-100-105.txt']),
    (L7, 'A marcha pela Trácia (106–120)', ['livro7-106-120.txt']),
    (L7, 'Pela Macedônia até a Tessália (121–131)', ['livro7-121-131.txt']),
    (L7, 'Os gregos que tomaram o partido dos medos; Espértias e Búlis (132–137)', ['livro7-132-137.txt']),
    (L7, 'Atenas e o muro de madeira (138–144)', ['livro7-138-144.txt']),
    (L7, 'A aliança dos gregos e Argos (145–152)', ['livro7-145-152.txt']),
    (L7, 'Gelão de Siracusa (153–162)', ['livro7-153-162.txt']),
    (L7, 'Hímera; Corcira e Creta (163–171)', ['livro7-163-171.txt']),
    (L7, 'Tempe abandonado; Termópilas e Artemísio (172–178)', ['livro7-172-178.txt']),
    (L7, 'Os primeiros encontros no mar; o tamanho do exército (179–187)', ['livro7-179-187.txt']),
    (L7, 'A tempestade na Magnésia (188–195)', ['livro7-188-195.txt']),
    (L7, 'Xerxes na Tessália e na Málida (196–201)', ['livro7-196-201.txt']),
    (L7, 'As Termópilas: os primeiros dias (202–212)', ['livro7-202-212.txt']),
    (L7, 'Efialtes e a última luta (213–225)', ['livro7-213-225.txt']),
    (L7, 'Os que se distinguiram; os epitáfios (226–233)', ['livro7-226-233.txt']),
    (L7, 'Demarato e o corpo de Leônidas (234–239)', ['livro7-234-239.txt']),
    # livro VIII (Urânia)
    (L8, 'A frota grega no Artemísio (1–5)', ['livro8-1-5.txt']),
    (L8, 'As primeiras batalhas no Artemísio e a tempestade (6–14)', ['livro8-6-14.txt']),
    (L8, 'A última batalha no Artemísio; os mortos das Termópilas (15–26)', ['livro8-15-26.txt']),
    (L8, 'Os fócios e o ataque a Delfos (27–39)', ['livro8-27-39.txt']),
    (L8, 'Atenas abandonada; a frota em Salamina (40–48)', ['livro8-40-48.txt']),
    (L8, 'O conselho em Salamina; a tomada da acrópole (49–55)', ['livro8-49-55.txt']),
    (L8, 'Temístocles convence Euribíades (56–64)', ['livro8-56-64.txt']),
    (L8, 'A visão de Diceu; o conselho de Xerxes e Artemísia (65–69)', ['livro8-65-69.txt']),
    (L8, 'O muro do istmo, a mensagem de Sicino e Aristides (70–82)', ['livro8-70-82.txt']),
    (L8, 'A batalha de Salamina (83–89)', ['livro8-83-89.txt']),
    (L8, 'O fim da batalha (90–96)', ['livro8-90-96.txt']),
    (L8, 'Xerxes decide voltar; Hermótimo (97–107)', ['livro8-97-107.txt']),
    (L8, 'Temístocles e Andros (108–112)', ['livro8-108-112.txt']),
    (L8, 'A volta de Xerxes (113–120)', ['livro8-113-120.txt']),
    (L8, 'Os prêmios; Artabazo em Potideia e Olinto (121–129)', ['livro8-121-129.txt']),
    (L8, 'As frotas em Samos e em Delos; Mardônio e os oráculos (130–135)', ['livro8-130-135.txt']),
    (L8, 'Alexandre da Macedônia e os seus antepassados (136–139)', ['livro8-136-139.txt']),
    (L8, 'A resposta dos atenienses (140–144)', ['livro8-140-144.txt']),
]
