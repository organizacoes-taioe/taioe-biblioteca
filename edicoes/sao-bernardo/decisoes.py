"""São Bernardo — decisões editoriais sobre o texto estabelecido.

EMENDAS: (tipo, busca, troca) na grafia do texto-base (tokens separados como no texto).
AJUSTES: (tipo, antes, de, para, depois) em tokens do texto já atualizado.
MANUAL: grafia atual de palavras que o léxico não resolve.

conferencia.json: cada ponto conferido nas imagens do fac-símile de 1947 (as mudanças sobre 1934 e
os desempates sem apoio). 'de' é 1934, 'para' é o texto como saiu do confronto, 'texto' a leitura
certa; 'cod': ok (1947 confirma), g (só grafia), ws (erro do Wikisource em 1934), fix (erro dos
OCRs), erro (erro tipográfico de 1947, corrigido e listado), ital (itálico de 1947), v, v34, ver
(a conferir). corrigir() aplica fix, erro e ital ao texto pronto.
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
    'excepção': 'exceção', 'Safadissimo': 'Safadíssimo', 'Job': 'Jó',
    'ss': 'ss',                                   # os «ss» de d. Marcela (sem isto viram «s»)
    'embirra': 'embirra', 'escoram': 'escoram', 'arear': 'arear', 'ahi': 'aí',   # o léxico não as tem
    # OCR que o confronto não resolveu (conferido no fac-símile)
    'macador': 'maçador', 'crianca': 'criança', 'Penseique': 'Pensei que',
}

CONFERENCIA = json.load(open(os.path.join(AQUI, 'conferencia.json'), encoding='utf-8'))
ERROS = []                    # (capítulo, 1947, corrigido), para notas.ERROS_ANTERIORES
FALHAS = []                   # correções que não acharam o lugar (para rever)


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
    if FALHAS:
        print('conferência: correções sem lugar:', FALHAS)
    return out, flags
