"""Macunaíma — intervenções no texto de 1928 (ver CONVENCOES.md e revisao.json).

Regra da obra: a grafia de Mário é parte da obra (si, sinão, siquer, mãi, milhor, guspir, enguliu,
frexa e flexa, guela, pra/prá, inda, riba, adonde, os pronomes no começo da frase, as formas da fala).
Muda só a ortografia de época sem valor de estilo (acentos; quasi, tribu, poude; geito, tezouro,
gosar, dansa; ch/x, s/ç/z nas palavras que hoje se escrevem de outro jeito) e o erro tipográfico
conferido no fac-símile.

MANUAL: grafia de 1928 -> de hoje (chave em minúsculas; a caixa se refaz).
AJUSTES: depois da modernização, em tokens da grafia de hoje: (tipo, antes, de, para, depois).
  'ocr'  erro das leituras do OCR que o voto não pegou (conferido no fac-símile de 1928)
  'erro' erro tipográfico evidente da edição de 1928 (vai para a «Sobre»)
"""
EMENDAS = []

MANUAL = {
    'á': 'à', 'ás': 'às',          # a crase de 1928 leva agudo («ás ordens»)
    # ortografia de época, sem marca de fala (revisao.json: quasi-tribu-poude, letras-de-epoca)
    'quasi': 'quase', 'tribu': 'tribo', 'tribus': 'tribos', 'poude': 'pôde',
    'geito': 'jeito', 'geitoso': 'jeitoso', 'tezouro': 'tesouro', 'tezouros': 'tesouros',
    'tezoura': 'tesoura', 'tezouras': 'tesouras', 'tezoiros': 'tesoiros',
    'gôso': 'gozo', 'gosar': 'gozar', 'gosou': 'gozou', 'gosada': 'gozada', 'gosados': 'gozados',
    'antegôso': 'antegozo', 'dansa': 'dança', 'dansando': 'dançando', 'dansarina': 'dançarina',
    'dansaram': 'dançaram', 'dansava': 'dançava', 'dansar': 'dançar', 'dansas': 'danças',
    'cincoenta': 'cinquenta', 'milreis': 'mil-réis', 'duzentorreis': 'duzentorréis',
    'quinhentorreis': 'quinhentorréis',
    'elegancia': 'elegância', 'consciencia': 'consciência', 'sciencia': 'ciência',
    'scientifica': 'científica', 'scisma': 'cisma', 'civilisação': 'civilização',
    'civilisações': 'civilizações', 'realisava': 'realizava', 'desmoralisações': 'desmoralizações',
    'infernisado': 'infernizado', 'infernisava': 'infernizava', 'batisar': 'batizar',
    'batisou': 'batizou', 'organisados': 'organizados', 'utilisarem': 'utilizarem',
    'penalisado': 'penalizado', 'simpatisadas': 'simpatizadas', 'enlambusado': 'enlambuzado',
    'enfesado': 'enfezado', 'trapesio': 'trapézio', 'guisos': 'guizos', 'turquezas': 'turquesas',
    'sugeitos': 'sujeitos', 'lisongeiras': 'lisonjeiras', 'accrescentam': 'acrescentam',
    'lampeões': 'lampiões', 'procreação': 'procriação', 'surprêza': 'surpresa',
    'outrosim': 'outrossim', 'pezares': 'pesares', 'dactilographas': 'datilógrafas',
    'discreção': 'discrição', 'tranzatlantico': 'transatlântico', 'gazolina': 'gasolina',
    'gorgetas': 'gorjetas', 'caximbando': 'cachimbando', 'gorduxa': 'gorducha',
    'cochilhas': 'coxilhas', 'vasante': 'vazante', 'lage': 'laje', 'maguas': 'mágoas',
    'arrazo': 'arraso', 'gazeo': 'gázeo', 'cáis': 'cais', 'pausinhos': 'pauzinhos',
    'papeisinhos': 'papeizinhos', 'cristaisinhos': 'cristaizinhos', 'bezourenta': 'besourenta',
    'brazonados': 'brasonados', 'expontaneamente': 'espontaneamente', 'emquanto': 'enquanto',
    'idea': 'ideia', 'ideas': 'ideias', 'melopea': 'melopeia', 'húmida': 'úmida',
    'sopetão': 'supetão', 'afan': 'afã', 'trireme': 'trirreme',
    'masorqueiros': 'mazorqueiros', 'correcorre': 'corre-corre',
    # acento grave de 1928 nas derivadas
    'pèsão': 'pezão', 'sabiàpiranga': 'sabiapiranga', 'sabiàgongá': 'sabiagongá',
    'sabiàcica': 'sabiacica', 'sabiàpoca': 'sabiapoca', 'sabiàúna': 'sabiaúna',
    'jacarèuna': 'jacareúna', 'jacarètinga': 'jacaretinga', 'jacarèassú': 'jacareaçu',
    'inteiràmos': 'inteiramos', 'descuidàmos': 'descuidamos', 'falàmos': 'falamos',
    'chaminèzona': 'chaminezona', 'candomblèseira': 'candomblezeira', 'agùinha': 'aguinha',
    # palavras indígenas e africanas com a grafia de hoje (revisao.json: palavras-indigenas)
    'ochum': 'oxum', 'ochosse': 'oxóssi', 'macacheira': 'macaxeira', 'girau': 'jirau',
    'sussuarana': 'suçuarana', 'massaroca': 'maçaroca', 'mussuãs': 'muçuãs',
    'pagé': 'pajé', 'pagés': 'pajés', 'pagelança': 'pajelança', 'pageú': 'pajeú', 'pegí': 'peji',
    'matrinchão': 'matrinxão', 'piché': 'pixé', 'assai': 'açaí', 'assaizeiro': 'açaizeiro',
    'guassú': 'guaçu', 'saguiassú': 'saguiaçu', 'ubussú': 'ubuçu', 'ubussús': 'ubuçus',
    'taiassú': 'taiaçu', 'embirossú': 'embiroçu', 'cupuassú': 'cupuaçu', 'cangussú': 'canguçu',
    'baguassú': 'baguaçu', 'vupabussú': 'vupabuçu', 'assú': 'açu', 'uirauassús': 'uirauaçus',
    # acentos que o léxico não acertou (a forma sem acento é outra palavra, ou veio do OCR)
    'macunaima': 'macunaíma', 'porem': 'porém', 'voce': 'você', 'patria': 'pátria',
    'existéncia': 'existência', 'eloquéncia': 'eloquência', 'originarias': 'originárias',
    'policia': 'polícia', 'noticia': 'notícia', 'eletrica': 'elétrica', 'serio': 'sério',
    'cunhatá': 'cunhatã', 'cunhatâ': 'cunhatã', 'măi': 'mãi', 'èh': 'eh', 'cleopátra': 'cleópatra',
    'jóias': 'joias', 'uhúm': 'uhum', 'alvíçaras': 'alvíssaras', 'alviçaras': 'alvíssaras',
    'pêlo': 'pelo', 'tâpanhumas': 'tapanhumas', 'niesmo': 'mesmo', 'aparececesse': 'aparecesse',
    'quinhentonreis': 'quinhentorréis', 'caculou': 'calculou', 'prd': 'pra', 'cunhatās': 'cunhatãs',
    'estréias': 'estrelas', 'amaginou': 'imaginou', 'zangai': 'zangar', 'respirada': 'respirava',
    'vetes': 'vezes', 'rufaram': 'rumaram', 'castigando': 'mastigando', 'tucümãs': 'tucumãs',
    'jiguê': 'jiguê', 'jiguè': 'jiguê',
    'tucuchí': 'tucuxi', 'jamachí': 'jamaxi', 'cachirí': 'cachiri', 'çairê': 'sairê',
}

# erros de OCR que o voto não pegou e erros de 1928, conferidos no fac-símile (tokens da grafia de hoje)
AJUSTES = [
    ('ocr', 'punha os', 'lhos', 'olhos', 'em'),
    ('ocr', 'aromava', 's', 'os', 'cabelos'),
    ('ocr', 'Macunaíma', 'S (', 'se', 'aproximou'),
    ('ocr', 'rede que', 'la', 'ela', 'mesmo'),
    ('ocr', 'Ci queria', 'ir', 'rir', 'com'),
    ('ocr', 'crescia pra', 'ci -', 'cima', 'dele'),
    ('erro', 'como Jiguê', 'são', 'não', 'conseguira'),
    ('ocr', 'aqueles', 'hiatos', 'matos', 'sobre'),
    ('ocr', 'lagartixa que', 'Onda', 'anda', 'de'),
    ('ocr', 'catauaris de', 'beirado', 'beira-rio', 'o'),
    ('ocr', 'conversa ! !', '- Mira', 'Atira', 'a gente'),
    ('ocr', 'Pietra', 'Piais', 'mais', 'uma vez'),
    ('ocr', 'não', 'lenho', 'tenho', 'bastante'),
    ('ocr', 'de', 'tonta', 'tanta', 'dor'),
    ('ocr', 'caiu no', 'auto', 'santo', 'e'),
    ('ocr', 'veio vindo veio', 'indo', 'vindo', 'e'),
    ('ocr', 'Paulo', 'unha', 'tinha', 'um'),
    ('ocr', 'duma', 'ar ova', 'sova', 'de'),
    ('ocr', 'se rindo em', 'a', '', 'felicidade'),
    ('ocr', 'jangada e', 'Hão', 'não', 'ir'),
    ('ocr', 'longínquas e', 'medos', 'menos', 'férteis'),
    ('ocr', 'infestam a', 'Possa', 'nossa', 'geografia'),
    ('ocr', 'Macunaíma ,', 'tez', 'fez', 'discurso'),
    ('ocr', 'peixe nem', 'hem', 'bem', 'de'),
    ('ocr', 'furor', 'n', 'no', 'sertão'),
    ('ocr', 'Pestana e', 'debite', 'de-noite', ','),
    ('ocr', 'pais', 'mais', 'mãis', 'tias'),
    ('ocr', 'não', 'linha', 'tinha', 'nenhum'),
    ('ocr', '! ¶ —', 'EM', 'E’ !', '¶ — Ora'),
    ('ocr', 'e pernas', 'UM Praquê', 'praquê', 'vos'),
    ('ocr', 'passando', 'per', 'por', 'debaixo'),
    ('ocr', 'sem', '%', '', 'vitória'),
    ('ocr', 'essas caças', '>', '.', 'Porém'),
    ('ocr', 'urbi', 'el', 'et', 'orbe'),
    ('ocr', 'presentinhos de', 'bolode-aipim', 'bolo-de-aipim', ''),
    ('ocr', 'pra', 'SanfAna', 'Sant’Ana', 'encomendando'),
    ('ocr', 'nossa', 'mãe', 'mãi', 'Vei não'),
    ('ocr', 'Veja , nossa', 'mãe', 'mãi', 'Vei'),
    ('ocr', '¶ —', 'Mãe', 'Mãi', ', quem'),
]
