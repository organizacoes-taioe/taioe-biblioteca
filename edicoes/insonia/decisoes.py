"""Insônia — decisões editoriais sobre o texto estabelecido.

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
'''.split())

# versos citados (em itálico em 1947, conferidos nas imagens; italico.py): o primeiro verso e quantos
# são. No texto vêm um por parágrafo; corrigir() junta o bloco (versos separados por «/») e põe o itálico
VERSOS_ITALICOS = []
# outros trechos em itálico em 1947 (conferidos nas imagens)
# (trecho, de, até): só as palavras trecho[de:até] (em tokens) vão em itálico, ali; texto puro = todas
ITALICOS = ['Diário Oficial', ('sentido exato de legião', 3, 4),
            ('dissera não quando era preciso dizer sim', 1, 2), ('dissera não quando era preciso dizer sim', 6, 7)]

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
