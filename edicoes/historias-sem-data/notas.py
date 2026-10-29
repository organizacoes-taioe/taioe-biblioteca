"""Histórias sem Data — texto da página «Sobre esta edição» (o mesmo para todos os contos)."""

COMENTARIO = '''Histórias sem Data — Machado de Assis
   Gerado por ferramentas/texto.py a partir de edicoes/historias-sem-data/: um BIBLIOTECA.obra()
   por conto. Não edite à mão: corrija as decisões nessa pasta e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos (ou epígrafe), uma linha por verso.'''

APRESENTACAO = '''**Texto-base.** Os contos seguem a primeira e única edição de _Histórias sem Data_ publicada em vida do autor (Rio de Janeiro, B. L. Garnier, 1884). O texto foi estabelecido pelo confronto de três leituras dessa edição — a transcrição do Projeto Gutenberg e dois reconhecimentos de texto (OCR) do exemplar da Universidade de Toronto digitalizado pelo Internet Archive, com programas diferentes —, com as edições modernas como árbitro. A transcrição do Gutenberg saiu da camada de texto do Internet Archive e repete os erros dela (_telus_ por telas, _tornados_ por tomados); onde as duas concordam contra o terceiro OCR, decidiram as edições modernas, e os casos duvidosos foram conferidos no fac-símile.

**Publicação original.** Todos os contos saíram antes em jornais e revistas, entre 1883 e 1884 (_Gazeta de Notícias_, _A Estação_, _Gazeta Literária_); a indicação acompanha cada conto. O texto aqui é o do livro.

**Errata do livro.** A edição de 1884 traz uma errata com quatro emendas: «Escaparam alguns erros typographicos faceis de emendar; entre outros, estes». As quatro foram aplicadas e vão listadas com os erros corrigidos: _coser-lhe_ por _coser_ (Último Capítulo), _estar-lhe a contar_ por _estar a contar-lhe_ (Fulano), _deram a força_ por _lhe deram a força_ (Noite de Almirante) e _evidente mais_ por _evidentemente mais_ (As Academias de Sião).

**Correções.** Corrigiram-se os erros evidentes do impresso de 1884 e das transcrições, listados abaixo. Onde a leitura de 1884 faz sentido, ficou, ainda que as edições modernas a emendem.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira (_egreja_ → igreja, _idéa_ → ideia, _elle_ → ele). As formas antigas de palavras que continuam em uso passaram à forma atual (_cousa_ → coisa, _dous_ → dois, _mais_ conjunção → mas, _desemparar_ → desamparar); os nomes bíblicos e históricos tomaram a forma portuguesa atual (_David_ → Davi, _Job_ → Jó, _Mahomet_ → Maomé). O vocabulário e as construções do autor ficaram como estão — as mesóclises, a colocação dos pronomes, os travessões e as aspas angulares, os itálicos e as abreviaturas. As epígrafes em francês e os nomes estrangeiros ficam como no livro.'''

BASE = 'Edição de 1884'

SECOES = {
    'erros': {'titulo': 'Erros corrigidos',
              'explica': 'Do impresso de 1884 (com as emendas da errata do próprio livro) e das transcrições. Grafia de 1884.'},
    'mantidas': {'titulo': 'Lições de 1884 mantidas',
                 'explica': 'Pontos em que as edições modernas leem diferente.'},
}

FONTES = [
    {'nome': 'Fac-símile da edição de 1884 (Universidade de Toronto / Internet Archive)',
     'url': 'https://archive.org/details/historiassemdata00machuoft',
     'nota': 'texto-base; dois OCRs usados no confronto (o do Internet Archive e um nosso, com o Tesseract)'},
    {'nome': 'Projeto Gutenberg, nº 33056', 'url': 'https://www.gutenberg.org/ebooks/33056',
     'nota': 'transcrição da edição de 1884 (a mesma do Wikisource)'},
    {'nome': 'machadodeassis.net (Fundação Casa de Rui Barbosa)', 'url': 'https://machadodeassis.net/colecoes/historias-sem-data/28920',
     'nota': 'texto moderno, conto a conto; dados da primeira publicação; referência para a ortografia'},
    {'nome': 'Obra Completa, Nova Aguilar, 1994 (MEC / Domínio Público)', 'url': 'https://archive.org/details/historiasSemData',
     'nota': 'texto moderno'},
    {'nome': 'Biblioteca Virtual do Estudante (USP) / Curso Objetivo',
     'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/machado-de-assis/historias-sem-data.pdf',
     'nota': 'outra digitação do texto do Aguilar'},
]

# (trecho do texto final, leitura de outras edições, observação)
MANTIDAS = [
    ('a ideia de ir lembrar', 'de lembrar', ''),
    ('falava da fabricação', 'de fabricação', ''),
    ('acabava de ser eleito', 'de sair eleito', ''),
    ('chegou a atrever-se', 'chegou atrever-se', ''),
    ('revista e expurgada', 'revista a expurgada', 'MDN, Aguilar'),
    ('versos de _Hissope_', 'do _Hissope_', 'MDN, Aguilar'),
    ('marquesas de antigo regímen', 'do antigo regímen', ''),
    ('estavam distribuídos', 'estava distribuído', ''),
    ('Vive Hélios', 'Viva Hélios', ''),
    ('terror de escalpelo', 'do escalpelo', ''),
    ('até o convento da Ajuda', 'ao convento', ''),
    ('por motivos de amores', 'por motivo de amores', ''),
    ('perdia a energia', 'perdi a energia', ''),
    ('ou amor ou o jantar', 'ou o amor', ''),
    ('o ser parenta', 'o ser parente', ''),
    ('demais aparelho masculino', 'aparelhos masculinos', ''),
    ('meteu o bilhete no vestido', 'no bolso do vestido', 'MDN'),
    ('realmente magnífico', 'magníficos', ''),
    ('Caíram-lhe em cima', 'Caíram-lhes', ''),
    ('fizeram delas colar', 'colares', ''),
    ('esteiriçava-se', 'inteiriçava-se', ''),
    ('sussurrou-lhe ao ouvido', 'sussurrou ao ouvido', ''),
]

ERROS_ANTERIORES = []
