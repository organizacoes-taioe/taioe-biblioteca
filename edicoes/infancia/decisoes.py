"""Infância — decisões editoriais sobre o texto estabelecido.

EMENDAS: (tipo, busca, troca) na grafia do texto-base (tokens separados como no texto).
AJUSTES: (tipo, antes, de, para, depois) em tokens do texto já atualizado.
MANUAL: grafia atual de palavras que o léxico não resolve.

conferencia.json: cada ponto conferido nas imagens do fac-símile de 1947 (os desempates sem
maioria, os acentos, as palavras fora do léxico). 'de' é a leitura de 1933 ou de um OCR, 'para' é o texto como
saiu do confronto, 'texto' a leitura certa; 'cod': ok (1947 confirma o texto), g (só grafia),
fix (erro dos OCRs de 1947), erro (erro
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
    'quási': 'quase', 'Quási': 'Quase', 'quáSi': 'quase',          # quáSi: o S maiúsculo do OCR
    'excepção': 'exceção', 'facto': 'fato', 'dactilógrafa': 'datilógrafa', 'desinfectantes': 'desinfetantes',
    'sossêgo': 'sossego', 'Zêzinho': 'Zezinho', 'Zézinho': 'Zezinho',
    'Rio-Grande-do-Norte': 'Rio Grande do Norte',
    'bôjo': 'bojo', 'apôdo': 'apodo',
}

# palavras fora do léxico do sistema que são do texto (do autor, regionais, nomes, números), lidas na
# triagem: não vão para a conferência nas imagens (revisao.py)
LEXICO_OK = set('''
levantar-me-ei inteiriçado procurá-lo-ei encontrá-lo-ei tique-taque certificar-me-ei tiquetaquear
interminavelmente matracar comportar-me-ei desgraçou consertador margeando estravancavam vergar ventanista
papuda resplendores esboços Destrancou desembestadamente intrujão cristaleira descontentaria incisão formol
encatarroado friorento desdentadas desconchavou cadaverosas julgar-me-ei rebelar-me-ei aquietou negrejando
gemedeira rastejantes esfrangalhados emaranhar-se cipoais autoclave lavandaria maçadora fonfonar engelhou
réstias camisões neblinosa maçadores impacientei-me Curar-me-ei arrastar-me-ei habituar-me-ei amalucado
sacodem-me espojar-me arreliando-se remedando Henriqueta maçarocas coraçãozinho desembestou atenazou retinto
carrapinha sossegadinha zangadíssima desenxabido ciciando bicoradas arrelias dessorada pezunhava
locomover-se integralista debilmente esgueirou-se envesgou prosar encalacrada gordinho desatinar execranda
objurgatórias readquirira 1930 exprobrava-se mal-amanhado encanar enfileiravam empapuçados amofinar-se
cambavam sobraçando nádega bridar pedantes achatavam disparatou vergou carunchosas amacacado Zulmira
aperreação obscenidades leviandades achatavam-se cachos planeando achatar-se monologou reluzia
esgueirava-se despregar-se escorava-se desgrudavam despregara semelhava bugalho baboso morrinhenta
amodorrada desbotando humanidades macambúzio J Zezinho Engulhou frocado cameleão gorgolejala Massé massé
abat-jour 3º carunchoso moleca
1900 1905 1934 Agnelina Aquinos Bezerro-encourado Bonitona Cavalcantis Delfino Descurei Dondom Engelhou Engordou
Enverguei Escancharam-me Enfileiravam-se Inficionara-se Inhô Jacinta Loriano Maroca Notre-Dame Perispírito Propendia
Siqueiras Tenórios Tergiversei Versalhes aceiro achatava achatava-me achatava-se acocorando-se acocoravam acocorou-se
agoniava alfaia alfenim aluir aluí aluímos amofinava amunhecava ancoretas animalejo apaniguados aparatosa apojado
aprestos aquietasse aquietava arrebicava-se arrebiques arrenegou arrieiro arrieiros atenaza atenazar-me atenazavam
atroaria baldaria baldeava banguelo baralhava barbicachos barrote batecum baça beiral bezerro-encourado biliosa
bocejador bordos bossas branquejando brumosos bulhenta cabelinho cabeçotes caboré cachações cafusa calcinação
camaradagens camarinhas capinzais capulhos caraminholas carapinha carceragem careteando caridosamente carregação
cartonagem cartonagens carunchosa cascalhoso cassineta caçuás cerimoniosamente ceroulão charque chouto ciscador
comendadores contundente contundentes contusos cordõezinhos cruviana cueiros curtume cururus debruando debrum
desabalado desacordava desarranjos desarrumava desatinava desbotaram desbotava desbotavam desconcertantes
desconchavada desconchavando-se desconchavos desconversava desencapei-os desentocasse desentranhá-lo desfavorecia
desgraçadinhos despachos desparamentava desprecatar-me despregava despregá-la desprestigiar-me desprestigiou-se
destampatório destapava destrinçar desvariando diabinhos diferençando-me diferençando-se diletantes distilavam duelos
durezas efe emaranhavam-se emaranhei-me embiravam-se embirrei emboanças embuste empanzinada empenachados empoava-se
emproava-se encabulava encafuar-se encalacrara-se encalombada encanecida encangados encolerizava-se encompridando
encourado encourados encouravam encovados engelhavam engenhando engordado engrolada engrolei enleado enodoavam
ensanguentavam-se ensombravam ensossas ensossos entremeadas envergasse envesgava enxeriam-se epizootia escanchava-me
escoicear escorregos esfarinhado esfumara esfumava-se esfumavam-se esgoelar-se esgoelavam esgoelavam-se esgoelou
esgueirando-me esgueirava-me esgueiravam-se espanavam esquipador estazavam esteado estimativo estrepolias estridência
estrondava estrugiam estrumeira explanava fantasmagorias farpela fatiotas ferrabrás finava fluidificando-a
flós-santório franjadas frufru fubá fuliginoso fumacenta fumacentas furdunços fusca fustão fênico gabos gatimônias
gemente gogó gostosamente guabiru guinchinhos hirsutas homiziou-se idiotamente imodesta impacientavam impacientou
impacientou-se impudência inaudível incerimoniosos indecentemente inflexões inomináveis inquirição insultuosa
intratável irreconhecíveis jaça jitó jungiu ladeavam lanhos lassos latada lavandeiras lengalengas letrada liliputiana
limosas lugubremente lumes lusco-fusco malandravam malassombradas malva mandiga maneirosos mangassem maravalhas
marchante marujada matracava melros mercadejava mergulhões minguava monotonamente mordazes morim morrinhentas
mortificante moscazinha mosqueteiros motejos mussambê nauseavam-me negrita novelista obsessor obstinadamente oftalmia
ombreira ossuário ourela ouricuris pachorrentamente pachorrentas pacientemente pacotinhos paiol palmeirinha palrador
palradores palravam papangus parolando pardavasco percalina perispírito pesadume pessoinha pipilar pisaduras
pisunhando pitombas piões plumagem ponderoso ponderosos pospontos preparos prolegômenos propendia prosápias
pusilanimidade puía pústulas quezília quinzenário quiproquós quépi rabugice rapariguinha rascunhos raspadeira
reciprocavam reimosa rejeitos relho relhos repisando resmungos ressecava-se ressumando resvaladiço retalhista
retrogradei reverenciosos rinchos ringidoras ronrom rumoroso salesianos sanguinoso sapa sapequei silhão soba socavão
sovelas suadouros sujeitinho superfluidades supurantes surrões susceptibilizei suspeitosa teologais tepidez tesouravam
tilintantes tinadas tisna tisnada toldavam tormentosa torqueses torvos traslado tremelicavam trigais tropicavam
tropicões tufava tulha tulhas urupemas vaga-lumes vagabundagem variolosos venial verbosos vergando vergavam vergônteas
vinhedos viravoltas virgindades vultosas zebradas zigomas
ba be uia nenhuia tenteava balda revdma tunco empacavirados peruzinhos azinhavrada turíbulo efemérides
desempacavirei-o Estarrecia-me equitativamente escapole-se ignóbil zinguezagueava
bojo coriáceas esganiçava ininteligíveis apodo cache-nez piscos recompusera-se desgraçar torvas
'''.split())

# versos citados (em itálico em 1947, conferidos nas imagens; italico.py): o primeiro verso e quantos
# são. No texto vêm um por parágrafo; corrigir() junta o bloco (versos separados por «/») e põe o itálico
VERSOS_ITALICOS = [
    ('Acorde , seu papa ...', 1),
    ('Acorde , seu Papa-hóstia , Nos braços de ...', 2),
    ('Acorde , seu Papa-hóstia , Nos braços de Folgazona .', 2),
    ('Levante , seu Papa-hóstia , Dos braços de Folgazona . Outra emenda', 2),
    ('Levante , seu Papa-hóstia , Dos braços de Folgazona . Venha ver o papa-rato', 4),
    ('Acuda com todos os diabos .', 1),
    ('Eu nasci de sete meses ,', 4),
    ('Pedro Paulino , Leodoro , Loriano .', 3),
    ('Sapo cururu', 5),
    ('Assentei praça . Na polícia eu vivo', 4),
    ('Eu largo a farda , pego no capote ,', 2),
    ('Agora é tarde . Me recordo e penso . Trabalho imenso ...', 2),
    ('A letra A quer dizer', 6),
    ('Mestre piloto ,', 4),
    ('O capitão cheira a cravo ;', 4),
    ('Os olhos encovados e a postura', 2),
    ('Levante-se , Papa-hóstia .', 1),
    ('Levante , seu Papa-hóstia .', 1),
]
# outros trechos em itálico (conferidos nas imagens). (trecho, de, até): só os tokens trecho[de:até]
ITALICOS = [
    'Rougon-Macquart', 'Moço Louro', 'O Menino da Mata e o seu Cão Piloto', 'O Guarani', 'O Plebeu', 'Dilúculo',
    'Baladilhas', 'Romanceiro', 'Pequeno Mendigo', 'Casa de Pensão', 'O Coruja', 'Cenas da Vida Amazônica',
    'O Cortiço', 'Aquéda', 'incorrigível',
    ('do Guarani .', 1, 2), ('conservava O Sonho', 1, 3),
    ('tratamento de meu senhor', 2, 4), ('vários , meu senhor traduzia', 2, 4),
    ('tinha besouro como', 1, 2), ('terminava em barata', 2, 3),
    ('Tinha dito sim', 2, 3), ('a dizer não :', 2, 3), ('palavra auréola ,', 1, 2),
    ('muito o e de serviço , prosódia', 2, 3), ('muito o e de serviço , prosódia', 4, 5),
    ('sílaba de serviço quando', 2, 3),
    ('— Cabra-cega ! ¶ — Inhô . ¶ — Donde vem ? ¶ — Do mundéu .', 0, 19),
    ('— Traz ouro ou prata ? ¶ — Ouro .', 0, 10),
]

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
    for item in ITALICOS:
        trecho, desde, ate = (item, 0, None) if isinstance(item, str) else item
        P = _toks(trecho)
        ate = len(P) if ate is None else ate
        achados = [i for i in range(len(out) - len(P) + 1) if out[i:i + len(P)] == P]
        if not achados:
            FALHAS.append(('itálico', trecho, len(achados)))
            continue
        for a in achados:                           # todas as vezes («Qui se ressemble» vem duas)
            for k in range(a + desde, a + ate):
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
