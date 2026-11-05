"""Vida de Anchieta — decisões de grafia e de leitura (ver montar.py).

Tudo na forma do impresso de 1897 (1897/NN.txt). O que muda a leitura vai para a «Sobre esta edição»
(ERROS, OMITIDAS) ou para o revisao.json (as decisões do Gere).
"""

# palavra partida no fim da linha diante de «lhe», «se», «o»…: hífen de verdade quando a primeira parte é palavra
HIFEN_ANTES = set()
JUNTAR = set()          # juntar mesmo assim
ABREVIATURAS = {'s', 'd', 'n', 'lib', 'luc', 'cap', 'etc'}

# ------------------------------------------------------------------ antes da grafia (texto de 1897)
# As marcas de A. F. Barata, o copista de 1896 (a lição do manuscrito entre parênteses, «sic», a nota de
# rodapé), saem do texto e vão listadas na «Sobre esta edição» (OMITIDAS): (página, trecho, onde estava).
OMITIDAS = [
    (4, ' _(comuco)_', 'depois de «começo» (cap. 1): a lição do manuscrito, «comuco»'),
    (9, ' _(heiuor)_', 'depois de «fervor» (cap. 6): a lição do manuscrito, «heiuor»'),
    (8, ' _(sic)_', 'depois de «infabilidade» (cap. 5)'),
    (20, ' _(sic)_', 'depois de «sem ocasião nenhuma» (cap. 11)'),
    (33, ' _(sic)_', 'depois de «nunca mais o perdeu» (cap. 18)'),
    (35, ' _(sic)_', 'depois de «Garcia da vila» (cap. 19)'),
    (45, ' _(sic)_', 'depois de «desta a choupana» (cap. 24)'),
    (15, ' (adortio)', 'depois de «José Adortio» (cap. 8)'),
    (7, ' (1)', 'depois de «lissão» (cap. 4): a chamada da nota de rodapé «ou tissão = tição?»'),
    (46, ' (_bibara_)', 'depois de «víbora» (cap. 24): a lição do manuscrito, «bibara»'),
]

# erros evidentes do impresso de 1897, corrigidos: (página, de, para, comentário); vão na «Sobre»
ERROS = [
    (15, 'senho de um engenho', 'senhor de um engenho', ''),
    (16, 'Onvindo', 'Ouvindo', ''),
    (18, 'aqual', 'a qual', ''),
    (22, 'morreram ali máo estado', 'morreram ali em máo estado', 'falta «em»'),
    (24, 'iriam fazer fazer', 'iriam fazer', 'palavra repetida'),
    (24, 'foram fazer fazer', 'foram fazer', 'palavra repetida'),
    (27, 'dissimuladameute', 'dissimuladamente', ''),
    (47, 'recolberam', 'recolheram', ''),
    (47, 'divina bontade', 'divina bondade', ''),
    (8, 'nas quaes Sempre mostrou muito animo, exemplo e paciencia tiveram',
     'nas quaes sempre mostrou muito animo, exemplo e paciencia. Tiveram', 'pontuação'),
]
# erros miúdos de composição, corrigidos sem lista: (página, de, para)
COMPOSICAO = [
    (21, 'devaçaõ', 'devação'),
    (24, 'Irmaõ', 'Irmão'),
    (5, 'fez à doutrina', 'fez a doutrina'),
    (18, 'depois ser verdade,', 'depois ser verdade.'),
    (22, 'de nossa Religião deram', 'de nossa Religião) deram'),
    (30, 'fim do Mez de', 'fim do mez de'),
]

# leituras de Barata emendadas (decisões do Gere no revisao.json: o texto segue a recomendação)
EMENDAS = [
    (8, 'infabilidade', 'afabilidade'),
    (35, 'Garcia da villa', "Garcia d'Avila"),
    (8, 'afabilidade O Padre', 'afabilidade. O Padre'),
]

# abreviaturas e números (regex sobre o texto de 1897)
PRE = [
    (r'P\.e P\.o Rodrigues', 'Padre Pero Rodrigues'),
    (r'S\. P\.º', 'S. Pedro'),
    (r'P\.º RODRIGUES\.', 'Pero Rodrigues.'),
    (r'\bP\.?º (?=Leitão|André)', 'Pero '),
    (r'(\d)\.([ºª])', r'\1\2'),
    (r"\bE' ", 'É '),
    (r'\bP\. José', 'Padre José'),
    (r'\bel Rei\b', 'el-rei'),
    (r'\bem quanto (?=se representava|a sombra|vivessem)', 'enquanto '),
    (r'lib\. 1º Cap\. 8', 'lib. 1º, cap. 8'),
    (r'livro 1º Cap\. 9', 'livro 1º, cap. 9'),
    (r'livro 2º cap\. 2º', 'livro 2º, cap. 2º'),
    (r'Luc\. 22\. Ego', 'Luc. 22: Ego'),
    (r'deu palavra de si;', 'deu palavra de sim;'), (r'Irmão: Porque\?', 'Irmão: Por quê?'), (r'vamo nos', 'vamo-nos'),
    (r'Cabo frio|cabo Frio', 'Cabo Frio'), (r'Fim do Livro 3º', 'Fim do livro 3º.'), (r'Na Baia a 3º de Janeiro de 1607', 'Na Baia, a 3º de Janeiro de 1607.'), (r'José: si sei', 'José: sim sei'), (r'Respondeu: si\.', 'Respondeu: sim.'), (r'dizia que si,', 'dizia que sim,'),
    (r'que estê en gloria', 'que _esté en gloria_'),
    (r'(?<=ministro, )porque(?= se houvera)', 'por que'),       # interrogativa indireta: «por que»
    (r'(?<=perguntou-lhe )porque(?= não ia)', 'por que'),
    (r'(?<=dispenseiro, )porque(?= lhe não dera)', 'por que'),
]

# trechos em latim: em itálico e sem mudança de grafia
LATIM = [
    'in nomine Domini',
    'vade, frater, quia postea nos coniunget locus',
    'Qui se humiliat exaltabitur',
    'quia longa tibi restat vita',
    'qui est mirabilis in sanctis suis',
    'Ego rogavi pro te Petre ut non deficiat fides tua',
    'requiem',
]

# ------------------------------------------------------------------ grafia
# forma de 1897 → forma de hoje (palavra inteira; em minúscula vale para qualquer caixa)
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
    'pera': 'para', 'per': 'por', 'té': 'até', 'vae-te': 'vai-te', 'frecha': 'flecha', 'chamar-se-á': 'chamar-se-á', 'vae-se': 'vai-se', 'saio': 'saiu', 'ayres': 'aires', 'victoria': 'vitória', 'bocca': 'boca', 'summa': 'suma', 'vae': 'vai', 'riba': 'riba', 'serrão': 'serrão', 'lacão': 'lacão', 'croncrenas': 'croncrenas', 'lissão': 'lissão', 'gasalhado': 'gasalhado',
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


def crase(t, seg, ant):
    """á, ás, áquelle… de 1897: crase de hoje (a revisão olhou todas, relatorios/crase.tsv)."""
    base = {'á': 'à', 'ás': 'às', 'áquelle': 'àquele', 'áquella': 'àquela', 'áquelles': 'àqueles',
            'áquellas': 'àquelas', 'áquillo': 'àquilo'}[t.lower()]
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
