"""Reinações de Narizinho: a grafia de 1931 passada à de hoje (Acordo de 1990, forma brasileira), palavra por
palavra, com o modernizador das Poesias Completas de Machado (edicoes/poesias-completas-machado/modernizar.py:
contrações, ênclise «accommodal-a» → «acomodá-la», «á» → «à», léxico do sistema, dicionário de modernização do
Wikisource, esqueleto ph/f, y/i, consoantes dobradas…), com as decisões desta obra em MANUAL e FICAM.

    python3 -I edicoes/reinacoes-de-narizinho/grafia.py      relatório de todas as trocas (rel/grafia.tsv)

O dicionário do Wikisource (wsdic-pt-BR.txt e wsdic-pt-PT.txt, de «Wikisource:Modernização/Dicionário») fica em
ferramentas/cache/reinacoes-de-narizinho/ (fora do git).
"""
import importlib.util
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
_spec = importlib.util.spec_from_file_location('pcm_mod', os.path.join(RAIZ, 'edicoes', 'poesias-completas-machado', 'modernizar.py'))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
M.B = os.path.join(RAIZ, 'ferramentas', 'cache', 'reinacoes-de-narizinho')

# ------------------------------------------------------------------ decisões desta obra
MANUAL = {
    # nomes de pessoas e lugares na grafia de hoje
    'Emilia': 'Emília', 'Emilias': 'Emílias', 'EMILIA': 'EMÍLIA', 'Nastacia': 'Nastácia', 'Nastacias': 'Nastácias',
    'NASTACIA': 'NASTÁCIA', 'Anastacia': 'Anastácia', 'Lucia': 'Lúcia', 'Felix': 'Félix', 'FELIX': 'FÉLIX',
    'Antonia': 'Antônia', 'Christovão': 'Cristóvão', 'Christo': 'Cristo', 'Egypto': 'Egito', 'Italia': 'Itália',
    'Grecia': 'Grécia', 'Arabia': 'Arábia', 'Patagonia': 'Patagônia', 'Cornelio': 'Cornélio', 'Theseu': 'Teseu',
    'Athenas': 'Atenas', 'Hippocrates': 'Hipócrates', 'Mephistopheles': 'Mefistófeles', 'Dodóca': 'Dodoca',
    'Biotonico': 'Biotônico', 'Alice': 'Alice', 'Ann': 'Ann', 'Raggedy': 'Raggedy', 'York': 'York', 'Wendy': 'Wendy',
    'Grimm': 'Grimm', 'Spinelli': 'Spinelli', 'Scheherazade': 'Scheherazade', 'Sheherazade': 'Sheherazade',
    'Stylopyga': 'Stylopyga', 'Moraes': 'Moraes', 'Capuzinho': 'Capuzinho', 'Cavallete': 'Cavalete',
    # nomes inventados pelo autor: ficam (só a grafia de época muda)
    'Pinocchio': 'Pinocchio', 'PINOCCHIO': 'PINOCCHIO', 'pinocchianas': 'pinocchianas',
    'Escavallinho': 'Escavalinho', 'escavallinho': 'escavalinho', 'ESCAVALLINHO': 'ESCAVALINHO',
    'Penninha': 'Peninha', 'penninha': 'peninha', 'PENNINHA': 'PENINHA', 'Pollegada': 'Polegada',
    'Lafontaine': 'Lafontaine', 'Munkausen': 'Munkausen', 'Munchkausen': 'Munchkausen', 'Pixoxó': 'Pixoxó',
    'pichochó': 'pixoxó', 'Fazdeconta': 'Fazdeconta', 'Pantasma': 'Pantasma', 'PANTASMA': 'PANTASMA',
    'mecê': 'mecê', 'Mecê': 'Mecê', 'sêo': 'sêo', 'Sêo': 'Sêo', 'Nha': 'Nhá', 'pezes': 'pezes', 'han': 'han',
    'Ché': 'Ché', 'ahhh': 'ahhh', 'Ahn': 'Ahn', 'ahn': 'ahn', 'zunnn': 'zunnn', 'fiunnn': 'fiunnn', 'Uff': 'Uff',
    'uff': 'uff', 'hou': 'hou', 'bá': 'bá', 'areoplano': 'areoplano', 'cincoentaneto': 'cinquentaneto',
    'Li-pa-ris': 'Li-pa-ris', 'POL-LE-GA-DA': 'POL-LE-GA-DA', 'Qua-dra-ge-si-mo': 'Qua-dra-gé-si-mo',
    'sa-bé-dó-ria': 'sa-bé-dó-ria', 'TOM-MIX': 'TOM-MIX', 'Tom-Mix': 'Tom-Mix', 'cowboy': 'cowboy',
    # o modernizador acharia par errado ou não acharia
    'ahi': 'aí', 'Ahi': 'Aí', 'dahi': 'daí', 'Dahi': 'Daí', "d'ahi": 'daí', 'Amen': 'Amém', 'amen': 'amém',
    'Arre': 'Arre', 'azinhas': 'asinhas', 'bicharia': 'bicharia', 'bobinha': 'bobinha', 'cartolinha': 'cartolinha',
    'elephantinho': 'elefantinho', 'francez': 'francês', 'galhinho': 'galhinho', 'igualha': 'igualha',
    'macella': 'macela', 'Macella': 'Macela', 'macellar': 'macelar', 'mez': 'mês', 'paiz': 'país', 'Paiz': 'País',
    'rataria': 'rataria', 'ricino': 'rícino', 'Ricino': 'Rícino', 'vóvó': 'vovó', 'Vóvó': 'Vovó', 'vóvós': 'vovós',
    'VÓVÓ': 'VOVÓ', 'zoada': 'zoada', 'sura': 'sura', 'areie': 'areie', 'cômo': 'como', 'experto': 'esperto',
    'élle': 'ele', 'continua': 'continua', 'viramos': 'viramos', 'vivido': 'vivido', 'duvida': 'dúvida',
    'pintão': 'pintão', 'PINTÃO': 'PINTÃO', 'Pintão': 'Pintão', 'bóia': 'boia', 'cassinha': 'cassinha',
    'escoral-a': 'escorá-la', 'restituil-a': 'restituí-la', 'substituil-o': 'substituí-lo',
    'pelo-signaes': 'pelo-sinais', 'zaz-traz': 'zás-trás', 'ouro-macella': 'ouro-macela', 'deLicadissimo': 'delicadíssimo',
    'afin': 'a fim', 'afim': 'a fim', 'zeppelin': 'zepelim', 'detective': 'detetive',
    # formas de 1931 de palavras de hoje
    'quasi': 'quase', 'poude': 'pôde', 'peor': 'pior', 'Peor': 'Pior', 'peores': 'piores', 'Porisso': 'Por isso',
    'porisso': 'por isso', 'deante': 'diante', 'adeante': 'adiante', 'adeanta': 'adianta', 'adeantada': 'adiantada',
    'adeantou': 'adiantou', 'idéa': 'ideia', 'idéas': 'ideias', 'Idéa': 'Ideia', 'teem': 'têm', 'Teem': 'Têm',
    'creada': 'criada', 'creados': 'criados', 'creando': 'criando', 'creança': 'criança', 'Creança': 'Criança',
    'creanças': 'crianças', 'crear': 'criar', 'creatura': 'criatura', 'creaturas': 'criaturas',
    'creaturinha': 'criaturinha', 'creaturinhas': 'criaturinhas', 'creou': 'criou', 'Malcreada': 'Malcriada',
    'malcreado': 'malcriado', 'malcreações': 'malcriações', 'dagua': "d'água", 'nalguem': 'nalguém',
    'cincoenta': 'cinquenta', 'logar': 'lugar', 'legoas': 'léguas', 'machina': 'máquina', 'chimica': 'química',
    'orchestra': 'orquestra', 'gavea': 'gávea', 'gigantea': 'gigântea', 'restea': 'réstia', 'craneo': 'crânio',
    'heroe': 'herói', 'heroes': 'heróis', 'heroezinho': 'heroizinho', 'assembléa': 'assembleia',
    'Bemvindo': 'Bem-vindo', 'Bemvinda': 'Bem-vinda', 'semcerimonia': 'sem-cerimônia', 'atôa': 'à toa',
    'louvadeus': 'louva-a-deus', 'guardachuvinha': 'guarda-chuvinha', 'furabolos': 'fura-bolos',
    'coisaruim': 'coisa-ruim', 'archibancadas': 'arquibancadas', 'taboa': 'tábua', 'taboas': 'tábuas',
    'taboleiro': 'tabuleiro', 'taboleta': 'tabuleta', 'cubiça': 'cobiça', 'cordeal': 'cordial',
    'cortezmente': 'cortesmente', 'kilo': 'quilo', 'kilinho': 'quilinho', 'nickeis': 'níqueis', 'torquez': 'torquês',
    'gasteropode': 'gasterópode', 'camondongo': 'camundongo', 'camondongos': 'camundongos', 'motuca': 'mutuca',
    'reboliço': 'rebuliço', 'rebolico': 'rebuliço', 'lampeão': 'lampião', 'Lampeão': 'Lampião',
    'lampeões': 'lampiões', 'resabiado': 'ressabiado', 'resabiados': 'ressabiados', 'receiasse': 'receasse',
    'receiava': 'receava', 'Receiava': 'Receava', 'receiavam': 'receavam', 'recheiada': 'recheada',
    'recheiado': 'recheado', 'recheiassemos': 'recheássemos', 'recheiou': 'recheou', 'enleiaram': 'enlearam',
    'arreiados': 'arreados', 'constitue': 'constitui', 'diminue': 'diminui', 'distribue': 'distribui',
    'possue': 'possui', 'Possue': 'Possui', 'azues': 'azuis', 'signaes': 'sinais', 'signalzinho': 'sinalzinho',
    'subditas': 'súditas', 'jaboti': 'jabuti', 'jaboticaba': 'jabuticaba', 'jaboticabas': 'jabuticabas',
    'jaboticabeira': 'jabuticabeira', 'JABOTICABAS': 'JABUTICABAS', 'nacar': 'nácar', 'tútú': 'tutu',
    'hade': 'há de', 'mingoante': 'minguante', 'recae': 'recai', 'Sáe': 'Sai', 'cáe': 'cai', 'Egypcios': 'Egípcios',
    'Allemanha': 'Alemanha', 'Troia': 'Troia',
    'depézinha': 'depezinha', 'cow-boy': 'cowboy', 'Marquez': 'Marquês', 'marquez': 'marquês', 'MARQUEZ': 'MARQUÊS', 'marqueza': 'marquesa', 'Marqueza': 'Marquesa',
    'filés': 'filés', 'hurrahs': 'hurras', 'nhen': 'nhen', 'HOJE': 'HOJE', 'facto': 'fato', 'effeito': 'efeito',
    'trophéos': 'troféus', 'caracter': 'caráter', 'flôr': 'flor', 'beija-flôr': 'beija-flor',
    'damnadissima': 'danadíssima', 'acção': 'ação', 'siquer': 'sequer', 'princezinha': 'princesinha',
    'hervinhas': 'ervinhas', 'nubia': 'núbia', 'nubios': 'núbios', 'escaléres': 'escaleres', 'peteléco': 'peteleco',
    'potóca': 'potoca', 'ajutorio': 'ajutório', 'há-de': 'há de', 'hei-de': 'hei de', 'Há-de': 'Há de',
    'super-alimentação': 'superalimentação', 'para-quedas': 'paraquedas', 'dona-de-casa': 'dona de casa',
    'engulir': 'engolir', 'enguliu': 'engoliu', 'engulido': 'engolido', 'engulida': 'engolida', 'enguli': 'engoli',
    'engulira': 'engolira', 'engulo': 'engulo', 'engulidinha': 'engolidinha', 'desengulir': 'desengolir',
    'desengula': 'desengula', 'engula': 'engula', 'aproveitavel': 'aproveitável', 'cascavel': 'cascavel', 'exquisitissimo': 'esquisitíssimo', 'exquisitissima': 'esquisitíssima', 'furtar-côr': 'furtar-cor', 'phelómeno': 'felômeno', 'resomnando': 'ressonando', 'PiNOCCHIO': 'PINOCCHIO',
}
FICAM = set()

# léxico a mais: as palavras dos livros em português já publicados (grafia de hoje) que aparecem em duas
# obras ou mais (uma só pode ser forma antiga esquecida, como «sossêgo»); o /usr/share/dict/brazilian não
# tem palavras comuns («vontade», «mãos»), e sem elas o esqueleto procurava par onde não precisa.
PORTUGUES = ['machado-de-assis', 'graciliano-ramos', 'lima-barreto', 'jose-de-alencar', 'eca-de-queiros',
             'manuel-antonio-de-almeida', 'mario-de-andrade', 'camilo-castelo-branco', 'raul-pompeia',
             'aluisio-azevedo', 'joaquim-nabuco']


def _lexico_extra():
    import glob
    from collections import defaultdict
    obras = defaultdict(set)
    for aut in PORTUGUES:
        for arq in glob.glob(os.path.join(RAIZ, 'conteudo', aut, '*.js')):
            corpo = open(arq, encoding='utf-8').read()
            i = corpo.find('partes:')
            corpo = corpo[i:] if i >= 0 else corpo
            for w in set(re.findall(r'[^\W\d_]+', corpo)):
                if w[:1].islower():
                    obras[w].add(arq)
    return {w for w, a in obras.items() if len(a) >= 2}


_lex0 = M.lexico


def _lexico():
    if M._LEX is None:
        _lex0()
        extra = _lexico_extra() - M._LEX
        M._LEX |= extra
        for w in extra:
            if w != M.sem_acento(w):
                M._ACENTO[M.sem_acento(w)].append(w)
            M._IDX[M.esqueleto(w)].append(w)
    return M._LEX


M.lexico = _lexico
M.MANUAL = {**M.MANUAL, **MANUAL}
M.FICAM = set(M.FICAM) | FICAM


# palavras com apóstrofo (o modernizador as deixa como estão)
APOSTROFO = {"E'": 'É', "A'": 'À', "A's": 'Às', "E'pé": 'Épé', "p'ra": 'pra', "d'ora": 'de ora',
             "sobr'olhos": 'sobrolhos', "p'r'áqui": "p'r'aqui", "p'r'alli": "p'r'ali", "PO'": 'PÓ'}


def linha(l, rel):
    out = []
    l = l.replace('A´', "A'").replace('E´', "E'").replace('O´', "O'")
    for w in M.TOK.findall(l):
        if w in APOSTROFO:
            rel.append((w, APOSTROFO[w], 'manual'))
            out.append(APOSTROFO[w])
        elif len(w) > 1 and w.isupper() and w not in MANUAL:   # palavra em maiúsculas (CARA DE CORUJA): fica em maiúsculas
            r2 = []
            n = M.token(w.lower(), r2)
            n = (_regras_finais(n) if n == w.lower() else n).upper()
            if n != w:
                rel.append((w, n, 'maiúsculas'))
            out.append(n)
        elif '-' in w and w in MANUAL:              # palavras com hífen decididas inteiras (ênclise, soletração)
            if MANUAL[w] != w:
                rel.append((w, MANUAL[w], 'manual'))
            out.append(MANUAL[w])
        else:
            n = M.token(w, rel)
            if n == w:
                n = _regras_finais(w)
                if n != w:
                    rel.append((w, n, 'regra'))
            out.append(n)
    return ''.join(out)


def _regras_finais(w):
    """O que o modernizador deixa sem par: superlativos e -ável/-ível sem acento (aborrecidissimo, aproveitavel)."""
    if re.search(r'[áéíóúâêôãõ]', w.lower()):
        return w
    n = re.sub(r'issim(o|a|os|as)$', r'íssim\1', w)
    n = re.sub(r'ISSIM(O|A|OS|AS)$', r'ÍSSIM\1', n)
    n = re.sub(r'(?<=[^aeiou])(av|iv)(el|eis)$', lambda m: {'av': 'áv', 'iv': 'ív'}[m.group(1)] + m.group(2), n)
    return n


def texto(t, rel):
    """Um parágrafo (ou bloco) inteiro; «porque» de pergunta → «por que»."""
    return M.por_que(linha(t, rel))


if __name__ == '__main__':
    import json
    from collections import Counter
    P = json.load(open(os.path.join(AQUI, '1931', 'paginas.json'), encoding='utf-8'))
    rel = []
    for n, v in sorted(P.items(), key=lambda x: int(x[0])):
        for b in v['texto'].split('\n\n'):
            texto(b, rel)
    cont = Counter((a, b, f) for a, b, f in rel)
    REL = os.path.expanduser('~/.cache/claude-pedidos-2611/reinacoes-de-narizinho/rel')
    os.makedirs(REL, exist_ok=True)
    with open(os.path.join(REL, 'grafia.tsv'), 'w', encoding='utf-8') as f:
        for (a, b, fo), c in sorted(cont.items(), key=lambda x: (x[0][2], x[0][0].lower())):
            f.write(f'{fo}\t{a}\t{b}\t{c}\n')
    print(Counter(f for _, _, f in rel))
    print(Counter(f for (_, _, f) in cont))
