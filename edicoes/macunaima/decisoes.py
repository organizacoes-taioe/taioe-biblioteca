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
    'boiuna': 'boiúna', 'querencia': 'querência', 'beijú': 'beiju', 'pajuarí': 'pajuari', 'carurús': 'carurus', 'macurú': 'macuru', 'javarí': 'javari', 'hindú': 'hindu',
    'tucuchí': 'tucuxi', 'jamachí': 'jamaxi', 'cachirí': 'cachiri', 'çairê': 'sairê',
}

AJUSTES = []

# erros de OCR que o voto não pegou e erros de 1928, conferidos no fac-símile: (tipo, antes, de, para,
# depois), em tokens do texto pronto («-» vale pelo travessão em que o hífen solto se torna); corrigir()
CORRECOES = [
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
    ('ocr', 'e as', '- Mulheres', 'mulheres', 'soltavam'),
    ('ocr', 'não quis', 'por - quê', 'porquê', 'não'),
    ('ocr', 'tronco de', 'co - Paíba', 'copaíba', 'e'),
    ('ocr', 'não se', 'ave - Xe', 'avexe', 'não'),
    ('ocr', 'bichinho muito', '- Pra', 'pra', 'longe'),
    ('ocr', 'de tanta', 'como - Cão', 'comoção', 'e'),
    ('ocr', 'Então', 'Cama-Pá - bimque', 'Cama-Pabimque', 'virou'),
    # ponto final que o OCR leu como hífen
    ('ocr', 'estava fechada', '-', '.', 'Maanape coçou'),
    ('ocr', 'de assacu', '-', '.', 'Entrou na'),
    ('ocr', 'de horror', '-', '.', 'Tia Ciata'),
    ('ocr', 'mestre Cosme', '-', '.', 'Então voltou'),
    ('ocr', 'a inesquecível', '-', '.', 'Chamou os'),
    ('ocr', 'de mim', '-', '.', 'Esconde lá'),
    ('ocr', 'pé esquerdo', '-', '.', 'Tomou banho'),
    ('ocr', 'cara dele', '-', '.', 'Ajuntou um'),
    ('ocr', 'sabendo escolher', '-', '.', 'O coração'),
    # maiúscula que o OCR pôs no começo da linha, e pontos perdidos (conferidos com outra edição e no fac-símile)
    ('ocr', 'rede', 'Jiguê', '. Jiguê', 'já'),
    ('ocr', 'todos', 'Que', 'que', 'de'),
    ('ocr', 'ele', 'Passear', 'passear', 'e'),
    ('ocr', 'num', 'Príncipe', 'príncipe', 'fogoso'),
    ('ocr', 'boto', 'Pra', 'pra', 'comerem'),
    ('ocr', 'corria', 'Pelo', 'pelo', 'mato'),
    ('ocr', 'o', 'Pescoço', 'pescoço', ','),
    ('ocr', 'noite', 'Inteira', 'inteira', ','),
    ('ocr', 'desesperado', 'Porquê', 'porquê', 'era'),
    ('ocr', 'volvendo', 'Pros', 'pros', 'matos'),
    ('ocr', 'numa', 'Maloca', 'maloca', 'mais'),
    ('ocr', 'é', 'Mui', 'mui', 'alta'),
    ('ocr', 'alta', 'Os', '. Os', 'dois'),
    ('ocr', 'não', 'Secundar', 'secundar', 'cantiga'),
    ('ocr', 'me', 'Pica', 'pica', 'não'),
    ('ocr', 'ficou', 'Pesado', 'pesado', 'mas'),
    ('ocr', 'bem', 'Perguntando', 'perguntando', 'si'),
    ('ocr', 'carnaúba', 'Posta', 'posta', 'ali'),
    ('ocr', 'mais', 'Preso', 'preso', '.'),
    ('ocr', 'sem', 'Nenhuma', 'nenhuma', 'falsidade'),
    ('ocr', 'enregelado', 'Mordido', 'mordido', 'e'),
    ('ocr', 'calor', 'Porquê', 'porquê', 'ele'),
    ('ocr', 'erguida', 'Pelo', 'pelo', 'andar'),
    ('ocr', 'não', 'Podia', 'podia', 'nem'),
    ('ocr', 'gigante', 'Imaginou', '. Imaginou', 'botar'),
    ('ocr', 'rede', 'Mastigando', 'mastigando', 'beiju'),
    ('ocr', 'perguntar', 'Pros', 'pros', 'outros'),
    ('ocr', 'bem', 'Maanape', '. Maanape', 'e'),
    ('ocr', 'tem', 'Pescoço', 'pescoço', ','),
    ('ocr', 'número', 'Igual', 'igual', '.'),
    ('ocr', 'madrugada', 'Veio', 'veio', 'a'),
    ('ocr', 'na', 'Madrugada', 'madrugada', '.'),
    ('ocr', 'um', 'Puro', 'puro', 'de'),
    # «E’» de 1928 é «É»: o OCR perdeu o apóstrofo, e ficou a conjunção
    ('ocr', 'um cipó .', 'E', 'É', 'lá que Ci'),
    ('ocr', 'numa planta .', 'E', 'É', 'aquela uma'),
    ('ocr', 'é cruel .', 'E', 'É', 'capaz de pedir'),
    ('ocr', 'desagradável nova .', 'E', 'É', 'bem verdade'),
    ('ocr', 'do céu .', 'E', 'É', 'aquele caminho de luz'),
    ('ocr', 'Cruzeiro nada !', 'E', 'É', 'o Pai do Mutum'),
    ('ocr', 'do Mutum !', 'E', 'É', 'o Pai do Mutum'),
    ('ocr', 'minha gente !', 'E', 'É', 'o Pai do Mutum'),
    ('ocr', 'que é :', "E '", 'É', 'comprido roliço'),
    ('ocr', 'Cachorro !', "E '", 'É', 'na África'),
    ('ocr', '! ¶ —', 'E’', 'É', '! ¶ — Ora'),
    # D’aí, A’s: o apóstrofo de 1928
]


# grafia de hoje que o MANUAL não alcança (palavra colada ao «_» do itálico, ou que entrou pelo voto)
FINAL = {
    'falàmos': 'falamos', 'descuidàmos': 'descuidamos', 'inteiràmos': 'inteiramos',
    'linguas': 'línguas', 'india': 'índia', 'género': 'gênero', 'dificil': 'difícil',
    'tumulo': 'túmulo', 'circunstancias': 'circunstâncias', 'mingua': 'míngua', 'abricôs': 'abricós',
    'desagradavel': 'desagradável', 'abstinéncia': 'abstinência', 'exceléncia': 'excelência',
    'orificio': 'orifício', 'sincope': 'síncope', 'simbolo': 'símbolo', 'masorqueiros': 'mazorqueiros',
    'alvíçaras': 'alvíssaras', 'uirauassús': 'uirauaçus', 'cincoenta': 'cinquenta',
}


def _final(t):
    import re as _re
    m = _re.match(r'^(_*)(.*?)(_*)$', t)
    a, w, z = m.groups()
    nova = FINAL.get(w.lower())
    if not nova:
        return t
    if w[:1].isupper():
        nova = nova[:1].upper() + nova[1:]
    return a + nova + z


def corrigir(out, flags):
    """Aplica FINAL e CORRECOES ao texto pronto (cada trecho de CORRECOES aparece uma vez só)."""
    out = [_final(t) for t in out]
    for tipo, antes, de, para, depois in CORRECOES:
        tr = lambda x: ['—' if t == '-' else t for t in x.split()]
        a, d, p, z = tr(antes), tr(de), tr(para), tr(depois)
        pad = a + d + z
        achados = [i for i in range(len(out) - len(pad) + 1) if out[i:i + len(pad)] == pad]
        if len(achados) != 1:
            raise SystemExit(f'correção {antes!r} [{de}] {depois!r}: {len(achados)} ocorrências')
        i = achados[0] + len(a)
        out = out[:i] + p + out[i + len(d):]
        flags = flags[:i] + [False] * len(p) + flags[i + len(d):]
    return out, flags
