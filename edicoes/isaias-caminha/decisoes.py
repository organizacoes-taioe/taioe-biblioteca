"""Recordações do Escrivão Isaías Caminha — decisões editoriais.

EMENDAS: intervenções no texto-base, na grafia de 1917: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1917 (ou corrigido pela errata do próprio volume)
  'ocr'     erro das leituras; o impresso de 1917 traz a forma certa (conferido no fac-símile)
  'revisao' lição de 1917 conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que as edições de referência não resolvem
Os pontos conferidos no fac-símile que o voto decide ficam em conferencia.json (ver config.rever).
"""

EMENDAS = [
    # a errata do próprio volume de 1917 (p. [235]): «veio» por «vinha», «deserrollar-se» (a errata dá a forma
    # errada igual à certa, «desenrolar-se»); as outras três («attendia», «dissolver-se», «diminuiu-lhe») o
    # confronto já trouxe corrigidas: ver notas.ERROS_ANTERIORES
    ('erro', "uma vez ou outra, veio perturbar", "uma vez ou outra, vinha perturbar"),
    ('erro', "algo de grave deserrollar-se", "algo de grave desenrolar-se"),
    # linhas que a composição de 1917 perdeu, completadas pela 1ª edição (1909)
    ('erro', "engrossadores com as, a senhora", "engrossadores com as suas mulheres e filhas encontravam-se alli em "
             "tocantes despedidas a amigos das duas camaras. A viscondessa de Varennes, a famosa Odalina, poetisa de "
             "muito merito e tão do gosto de Floc, viera tambem. O dr. Ricardo afastou-se logo d'ella com a senhora"),
    ('erro', "com um engenhoso aptablado de magica", "com um engenhoso apparelho de apparições e eclipses, especie "
             "complicada de tablado de magica"),
    # erros tipográficos evidentes de 1917 (conferidos no fac-símile; quase todos ausentes de 1909)
    ('erro', "creio descobrir descobrir alguma", "creio descobrir alguma"),
    ('erro', "escrever alguma verrinas", "escrever algumas verrinas"),
    ('erro', "estava em nós, na na nossa", "estava em nós, na nossa"),
    ('erro', "entre vinte cinco ou", "entre vinte e cinco ou"),
    ('erro', "das suas biographicas heroicas", "das suas biographias heroicas"),
    ('erro', "Sendo obrigado obrigado a", "Sendo obrigado a"),
    ('erro', "responder Plinio — Pagou sim, apressou-se em responder Plinio de Andrade", "responder Plinio de Andrade"),
    ('erro', "me convidada a jantar", "me convidava a jantar"),
    ('erro', "esperava essa perguntou", "esperava essa pergunta"),
    ('erro', "ou em pelotiqueiro", "ou um pelotiqueiro"),
    ('erro', "recitar versos na salas", "recitar versos nas salas"),
    ('erro', "encontrados ortos a facadas", "encontrados mortos a facadas"),
    ('erro', "dez horas eu recebera", "dez horas e eu recebera"),
    ('erro', "para o fortuna do dr", "para a fortuna do dr"),
    ('erro', "Fomos a una venda", "Fomos a uma venda"),
    ('erro', "de força. alvez se sentisse", "de força. Talvez se sentisse"),
    ('erro', "tudo aquillo á ser lido", "tudo aquillo ia ser lido"),
    ('erro', "de fraqueza, de décisão é mais", "de fraqueza, de decisão e mais"),
    ('erro', "ferir a marmellada", "ferir a martellada"),
    ('erro', "do que por quer outra", "do que por qualquer outra"),
    ('erro', "me venham ar sensações", "me venham as sensações"),
    ('erro', "parecia ser em homem rico", "parecia ser um homem rico"),
    ('erro', "arqueologia, e muita certa", "arqueologia, e muito certa"),
    ('erro', "debaixo das nações livrescas", "debaixo das noções livrescas"),
]

AJUSTES = [
]

MANUAL = {
    # formas antigas de palavras atuais (as edições de referência não dão o par)
    'cousa': 'coisa', 'cousas': 'coisas', 'Cousa': 'Coisa', 'dous': 'dois', 'bebedo': 'bêbedo',
    # abreviaturas da época (a edição moderna as desdobra)
    'dr': 'dr', 'Dr': 'Dr', 'Sr': 'Sr', 'sr': 'sr', 'snr': 'snr', 'Snr': 'Snr', 'srs': 'srs', 'Srs': 'Srs',
    'D': 'D', 'S': 'S', 'Ex': 'Ex', 'V': 'V', 'C': 'C', 'Club': 'Club',
    # o português do séc. XV da «Ensynança de Bem Cavalgar», citado no cap. XIV: fica como impresso
    'Ensynança': 'Ensynança', 'alguũs': 'alguũs', 'boos': 'boos', 'cavalgadores': 'cavalgadores', 'dũas': 'dũas',
    'sellas': 'sellas', 'queo': 'queo', 'nom': 'nom', 'som': 'som', 'doutras': 'doutras', 'Ca': 'Ca',
}

import os  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ferramentas'))
from edicao.tokens import TOK  # noqa: E402

# nomes uniformizados (revisao.json, «loberant»): 1909 e 1917 imprimem «Leborant» do cap. IX em diante
NOMES = {'Leborant': 'Loberant', 'Leborante': 'Loberant'}

# versos citados que o texto moderno compõe um por parágrafo: (começo do 1º verso, número de versos)
VERSOS_BLOCOS = [('Quando ele se viu sozinho', 4)]

# trechos em itálico em 1917 (conferidos nas imagens); (trecho, de, até): só os tokens trecho[de:até]
ITALICOS = [
    'donnée', 'footing', ('Veio-me a pose', 2, 3), 'Poder da Vontade', 'Xerez', 'peppermint', 'guichet', 'pince-nez',
    'toilettes', 'Peço a palavra para uma explicação pessoal.', 'Tem a palavra o Snr. Carlos Barromeu.', 'Sonâmbula',
    'restaurant', 'charge', '(mudou logo de tratamento)', 'coisa-feita', 'estava mudo e só na rocha de granito?',
    'é o triunfo imortal da carne e da beleza?', 'Gazeta! País! Jornal do Comércio!', 'carrousel', 'Diário Fluminense',
    'condottiere', 'o valente filho de «Bayard» e «Ninive»', 'a vitoriosa pensionista do «stud» S. Francisco',
    'Aplomb Club', 'et reliqua', 'clichés', 'cliché', 'pesados 200$000 impostos pelo Congresso', '200 ovos postos pelo Congresso',
    'plaquette', 'Eis aqui um caso singular, e que desnorteia os princípios geralmente admitidos em hereditariedade.',
    'filho de peixe sabe nadar; quem sai aos seus não degenera', 'Quem tem amores vai dormir', 'e dinheiro não virá',
    'squares', 'Foram concedidos passes aos telegrafistas', 'Descampado da morte', 'complot', 'gauloiseries',
    "Vous m'en direz tant", 'Anthropométrie', 'desta nossa forte geração moderna, que sabe aliar o saber e a simplicidade',
    'era uma tenda de trabalho onde mourejavam irmãos', 'uma tenda de trabalho onde mourejam irmãos',
    'de grão em grão a galinha enche o papo', "petit à petit l'oiseau fait son nid", 'Colocação dos Pronomes; teoria e prática',
    'claque', 'mutatis mutandis', 'quitute', 'sui generis', 'atrabílis', 'cotillon', 'procure-me em casa',
    'aqui não lhe posso atender', 'frutos do jardim do mundo', 'noblesse oblige', 'Moulin-Rouge', 'Ensynança de Bem Cavalgar',
    'Ca som alguũs boos cavalgadores dũas sellas queo nom som doutras', 'chanteuse', 'baccarat', 'menu', 'verve',
]

TROCAS_NOMES = []
DIC = set()
NOMES_COMUNS = {'Estado', 'Senhor', 'Senhora', 'Dona', 'Rua', 'Largo', 'Deus', 'Imprensa', 'Presidente', 'Ministro',
                'Coronel', 'Câmara', 'Congresso', 'Diretor', 'República', 'Escrivão', 'Almirante', 'Capitão', 'Doutor'}


def _toks(s):
    return TOK.findall(s)


ACENTOS = {}
ACENTOS_TROCADOS = []
# palavras que ficam sem o acento que o dicionário sugere (estrangeiras, nomes)
SEM_ACENTO = {'restaurant', 'reporters', 'reporter', 'toilettes', 'toilette', 'baccarat', 'menu', 'Floc', 'Leiva', 'Laje'}


# trocas conferidas uma a uma na lista que _acentos() propõe (as outras propostas eram erradas: pôde, àquela...)
ACENTOS_OK = {a: b for a, b in (
    ('prestigio', 'prestígio'), ('oficio', 'ofício'), ('espirito', 'espírito'), ('juizes', 'juízes'), ('circulo', 'círculo'),
    ('distancia', 'distância'), ('varias', 'várias'), ('policia', 'polícia'), ('silabas', 'sílabas'),
    ('desnecessario', 'desnecessário'), ('literario', 'literário'), ('veiculo', 'veículo'), ('vicio', 'vício'),
    ('beneficio', 'benefício'), ('virgulas', 'vírgulas'), ('atras', 'atrás'), ('substancia', 'substância'),
    ('tambem', 'também'), ('secretario', 'secretário'), ('paginas', 'páginas'), ('cientifico', 'científico'),
    ('historia', 'história'), ('mingua', 'míngua'), ('viamos', 'víamos'), ('priamo', 'príamo'), ('avancava', 'avançava'),
    ('preguicosa', 'preguiçosa'), ('comecamos', 'começamos'), ('atraiam', 'atraíam'), ('atraia', 'atraía'),
    ('saira', 'saíra'), ('forca', 'força'), ('observacões', 'observações'), ('ocasiào', 'ocasião'), ('políciais', 'policiais'),
    ('critíca', 'crítica'), ('tólstoi', 'tolstói'), ('sófia', 'sofia'), ('términus', 'terminus'), ('marques', 'marquês'),
    ('açhas', 'achas'), ('noticia', 'notícia'), ('noticias', 'notícias'), ('titulo', 'título'), ('titulos', 'títulos'),
    ('intimo', 'íntimo'))}
AMBIGUAS = {'critica': 'crítica', 'criticas': 'críticas', 'intima': 'íntima', 'intimo': 'íntimo', 'intimas': 'íntimas',
            'intimos': 'íntimos', 'baia': 'baía', 'pratica': 'prática', 'praticas': 'práticas', 'duvida': 'dúvida',
            'duvidas': 'dúvidas', 'continuo': 'contínuo', 'continuos': 'contínuos', 'critico': 'crítico',
            'criticos': 'críticos', 'publico': 'público', 'publica': 'pública', 'publicos': 'públicos', 'publicas': 'públicas'}
DETERMINANTES = {'a', 'as', 'o', 'os', 'da', 'das', 'do', 'dos', 'na', 'nas', 'no', 'nos', 'uma', 'umas', 'um', 'uns',
                 'sua', 'suas', 'seu', 'seus', 'minha', 'minhas', 'meu', 'meus', 'pela', 'pelas', 'pelo', 'pelos',
                 'esta', 'essa', 'aquela', 'à', 'às', 'de', 'em', 'com', 'sem', 'por', 'para', 'que', 'outra', 'qualquer',
                 'tal', 'cada', 'nenhuma', 'alguma', 'grande', 'boa', 'e', 'numa', 'num', 'duma', 'dum', 'este', 'esse', 'aquele', 'ao', 'aos'}


def _acentos():
    """Forma acentuada mais comum nos outros livros da Biblioteca (já na grafia de hoje), pela forma sem
    acento: a edição moderna de referência (Ática, pela BVEB) perdeu muitos acentos («noticia», «titulo»,
    «espirito»). Vale quando a acentuada é ao menos 5 vezes mais frequente que a forma do texto."""
    if not ACENTOS:
        import glob
        import unicodedata
        from collections import Counter
        sem = lambda w: ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
        raiz = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'conteudo')
        n = Counter()
        for f in glob.glob(os.path.join(raiz, '*', '*.js')):
            if os.path.basename(f) == 'isaias-caminha.js':
                continue
            n.update(w.lower() for w in re.findall(r'[^\W\d_]+', open(f, encoding='utf-8').read()))
        melhor = {}
        for w, c in n.items():
            k = sem(w)
            if c > melhor.get(k, ('', 0))[1]:
                melhor[k] = (w, c)
        ACENTOS.update({'n': n, 'melhor': melhor, 'sem': sem})
    return ACENTOS


def corrigir(out, flags):
    """Sobre o texto pronto (grafia de hoje): acentos perdidos pela referência, nomes uniformizados, blocos
    de versos e itálicos."""
    out, flags = list(out), list(flags)
    ACENTOS_TROCADOS.clear()
    for i, t in enumerate(out):
        low = t.lower()
        if low in AMBIGUAS:                 # verbo ou nome: nome depois de artigo, possessivo ou preposição
            w = AMBIGUAS[low]
            if low.startswith('contínu'.replace('í', 'i')):
                if out[i - 1].lower() == 'eu':
                    continue
            elif out[i - 1].lower() not in DETERMINANTES:
                continue
        elif low in ACENTOS_OK:
            w = ACENTOS_OK[low]
        else:
            continue
        novo = w[0].upper() + w[1:] if t[0].isupper() else w
        ACENTOS_TROCADOS.append((t, novo))
        out[i] = novo
    # vírgula lida no lugar do ponto antes de palavra comum em maiúscula («sem origens, Que mal havia»)
    if not DIC:
        DIC.update(l.strip() for l in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore') if l.strip())
    for i in range(1, len(out) - 1):
        prox = out[i + 1].split('-')[0]
        if (out[i] == ',' and out[i - 1][:1].isalpha() and prox[:1].isupper() and len(prox) > 1 and prox.lower() in DIC
                and prox not in DIC and prox not in NOMES_COMUNS):
            out[i] = '.'
    TROCAS_NOMES.clear()
    for i, t in enumerate(out):
        if t in NOMES:
            TROCAS_NOMES.append(t)
            out[i] = NOMES[t]
    for primeiro, n in VERSOS_BLOCOS:
        P = _toks(primeiro)
        achados = [i for i in range(1, len(out) - len(P)) if out[i - 1] == '¶' and out[i:i + len(P)] == P]
        if len(achados) != 1:
            raise SystemExit(f'versos {primeiro!r}: {len(achados)} ocorrências')
        i, k = achados[0], 1
        while k < n:
            i += 1
            if out[i] == '¶':
                out[i] = '/'
                k += 1
    falhas = []
    for item in ITALICOS:
        trecho, desde, ate = (item, 0, None) if isinstance(item, str) else item
        P = _toks(trecho)
        ate = len(P) if ate is None else ate
        achados = [i for i in range(len(out) - len(P) + 1) if out[i:i + len(P)] == P]
        if not achados:
            falhas.append(trecho)
        for a in achados:
            for k in range(a + desde, a + ate):
                flags[k] = flags[k] or out[k][:1].isalpha()
    if falhas:
        print('itálicos sem lugar:', falhas)
    return out, flags
