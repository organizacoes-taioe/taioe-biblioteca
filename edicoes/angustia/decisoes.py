"""Angústia — decisões editoriais sobre o texto estabelecido.

EMENDAS: (tipo, busca, troca) na grafia do texto-base (tokens separados como no texto).
AJUSTES: (tipo, antes, de, para, depois) em tokens do texto já atualizado.
MANUAL: grafia atual de palavras que o léxico não resolve.

conferencia.json: cada ponto conferido nas imagens do fac-símile de 1947 (as diferenças entre as
provas de 1946 e 1947, e os desempates sem apoio). 'de' é a leitura das provas, 'para' é o texto como
saiu do confronto, 'texto' a leitura certa; 'cod': ok (1947 confirma: correção do autor nas provas),
g (só grafia), p (erro de leitura das provas: não é mudança), fix (erro dos OCRs de 1947), erro (erro
tipográfico de 1947, corrigido e listado), ital (itálico de 1947), ver (a conferir). corrigir() aplica
fix, erro e ital ao texto pronto.
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'ferramentas'))
from edicao.tokens import TOK  # noqa: E402

EMENDAS = []

AJUSTES = []

MANUAL = {
    'quási': 'quase', 'Quási': 'Quase',
    'sossêgo': 'sossego',                         # o léxico do sistema não tem a forma de hoje
    'Escorei-me': 'Escorei-me',                   # o esqueleto a tomava por «escorrer»
}

# palavras fora do léxico do sistema que são do texto (do autor, regionais, nomes, números), lidas na
# triagem de 2026-10-26: não vão para a conferência nas imagens (revisao.py)
LEXICO_OK = set('''
1910 1911 384 Acanhei-me Aporrinhações Aquietava-se Basbaques Bichinha Cia Corrote Derreei-me
Encabulei Encolerizei-me Engrola Escanzelada Escapole-se Esmolambado Fusuês Good-bye Gritinhos
Grunhi Hi Impacientei-me Inteiriçava-me Lambisgoia Monturos Pfu Pst Repisava Rosália Sirigaita
Vossemecês abancava acaboclado acanalhada acanhei-me acavalados acavalavam achatar-me achatar-me-ia
achatar-se achataria acocorar-se acocorara acocorara-se acocorava-se acocorei-me aduelas afogueada
afogueava agadanhar agatanhavam alagoanas alagoanos alatoados alemãzinha almocreves amanhadas
amolegações amorrinhava-lhe amunhecando apalermado aperrado aperre apoquentações aporrinhava-me
aporrinhações aquietava-se arengava arquejante arreliada arribação atarantam atenazavam-me atocaiava
atraçadas azucrinante bagaceira balãozinho bambeante barbinha basbaque baças beicinho bichinha
bilioso biqueiras bisaco bochechos bodejando bordões bruscamente bueira bureau béri-béri bípede
bípedes cabelinhos cachenê cacoetes caitetu caitetus calceteiros cambados camisão capitel capueiras
capulho carapanás carapanãs carocinhos carolinas carrapeta casse-tête catitas caçoleta certinha
chauffeur chauffeurs chegança chiadeira chichichi chimbo chinfrim choramigar chupões cintado
cintados clavinote contra-sensos coqueirais cornear correntinha correntão corrote crispada crispados
crótons dengues derreados desacatar desamassado desasnar desbragadíssima descangotar descompô-la
desconchavo descontenta-se descontentara-a descontentes desdentada desembesta desentoquei-me
desgraçam desmedidamente desprecatada despregado despropositava despropositei destambocou destampar
destorcia-se diatribes discursador dispéptico dobrão doidices dorna dornas dístico embaciados
embebedar-me embeiçada embicado embiocados emboléus empacaviradas empapuçadas empastou-se empatou
emproava-se empáfia encafuava-se encalacrar-me encalistrada encandeado encanecido encaroçado
encastoado encatarroada enchumaçada encolerizar-me encolerizei-me encolerizou-me enfrenesiava
engelhada engelhado engordando engulhando engulhava engulhos enrijasse enrodilhadas ensombra
ensombrando entocado entrapada entrouxa entrouxada entufada envergavam enxeria-se enxerida enxofrada
esbagaçado esbagaçando escabujar escalavradas escanchada escrevedor escuridões esfoladura
esgaravatar esgueirou-se esmolambado espojado espojar-me espojava-se esquentamento esquipava
estarreceu-me estazando-se estertorosa estiava estrangeirada esturrasse esverdinhando-se
exprobrações feixinho ferragem fininha florinhas fornidas fossando franga frege frege-moscas
friorenta frontaria fumacento fundilhos fusuês galicada ganzá garlopa garçon gatimanhos gluglu goma-
arábica gorgolejados gorgolejar gorgolejo grelando gretados gritinhos grunhi grunhia grunhindo
guenza guindar hall himeneu horrivelmente impando impava imundícies indignidade indignidades
infindável inquilina insubstituíveis inteirinha inteiriçavam-se inverídica ioiô joalharia juá
lambanças lazarinas lembrancinha loquacidade lorgnon lúbricos macambúzios madorna malotes mamulengo
mangasse mangava manzanzando marginavam marquesão membrudo mergulhos minguar monologando
monstruosidades monturo monturos mulherona mulherão muques ofegava ofertantes opalinos paina
palacetes papaco papelinhos papudas papudo papudos parafusou parolar passinhos passivamente pecúnia
peganhenta peignoir peitilho pejando pelega peleiro pererê perfilados pernão pinguinhos piongos
pipiri pontinhas postigos prenha putaria puídas puídos pândega queixume quibas quixabeiras quépis
ran ratuína recomposta reisado reisados retocava ringindo risadinha robe rompantes rr rufos
ruindades salamaleques salpicos sapataria sapateava sapateou sapecando sapecava sapeco sarjando sem-
vergonheza sem-vergonhezas sinecura sirigaita smoking sobrenome sorrisinho sujidade surucucus sururu
tabaqueiro tacões taludinha tangerinos tarimbas telheiro tipa tipinha tique-taque tisnado tisnados
toldando trabalhinho tremeliques treponema tresvariar trombuda três-setes vascolejar vasqueiros
verbiagem vergaram vergões vermelhaça virgindade visagens vuco xente xerém xiquexique zambeta
zebravam
'''.split())

# versos citados (em itálico em 1947, conferidos nas imagens; italico.py): o primeiro verso e quantos
# são. No texto vêm um por parágrafo; corrigir() junta o bloco (versos separados por «/») e põe o itálico
VERSOS_ITALICOS = [
    ('Assentei praça. Na polícia eu vivo', 2),
    ('Currupaco, papaco. A mulher do macaco Ela fia', 5),
    ('Currupaco, papaco. A mulher do macaco...', 2),
    ('Liberdade, liberdade,', 2),
    ('Minha santa Margarida,', 4),
]
# outros trechos em itálico em 1947 (conferidos nas imagens)
ITALICOS = ['ar, mar, rima, arma, ira, amar', 'Ar, mar, ria, arma, ira', 'aquele boa noite']

CONFERENCIA = json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8'))
ERROS = []                    # (capítulo, 1947, corrigido), para notas.ERROS_ANTERIORES
FALHAS = []                   # correções que não acharam o lugar (para rever)
VIRGULAS = []                 # vírgulas de fim de parágrafo trocadas por ponto


def _toks(s):
    out = []
    for parte in re.split(r'(¶)', s):
        out += ['¶'] if parte == '¶' else TOK.findall(parte)
    return out


def _limpo(ts):
    return [t for t in ts if t != '_']


def corrigir(out, flags):
    """Aplica as leituras conferidas no fac-símile. Procura o trecho inteiro de 'para' no texto (no
    capítulo dele, se houver mais de um); só troca o miolo que difere."""
    ERROS.clear()
    FALHAS.clear()
    VIRGULAS.clear()
    o2, f2 = [], []                   # pontos soltos seguidos («.», «.») viram um token só («..»)
    for t, f in zip(out, flags):
        if t.startswith('.') and set(t) == {'.'} and o2 and o2[-1].startswith('.') and set(o2[-1]) == {'.'}:
            o2[-1] += t
            continue
        o2.append(t); f2.append(f)
    out, flags = o2, f2
    caps = {}
    cap = None
    for i, t in enumerate(out):
        if t.startswith('#'):
            cap = t[1:]
        caps[i] = cap
    for d in CONFERENCIA:
        if d['cod'] not in ('fix', 'erro', 'ital'):
            continue
        P = _toks(d['para'])
        C = _toks(d['texto'])
        ital = [False] * len(C)
        k, C2 = 0, []
        for t in C:                         # _palavras em itálico_
            if t == '_':
                k ^= 1
                continue
            C2.append(t)
            ital.append(bool(k))
        ital = ital[len(C):]
        C = C2
        n = len(P)
        achados = [i for i in range(len(out) - n + 1) if out[i:i + n] == P]
        if len(achados) > 1 and d['cap']:
            achados = [i for i in achados if caps.get(i) == d['cap']]
        if len(achados) != 1:
            m = len(C)
            ja = [i for i in range(len(out) - m + 1) if out[i:i + m] == C]
            if not ja:
                FALHAS.append((d['id'], d['para'], len(achados)))
            continue
        i = achados[0]
        a = 0
        while a < min(n, len(C)) and P[a] == C[a]:
            a += 1
        z = 0
        while z < min(n, len(C)) - a and P[n - 1 - z] == C[len(C) - 1 - z]:
            z += 1
        novo = out[:i + a] + C[a:len(C) - z] + out[i + n - z:]
        nf = flags[:i + a] + [False] * (len(C) - z - a) + flags[i + n - z:]
        for k, it in enumerate(ital):        # o itálico vale para o trecho inteiro
            if it:
                nf[i + k] = True
        out, flags = novo, nf
        if d['cod'] == 'erro':
            ERROS.append((d['cap'], d['para'], d['texto'].replace('_', '')))
    out, flags = _versos(out, flags)
    # «Às vezes» no começo da frase: o OCR perde o grave (o livro sempre o traz)
    for i in range(len(out) - 1):
        if out[i] == 'As' and out[i + 1] == 'vezes' and (i == 0 or out[i - 1] in ('.', '!', '?', '¶', '—', '…')):
            out[i] = 'Às'
    # número com ponto de milhar («16.384») ou ordinal («1.º»): o tokenizador o parte em três
    i = 0
    while i < len(out) - 2:
        if out[i].isdigit() and out[i + 1] == '.' and (re.fullmatch(r'\d{3}', out[i + 2]) or out[i + 2] == 'º'):
            out[i:i + 3] = [out[i] + '.' + out[i + 2]]
            flags[i:i + 3] = [False]
        i += 1
    # vírgula no fim de parágrafo é o ponto mal lido pelo Tesseract
    for i in range(len(out) - 1):
        if out[i] == ',' and (out[i + 1] == '¶' or out[i + 1].startswith('#')):
            out[i] = '.'
            VIRGULAS.append(' '.join(out[max(0, i - 5):i + 1]))
    for trecho in ITALICOS:
        P = _toks(trecho)
        if trecho.startswith('aquele '):            # só «boa noite» vai em itálico
            P, desde = P, 1
        else:
            desde = 0
        achados = [i for i in range(len(out) - len(P) + 1) if out[i:i + len(P)] == P]
        if len(achados) != 1:
            FALHAS.append(('itálico', trecho, len(achados)))
            continue
        for k in range(achados[0] + desde, achados[0] + len(P)):
            flags[k] = flags[k] or out[k][:1].isalpha()
    if FALHAS:
        print('conferência: correções sem lugar:', FALHAS)
    return out, flags


def _versos(out, flags):
    """Junta em bloco os versos de VERSOS_ITALICOS (um por parágrafo no texto) e os põe em itálico."""
    for primeiro, n in VERSOS_ITALICOS:
        P = _toks(primeiro)
        # o bloco começa num parágrafo novo; os versos seguintes também (¶ entre eles)
        sem = [t for t in P]
        achados = []
        for i in range(len(out)):
            if out[i - 1] != '¶':
                continue
            j, k = i, 0
            while k < len(sem) and j < len(out):
                if out[j] == '¶':
                    j += 1
                    continue
                if out[j] != sem[k]:
                    break
                j += 1; k += 1
            if k == len(sem):
                achados.append(i)
        if len(achados) != 1:
            FALHAS.append(('versos', primeiro, len(achados)))
            continue
        i = achados[0]
        vistos, j = 0, i
        while j < len(out) and vistos < n:
            if out[j] == '¶':
                vistos += 1
                if vistos < n:
                    out[j] = '/'
            elif out[j][:1].isalpha():
                flags[j] = True
            j += 1
    return out, flags
