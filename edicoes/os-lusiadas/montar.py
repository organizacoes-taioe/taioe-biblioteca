"""Os Lusíadas: o texto da 1ª edição (1572) na grafia brasileira de hoje, sobre a divisão em versos e a
pontuação do Wikisource.

uso: python3 edicoes/os-lusiadas/montar.py            monta texto.txt e confere as rimas
     python3 edicoes/os-lusiadas/montar.py --tabela   grava a tabela das diferenças (cache) para revisão
     python3 edicoes/os-lusiadas/montar.py --publicar e grava conteudo/luis-de-camoes/os-lusiadas.js

Cada diferença de palavra entre as duas fontes que não seja só de grafia (fontes.chave) tem uma decisão
em decisoes.json, pela chave «1572|Wikisource»: "W" (a do Wikisource: erro de 1572, ou grafia que a regra
não cobre), "K" ou ausente (a de 1572 na grafia de hoje, grafia.span) ou o texto exato. Um «/» separa
versos. linhas.json corrige versos inteiros (o Wikisource quebrou mal X,13 e X,94).
"""
import collections, json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, '..', '..')
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'os-maias'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import fontes as base, grafia, rimas  # noqa: E402
import brasil  # noqa: E402  (de Os Maias: é/ó antes de m/n, Egipto...)
from grafia import span  # noqa: E402
DEC = json.load(open(os.path.join(AQUI, 'decisoes.json')))
LINHAS = json.load(open(os.path.join(AQUI, 'linhas.json')))
tok = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
avisos = []
ocorrencias = []          # (canto, estrofe, 1572, Wikisource, saída, decisão)
# erros do Wikisource e grafia portuguesa que sobra (passa à brasileira do Acordo de 1990)
PALAVRAS = {'alhea': 'alheia', 'governá-Ia': 'governá-la', 'Alvares': 'Álvares', 'préminente': 'preminente',
            'Pólo': 'Polo', 'pólo': 'polo', 'Pólos': 'Polos', 'Tróia': 'Troia', 'jóias': 'joias', 'heróica': 'heroica',
            'Heróicos': 'Heroicos', 'Hebréia': 'Hebreia', 'Eôo': 'Eoo', 'Européias': 'Europeias',
            'Antarctico': 'Antártico', 'Antarcticos': 'Antárticos', 'Dêem-lhe': 'Deem-lhe', 'dêem': 'deem',
            'Vêem': 'Veem', 'vêem': 'veem', 'Vêem-se': 'Veem-se', 'Há-de': 'Há de', 'há-de': 'há de', 'hão-de': 'hão de',
            'Neptuno': 'Netuno', 'Neptunino': 'Netunino', 'Neptuninas': 'Netuninas', 'Octaviano': 'Otaviano',
            'Octávio': 'Otávio', 'Tethys': 'Tétis', 'ceptro': 'cetro', 'instructo': 'instruto', 'sumptuosas': 'suntuosas',
            'sumptuoso': 'suntuoso', 'sumptuosos': 'suntuosos', 'tracto': 'trato', 'subtil': 'sutil', 'subtis': 'sutis', 'Anibal': 'Aníbal'}

def saida(a, b, B):
    v = DEC.get(a + '|' + b, 'K')
    if v == 'W': return ' '.join(B)
    if v == 'K': return span(a, b)
    return v

# sobras de digitalização do Wikisource e acentos que o Acordo tirou (trechos exatos)
TRECHOS = [('f az', 'faz'), ('f rio', 'frio'), ('ef eito', 'efeito'), ('pres[s]aga', 'pressaga'), ('res[s]ucite', 'ressucite'),
           ('ale vantavam', 'alevantavam'), ('désse', 'desse'), ('péla', 'pela'), ('atéli', 'até ali'), ('fàcilmente', 'facilmente'),
           ('sòmente', 'somente'), ('prègando', 'pregando'), ('ínvisíbil', 'invisíbil'), ('razãõ', 'razão'), ('frvito', 'fruito'),
           ('leuam', 'levam'), ('maquinauam', 'maquinavam'), ('tremolauam', 'tremolavam'), ('sefizeram', 'se fizeram'),
           ('dũma', 'duma'), ('cũa', "c'uma"), ('ũa', 'uma'), ('crêm', 'creem'), ('decem', 'descem'), ('Ptei', 'Rei')]
NASCE = {'nace': 'nasce', 'naceram': 'nasceram', 'naceste': 'nasceste', 'nacido': 'nascido', 'florece': 'floresce'}

def contracoes(l):
    """Uma notação só para «com» + artigo de 1572: co'o, co'a, co'os, co'as, c'um, c'uma; «co» só antes de pronome."""
    l = re.sub(r"\b([Cc])o a(s?)\b", r"\1o'a\2", l)
    l = re.sub(r"\b([Cc])o(a|as|s)\b", lambda m: m.group(1) + {'a': "o'a", 'as': "o'as", 's': "o'os"}[m.group(2)], l)
    l = re.sub(r"\bC'os\b", "Co'os", l); l = re.sub(r"\bCuma\b", "C'uma", l)
    l = re.sub(r"\b([Cc])o alma\b", r"\1o'a alma", l)
    l = re.sub(r"\b([Cc])o (?!(?:ele|ela|eles|elas|isto|isso|este|esta|estes|estas|estoutro|estoutra|outro|outra)\b)(?=\w)", r"\1o'o ", l)
    return l

def brasileira(l):
    for v, nv in TRECHOS: l = l.replace(v, nv)
    l = contracoes(l)
    for v, nv in NASCE.items(): l = re.sub(r'(?<![\w-])' + v + r'(?![\w-])', nv, l)
    for v, nv in PALAVRAS.items(): l = re.sub(r'(?<![\w-])' + v + r'(?![\w-])', nv, l)
    return re.sub(r"[^\W\d_]+(?:-[^\W\d_]+)*", lambda m: brasil.converter(m.group()), l)

def estrofe(c, n, ls, gp, fim=None):
    ls = [l for l in ls if l != 'Fala do Samorim ao Gama']
    wt = [(li, m.start(), m.end(), m.group()) for li, l in enumerate(ls) for m in tok.finditer(l)]
    ops = base.alinhar([base.chave(x) for x in gp], [base.chave(x[3]) for x in wt])
    edits = []
    for t, a1, a2, b1, b2 in ops:
        if t == 'equal': continue
        a = ' '.join(gp[a1:a2]); B = [x[3] for x in wt[b1:b2]]; b = ' '.join(B)
        if base.chave(a) == base.chave(b): continue
        o = saida(a, b, B)
        ocorrencias.append((c, n, a, b, o, DEC.get(a + '|' + b, 'K'), gp[a2] if a2 < len(gp) else '', wt[b2][3] if b2 < len(wt) else ''))
        edits.append((b1, b2, o, a, b, bool(fim and a2 > a1 and fim[a2 - 1])))
    ls = list(ls)
    for b1, b2, out, a, b, nofim in sorted(edits, key=lambda e: -e[0]):
        if b1 == b2:
            if not out: continue
            if b1 > 0 and (nofim or b1 == len(wt)) and wt[b1 - 1][0] != (wt[b1][0] if b1 < len(wt) else -1):
                li, e = wt[b1 - 1][0], wt[b1 - 1][2]
                ls[li] = ls[li][:e] + ' ' + out + ls[li][e:]
            elif b1 < len(wt):
                li, s = wt[b1][0], wt[b1][1]
                ls[li] = ls[li][:s] + out + ' ' + ls[li][s:]
            else:
                li, e = wt[-1][0], wt[-1][2]
                ls[li] = ls[li][:e] + ' ' + out + ls[li][e:]
            continue
        linhas = sorted({wt[i][0] for i in range(b1, b2)})
        if len(linhas) == 1:
            partes = [out]
        elif ' / ' in out and len(out.split(' / ')) == len(linhas):
            partes = out.split(' / ')
        elif len(out.split()) == b2 - b1:
            ws_ = out.split(); partes = []
            for li in linhas:
                partes.append(' '.join(w for w, i in zip(ws_, range(b1, b2)) if wt[i][0] == li))
        else:
            avisos.append(f'{c},{n}: {a}|{b} -> {out}'); partes = [out] + [''] * (len(linhas) - 1)
        for li, p in zip(reversed(linhas), reversed(partes)):
            idx = [i for i in range(b1, b2) if wt[i][0] == li]
            s, e = wt[idx[0]][1], wt[idx[-1]][2]
            ls[li] = ls[li][:s] + p + ls[li][e:]
    out = []; interna = False
    for i, l in enumerate(ls):
        l = LINHAS.get(f'{c},{n},{i + 1}', l)
        l = re.sub(r'-\s*"\s*', '“', l); l = re.sub(r'\s*"\s*-', '”', l)
        l = re.sub(r'^\s*-\s*', '— ', l); l = re.sub(r'\s+-\s+', ' — ', l); l = re.sub(r'\s*-\s*$', '', l)
        l = re.sub(r'([!?])(?=[A-ZÀ-Ý])', r'\1 ', l)
        l = re.sub(r'\s+', ' ', l).strip(); l = re.sub(r'\s+([,;:.!?)])', r'\1', l)
        res = []
        for j, ch in enumerate(l):
            if ch == '“': interna = True; res.append(ch)
            elif ch == '”': interna = False; res.append(ch)
            elif ch == '"':
                if interna: res.append('”'); interna = False
                elif j == 0 or l[j - 1] in ' (—': res.append('«')
                else: res.append('»')
            else: res.append(ch)
        l = ''.join(res)
        l = re.sub(r'([«“(—]) ', r'\1', l) if not l.startswith('— ') else l[:2] + re.sub(r'([«“(]) ', r'\1', l[2:])
        l = re.sub(r' ([»”])', r'\1', l)
        k = 2 if l.startswith('— ') else 0
        k += 1 if l[k:k + 1] in '«“(' else 0
        l = l[:k] + l[k:k + 1].upper() + l[k + 1:]
        l = brasileira(l)
        out.append(l)
    return out

def obra():
    W = base.ws_estrofes(); G = base.g_estrofes()
    res = []
    for (c, n, ls), (c2, gp, gb, fim) in zip(W, G):
        res.append((c, n, estrofe(c, n, ls, gp, fim)))
    return res

CANTOS = base.CANTOS

def gravar_texto(est):
    with open(os.path.join(AQUI, 'texto.txt'), 'w', encoding='utf-8', newline='\n') as f:
        for c, n, ls in est: f.write(f'{c},{n}\n' + '\n'.join(ls) + '\n\n')

def tabela():
    """As diferenças por tipo, com a saída de hoje: para revisar as decisões."""
    obra()
    cont = collections.Counter((a, b) for c, n, a, b, o, d, *_ in ocorrencias)
    saidas = {(a, b): (o, d, f'{c},{n}') for c, n, a, b, o, d, *_ in ocorrencias}
    with open(base.D + 'tabela.tsv', 'w') as f:
        for (a, b), k in cont.most_common():
            o, d, ex = saidas[(a, b)]
            f.write(f'{k}\t{a}\t{b}\t{o}\t{d}\t{ex}\n')
    print('gravado', base.D + 'tabela.tsv')

if __name__ == '__main__':
    if '--tabela' in sys.argv:
        tabela(); sys.exit()
    est = obra()
    gravar_texto(est)
    print(len(est), 'estrofes;', len(avisos), 'avisos'); print('\n'.join(avisos))
    for r in rimas.conferir(est): print('rima?', r)
    if '--publicar' in sys.argv:
        import publicar
        publicar.publicar(est, ocorrencias, brasileira)
