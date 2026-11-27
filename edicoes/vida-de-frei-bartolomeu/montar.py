"""Vida de D. Frei Bertolameu dos Mártires — do voto (votar.py) ao texto estabelecido, por capítulo.

  python3 -I edicoes/vida-de-frei-bartolomeu/montar.py            # grava PASTA/montado/ (para conferir)
  python3 -I edicoes/vida-de-frei-bartolomeu/montar.py --gravar   # grava texto/ (na grafia de 1619, sem ſ)

Corpo: páginas 19–582 do exemplar da BNP; dedicatória: 15–17. As formas que só 1619 deu (sem apoio das
edições de Lisboa) passam pelo vocabulário de Lisboa (ſ lido «f» ou «l» → s). As correções da conferência
nas imagens (conferencia.tsv) se aplicam por unidade do voto.
"""
import collections
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import colacao as C  # noqa: E402
import testemunhos as T  # noqa: E402

CORPO = (19, 582)
DEDICATORIA = (15, 17)
ROMANOS = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
ORDINAIS = {'primeiro': 1, 'segundo': 2, 'segvndo': 2, 'terceiro': 3, 'quarto': 4, 'quinto': 5, 'sexto': 6, 'seisto': 6}


def romano(s):
    s = s.upper().strip('.,:;')
    s = s.replace('1', 'I').replace('l', 'I').replace('U', 'V')
    if not s or any(c not in ROMANOS for c in s):
        return None
    tot = 0
    for i, c in enumerate(s):
        v = ROMANOS[c]
        tot += -v if i + 1 < len(s) and ROMANOS[s[i + 1]] > v else v
    return tot


def vocabulario():
    """Formas da edição de 1850–1853 (Tesseract), com o número de ocorrências."""
    voc = collections.defaultdict(collections.Counter)
    for nome in ('r185',):           # a de 1818 ainda usa o ſ, e o OCR o lê «f»
        d = json.load(open(os.path.join(T.PASTA, 'colacao', nome + '.json')))
        for w in d['palavras']:
            t = re.sub(r'^[^\wÀ-ÿ&]+|[^\wÀ-ÿ&]+$', '', w['t'])
            if t and re.fullmatch(r'[A-Za-zÀ-ÿ&]+', t):
                voc[t.lower()]['n'] += 1
    return voc


_VOC = None


TIL = {'á': 'an', 'ã': 'an', 'â': 'an', 'é': 'en', 'ẽ': 'en', 'ê': 'en', 'ó': 'on', 'õ': 'on', 'ô': 'on',
       'í': 'in', 'ĩ': 'in', 'ú': 'un', 'ũ': 'un'}


def _variantes_1619(lw):
    """Leituras possíveis de uma forma de 1619 lida pelo OCR: ſ lido f/l/í; til lido como acento (lébrança)."""
    lw = re.sub(r'(?<=[aeiou])u(?=[aeiou])', 'v', lw)          # 1619: u por v entre vogais (controuersia)
    lw = re.sub(r'^u(?=[aeiou])', 'v', lw)
    pos_s = [i for i, c in enumerate(lw) if c in 'flí' and i + 1 < len(lw) and lw[i + 1] not in 'rl']
    pos_t = [i for i, c in enumerate(lw) if c in TIL and i + 1 < len(lw) and lw[i + 1] in 'bcdfgjlmpqstvxz']
    from itertools import combinations
    out = []
    for ns in range(0, min(3, len(pos_s)) + 1):
        for cs in combinations(pos_s, ns):
            for nt in range(0, min(2, len(pos_t)) + 1):
                for ct in combinations(pos_t, nt):
                    v = ''
                    for i, c in enumerate(lw):
                        if i in cs:
                            v += 's'
                        elif i in ct:
                            base = TIL[c]
                            v += base[0] + ('m' if lw[i + 1] in 'bp' else 'n')
                        else:
                            v += c
                    out.append(v)
    return out


def de_1619(t):
    """Forma de 1619 lida pelo OCR → grafia das edições de Lisboa (ſ: f/l/í lidos onde era s; til lido como
    acento); a pontuação colada no meio («mão,a») se separa."""
    global _VOC
    if _VOC is None:
        _VOC = vocabulario()
    if re.search(r'[A-Za-zÀ-ÿ][,;:][A-Za-zÀ-ÿ]', t):
        return ' '.join(de_1619(p) for p in re.sub(r'([,;:])(?=[A-Za-zÀ-ÿ])', r'\1 ', t).split())
    m = re.match(r'^([^\wÀ-ÿ&]*)(.*?)([^\wÀ-ÿ&]*)$', t)
    a, w, z = m.groups()
    if not w or _VOC.get(w.lower(), {}).get('n', 0) >= 2:
        return t
    lw = w.lower()
    variantes = _variantes_1619(lw)
    melhores = [(_VOC[v]['n'], v) for v in variantes if v in _VOC]
    if not melhores:
        for v in sorted(variantes, key=lambda v: sum(1 for x, y in zip(v, lw) if x != y)):
            if valida(v):
                melhores = [(1, v)]
                break
    if melhores:
        v = max(melhores)[1]
        v = ''.join(c.upper() if i < len(w) and w[i].isupper() else c for i, c in enumerate(v))
        return a + v + z
    return t


def valida(t):
    """Palavra de verdade: dada ≥ 2 vezes pelas edições de Lisboa, ou do léxico de hoje, ou latina."""
    global _VOC
    if _VOC is None:
        _VOC = vocabulario()
    w = re.sub(r'^[^\wÀ-ÿ&]+|[^\wÀ-ÿ&]+$', '', t)
    if not w or w == '&' or w.isdigit():
        return True
    if _VOC.get(w.lower(), {}).get('n', 0) >= 2:
        return True
    if not re.fullmatch(r"[A-Za-zÀ-ÿ]+(-[A-Za-zÀ-ÿ]+)*", w):
        return False
    import latim
    if latim.norm(w) in latim.vocabulario():
        return True
    if _no_lexico(w):
        return True
    import grafia
    enc = grafia.enclise_antiga(w)
    return bool(enc) and (_VOC.get(enc[0], {}).get('n', 0) >= 2 or _no_lexico(enc[0]))


_LEXC = {}


def _no_lexico(w):
    if w not in _LEXC:
        import grafia
        n = grafia.uma(w, '', '').split('-')[0].lower()
        _LEXC[w] = n in grafia.G.lexico()
    return _LEXC[w]


def trocar_invalidas(x):
    """Unidade com palavra que não existe: a leitura (de qualquer testemunho, 1619 convertido) só de palavras de
    verdade e mais parecida com a escolhida."""
    import difflib
    if all(valida(t) for t in x['f']):
        return False
    k0 = _k(x['f'])
    cands = []
    for n, l in x['lido'].items():
        if not l:
            continue
        toks = l.split()
        if n in ('bnp', 'ia', 'ga'):
            toks = ' '.join(de_1619(t) for t in toks).split()
        if toks and all(valida(t) for t in toks):
            r = difflib.SequenceMatcher(None, k0, _k(toks)).ratio()
            if r >= 0.7:
                cands.append((r + (0.05 if n in ('r185', 'r1818') else 0), toks))
    if cands:
        x['f'] = max(cands, key=lambda c: c[0])[1]
        return True
    return False


def _k(ts):
    return ''.join(C.chave(t) for t in ts)


def _perto(a, b, lim=0.85):
    import difflib
    return bool(a) and bool(b) and difflib.SequenceMatcher(None, a, b).ratio() >= lim


def limpar_unidades(v, log):
    """Repetições que o alinhamento cria nas palavras partidas no fim da linha: a palavra inteira inserida
    (de Lisboa) entre os dois pedaços lidos por 1619 («Mar | Martyres | tyres»), o pedaço repetido depois da
    palavra inteira («despois pois») e a mesma palavra duas vezes seguidas («qnando quando»)."""
    us = [x for x in v if x['f']]
    for k in range(len(us)):
        x = us[k]
        if not x['f']:
            continue
        p = next((us[j] for j in range(k - 1, -1, -1) if us[j]['f']), None)
        n = next((us[j] for j in range(k + 1, len(us)) if us[j]['f']), None)
        kx = _k(x['f'])
        kp = _k(p['f']) if p else ''
        kn = _k(n['f']) if n else ''
        if x.get('vao') and len(x['f']) == 1:
            if kp and kn and _perto(kx, kp + kn):
                log.append(('junta', ' '.join(p['f']), ' '.join(x['f']), ' '.join(n['f'])))
                p['f'], n['f'] = list(x['f']), []
                x['f'] = []
                continue
            if kp and len(kp) < len(kx) and kx.startswith(kp[:max(2, len(kp) - 1)]) and not _perto(kp, kx, 0.95):
                log.append(('pedaço antes', ' '.join(p['f']), ' '.join(x['f']), ''))
                p['f'] = []
            elif kn and len(kn) < len(kx) and kx.endswith(kn[-max(2, len(kn) - 1):]) and not _perto(kn, kx, 0.95):
                log.append(('pedaço depois', '', ' '.join(x['f']), ' '.join(n['f'])))
                n['f'] = []
            elif _perto(kx, kp) or _perto(kx, kn):
                log.append(('repetida', ' '.join(p['f']) if p else '', ' '.join(x['f']), ' '.join(n['f']) if n else ''))
                x['f'] = []
            continue
        # pedaço depois da palavra inteira: as edições de Lisboa não têm nada nesta unidade
        lis = [x['lido'].get(m) for m in ('r185', 'r1818', 'gr185', 'gr1818')]
        lis = [y for y in lis if y is not None]
        if p and lis and all(y == '' for y in lis) and len(kx) >= 2 and kp.endswith(kx) and len(kp) > len(kx) + 1:
            log.append(('pedaço repetido', ' '.join(p['f']), ' '.join(x['f']), ''))
            x['f'] = []
            continue
        plis = [p['lido'].get(m) for m in ('r185', 'r1818', 'gr185', 'gr1818')] if p else []
        plis = [y for y in plis if y is not None]
        if p and plis and all(y == '' for y in plis) and kp and kx.startswith(kp) and len(kx) > len(kp) + 1:
            log.append(('pedaço antes', ' '.join(p['f']), ' '.join(x['f']), ''))
            p['f'] = []
            continue
        if p and len(kx) >= 4 and (kx == kp or _perto(kx, kp, 0.92)) and len(x['f']) == 1 and len(p['f']) == 1:
            log.append(('dobrada', ' '.join(p['f']), ' '.join(x['f']), ''))
            x['f'] = []


def fluxo(log=None):
    """Lista de palavras do texto: dict(t, sit, u, i, p, c, lido)."""
    v = json.load(open(os.path.join(T.PASTA, 'voto.json')))
    ref = json.load(open(os.path.join(T.PASTA, 'colacao', 'bnp.json')))['palavras']
    corr = conferencia()
    log = [] if log is None else log
    for x in v:
        x['chave'] = ('v' if x.get('vao') else 'u') + str(x['u'])
        if x['chave'] in corr:
            x['f'] = corr[x['chave']].split() if corr[x['chave']] != '∅' else []
            x['sit'] = 'conf'
        else:
            if x['f']:
                x['f'] = ' '.join(t if valida(t) else de_1619(t) for t in x['f']).split()
            x['f'] = list(x['f'] or [])
            if x['f'] and DEDICATORIA[0] <= ref[min(x['i'], len(ref) - 1)]['p'] <= CORPO[1] and trocar_invalidas(x):
                log.append(('troca', '', ' '.join(x['f']), ''))
        x['f'] = list(x['f'] or [])
    limpar_unidades(v, log)
    out = []
    for x in v:
        if not x['f']:
            continue
        r = ref[x['i']] if x['i'] < len(ref) else ref[-1]
        for t in x['f']:
            out.append({'t': t, 'sit': x['sit'], 'u': x['chave'], 'i': x['i'], 'p': r['p'], 'c': r.get('c', ''),
                        'lido': x['lido']})
    return out


def conferencia():
    f = os.path.join(AQUI, 'conferencia.tsv')
    out = {}
    if os.path.exists(f):
        for l in open(f, encoding='utf-8'):
            if l.strip() and not l.startswith('#'):
                c = l.rstrip('\n').split('\t')
                out[c[0]] = c[1]
    return out


def cabecalhos(fl):
    """Posições dos títulos de capítulo: «CAPITULO»/«CAP.» seguido de número romano ou ordinal."""
    achados = []
    for k, w in enumerate(fl):
        if not (CORPO[0] <= w['p'] <= CORPO[1]):
            continue
        k0 = C.chave(w['t'])
        if not (k0.startswith('kapet') or k0 in ('kap', 'kapt', 'kapet') or re.match(r'(?i)^c[aá]p[iíl1]?t?[uv]?[lI1]?o?\.?$', w['t'])):
            continue
        for d in (1, 2):
            if k + d < len(fl):
                s = fl[k + d]['t']
                n = romano(s)
                if n is None and s.lower().strip('.,:') in ORDINAIS:
                    n = ORDINAIS[s.lower().strip('.,:')]
                if n:
                    achados.append((k, n, k + d))
                    break
    return achados


def taboada():
    """[(livro, cap, título, fólio)] da Taboada de 1619 (taboada/taboada-1619.tsv, transcrita das imagens)."""
    out = []
    for l in open(os.path.join(AQUI, 'taboada', 'taboada-1619.tsv'), encoding='utf-8').read().splitlines()[1:]:
        c = l.split('\t')
        out.append((int(c[0]), int(c[1]), c[2], int(c[3]) if c[3].strip().isdigit() else None))
    return out


def pagina_do_folio(f):
    return CORPO[0] + 2 * (f - 1)


def localizar(fl):
    """Para cada capítulo da Taboada: (início do cabeçalho, fim do título) no fluxo, achados pelo título da
    Taboada (chaves) nas páginas do fólio indicado."""
    import difflib
    tab = taboada()
    chaves = [C.chave(w['t']) for w in fl]
    por_pag = collections.defaultdict(list)
    for k, w in enumerate(fl):
        por_pag[w['p']].append(k)
    res = []
    for liv, cap, tit, fol in tab:
        p0 = pagina_do_folio(fol)
        idx = [k for p in range(p0 - 1, p0 + 3) for k in por_pag.get(p, [])]
        kt = [x for x in (C.chave(t) for t in tit.split()) if x]
        melhor = (0, None, None)
        n = len(kt)
        for a in range(len(idx)):
            for L in (n - 2, n, n + 2):
                if L <= 0 or a + L > len(idx):
                    continue
                janela = [chaves[k] for k in idx[a:a + L]]
                r = difflib.SequenceMatcher(None, kt, janela, autojunk=False).ratio()
                if r > melhor[0]:
                    melhor = (r, idx[a], idx[a + L - 1])
        # preferir a posição logo depois de um «CAP…» (o título do corpo começa ali)
        caps = [k for k in idx if C.chave(fl[k]['t']).startswith('kap') or re.match(r'(?i)^[cg][aáà4]?[pf][iíl1.,]', fl[k]['t'])]
        melhor_cap = (0, None, None)
        for kc in caps:
            for d in (1, 2, 3):
                a = idx.index(kc) + d
                L = n
                if a + L > len(idx):
                    continue
                janela = [chaves[k] for k in idx[a:a + L]]
                r = difflib.SequenceMatcher(None, kt, janela, autojunk=False).ratio()
                if r > melhor_cap[0]:
                    melhor_cap = (r, idx[a], idx[a + L - 1])
        if melhor_cap[0] >= 0.3 and melhor_cap[0] >= melhor[0] - 0.25:
            melhor = melhor_cap
        r, s, e = melhor
        ini = s
        if s is not None:
            for k in range(s - 1, max(s - 6, -1), -1):
                if C.chave(fl[k]['t']).startswith('kap') or re.match(r'(?i)^c[aá]p', fl[k]['t']):
                    ini = k
                    break
        res.append({'livro': liv, 'cap': cap, 'tab': tit, 'r': round(r, 2), 'ini': ini, 's': s, 'e': e})
    return res


def capitulos(fl):
    """[{livro, cap, titulo (da Taboada), corpo: [palavras]}] e a dedicatória."""
    loc = localizar(fl)
    caps = []
    for k, x in enumerate(loc):
        fim = loc[k + 1]['ini'] if k + 1 < len(loc) else next(j for j in range(len(fl) - 1, -1, -1) if fl[j]['p'] <= CORPO[1]) + 1
        corpo = [w for w in fl[x['e'] + 1:fim] if not re.fullmatch(r'[(\[{]?[0-9IlJ]{1,2}[)\]}]', w['t'])]
        caps.append({'livro': x['livro'], 'cap': x['cap'], 'titulo': x['tab'], 'corpo': corpo, 'r': x['r'],
                     'ini': x['ini'], 's': x['s'], 'e': x['e']})
    ded = [w for w in fl if DEDICATORIA[0] <= w['p'] <= DEDICATORIA[1]]
    return caps, ded


def texto(ws):
    s = ' '.join(w['t'] for w in ws)
    s = re.sub(r'\s+([,;:.!?)])', r'\1', s)
    s = re.sub(r'([(])\s+', r'\1', s)
    return s


if __name__ == '__main__':
    log = []
    fl = fluxo(log)
    caps, ded = capitulos(fl)
    dest = os.path.join(AQUI, 'texto') if '--gravar' in sys.argv else os.path.join(T.PASTA, 'montado')
    os.makedirs(dest, exist_ok=True)
    open(os.path.join(dest, 'dedicatoria.txt'), 'w', encoding='utf-8').write(texto(ded) + '\n')
    for c in caps:
        open(os.path.join(dest, f"l{c['livro']}-c{c['cap']:02d}.txt"), 'w', encoding='utf-8').write(
            '## ' + c['titulo'] + '\n\n' + texto(c['corpo']) + '\n')
    n = sum(len(c['corpo']) for c in caps)
    print(len(caps), 'capítulos,', n, 'palavras no corpo;', len(ded), 'na dedicatória')
