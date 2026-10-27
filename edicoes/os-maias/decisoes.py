"""Os Maias — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia da 1ª edição: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da 1ª edição
  'ocr'     erro das transcrições digitais; a 1ª edição traz a forma correta (conferido no fac-símile)
  'revisao' lição da 1ª edição conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem
VERSOS / TITULOS: não há
"""

EMENDAS = [
    # erros tipográficos da 1ª edição
    ('erro', "Emfim, o sr. Affonso de Maia trazia", "Emfim, o sr. Affonso da Maia trazia"),
    ('erro', "aos uivos lacinantes", "aos uivos lancinantes"),
    ('erro', "as duas cadeias estavam", "as duas cadeiras estavam"),
    ('erro', "porque o Carlos Gomes não", "porque o Castro Gomes não"),
    ('erro', "que teve a hora de apertar", "que teve a honra de apertar"),
    ('erro', "nós declamamos Mussuet", "nós declamamos Musset"),
    ('erro', "que entravam que preserverassem", "que entravam que perseverassem"),
    ('erro', "semblante feroz de Santanaz", "semblante feroz de Satanaz"),
    ('erro', "fizeram tilintir os vidros", "fizeram tilintar os vidros"),
    ('erro', "no vago das Nebuloses", "no vago das Nebulosas"),
    ('erro', "roída de syphlis", "roída de syphilis"),
    ('erro', "Veja você esse Deft", "Veja você esse Delft"),
    ('erro', "no café dos Romulares", "no café dos Remolares"),
    ('erro', "moveis enramelhetados d'ouro", "moveis enramalhetados d'ouro"),
    ('erro', "esta intallação summaria", "esta installação summaria"),
    ('erro', "Foi uma flitartion de praia", "Foi uma flirtation de praia"),
    ('erro', "aguardasolados de auraucarias", "aguardasolados de araucarias"),
    ('erro', "velha ballada escandinavia", "velha ballada escandinava"),
    ('erro', "imagem roubada a Beaudelaire", "imagem roubada a Baudelaire"),
    ('erro', "ao lado de Beaudelaíre", "ao lado de Baudelaire"),
    ('erro', "que redominava", "que predominava"),
    ('erro', "o tenuo e leve", "o tenue e leve"),
    ('erro', "convento das Selesias", "convento das Salesias"),
    # lições da 1ª edição (conferidas no fac-símile) que o confronto perdia para as edições posteriores
    ('revisao', "para lá se arrecadarem as mobilias", "para lá se arrecadaram as mobilias"),
    ('revisao', "a entregar-lhe as amendoas", "a entregar-lha as amendoas"),
    ('revisao', "N'esse momento, alguns dos rapazes", "N'esse momento, algum dos rapazes"),
    ('ocr', "elle ia amarguarar a velhice", "elle ia amargurar a velhice"),
    ('ocr', "as pancadas desordenandas do", "as pancadas desordenadas do"),
    ('ocr', "faziam uma neva onde", "faziam uma nevoa onde"),
    ('ocr', "n'um coupé estufo de", "n'um coupé escuro de"),
    ('ocr', "a mamã parcela ir", "a mamã parecia ir"),
    ('ocr', "kiosque parceia ter", "kiosque parecia ter"),
    ('ocr', "Maria rindo, rodas estas", "Maria rindo, todas estas"),
    ('ocr', "uma teia banal", "uma tela banal"),
    ('ocr', "rica senhora para quer foi", "rica senhora, para que foi"),
    ('revisao', "a impressão de uma catastrophe", "a impressão d'uma catastrophe"),
    ('revisao', "no fundo de uma poltrona, com o", "no fundo d'uma poltrona, com o"),
    ('revisao', "serenamente, subiu ao primeiro", "serenamente, subia ao primeiro"),
    ('revisao', "Ega pareceu surprendido", "Ega pareceu surprehendido"),
    ('revisao', "aparentada com os Medina-Coeli", "aparentada com os Medina-Cœli"),
    ('revisao', "a parenta dos Medina-Coeli", "a parenta dos Medina-Cœli"),
    ('revisao', "profond de son coeur", "profond de son cœur"),
    ('revisao', "C'était un oeillet", "C'était un œillet"),
]

AJUSTES = []

# chave: a palavra da 1ª edição (depois da separação de «d'»: d'ora -> de + ora); valor: a forma final
MANUAL = {
    # formas antigas de palavras atuais
    'Bureocracia': 'Burocracia', 'agazalhando-se-lhe': 'agasalhando-se-lhe', "Juro-t'o": 'Juro-to',
    "Senta-t'ahi": 'Senta-te aí', 'alcools': 'álcoois', 'almanach': 'almanaque', 'Almanachs': 'Almanaques',
    'asthma': 'asma', 'brazileirito': 'brasileirito', 'chaile': 'xale', 'chaile-manta': 'xale-manta',
    'cincoenta': 'cinquenta', 'costellas': 'costelas', 'continuára': 'continuara', 'sustára': 'sustara',
    'desesete': 'dezessete', 'dezesete': 'dezessete', 'dezeseis': 'dezesseis', 'lithographia': 'litografia',
    'pertenção': 'pretensão', 'psalmos': 'salmos', 'quiz-lhe': 'quis-lhe', 'structura': 'estrutura',
    'spiritismo': 'espiritismo', 'tagarallice': 'tagarelice', 'trespassal-o': 'trespassá-lo',
    'vacillando': 'vacilando', 'voltarianna': 'voltariana', 'reportorios': 'reportórios',
    'dignatario': 'dignatário', 'tegurio': 'tegúrio', 'Romelia': 'Romélia', 'Claudio': 'Cláudio',
    'Thiago': 'Tiago', 'Magdalena': 'Madalena', 'Judith': 'Judite', 'Gran-Bretanha': 'Grã-Bretanha',
    'gran-cruz': 'grã-cruz', 'gran-cruzes': 'grã-cruzes', 'Sparta': 'Esparta', 'Strasburgo': 'Estrasburgo',
    'Nova-Orleans': 'Nova Orleans', 'New-York': 'Nova York', 'Démos-nos': 'Demo-nos', 'exª': 'ex.ª',
    'regimen': 'regímen', 'Couces': 'Coices', 'couce': 'coice', 'bonet': 'boné', 'rewolver': 'revólver',
    'faiença': 'faiança', 'faienças': 'faianças', 'faenças': 'faianças', 'lageas': 'lajes',
    'escondrijo': 'esconderijo', 'embigo': 'umbigo', 'infanteria': 'infantaria', 'artilheria': 'artilharia',
    'walsa': 'valsa', 'walsas': 'valsas', 'walsar': 'valsar', 'walsando': 'valsando', 'perceptor': 'preceptor',
    'balustrada': 'balaustrada', 'choramigar': 'choramingar', 'esgouroviado': 'esgrouviado',
    'resvelando': 'resvalando', 'obdecendo': 'obedecendo', 'longiquo': 'longínquo', 'facha': 'faixa',
    'Filandia': 'Finlândia', 'filandez': 'finlandês', 'filandezas': 'finlandesas', 'Filandezas': 'Finlandesas',
    'Belzebut': 'Belzebu', 'Bebado': 'Bêbado', 'bebado': 'bêbado', 'bebedo': 'bêbedo',
    'ora': 'ora', 'menage': 'ménage', 'emfim': 'enfim', 'Emfim': 'Enfim', 'hontem': 'ontem',
    'hombro': 'ombro', "d'outr'ora": "d'outrora", "d'ora": 'de ora', "d'esse": 'desse', 'Orleans': 'Orleans',
    'chapéos': 'chapéus', 'soffre': 'sofre', 'substitue-se': 'substitui-se', 'palletot': 'paletot',
}

# abreviaturas com letras sobrescritas na 1ª edição (sr.ª, S.ta, M.me, v. ex.as, n.º): as letras
# ficam em linha, coladas ao ponto, como uma palavra só
SOBRESCRITAS = {
    'ª': None, 'º': None,                                   # depois de qualquer abreviatura
    'ta': {'S', 'St'}, 't': {'S'}, 'me': {'M'}, 'mo': {'Ex', 'Exc', 'ex', 'exc'},
    'as': {'ex', 'exc', 'Ex', 'Exc', 'C'}, 'os': {'ex', 'exc', 'Ex', 'Exc'},
}


def corrigir(out, flags):
    novo, nf = [], []
    i = 0
    while i < len(out):
        t = out[i]
        if (i + 2 < len(out) and out[i + 1] == '.' and t[:1].isalnum() and len(t) <= 4
                and out[i + 2] in SOBRESCRITAS
                and (SOBRESCRITAS[out[i + 2]] is None or t in SOBRESCRITAS[out[i + 2]])):
            novo.append(t + '.' + out[i + 2]); nf.append(flags[i])
            i += 3
            continue
        novo.append('...' if t == '..' else t); nf.append(flags[i])      # «!..» da 1ª edição
        i += 1
    return novo, nf
