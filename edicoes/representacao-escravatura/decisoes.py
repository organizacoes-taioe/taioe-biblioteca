"""Decisões da grafia de hoje para a Representação (impresso de Paris, 1825)."""
HIFEN_FICA = set()
PRE = [
    # itálico do Wikisource, partido em duas linhas
    (r"''\s+''", ' '), (r"''(.+?)''", r'_\1_'),
    (r'ráō\b', 'rão'), (r'\bO I° é\b', 'O 1º é'), (r'°', 'º'),
    # palavras coladas no impresso (composição apertada)
    (r'\bAnossa\b', 'A nossa'), (r'\bAsociedade\b', 'A sociedade'), (r'\bOluxo\b', 'O luxo'), (r'\bAescrava\b', 'A escrava'),
    (r'\bAinnocencia\b', 'A inocência'), (r'\bAvós\b', 'A vós'), (r'\bEqual\b', 'E qual'),
    # pronome pendurado
    (r"\bdal-o\b", 'dá-lo'), (r"\brecomendal-o\b", 'recomendá-lo'), (r"\bcompral-os\b", 'comprá-los'), (r"\bvendel-os\b", 'vendê-los'),
    (r"\bestabelecel-os\b", 'estabelecê-los'), (r'\brecebela\b', 'recebê-la'), (r'\bfaze-los\b', 'fazê-los'), (r'\bconverte-los\b', 'convertê-los'),
    (r'\benriquece-lo\b', 'enriquecê-lo'), (r'\bsustenta-lo\b', 'sustentá-lo'), (r'\btrata-lo\b', 'tratá-lo'), (r'\bdeixa-lo\b', 'deixá-lo'),
    (r'\bconsultar-mos\b', 'consultarmos'), (r'\bLea-se\b', 'Leia-se'), (r'\bLeão-se\b', 'Leiam-se'),
    # locuções
    (r'\bEntre tanto\b', 'Entretanto'), (r'\ba pesar\b', 'apesar'), (r'\bse quer pagárão\b', 'sequer pagaram'), (r'\bcom nosco\b', 'conosco'), (r'\bse quer\b', 'sequer'), (r'\ba cima\b', 'acima'),
    (r'\bpor ventura\b', 'porventura'), (r'\boutro sim\b', 'outrossim'), (r'\b([Dd])e certo\b', r'\1ecerto'), (r'\bá cerca\b', 'acerca'), (r'\bapôz-si\b', 'após si'),
    (r'\bCon-cidadão\b', 'Concidadão'), (r'\bpseudos-estadistas\b', 'pseudoestadistas'), (r'\banti-sociaes\b', 'antissociais'),
    (r'\bEstados-Unidos\b', 'Estados Unidos'), (r"\bAzia-menor\b", 'Ásia Menor'), (r'\bCapitam mór\b', 'Capitão-mor'),
    (r"\bd'Africa\b", 'da África'), (r"\bd'Azia\b", 'da Ásia'), (r"\bd'America\b", 'da América'), (r"\bd'então\b", 'de então'), (r"\bd'aguia\b", 'de águia'),
    (r'\bcontinuarão e continuão\b', 'continuaram e continuam'), (r'\bpor por\b', 'por'),
    (r'\bE porque (os Brasileiros|continua)', r'E por que \1'), (r'\bporque o não serão\b', 'por que o não serão'), (r'\bé por que nos\b', 'é porque nos'),
    (r'\bVos sabeis\b', 'Vós sabeis'), (r'\bE vos, traficantes de carne humana, vos senhores\b', 'E vós, traficantes de carne humana, vós senhores'),
    (r'\bdois 3\b', 'dois 3.os'), (r'\bme empego\b', 'me emprego'), (r'\bouthr\b', 'outubro'), (r'outbr\. 1825', 'outubro de 1825'),
]
POS = [
    (r'\bá\b', 'à'), (r'\bás\b', 'às'), (r'\bÁ\b', 'À'), (r'\bÁs\b', 'Às'),
    # crase: o impresso põe «á» onde hoje não há crase, e o contrário
    (r'\bà (esta|favor|nosso|seus|brutos|uma|um|quem|mais de|render|obedecer|bem|valores)\b', r'a \1'),
    (r'\ba risca\b', 'à risca'), (r'\bas vezes\b', 'às vezes'), (r'\bassim a proporção\b', 'assim à proporção'), (r'\bpor a render\b', 'pôr a render'),
    # verbo no plural e «ver»
    (r'\bvêm homens\b', 'veem homens'), (r'\bse vêm precisados\b', 'se veem precisados'), (r'\bvem homens\b', 'veem homens'), (r'\bse vem precisados\b', 'se veem precisados'),
    (r'\bmas vem voluntariamente\b', 'mas vêm voluntariamente'), (r'experiência tem em mim', 'experiência têm em mim'),
    (r'\bfamílias não tem\b', 'famílias não têm'), (r'\beles não tem\b', 'eles não têm'), (r'do açúcar tem crescido', 'do açúcar têm crescido'),
    (r'\bque hoje não tem\b', 'que hoje não têm'), (r'\bque nada tem que\b', 'que nada têm que'), (r'\baqueles que tem\b', 'aqueles que têm'),
    (r'\bnão poder pagar\b', 'não puder pagar'), (r'\bcompõem em grande\b', 'compõe em grande'),
    (r'\bsabia política\b', 'sábia política'), (r'\bprovida, e sabia\b', 'provida, e sábia'),
    (r'ver-se-há', 'ver-se-á'), (r'Mordomia mor', 'Mordomia-Mor'), (r'da Razão e da Moral$', 'da Razão e da Moral.'),
    (r'« ', '«'), (r' »', '»'),
    (r'\( ', '('), (r' \)', ')'), (r' +\[(\d)\]', r'[\1]'),
    (r'(\d)os\b', r'\1.os'), (r'(\d)as\b', r'\1.as'),
]
EXATO = {}
M = {
 'he': 'é', 'hum': 'um', 'huma': 'uma', 'huns': 'uns', 'humas': 'umas', 'hun': 'um', 'huna': 'uma', 'nenuma': 'nenhuma',
 'ha': 'há', 'ja': 'já', 'paiz': 'país', 'pays': 'país', 'mez': 'mês', 'meza': 'mesa', 'dahi': 'daí', 'quasi': 'quase',
 'emfim': 'enfim', 'porisso': 'por isso', 'comsigo': 'consigo', 'nosco': 'nosco', 'deos': 'Deus', 'ceo': 'céu', 'ceos': 'céus',
 'assembléa': 'Assembleia', 'assemblea': 'Assembleia', 'epocha': 'época', 'europea': 'europeia', 'europeo': 'europeu', 'europeos': 'europeus',
 'hebreos': 'hebreus', 'hespanhoes': 'espanhóis', 'parocho': 'pároco', 'parochos': 'párocos', 'patriarcha': 'patriarca', 'habrahão': 'Abraão',
 'capitam': 'capitão', 'regulos': 'régulos', 'acquisição': 'aquisição', 'adquerido': 'adquirido', 'asphexia': 'asfixia', 'assucar': 'açúcar',
 'assumpto': 'assunto', 'augmenta': 'aumenta', 'augmentados': 'aumentados', 'augmentar': 'aumentar', 'augmentemos': 'aumentemos', 'augmento': 'aumento',
 'baratissimo': 'baratíssimo', 'chara': 'cara', 'chimica': 'química', 'conseguio': 'conseguiu', 'constitue': 'constitui', 'creados': 'criados',
 'creaturas': 'criaturas', 'creação': 'criação', 'descanço': 'descanso', 'destruio': 'destruiu', 'dexteridade': 'destreza', 'experencia': 'experiência',
 'humidade': 'umidade', 'ideas': 'ideias', 'immemorial': 'imemorial', 'impolitica': 'impolítica', 'machinas': 'máquinas', 'oxygeno': 'oxigênio',
 'pertende': 'pretende', 'pertendemos': 'pretendemos', 'peór': 'pior', 'podesse': 'pudesse', 'podessem': 'pudessem', 'prompto': 'pronto',
 'respiravel': 'respirável', 'similhante': 'semelhante', 'utencilios': 'utensílios', 'vehemente': 'veemente', 'intensoes': 'intenções',
 'poem': 'põe', 'compoem': 'compõem', 'roe': 'rói', 'róe': 'rói', 'máo': 'mau', 'arêa': 'areia', 'páe': 'pai', 'lle': 'lhe', 'saâ': 'sã', 'saã': 'sã',
 'officio': 'ofício', 'fosseis': 'fôsseis', 'fossemos': 'fôssemos', 'dezejára': 'desejara', 'serà': 'será', 'serviráõ': 'servirão', 'presidiráō': 'presidirão',
 # -ão = -am
 'advinhão': 'adivinham', 'agitão': 'agitam', 'amortizão': 'amortizam', 'apresentão': 'apresentam', 'attendão': 'atendam', 'bradão': 'bradam',
 'caracterisão': 'caracterizam', 'cativão': 'cativam', 'conheção': 'conheçam', 'considerão': 'consideram', 'continuão': 'continuam', 'convertão': 'convertam',
 'cultivão': 'cultivam', 'deixão': 'deixam', 'dilacérão': 'dilaceram', 'empunhão': 'empunham', 'entregão': 'entregam', 'erão': 'eram', 'escapão': 'escapam',
 'escudão': 'escudam', 'espremão': 'espremam', 'estavão': 'estavam', 'favorêção': 'favoreçam', 'fizerão': 'fizeram', 'formão': 'formam', 'forão': 'foram', 'fôrão': 'foram',
 'fundão': 'fundam', 'gritão': 'gritam', 'habilitavão': 'habilitavam', 'hájão': 'hajam', 'inoculão': 'inoculam', 'inutilizão': 'inutilizam', 'melhorão': 'melhoram',
 'mudão': 'mudam', 'necessitão': 'necessitam', 'oução': 'ouçam', 'podião': 'podiam', 'possão': 'possam', 'poupão': 'poupam', 'pullulão': 'pululam', 'queirão': 'queiram',
 'séjão': 'sejam', 'sayão': 'saiam', 'saião': 'saiam', 'tenhão': 'tenham', 'tinhão': 'tinham', 'trabalhão': 'trabalham', 'trovêjão': 'trovejam', 'venhão': 'venham',
 'subnegárão': 'subnegaram', 'aproveitarião': 'aproveitariam', 'estarião': 'estariam', 'ficarião': 'ficariam', 'morrião': 'morriam', 'poderião': 'poderiam',
 'pouparião': 'poupariam', 'serião': 'seriam', 'valerião': 'valeriam',
 'ella': 'ela', 'elle': 'ele', 'elles': 'eles', 'ellas': 'elas', 'porem': 'porém', 'copia': 'cópia', 'commercio': 'comércio', 'commercia': 'comercia',
 'trafico': 'tráfico', 'ultimas': 'últimas', 'ultimo': 'último', 'possivel': 'possível', 'experiencia': 'experiência', 'annos': 'anos', 'effeito': 'efeito',
 'providencia': 'providência', 'providencias': 'providências', 'dizimo': 'dízimo', 'paramos': 'páramos', 'páramos': 'páramos', 'premio': 'prêmio', 'vicio': 'vício', 'jubilo': 'júbilo',
 'titulo': 'título', 'numero': 'número', 'arvores': 'árvores', 'celebre': 'célebre', 'exercito': 'exército', 'perpetuo': 'perpétuo', 'publico': 'público',
 'publica': 'pública', 'publicas': 'públicas', 'domestica': 'doméstica', 'vitimas': 'vítimas', 'victimas': 'vítimas', 'contrario': 'contrário', 'arbitraria': 'arbitrária',
 'facto': 'fato', 'capitaes': 'capitais', 'mór': 'mor', 'dice': 'disse', 'haren': 'harém', 'cyrus': 'Ciro', 'nabucodonozor': 'Nabucodonosor', 'conchinchina': 'Cochinchina',
 'luis': 'Luís', 'wilberfoces': 'Wilberforces', 'say': 'Say', 'pensão': 'pensam', 'fação': 'façam', 'levantarão': 'levantaram', 'arruinarão': 'arruinaram',
 'cansarão': 'cansaram', 'cometterão': 'cometeram', 'mudarão': 'mudaram', 'sahirão': 'saíram', 'nascerão': 'nasceram', 'custarão': 'custaram', 'perderão': 'perderam',
 'huive': 'uive', 'mor': 'mor', 'levantárão': 'levantaram', 'arruinárão': 'arruinaram', 'nascêrão': 'nasceram', 'custárão': 'custaram', 'perdêrão': 'perderam', 'pagárão': 'pagaram', 'escrivadão': 'escravidão', 'summariameute': 'sumariamente', 'imagen': 'imagem', 'servicos': 'serviços', 'fôrros': 'forros', 'devastadôras': 'devastadoras', 'lea': 'leia',
}

# citações em francês: ficam como no impresso
FRANCES = r'_((?:Le mot|Toute cargaison|Congr)[^_]*)_'
