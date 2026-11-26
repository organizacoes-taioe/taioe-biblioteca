"""Reinações de Narizinho: decisões editoriais sobre o texto de 1931.

CORRECOES: (página do PDF, trecho de 1931 como está em 1931/paginas.json, troca, tipo), aplicadas antes da
  grafia; o trecho tem de aparecer uma vez só na página. Tipos:
    'ws'    erro da transcrição do Wikisource; o fac-símile traz a forma certa (conferido nas imagens);
    'erro'  erro tipográfico evidente da edição de 1931 (vai para a lista da página «Sobre»).
NUMEROS_CAP: números de capítulo errados no impresso ((história, número de 1931) -> número certo).
INTERTITULOS: títulos sem número dentro de um capítulo (1931 -> hoje).
HIFEN_FICA: palavras partidas na virada da página que levam hífen de verdade (o resto se junta).
FICA_TRECHOS: trechos que ficam na grafia de 1931 (o bilhete de Rabicó, a piada do «elle» com dois «ll»).
FINAL: trocas depois da grafia (texto de hoje), para o que o modernizador não decide sozinho.
"""

CORRECOES = []

NUMEROS_CAP = {('II', 'XIII'): 'VIII'}          # «XIII — TOM-MIX», p. 60 do livro

INTERTITULOS = {'O CASAMENTO': 'O casamento'}

HIFEN_FICA = set()

FICA_TRECHOS = []

FINAL = []
