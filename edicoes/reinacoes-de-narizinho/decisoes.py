"""Reinações de Narizinho: decisões editoriais sobre o texto de 1931.

CORRECOES: (página do PDF, trecho de 1931 como está em 1931/paginas.json, troca, tipo), aplicadas antes da
  grafia; o trecho tem de aparecer uma vez só na página. Tipos:
    'ws'    erro da transcrição do Wikisource; o fac-símile traz a forma certa (conferido nas imagens);
    'ws*'   o mesmo, em todas as ocorrências da página;
    'linhas' linhas trocadas na composição de 1931, recompostas (descrito na «Sobre»);
    'erro'  erro tipográfico evidente da edição de 1931 (vai para a lista da página «Sobre»).
NUMEROS_CAP: números de capítulo errados no impresso ((história, número de 1931) -> número certo).
INTERTITULOS: títulos sem número dentro de um capítulo (1931 -> hoje).
HIFEN_FICA: palavras partidas na virada da página que levam hífen de verdade (o resto se junta).
FICA_TRECHOS: trechos que ficam na grafia de 1931 (o bilhete de Rabicó, a piada do «elle» com dois «ll»).
FINAL: trocas depois da grafia (texto de hoje), para o que o modernizador não decide sozinho.
"""

CORRECOES = [
    # p. 249 do livro (PDF 260), que falta no fac-símile: o texto posto pelo Wikisource (de outra edição) acaba no
    # meio da palavra que a p. 250 completa («ter» + «ria»)
    (260, 'no mundo inteiro, ter', 'no mundo inteiro, ter-', 'ws'),
    # na p. 282 (PDF 294), também de outra edição, o nome do fabulista na forma de 1931 («Lafontaine»)
    (294, 'La Fontaine', 'Lafontaine', 'ws*'),
    # p. 283 do livro (PDF 295): linhas trocadas na composição de 1931 (conferido na imagem). Ordem impressa:
    # «...para virem cor- / e olhou. / — Inda é o que vale... casa... / Os meninos... Paiz das Fa- / para a primeira
    # viagem pelo Mundo das Maravilhas. / Isso foi daquella vez... Penninha / rendo atraz destes lambaryzinhos fritos.
    # / bulas. Mas vinham vindo. / O relogio... / ...disse dona Benta ap- / Minutos depois... / — Vem vindo...
    # você que / A negra veio da cozinha, com a colher de pau na mão, / prehensiva, indo postar-se... estrada. / tem
    # melhor vista, venha ver se descobre quem é.» Cada linha volta ao único lugar em que a frase se completa.
    (295, 'para virem cor- e olhou.\n\n— Inda é o que vale, concordou dona Benta. A fome é a unica coisa que faz Pedrinho e Narizinho voltarem para casa...\n\nOs meninos ainda não tinham voltado do Paiz das Fa- para a primeira viagem pelo Mundo das Maravilhas.\n\nIsso foi daquella vez em que partiram com o Penninha rendo atraz destes lambaryzinhos fritos. bulas. Mas vinham vindo.\n\nO relogio bateu seis horas.\n\n— Tão tarde já, Nastacia! Estou com medo que lhes tenha acontecido qualquer coisa!... disse dona Benta ap-\n\nMinutos depois viu lá longe uma nuvem de poeira.\n\n— Vem vindo um cavalleiro! Ande, Nastacia, você que\n\nA negra veio da cozinha, com a colher de pau na mão, prehensiva, indo postar-se na varanda, de olhos na estrada. tem melhor vista, venha ver se descobre quem é.',
     'para virem correndo atraz destes lambaryzinhos fritos.\n\n— Inda é o que vale, concordou dona Benta. A fome é a unica coisa que faz Pedrinho e Narizinho voltarem para casa...\n\nOs meninos ainda não tinham voltado do Paiz das Fabulas. Mas vinham vindo.\n\nIsso foi daquella vez em que partiram com o Penninha para a primeira viagem pelo Mundo das Maravilhas.\n\nO relogio bateu seis horas.\n\n— Tão tarde já, Nastacia! Estou com medo que lhes tenha acontecido qualquer coisa!... disse dona Benta apprehensiva, indo postar-se na varanda, de olhos na estrada.\n\nMinutos depois viu lá longe uma nuvem de poeira.\n\n— Vem vindo um cavalleiro! Ande, Nastacia, você que tem melhor vista, venha ver se descobre quem é.\n\nA negra veio da cozinha, com a colher de pau na mão, e olhou.', 'linhas'),
]

NUMEROS_CAP = {('II', 'XIII'): 'VIII'}          # «XIII — TOM-MIX», p. 60 do livro

INTERTITULOS = {'O CASAMENTO': 'O casamento'}

HIFEN_FICA = set()

FICA_TRECHOS = [
    # o bilhete de Rabicó (p. 65 do livro), com os erros de propósito: «O estylo, a letra, a ortographia e a
    # grammatica é tudo delle!»
    '_Pesso-vos-lhe perdão da minha kovardia. Tommiques stá qui amolando a phaca pra me matttar. Tenha ddó deste infeliz, que se assina, com perdão da palavra,_',
    'RABICO_',
]

FINAL = [
    # palavra de dois sentidos que o modernizador acentuou como substantivo: aqui é verbo
    ('quem é que fábrica esta fazenda', 'quem é que fabrica esta fazenda'),
    # o «á» de 1931 que hoje não leva crase (antes de verbo e de pronome de tratamento) ou leva no plural
    ('punha-se à farejar', 'punha-se a farejar'), ('trazemos à Vossa Sublime', 'trazemos a Vossa Sublime'),
    ('sempre à suas ordens', 'sempre às suas ordens'),
    # as piadas que dependem da grafia de 1931 (a mesma palavra, outra grafia): ficam como em 1931
    ('Fantasma, Emília, corrigiu Narizinho. F é igual a F, como você pode ver nesta caixa de fósforos.',
     'Phantasma, Emília, corrigiu Narizinho. PH é igual a F, como você pode ver nesta caixa de phosphoros.'),
    ('se encontrava um "ele" escrito com um "l" só, dizia: "Isto é bobagem; "ele" toda a vida teve dois "l".',
     'se encontrava um "elle" escrito com um "l" só, dizia: "Isto é bobagem; "elle" toda a vida teve dois "ll".'),
]
