import re
def tokens(arq, refs=None):
    """Lista de tokens (palavras com pontuação; '¶' = parágrafo novo)."""
    out = []
    pend = ''  # pedaço de palavra partida
    for ln in open(arq, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('PG|'):
            continue
        tipo, t = ln[0], ln[2:]
        ref = None
        if '\t' in t:
            t, ref = t.split('\t'); ref = [int(x) for x in ref.split(',')]
        t = re.sub(r'^\s*[-~]\s+', '', t)          # «- » de margem (bwb)
        t = re.sub(r'\s+[~|l]$', '', t)              # sujeira no fim
        t = re.sub(r'\(\s*[0-9IlTJ]{1,2}\s*\)', ' ', t)  # chamada de nota (1)
        t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
        ws = t.split()
        if not ws:
            continue
        if tipo == 'P' and not pend:
            out.append('¶')
            if refs is not None: refs.append(ref)
        if pend:
            ws[0] = pend + ws[0]; pend = ''
        if ws[-1].endswith('-') and len(ws[-1]) > 1 and not ws[-1].endswith('--'):
            pend = ws[-1][:-1]; ws = ws[:-1]
            if not ws: continue
        out.extend(ws)
        if refs is not None: refs.extend([ref] * len(ws))
    if pend:
        out.append(pend)
        if refs is not None: refs.append(ref)
    return out

def norm(w):
    w = w.lower()
    w = re.sub(r'[^\wáéíóúüñ]', '', w)
    return w
