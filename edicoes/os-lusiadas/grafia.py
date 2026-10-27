"""Grafia de hoje de uma forma da 1ª edição, guiada pela forma do Wikisource: muda a maneira de escrever
(ſ, u/v, i/j, y, ph, letras dobradas, til, -ão/-am), nunca a forma da palavra (pera, imigo, fermoso ficam)."""
import re, unicodedata
from difflib import SequenceMatcher

def _base(w):
    w = w.replace('ſ', 's')
    w = re.sub(r'[àèìòùâêîôû]', lambda m: _sem(m.group()), w)       # acentos de 1572 (tomàrão, podêra)
    w = re.sub(r'[ÀÈÌÒÙÂÊÎÔÛ]', lambda m: _sem(m.group()), w)
    w = w.replace('y', 'i').replace('Y', 'I')
    w = w.replace('ph', 'f').replace('Ph', 'F').replace('th', 't').replace('Th', 'T')
    w = re.sub(r'(?i)ch(?=[rl])', lambda m: m.group()[0], w)
    w = re.sub(r'([bcdfglmnpt])\1', r'\1', w)                    # dobradas (fica rr, ss)
    w = re.sub(r'(?<=[aeiouAEIOU])u(?=[aeiou])', 'v', w)       # nouo -> novo
    w = re.sub(r'(?<=[rlnRLN])u(?=[aeiou])', 'v', w)           # Neruo? (rara)
    w = re.sub(r'^([Vv])(?=[^aeiouAEIOU])', lambda m: 'U' if m.group() == 'V' else 'u', w)
    w = re.sub(r'^h(?=[ũu]|e$|ia|ião|iam|ir|ião)', '', w); w = re.sub(r'^H(?=[ũu]|e$|ia|ião|iam)', '', w)
    w = re.sub(r'oẽs$', 'ões', w); w = re.sub(r'oẽ$', 'õe', w); w = re.sub(r'aã(s?)$', r'ã\1', w)
    w = re.sub(r'(?<=[hnNgdD])ũa', 'uma', w); w = w.replace('ũa', 'ua')
    w = w.replace('ũs', 'uns').replace('ũ', 'um').replace('Ũ', 'Um')
    w = re.sub(r'ẽs$', 'ens', w); w = re.sub(r'ẽ$', 'em', w); w = re.sub(r'ẽ(?=[pb])', 'em', w); w = w.replace('ẽ', 'en')
    w = re.sub(r'ã(?=[pb])', 'am', w); w = re.sub(r'ã(?=[^aoesm]|s[^$])', 'an', w); w = re.sub(r'õ(?=[^aeis])', 'on', w)
    w = re.sub(r'um(?=n)', 'u', w)
    w = re.sub(r'^([Dd])eo(s?)$', r'\1eus\2', w).replace('Deuss', 'Deus').replace('deuss', 'deus')
    w = re.sub(r'^([Cc])eo(s?)$', r'\1éu\2', w)
    w = re.sub(r'(?<=[DdCc])eo(?=s)', 'eu', w)                 # Deoses
    w = re.sub(r'(?<=[mpn])ao(s?)$', r'au\1', w)               # mao, naos, pao
    w = re.sub(r'ae(s?)$', r'ai\1', w)                          # quaes
    w = re.sub(r'(?<=[gq])o(?=a)', 'u', w)                      # agoa, lingoa, igoal
    w = re.sub(r'c(?=t)|(?<=m)p(?=t)', '', w)                  # victoria, prompto
    w = re.sub(r'(?<=[aeiou])p(?=t)', '', w)                   # escripto
    w = re.sub(r'mt', 'nt', w)
    w = re.sub(r'^aa(s?)$', r'à\1', w); w = re.sub(r'^Aa(s?)$', r'À\1', w)
    w = w.replace('ee', 'é').replace('aa', 'a').replace('oo', 'o')
    w = re.sub(r'([sS])pr', r'\1pr', w)
    return w

def _sem(w):
    return ''.join(ch for ch in unicodedata.normalize('NFD', w) if unicodedata.category(ch) != 'Mn')

def acentuar(novo, ws):
    """Põe em `novo` os acentos de `ws`, onde as letras se alinham."""
    if not ws: return novo
    a, b = _sem(novo).lower(), _sem(ws).lower()
    nf = list(unicodedata.normalize('NFC', novo)); wf = list(unicodedata.normalize('NFC', ws))
    if len(nf) != len(a) or len(wf) != len(b): return novo
    for t, i1, i2, j1, j2 in SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if t == 'equal':
            for k in range(i2 - i1):
                c = wf[j1 + k]
                if _sem(c).lower() == a[i1 + k] and c.lower() != c.lower().encode('ascii', 'ignore').decode() or c in 'ãõâêôáéíóúàÃÕÂÊÔÁÉÍÓÚÀ':
                    nf[i1 + k] = c.upper() if nf[i1 + k].isupper() else c.lower()
    return ''.join(nf)

GRAF = {('ch', 'qu'), ('ch', 'c'), ('h', ''), ('m', 'n'), ('', 'h'), ('i', 'j'), ('u', 'v'), ('v', 'u'), ('s', 'ss'), ('ss', 's'), ('c', 'ç'), ('ç', 'c'), ('ç', 'ss'), ('ç', 's'), ('c', 'sc'), ('', 's'), ('x', 'ex'), ('z', 's'), ('s', 'z'), ('ea', 'eia'), ('e', 'ei'), ('', 'e'), ('o', 'u'), ('', 'i'), ('o', 'e')}
GRAF_SEGURO = {('g', 'j'), ('j', 'g'), ('ch', 'qu'), ('ch', 'c'), ('h', ''), ('', 'h'), ('i', 'j'), ('u', 'v'), ('v', 'u'), ('s', 'ss'), ('ss', 's'), ('c', 'ç'), ('ç', 'c'), ('ç', 'ss'), ('c', 'sc'), ('ç', 'sc'), ('e', 'ei'), ('', 'i'), ('m', 'n')}

def pela_ws(n, ws):
    """Adota as letras do Wikisource onde a diferença é só gráfica (ch/qu, h, i/j, u/v, ss/ç...)."""
    if not ws: return n
    a, b = n.lower(), _sem(ws).lower()
    if len(a) != len(n) or len(b) != len(ws): return n
    out, wl = [], _sem(ws)
    for t, i1, i2, j1, j2 in SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if (t != 'equal' and (a[i1:i2], b[j1:j2]) in GRAF_SEGURO and not (a[i1:i2] == 'm' and b[j1:j2] == 'n' and b[j2:j2+1] not in 'fv')
                and not (b[j1:j2] == 'i' and a[i1:i1 + 1] == 'x')):         # baxo, pexe, dexa: forma de 1572
            seg = wl[j1:j2]
            if i1 == 0 and n[:1].isupper(): seg = seg[:1].upper() + seg[1:]
            elif i1 == 0: seg = seg.lower()
            out.append(seg)
        else:
            out.append(n[i1:i2])
    return ''.join(out)

def palavra(w, ws=''):
    n = _base(w)
    n = pela_ws(n, ws)
    if w[:1].isupper(): n = n[:1].upper() + n[1:]
    n = re.sub(r'ã$', 'ã', n)
    # -eo/-io finais (vio, moueo, alheo, feo): segue o Wikisource
    m = re.search(r'([ei])o(s?)$', n)
    if m and ws:
        if re.search(r'[eéií]u(s?)$', ws): n = n[:m.start()] + m.group(1) + 'u' + m.group(2)
        elif re.search(r'eio(s?)$', ws) and not re.search(r'eio(s?)$', n): n = n[:m.start()] + 'eio' + m.group(2)
    # -am / -ão finais: segue o Wikisource quando ele tem o par
    if re.search(r'(am|ão)$', n) and ws and re.search(r'(am|ão)$', ws):
        n = n[:-2] + ws[-2:]
    elif re.search(r'ão$', n) and n[:1].islower() and len(n) > 4 and re.search(r'(r|v|i|ss|x)ão$', n):
        n = n[:-2] + 'am'                                        # forão, fizerão, andauão, podião
    elif re.search(r'am$', n) and not ws.endswith('am'):
        n = n[:-2] + 'ão'                                        # nam, tam, antam, coraçam
    # i/j e u/v pela forma moderna
    if ws and n[:1] in 'Ii' and ws[:1] in 'Jj': n = ('J' if n[0] == 'I' else 'j') + n[1:]
    if ws and _sem(ws).lower() != _sem(n).lower() and re.sub(r'ei(?=[aoeã])', 'e', _sem(ws).lower()) == re.sub(r'ei(?=[aoeã])', 'e', _sem(n).lower()):
        return ws if not n[:1].isupper() or ws[:1].isupper() else ws[:1].upper() + ws[1:]
    return acentuar(n, ws)


def hifenizar(n, ws):
    """Põe em n os hífens e apóstrofos do Wikisource (Perguntalhe -> Pergunta-lhe; cos -> co'os)."""
    if not ws or not re.search(r"[-'’]", ws) or re.search(r"[-'’]", n): return n
    partes = re.split(r"([-'’])", ws)
    # sufixo (clítico) igual: corta n no mesmo ponto a partir do fim
    suf = ''.join(partes[1:]); cl = re.sub(r"[-'’]", '', suf)
    if _sem(n).lower().endswith(_sem(cl).lower()) and len(n) > len(cl):
        r = n[:len(n) - len(cl)] + re.sub(r"[^-'’].*", '', suf) + n[len(n) - len(cl):]
        return re.sub(r'n(?=-(se|me|te|nos|vos|lhe|lhes|o|a|os|as)$)', 'm', r)
    return n


def span(a, b):
    """Saída de uma diferença (1572 a × Wikisource b), palavra a palavra quando as contas batem."""
    A, B = a.split(), b.split()
    if len(A) == len(B): return ' '.join(hifenizar(palavra(x, y), y) for x, y in zip(A, B))
    return ' '.join(palavra(x) for x in A)
