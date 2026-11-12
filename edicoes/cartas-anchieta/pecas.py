"""Cartas de Anchieta — as peças escolhidas da edição de 1933 e onde estão no fac-símile.

Fac-símile: Internet Archive, `r-19794-v_0000_grav-569_t24-C-R0150` (exemplar da Biblioteca Nacional de
Portugal). Folha do arquivo (leaf, a partir de 0) = página impressa − 3.

Cada peça: número da edição de 1933 (romano), folhas do texto (sem as notas de A. de Alcântara Machado),
língua em que Anchieta escreveu e o título que vai ao site.
"""

ITEM = 'r-19794-v_0000_grav-569_t24-C-R0150'

PECAS = [
    # (n1933, primeira folha, última folha, língua original, título)
    ('I', 32, 46, 'la', 'Ao Padre Inácio de Loiola, de Piratininga (setembro de 1554)'),
    ('II', 59, 61, 'pt', 'Aos irmãos enfermos de Coimbra, de São Vicente (1554)'),
    ('III', 64, 66, 'es', 'Ao Padre Inácio de Loiola, de Piratininga (julho de 1554)'),
    ('X', 100, 126, 'la', 'Ao Padre Geral, de São Vicente (maio de 1560): as coisas naturais de São Vicente'),
    ('XI', 141, 157, 'es', 'Ao Padre Geral, de São Vicente (1º de junho de 1560)'),
    ('XIV', 178, 191, 'es', 'Ao Padre Diogo Laínez, de São Vicente (16 de abril de 1563)'),
    ('XV', 193, 237, 'es', 'Ao Padre Diogo Laínez, de São Vicente (janeiro de 1565): as pazes de Iperoig'),
    ('XVI', 242, 251, 'pt', 'Ao Padre Diogo Mirão, da Bahia (9 de julho de 1565)'),
    ('XX', 265, 267, 'pt', 'Ao capitão Jerônimo Leitão, de Piratininga (15 de novembro de 1579)'),
    ('XXVII', 288, 290, 'es', 'Ao Padre Cláudio Aquaviva, do Espírito Santo (7 de setembro de 1594)'),
    ('XXIX', 298, 332, 'pt', 'Informação do Brasil e de suas capitanias (1584)'),
    ('XXXIII', 445, 451, 'pt', 'Informação dos casamentos dos índios do Brasil'),
    ('XXXVIII', 510, 529, 'pt', 'Sermão da Conversão de São Paulo (1568)'),
]


# folhas de figura no meio de uma peça (a 266 é o fac-símile do autógrafo da XX)
SALTAR = {266}

# o começo do texto na primeira folha de cada peça (o que vem antes é número, título e sumário de 1933)
INICIO = {
    'I': 'paz de N. S.', 'II': 'Christi', 'III': 'Maria.', 'X': 'seja comnosco', 'XI': 'ano de 1558',
    'XIV': 'Christi', 'XV': 'amor do Espirito Santo', 'XVI': 'São Vicente se escreveu', 'XX': 'vim até agora',
    'XXVII': 'Mui Reverendo em Cristo Padre Nosso', 'XXIX': 'primeiros Portugueses', 'XXXIII': 'Indios do Brasil parece', 'XXXVIII': 'JESUS',
}


def folhas_de(p):
    return [f for f in range(p[1], p[2] + 1) if f not in SALTAR]


def folhas():
    for p in PECAS:
        yield from folhas_de(p)


def pagina(folha):
    return folha + 3
