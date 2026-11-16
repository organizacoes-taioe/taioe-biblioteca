"""Cartas do Brasil (Nóbrega) — decisões de grafia e de leitura (ver montar.py).

Tudo na forma do impresso de 1886 (1886/<p>.txt). O que muda a leitura vai para a «Sobre esta edição»
(ERROS, OMITIDAS) ou para o revisao.json (as decisões do Gere).
"""

# palavra partida no fim da linha diante de «lhe», «se», «o»…: hífen de verdade quando a primeira parte é palavra
HIFEN_ANTES = set()
JUNTAR = set()          # juntar mesmo assim
ABREVIATURAS = {'s', 'd', 'n', 'lib', 'luc', 'cap', 'etc'}

# ------------------------------------------------------------------ antes da grafia (texto de 1886)
# As marcas de A. F. Barata, o copista de 1896 (a lição do manuscrito entre parênteses, «sic», a nota de
# rodapé), saem do texto e vão listadas na «Sobre esta edição» (OMITIDAS): (página, trecho, onde estava).
OMITIDAS = []

# erros evidentes do impresso de 1886, corrigidos: (página, de, para, comentário); vão na «Sobre»
ERROS = []
# erros miúdos de composição, corrigidos sem lista: (página, de, para)
COMPOSICAO = []

# leituras de Barata emendadas (decisões do Gere no revisao.json: o texto segue a recomendação)
EMENDAS = []

# abreviaturas e números (regex sobre o texto de 1886)
PRE = [
    (r'(?i)\s+(?:No\s)?\d{1,3}\s+N[oó]b?rega\s*[:.]+\s*Cartas', ''),    # cabeçalho corrente que ficou no meio do texto
    (r'(?i)\s*N[oó]b?rega\s*[:.]+\s*Cartas', ''),
    (r'&\s*c\.', '&c.'),
]

# linhas do fac-símile que são nota de rodapé de Valle Cabral que a detecção automática deixou passar: (página, de, até)
LINHAS_FORA = [(148, 34, 35), (157, 44, 44), (158, 1, 1), (108, 3, 6), (183, 42, 42)]

# trechos em latim: em itálico e sem mudança de grafia
LATIM = [
    'ego, Pater mi, in tanto positus igne charitatis non cremor',
    'sicut alioquin te audivi prophetantem',
    'compelle multas intrare naves et venire ad hanc quam plantat Dominus vineam suam',
    'Tu autem, Pater, ora pro omnibus et presertim pro filiis quos enutristi',
    'qui quœrant Jesum Christum solum crucifixum',
    'omnes quœrunt quæ sua sunt',
    'sed mitte, Pater, filios tuos in Domino nutritos fratres meos, ut in omnem hanc terram exeat sonus eorum',
    'quia patres eorum nuntiaverunt eis',
    'Mitte igitur operarios quia jam satis alba est messis',
    'Vale semper in Domino, mi Pater, et benedic nos omnes in Christo Jesu',
    'petentes panem et non est qui frangat eis',
    'quœrunt sua, sed quæ Jesu Christi',
    'ut quos dedisti non perdam ex eis quemquam',
    'Non solum nobis nati estis',
    'Valete, mi fratres',
    'commixti sunt inter gentes et didicerunt opera eorum',
    'Volumus Jesum videre',
    'Pater, quos dedisti mihi non perdidi',
    'Veniat, pater, veniat, si amat Jesum Christum',
    'sed tristitia nostra versa est in gaudium',
    'quia amo patrem meum, qui et ipse amat me',
    'hoc nomine et titulo',
    'quae sua sunt, non quae Jesus Christi',
    'pax, et non erat pax; curavimus Babilonem, et non est curata',
    'qui est benedictus in sœcula',
    'apposuit ut apprehenderentur alii malefactores',
    'in utroque homine',
    'in nomine Domini',
    'adquiess concilio ejus',
    'Sancti Spiritus',
    'Miserere mei Deus',
    'irruit spiritus Domini in eis',
    'quis mihi daret ut pro te morerer',
    'quid amplius de fratre nostro',
    'ignem et aquam',
    'et ne nos inducas in tentationem',
    'lumen ad revelationem gentium, et gloriam plebis tuæ',
    'defeceruntur præ lacrymis oculi mei, conturbata sunt viscera mea, effusum est in terra jecur meum',
    'qui venit quærere ovem quæ perierat',
    'et manducabat cum peccatoribus et publicanis',
    'et venit quærere et salvum facere quod perierat',
    'beati misericordes, quoniam ipsi misericordiam consequentur',
    'usque in finem dilexit eos',
    'potest unguentum istud venundari multo et dari pauperibus, non quia de egenis pertinebat ad eum, sed quia fur erat',
    'respicite, nationes hominum et scitote quia nullus sperabit in Domino et confusus est',
    'spera in Domino et fac bonitatem',
    'Venite hunc ignem mittere in terram et vultur accendatur',
    'mentita est iniquitas sibi',
    'ne redeat immundus spiritus cum aliis septem nequioribus se, et sint novissima pejora prioribus',
    'in lege naturæ',
    'scilicet',
    'Pater Noster',
]

# ------------------------------------------------------------------ grafia
# forma de 1886 → forma de hoje (palavra inteira; em minúscula vale para qualquer caixa)
MANUAL = {
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
MANUAL_EXATO = {"d'Arça": "d'Arça", "d'Amaral": "d'Amaral", "d'Azevedo": "d'Azevedo", "d'Azeredo": "d'Azeredo",
                "d'Avila": "d'Ávila", 'S.': 'S.', 'D.': 'D.', 'N': 'N'}

# «palavra|seguinte» → forma
CONTEXTO = {
    'maos|postas': 'mãos', 'Baia|do': 'baía', 'saia|um': 'saía', 'saia|de': 'saía', 'Baia|de': 'Baía', 'saia|da': 'saía', 'saiam|as': 'saíam',
    'saiam|verdadeiras': 'saíam', 'á|Deos': 'a', 'Á|todos': 'A', 'á|algum': 'a', 'á|sentença': 'a',
    'á|qualidade': 'a', 'á|pedra': 'a',
}

# ------------------------------------------------------------------ Nóbrega (1886): formas desta obra
MANUAL.update({
    'cousa': 'coisa', 'cousas': 'coisas', 'sinão': 'senão', 'dous': 'dois', 'ilhéos': 'ilhéus', 'charissimos': 'caríssimos',
    'charissimo': 'caríssimo', 'charissima': 'caríssima', 'charidade': 'caridade', 'charidades': 'caridades',
    'similhante': 'semelhante', 'similhantes': 'semelhantes', 'similhança': 'semelhança', 'deante': 'diante', 'adeante': 'adiante',
    'alembrará': 'lembrará', 'alembrar': 'lembrar', 'augmentar': 'aumentar', 'augmentada': 'aumentada', 'eguaes': 'iguais',
    'mandioqua': 'mandioca', 'inda': 'ainda', 'quaesquer': 'quaisquer', 'christianissimo': 'cristianíssimo',
    'junctamente': 'juntamente', 'junctas': 'juntas', 'ajunctou': 'juntou', 'ajunctamos': 'juntamos', 'ajunctava': 'juntava',
    'ajunctassem': 'juntassem', 'circumstancias': 'circunstâncias', 'açoute': 'açoite', 'fruito': 'fruto', 'hontem': 'ontem',
    'humida': 'úmida', 'hervas': 'ervas', 'ceremonias': 'cerimônias', 'dansas': 'danças', 'escumando': 'espumando',
    'escarneo': 'escárnio', 'bemaventurança': 'bem-aventurança', "est'outras": 'estoutras', 'contumaces': 'contumazes',
    'salvarse-ão': 'salvar-se-ão', 'crearem': 'criarem', 'crearam': 'criaram', 'crear': 'criar', 'creados': 'criados',
    'creatura': 'criatura', 'creou': 'criou', 'proluxa': 'prolixa', 'assignaturas': 'assinaturas', 'excusára': 'excusara',
    'fleugmatico': 'fleumático', 'reveredissimama': 'reverendíssima', 'fal-o-ha': 'fá-lo-á', 'deshonra': 'desonra',
    'deshonrados': 'desonrados', 'obrigavamo-nos': 'obrigávamo-nos', 'veiu-se': 'veio-se', 'veiu-lhes': 'veio-lhes',
    'piadoso': 'piedoso', 'presumpções': 'presunções', 'esperdiçar': 'desperdiçar', 'abrahão': 'abraão', 'bemdito': 'bendito',
    'assucar': 'açúcar', 'comtigo': 'contigo', 'desassocego': 'desassossego', 'desassocegados': 'desassossegados',
    'irmãosinho': 'irmãozinho', 'extranhar': 'estranhar', 'testimunhar': 'testemunhar', 'fazêl-os': 'fazê-los',
    'dilectissimos': 'diletíssimos', 'cadêa': 'cadeia', 'descommungados': 'descomungados', 'fedelidade': 'fidelidade',
    'sobreveiu': 'sobreveio', 'prompto': 'pronto', 'creanças': 'crianças', 'reprehender': 'repreender',
    'reprehendido': 'repreendido', 'inutilissimo': 'inutilíssimo', 'leixou': 'deixou', 'trensplantada': 'transplantada',
    'capaces': 'capazes', 'treslado': 'traslado', 'sartão': 'sertão', 'destrue': 'destrói', 'pernãobuco': 'pernambuco',
    'immundicia': 'imundícia', 'hectico': 'hético', 'imigo': 'inimigo', 'polas': 'pelas', 'diminue': 'diminui',
    'consinte': 'consente', 'magua': 'mágoa', 'poderam': 'puderam', 'generações': 'gerações', 'mamalucos': 'mamelucos',
    'cans': 'cãs', 'supito': 'súbito', 'villagalhão': 'vilagalhão', 'manchêa': 'manchea', 'acceptas': 'aceitas',
    'sera': 'será', 'fara': 'fará', 'eramos': 'éramos', 'thomaz': 'tomás', 'christovão': 'cristóvão', 'rezões': 'razões',
    'proveitos': 'proveitos', 'mai': 'mal', 'jorém': 'porém', 'hontem': 'ontem', 'tristesa': 'tristeza', 'dominga': 'domingo',
    'dextra': 'dextra', 'lã': 'lá', 'là': 'lá', 'cà': 'cá', 'ca': 'cá', 'hi': 'aí', 'des': 'des', 'cae': 'cai', 'cahe': 'cai', 'crêm': 'creem', 'dêm': 'deem', 'sahia': 'saía', 'entonces': 'entonces', 'scilicet': 'scilicet', 'omnibus': 'omnibus',
})


SEM_CRASE = {'um', 'uns', 'estes', 'esses', 'aqueles', 'aquelles', 'outros', 'todos', 'muitos', 'alguns', 'cada', 'quem', 'vossa', 'vossas', 'sua',
             'suas', 'deus', 'pouco', 'poucos', 'si', 'vós', 'nós', 'elles', 'eles', 'elle', 'ele', 'mim', 'nos', 'vos', 'mestre', 'padre',
             'padres', 'irmãos', 'ver', 'sertão', 'ella', 'ellas', 'tantos', 'quaesquer', 'quaisquer', 'qualquer', 'nenhum'}
FEM_OK = {'sua', 'suas'}          # «à sua casa» tem crase; «a Sua Alteza» (maiúscula) não
NAO_INF = {'mulher', 'amor', 'valor', 'favor', 'senhor', 'pior', 'melhor', 'maior', 'menor', 'calor', 'temor', 'fervor', 'clamor', 'dor', 'mar',
           'lugar', 'par', 'lar', 'altar', 'colher', 'prazer', 'poder', 'dever', 'viver', 'ser', 'parecer', 'ar', 'cear', 'tear', 'seguir',
           'servir', 'fazer', 'saber', 'haver'}


def crase(t, seg, ant):
    """á, à, ás, às, áquelle… de 1886: «a» simples (diante de infinitivo, de pronome de tratamento ou de palavra masculina)
    ou crase de hoje (a revisão olhou todas, relatorios/crase.tsv)."""
    lt = t.lower()
    sl = seg.lower().strip('.,;:!?')
    if lt in ('á', 'à'):
        if ant.lower() in ('em', 'de', 'por', 'com', 'sem', 'sobre', 'entre', 'até', 'desde', 'perante') and sl not in ('vossa', 'sua'):
            return 'A' if t[:1].isupper() else 'a'     # «em à terra» = «em a terra»
        inf = sl.endswith(('ar', 'er', 'ir', 'or')) and len(sl) > 3 and sl not in NAO_INF and not sl.endswith(('ador', 'edor', 'idor'))
        if sl in SEM_CRASE and not (sl in FEM_OK and not seg[:1].isupper()) or inf or (sl in ('vossa', 'sua', 'vossas') and seg[:1].isupper()):
            return 'A' if t[:1].isupper() else 'a'
        return 'À' if t[:1].isupper() else 'à'
    base = {'ás': 'às', 'às': 'às', 'áquelle': 'àquele', 'áquella': 'àquela', 'áquelles': 'àqueles',
            'áquellas': 'àquelas', 'áquillo': 'àquilo', 'àquelle': 'àquele', 'àquella': 'àquela', 'àquelles': 'àqueles',
            'àquellas': 'àquelas'}[lt]
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
    """Depois da grafia: chamadas de nota de rodapé de Valle Cabral («Negros 12)»), maiúscula solta, nomes."""
    import re
    s = re.sub(r'(?<=[A-Za-zÀ-ÿ.,;:!?])\s?\(?\d{1,3}\)', '', s)
    s = re.sub(r'\b(e|que|com|de|por|para|do|da|dos|das) (Os|As|O|A)(?= [a-zà-ÿ])', lambda m: m.group(1) + ' ' + m.group(2).lower(), s)
    s = s.replace('nô-las', 'no-las').replace('nô-lo', 'no-lo').replace('vô-lo', 'vo-lo')
    s = re.sub(r' {2,}', ' ', s)
    return s.replace('Rio de janeiro', 'Rio de Janeiro')
