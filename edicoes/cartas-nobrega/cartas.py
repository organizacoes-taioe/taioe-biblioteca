"""As cartas escolhidas (as 19 de Nóbrega em português do volume de 1886; ficam de fora IV e VI, que o editor traduziu
do italiano). Limites no fac-símile (páginas do PDF da Brasiliana; impressa = PDF − 16):
n = número no volume; p0/ini = página e primeira linha do corpo (depois do título e do sumário); p1/fim = página e
última linha do corpo (a data e o lugar, no fim); as notas de Valle Cabral que vêm depois ficam de fora."""

CARTAS = [
    dict(n='I', num=1, titulo='Ao Padre Mestre Simão Rodrigues', local='Bahia, abril de 1549', p0=63, ini=r'^A graça o amor', p1=67, fim=r'^Desta Bahia, 1549'),
    dict(n='II', num=2, titulo='Ao Padre Mestre Simão Rodrigues', local='Bahia, abril de 1549', p0=68, ini=r'^A graça c amor', p1=69, fim=r'^Da Bahia, 1549'),
    dict(n='III', num=3, titulo='Ao Padre Mestre Simão Rodrigues', local='Bahia, 9 de agosto de 1549', p0=70, ini=r'^A graça e amor de Nosso', p1=77, fim=r'^Desta Bahia à 9'),
    dict(n='V', num=5, titulo='Informação das terras do Brasil', local='Bahia, 1549', p0=85, ini=r'^A informação que destas', p1=89, fim=r'^fazer\.$'),
    dict(n='VII', num=7, titulo='Aos Padres e Irmãos', local='Pernambuco, 1551', p0=99, ini=r'^Em estas partes', p1=101, fim=r'^\(De Pernambuco'),
    dict(n='VIII', num=8, titulo='Aos Irmãos do Colégio de Jesus de Coimbra', local='Pernambuco, 13 de setembro de 1551', p0=102, ini=r'^Porque me quero', p1=105, fim=r'^Desta capitania de Paranambuco'),
    dict(n='IX', num=9, titulo='A El-Rei D. João III', local='Olinda, 14 de setembro de 1551', p0=106, ini=r'A graça e amor de Christo Nosso Senhor seja com', p1=109, fim=r'^Desta villa de Olinda'),
    dict(n='X', num=10, titulo='Ao Padre Provincial de Portugal', local='Bahia, 1552', p0=110, ini=r'^Uma recebi', p1=113, fim=r'^\(Da Bahia, 1552'),
    dict(n='XI', num=11, titulo='A El-Rei D. João III', local='Bahia, 1552', p0=114, ini=r'^Nosso Senhor Jesus Christo dê', p1=116, fim=r'\(Da Bahia, 1552'),
    dict(n='XII', num=12, titulo='Ao Padre Mestre Simão Rodrigues', local='Bahia, 1552', p0=117, ini=r'^Por todas as vias', p1=121, fim=r'\(Da Bahia, 1552'),
    dict(n='XIII', num=13, titulo='A El-Rei D. João III', local='São Vicente, 1554', p0=122, ini=r'graça e consolação do Espirito', p1=123, fim=r'^1554\.\)'),
    dict(n='XIV', num=14, titulo='Ao Padre Inácio de Azevedo', local='São Vicente, 1556', p0=125, ini=r'^A summa graça', p1=126, fim=r'\(Da capitania de S\. Vicente, 1556'),
    dict(n='XV', num=15, titulo='A Santo Inácio de Loyola', local='São Vicente, 1556', p0=127, ini=r'^Saberá Vossa Paternidade', p1=131, fim=r'\(De Piratininga, 1556'),
    dict(n='XVI', num=16, titulo='A Santo Inácio de Loyola: o quadrimestre de janeiro a abril de 1557', local='Bahia, 1557', p0=132, ini=r'^Este quadrimestre', p1=137, fim=r'\(Da Bahia\.\)'),
    dict(n='XVII', num=17, titulo='Aos moradores de São Vicente', local='Bahia, 1557', p0=138, ini=r'^Muito amados em Jesus', p1=142, fim=r'^Desta Bahia\.'),
    dict(n='XVIII', num=18, titulo='Ao Provincial de Portugal', local='Bahia, 1557', p0=143, ini=r'^Por via de Pernambuco', p1=149, fim=r'^\(Da Bahia, 1557'),
    dict(n='XIX', num=19, titulo='Aos Padres e Irmãos de Portugal', local='Bahia, 5 de julho de 1559', p0=150, ini=r'^A paz e amor de Christo', p1=161, fim=r'^Inutilissimo filho'),
    dict(n='XX', num=20, titulo='A Tomé de Sousa', local='Bahia, 5 de julho de 1559', p0=162, ini=r'^A paz e amor de Christo', p1=184, fim=r'^Desta Bahia, a 5 de Julho'),
    dict(n='XXI', num=21, titulo='Ao Infante Cardeal D. Henrique', local='São Vicente, 1º de junho de 1560', p0=185, ini=r'^A paz de Christo', p1=192, fim=r'^De S\. Vicente o 1'),
]
