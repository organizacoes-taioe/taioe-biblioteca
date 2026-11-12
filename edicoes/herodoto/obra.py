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
        'apresentacao': 'PROVISÓRIO',
        'fontes': [],
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
