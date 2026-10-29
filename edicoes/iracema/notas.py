"""Iracema — texto da página «Sobre esta edição»."""
import json
import os

COMENTARIO = '''Iracema — José de Alencar
   Gerado por ferramentas/texto.py a partir de edicoes/iracema/. Não edite à mão:
   corrija as decisões em edicoes/iracema/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - parágrafos começados por "¤ " são notas do autor;
     - "## " abre uma seção (no pós-escrito);
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = '''**Texto-base.** Este texto reproduz a terceira edição de _Iracema. Lenda do Ceará_ (Rio de Janeiro, B. L. Garnier, 1878), a última revista pelo autor que hoje se pode ler em fac-símile. Alencar a preparou, mas morreu em dezembro de 1877, e ela saiu no ano seguinte; é a base da edição crítica de M. Cavalcanti Proença (José Olympio, 1965). A primeira edição saiu em 1865 (Rio de Janeiro, Tipografia de Viana & Filhos), paga pelo autor; a segunda, de 1870 (Garnier), também revista por ele e a primeira com o pós-escrito, não está digitalizada.

**Como foi estabelecido.** O fac-símile de 1878 (exemplar da Biblioteca Real da Bélgica, no Google Livros) foi lido pela camada de texto que o próprio Google oferece. Essa leitura é boa nas palavras, mas perde os travessões das falas, as linhas curtas (a última linha de um parágrafo, as falas de uma linha só) e os itálicos, e embaralha as notas. Ela foi confrontada palavra por palavra com a transcrição da primeira edição no Wikisource, toda revista e validada sobre o fac-símile da Brasiliana USP. Onde as duas divergem, ficou 1878, salvo erro evidente da leitura (palavra que não existe, linha perdida), em que vale a primeira edição; os casos duvidosos foram conferidos nas imagens de 1878. Os itálicos são os da primeira edição. Duas edições modernas, a da Ática (1991) e a do MEC (na edição da Luso Livros), serviram de apoio e de referência para a ortografia; nenhuma das duas reproduz fielmente a de 1878 — ambas conservam muitas lições de 1865 —, e as imagens confirmaram 1878 contra elas sempre que foram consultadas («o estampido», «entre nuvem de sangue», «Eis late o cão selvagem»).

**A edição de 1878.** Sobre a primeira edição, o texto mudou em mais de setecentos pontos (lista completa abaixo): palavras trocadas («mais rápida que a ema selvagem», onde 1865 dizia «a corça»; «Bem-vindo sejas», onde dizia «Bem vieste»), frases refeitas («A fronte reclinara, e a flor do sorriso expandia-se como o nenúfar ao beijo do sol»), repetições cortadas («Bramiu Irapuã, bramiu», «Ergue Martim, ergue»), o artigo tirado antes do possessivo («colheu sua alva rede»), nomes de lugares postos na forma indígena (o _rio das garças_ e o _Acaracu_, onde 1865 dizia _Acaraú_), e a pontuação revista. Parte dessas mudanças já vinha da segunda edição. As notas também mudaram: algumas saíram (a do verbo _rugitar_, a da _cotia_), outras entraram (_aflar_, _capoeira_, _ubaia_, _inhuma_, _maracá_ e várias de lugares do Ceará).

**Correções.** Corrigiram-se só os erros tipográficos evidentes da edição de 1878 (lista abaixo, conferidos nas imagens). As palavras que a leitura do Google errou e as linhas que ela perdeu foram restituídas pela primeira edição e pelas imagens, sem registro à parte, porque não são lições de edição nenhuma.

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990 (_elle_ → ele, _hospede_ → hóspede, _christão_ → cristão, _idéa_ → ideia), também nos nomes, na forma das edições modernas (_Araken_ → Araquém, _Poty_ → Poti, _Tupan_ → Tupã, _Irapuam_ → Irapuã, _Cauby_ → Caubi, _pagé_ → pajé, _Pytiguaras_ → Pitiguaras). O _si_ conjunção passou a _se_, e o _á_ de 1878, que servia à preposição e à crase, a _a_ ou _à_ conforme o caso. Ficaram as palavras e as construções do autor: as mesóclises, a colocação dos pronomes, as formas que a língua ainda registra (_múrmuros_, _mau grado_, _quais frouxo raio_). Nas notas, as palavras tupis que o autor decompõe ficam como ele as escreveu (_ira_ — mel, _caa-pora_), porque são a matéria da etimologia. A primeira seção do pós-escrito, em que o autor discute a ortografia do seu tempo (os acentos, a preposição _á_, a conjunção _si_, as terminações _ão_ e _am_), fica na grafia de 1878: atualizada, perderia o sentido.

**Divisão e notas.** O livro tem 33 capítulos numerados, sem título; cada um é uma página desta biblioteca. Antes deles vêm a dedicatória e o prólogo da primeira edição; depois, o argumento histórico (que o livro põe no começo das notas), a carta ao Dr. Jaguaribe, da primeira edição, e o pós-escrito da segunda. Nas edições do autor as notas ficam no fim do volume, numeradas pela página; aqui cada nota vai no fim do capítulo a que se refere, sem o número da página.'''

BASE = 'Edição de 1878'

_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mudancas.json'), encoding='utf-8'))

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1878 corrigidos',
              'explica': 'Conferidos nas imagens de 1878. Na grafia de 1878.'},
    'tradicao': {'titulo': 'Mudanças da terceira edição (1878) sobre a primeira (1865)',
                 'explica': 'Todos os pontos do prólogo, do texto, do argumento histórico e da carta em que 1878 difere '
                            'de 1865, fora a grafia (as notas e o pós-escrito ficam de fora). Parte das mudanças já '
                            'estava na segunda edição (1870), que não se pôde ler. ¶ marca o começo de um parágrafo. '
                            'Grafia atualizada nas duas colunas.',
                 'de': '1ª edição (1865)', 'para': '3ª edição (1878)'},
    'mantidas': {'titulo': 'Lições de 1878 mantidas',
                 'explica': 'Pontos em que as edições modernas leem diferente (quase sempre como a primeira edição); '
                            'este texto segue 1878.'},
}

FONTES = [
    {'nome': 'Fac-símile da 3ª edição, 1878 (Google Livros)', 'url': 'https://books.google.com.br/books?id=YXq66mVeOGAC',
     'nota': 'texto-base; exemplar da Biblioteca Real da Bélgica; lido pela camada de texto do Google, com as dúvidas conferidas nas imagens'},
    {'nome': 'Fac-símile da 1ª edição, 1865 (Brasiliana USP)', 'url': 'https://digital.bbm.usp.br/handle/bbm/4660',
     'nota': 'também no Wikimedia Commons'},
    {'nome': 'Wikisource em português: a 1ª edição, 1865', 'url': 'https://pt.wikisource.org/wiki/Iracema',
     'nota': 'transcrição página a página, toda validada, sobre o fac-símile da Brasiliana'},
    {'nome': 'Edição da Ática (1991), na Biblioteca Virtual do Estudante Brasileiro (USP)',
     'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/jose-de-alencar/iracema.pdf',
     'nota': 'texto moderno; referência para a ortografia'},
    {'nome': 'Texto do MEC (Biblioteca Digital), na edição da Luso Livros (2013)',
     'url': 'https://archive.org/details/iracema-jose-de-alencar-original-lusolivros',
     'nota': 'texto moderno de outra linhagem; referência para a ortografia'},
    {'nome': 'É. D. F. Silva, dissertação sobre as edições de Iracema (PUC Minas)',
     'url': 'https://bib.pucminas.br/teses/Letras_SilvaED.pdf',
     'nota': 'quadro das variantes de 1865, 1870 e 1878, a partir da edição crítica de Cavalcanti Proença'},
]

# (trecho do texto final, leitura de outras edições, observação)
MANTIDAS = [
    ('agora que ele não tinha o ninho', 'ela (1865, Ática)', 'conferido nas imagens'),
    ('Araquém nada fez pelo hóspede', 'pelo seu hóspede (1865, Ática)', 'conferido nas imagens'),
    ('Antes de penetrar no recôndito', 'penetrar o recôndito (1865, Ática, MEC)', 'lição de 1878 também na edição crítica'),
    ('Iracema deixou pender a fronte', 'pendeu a fronte (1865, Ática, MEC)', ''),
    ('Treme a selva com o estampido', 'estrupido (1865, Ática, MEC)', 'conferido nas imagens'),
    ('entre nuvem de sangue', 'nuvens (1865, Ática, MEC)', 'conferido nas imagens'),
    ('Eis late o cão selvagem', 'Eis que late (1865, Ática)', 'conferido nas imagens'),
    ('O luar passava entre as folhas', 'passava por entre (1865, Ática, MEC)', 'conferido nas imagens'),
    ('Esta é taba dos pitiguaras', 'é a taba (1865, Ática, MEC)', 'conferido nas imagens'),
    ('alegrou-se vendo seu hóspede', 'vendo chegar seu hóspede (1865, Ática, MEC)', 'conferido nas imagens'),
    ('excursões pela montanha', 'pelas montanhas (1865, Ática, MEC)', 'lição de 1878 também na edição crítica'),
    ('ensaio ou antes mostra', 'amostra (1865, Ática, MEC)', 'lição de 1878 também na edição crítica'),
    ('reli já apurado na estampa', 'aparado (1865, Ática)', 'lição de 1878 também na edição crítica'),
]

TRADICAO_EXTRA = [(x['cap'], x['de'], x['para']) for x in _M['itens']]
