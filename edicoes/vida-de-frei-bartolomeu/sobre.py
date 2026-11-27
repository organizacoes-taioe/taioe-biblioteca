"""Vida de D. Frei Bartolomeu dos Mártires — a página «Sobre esta edição» e a descrição (usadas por publicar.py)."""

DESCRICAO = ('A vida do arcebispo de Braga que levou a Portugal a reforma do Concílio de Trento, escrita por um '
             'frade da sua Ordem sobre os materiais de Frei Luís de Cácegas; a prosa de Frei Luís de Sousa é tida '
             'como modelo da língua.')

APRESENTACAO = """**A obra.** A _Vida de D. Frei Bertolameu dos Mártires_ saiu em Viana, em 1619, «à custa da mesma vila», na oficina de Nicolau Carvalho. A folha de rosto diz como se fez: «repartida em seis livros com a solenidade de sua tresladação, por Frei Luís Cácegas, da mesma Ordem e cronista dela na província de Portugal; reformada em estilo e ordem e ampliada em sucessos e particularidades de novo achadas por Frei Luís de Sousa». Na dedicatória à Câmara de Viana, Frei Luís de Sousa conta que Frei Luís de Granada começou a apontar as virtudes do arcebispo ainda em vida dele, que o bispo de Viseu D. Frei António de Sousa quis escrevê-la e morreu antes, e que Frei Luís de Cácegas, cronista da província, juntou os materiais num grosso volume; o provincial mandou que Frei Luís de Sousa os refizesse, e ele levou dois anos nisso. É a única edição feita em vida do autor. São Bartolomeu dos Mártires (1514–1590), arcebispo de Braga, foi beatificado em 2001 e canonizado em 2019.

**Texto-base.** A edição de 1619, lida no exemplar da Biblioteca Nacional de Portugal (res-33-a) e conferida no da Biblioteca Nacional Central de Roma (digitalizado pelo Google, no Internet Archive). As reimpressões da Tipografia Rolandiana de Lisboa (tomo I de 1818; tomos I e II de 1850 e 1853), que seguem o texto de 1619, serviram de transcrição de trabalho, para ler sem o s longo e sem as abreviaturas; onde diferem de 1619, ficou 1619.

**Como foi estabelecido.** {COMO}

**O que fica de fora.** As aprovações e licenças dos censores (fr. Tomás de Brito, fr. Agostinho de Sousa e os do Santo Ofício, do Ordinário e do Paço), que não são do autor; a tábua dos capítulos do fim do volume, que serviu para conferir os títulos; e as citações à margem (os lugares da Escritura e dos autores, como «Matth. 20»), {MARGEM}

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem das frases de 1619: he → é, hum → um, hũa → uma, Deos → Deus, foy → foi, muyto → muito, polo → pelo, pera → para, assi → assim, despois → depois, cousa → coisa, dous → dois, oje → hoje, avia → havia, erão → eram, respondeo → respondeu, sintir → sentir, minino → menino, fogir → fugir; o pronome pegado ao verbo ganha o hífen (fezlhes → fez-lhes). As mesóclises do autor ficam. Nomes de pessoas e de lugares na forma de hoje (Bertolameu → Bartolomeu, Hespanha → Espanha). Palavras que não se usam mais ficam como estão, com nota no vocabulário. As citações latinas vão em itálico, como em 1619, sem mudança de grafia. A pontuação é a de 1619. Como no impresso, cada capítulo corre num parágrafo só."""

FONTES = [
    {'nome': 'Vida de Dom Frei Bertolameu dos Martyres, Viana, 1619 — exemplar da Biblioteca Nacional de Portugal (res-33-a), fac-símile',
     'url': 'https://purl.pt/33227', 'nota': 'texto-base'},
    {'nome': 'Idem, exemplar da Biblioteca Nacional Central de Roma (Google), no Internet Archive',
     'url': 'https://archive.org/details/bub_gb_ejJfgR_PmtQC', 'nota': 'conferência'},
    {'nome': 'Vida de D. Fr. Bertolameu dos Martyres, Lisboa, Tipografia Rolandiana, 1818, tomo I (Universidade de Oxford)',
     'url': 'https://archive.org/details/vidadedfrbertol00sousgoog', 'nota': 'transcrição de trabalho'},
    {'nome': 'Idem, 1850–1853, tomos I e II (Universidade de Michigan)',
     'url': 'https://archive.org/details/vidadedfrbertol00luisgoog', 'nota': 'transcrição de trabalho; o tomo II em https://archive.org/details/vidadedfrbertol01luisgoog'},
]

COMO = ('Sete leituras por OCR (cinco feitas por nós com o Tesseract, nas duas cópias de 1619 e nas três '
        'digitalizações de Lisboa, e as do Internet Archive) foram alinhadas palavra a palavra e votadas, com 1619 '
        'decidindo; as palavras em que as leituras não concordavam, ou que não existem, foram conferidas nas imagens '
        'de 1619, assim como os títulos e o começo de cada capítulo. Os títulos dos capítulos seguem o corpo do livro, '
        'conferidos com a tábua do fim.')
MARGEM = 'que as edições de Lisboa passaram a notas de rodapé.'


def edicao():
    return {
        'base': '1619',
        'apresentacao': APRESENTACAO.replace('{COMO}', COMO).replace('{MARGEM}', MARGEM),
        'fontes': FONTES,
    }
