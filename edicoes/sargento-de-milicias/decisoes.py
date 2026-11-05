"""Memórias de um Sargento de Milícias — decisões editoriais (EM ANDAMENTO: ver FALTA.md).

EMENDAS: intervenções no texto-base, na grafia de 1854–55: (tipo, trecho, troca)
  'erro'    erro tipográfico evidente da edição de 1854–55
  'ocr'     erro dos OCRs; o impresso traz a forma certa (conferido no fac-símile)
  'revisao' lição de 1854–55 conferida no fac-símile que o confronto perdeu
AJUSTES: depois da modernização, em tokens separados por espaço: (tipo, antes, de, para, depois)
MANUAL: grafia final de palavras que a edição de referência não resolve
TITULOS: os títulos dos capítulos (config.TITULOS), na grafia de hoje

conferencia.json: os pontos de revisao.py (o texto pronto contra a moderna) conferidos nas imagens de
1854–55. 'para' é o trecho como saiu do confronto (grafia de hoje), 'texto' a leitura certa; 'cod': ok (1854
confirma o texto), fix (erro dos OCRs), erro (erro tipográfico de 1854–55, corrigido e listado na «Sobre»),
ws (a moderna tem razão; 'texto' já traz a leitura dela). corrigir() aplica fix, erro e ws ao texto pronto.
"""
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'ferramentas'))
from edicao.tokens import TOK  # noqa: E402

_spec = importlib.util.spec_from_file_location('sm_config', os.path.join(os.path.dirname(__file__), 'config.py'))
_cfg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cfg)
TITULOS = dict(_cfg.TITULOS)

EMENDAS = [
    # leituras dos OCRs que o voto não corrigiu, conferidas no fac-símile (pranchas de 02/11, pontos 1–20)
    ('ocr', 'um sem numero do pontos', 'um sem numero de pontos'),
    ('ocr', 'certa Maria do hortaliça', 'certa Maria da hortaliça'),
    ('ocr', 'foi a honrai', 'foi a honra!'),
    ('ocr', 'arrependida doudicesde rapariga', 'arrependida..... doudices de rapariga'),
    ('ocr', 'e acahe-se tudo', 'e acabe-se tudo'),
    # pontos 41–62
    ('ocr', 'habitada por unia', 'habitada por uma'),
    ('ocr', 'talvez para ã cadê,', 'talvez para a cadêa...'),
    ('ocr', 'os industriosos ]', 'os industriosos!'),
    ('ocr', 'meirinho!.;. Nada', 'meirinho!... Nada'),
    # pontos 63–72
    ('ocr', 'eimaginouqueopequeno ajleria', 'e imaginou que o pequeno a teria'),
    ('ocr', 'Ciganos. Tinhãoesses meninos', 'Ciganos. Tinhão esses meninos'),
    # palavras que só os OCRs têm (relatorios/modernas.tsv), de correção evidente; a moderna arbitra
    ('ocr', 'eslevlado', 'este lado'),
    ('ocr', 'iembrasse', 'lembrasse'),
    ('ocr', 'com prelenções de', 'com pretenções de'),
    ('ocr', 'suas prelenções ou', 'suas pretenções ou'),
    ('ocr', 'mpito', 'muito'),
    ('ocr', 'imniunda', 'immunda'),
]

AJUSTES = []

MANUAL = {
    # formas de 1854 que a moderna, no mesmo ponto, não alinha 1:1
    'dansa': 'dança', 'dansão': 'dançam', 'dansavão': 'dançavam', "fizerão-n'a": 'fizeram-na', 'mudavão-se': 'mudavam-se',
    # resíduo evidente de OCR (relatorios/vocabulario.tsv: palavras que nenhuma edição moderna tem); a moderna arbitra
    'Leopardo': 'Leonardo', 'Leonardo-Pataça': 'Leonardo-Pataca', 'Jesé': 'José', 'Ob': 'Oh', 'abaridonado': 'abandonado',
    'ainigo': 'amigo', 'appareeer': 'aparecer', 'aqnellas': 'aquelas', 'assumplo': 'assunto', 'comsSgo': 'consigo',
    'conliverão-se': 'contiveram-se', 'consa': 'coisa', 'consas': 'coisas', 'digainos': 'digamos', 'ejla': 'ela',
    'emfini': 'enfim', 'eseravo': 'escravo', 'finalmgnte': 'finalmente', 'gue': 'que', 'hayia': 'havia',
    'incomniodava': 'incomodava', 'jue': 'que', 'mesino': 'mesmo', 'pelQ': 'pelo', 'possivei': 'possível',
    'prometlia': 'prometia', 'qfie': 'que', 'qjue': 'que', 'sugeilinho': 'sujeitinho', 'triumpbo': 'triunfo',
    'typq': 'tipo', 'utn': 'um', 'vizihança': 'vizinhança',
}


# grafia final de palavras que sobraram na forma de 1854 (o alinhamento com a moderna não as pegou), aplicada
# palavra a palavra ao texto pronto, depois da conferência. A 3ª do plural em -ão de tempo passado ou do
# presente vai a -am (o futuro, «verão», «estarão», fica)
FINAL = {
    'erão': 'eram', 'servião': 'serviam', 'Fazião-lhes': 'Faziam-lhes', 'deixavão': 'deixavam', 'tinhão': 'tinham',
    'darião': 'dariam', 'Caminhavão': 'Caminhavam', 'Chegárão': 'Chegaram', 'puzerão-se': 'puseram-se',
    'occupavão': 'ocupavam', 'atormentão': 'atormentam', 'acalmárão-se': 'acalmaram-se', 'estejão': 'estejam',
    'Valhão-me': 'Valham-me', 'Pensavão': 'Pensavam', 'cantavão-lhe': 'cantavam-lhe', 'postárão-sé': 'postaram-se',
    'Vejão': 'Vejam', 'vejão': 'vejam', 'estavaò': 'estavam',
    'Couces': 'Coices', 'couces': 'coices', 'pataças': 'patacas', 'bonanchona': 'bonachona', 'vestoria': 'vistoria',
    "d'el-rei": 'del-rei', 'conheco': 'conheço', 'cocou': 'coçou', 'açode': 'acode', 'afféçtos': 'afetos',
    'susurro': 'sussurro', 'forcada': 'forçada', '$': ';', 'desculpavel': 'desculpável', 'esconjurio': 'esconjúrio',
}

_ARQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conferencia.json')
CONFERENCIA = json.load(open(_ARQ, encoding='utf-8')) if os.path.exists(_ARQ) else []
ERROS = []                    # (capítulo, 1854–55, corrigido), para a «Sobre»
FALHAS = []


def _toks(s):
    out = []
    for parte in re.split(r'(¶)', s):
        out += ['¶'] if parte == '¶' else TOK.findall(parte)
    return out


ABREVIATURAS = {'Sr', 'Sra', 'Srs', 'Rev', 'Revma', 'Revmo', 'Vm', 'Vms', 'Vmcê', 'V', 'S', 'D', 'etc', 'N', 'Sto', 'Exa'}
SUJEIRA = {"'", '■', '•', '<', '>', '^', '}', '{', '|', '~', '*', '"', '„', '%'}
PONTUACAO = []                # (antes, depois) de cada limpeza, para conferir


def _pontuacao(out, flags):
    """Limpa a pontuação falsa dos OCRs, que nenhuma leitura de 1854 traz assim: sujeira solta («'», «•», «<»),
    ponto antes de minúscula (salvo abreviatura), pares impossíveis («.,», «,.», «.:», «?.», «,,»)."""
    PONTUACAO.clear()
    o, f = [], []
    for t, fl in zip(out, flags):
        if t in SUJEIRA:
            PONTUACAO.append((' '.join(o[-4:]), t))
            continue
        o.append(t); f.append(fl)
    out, flags = o, f
    fortes = {'?', '!', '?!', '!?'}
    # tokens de pontuação composta que o voto deixou («.,», «?.», «.:», «!,..»): reduzidos ao sinal plausível
    for i, t in enumerate(out):
        if len(t) < 2 or not re.fullmatch(r'[.,;:!?]+', t) or set(t) == {'.'}:
            continue
        if re.fullmatch(r'[!?]+\.*', t):
            continue
        c = out[i + 1] if i + 1 < len(out) else '¶'
        fim = c == '¶' or c.startswith('#') or c[:1].isupper() or c == '—'
        forte = ''.join(ch for ch in t if ch in '!?')
        pontos = re.search(r'\.{2,}$', t)
        if forte:
            novo = forte + (pontos.group(0) if pontos else '')
        elif ':' in t:
            novo = ':'
        elif ';' in t:
            novo = ';'
        else:
            novo = '.' if fim else ','
        PONTUACAO.append((' '.join(out[max(0, i - 3):i + 2]), novo))
        out[i] = novo
    # travessão repetido («— —»): um só
    o, f = [], []
    for t, fl in zip(out, flags):
        if t == '—' and o and o[-1] == '—':
            continue
        o.append(t); f.append(fl)
    out, flags = o, f
    i = 0
    while i < len(out) - 1:
        a, b = out[i], out[i + 1]
        c = out[i + 2] if i + 2 < len(out) else '¶'
        novo = None
        fim = c == '¶' or c.startswith('#') or c[:1].isupper() or c == '—'
        if a == ',' and b == ',':
            novo = ','
        elif {a, b} <= {'.', ','} and a != b:
            novo = '.' if fim else ','
        elif {a, b} in ({'.', ':'}, {',', ':'}):
            novo = ':'
        elif {a, b} in ({',', ';'}, {'.', ';'}):
            novo = ';'
        elif a in fortes and b in ('.', ','):
            novo = a
        elif a in (',', '.') and (b in fortes or b.startswith('!') or b.startswith('?')):
            novo = b
        elif a in fortes and b.startswith('..'):
            novo = a + b
        elif a == ',' and b.startswith('..'):
            novo = b
        if novo is not None:
            PONTUACAO.append((' '.join(out[max(0, i - 3):i + 3]), novo))
            out[i:i + 2] = [novo]
            flags[i:i + 2] = [flags[i]]
            continue
        if a == '.' and re.match(r'[a-zà-ú]', b) and i > 0 and out[i - 1] not in ABREVIATURAS and not out[i - 1].isdigit():
            PONTUACAO.append((' '.join(out[max(0, i - 3):i + 3]), ''))
            del out[i]; del flags[i]
            continue
        i += 1
    return out, flags


def corrigir(out, flags):
    """Aplica as leituras conferidas no fac-símile (conferencia.json): acha o trecho 'para' (no capítulo
    dele, se houver mais de um) e troca só o miolo que difere."""
    ERROS.clear()
    FALHAS.clear()
    # tokens que o tokenizador de hoje partiria («'OS»): partidos, para os trechos acharem o lugar
    o2, f2 = [], []
    for t, f in zip(out, flags):
        ps = [t] if (t.startswith('#') or t == '¶') else (_toks(t) or [t])
        if ps == ['.'] and o2 and set(o2[-1]) == {'.'}:          # «...» + «.» = «....»
            o2[-1] += '.'
            continue
        o2 += ps
        f2 += [f] * len(ps)
    out, flags = o2, f2
    caps, cap = {}, None
    for i, t in enumerate(out):
        if t.startswith('#'):
            cap = t[1:]
        caps[i] = cap
    for d in CONFERENCIA:
        if d['cod'] not in ('fix', 'erro', 'ws'):
            continue
        P = _toks(d['para'])
        C, ital, k = [], [], 0
        for t in _toks(d['texto']):              # _palavras em itálico_
            if t == '_':
                k ^= 1
                continue
            C.append(t)
            ital.append(bool(k))
        sem = [k for k, t in enumerate(out) if t != '¶']          # o trecho não conta as quebras de parágrafo
        plano = [out[k] for k in sem]
        n = len(P)
        achados = [i for i in range(len(plano) - n + 1) if plano[i:i + n] == P]
        if len(achados) > 1 and d.get('cap'):
            achados = [i for i in achados if caps.get(sem[i]) == d['cap']]
        if len(achados) != 1:
            m = len(C)
            ja = [i for i in range(len(plano) - m + 1) if plano[i:i + m] == C]
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
        ini = sem[i + a] if a < n else sem[i + n - 1] + 1
        fim = sem[i + n - z - 1] + 1 if n - z > a else ini
        novo = C[a:len(C) - z]
        velho = out[ini:fim]
        if '¶' in velho and '¶' not in novo:            # as quebras de parágrafo do miolo voltam no mesmo lugar
            import difflib
            vs = [t for t in velho if t != '¶']
            antes_de = set()
            k = 0
            for t in velho:
                if t == '¶':
                    antes_de.add(k)
                else:
                    k += 1
            mapa = {}
            for tp, i1, i2, j1, j2 in difflib.SequenceMatcher(None, vs, novo, autojunk=False).get_opcodes():
                for x in range(i1, i2):
                    mapa.setdefault(x, j1 + (x - i1 if tp == 'equal' else 0))
            mapa.setdefault(len(vs), len(novo))
            pos = sorted({min(mapa.get(x, len(novo)), len(novo)) for x in antes_de}, reverse=True)
            novo = list(novo)
            for j in pos:
                novo.insert(j, '¶')
        out = out[:ini] + novo + out[fim:]
        flags = flags[:ini] + [False] * len(novo) + flags[fim:]
        if any(ital):                           # o itálico vale para o trecho inteiro
            j = sem[i]
            while j < len(out) and out[j] == '¶':
                j += 1
            k = 0
            for x in range(j, len(out)):
                if k >= len(C):
                    break
                while k < len(C) and C[k] == '¶':
                    k += 1
                if out[x] == '¶' or k >= len(C):
                    continue
                if ital[k] and out[x][:1].isalpha():
                    flags[x] = True
                k += 1
        caps = {}
        cap = None
        for k, t in enumerate(out):
            if t.startswith('#'):
                cap = t[1:]
            caps[k] = cap
        if d['cod'] == 'erro':
            ERROS.append((d.get('cap'), d['para'], d['texto']))
    out = [FINAL.get(t, t) for t in out]
    # parágrafo que começaria por pontuação («¶ :»): a quebra vai para depois dela
    for i in range(len(out) - 1):
        if out[i] == '¶' and out[i + 1] in (',', ';', ':', '.'):
            out[i], out[i + 1] = out[i + 1], out[i]
            flags[i], flags[i + 1] = flags[i + 1], flags[i]
    out, flags = _pontuacao(out, flags)
    if FALHAS:
        print('conferência: correções sem lugar:', len(FALHAS), FALHAS[:8])
    return out, flags
