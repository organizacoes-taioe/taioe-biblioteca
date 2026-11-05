"""Poesias Completas (1901): o texto de 1901/ (grafia do volume) passado à grafia de hoje em texto/.

    python3 edicoes/poesias-completas-machado/modernizar.py        (na raiz do repositório)

Palavra por palavra, nesta ordem: MANUAL (decisões, abaixo); regras (contrações com apóstrofo que têm forma de
hoje, ênclise «vêl-o» → «vê-lo», mesóclise «-ha» → «-á», «á» → «à», «-éo» → «-éu»); a forma já atual (no
léxico: /usr/share/dict/brazilian no Acordo de 1990 e os romances do Machado publicados na Biblioteca); o
dicionário de modernização do Wikisource (pt-BR, depois pt-PT, só se a forma estiver no léxico); a forma do léxico
de mesmo esqueleto (ph/f, y/i, th/t, consoantes dobradas, h mudo, ct/t, mm/m…). Ficam as formas que mudam o metro
ou que a língua ainda registra (inda, co'a, minh'alma, d'alma, té, p'ra); as formas antigas de palavra de hoje
passam à de hoje (cousa → coisa, dous → dois). Grava relatorios/grafia.tsv (cada troca, com a fonte) para
conferência; o que não achou par vai como SEM_PAR.
Os textos em outra língua (Un vieux pays, epígrafes estrangeiras, a citação de F. Denis) não se tocam.
"""
import glob, json, os, re, sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from edicao.grafia import ao1990, esqueleto, forma_atual, igualar_caixa, sem_acento  # noqa: E402

B = os.path.expanduser('~/.cache/claude-pedidos-0511/poesias-completas-machado')
TOK = re.compile(r"[^\W\d_]+(?:['’′\-][^\W\d_]+)*['’′]?|\d+|\s+|.", re.U)

# ------------------------------------------------------------------ decisões (conferidas)
MANUAL = {
    # nomes próprios: na forma das edições de hoje
    'Myrto': 'Mirto', 'Lysias': 'Lísias', 'LYSIAS': 'LÍSIAS', 'MYRTO': 'MIRTO', 'Cleon': 'Cléon', 'CLEON': 'CLÉON',
    'Corinna': 'Corina', 'Potyra': 'Potira', 'Tupan': 'Tupã', 'Jacy': 'Jaci', 'Coaracy': 'Coaraci',
    'Tamoyo': 'Tamoio', 'Tamoyos': 'Tamoios', 'tamoyo': 'tamoio', 'tamoya': 'tamoia', 'tamoyos': 'tamoios',
    'Guaycurú': 'Guaicuru', 'Guaycurús': 'Guaicurus', 'guaycurú': 'guaicuru', 'guaycurús': 'guaicurus',
    'Lindoya': 'Lindoia', 'Iguassú': 'Iguaçu', 'Affonso': 'Afonso', 'Paraguay': 'Paraguai',
    'Mickiewicz': 'Mickiewicz', 'Spinoza': 'Spinoza', 'Vischnu': 'Vixnu', 'Sappho': 'Safo', 'Anacreonte': 'Anacreonte',
    'Theos': 'Teos', 'Teos': 'Teos', 'Ephraim': 'Efraim', 'Issacar': 'Issacar', 'Achilles': 'Aquiles',
    'Isaias': 'Isaías', 'Eschylo': 'Ésquilo', 'Orestes': 'Orestes', 'Prometheu': 'Prometeu', 'Homero': 'Homero',
    'Juvenal': 'Juvenal', 'Catullo': 'Catulo', 'Tibullo': 'Tibulo', 'Propercio': 'Propércio', 'Lesbia': 'Lésbia',
    'Cynthia': 'Cíntia', 'Delia': 'Délia', 'Lydia': 'Lídia', 'Horacio': 'Horácio', 'Ovidio': 'Ovídio',
    'Petrarca': 'Petrarca', 'Rembrant': 'Rembrandt', 'Tasso': 'Tasso', 'Leonor': 'Leonor', 'Beatriz': 'Beatriz',
    'Catharina': 'Catarina', 'Clodia': 'Clódia', 'Celio': 'Célio', 'Cesar': 'César', 'Sabina': 'Sabina',
    'Octavio': 'Otávio', 'Ithaque': "Ithaque", 'Judith': 'Judith', 'Walter': 'Walter',
    'Tchê-Tsi': 'Tchê-Tsi', 'Thu-Fu': 'Thu-Fu', 'Han-Tiê': 'Han-Tiê', 'Tan-Jo-Lu': 'Tan-Jo-Lu',
    'Tchan-Tiú-Lin': 'Tchan-Tiú-Lin', 'Tin-Tun-Sing': 'Tin-Tun-Sing', 'Su-Tchon': 'Su-Tchon',
    'Simão': 'Simão', 'Vasconcellos': 'Vasconcelos', 'Laynez': 'Laínez', 'Marcgraff': 'Marcgraf',
    'Ayres': 'Aires', 'Escragnolle': 'Escragnolle', 'Taunay': 'Taunay', 'Baptista': 'Batista',
    'Japorá': 'Japorá', 'Lapagata': 'Lapagata', 'Capitãosinho': 'Capitãozinho', 'Matto-Grosso': 'Mato Grosso',
    'Yppané': 'Ipané', 'Cayavaba': 'Caiavaba', 'Panenioxe': 'Panenioxe', 'Nanine': 'Nanine', 'Niani': 'Niani',
    'Rebecca': 'Rebeca', 'Gurgel': 'Gurgel', 'Hespanha': 'Espanha', 'hespanhóes': 'espanhóis', 'hespanhol': 'espanhol',
    'Monterroyo': 'Monterroio', 'Montaigne': 'Montaigne', 'Cupuaba': 'Cupuaba', 'Oitipó-cupuaaba': 'Oitipó-cupuaaba',
    'Anhangá': 'Anhangá', 'Jaciuca': 'Jaciuca', 'Içayba': 'Içaíba', 'Tatupeba': 'Tatupeba', 'Tymbiras': 'Timbiras',
    'Mustre': 'Mustre', 'Alvarenga': 'Alvarenga', 'Moema': 'Moema', 'Orizes': 'Orizes', 'Orises': 'Orizes',
    'Phalenas': 'Falenas', 'Chrysalidas': 'Crisálidas', 'Occidentaes': 'Ocidentais', 'Americanas': 'Americanas',
    'Demophilo': 'Demófilo', 'Heitor': 'Heitor', 'Elvira': 'Elvira', 'Ulysses': 'Ulisses',
    # acento ou forma que o léxico não decide
    'ha': 'há', 'Ha': 'Há', 'paiz': 'país', 'paizes': 'países', 'raiz': 'raiz', 'raizes': 'raízes',
    'comtigo': 'contigo', 'comtudo': 'contudo', 'emfim': 'enfim', 'Emfim': 'Enfim', 'Comtudo': 'Contudo',
    'emtanto': 'entanto', 'comvosco': 'convosco', 'comnosco': 'conosco', 'commigo': 'comigo', 'comsigo': 'consigo',
    'mãi': 'mãe', 'mãis': 'mães', 'idéa': 'ideia', 'idéas': 'ideias', 'idéal': 'ideal', 'extranho': 'estranho',
    'extranha': 'estranha', 'extranhos': 'estranhos', 'extranhas': 'estranhas', 'explendor': 'esplendor',
    'explendores': 'esplendores', 'fructo': 'fruto', 'fructos': 'frutos', 'vae': 'vai', 'Vae': 'Vai', 'cae': 'cai',
    'sae': 'sai', 'Sae': 'Sai', 'ella': 'ela', 'Ella': 'Ela', 'ellas': 'elas', 'elle': 'ele', 'Elle': 'Ele', 'elles': 'eles',
    'Elles': 'Eles', 'aquelle': 'aquele', 'Aquelle': 'Aquele', 'aquella': 'aquela', 'Aquella': 'Aquela',
    'aquelles': 'aqueles', 'aquellas': 'aquelas', 'Aquelles': 'Aqueles', 'Aquellas': 'Aquelas',
    'della': 'dela', 'dellas': 'delas', 'delle': 'dele', 'delles': 'deles', 'nella': 'nela', 'nelle': 'nele',
    'daquelle': 'daquele', 'daquella': 'daquela', 'naquelle': 'naquele', 'naquella': 'naquela',
    'Daquellas': 'Daquelas', 'Naquelle': 'Naquele', 'daquelles': 'daqueles', 'naquellas': 'naquelas',
    'oiro': 'ouro', 'socegado': 'sossegado', 'socego': 'sossego', 'socegada': 'sossegada', 'cançado': 'cansado',
    'cançada': 'cansada', 'cançaço': 'cansaço', 'cansaço': 'cansaço', 'deos': 'deus', 'Deos': 'Deus', 'deoses': 'deuses',
    'heroe': 'herói', 'heroes': 'heróis', 'Heroe': 'Herói', 'heroina': 'heroína', 'christans': 'cristãs',
    'ancian': 'anciã', 'ancians': 'anciãs', 'irman': 'irmã', 'irmans': 'irmãs', 'manhan': 'manhã', 'lan': 'lã',
    'sinhá': 'sinhá', 'Sinhá': 'Sinhá', 'tambem': 'também', 'Tambem': 'Também', 'porém': 'porém', 'alguem': 'alguém',
    'ninguem': 'ninguém', 'Ninguem': 'Ninguém', 'além': 'além', 'aquem': 'aquém', 'tem': 'tem', 'teem': 'têm',
    'vêem': 'veem', 'lêem': 'leem', 'crêem': 'creem', 'dêem': 'deem', 'hontem': 'ontem', 'hoje': 'hoje',
    'egreja': 'igreja', 'egrejas': 'igrejas', 'pêjo': 'pejo', 'enôjo': 'enojo', 'côro': 'coro', 'sôbre': 'sobre',
    'gôsto': 'gosto', 'êsse': 'esse', 'êste': 'este', 'pôde': 'pôde', 'póde': 'pode', 'pódes': 'podes',
    'pódem': 'podem', 'apprende': 'aprende', 'jámais': 'jamais', 'jamais': 'jamais', 'Já': 'Já',
    'quasi': 'quase', 'Quasi': 'Quase', 'atravez': 'através', 'através': 'através', 'emquanto': 'enquanto',
    'Emquanto': 'Enquanto', 'ámanhã': 'amanhã', 'Hade': 'Há de', 'hade': 'há de', 'heide': 'hei de',
    'hão': 'hão', 'trez': 'três', 'tres': 'três', 'Tres': 'Três', 'mez': 'mês', 'mezes': 'meses', 'portuguez': 'português',
    'portuguezes': 'portugueses', 'francez': 'francês', 'francezes': 'franceses', 'inglez': 'inglês',
    'chineza': 'chinesa', 'princeza': 'princesa', 'princezas': 'princesas', 'cortezã': 'cortesã', 'Theresa': 'Teresa',
    'mysterio': 'mistério', 'mysterios': 'mistérios', 'mysteriosa': 'misteriosa', 'mysterioso': 'misterioso',
    'paraiso': 'paraíso', 'juizo': 'juízo', 'saudade': 'saudade', 'ruina': 'ruína', 'ruinas': 'ruínas',
    'Ruinas': 'Ruínas', 'egoismo': 'egoísmo', 'Egoismo': 'Egoísmo', 'heroismo': 'heroísmo', 'atheu': 'ateu',
    'europêa': 'europeia', 'idêa': 'ideia', 'assembléa': 'assembleia', 'colméa': 'colmeia', 'aldêa': 'aldeia',
    'aldêas': 'aldeias', 'odysséa': 'odisseia', 'epopéa': 'epopeia', 'Galiléa': 'Galileia', 'Judéa': 'Judeia',
    'cheiroso': 'cheiroso', 'benção': 'bênção', 'Benção': 'Bênção', 'orgam': 'órgão', 'orgão': 'órgão',
    'orphão': 'órfão', 'orphã': 'órfã', 'sertões': 'sertões', 'vagalume': 'vaga-lume', 'vaga-lume': 'vaga-lume',
    'Tupan': 'Tupã', 'cauim': 'cauim', 'pocema': 'pocema', 'mussurana': 'muçurana', 'tangapema': 'tangapema',
    'kanitar': 'canitar', 'Guanamby': 'Guanambi', 'Anagê': 'Anajê', 'bocayuva': 'bocaiuva', 'bocayuvas': 'bocaiuvas',
    'embiroçu': 'embiroçu', 'embiroçú': 'embiroçu', 'Embiroçu': 'Embiroçu', 'jurity': 'juriti', 'maracá': 'maracá',
    'goso': 'gozo', 'gosos': 'gozos', 'gosar': 'gozar', 'gosa': 'goza', 'gosam': 'gozam', 'deslisas': 'deslizas',
    'deslisa': 'desliza', 'horisonte': 'horizonte', 'horisontes': 'horizontes', 'horisonte.': 'horizonte',
    'brazileiro': 'brasileiro', 'brasileiro': 'brasileiro', 'Brazil': 'Brasil', 'brasilica': 'brasílica',
    'familiarisado': 'familiarizado', 'baptisassem': 'batizassem', 'baptismo': 'batismo', 'baptista': 'batista',
    'quiz': 'quis', 'quizeres': 'quiseres', 'quizera': 'quisera', 'Quizera': 'Quisera', 'puz': 'pus', 'compuz': 'compus',
    'fiz': 'fiz', 'diz': 'diz', 'sizo': 'siso', 'pezares': 'pesares', 'pezar': 'pesar', 'pezava': 'pesava',
    'maguas': 'mágoas', 'magua': 'mágoa', 'agoas': 'águas', 'egual': 'igual', 'eguaes': 'iguais',
    'rubim': 'rubim', 'bambús': 'bambus', 'cajús': 'cajus', 'tribu': 'tribo', 'tribus': 'tribos',
    'anciões': 'anciões', 'cahos': 'caos', 'Chãos': 'Caos', 'iris': 'íris', 'oásis': 'oásis', 'ether': 'éter',
    'ethereo': 'etéreo', 'etherea': 'etérea', 'lagryma': 'lágrima', 'lagrymas': 'lágrimas', 'nympha': 'ninfa',
    'nymphas': 'ninfas', 'sylpho': 'silfo', 'mirtho': 'mirto', 'myrtho': 'mirto', 'myrthos': 'mirtos',
    'phrase': 'frase', 'theatro': 'teatro', 'rhythmo': 'ritmo', 'hymeneu': 'himeneu', 'Hymenêo': 'Himeneu',
    'Hymeneo': 'Himeneu', 'hymenêo': 'himeneu', 'Pœan': 'Peã', 'Poean': 'Peã', 'Io': 'Io',
    'Elviva': 'Elvira', 'hermonia': 'hemônia', 'sestereios': 'sestércios', 'Tenodos': 'Tênedos', 'Cyntia': 'Cíntia',
    'AiTeições': 'Afeições', 'aífronta': 'afronta', 'ellesvou': 'eles vou', 'Qnando': 'Quando', 'symlolica': 'simbólica',
    'tereeiro': 'terceiro', 'aspennas': 'as penas', 'lllusões': 'ilusões', 'Soleninissima': 'Soleníssima',
    'Tamojo': 'Tamoio', 'Niâni': 'Niani',
    'receiosa': 'receosa', 'ponteagudas': 'pontiagudas', 'legoas': 'léguas', 'mingoa': 'míngua', 'Perdeirei': 'Perderei',
    'palíido': 'pálido', 'complice': 'cúmplice', 'complices': 'cúmplices', 'aborigenes': 'aborígenes',
    'cubiçosos': 'cobiçosos', 'cubiçosa': 'cobiçosa', 'cubrira': 'cobrira', 'glotão': 'glutão', 'invillecida': 'envilecida',
    'vecejam': 'vicejam', 'vecejante': 'vicejante', 'vecejantes': 'vicejantes', 'ferio': 'feriu', 'ouvio': 'ouviu',
    'Ouvio': 'Ouviu', 'presentio': 'pressentiu', 'Vivireis': 'Vivereis', 'vivireis': 'vivereis', 'Trepido': 'Trépido',
    'angelicaes': 'angelicais', 'humbraes': 'umbrais', 'umbraes': 'umbrais', 'infernaes': 'infernais', 'matinaes': 'matinais',
    'mortaes': 'mortais', 'portaes': 'portais', 'usuaes': 'usuais', 'estaes': 'estais', 'levaes': 'levais', 'Voaes': 'Voais',
    'Empunhae': 'Empunhai', 'suspirae': 'suspirai', 'descae': 'descai', 'esvae': 'esvai', 'extrahe': 'extrai',
    'destróe': 'destrói', 'dilue': 'dilui', 'exclue': 'exclui', 'restitue': 'restitui', 'Restitue': 'Restitui',
    'attribue': 'atribui', 'distilla': 'destila', 'créador': 'criador', 'meneiando': 'meneando', 'maguada': 'magoada',
    'Maguados': 'Magoados', 'escarneos': 'escárnios', 'commuuns': 'comuns', 'alardeam': 'alardeiam', 'ameigava': 'ameigava',
    'melancholica': 'melancólica', 'Melancholica': 'Melancólica', 'melancholia': 'melancolia', 'Melancholicamente': 'Melancolicamente',
    'melancholico': 'melancólico', 'Melancholico': 'Melancólico', 'Impeto': 'Ímpeto', 'impeto': 'ímpeto',
    'cahe': 'cai', 'Cahe': 'Cai', 'admissivel': 'admissível', 'asperrimos': 'aspérrimos', 'magoadissimos': 'magoadíssimos',
    'ternissimos': 'ternissimos', 'balsamos': 'bálsamos', 'billião': 'bilião', 'bithynio': 'bitínio', 'callosa': 'calosa',
    'capello': 'capelo', 'cancellos': 'cancelos', 'celicos': 'célicos', 'chylo': 'quilo', 'clepsydra': 'clepsidra',
    'Clytemnestra': 'Clitemnestra', 'Egistho': 'Egisto', 'enluctar': 'enlutar', 'enluctou': 'enlutou', 'ennoitecer': 'enoitecer',
    'equoreo': 'equóreo', 'espumeo': 'espúmeo', 'eolia': 'eólia', 'Egeo': 'Egeu', 'fertiles': 'férteis', 'funeraes': 'funerais',
    'gyneceo': 'gineceu', 'gynecêo': 'gineceu', 'Hymmeto': 'Himeto', 'impolluto': 'impoluto', 'polluto': 'poluto', 'polluira': 'poluíra',
    'innocentinha': 'inocentinha', 'luctuosa': 'lutuosa', 'Luctuosas': 'Lutuosas', 'luctuoso': 'lutuoso', 'luctuosos': 'lutuosos',
    'lybicos': 'líbicos', 'Lyeo': 'Lieu', 'Lysicles': 'Lísicles', 'mussuranna': 'muçurana', 'nayade': 'náiade', 'nayras': 'naires',
    'nenia': 'nênia', 'nivea': 'nívea', 'niveos': 'níveos', 'nuncia': 'núncia', 'pavido': 'pávido', 'psalmo': 'salmo',
    'psalterio': 'saltério', 'rabido': 'rábido', 'sepulchraes': 'sepulcrais', 'sepulchral': 'sepulcral', 'senhoriaes': 'senhoriais',
    'salgueiraes': 'salgueirais', 'soffreando': 'sofreando', 'spectro': 'espectro', 'sphynge': 'esfinge', 'strophe': 'estrofe',
    'succuriuba': 'sucuriúba', 'thuribulo': 'turíbulo', 'triumphaes': 'triunfais', 'troyanas': 'troianas', 'turgido': 'túrgido',
    'umbella': 'umbela', 'virgineo': 'virgíneo', 'zephyros': 'zéfiros', 'voluveis': 'volúveis', 'volupias': 'volúpias',
    'Arethusa': 'Aretusa', 'Amathonte': 'Amatonte', 'alcyone': 'alcíone', 'alcyones': 'alcíones', 'Lethes': 'Letes',
    'Philinto': 'Filinto', 'Philomela': 'Filomela', 'photographicamente': 'fotograficamente', 'Protheo': 'Proteu',
    'Thessalia': 'Tessália', 'Ruth': 'Rute', 'Ybake': 'Ibaque', 'Ibake': 'Ibaque', 'Nahum': 'Naum', 'Cayavabá': 'Caiavabá',
    'guayanaz': 'guaianás', 'Guanumby': 'Guanambi', 'guanumby': 'guanambi', 'Parthenis': 'Partênis', 'Stella': 'Stella',
    'Sabello': 'Sabelo', 'Puccio': 'Puccio', 'phalenas': 'falenas', 'Gaville': 'Gaville', 'Duclere': 'Duclerc',
    'Tajassú': 'Tajaçu', 'tajassús': 'tajaçus', 'japú': 'japu', 'aruspice': 'arúspice', 'Aulicos': 'Áulicos',
    'Ciceronica': 'Ciceroniana', 'Cassange': 'Cassange', 'iriado': 'iriado', 'pagé': 'pajé', 'pagés': 'pajés',
    'Pœstum': 'Pesto', 'Scamandro': 'Escamandro', 'Sciancato': 'Sciancato', 'agra': 'agra', 'perduravel': 'perdurável',
    'Revivirião': 'Reviviriam', 'Pallejou': 'Palejou', 'Romeos': 'Romeus', 'Lenora': 'Lenora', 'cherubim': 'querubim',
    'prantêe': 'pranteie', 'affouta': 'afoita', 'affouto': 'afoito', 'almanach': 'almanaque', 'archiduqueza': 'arquiduquesa',
    'azues': 'azuis', 'Azues': 'Azuis', 'bemvinda': 'bem-vinda', 'Chapeo': 'Chapéu', 'Chimera': 'Quimera', 'chimera': 'quimera',
    'chimeras': 'quimeras', 'Chr': 'Chr', 'craneo': 'crânio', 'creada': 'criada', 'creado': 'criado', 'Creador': 'Criador',
    'creador': 'criador', 'creadora': 'criadora', 'creança': 'criança', 'creanças': 'crianças', 'creatura': 'criatura',
    'creaturas': 'criaturas', 'creação': 'criação', 'Creação': 'Criação', 'Doirado': 'Dourado', 'doirado': 'dourado',
    'egualmente': 'igualmente', 'fouce': 'foice', 'Heróe': 'Herói', 'heróe': 'herói', 'influe': 'influi', 'lampeão': 'lampião',
    'logar': 'lugar', 'orchestra': 'orquestra', 'peior': 'pior', 'peor': 'pior', 'possue': 'possui', 'pozeram': 'puseram',
    'sorpresa': 'surpresa', 'taboa': 'tábua', 'veiu': 'veio', 'Veiu': 'Veio', 'reconnaît': 'reconnaît', 'Ulysse': 'Ulysse',
    'Lisias': 'Lísias', 'LISIAS': 'LÍSIAS', 'cabedaes': 'cabedais', 'fataes': 'fatais', 'finaes': 'finais', 'vio': 'viu', 'Vio': 'Viu', 'Sentio': 'Sentiu', 'conseguio': 'conseguiu', 'abrio': 'abriu',
    'fugio': 'fugiu', 'surgio': 'surgiu', 'erão': 'eram', 'ião': 'iam', 'edade': 'idade', 'delia': 'dela', 'Neila': 'Nela',
    'Elie': 'Ele', 'leidos': 'lépidos', "mimh'alma": "minh'alma", 'ceo': 'céu', 'XLTX': 'XLIX',
    'abraza': 'abrasa', 'Abrazada': 'Abrasada', 'abrazava': 'abrasava', 'Agnel': 'Agnel', 'ahi': 'aí', 'Ahi': 'Aí',
    'aldea': 'aldeia', 'analyses': 'análises', 'ancias': 'ânsias', 'antaño': 'antaño', 'apostrophe': 'apóstrofe',
    'arêa': 'areia', 'arêas': 'areias', 'ARTHUR': 'ARTUR', 'BB': 'BB', 'DD': 'DD', 'NN': 'NN', 'AA': 'AA', 'CC': 'CC',
    'cant': 'cant', 'Cant': 'Cant', 'Amaz': 'Amaz', 'Math': 'Math', 'Thes': 'Tes', 'cazavam': 'casavam',
    'cerviz': 'cerviz', 'ceu': 'céu', 'Ceu': 'Céu', 'ceus': 'céus', 'esfolha': 'esfolha', 'Esfolhadas': 'Esfolhadas',
    'Estacio': 'Estácio', 'fallaz': 'falaz', 'franças': 'franças', 'frisões': 'frisões', 'hay': 'hay', 'Pallas': 'Palas',
    'pe': 'pé', 'pes': 'pés', 'presagio': 'presságio', 'po': 'pó', 'Poz': 'Pôs', 'poz': 'pôs', 'Pollião': 'Polião',
    'roe': 'rói', 'rudez': 'rudez', 'liça': 'liça', 'sabiá': 'sabiá', 'Sabiá': 'Sabiá', 'Páris': 'Páris',
    'seducção': 'sedução', 'semêa': 'semeia', 'sera': 'será', 'Sera': 'Será', 'seras': 'serás', 'tera': 'terá',
    'serros': 'serros', 'Sibille': 'Sibile', 'supplicio': 'suplício', 'thalamo': 'tálamo', 'trillos': 'trilos',
    'Visio': 'Visio', 'viçam': 'viçam', 'â': 'à', 'recende': 'recende', 'rescende': 'recende', 'rescendente': 'recendente',
    'has': 'hás', 'Has': 'Hás', 'es': 'és', 'vas': 'vais', 'vás': 'vais', 'Vás': 'Vais', 'pays': 'país',
    'hardido': 'ardido', 'Haveras': 'Haverás', 'sa': 'sã', 'dissereis': 'disséreis', 'Eden': 'Éden', 'Felicio': 'Felício',
    'Elysio': 'Elísio', 'Pericles': 'Péricles', 'Moyses': 'Moisés', 'Nictheroy': 'Niterói', 'Corintho': 'Corinto',
    'vello': 'velo', 'liteira': 'liteira', 'hostes': 'hostes', 'torva': 'torva', 'Torva': 'Torva', 'torvos': 'torvos',
    'ermas': 'ermas', 'ledas': 'ledas', 'fuscas': 'fuscas', 'centos': 'centos', 'cotias': 'cutias', 'Cresta': 'Cresta',
    'descora': 'descora', 'empos': 'empós', 'Camenas': 'Camenas', 'aromados': 'aromados', 'arrulha': 'arrulha',
    'arrulho': 'arrulho', 'abelhitas': 'abelhitas', 'peava': 'peava', 'Remador': 'Remador', 'Vesta': 'Vesta',
    'approuve': 'approuve', 'pensées': 'pensées', 'rives': 'rives', 'soupire': 'soupire', 'sur': 'sur', 'escruto': 'escruto',
    'Fil': 'Fil', 'Elie': 'Elie', 'Neila': 'Neila', 'invio': 'ínvio', 'páreas': 'páreas', 'poleá': 'poleá',
    'pascia': 'pascia', 'leidos': 'leidos', 'ideial': 'ideal', 'Paulos': 'Paulos', 'consomem': 'consomem', 'encendido': 'encendido', 'cholera': 'cólera', 'consolatrix': 'consolatrix',
    'sr': 'sr', 'Sr': 'Sr', 'Sra': 'Sra', 'Dr': 'Dr', 'S': 'S',
}
# palavras que ficam (formas do autor que a língua registra, ou que mudam o metro)
FICAM = {'inda', 'té', "co'a", "co'as", "co'o", "co'os", "minh'alma", "d'alma", "d'agua", "d'água", "p'ra",
         "tu'alma", "d'oiro", "d'ouro", 'mui', 'assaz', 'hi', 'despareceu', 'desparecêra', 'entregalh', 'esquivo',
         'n', 'd', 'lh', 'm'}
# contrações com apóstrofo que têm forma de hoje
JUNTAR = {"n'um": 'num', "n'uma": 'numa', "n'uns": 'nuns', "n'umas": 'numas', "d'ella": 'dela', "d'ellas": 'delas',
          "d'elle": 'dele', "d'elles": 'deles', "n'ella": 'nela', "n'elle": 'nele', "n'ellas": 'nelas', "n'elles": 'neles',
          "d'aquelle": 'daquele', "d'aquella": 'daquela', "d'aquelles": 'daqueles', "d'aquellas": 'daquelas',
          "outr'ora": 'outrora', "n'esta": 'nesta', "n'este": 'neste', "n'essa": 'nessa', "n'esse": 'nesse',
          "n'estas": 'nestas', "n'estes": 'nestes', "n'essas": 'nessas', "n'esses": 'nesses', "d'esta": 'desta',
          "d'este": 'deste', "d'essa": 'dessa', "d'esse": 'desse', "d'estes": 'destes', "d'estas": 'destas',
          "d'esses": 'desses', "d'essas": 'dessas', "d'entre": 'dentre', "n'aquelle": 'naquele', "n'aquella": 'naquela',
          "d'antes": 'dantes', "d'outro": 'doutro', "d'outra": 'doutra', "n'outro": 'noutro', "n'outra": 'noutra',
          "d'aqui": 'daqui', "d'ali": 'dali', "d'alli": 'dali', "d'onde": 'donde', "d'isso": 'disso', "d'isto": 'disto',
          "n'isso": 'nisso', "n'isto": 'nisto', "d'olhos": 'de olhos', "d'ebano": 'de ébano', "d'agua": "d'água",
          "d'ahi": 'daí', "lh'o": 'lho', "lh'a": 'lha', "lh'os": 'lhos', "lh'as": 'lhas', "d'amor": 'de amor',
          "d'arte": 'de arte', "d'ouro": 'de ouro', "n'agua": "n'água", "d'um": 'de um', "d'uma": 'de uma'}
ESTRANGEIRO = {'un-vieux-pays'}   # o poema inteiro
# cabeçalhos em outra língua (as epígrafes de Musset, Shakespeare, Garção é português…)
EPIGRAFES_FORA = ("Oh! la fleur", "She speaks", "No hay", "Je veux", "Ulysse", "Tacendo", "... che piagne", "... juntamente")

_LEX = None
_IDX = None
_WS = None


def lexico():
    global _LEX, _IDX
    if _LEX is None:
        lex = set()
        for w in open('/usr/share/dict/brazilian', encoding='utf-8'):
            w = w.strip()
            if w:
                lex.add(ao1990(w).lower())
        for f in glob.glob(os.path.join(RAIZ, 'conteudo', 'machado-de-assis', '*.js')):
            if f.endswith('poesia.js'):
                continue
            corpo = open(f, encoding='utf-8').read()
            corpo = corpo[corpo.find('"partes"') if '"partes"' in corpo else corpo.find('partes:'):]
            corpo = corpo[:corpo.find('"edicao"')] if '"edicao"' in corpo else corpo
            for w in re.findall(r"[^\W\d_]+", corpo):
                lex.add(w.lower())
        _LEX = lex
        _IDX = defaultdict(list)
        for w in lex:
            _IDX[esqueleto(w)].append(w)
    return _LEX


def wsdic():
    global _WS
    if _WS is None:
        _WS = {}
        for nome in ('wsdic-pt-PT.txt', 'wsdic-pt-BR.txt'):   # o do Brasil por cima
            for l in open(os.path.join(B, nome), encoding='utf-8'):
                m = re.match(r'^\*\s*([^:]+?)\s*:\s*(.+?)\s*$', l)
                if m and ' ' not in m.group(1):
                    _WS[m.group(1)] = m.group(2)
    return _WS


def vogais(w):
    return re.sub(r'[^aeiou]', '', sem_acento(w.lower()).replace('y', 'i'))


def palavra(w):
    """(forma atual, fonte) de uma palavra sem hífen."""
    lex = lexico()
    if w in MANUAL:
        return MANUAL[w], 'manual'
    lw = w.lower()
    if lw in MANUAL:
        return igualar_caixa(w, MANUAL[lw]), 'manual'
    if lw in FICAM:
        return w, 'fica'
    if lw in ('á', 'ás'):
        return igualar_caixa(w, 'à' + lw[1:]), 'regra'
    if re.match(r'^á(quell|quill)', lw):
        return igualar_caixa(w, ao1990(MANUAL.get('a' + lw[1:], 'à' + re.sub('ll', 'l', lw[1:])))), 'regra'
    m = re.match(r'^(.*)éo(s?)$', lw)
    if m:
        return igualar_caixa(w, m.group(1) + 'éu' + m.group(2)), 'regra'
    f = forma_atual(w)
    if f != w:
        return f, 'forma'
    a = ao1990(lw).replace('ü', 'u')
    if a in lex:
        return igualar_caixa(w, a), 'lexico'
    ws = wsdic().get(lw) or wsdic().get(w)
    if ws and ao1990(ws.lower()) in lex and ws[-1:].lower() == lw[-1:] and vogais(ws) == vogais(lw):
        return igualar_caixa(w, ao1990(ws.lower())), 'wikisource'
    if lw.endswith('io') and lw not in lex and (lw[:-2] + 'iu') in lex:   # pretérito: abrio → abriu
        return igualar_caixa(w, lw[:-2] + 'iu'), 'regra'
    if lw.endswith('ão') and len(lw) > 4:   # -ão átono do verbo (dominão, errão) = -am
        n, f = palavra(w[:-2] + 'am')
        if f in ('lexico', 'esqueleto', 'wikisource', 'manual'):
            return n, f
    ops = [o for o in _IDX.get(esqueleto(lw), []) + _IDX.get(esqueleto(lw, 'k'), []) if vogais(o) == vogais(lw)]
    if not ops:
        ops = [o for o in _IDX.get(esqueleto(lw), [])]
        ops = [o for o in ops if SequenceMatcher(None, sem_acento(o), sem_acento(lw)).ratio() > 0.75]
        if ops:
            o = max(ops, key=lambda o: SequenceMatcher(None, lw, o).ratio())
            return igualar_caixa(w, regras(lw)), 'SEM_PAR'   # par duvidoso (%s): fica a regra
    if ops:
        o = max(ops, key=lambda o: (SequenceMatcher(None, lw, o).ratio(), o))
        return igualar_caixa(w, o), 'esqueleto'
    r = regras(lw)
    if r != lw:
        if r in lex:
            return igualar_caixa(w, r), 'regras'
        return igualar_caixa(w, r), 'SEM_PAR'
    return w, 'SEM_PAR'


def regras(w):
    """As mudanças de grafia certas, sem o léxico (o acento fica para a conferência)."""
    w = w.replace('ph', 'f').replace('th', 't').replace('rh', 'r').replace('y', 'i')
    w = re.sub(r'ch(?=[rl])', 'c', w)
    w = re.sub(r'([bcdfglmnpt])\1', r'\1', w)
    w = re.sub(r'(?<=[aeiouáéíóúâêô])h(?=[aeiouáéíóú])', '', w)
    w = re.sub(r'(?<=[aeiou])c(?=t)', '', w)
    w = re.sub(r'mn', 'n', w)
    w = re.sub(r'ae$', 'ai', w); w = re.sub(r'aes$', 'ais', w)
    w = re.sub(r'oe$', 'oi', w); w = re.sub(r'oes$', 'ois', w)
    w = re.sub(r'eo$', 'eu', w)
    return ao1990(w)


ENCL = re.compile(r"^([^\W\d_]+?)l-(o|a|os|as)$", re.U)
MESO = {'ha': 'á', 'hei': 'ei', 'has': 'ás', 'hemos': 'emos', 'heis': 'eis', 'hão': 'ão', 'hia': 'ia', 'hias': 'ias',
        'hiamos': 'íamos', 'hieis': 'íeis', 'hiam': 'iam'}


def token(w, rel):
    if re.match(r"^[^\W\d_]", w) is None:
        return w
    w0 = w
    w = w.replace('′', "'").replace('’', "'")
    lw = w.lower()
    if lw in JUNTAR:
        n = igualar_caixa(w, JUNTAR[lw]); rel.append((w0, n, 'contração')); return n
    if lw in FICAM:
        return w
    m = ENCL.match(w)
    if m and m.group(1).lower() not in ('a', 'e', 'o'):   # vêl-o → vê-lo, dal-os → dá-los, acordal-a → acordá-la
        base = m.group(1)
        if base[-1] in 'aeo' and not re.search(r'[áéêôó]$', base):
            base = base[:-1] + {'a': 'á', 'e': 'ê', 'o': 'ô'}[base[-1]]
        n, f = palavra(base) if base.lower() not in lexico() else (base, 'lexico')
        n = n + '-l' + m.group(2)
        rel.append((w0, n, 'ênclise')); return n
    partes = w.split('-')
    if len(partes) > 1:
        novas = []
        for k, p in enumerate(partes):
            if k and p.lower() in MESO and k == len(partes) - 1 and len(partes) >= 3:
                novas.append(MESO[p.lower()]); continue
            if k and p.lower() in ('o', 'a', 'os', 'as', 'me', 'te', 'se', 'lhe', 'lhes', 'nos', 'vos', 'lo', 'la', 'los',
                                  'las', 'no', 'na', 'nas'):
                novas.append(p); continue
            if not p:
                novas.append(p); continue
            novas.append(palavra(p)[0])
        n = '-'.join(novas)
        n = {'meia-noite': 'meia-noite'}.get(n, n)
        if n != w0:
            rel.append((w0, n, 'hífen'))
        return n
    if "'" in w:
        return w   # elisão do verso que fica (co'as, minh'alma…)
    n, f = palavra(w)
    if n != w0:
        rel.append((w0, n, f))
    elif f == 'SEM_PAR':
        rel.append((w0, n, f))
    return n


def por_que(t):
    """«porque» de pergunta direta (antes do «?» da mesma frase) > «por que»; antes da pontuação, «por quê»."""
    def frase(m):
        s = m.group(0)
        if '?' not in s:
            return s
        s = re.sub(r'\b([Pp])orque(?=\s*[?!])', lambda x: x.group(1) + 'or quê', s)
        return re.sub(r'(?<!\bo )\b([Pp])orque\b(?=[^.!]*\?)', lambda x: x.group(1) + 'or que', s)
    return re.sub(r'[^.!?]*[.!?]+', frase, t)


def modernizar_linha(l, rel, estrangeiro=False):
    if estrangeiro:
        return l
    out = []
    for w in TOK.findall(l):
        out.append(token(w, rel))
    return ''.join(out)


def arquivo(pid, rel):
    linhas = open(os.path.join(AQUI, '1901', pid + '.txt'), encoding='utf-8').read().split('\n')
    out = []
    for l in linhas:
        m = re.match(r'^# (\w+):? ?(.*)$', l)
        if m:
            k, v = m.group(1), m.group(2)
            if k in ('nota',) or (k == 'epigrafe' and v.startswith(EPIGRAFES_FORA)):
                out.append(l); continue
            if k == 'epigrafe' and '(' in v:   # o autor citado entre parênteses também se atualiza
                pass
            out.append('# %s: %s' % (k, modernizar_linha(v, rel)) if v else l)
            continue
        if pid in ESTRANGEIRO or re.match(r'^[=@] ', l):
            out.append(l); continue
        # citação estrangeira em itálico longo (F. Denis, nas notas): fica
        partes = re.split(r'(_[^_]{60,}_)', l)
        out.append(''.join(p if (p.startswith('_') and re.search(r"\b(les|des|et|du|le|la)\b", p)) else modernizar_linha(p, rel) for p in partes))
    t = '\n'.join(out)
    return por_que_linhas(t)


def por_que_linhas(t):
    # junta os versos de cada estrofe para achar as perguntas, e reparte de novo
    blocos = t.split('\n\n')
    novos = []
    for b in blocos:
        ls = b.split('\n')
        corpo = [i for i, l in enumerate(ls) if not l.startswith('#')]
        if not corpo:
            novos.append(b); continue
        sep = '\u0001'
        junto = sep.join(ls[i] for i in corpo)
        novo = por_que(junto).split(sep)
        for i, n in zip(corpo, novo):
            ls[i] = n
        novos.append('\n'.join(ls))
    return '\n\n'.join(novos)


if __name__ == '__main__':
    P = json.load(open(os.path.join(AQUI, 'poemas.json'), encoding='utf-8'))
    os.makedirs(os.path.join(AQUI, 'texto'), exist_ok=True)
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    cont = Counter(); fonte = {}
    for p in P:
        rel = []
        t = arquivo(p['id'], rel)
        open(os.path.join(AQUI, 'texto', p['id'] + '.txt'), 'w', encoding='utf-8').write(t)
        for a, b, f in rel:
            cont[(a, b)] += 1; fonte[(a, b)] = f;
    with open(os.path.join(AQUI, 'relatorios', 'grafia.tsv'), 'w', encoding='utf-8') as fo:
        for (a, b), n in sorted(cont.items(), key=lambda x: (fonte[x[0]], x[0][0].lower())):
            fo.write('%s\t%s\t%s\t%d\n' % (fonte[(a, b)], a, b, n))
    print(Counter(fonte.values()))
