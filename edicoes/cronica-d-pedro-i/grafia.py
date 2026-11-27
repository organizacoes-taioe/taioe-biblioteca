"""Crónica de D. Pedro I — tabelas de grafia (decisões à mão) para modernizar.py.

GRAFIA: forma de 1816 (minúscula) → forma de hoje. «=95»: a palavra de 1895 alinhada decide
(formas de duplo sentido). Palavras que não se usam mais ficam, na grafia de hoje, e vão para o
vocabulário (estonce, u, ca, pero, al, aazo, sazão…); formas antigas de palavras atuais passam à
forma atual (cousa → coisa, leixar → deixar, per → por, pera → para, assi → assim, ataa → até).
GRAFIA95: forma de 1895 (minúscula) → forma de hoje, onde o léxico não acerta sozinho.
"""

GRAFIA = {
    # preposições, advérbios, pronomes
    'per': 'por', 'pera': 'para', 'pora': 'para', 'el': 'ele', 'assi': 'assim', 'asi': 'assim', 'ataa': 'até',
    'aquel': 'aquele', 'aquell': 'aquele', 'aaquel': 'àquele', 'naquel': 'naquele', 'daquel': 'daquele',
    'todollos': 'todos os', 'todallas': 'todas as', 'todolos': 'todos os', 'todalas': 'todas as',
    'hi': 'aí', 'dhi': 'daí', 'poer': 'pôr', 'ante': 'antes', 'amte': 'antes', 'come': 'como',
    'antre': 'entre', 'amtre': 'entre', 'esto': 'isto', 'desto': 'disto', 'nesto': 'nisto', 'aquesto': 'isto',
    'ella': 'ela', 'ellas': 'elas', 'elle': 'ele', 'elles': 'eles', 'delle': 'dele', 'della': 'dela',
    'delles': 'deles', 'dellas': 'delas', 'nelle': 'nele', 'nella': 'nela', 'nelles': 'neles', 'nellas': 'nelas',
    'aquella': 'aquela', 'aquellas': 'aquelas', 'aquelles': 'aqueles', 'aquelle': 'aquele',
    'daquella': 'daquela', 'daquellas': 'daquelas', 'daquelles': 'daqueles', 'daquelle': 'daquele',
    'naquella': 'naquela', 'naquellas': 'naquelas', 'naquelles': 'naqueles',
    'estonçe': 'estonce', 'estomçe': 'estonce', 'estomce': 'estonce', 'estonce': 'estonce',
    'emtom': 'então', 'entom': 'então', 'emtam': 'então',
    'hu': 'u', 'dous': 'dois', 'duas': 'duas', 'quamto': 'quanto', 'quamta': 'quanta', 'quamtos': 'quantos',
    'quamtas': 'quantas', 'pollo': 'pelo', 'polla': 'pela', 'pollos': 'pelos', 'pollas': 'pelas',
    'sa': 'sua', 'sas': 'suas', 'mujto': 'muito', 'mujta': 'muita', 'mujtos': 'muitos', 'mujtas': 'muitas',
    'muj': 'mui', 'muy': 'mui', 'mui': 'mui',
    # contrações de «de» com vogal (1816 escreve junto, sem apóstrofo)
    'daragom': 'de Aragão', 'dalguuns': 'de alguns', 'dalguumas': 'de algumas', 'dalguuma': 'de alguma',
    'dalguum': 'de algum', 'dalgum': 'de algum', 'dalguns': 'de alguns', 'dalgumas': 'de algumas',
    'davis': 'de Avis', 'dhuum': 'de um', 'dhuuma': 'de uma', 'dhuma': 'de uma', "d'huuma": 'de uma',
    "d'huum": 'de um', 'doutra': 'de outra', 'doutras': 'de outras', 'doutro': 'de outro', 'doutros': 'de outros',
    'daver': 'de haver', 'dabril': 'de abril', 'dagosto': 'de agosto', 'doutubro': 'de outubro',
    'dandradre': 'de Andrade', 'devora': 'de Évora', 'dalboquerque': 'de Albuquerque', 'dalcobaça': 'de Alcobaça',
    # el-rei
    'elrei': 'el-rei', 'delrei': 'del-rei', 'aelrei': 'a el-rei', 'oelrei': 'o el-rei', 'dalrei': 'del-rei',
    # formas antigas de palavras atuais
    'cousa': 'coisa', 'cousas': 'coisas', 'leixou': 'deixou', 'leixar': 'deixar', 'leixasse': 'deixasse',
    'regno': 'reino', 'regnos': 'reinos', 'regnado': 'reinado', 'tragia': 'trazia', 'poinha': 'punha',
    'reposta': 'resposta', 'repostas': 'respostas', 'carrego': 'cargo', 'trautar': 'tratar',
    'inmijgos': 'inimigos', 'moesteiro': 'mosteiro', 'escripvam': 'escrivão', 'prougue': 'prouve',
    'prouguerom': 'prouveram', 'livras': 'libras', 'livra': 'libra', 'naaos': 'naus', 'boom': 'bom', 'boons': 'bons',
    'poboo': 'povo', 'poboos': 'povos', 'irmaao': 'irmão', 'irmaão': 'irmão', 'irmaaos': 'irmãos',
    'maão': 'mão', 'maaos': '=95', 'maao': '=95', 'razooens': 'razões', 'razoões': 'razões',
    'foromsse': 'foram-se', 'fezeo': 'fê-lo', 'açerca': 'acerca', 'ouro': 'ouro', 'moor': '=95',
    'se': '=95', 'dei': '=95', 'des': '=95', 'de': 'de', 'adeparte': 'à parte', 'aveo': 'adveio',
    'sazom': 'sazão', 'sazoões': 'sazões',
    # nomes
    'enes': 'Inês', 'diego': 'Diogo', 'alvoro': 'Álvaro', 'lixboa': 'Lisboa', 'graada': 'Granada',
    'anrrique': 'Henrique', 'hemrrique': 'Henrique', 'joham': 'João', 'samtiago': 'Santiago',
    'samtiaguo': 'Santiago', 'valhadolide': 'Valladolid', 'purtugal': 'Portugal', 'castella': 'Castela',
    'iffamte': 'infante', 'iffante': 'infante', 'iffamtes': 'infantes', 'iffantes': 'infantes',
    'dom': 'Dom', 'dona': '=95', 'hade': 'há de', 'ade': 'há de', 'ca': 'ca', 'ameude': 'amiúde',
    'galees': 'galés', 'gallees': 'galés', 'galee': 'galé', 'estevam': 'Estêvão', 'ia': '=95', 'fradarique': 'Fradique', 'fradrique': 'Fradique', 'arreal': 'arraial', 'arreai': 'arraial', 'annes': 'Anes', 'eanes': 'Eanes', 'çuja': 'suja', 'mocos': 'moços', 'lancou': 'lançou',
}

GRAFIA95 = {
    'elle': 'ele', 'elles': 'eles', 'ella': 'ela', 'ellas': 'elas', 'aquelle': 'aquele', 'aquelles': 'aqueles',
    'aquella': 'aquela', 'aquellas': 'aquelas', "d'elle": 'dele', "d'ella": 'dela', "d'elles": 'deles',
    "d'ellas": 'delas', 'castella': 'Castela', 'mez': 'mês', 'mezes': 'meses', 'galliza': 'Galiza',
    'ignez': 'Inês', 'tello': 'Telo', 'logar': 'lugar', 'logares': 'lugares', 'poude': 'pôde',
    'cincoenta': 'cinquenta', 'aviz': 'Avis', 'valhadolid': 'Valladolid', 'prompto': 'pronto',
    'adveiu': 'adveio', 'fel-o': 'fê-lo', 'fel-a': 'fê-la', 'mór': 'mor', 'oiro': 'ouro', 'd': 'Dom',
    'castelhanos': 'castelhanos', 'hespanha': 'Espanha', 'annos': 'anos', 'anno': 'ano', 'cavallo': 'cavalo',
    'cavallos': 'cavalos', 'maravedis': 'maravedis', 'chanceller': 'chanceler', 'commendadores': 'comendadores',
    'commendador': 'comendador', 'fallar': 'falar', 'geito': 'jeito', 'peior': 'pior', 'céo': 'céu',
    'magestade': 'majestade', 'podessem': 'pudessem', 'podesse': 'pudesse', 'emquanto': 'enquanto',
    'subditos': 'súditos', 'quaesquer': 'quaisquer', 'egual': 'igual', 'eguaes': 'iguais',
    'reprehendendo': 'repreendendo', 'reprehensão': 'repreensão', 'repartio': 'repartiu', 'civeis': 'cíveis',
    'dispender': 'despender', 'dispenderam': 'despenderam', 'dispendereis': 'despendereis', 'cubiça': 'cobiça',
    'cubiçoso': 'cobiçoso', 'calladamente': 'caladamente', 'annojava': 'anojava', 'annojado': 'anojado',
    'entremettendo': 'entremetendo', 'comsigo': 'consigo', 'dispenseiro': 'despenseiro', 'accorrimento': 'acorrimento',
    'accorros': 'acorros', 'supplicação': 'suplicação', 'ello': 'ello',
    'á': 'à', 'ás': 'às', 'áquella': 'àquela', 'áquelle': 'àquele', 'áquellas': 'àquelas', 'áquelles': 'àqueles',
    'poz': 'pôs', 'pôz': 'pôs', 'villa': 'vila', 'villas': 'vilas',
}
