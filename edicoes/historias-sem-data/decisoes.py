"""Histórias sem Data — decisões editoriais sobre o texto estabelecido.

EMENDAS: (tipo, busca, troca) na grafia do texto-base.
  'erro' — erro evidente do impresso de 1884 (conferido no fac-símile de Toronto), aí incluídas as
           quatro emendas da errata do próprio livro;
  'ocr'  — erro só da transcrição do Gutenberg (o impresso traz a forma certa).
As lições de 1884 que fazem sentido ficam, ainda que as edições modernas as emendem (notas.MANTIDAS).
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois).
"""

EMENDAS = [
    # a errata do livro («Escaparam alguns erros typographicos faceis de emendar»)
    ('erro', 'coser-lhe as mais finas', 'coser as mais finas'),
    ('erro', 'estar-lhe a contar tudo', 'estar a contar-lhe tudo'),
    ('erro', 'que deram a força de viver', 'que lhe deram a força de viver'),
    ('erro', 'cousa evidente mais dantesca', 'cousa evidentemente mais dantesca'),
    # A Igreja do Diabo
    ('erro', 'restituam-lhe pequenas', 'restituiam-lhe pequenas'),
    ('erro', 'mais directamente e mal', 'mais directamente o mal'),
    # O Lapso
    ('erro', 'ficaram embascados', 'ficaram embasbacados'),
    ('erro', 'Logo foi o debate', 'Longo foi o debate'),
    ('erro', 'os do cabelleiro', 'os do cabelleireiro'),
    ('erro', 'serviço relevantes', 'serviço relevante'),
    ('erro', 'Desse esse dia', 'Desde esse dia'),
    # Último Capítulo
    ('erro', 'disse-me Serei padrinho', 'disse-me; serei padrinho'),
    # Singular Ocorrência
    ('erro', 'com ambos as mãos', 'com ambas as mãos'),
    # Galeria Póstuma
    ('erro', 'possivel que conchilasse', 'possivel que cochilasse'),
    ('erro', 'sobre ellas as coroas', 'sobre ella as coroas'),
    ('erro', 'anciosos; fizera-lhe', 'anciosos; fizeram-lhe'),
    # Capítulo dos Chapéus
    ('erro', 'passar o cavallo de tarde', 'passar a cavallo de tarde'),
    ('erro', 'Foi fallar á duas', 'Foi fallar ás duas'),
    # Conto Alexandrino
    ('erro', 'O meu sacrifio', 'O meu sacrificio'),
    ('erro', 'A Pythias foi o primeiro', 'E Pythias foi o primeiro'),
    ('erro', 'prisões egypicias', 'prisões egypcias'),
    ('erro', 'nervo do latrocionio', 'nervo do latrocinio'),
    # Primas de Sapucaia!
    ('erro', 'dois mezes no côrte', 'dois mezes na côrte'),
    # Uma Senhora
    ('erro', 'que não e conheciam', 'que não a conheciam'),
    ('erro', 'nutridas de arithemetica', 'nutridas de arithmetica'),
    ('erro', 'Out, damnet spot', 'Out, damned spot'),
    # Fulano
    ('erro', 'á dona casa', 'á dona da casa'),
    ('erro', 'e ao boas acções', 'e as boas acções'),
    # A Segunda Vida
    ('erro', 'tal era o o motivo', 'tal era o motivo'),
    # Noite de Almirante
    ('erro', 'rapido .. Genoveva', 'rapido . Genoveva'),
    # Manuscrito de um Sacristão
    ('erro', 'dos vinte sete annos', 'dos vinte e sete annos'),
    ('erro', 'Volto para o roça', 'Volto para a roça'),
    # Ex Cathedra
    ('erro', 'diante da mim', 'diante de mim'),
    ('erro', 'edades, não tinha mais', 'edades, não tinham mais'),
    # A Senhora do Galvão
    ('erro', 'A nhanhã obdeceu', 'A nhanhã obedeceu'),
    # As Academias de Sião
    ('erro', 'pediu e obeteve', 'pediu e obteve'),
    ('erro', 'a opinão de', 'a opinião de'),
    ('erro', 'proferiram elles o formula', 'proferiram elles a formula'),
    # só do Gutenberg (e da camada de texto do Internet Archive, de que ele saiu)
    ('ocr', 'uma que não a amasse. Diabo alçou', 'uma raça que não a amasse. O Diabo alçou'),
    ('ocr', 'SCAGNARELLE', 'SGANARELLE'),
    ('ocr', 'Chegando á casa ? Virginia', 'Chegando á casa, Virginia'),
    ('ocr', 'vai você pasar', 'vai você passar'),
    ('ocr', 'Deu logar a essa', 'Deu logar, a essa'),
    ('ocr', 'medo e da esperanca', 'medo e da esperança'),
    ('ocr', 'incuravel, disse o medico ¶ — Ah', 'incuravel, disse o medico. ¶ — Ah'),
]

AJUSTES = [
    ('grafia', 'Os serafins que engrinaldavam o', 'recém chegado', 'recém-chegado', ', detiveram-se logo'),
]

MANUAL = {
    'cincoenta': 'cinquenta',
    'Mahomet': 'Maomé',
    'David': 'Davi',
    'Job': 'Jó',
    'máu': 'mau',
    'sphynge': 'esfinge',
    'calix': 'cálix',
    'humiliação': 'humilhação',
    'almanaks': 'almanaques',
    'absorpções': 'absorções',
    'emphasis': 'ênfase',
    'desemparal-o': 'desampará-lo',
    'mau-estar': 'mal-estar',
    # formas em que as modernas leem outra palavra (lições de 1884 mantidas): grafia à mão
    'Cahiram-lhe': 'Caíram-lhe',
    'apparelho': 'aparelho',
    'collar': 'colar',
    "d'aquelle": 'daquele',
    'distribuidos': 'distribuídos',
    'magnifico': 'magnífico',
}

VERSOS = {}

# títulos de capítulo em caixa-alta no impresso: forma de frase
TITULOS = {
    'De Uma Ideia Mirífica': 'De uma ideia mirífica',
    'Entre Deus E O Diabo': 'Entre Deus e o Diabo',
    'A Boa Nova Aos Homens': 'A boa nova aos homens',
    'Franjas E Franjas': 'Franjas e franjas',
    'No Mar': 'No mar',
    'Plus Ultra!': 'Plus ultra!',
}

# As duas epígrafes, compostas em linhas no impresso (versaletes em caixa alta e baixa). O voto
# perde as quebras de linha; aqui elas voltam, linha a linha, no parágrafo logo depois do título.
EPIGRAFES = {
    ('O', 'LAPSO'): [
        'E vieram todos os oficiais... e o resto do povo, desde o pequeno até ao grande.',
        'E disseram ao profeta Jeremias: Seja aceita a nossa súplica na tua presença.',
        'Jerem. XLII, 1, 2.',
    ],
    ('CAPÍTULO', 'DOS', 'CHAPÉUS'): [
        'Géronte',
        "Dans quel chapitre, s'il vous plaît?",
        'Sganarelle',
        'Dans le chapitre des chapeaux.',
        'Molière.',
    ],
}


def corrigir(out, flags):
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
    from edicao.tokens import TOK
    for titulo, linhas in EPIGRAFES.items():
        n = len(titulo)
        achados = [i for i in range(len(out) - n) if tuple(out[i:i + n]) == titulo and out[i + n] == '¶']
        if len(achados) != 1:
            raise SystemExit(f'epígrafe de {titulo}: {len(achados)} ocorrências')
        j = achados[0] + n + 1
        fim = out.index('¶', j)
        novo = []
        for k, l in enumerate(linhas):
            novo += (['/'] if k else []) + TOK.findall(l)
        out = out[:j] + novo + out[fim:]
        flags = flags[:j] + [False] * len(novo) + flags[fim:]
    return out, flags
