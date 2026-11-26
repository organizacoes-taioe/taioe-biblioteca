"""Reinações de Narizinho: o texto da página «Sobre esta edição» (rascunho; completar no fim)."""

APRESENTACAO = '(a escrever)'
FONTES = []
ERROS = []


def edicao():
    return {'base': 'Edição de 1931', 'apresentacao': APRESENTACAO, 'fontes': FONTES,
            'erros': [{'cap': c, 'de': d, 'para': p} for c, d, p in ERROS]}
