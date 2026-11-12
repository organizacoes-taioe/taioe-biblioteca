"""Cartas de Anchieta — decisões de grafia e de leitura (ver montar.py).

Tudo na forma do impresso de 1933 (1933/<folha>.txt). O que muda a leitura vai para a «Sobre esta edição»
(ERROS) ou para o revisao.json (as decisões do Gere). Base: as decisões da Vida de Anchieta (1897), que
passou o português do século XVI à grafia de hoje.
"""

HIFEN_ANTES = set()
JUNTAR = set()
ABREVIATURAS = {'s', 'd', 'n', 'v', 'cap', 'etc', 'sr', 'dr', 'fl', 'p', 'pe', 'r'}

# erros evidentes do impresso de 1933, corrigidos: (peça, de, para, comentário); vão na «Sobre»
ERROS = [
    ('II', 'ut semprer or etis pro', 'ut semper oretis pro', ''),
    ('II', 'et nutuerunt', 'et nutrierunt', ''),
    ('X', 'até que corsuma a árvore', 'até que consuma a árvore', ''),
    ('XI', 'onde har muitos', 'onde ha muitos', ''),
    ('XIV', 'tanta pressa qse não', 'tanta pressa que se não', ''),
    ('XV', 'nos rescostavamos a dormir', 'nos recostavamos a dormir', ''),
    ('XV', 'que não house medo', 'que não houvesse medo', ''),
    ('XV', 'não faza senão gritar', 'não fazia senão gritar', ''),
    ('XXVII', 'nem os merciono', 'nem os menciono', ''),
    ('XXIX', 'e trase começaram de edificar igrejas entre os Indios e se deu prindencia, como conservou',
     'e trabalhou muito de conservar a paz com os Indios com muita prudencia, como conservou',
     'linha trocada na composição; texto pela edição de Capistrano de Abreu (1886)'),
    ('XXIX', 'mais que Jouvar', 'mais de louvar', 'pela edição de 1886'),
    ('XXXVIII', 'grande mutidão de almas', 'grande multidão de almas', ''),
]
# erros miúdos de composição e de leitura, corrigidos sem lista: (peça, de, para)
COMPOSICAO = [
    ('XI', 'pronunciei ciei', 'pronunciei'),
    ('XIV', 'Pouço tempo', 'Pouco tempo'),
    ('XIV', 'Piratiuinga', 'Piratininga'),
    ('XV', 'que Jébres', 'que lebres'),
    ('XV', 'Tperuig', 'Iperuig'),
    ('XV', 'Beriguioca', 'Beriquioca'),
    ('XV', 'Venhovos a dar', 'Venho-vos a dar'),
    ('XXIX', 'Indios Jivres', 'Indios livres'),
    ('XXIX', 'Compauhia', 'Companhia'),
    ('XXIX', 'Biscairho', 'Biscainho'),
    ('XVI', 'Cabo-Prio', 'Cabo-Frio'),
    ('XV', 'Fadre', 'Padre'),
    ('XI', 'Tugares', 'lugares'),
    ('XXIX', "morreu'se confessou", 'morreu se confessou'),
    ('XXIX', '_initium sapientiœ timor Domini_ est', '_initium sapientiœ timor Domini est_'),
    ('XXXVIII', 'Bt sua serva', 'Et sua serva'),
    ('XXXVIII', 'Vêdeme', 'Vêde-me'),
    ('XV', 'Respondendolhe', 'Respondendo-lhe'),
    ('XXXIII', 'parentecco', 'parentesco'),
]
EMENDAS = []

# regex sobre o texto de 1933, antes da grafia
PRE = [
    (r"\b([EA])['’]s\b", lambda m: {'E': 'És', 'A': 'Às'}[m.group(1)]),
    (r"\bE['’] ", 'É '),
    (r"\bA['’] ", 'À '),
    (r'(\d)\.([ºª])', r'\1\2'),
    (r'\bE[º°] ', 'É '),
]

# trechos em latim fora de itálico na leitura (só as linhas conferidas trazem o itálico): vão em itálico e
# sem mudança de grafia. italicos() junta os vizinhos («_virtus_ _in infirmitate_» → um só).
LATIM_ITALICO = [
    'virtus', 'in medio iniquitatis et super flumina Babylonis', 'omnes bene valere', 'Pauper et inutilis',
    'Pax Christi', 'Pax', 'Minimus Societatis Jesu', 'Agnus Dei', 'in extremis', 'extremis', 'etiam', 'scilicet',
    'nescio quid', 'sc. furtum', 'furtum', 'lupus rapaz', 'lupus rapax', 'mane comedet predam et vespere',
    'pre consortibus suis', 'et vicit leo de tribu Juda, radix David', 'Saule, Saule, quid me persequeris',
    'Quid me persequeris', 'quid me persequeris', 'Et Saulus: Qui es, Domine', 'Ego sum Jesus, quem tu persequeris',
    'Ego sum Jesus quem tu persequeris', 'durum est tibi', 'vas electionis', 'Vas electionis est mihi iste',
    'Domine, quid me vis facere', 'quid me vis facere', 'arma iniquitatis', 'in mentis excessu', 'et vespere dividet',
    'sunt', 'Quia qui', 'ingredere civitatem', 'Ingredere civitatem', 'Deus meus, Deus meus, quid dereliquisti me',
    'Ad quam', 'militia est vita', 'de tribu Juda', 'sponsa',
]
LATIM = []


def italicos(texto):
    import re
    partes = re.split(r'(_[^_]+_)', texto)
    for i in range(0, len(partes), 2):
        p = partes[i]
        for fr in sorted(LATIM_ITALICO, key=len, reverse=True):
            p = re.sub(r'(?<![A-Za-zÀ-ÿ_])' + re.escape(fr) + r'(?![A-Za-zÀ-ÿ_])', '_' + fr + '_', p)
        partes[i] = p
    t = ''.join(partes)
    for _ in range(3):
        t = re.sub(r'_([^_]+)_([ ,;:.]+)_([^_]+)_', r'_\1\2\3_', t)
    return t


# ------------------------------------------------------------------ grafia
# forma de 1897 → forma de hoje (palavra inteira; em minúscula vale para qualquer caixa)
MANUAL = {
    # 1933 (Cartas de Anchieta)
    'deante': 'diante', 'adeante': 'adiante', 'deanteira': 'dianteira', 'deanteiras': 'dianteiras',
    'maximê': 'máxime', 'maximé': 'máxime', 'maximè': 'máxime', 'maxime': 'máxime', 'peor': 'pior', 'peores': 'piores',
    'assucar': 'açúcar', 'assucares': 'açúcares', 'polas': 'pelas', 'polo': 'pelo', 'polos': 'pelos',
    'deshonra': 'desonra', 'deshonrar': 'desonrar', 'deshonrado': 'desonrado', 'deshonrados': 'desonrados',
    'deshonesto': 'desonesto', 'deshonestos': 'desonestos', 'deshonesta': 'desonesta', 'deshonestas': 'desonestas',
    'deshumana': 'desumana', 'bemdito': 'bendito', 'bemdita': 'bendita', 'bemaventurado': 'bem-aventurado',
    'bemaventurados': 'bem-aventurados', 'bemaventurada': 'bem-aventurada', 'incançavel': 'incansável',
    'sinão': 'senão', 'soia': 'soía', 'soiam': 'soíam', 'soíam': 'soíam', 'catequismo': 'catecismo',
    'comecou': 'começou', 'comecaram': 'começaram', 'comecaram-se': 'começaram-se', 'comecado': 'começado',
    'comecariam': 'começariam', 'graca': 'graça', 'cabeca': 'cabeça', 'crianca': 'criança', 'justica': 'justiça',
    'espacosas': 'espaçosas', 'carecamos': 'careçamos', 'faco': 'faço', 'facam': 'façam', 'conhecas': 'conheças',
    'lourenco': 'lourenço', 'goncalo': 'gonçalo', 'goncalves': 'gonçalves', 'esperanca': 'esperança',
    'peconha': 'peçonha', 'conceicão': 'conceição', 'alcancado': 'alcançado', 'esforcavam': 'esforçavam',
    'rocarias': 'roçarias', 'lanca': 'lança', 'despedacar-lhe': 'despedaçar-lhe', 'alvorocados': 'alvoroçados',
    'adelgacar': 'adelgaçar', 'ameacas': 'ameaças', 'ameacando-nos': 'ameaçando-nos', 'tribu': 'tribo',
    'ete': 'etc', 'emfim': 'enfim', "n'agua": "n'água", 'nagua': "n'água", 'mangedoura': 'manjedoura',
    'mágua': 'mágoa', 'amen': 'amém', 'dezaseis': 'dezesseis', 'eramos': 'éramos', 'estrêmo': 'extremo',
    'foramos': 'fôramos', 'féros': 'feros', 'has': 'hás', 'intitula': 'intitula', 'agasta': 'agasta',
    'cameras': 'câmaras', 'cativara': 'cativara', 'crêm': 'creem', 'dêm': 'deem', 'mezinhas': 'mezinhas',
    'regimen': 'regime', 'saíram': 'saíram', 'subministra-se': 'subministra-se', 'destempera': 'destempera',
    'idéa': 'ideia', 'catecúmena': 'catecúmena', 'açoutado': 'açoitado', 'açoutes': 'açoites', 'açoute': 'açoite',
    'encarnicadamente': 'encarniçadamente', 'subtis': 'sutis', 'subtil': 'sutil', 'subtilissimas': 'sutilíssimas',
    'priguiça': 'preguiça', 'sententrião': 'setentrião', 'interveiu': 'interveio', 'emtanto': 'entanto',
    'medeante': 'mediante', 'exgotam': 'esgotam', 'exgotava': 'esgotava', 'exgotar-se': 'esgotar-se', 'exgota': 'esgota',
    'ceremonias': 'cerimônias', 'artilheria': 'artilharia', 'descança': 'descansa', 'descanço': 'descanso',
    'cançados': 'cansados', 'pretenções': 'pretensões', 'hervas': 'ervas', 'semrazões': 'sem-razões',
    'vespões': 'vespões', 'rechassa': 'rechaça', 'repilindo': 'repelindo', 'entremeiadas': 'entremeadas',
    'humidos': 'úmidos', 'distilam': 'destilam', 'creação': 'criação', 'creatura': 'criatura', 'creador': 'criador',
    'procreação': 'procriação', 'hidropico': 'hidrópico', 'subitanea': 'subitânea', 'afeiado': 'afeado',
    'hebrêa': 'hebreia', 'alternatim': 'alternatim', 'dous': 'dois', 'veiu': 'veio', 'Veiu': 'Veio',
    'senvergonha': 'sem-vergonha', 'encasado': 'encasado', 'tapiíra': 'tapiíra', 'rehú': 'rehú',
    'mamalucos': 'mamelucos', 'mamalucas': 'mamelucas', 'resava': 'rezava', 'resurreição': 'ressurreição',
    'magestade': 'majestade', 'satanaz': 'satanás', 'goiaz': 'goiás', 'altesa': 'alteza', 'praza': 'praza',
    'prazerá': 'prazerá', 'estacio': 'estácio', 'gran': 'grão', 'trisca': 'trisca', 'perenal': 'perenal',
    'acolheita': 'acolheita', 'asinha': 'asinha', 'vimes': 'vimes', 'sanie': 'sânie', 'catadura': 'catadura',
    # formas antigas de palavras atuais (Barata deixou algumas de propósito: giolho, antre, devação)
    'deos': 'deus', 'assi': 'assim', 'logar': 'lugar', 'logares': 'lugares', 'legoa': 'légua', 'legoas': 'léguas',
    'lingoa': 'língua', 'lingoas': 'línguas', 'agoa': 'água', "d'agoa": "d'água", 'céo': 'céu', 'ceo': 'céu',
    'giolhos': 'joelhos', 'giolho': 'joelho', 'devação': 'devoção', 'antre': 'entre', "d'antre": 'dentre',
    'testimunho': 'testemunho', 'testimunhos': 'testemunhos', 'testimunha': 'testemunha',
    'testimunhas': 'testemunhas', 'testimunhou': 'testemunhou', 'quasi': 'quase', 'comsigo': 'consigo',
    'bençam': 'bênção', 'signal': 'sinal', 'signaes': 'sinais', 'assignado': 'assinado',
    'edade': 'idade', 'edades': 'idades', 'outo': 'oito', 'outava': 'oitava', 'egual': 'igual', 'egreja': 'igreja',
    'egrejas': 'igrejas', 'imigos': 'inimigos', 'descançar': 'descansar', 'creador': 'criador',
    'creaturas': 'criaturas', 'creança': 'criança', 'creara': 'criara', 'magestade': 'majestade',
    'podesse': 'pudesse', 'podessem': 'pudessem', 'pozesse': 'pusesse', 'pozessem': 'pusessem',
    'pozeram': 'puseram', 'poz': 'pôs', 'poz-se': 'pôs-se', 'poude': 'pôde', 'podera': 'pudera',
    'passeiando': 'passeando', 'passeiado': 'passeado', 'passeiara': 'passeara', 'receiava': 'receava',
    'ceiar': 'cear', 'ceiando': 'ceando', 'ceiavam': 'ceavam', 'aprendeo': 'aprendeu', 'pedio': 'pediu',
    'felice': 'feliz', 'deshonestos': 'desonestos', 'deahi': 'daí', 'ahi': 'aí', 'dahi': 'daí', "d'ahi": 'daí',
    'emquanto': 'enquanto', 'reprehensão': 'repreensão', 'reprehendeu': 'repreendeu', 'geito': 'jeito',
    'calidade': 'qualidade', 'meudo': 'miúdo', 'meudamente': 'miudamente', 'peior': 'pior',
    'lençoes': 'lençóis', 'taboa': 'tábua', 'cartapacios': 'cartapácios', 'bemfeitor': 'benfeitor',
    'bemdita': 'bendita', 'redemptor': 'redentor', 'encubrira': 'encobrira', 'sembrante': 'semblante',
    'conjunccção': 'conjunção', 'apparacer': 'aparecer', 'signifiando': 'significando', 'eschola': 'escola',
    'devotissimo': 'devotíssimo', 'eucharistia': 'eucaristia', 'viatico': 'viático', 'cleresia': 'clerezia',
    'obrára': 'obrara', 'socegando': 'sossegando', 'alumear': 'alumiar', 'alumeada': 'alumiada',
    'alampada': 'lâmpada', 'alampadas': 'lâmpadas', 'hombro': 'ombro', 'hombros': 'ombros',
    'sobegidão': 'sobejidão', 'pola': 'pela', 'veiu': 'veio', 'fruita': 'fruta', 'páos': 'paus', 'páo': 'pau',
    'gráos': 'graus', 'náo': 'nau', 'náos': 'naus', 'máo': 'mau', 'máos': 'maus', 'maos': 'maus',
    'candea': 'candeia', 'candeas': 'candeias', 'aldea': 'aldeia', 'aldeas': 'aldeias', 'aldêa': 'aldeia',
    'mea': 'meia', 'xareo': 'xaréu', 'xaréos': 'xaréus', 'lagea': 'laje', 'bogio': 'bugio',
    'dozentas': 'duzentas', 'cincoenta': 'cinquenta', 'bolir': 'bulir', 'bolira': 'bulira',
    'homisiado': 'homiziado', 'coffo': 'cofo', 'cobrello': 'cobrelo', 'quartans': 'quartãs',
    'cossairos': 'corsários', 'veador': 'vedor', 'conclue': 'conclui', 'comtudo': 'contudo',
    'fermoso': 'formoso', 'melenconisado': 'melancolizado', 'melanconisada': 'melancolizada',
    'reteudo': 'retido', 'foão': 'fulano', 'fuão': 'fulano', 'foã': 'fulana', 'ascenção': 'ascensão',
    'mez': 'mês', 'teem': 'têm', 'sae': 'sai', 'poem': 'põem', 'dispo': 'dispo', 'dae': 'dai',
    'heide': 'hei de', 'hade': 'há de', 'vamonos': 'vamo-nos', 'foio': 'foi-o', 'partindoo': 'partindo-o',
    'trouxeas': 'trouxe-as', 'la': 'lá', 'doe': 'dói', 'va': 'vá', 'officio': 'ofício', 'asou': 'azou',
    'feros': 'feros', 'ingres': 'inglês', 'brasilica': 'brasílica', 'spirito': 'espírito',
    'tupinambas': 'tupinambás', 'iesus': 'jesus', 'porem': 'porém', 'logral-a-eis': 'lográ-la-eis', 'acunhae': 'acunhai', 'taparica': 'itaparica',
    # nomes de pessoas e de lugares na forma de hoje
    'estevam': 'estêvão', 'christovam': 'cristóvão', 'ignacio': 'inácio', 'luiz': 'luís', 'gram': 'grã',
    'magdalena': 'madalena', 'filippo': 'filipe', 'hespanha': 'espanha', 'castella': 'castela',
    'gouvêa': 'gouveia', 'gouvea': 'gouveia', 'loureto': 'loreto', 'ilheos': 'ilhéus', 'pirajaa': 'pirajá',
    'rochella': 'rochela', 'frandes': 'flandres', 'tanarife': 'tenerife', 'britioga': 'bertioga',
    'baia': 'bahia', 'avila': 'ávila',
    # ficam como estão
    'pera': 'para', 'per': 'por', 'té': 'até', 'dispensa': 'despensa', 'dispenseiro': 'despenseiro', 'vae-te': 'vai-te', 'frecha': 'flecha', 'chamar-se-á': 'chamar-se-á', 'vae-se': 'vai-se', 'saio': 'saiu', 'ayres': 'aires', 'victoria': 'vitória', 'bocca': 'boca', 'summa': 'suma', 'vae': 'vai', 'riba': 'riba', 'serrão': 'serrão', 'lacão': 'lacão', 'croncrenas': 'croncrenas', 'lissão': 'lissão', 'gasalhado': 'gasalhado',
}
# com a caixa exata (nomes com «d'»)
MANUAL_EXATO = {'Acosta': 'Acosta', 'Castela': 'Castela', 'Cay': 'Cay', "d'ouro": "d'ouro", 'Nha': 'Ilha', 'Ceu': 'Céu', 'Ha-os': 'Há-os', 'Florez': 'Flores', 'Itañae': 'Itañae', 'Aviz': 'Avis', 'Mem': 'Mem', 'Joannes': 'Joannes', "d'Arça": "d'Arça", "d'Amaral": "d'Amaral", "d'Azevedo": "d'Azevedo", "d'Azeredo": "d'Azeredo",
                "d'Avila": "d'Ávila", 'S.': 'S.', 'D.': 'D.', 'N': 'N'}

# «palavra|seguinte» → forma
CONTEXTO = {
}


def crase(t, seg, ant):
    """á, ás, áquele… de 1933: crase de hoje (relatorios/crase.tsv)."""
    base = {'á': 'à', 'ás': 'às', 'áquele': 'àquele', 'áquela': 'àquela', 'áqueles': 'àqueles',
            'áquelas': 'àquelas', 'áquilo': 'àquilo'}[t.lower()]
    return base[0].upper() + base[1:] if t[:1].isupper() else base


# palavras sem acento em 1897 que hoje têm duas formas (pratica × prática): a escolhida pelo contexto
AMBIG = {
    'alivio': 'alívio', 'animo': 'ânimo', 'arvore': 'árvore', 'arvores': 'árvores', 'beneficio': 'benefício',
    'capitulo': 'capítulo', 'contrario': 'contrário', 'credito': 'crédito', 'dialogo': 'diálogo',
    'diligencia': 'diligência', 'distancia': 'distância', 'experiencia': 'experiência', 'habito': 'hábito',
    'historia': 'história', 'hospede': 'hóspede', 'injurias': 'injúrias', 'interprete': 'intérprete',
    'medico': 'médico', 'musica': 'música', 'negocio': 'negócio', 'noticia': 'notícia', 'noticias': 'notícias',
    'penitencia': 'penitência', 'perpetua': 'perpétua', 'pratica': 'prática', 'praticas': 'práticas',
    'premio': 'prêmio', 'principio': 'princípio', 'privilegio': 'privilégio', 'prosperas': 'prósperas',
    'providencia': 'providência', 'publica': 'pública', 'publicas': 'públicas', 'publico': 'público',
    'reverencia': 'reverência', 'solicito': 'solícito', 'titulo': 'título', 'varias': 'várias',
    'espirito': 'espírito', 'antonio': 'antônio', 'continua': 'contínua', 'continuas': 'contínuas',
    'continuo': 'contínuo',
}


def desambiguar(t, ant, seg, formas):
    return AMBIG.get(t.lower(), t.lower())


def depois(s):
    return s.replace('Rio de janeiro', 'Rio de Janeiro')
