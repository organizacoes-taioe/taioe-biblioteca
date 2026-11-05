"""Minha Formação — texto da página «Sobre esta edição»."""

COMENTARIO = '''Minha Formação — Joaquim Nabuco
   Gerado por ferramentas/texto.py a partir de edicoes/minha-formacao/. Não edite à mão:
   corrija as decisões em edicoes/minha-formacao/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso;
     - parágrafos começados por "¤ " são as notas do autor, no fim do capítulo.'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a primeira edição em livro de _Minha Formação_ (Rio de Janeiro e Paris, H. Garnier, 1900), a única publicada em vida do autor, morto em 1910. Como diz o prefácio, a maior parte do livro saiu antes no _Commercio de S. Paulo_, em 1895, e depois na _Revista Brasileira_; para o volume, Nabuco juntou capítulos de um manuscrito mais antigo, escreveu a conclusão e fez «emendas e variantes» nos artigos. O texto aqui é o de 1900.

**Como foi estabelecido.** Foram confrontadas palavra por palavra três leituras da edição de 1900, de dois exemplares: a transcrição do Projeto Gutenberg (2025, feita à mão pelos revisores do Distributed Proofreaders sobre as imagens do exemplar da Universidade de Toronto), o reconhecimento automático (OCR) do mesmo exemplar, no Internet Archive, e o OCR do exemplar da Universidade Harvard, digitalizado pelo Google. A transcrição do Gutenberg é fiel ao livro, até nos erros de composição; os dois OCRs serviram para apontar onde ela podia ter errado, e cada um desses pontos foi conferido nas imagens. Assim se corrigiram umas poucas leituras dela («Sua Eminência, com efeito», e não «cora efeito»; «cristalizava-se»; «da casa tudo», e não «da casatudo»). Dois textos modernos serviram só para a grafia: o que está no Wikisource, sobre as páginas do exemplar de Harvard, e o das _Obras Completas_ (São Paulo, Instituto Progresso Editorial, 1949); os dois mudam o texto em vários pontos, e aqui ficou o de 1900.

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1900, que os dois exemplares trazem: letras trocadas ou que faltam («ciaphana», «concidiu», «instituções», «servidares», «reponsabilidade»), palavras repetidas («diante de um de um grande chefe»), a concordância que a composição estragou («a cuja mãos», «sua marcas», «em um religião») e as palavras estrangeiras estropiadas («consuetuoinem», «self-governement», «constitutional»). A lista completa vem abaixo. Ficaram as formas do autor que podem ser intencionais: «bailada», «cravado» («o que havia impresso e cravado no dele»), «inda».

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _idéa_ → ideia, _paiz_ → país, _Egreja_ → Igreja, _Estados-Unidos_ → Estados Unidos, _Pariz_ → Paris, _Luiz_ → Luís, _cincoenta_ → cinquenta, _regimen_ → regímen. Os nomes de pessoas e lugares do Brasil e de Portugal também (_Ruy_ → Rui, _Luiz Gama_ → Luís Gama, _Parahyba_ → Paraíba); os estrangeiros ficam na língua deles, na forma certa (_Czacki_, _Bismarck_, onde 1900 tem _Czaki_, _Bismark_). As formas antigas de palavras que continuam em uso passaram à forma atual (_cousa_ → coisa, _coiro_ → couro). A crase segue a do livro, que a marca com o acento agudo («á», «áquelle»). O vocabulário e as construções do autor ficaram como estão: a colocação dos pronomes, as palavras e as citações em francês, inglês, latim, italiano e espanhol (_self-government_, _politicians_, _bon à tirer_), os títulos de jornais e livros, a pontuação, as reticências, as aspas angulares, os itálicos e as abreviaturas da época (_S. Paulo_, _D. Pedro II_, _Mme._, _Mgr_).

**Divisão.** O livro tem um prefácio, datado de San Sebastián, 8 de abril de 1900, e vinte e seis capítulos numerados e com título, como em 1900; cada capítulo é uma página desta biblioteca. A dedicatória («A meus filhos») abre o prefácio. As quatro notas de rodapé do autor vão no fim do seu capítulo, e as linhas de asteriscos que separam as seções de alguns capítulos foram mantidas.'''

BASE = 'Edição de 1900'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1900 corrigidos',
              'explica': 'Grafia de 1900 nas duas colunas; ¶ marca o começo de um parágrafo.'},
}

FONTES = [
    {'nome': 'Fac-símile da 1ª edição, 1900, exemplar da Universidade de Toronto (Internet Archive)',
     'url': 'https://archive.org/details/minhaformao00nabuuoft',
     'nota': 'as imagens decidiram as dúvidas; o OCR que vem com elas foi a segunda leitura'},
    {'nome': 'Fac-símile da 1ª edição, 1900, exemplar da Universidade Harvard (Wikimedia Commons)',
     'url': 'https://commons.wikimedia.org/wiki/File:Minha_forma%C3%A7%C3%A3o_(1900).djvu',
     'nota': 'digitalização do Google pela HathiTrust; o OCR que vem no arquivo foi a terceira leitura'},
    {'nome': 'Projeto Gutenberg, nº 76030', 'url': 'https://www.gutenberg.org/ebooks/76030',
     'nota': 'transcrição da 1ª edição (2025), sobre as imagens do exemplar de Toronto'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Minha_forma%C3%A7%C3%A3o',
     'nota': 'texto moderno, posto sobre as páginas do exemplar de Harvard; referência para a ortografia'},
    {'nome': 'Obras Completas de Joaquim Nabuco, vol. 1 (Instituto Progresso Editorial, 1949), na Brasiliana USP',
     'url': 'https://digital.bbm.usp.br/handle/bbm/4743',
     'nota': 'referência para a ortografia onde o texto do Wikisource falta'},
]

MANTIDAS = []

# erros de 1900 que a transcrição do Gutenberg já traz corrigidos (os dois exemplares os têm; conferidos no
# fac-símile): (lugar, 1900, corrigido)
ERROS_ANTERIORES = [
    ('XVIII', 'o deposito da moral e das costumes', 'o deposito da moral e dos costumes'),
]
