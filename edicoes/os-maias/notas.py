"""Os Maias — texto da página «Sobre esta edição»."""

COMENTARIO = '''Os Maias — Eça de Queirós
   Gerado por ferramentas/texto.py a partir de edicoes/os-maias/. Não edite à mão:
   corrija as decisões em edicoes/os-maias/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição de _Os Maias. Episódios da vida romântica_ (Porto, Livraria Internacional de Ernesto Chardron — Lugan & Genelioux, 1888, dois volumes), a única publicada em vida do autor.

**Como foi estabelecido.** Foram confrontadas palavra por palavra três transcrições dessa edição: a do Projeto Gutenberg, a do Wikisource e a da Biblioteca Virtual do Estudante Brasileiro (USP). Elas não são independentes: o Wikisource partiu do Gutenberg (o segundo volume foi depois revisto sobre as imagens), e o Gutenberg repete muitos erros da transcrição da USP, que é mais antiga. Por isso, onde duas delas concordavam contra a terceira, a maioria só valeu quando as edições modernas não apoiavam a outra leitura, e os casos duvidosos foram conferidos no fac-símile da primeira edição. Assim se recuperaram palavras e linhas que as transcrições tinham perdido («com fome! A pobre criança», «dignidade doméstica», «uma tela banal», «uma névoa», «um coupé escuro»), e se manteve a primeira edição onde as edições posteriores a emendaram («para lá se arrecadaram as mobílias», «a entregar-lha», «algum dos rapazes mais amadores»).

**Correções.** Corrigiram-se só os erros tipográficos evidentes da primeira edição, quase todos de uma letra («lacinantes», «Mussuet», «Santanaz», «cadeias» por cadeiras, «intallação»), e dois nomes trocados («o sr. Afonso de Maia», «o Carlos Gomes» por Castro Gomes). A lista vem abaixo.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _pae_ → pai, _sciencia_ → ciência, _facto_ → fato, _genio_ → gênio, _Antonio_ → Antônio, _chegámos_ → chegamos, _humido_ → úmido, _comnosco_ → conosco. As formas antigas de palavras que continuam em uso passaram à forma atual (_cousa_ → coisa, _dous_ → dois, _cincoenta_ → cinquenta, _walsa_ → valsa, _Filandia_ → Finlândia), e o apóstrofo das contrações saiu, com a palavra separada (_d'um_ → de um, _d'agua_ → de água) ou junta (_d'elle_ → dele, _n'uma_ → numa), conforme se escreve hoje; nos versos citados, as elisões ficaram. O vocabulário e as construções do autor ficaram como estão — as mesóclises, a colocação dos pronomes, as formas que ainda correm (_louro_, _ouro_ e _oiro_, _covarde_, _governante_), as palavras estrangeiras (_paletot_, _divan_, _chic_, _cognac_, _toilette_, _phaeton_), a pontuação, os travessões e as aspas angulares, os itálicos e as abreviaturas da época, com as letras sobrescritas na linha (_sr.ª_, _S.ta Olávia_, _v. ex.ª_, _M.me_).

**Divisão.** O romance tem dezoito capítulos sem título. A primeira edição os numera por volume e com dois enganos (há dois capítulos VII no primeiro volume, e o segundo salta do IV para o VII); aqui eles vão de I a XVIII, como nas edições modernas, e cada capítulo é uma página desta biblioteca.'''

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, volume 1 (Wikimedia Commons)', 'url': 'https://commons.wikimedia.org/wiki/File:Os_Maias_-_Volume_1.djvu', 'nota': 'exemplar da Universidade da Califórnia digitalizado pelo Google; usado para conferir as leituras'},
    {'nome': 'Fac-símile da 1ª edição, volume 2 (Wikimedia Commons)', 'url': 'https://commons.wikimedia.org/wiki/File:Os_Maias_-_Volume_2.pdf', 'nota': 'usado para conferir as leituras'},
    {'nome': 'Projeto Gutenberg, nº 40409', 'url': 'https://www.gutenberg.org/ebooks/40409', 'nota': 'transcrição da 1ª edição (2012), sobre as imagens da Biblioteca Nacional de Portugal, com a lista dos erros tipográficos corrigidos'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Os_Maias', 'nota': 'transcrição da 1ª edição página a página, sobre os fac-símiles acima'},
    {'nome': 'Biblioteca Virtual do Estudante Brasileiro (Escola do Futuro, USP)', 'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/eca-de-queiros/os-maias.pdf', 'nota': 'transcrição da 1ª edição, a partir de texto digitalizado pela Biblioteca Nacional de Portugal'},
    {'nome': 'Luso Livros (2012)', 'url': 'https://archive.org/details/os-maias_lusolivros', 'nota': 'texto moderno, no Acordo de 1990 (norma de Portugal); referência para a ortografia'},
    {'nome': 'eBooksFrance (2000), na edição do eBooksBrasil (2006)', 'url': 'http://www.ebooksbrasil.org/eLibris/maias.html', 'nota': 'texto moderno da mesma linhagem, na ortografia portuguesa de 1945; referência para a ortografia'},
    {'nome': 'Wikisource, dicionário de modernização (pt-BR)', 'url': 'https://pt.wikisource.org/wiki/Wikisource:Moderniza%C3%A7%C3%A3o/Dicion%C3%A1rio/pt-BR', 'nota': 'diferenças entre a grafia de Portugal e a do Brasil'},
]

# (trecho do texto final, leitura de outras edições, observação)
MANTIDAS = [
    ('para lá se arrecadaram as mobílias', 'arrecadarem', 'lição da 1ª edição, conferida no fac-símile'),
    ('a entregar-lha as amêndoas', 'entregar-lhe', 'lição da 1ª edição, conferida no fac-símile'),
    ('algum dos rapazes mais amadores', 'alguns', 'lição da 1ª edição, conferida no fac-símile'),
    ('foram-o transportando', 'foram-no', 'lição da 1ª edição, conferida no fac-símile'),
    ('uma garrafa de Bourgonhe', 'Borgonha', 'lição da 1ª edição, conferida no fac-símile'),
    ('levando para sempre o seu testemunho', 'testamento', 'lição da 1ª edição, conferida no fac-símile'),
    ('só havia facilidades', 'felicidades', 'lição da 1ª edição, conferida no fac-símile'),
    ('com uma palidez impertinente', 'polidez', 'lição da 1ª edição, conferida no fac-símile'),
    ('na cela da madre Paula', 'ceia', 'lição da 1ª edição, conferida no fac-símile'),
    ('cavalheiros da partilha de', 'partida', 'lição da 1ª edição, conferida no fac-símile'),
    ('Íntimo de Gambetta', 'do', 'a 1ª edição traz «de» aqui e «do Gambetta» logo depois'),
]

# erros da 1ª edição que as transcrições já trazem corrigidos (lista do Projeto Gutenberg; o capítulo
# vem da página): (capítulo, 1ª edição, corrigido)
ERROS_ANTERIORES = [
    ('I', "d'um planta", "d'uma planta"),
    ('I', "n'eses", "n'esse"),
    ('II', 'dehruçando-se', 'debruçando-se'),
    ('III', 'mesmo olhos', 'mesmos olhos'),
    ('III', 'o o que', 'o que'),
    ('V', 'appproximava', 'approximava'),
    ('VI', 'ningnem', 'ninguem'),
    ('VI', 'pararello', 'paralello'),
    ('VIII', 'pohre', 'pobre'),
    ('IX', 'extraordinrio', 'extraordinario'),
    ('X', 'luvar', 'luvas'),
    ('X', 'hespanhla', 'hespanhola'),
    ('X', 'o os deus', 'e os seus'),
    ('XV', 'o o monoculo', 'o monoculo'),
    ('XVI', "n'um voz", "n'uma voz"),
    ('XVII', 'moresse', 'morresse'),
    ('XVII', 'Celerico', 'Celorico'),
    ('XVII', "n'um longa", "n'uma longa"),
]
