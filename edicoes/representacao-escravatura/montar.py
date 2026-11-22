"""Representação sobre a escravatura (José Bonifácio): da transcrição de 1825 (1825/NNN.txt, conferida nas imagens)
à grafia de hoje. python3 -I montar.py [--publicar]; relatórios em relatorios/ (fora do git)."""
import collections, os, re, sys, unicodedata
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path[:0] = [AQUI, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'), os.path.join(RAIZ, 'ferramentas')]
import grafia1990 as G  # noqa: E402
import decisoes as D  # noqa: E402

NOVO_PARAGRAFO = {30, 33, 34, 37, 38, 41}   # páginas que abrem com recuo ou título (vistas no fac-símile)
nfc = lambda s: unicodedata.normalize('NFC', s)

def paginas():
    corr = collections.defaultdict(list)
    tsv = os.path.join(AQUI, 'conferencia.tsv')
    if os.path.exists(tsv):
        for l in open(tsv, encoding='utf-8'):
            c = l.rstrip('\n').split('\t')
            if len(c) >= 3 and c[1] != 'OK' and not l.startswith('#'):
                corr[int(c[0])].append((c[1], c[2]))
    for n in range(11, 51):
        t = nfc(open(os.path.join(AQUI, '1825', f'{n:03d}.txt'), encoding='utf-8').read())
        for de, para in corr[n]:
            pad = r'\s+'.join(re.escape(x) for x in de.split(' '))
            t, q = re.subn(pad, lambda _: para, t)
            if q != 1:
                raise SystemExit(f'conferência: p. {n}: «{de}» aparece {q} vezes')
        corpo, _, notas = t.partition('\n---\n')
        yield n, corpo.strip(), [x for x in notas.strip().split('\n') if x]

def montar():
    """Blocos em ordem (parágrafos do impresso) e as notas, com a chamada [k] já global."""
    blocos, notas = [], []
    for n, corpo, ns in paginas():
        locais = {}
        for x in ns:
            if x.startswith('(continua) '):
                notas[-1] = notas[-1].rstrip('-') + ('' if notas[-1].endswith('-') else ' ') + x[11:]
            else:
                notas.append(x)
                locais[len(locais) + 1] = len(notas)
        corpo = re.sub(r'\[(\d+)\]', lambda m: f'⟦{locais[int(m.group(1))]}⟧', corpo)
        ps = [re.sub(r'-\n', '¬', p).replace('\n', ' ') for p in re.split(r'\n\s*\n', corpo) if p.strip()]
        if not ps:
            continue
        if blocos and n not in NOVO_PARAGRAFO and n != 15:
            ant = blocos[-1]
            blocos[-1] = ant[:-1] + '¬' + ps[0] if ant.endswith('-') else ant + ' ' + ps[0]
            ps = ps[1:]
        blocos += ps
    # títulos dos artigos: «ARTIGOS I.», «art. ii.»; no art. XXVII o texto vem colado ao título
    saida = []
    for b in blocos:
        x = re.match(r'^(?:ARTIGOS|art\.)\s+([IVXLivxl]+)\.\s*(.*)$', b, re.S)
        if x:
            saida.append(f'**Art. {x.group(1).upper()}.**')
            if x.group(2).strip():
                saida.append(x.group(2).strip())
        else:
            saida.append(b)
    return saida, notas

# hífen de fim de linha: some, salvo nos pronomes pendurados listados em decisoes.HIFEN_FICA (a«¬»b)
def desifeniza(s):
    return re.sub(r"(\w+)¬(\w+)", lambda m: m.group(1) + ('-' if (m.group(1) + '-' + m.group(2)).lower() in D.HIFEN_FICA else '') + m.group(2), s)

PAL = r"[A-Za-zÀ-ÿ]+(?:['-][A-Za-zÀ-ÿ]+)*"
def modernizar(s, rel):
    if s.startswith('**Art.'):
        return s
    s = desifeniza(s)
    for de, para in D.PRE:
        s = re.sub(de, para, s)
    guardados = []
    def guarda(m):
        guardados.append(m.group(0))
        return f'\ue000{len(guardados) - 1}\ue001'
    s = re.sub(D.FRANCES, guarda, s)
    def um(m):
        t = m.group(0)
        if t in D.EXATO:
            return D.EXATO[t]
        lw = t.lower()
        if lw in D.M:
            return G.igualar_caixa(t, D.M[lw])
        if '-' in t:
            a = t.split('-')
            return '-'.join(p if k and p.lower() in G.CLITICOS else um(re.match(PAL, p)) for k, p in enumerate(a))
        novo, f = G.atual(t)
        rel[f][(t, novo)] += 1
        return novo
    s = re.sub(PAL, um, s)
    for de, para in D.POS:
        s = re.sub(de, para, s)
    s = re.sub(r'\ue000(\d+)\ue001', lambda x: guardados[int(x.group(1))], s)
    return re.sub(r' +([,.;:!?])', r'\1', s).replace('⟦', '[').replace('⟧', ']')

def gerar():
    rel = {k: collections.Counter() for k in ('SEM_PAR', 'esqueleto', 'lexico')}
    bl, no = montar()
    return bl, no, [modernizar(x, rel) for x in bl], [modernizar(x, rel) for x in no], rel

if __name__ == '__main__':
    bl, no, mb, mn, rel = gerar()
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    with open(os.path.join(AQUI, 'relatorios', 'trocas.tsv'), 'w', encoding='utf-8') as f:
        for k in rel:
            for (a, b), c in sorted(rel[k].items()):
                if a != b or k == 'SEM_PAR':
                    f.write(f'{k}\t{a}\t{b}\t{c}\n')
    open(os.path.join(AQUI, 'relatorios', 'atual.txt'), 'w', encoding='utf-8').write('\n\n'.join(mb) + '\n\n=== NOTAS\n\n' + '\n\n'.join(mn) + '\n')
    print(len(mb), 'blocos;', len(mn), 'notas;', sum(len(x.split()) for x in mb + mn), 'palavras; sem par:', len(rel['SEM_PAR']))
    if '--publicar' in sys.argv:
        import publicar
        publicar.gravar(mb, mn)
