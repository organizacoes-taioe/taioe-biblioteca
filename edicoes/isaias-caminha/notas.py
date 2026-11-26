"""Recordações do Escrivão Isaías Caminha — texto da página «Sobre esta edição»."""
import json
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))
_ARQ_M = os.path.join(_AQUI, 'mudancas.json')
_M = json.load(open(_ARQ_M, encoding='utf-8')) if os.path.exists(_ARQ_M) else {'itens': [], 'longos': []}
_C = json.load(open(os.path.join(_AQUI, 'conferencia.json'), encoding='utf-8'))
_N_CONF = len(_C)
_N_LONGOS = len(_M['longos'])
_PALAVRAS_LONGOS = round(sum(x['n'] for x in _M['longos']), -2)

COMENTARIO = '''Recordações do Escrivão Isaías Caminha — Lima Barreto
   Gerado por ferramentas/texto.py a partir de edicoes/isaias-caminha/. Não edite à mão:
   corrija as decisões em edicoes/isaias-caminha/ e rode de novo com --publicar.

   Formato do texto de cada parte:
     - parágrafos separados por uma linha em branco;
     - _itálico_ entre sublinhados;
     - linhas começadas por "| " formam um bloco de versos, uma linha por verso.'''

APRESENTACAO = f'''**Texto-base.** Este texto reproduz a segunda edição das _Recordações do Escrivão Isaías Caminha_ (Rio de Janeiro, A. de Azevedo & Costa, 1917), «revista e augmentada», a última publicada em vida do autor, morto em 1922. O romance começou a sair em 1907 na revista _Floreal_, que o próprio Lima Barreto editava, e saiu em livro em Lisboa, pela Livraria Clássica de A. M. Teixeira, em 1909. Na edição de 1917 o autor acrescentou a «Breve notícia», que restitui o prefácio de Isaías cortado em 1909, e devolveu ao romance trechos que tinha suprimido. O volume de 1917 traz uma errata, que foi seguida aqui.

**Como foi estabelecido.** O texto de 1917 foi lido duas vezes por reconhecimento automático (OCR), no exemplar da Brasiliana USP: a camada de texto que vem no arquivo digitalizado e uma leitura nova, feita para esta edição. As duas leituras foram confrontadas palavra por palavra; onde divergiam, valeu a que tem apoio nas edições modernas, e onde nenhuma tinha, ou onde o texto se afastava da edição moderna que segue 1917 (a da Ática), a decisão veio das imagens do livro: {_N_CONF} pontos conferidos. As edições modernas gratuitas (a da Biblioteca Virtual do Estudante Brasileiro, da USP, tirada da edição da Ática de 1995, e a do Wikisource, que segue o texto de 1909) serviram para a grafia e para o desempate, não como texto: elas mudam palavras, desdobram as abreviaturas e escrevem os números por extenso; aqui ficou o de 1917. Um exemplo: a primeira frase do livro traz, nas duas edições do autor, «a tristeza, a compressão e a desigualdade de nível mental do meu meio familiar», e não «a compreensão», como nas edições modernas.

**As mudanças de 1917.** Além da «Breve notícia», a segunda edição tem {_N_LONGOS} trechos novos, cortados ou refeitos de mais de doze palavras (umas {_PALAVRAS_LONGOS} palavras a mais), como os retratos do charadista e do cronista esportivo do jornal, no capítulo VIII, e páginas novas nos capítulos IX, X, XIII e XIV; o jornalista russo Michaelowsky passou a se chamar Gregorovitch, e a moça italiana do último capítulo, Espranza, passou a Leda; e há centenas de pequenas mudanças de palavras. A lista abaixo traz as que puderam ser confirmadas: a leitura de 1909 nas duas leituras automáticas de 1909 e na edição do Wikisource, e a de 1917 nas duas de 1917 e na edição da Ática. As de pontuação ficaram de fora, porque nelas a leitura automática não é segura.

**Correções.** Corrigiram-se os erros tipográficos evidentes da edição de 1917 (lista abaixo): as emendas da errata do próprio volume, letras e palavras trocadas ou repetidas («encontrados ortos», «creio descobrir descobrir», «Sendo obrigado obrigado»), uma fala composta duas vezes e duas passagens em que a composição de 1917 perdeu linhas inteiras, completadas pela edição de 1909 («um engenhoso aparelho de aparições e eclipses, espécie complicada de tablado de mágica»; a despedida no cais, de «com as suas mulheres e filhas» a «afastou-se logo dela com a senhora»). O nome do dr. Ricardo, diretor do jornal, foi uniformizado como «Loberant»: as duas edições do autor o escrevem assim até o capítulo IX e quase sempre «Leborant» dali em diante, e a errata de 1909 manda ler «Loberant». Ficaram as formas do autor que podem ser intencionais (lista abaixo).

**Ortografia.** A grafia foi atualizada pelo Acordo Ortográfico de 1990, na forma brasileira: _elle_ → ele, _Isaias_ → Isaías, _director_ → diretor, _idéa_ → ideia. As formas antigas de palavras que continuam em uso passaram à forma atual (_cousa_ → coisa, _dous_ → dois). O vocabulário e as construções do autor ficaram como estão: a colocação dos pronomes, as palavras estrangeiras (_footing_, _toilettes_, _pince-nez_, _restaurant_, _reporters_), os números («às 10 ou 11 horas»), a pontuação, as aspas angulares, os itálicos e as abreviaturas da época (dr., Snr., S. Ex.ª, D. Inês). A citação da _Ensynança de Bem Cavalgar_, de D. Duarte, no capítulo XIV, fica na grafia do século XV, como o autor a imprimiu.

**Divisão.** A «Breve notícia» e os catorze capítulos numerados, sem título, como em 1917; cada um é uma página desta biblioteca. A dedicatória («A Benedito de Souza, meu compadre e meu amigo») e a epígrafe de Guyau abrem a «Breve notícia».'''

BASE = 'Edição de 1917'

SECOES = {
    'erros': {'titulo': 'Erros tipográficos da edição de 1917 corrigidos',
              'explica': 'Grafia de 1917 nas duas colunas; ¶ marca o começo de um parágrafo. Inclui as emendas da errata do próprio volume.'},
    'tradicao': {'titulo': 'Mudanças da edição de 1917 sobre a de 1909',
                 'explica': 'Grafia de cada edição. Os trechos longos vão resumidos (só as palavras), com o número de palavras; '
                            '«(N vezes)» junta a mesma troca repetida. Só as mudanças confirmadas pelas duas leituras de cada '
                            'edição e pelas edições modernas.',
                 'de': '1ª edição (1909)', 'para': '2ª edição (1917)'},
}

FONTES = [
    {'nome': 'Fac-símile da 2ª edição, 1917, exemplar da Brasiliana USP', 'url': 'https://digital.bbm.usp.br/handle/bbm/4808',
     'nota': 'texto-base; lido por dois OCRs, e as imagens decidiram as dúvidas'},
    {'nome': 'Fac-símile da 1ª edição, 1909, exemplar da Brasiliana USP', 'url': 'https://digital.bbm.usp.br/handle/bbm/4799',
     'nota': 'lido por dois OCRs, para a lista das mudanças e para as linhas que faltam em 1917'},
    {'nome': 'Biblioteca Virtual do Estudante Brasileiro (Escola do Futuro, USP)',
     'url': 'https://www.curso-objetivo.br/vestibular/assets/download/obras-literarias/lima-barreto/isaias-caminha.pdf',
     'nota': 'texto moderno, da edição da Ática (1995), que segue 1917; referência para a grafia'},
    {'nome': 'Wikisource em português', 'url': 'https://pt.wikisource.org/wiki/Recorda%C3%A7%C3%B5es_do_Escriv%C3%A3o_Isa%C3%ADas_Caminha',
     'nota': 'texto moderno: a «Breve notícia» de 1917 e o romance pelo texto de 1909; referência para a grafia'},
]

MANTIDAS = [
    ('Para eternidade da espécie', 'Para a eternidade da espécie', 'assim em 1909 e em 1917'),
    ('os outros pouca gastavam', 'os outros pouco gastavam', 'assim em 1909 e em 1917'),
    ('enobrecendo ao caso', 'enobrecendo ao acaso', 'assim em 1917; «ao acaso» na edição da Ática'),
    ('de fraqueza, de decisão e mais amolecido', 'de fraqueza, de falta de decisão e mais amolecido',
     '1917 imprime «de décisão é mais»; a edição da Ática acrescenta «de falta»'),
]

# erros de 1917 que o confronto já trouxe corrigidos (três deles da errata do volume): (lugar, 1917, corrigido)
ERROS_ANTERIORES = [
    ('VI', 'um qualquer deputado attendia um pedido', 'um qualquer deputado attendesse um pedido'),
    ('VI', 'a dissolver-se nas suas aguas', 'a dissolver-me nas suas aguas'),
    ('VII', 'desistiu da lição e diminuiu-lhe o ordenado', 'desistiu da lição e diminuiu-me o ordenado'),
    ('XIV', 'Todos os Santos, Rio de Janeiro — 908', 'Todos os Santos, Rio de Janeiro — 1908'),
]

TRADICAO_EXTRA = [(x['cap'], x['de'] or '—', x['para'] or '—') for x in _M['longos'] + _M['itens']]
