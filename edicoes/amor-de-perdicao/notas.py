"""Amor de Perdição — texto da página «Sobre esta edição»."""

COMENTARIO = '''Amor de Perdição — Camilo Castelo Branco
   Gerado por ferramentas/texto.py a partir de edicoes/amor-de-perdicao/. Não edite à mão:
   corrija as decisões em edicoes/amor-de-perdicao/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - parágrafos começados por "¤ " são notas do autor (vão para o fim da página).'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição de _Amor de Perdição (Memórias de uma família)_ (Porto, em casa de N. Moré, 1862), escrita, como diz a dedicatória, na cadeia da Relação do Porto, em 1861. Camilo reviu o romance na segunda edição (1864) e na quinta (1879), a que juntou um prefácio novo; essas edições estão digitalizadas só em imagem, sem transcrição que se possa confrontar, e por isso a base é a primeira, a única com transcrição feita sobre as imagens. As mudanças das edições revistas (por exemplo, a frase «Amou, perdeu-se e morreu amando», que entrou no prefácio depois de 1862) não estão aqui.

**Como foi estabelecido.** O texto é o da transcrição do Projeto Gutenberg, feita sobre as imagens da Biblioteca Nacional Digital de Portugal, confrontada palavra por palavra com a do Wikisource, página a página sobre o fac-símile da primeira edição (um terço das páginas revisto sobre as imagens). As duas são aparentadas, e onde divergiam valeu a leitura apoiada pelas edições modernas. Corrigiram-se os erros de leitura que as duas transcrições partilham, quase todos de uma letra («urn» por um, «fllha», «eslava», «hoa» por boa, «Monehique» por Monchique, «pergutou» por perguntou), todos conferidos nas imagens da primeira edição. Não há outras intervenções no texto; formas estranhas que a primeira edição de fato imprime, como «promenores» e «meus dezoitos anos» (na mesma página da carta que antes diz «dezoito»), ficaram.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _pae_ → pai, _Thereza_ → Teresa, _Balthazar_ → Baltasar, _sciencia_ → ciência, _Antonio_ → Antônio, _logar_ → lugar, _cincoenta_ → cinquenta, _roixo_ → roxo, _comsigo_ → consigo; o apóstrofo das contrações saiu, com a palavra junta ou separada como se escreve hoje (_d'elle_ → dele, _n'uma_ → numa). O vocabulário e as construções do autor ficaram como estão: as mesóclises, a colocação dos pronomes, as formas antigas que são do autor (_degradado_ por degredado, _esperam-a_, _impecer_), a pontuação, os travessões, as aspas angulares e os itálicos, e as abreviaturas da época, com as letras sobrescritas na linha (_v. s.ª_, _v. ex.ª_, _Ill.mo_, _vm.ce_).

**Divisão e notas.** O romance tem dedicatória, prefácio, duas partes de dez capítulos cada uma e conclusão. A primeira edição numera os capítulos de I a X em cada parte; aqui eles vão de I a XX, e cada um é uma página desta biblioteca. As seis notas do autor, que em 1862 vêm todas no fim do volume, estão no fim do capítulo em que aparece a chamada.'''

FONTES = [
    {'nome': 'Fac-símile da 1ª edição (Wikimedia Commons)', 'url': 'https://commons.wikimedia.org/wiki/File:Amor_de_Perdi%C3%A7%C3%A3o_(1862).pdf', 'nota': 'base do Wikisource'},
    {'nome': 'Projeto Gutenberg, nº 16425', 'url': 'https://www.gutenberg.org/ebooks/16425', 'nota': 'transcrição da 1ª edição (2005), sobre as imagens da Biblioteca Nacional Digital de Portugal'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Amor_de_Perdi%C3%A7%C3%A3o_(1862)', 'nota': 'transcrição da 1ª edição página a página, sobre o fac-símile acima'},
    {'nome': 'Wikisource: edições de 1864, 1876, 1879 e 1920', 'url': 'https://pt.wikisource.org/wiki/Amor_de_Perdi%C3%A7%C3%A3o', 'nota': 'fac-símiles das edições revistas pelo autor (2ª e 5ª), ainda sem transcrição'},
    {'nome': 'Biblioteca Virtual do Estudante Brasileiro (Escola do Futuro, USP)', 'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/camilo-castelo-branco/amor-de-perdicao.pdf', 'nota': 'texto da 5ª edição na grafia brasileira, com os prefácios da 2ª e da 5ª; referência para a ortografia'},
    {'nome': 'Luso Livros (2012)', 'url': 'https://archive.org/details/branco-camilo-castelo-amor-de-perdicao-lusolivros', 'nota': 'texto moderno, no Acordo de 1990 (norma de Portugal), em parte adaptado; referência para a ortografia'},
]

# (trecho do texto final, leitura de outras edições, observação)
MANTIDAS = []

# erros da 1ª edição que as transcrições já trazem corrigidos: (capítulo, 1ª edição, corrigido)
ERROS_ANTERIORES = []
