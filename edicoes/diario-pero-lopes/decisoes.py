"""Decisões da grafia de hoje para o Diário de Pero Lopes (texto de Varnhagen, 1839)."""
import re

COM_HIFEN = set()
JUNTAR = set()

# regras de contexto, antes da palavra por palavra
PRE = [
    (r'tam grande -revolta', 'tão grande revolta'), (r'\bsobe-la\b', 'sobre a'), (r'\blança-los\b', 'lançá-los'),
    (r"\b([Dd])esd['’] ", r'\1esde '),
    (r"\bA['’] ", 'À '), (r"\bDesde ['’] ", 'Desde '), (r"\bdesde ['’] ", 'desde '), (r'vinte é seis', 'vinte e seis'),
    (r'\bdia de natal\b', 'dia de Natal'),
    (r'\bcapitam J\.', 'capitão'),               # «capitam J.»: o capitão, irmão do autor (Varnhagen: J./I. = irmão)
    (r'\bcapitam Jd\.', 'capitão'),
    (r'\bSam (?=[A-Z])', 'São '),
    (r'\bsam (?=[A-Z])', 'São '),
    (r"\bSant'André", 'Santo André'),
    (r'\bMartimAfonso', 'Martim Afonso'),
    (r"\b[dº]'aloeste|\bdº'aloeste|\bd’aloeste", 'de oeste'),
    (r"\bdoeste\b", 'de oeste'),
    (r"\bd'elrei|\bd'elRei|\bdelRei|\bdelrei", 'del-rei'),
    (r'\belRei\b|\belrei\b', 'el-rei'),
    (r'\btodolos\b', 'todos os'), (r'\btodalas\b', 'todas as'),
    (r'\bTodolos\b', 'Todos os'), (r'\bTodalas\b', 'Todas as'),
    (r"\bn'hũa", 'numa'), (r"\bn'hum", 'num'), (r"\bd'hum", 'dum'), (r"\bd'ahi|\bdahi", 'daí'),
    (r"\bd'antes", 'dantes'), (r"\bd'outra", 'doutra'), (r"\bn'outro", 'noutro'), (r"\bdond'e", 'donde'),
    (r"\b([Dd])esd'(?=\w)", r'\1esde '), (r"\b([Dd])esd\b", r'\1esde'),
    (r"\bd'(?=\w)", 'de '), (r"\bD'(?=\w)", 'De '), (r"\bn'(?=\w)", 'na '), (r"\bnº", 'na '),
    (r'\bseis centos\b', 'seiscentos'), (r'\bsc\.', 'a saber'), (r'\bbemaventurada', 'bem-aventurada'),
    (r"\bachegandonos", 'achegando-nos'),
]
POS = [
    (r'tão grande-revolta', 'tão grande revolta'),
    (r'\bá\b', 'à'), (r'\bás\b', 'às'), (r'\bÁ\b', 'À'), (r'\bÁs\b', 'Às'),
    (r'\bmes\b', 'mês'), (r'\bmezes\b', 'meses'), (r'\bmeio dia\b', 'meio-dia'), (r'\bmeia noite\b', 'meia-noite'),
    (r'\bMeio dia\b', 'Meio-dia'), (r'\bterra do brasil\b', 'terra do Brasil'),
    (r'\b[sS]anto (?=[A-Z])', lambda m: 'Santo '), (r'\bsanta (?=[A-Z])', 'Santa '),
    (r'\bsanto (?=[A-Z])', 'Santo '), (r'\bnossa [sS]enhora\b', 'Nossa Senhora'), (r'\bnossa senhora\b', 'Nossa Senhora'),
    (r'\bBaía de todos os Santos', 'Baía de Todos os Santos'), (r'\bde de ', 'de '),
]

MANUAL_EXATO = {}

M = {
    # números e tempo
    'dous': 'dois', 'des': 'dez', 'desasete': 'dezessete', 'desaseis': 'dezesseis', 'desanove': 'dezenove',
    'desoito': 'dezoito', 'cincoenta': 'cinquenta', 'tres': 'três', 'febreiro': 'fevereiro', 'sesmo': 'sesmo',
    'segundafeira': 'segunda-feira', 'terçafeira': 'terça-feira', 'quartafeira': 'quarta-feira',
    'quintafeira': 'quinta-feira', 'sestafeira': 'sexta-feira', 'sabado': 'sábado',
    # negação, artigos, pronomes
    'nam': 'não', 'senam': 'senão', 'entam': 'então', 'nao': 'nau', 'naos': 'naus', 'tam': 'tão', 'gram': 'grande',
    'hum': 'um', 'huns': 'uns', 'hũa': 'uma', 'hũas': 'umas', 'hũs': 'uns', 'nenhũa': 'nenhuma', 'algũa': 'alguma',
    'algũas': 'algumas', 'elle': 'ele', 'ella': 'ela', 'elles': 'eles', 'della': 'dela',
    'delle': 'dele', 'dellas': 'delas', 'delles': 'deles', 'nella': 'nela', 'nelle': 'nele', 'nelles': 'neles',
    'nellas': 'nelas', 'aquelles': 'aqueles', 'aquelle': 'aquele', 'daquelle': 'daquele', 'aquillo': 'aquilo',
    'comnosco': 'conosco', 'comsigo': 'consigo', 'meo': 'meio', 'mea': 'meia', 'meos': 'meios', 'cheo': 'cheio',
    'chea': 'cheia', 'cheos': 'cheios', 'cheas': 'cheias', 'assi': 'assim', 'cousa': 'coisa', 'cousas': 'coisas',
    'antre': 'entre', 'fermosa': 'formosa', 'fermosas': 'formosas', 'fermoso': 'formoso', 'fermosura': 'formosura',
    'feo': 'feio', 'feos': 'feios', 'pexe': 'peixe', 'pexes': 'peixes', 'despois': 'depois', 'desd': 'desde',
    "desd'": 'desde', 'dond': 'donde', 'ahi': 'aí', 'he': 'é', 'ha': 'há', 'ham': 'hão',
    'per': 'por', 'pera': 'para', 'taboa': 'tábua', 'lingua': 'língua', 'linguas': 'línguas',
    # verbos em -eo / -io
    'veo': 'veio', 'choveo': 'choveu', 'perdeo': 'perdeu', 'pareceo': 'pareceu', 'morreo': 'morreu',
    'meteo': 'meteu', 'amanheceo': 'amanheceu', 'cresceo': 'cresceu', 'correo': 'correu', 'receo': 'receio',
    'vio': 'viu', 'fugio': 'fugiu', 'surgio': 'surgiu', 'deo': 'deu', 'ferio': 'feriu', 'rompeo': 'rompeu',
    'sae': 'sai', 'tomayam': 'tomavam', 'sosteve': 'susteve', 'sustivera': 'sustivera',
    'estrevemos': 'atrevemos', 'estrevi': 'atrevi', 'soportar': 'suportar', 'soportasse': 'suportasse',
    'soster': 'sustentar', 'prouve': 'prouve', 'correger': 'corrigir', 'corregemos': 'corrigimos',
    'corregendo': 'corrigindo', 'descubrir': 'descobrir', 'doscobrir': 'descobrir', 'desestisse': 'desistisse',
    'aprasivel': 'aprazível', 'aprazivel': 'aprazível', 'comegava': 'começava', 'caça': 'caça',
    # léxico náutico e gráfico
    'leguas': 'léguas', 'legua': 'légua', 'graos': 'graus', 'grao': 'grau', 'homês': 'homens', 'homẽs': 'homens',
    'menhãa': 'manhã', 'baxo': 'baixo', 'baxos': 'baixos', 'baxa': 'baixa', 'abaxo': 'abaixo', 'debaxo': 'debaixo',
    'abaxamos': 'abaixamos', 'masto': 'mastro', 'mastos': 'mastros', 'arboredo': 'arvoredo', 'arboredos': 'arvoredos',
    'arbore': 'árvore', 'arbores': 'árvores', 'anchora': 'âncora', 'anchoras': 'âncoras', 'aguagem': 'aguagem',
    'capitam': 'capitão', 'capitaina': 'capitânia', 'galeam': 'galeão', 'falcam': 'falcão', 'padram': 'padrão',
    'cerraçam': 'cerração', 'demarcaçam': 'demarcação', 'consolaçam': 'consolação', 'comunicaçam': 'comunicação',
    'informaçam': 'informação', 'geraçam': 'geração', 'salvaçam': 'salvação', 'muniçam': 'munição',
    'opiniam': 'opinião', 'escuridam': 'escuridão', 'tençam': 'tenção', 'monçam': 'monção', 'sartam': 'sertão',
    'artelharia': 'artilharia', 'artelheria': 'artilharia', 'emmendas': 'emendas', 'enjurias': 'injúrias',
    'cabellos': 'cabelos', 'captivos': 'cativos', 'christal': 'cristal', 'cristallinas': 'cristalinas',
    'gazellas': 'gazelas', 'francezes': 'franceses', 'franceza': 'francesa', 'portugues': 'português',
    'abre': 'abra', 'cõs': 'cós', 'ceos': 'céus', 'relampados': 'relâmpagos', 'pexe-': 'peixe',
    'barlaventeamos': 'barlaventeamos', 'monetas': 'monetas', 'des-': 'des',
    'loeste': 'oeste', 'aloeste': 'a oeste', 'lessueste': 'lés-sueste', 'lessuestes': 'lés-suestes',
    'lesnordeste': 'lés-nordeste', 'lessudoeste': 'lés-sudoeste', 'essudoeste': 'és-sudoeste',
    'oessudoeste': 'oés-sudoeste', 'loessudoeste': 'oés-sudoeste', 'loesnoroeste': 'oés-noroeste',
    'esnoroeste': 'és-noroeste', 'oestesudoeste': 'oés-sudoeste', 'nornordeste': 'nor-nordeste',
    'nornoroeste': 'nor-noroeste', 'sulsudoeste': 'su-sudoeste', 'sulsueste': 'su-sueste',
    'susudeste': 'su-sudoeste', 'suestes': 'suestes',
    # nomes
    'lixboa': 'Lisboa', 'tenarife': 'Tenerife', 'loronha': 'Noronha', 'maranham': 'Maranhão', 'lioa': 'Leoa',
    'peraguay': 'Paraguai', 'piratinimga': 'Piratininga', 'çofala': 'Sofala', 'india': 'Índia', 'indios': 'índios',
    'balta': 'Balta', 'agostinho': 'Agostinho', 'baltazar': 'Baltazar', 'bahia': 'baía',
}
M.update({
    'frechos': 'freixos',
    'grupezes': 'gurupés',
    'fatexa': 'fateixa',
    'taçalhos': 'tassalhos',
    'surderia': 'surdiria',
    'sorgem': 'surgem',
    'pilouro': 'pelouro',
    'repairo': 'reparo',
    'punhamo': 'púnhamo',
    'molher': 'mulher',
    'molheres': 'mulheres',
    'mercaderia': 'mercadoria',
    'meuda': 'miúda',
    'meudos': 'miúdos',
    'neboa': 'névoa',
    'nevoa': 'névoa',
    'pustura': 'postura',
    'páos': 'paus',
    'roim': 'ruim',
    'sacreficios': 'sacrifícios',
    'secenta': 'sessenta',
    'sigura': 'segura',
    'supita': 'súbita',
    'supito': 'súbito',
    'tauro': 'Touro',
    'sagitario': 'Sagitário',
    'tromenta': 'tormenta',
    'tromentas': 'tormentas',
    'tavoado': 'tabuado',
    'conversavel': 'conversável',
    'cubertas': 'cobertas',
    'dam': 'dão',
    'sam': 'são',
    'estam': 'estão',
    'derrador': 'derredor',
    'emburilhada': 'embrulhada',
    'emxarcia': 'enxárcia',
    'escarcéo': 'escarcéu',
    'escaços': 'escassos',
    'ilheos': 'ilhéus',
    'inavegavel': 'inavegável',
    'iamo': 'íamo',
    'faziame': 'fazia-me',
    'demoravame': 'demorava-me',
    'demoravamme': 'demorava-me',
    'rezões': 'razões',
    'carracas': 'carracas',
    'porras': 'porras',
    'eramos': 'éramos',
    'foramos': 'fôramos',
    'poz': 'pôs',
    'quasi': 'quase',
    'annes': 'anes', 'antonio': 'Antônio',
    'travez': 'través',
    'pareceo': 'pareceu',
    'rompeo': 'rompeu',
    'annos': 'anos',
    'anno': 'ano',
    'ma': 'ma'
})
M.update({'ló':'ló','saío':'saiu','daquesta':'desta','abombarda':'bombarda','sól':'sol','mór':'mor'})
M.update({'ellas':'elas','experiencia':'experiência','frecha':'flecha','frechas':'flecha','frechos':'freixos'})
M['frechas']='flechas'
MANUAL = M


# erros do impresso de 1839 emendados (de, para); entram na lista «Erros do impresso» da «Sobre»
ERROS = [
    ('mandon Martim Afonso', 'mandou Martim Afonso'),
    ('santa Crara', 'santa Clara'),
    ('Pedre Annes', 'Pedro Anes'),
    ('era oue nam', 'era que nam'),
    ('nao to- . mada', 'nao tomada'),
]


def corrigir(e):
    for de, para in ERROS:
        e = e.replace(de, para)
    return e
