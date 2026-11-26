"""Reinações de Narizinho: metadados, as onze histórias e os títulos dos capítulos na grafia de hoje.

Os títulos de 1931 vêm em maiúsculas (cabeçalhos «I — NARIZINHO»); aqui, só a caixa e a grafia mudam.
Erros do impresso nos cabeçalhos: «XIII — TOM-MIX» (é o VIII do «Sitio do Picapau Amarello») e, no índice
final, «Casa de Coruja» por «Cara de Coruja»; ver notas.py. «O CASAMENTO», no «Marquez de Rabicó», vem
em 1931 como título sem número entre os capítulos III e IV: fica como intertítulo dentro do III.
"""
META = {
    'id': 'reinacoes-de-narizinho',
    'autor': 'monteiro-lobato',
    'titulo': 'Reinações de Narizinho',
    'ano': 1931,
    'genero': 'Contos',
    'divisao': {'singular': 'história', 'plural': 'histórias', 'rotulo': 'nome', 'marcas': False},
    'descricao': 'As onze histórias do primeiro livro do Sítio do Picapau Amarelo, como saíram em 1931.',
}

ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

# (cabeçalho de 1931, título de hoje, [títulos dos capítulos de hoje, na ordem])
HISTORIAS = [
    ('NARIZINHO ARREBITADO', 'Narizinho Arrebitado',
     ['Narizinho', 'Uma vez...', 'No palácio', 'O bobinho', 'A costureira das fadas', 'A festa e o major',
      'A pílula falante']),
    ('O SITIO DO PICAPAU AMARELLO', 'O Sítio do Picapau Amarelo',
     ['As jabuticabas', 'O enterro da vespa', 'A pescaria', 'As formigas ruivas', 'Pedrinho', 'A viagem',
      'O assalto', 'Tom-Mix', 'As muletas do besouro', 'Saudades', 'A rainha', 'A volta']),
    ('O MARQUEZ DE RABICÓ', 'O Marquês de Rabicó',
     ['Os sete leitõezinhos', 'O pedido de casamento', 'O noivado de Emília', 'O jantar de Ano-Bom']),
    ('O CASAMENTO DE NARIZINHO', 'O Casamento de Narizinho',
     ['A doença do príncipe', 'O pedido', 'Os brincos do marquês', 'A chegada', 'Apuros do marquês',
      'O vestido maravilhoso', 'Vem vindo o socorro']),
    ('AVENTURAS DO PRINCIPE', 'Aventuras do Príncipe',
     ['O gato Félix', 'Entram todos', 'Tia Nastácia e a sardinha', 'Os segredos da aranha', 'Valentias',
      'Os espantos do príncipe', 'O desastre', 'Novo desastre']),
    ('O GATO FELIX', 'O Gato Félix',
     ['A história do gato', 'A história da Emília', 'O Sherlock', 'A história do visconde']),
    ('CARA DE CORUJA', 'Cara de Coruja',
     ['Preparativos', 'Cinderela', 'Branca de Neve', 'O Pequeno Polegar', 'Barba Azul', 'Outros convidados',
      'A coroinha', 'A varinha de condão', 'A partida']),
    ('O IRMÃO DE PINOCCHIO', 'O Irmão de Pinocchio',
     ['O irmão de Pinocchio', 'O pau vivente', 'O concurso', 'A zanga de Emília', 'João Fazdeconta',
      'Miragens', 'O alfinete']),
    ('O CIRCO DE ESCAVALLINHO', 'O Circo de Escavalinho',
     ['A operação cirúrgica', 'O plano de Emília', 'O circo', 'Chegam os convidados', 'O espetáculo',
      'O desastre']),
    ('A PENNA DE PAPAGAIO', 'A Pena de Papagaio',
     ['A voz', 'Preparativos', 'A partida', 'O senhor de Lafontaine', 'Emília e Lafontaine', 'A formiga coroca',
      'Esopo', 'Os animais e a peste', 'Prisioneiros', 'Peninha não falha']),
    ('O PÓ DE PIRLIMPIMPIM', 'O Pó de Pirlimpimpim',
     ['O burro falante', 'Dona Benta de cabeça virada', 'As árvores gêmeas', 'Um soco histórico',
      'Fim do Visconde de Sabugosa', 'O Pintão', 'Melhor que o pó']),
]
