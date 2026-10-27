"""Os Lusíadas: do texto montado (montar.obra) ao arquivo do site, conteudo/luis-de-camoes/os-lusiadas.js.

Chamado por montar.py --publicar. Cada canto é uma parte; cada estrofe, um bloco de versos com o
número à margem ({e N} no começo do primeiro verso). A página «Sobre» lista os erros da 1ª edição
corrigidos (só os de palavra: a grafia não entra) e as lições de 1572 mantidas contra o Wikisource.
"""
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao import montar as site  # noqa: E402

META = {
    'id': 'os-lusiadas',
    'autor': 'luis-de-camoes',
    'titulo': 'Os Lusíadas',
    'ano': 1572,
    'genero': 'Epopeia',
    'divisao': {'singular': 'canto', 'plural': 'cantos'},
    'descricao': 'Poema épico em dez cantos, publicado em 1572: a viagem de Vasco da Gama à Índia e a história de Portugal.',
}

APRESENTACAO = """**Texto-base.** Este texto reproduz a primeira edição de _Os Lusíadas_ (Lisboa, em casa de António Gonçalves, 1572), a única publicada em vida de Camões, na grafia brasileira de hoje.

**Como foi estabelecido.** A lição é a da 1ª edição, pela transcrição diplomática do Projeto Gutenberg, feita sobre as imagens da Biblioteca Nacional de Portugal. A pontuação e a divisão em versos partiram do texto em grafia atualizada do Wikisource, conferido palavra por palavra com a 1ª edição: onde os dois divergiam, valeu a 1ª edição, salvo erro evidente de composição, e as rimas de cada oitava foram conferidas uma a uma. Em alguns casos foi a rima que decidiu a favor de 1572 (_Reno_, III,58; _valo_, VI,65; _terreste_, VII,6). O Wikisource tem erros próprios, que a 1ª edição corrige: em dezoito versos troca «e» por «o», e em outros lê «amigo» por «imigo», «faina» por «fama», «inundo» por «mundo».

**Grafia.** Mudou só a maneira de escrever (ſ, u e v, i e j, y, ph, letras dobradas, til), nunca a forma da palavra. Ficam as formas de Camões, que muitas vezes pesam na contagem das sílabas ou na rima: _pera_, _polo_, _imigo_, _despois_, _fermoso_, _milhor_, _dous_, _cousa_, _inda_, _mui_, _assi_, _mi_, _baxo_, _sospeita_, _cubiça_, _insinar_. As contrações de «com» com o artigo seguem uma notação só (_co'o_, _co'a_, _co'os_, _c'um_), e as elisões levam apóstrofo (_d'alta_, _n'água_).

**Divisão.** Dez cantos, com o número de cada estrofe à margem."""

FONTES = [
    {'nome': 'Os Lusíadas, 1ª edição, 1572 (Biblioteca Nacional de Portugal)', 'url': 'https://purl.pt/1/',
     'nota': 'fac-símile; a transcrição usada foi feita sobre ele'},
    {'nome': 'Projeto Gutenberg, eBook nº 27236', 'url': 'https://www.gutenberg.org/ebooks/27236',
     'nota': 'transcrição diplomática da 1ª edição, por Rui Baptista: a base da lição'},
    {'nome': 'Wikisource, Os Lusíadas (grafia atualizada)', 'url': 'https://pt.wikisource.org/wiki/Os_Lus%C3%ADadas',
     'nota': 'base da pontuação e da divisão em versos; conferido palavra por palavra com a 1ª edição'},
]

# lições de 1572 mantidas contra o Wikisource (e parte das edições modernas)
MANTIDAS = [
    {'cap': 'I, 5', 'texto': 'Que se espalhe e se conte no universo', 'variante': 'se cante', 'obs': 'lição da 1ª edição'},
    {'cap': 'II, 43', 'texto': 'o choro lhe acrescenta', 'variante': 'acrescente', 'obs': 'rima com «aumenta» e «apresenta»'},
    {'cap': 'III, 58', 'texto': 'e do Reno', 'variante': 'Rene', 'obs': 'rima com «Sarraceno» e «ameno»'},
    {'cap': 'III, 84', 'texto': 'Com fama suas obras valerosas', 'variante': 'faina', 'obs': 'lição da 1ª edição'},
    {'cap': 'IV, 85', 'texto': 'Pera buscar do mundo novas partes', 'variante': 'inundo', 'obs': 'lição da 1ª edição'},
    {'cap': 'IV, 26–41', 'texto': 'imigo, imigas, imigos (5 vezes)', 'variante': 'amigo, amigas, amigos', 'obs': 'o sentido pede «inimigo»'},
    {'cap': 'VI, 65', 'texto': 'vão do valo', 'variante': 'vale', 'obs': 'rima com «intervalo» e «cavalo»'},
    {'cap': 'VII, 6', 'texto': 'A cidade Hierosólima terreste', 'variante': 'terrestre', 'obs': 'rima com «celeste» e «quiseste»'},
    {'cap': 'VII, 5–40', 'texto': 'Nem por tomar a terra… (6 versos)', 'variante': 'Não', 'obs': 'lição da 1ª edição'},
]

# diferenças que são só de grafia ou de notação, e não erro de 1572 (fora da lista de erros)
GRAFIA = {
    'q', 'poem', 'Poem', 'Poem ſe', 'poẽ', 'Poẽ', 'ſpirito', 'ſprito', 'Hião ſe', 'Vião ſe', 'Sentio o', 'vio o', 'Fim', 'F I M',
    'com noſco', 'com voſco', 'com tigo', 'inda q', 'ande', 'Ouuio o', 'Ouuio', 'Manoel', 'Monoel', 'Emanoel', 'Hemiſperio',
    'Emiſperio', 'Emiſperio ſomnolento', 'omnipotente', 'mais', 'ceita', 'aluerez', 'Alueres', 'Eſpedação ſe', 'Arrepião ſe',
    'Edificão ſe', 'Ficão lhe a tras', 'faltão lhe', 'Chamãolhe', 'Chorarão te', 'Condenarã no', 'Curão no aas', 'Dãos os',
    'Trazião a', 'Partioſe', 'ſatreue', 'ſacabaſſem', 'ſeſqueção', 'Ouuiolhe eſtas', 'lhapreſenta aſsi', 'deſdo', 'Deſdo', 'desda',
    'ate qui', 'Ate qui', 'Nũ', 'Cũa', 'Salgũa', 'ſobriſto', 'q ẽ Frãça', 'Porque creção', 'reuelde porque', 'reuela Porque',
    'Fujirme porque', 'fogio Por que', 'Hispheria', 'Hiſperia', 'Hisperia ati', 'gram viajem', 'dous veroẽs Em quanto',
    'cos paſſeos', 'Tambem', 'tãbem', 'vaãs tambem', 'Martyris', 'concelho', 'encenço', 'Scipioẽs', 'gouernala', 'Silicios',
    'prepheta', 'hypocreſia', 'emnobrecidos', 'velloces', 'veloces', 'feroces', 'ſequaces', 'oucioſos', 'oucioſa', 'eſparaua',
    'eſparança', 'ecceſsiuo', 'ecceſtiuos', 'eccellencia', 'currutos', 'Canareas', 'diuido', 'diuidoſo', 'caẽs de preſſa',
    'parelles', 'conſilio', 'Heroe', 'eſquecem', 'quaeſquer propafitos', 'Mohometa', 'Pera Eranceſes pera', 'deção Aſsi',
    'trabalho do', 'Neuarra cos', 'Co ſogo', 'Iuleo', 'Ouuemos', 'eſinaltão', 'Deoſes cos', 'corteſaõs a caſo', 'Corteſaõs',
    'corteſaõs', 'Aa Deoſa', 'ham de', 'Dhũa molher', 'Dhũa', 'de preſſa Aa', 'Deos homem', 'geito Pera', 'geito Aa', 'Poem me',
    'Seguẽ no', 'propoẽ lhe', 'cigueira Encherãome', 'doẽs', 'acrecenta',
}


def _sem(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def _forte(s):
    """Chave que ignora a grafia (para separar erro de palavra de diferença de grafia)."""
    s = _sem(s.lower().replace('ſ', 's').replace('ũ', 'un').replace('ẽ', 'en').replace('ã', 'an').replace('õ', 'on'))
    s = re.sub(r'[^a-z]', '', s)
    for a, b in [('ph', 'f'), ('th', 't'), ('ch', 'c'), ('qu', 'c'), ('y', 'i'), ('h', ''), ('z', 's'), ('x', 's'), ('j', 'i'), ('v', 'u')]:
        s = s.replace(a, b)
    s = re.sub(r'(.)\1', r'\1', s)
    s = re.sub(r'an?o(s?)$|a[nm](s?)$', r'an\1', s)
    s = re.sub(r'm(?=[^aeiou]|$)', 'n', s)
    s = re.sub(r'n$', '', s)
    s = re.sub(r'eo(s?)$', r'eu\1', s).replace('oe', 'oi').replace('ae', 'ai').replace('ue', 'ui')
    s = re.sub(r'gu(?=[ao])', 'g', s).replace('ct', 't').replace('pt', 't').replace('mn', 'n').replace('sc', 's')
    return re.sub(r'ei(?=[aou])', 'e', s)


def erros(ocorrencias, brasileira):
    lista = []
    for c, n, a, b, o, d, prox_g, prox_w in ocorrencias:
        if d == 'K' or a in GRAFIA:
            continue
        o = o.replace(' / ', ' ')
        if _forte(a) == _forte(o):
            continue
        de, para = a.replace('ſ', 's'), o
        if len(_sem(a)) <= 3 or not o:              # palavra curta ou suprimida: com a palavra seguinte
            de = (de + ' ' + prox_g.replace('ſ', 's')).strip()
            para = (para + ' ' + prox_w).strip() if o else '(suprimido) ' + prox_w
        lista.append({'cap': f'{c}, {n}', 'de': de, 'para': brasileira(para)})
    return lista


TITULOS = ['Canto Primeiro', 'Canto Segundo', 'Canto Terceiro', 'Canto Quarto', 'Canto Quinto', 'Canto Sexto', 'Canto Sétimo',
           'Canto Oitavo', 'Canto Nono', 'Canto Décimo']


def partes(est):
    cantos = {}
    for c, n, ls in est:
        cantos.setdefault(c, []).append({'verso': ['{e %d} %s' % (n, ls[0])] + ls[1:]})
    return [{'n': c, 'titulo': t, 'paragrafos': cantos[c]} for c, t in zip(cantos, TITULOS)]


def publicar(est, ocorrencias, brasileira):
    edicao = {'apresentacao': APRESENTACAO, 'fontes': FONTES, 'erros': erros(ocorrencias, brasileira), 'mantidas': MANTIDAS,
              'secoes': {'erros': {'titulo': 'Erros da 1ª edição corrigidos',
                                   'explica': 'Erros de composição e lições que a rima, o sentido ou as outras edições corrigem. '
                                              'À esquerda, a 1ª edição na grafia original; o lugar é canto e estrofe.'},
                         'mantidas': {'explica': 'Pontos em que o Wikisource (e parte das edições modernas) lê diferente.'}}}
    destino = os.path.join(RAIZ, 'conteudo', META['autor'], META['id'] + '.js')
    comentario = ('Os Lusíadas — Luís de Camões\n   Gerado por edicoes/os-lusiadas/montar.py --publicar. Não edite à mão:\n'
                  '   corrija as decisões em edicoes/os-lusiadas/ e rode de novo.\n\n'
                  '   Cada estrofe é um bloco de versos («| »); {e N} marca o número da estrofe.')
    site.publicar(destino, META, partes(est), edicao, comentario)
    rel = 'conteudo/' + META['autor'] + '/' + META['id'] + '.js'
    if site.registrar_no_index(os.path.join(RAIZ, 'index.html'), rel):
        print('acrescentado ao index.html:', rel)
    print('publicado:', destino, f"({len(edicao['erros'])} erros corrigidos)")
