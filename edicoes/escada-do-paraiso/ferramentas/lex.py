"""Léxico grego e correção de palavras do OCR por troca de letras que o Tesseract confunde na PG."""
import json, os, re, unicodedata, functools
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
_LEX = None
GRAVE = '̀'; AGUDO = '́'

def chave(w):
    d = unicodedata.normalize('NFD', w.lower()).replace(GRAVE, AGUDO)
    # enclítica: dois agudos → tira o segundo
    if d.count(AGUDO) + d.count('͂') > 1:
        i = max(d.rfind(AGUDO), -1)
        d = d[:i] + d[i + 1:]
    return unicodedata.normalize('NFC', d.replace('ς', 'σ'))

def lex():
    global _LEX
    if _LEX is None:
        _LEX = {}
        arqs = ['lex-f1k-todo.json' if os.path.exists(os.path.join(AQUI, 'lex-f1k-todo.json')) else 'lex-f1k.json', 'lex-pers.json']
        for a in arqs:
            if not os.path.exists(os.path.join(AQUI, a)): continue
            for w, n in json.load(open(os.path.join(AQUI, a), encoding='utf-8')).items():
                k = chave(w); _LEX[k] = _LEX.get(k, 0) + n
        extra = os.path.join(AQUI, 'lex-extra.json')   # formas aceitas na conferência
        if os.path.exists(extra):
            for w in json.load(open(extra, encoding='utf-8')): _LEX[chave(w)] = _LEX.get(chave(w), 0) + 5
    return _LEX

def freq(w):
    return lex().get(chave(w), 0)

# trocas (base sem diacríticos): o Tesseract lê κ como χ, β como δ/6, υ como υ/ν etc.
TROCAS = {'χ': 'κ', 'κ': 'χ', 'δ': 'β', 'β': 'δ', 'ν': 'υ', 'υ': 'ν', 'ο': 'σ', 'σ': 'ο', 'ε': 'ς', 'ρ': 'ϱ', 'η': 'ῃ', 'ζ': 'ξ', 'ξ': 'ζ', 'θ': 'ϑ', 'ϑ': 'θ', 'ϐ': 'β', 'π': 'τ', 'τ': 'π', 'γ': 'y', 'ι': 'ἰ'}

def _var(w):
    d = unicodedata.normalize('NFD', w)
    base_idx = [i for i, ch in enumerate(d) if unicodedata.category(ch) != 'Mn']
    for i in base_idx:
        ch = d[i]; lo = ch.lower()
        if lo in TROCAS:
            t = TROCAS[lo]; t = t.upper() if ch.isupper() else t
            yield unicodedata.normalize('NFC', d[:i] + t + d[i + 1:]), i

@functools.lru_cache(maxsize=None)
def corrigir(w):
    """Devolve (forma, motivo). Só troca se a forma do OCR não está no léxico e a trocada está."""
    if not w: return w, ''
    f0 = freq(w)
    melhor = None
    for v, i in _var(w):
        f = freq(v)
        if f and (melhor is None or f > melhor[1]): melhor = (v, f)
    if f0 > 0:
        if melhor and melhor[1] > 40 * f0 + 20: return melhor[0], 'troca1f'
        return w, ''
    if melhor: return melhor[0], 'troca1'
    for v, i in _var(w):
        for v2, j in _var(v):
            if j <= i: continue
            f = freq(v2)
            if f and (melhor is None or f > melhor[1]): melhor = (v2, f)
    if melhor and melhor[1] >= 3: return melhor[0], 'troca2'
    return w, '?'

AMBIG = {'χ': 'κ', 'κ': 'χ', 'δ': 'β', 'β': 'δ', 'ν': 'υγ', 'υ': 'ν', 'γ': 'ν', 'ο': 'σ', 'σ': 'ο', 'ζ': 'ξ', 'ξ': 'ζ', 'ϐ': 'β', 'θ': 'ϑ'}
import itertools

@functools.lru_cache(maxsize=None)
def corrigir2(w):
    """Como corrigir, mas tenta todas as combinações das letras ambíguas (até 7 posições)."""
    r = corrigir(w)
    if r[1] != '?': return r
    d = unicodedata.normalize('NFD', w)
    pos = [i for i, ch in enumerate(d) if ch.lower() in AMBIG][:7]
    if not pos: return r
    opts = []
    for i in pos:
        ch = d[i]; alts = [ch] + [a.upper() if ch.isupper() else a for a in AMBIG[ch.lower()]]
        opts.append(alts)
    melhor = None
    for combo in itertools.product(*opts):
        l = list(d)
        for i, c in zip(pos, combo): l[i] = c
        v = unicodedata.normalize('NFC', ''.join(l))
        f = freq(v)
        if f and (melhor is None or f > melhor[1]): melhor = (v, f)
    if melhor and melhor[1] >= 2: return melhor[0], 'combo'
    # tira sujeira: letra maiúscula duplicada no começo (ἸΙ), sinal solto
    w2 = re.sub(r'^([Ͱ-Ͽἀ-῿])Ι', r'\1', w).replace('’', '').replace("'", '')
    if w2 != w: 
        r2 = corrigir(w2)
        if r2[1] != '?': return r2[0], 'limpo'
    return r
