"""Vida do Padre José de Anchieta — da transcrição de 1897 (1897/NN.txt, conferida nas imagens) ao texto
na grafia de hoje.

  python3 edicoes/vida-de-anchieta/montar.py              # grava atual/ e relatorios/ (fora do git: relatorios)
  python3 edicoes/vida-de-anchieta/montar.py --publicar   # e conteudo/pero-rodrigues/vida-de-anchieta.js

Grafia: ferramentas da _São Bernardo_ (`edicoes/sao-bernardo/grafia1990.py`: léxico do sistema + textos
publicados, esqueleto ortográfico, formas atuais), mais as decisões desta obra em `decisoes.py`
(MANUAL por palavra, AMBIGUOS por contexto, CRASE, ERROS do impresso). Relatórios em relatorios/:
sem_par.tsv (palavras fora do léxico), esqueleto.tsv (trocas por esqueleto, para conferir),
ambiguos.tsv (palavra sem acento em 1897 que hoje pode levar acento ou não), crase.tsv.
"""
import collections
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'))
sys.path.insert(0, AQUI)
import grafia1990 as G  # noqa: E402
import decisoes as D  # noqa: E402
from edicao.grafia import esqueleto  # noqa: E402


def _lexico_ampliado():
    """O léxico da São Bernardo, refeito: o dicionário do Brasil do sistema, as palavras do texto (só os
    `texto:` das partes) das obras em prosa publicadas de Machado e Graciliano (a lista da São Bernardo lia
    também as páginas «Sobre», com grafias antigas: annos, elle) e as do dicionário português do sistema
    (Acordo de 1990, norma europeia) sem forma do mesmo esqueleto no do Brasil (entra virgindade, aquietou;
    ficam de fora facto, contacto)."""
    import glob
    from edicao.grafia import ao1990
    from edicao.tokens import TOK as TOKS, e_palavra
    lex = set()
    for w in open(G.DICIONARIO, encoding='utf-8'):
        w = nfc(w.strip())
        if w:
            lex.add(ao1990(w).lower())
    for f in glob.glob(os.path.join(RAIZ, 'conteudo', 'machado-de-assis', '*.js')) + \
            glob.glob(os.path.join(RAIZ, 'conteudo', 'graciliano-ramos', '*.js')):
        corpo = nfc(open(f, encoding='utf-8').read())
        for m in re.finditer(r'texto: `(.*?)`', corpo, re.S):
            for w in TOKS.findall(m.group(1)):
                if e_palavra(w) and '-' not in w:
                    lex.add(w.lower())
    idx = {}
    for w in lex:
        idx.setdefault(esqueleto(w), []).append(w)
    for w in open('/usr/share/dict/portuguese', encoding='utf-8'):
        w = nfc(w.strip()).lower()
        if w and w not in lex and "'" not in w:
            e = esqueleto(w)
            if e not in idx:
                lex.add(w)
                idx.setdefault(e, []).append(w)
    G._LEX, G._IDX = lex, idx


def nfc(s):
    return unicodedata.normalize('NFC', s)


_lexico_ampliado()

CLITICOS = {'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas', 'me', 'te', 'se', 'lhe', 'lhes', 'vos',
            'o', 'a', 'os', 'as', 'mo', 'ma', 'lho', 'lha'}
TOK = re.compile(r"[A-Za-zÀ-ÿºª0-9]+(?:['’\-][A-Za-zÀ-ÿºª0-9]+)*\.?|\.\.\.|[^\sA-Za-zÀ-ÿ0-9]")
ROMANOS = ['I', 'II']


def nfc(s):
    return unicodedata.normalize('NFC', s)


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


# ------------------------------------------------------------------ leitura da transcrição de 1897

def linhas_1897():
    """(página, linha, texto) da Vida (pp. 3–48, até a assinatura)."""
    out = []
    for p in range(3, 49):
        for k, l in enumerate(open(os.path.join(AQUI, '1897', f'{p:02d}.txt'), encoding='utf-8').read().splitlines(), 1):
            if l.strip() and not l.startswith('[nota]'):
                out.append((p, k, nfc(l.rstrip())))
        if p == 48:
            break
    fim = next(i for i, x in enumerate(out) if x[2].startswith('Codice'))
    return out[:fim]


def palavras_conhecidas(linhas):
    return {sem_acento(w).lower() for _, _, l in linhas for w in re.findall(r'[A-Za-zÀ-ÿ]+', l)}


def juntar(linhas):
    """Blocos: ('titulo', nivel, texto, onde) e ('par', texto, onde). Desfaz a hifenização do fim da linha."""
    conhecidas = palavras_conhecidas(linhas)
    lex = G.lexico()
    blocos = []
    atual = None
    for p, k, l in linhas:
        m = re.match(r'^(#{1,3}) (.*)$', l)
        if m:
            atual = None
            blocos.append(['titulo', len(m.group(1)), m.group(2).strip(), (p, k)])
            continue
        if l.startswith('> '):
            l = l[2:]
            if atual is None or atual[0] != 'pre':
                atual = ['pre', '', (p, k)]
                blocos.append(atual)
        elif l.startswith('¶ ') or atual is None or atual[0] != 'par' or re.match(r'(Fim do Livro|Na Baia a |P\.º RODRIGUES)', l):
            l = l[2:] if l.startswith('¶ ') else l
            atual = ['par', '', (p, k)]
            blocos.append(atual)
        t = atual[1]
        if t.endswith('-'):
            ant = re.search(r'([A-Za-zÀ-ÿ]+)-$', t)
            seg = re.match(r'([A-Za-zÀ-ÿ]+)', l)
            a = ant.group(1) if ant else ''
            b = seg.group(1) if seg else ''
            hifen = b.lower() in CLITICOS and (sem_acento(a).lower() in conhecidas and a.lower() in lex or
                                               a.lower() in D.HIFEN_ANTES) and (a + b).lower() not in D.JUNTAR
            if (a + '-' + b).lower() in D.JUNTAR:
                hifen = False
            atual[1] = t + l if hifen else t[:-1] + l
        else:
            atual[1] = (t + ' ' + l) if t else l
    return blocos


# ------------------------------------------------------------------ grafia

def tokens(s):
    return TOK.findall(s)


def ambiguo(w):
    """Formas do léxico com a mesma chave sem acento: {pratica, prática}."""
    lex = G.lexico()
    lw = w.lower()
    if lw != sem_acento(lw):
        return None
    idx = _idx_acentos()
    formas = idx.get(lw, set())
    if lw in formas and len(formas) > 1:
        return sorted(formas)
    return None


_IA = None


def _idx_acentos():
    global _IA
    if _IA is None:
        _IA = collections.defaultdict(set)
        for w in G.lexico():
            _IA[sem_acento(w)].add(w)
    return _IA


def enclise(t):
    """copial-o → copiá-lo, fazel-o → fazê-lo, reduzil-os → reduzi-los (a forma de 1897 com «l-»)."""
    m = re.match(r'^(.*?)([aeiouô])l-(o|a|os|as)$', t)
    if not m:
        return None
    base, v, pron = m.groups()
    nv = {'a': 'á', 'e': 'ê', 'i': 'i', 'o': 'ô', 'ô': 'ô', 'u': 'u'}[v]
    return G.atual(base + v + 'r')[0][:-2] + nv + '-l' + pron


def modernizar_bloco(texto, onde, rel):
    guardados = []

    def guardar(m):
        guardados.append(m.group(0))
        return f'LATIMXX{len(guardados) - 1}XX'
    for frase in D.LATIM:
        texto = re.sub(r'(?<![A-Za-zÀ-ÿ])' + re.escape(frase) + r'(?![A-Za-zÀ-ÿ])', guardar, texto)
    texto = re.sub(r'_[^_]+_', guardar, texto)          # o que já está em itálico (espanhol)
    out = []
    toks = tokens(texto)
    for i, t in enumerate(toks):
        if not re.match(r'[A-Za-zÀ-ÿ]', t) or t.startswith('LATIMXX'):
            out.append(t)
            continue
        ponto = ''
        if t.endswith('.') and t[:-1].lower() not in D.ABREVIATURAS:
            t, ponto = t[:-1], '.'
        ant = toks[i - 1] if i else ''
        seg = toks[i + 1] if i + 1 < len(toks) else ''
        chave_ctx = f'{t}|{seg.rstrip(".")}'
        lw = t.lower()
        if chave_ctx in D.CONTEXTO:
            novo, fonte = D.CONTEXTO[chave_ctx], 'contexto'
        elif t in D.MANUAL_EXATO:
            novo, fonte = D.MANUAL_EXATO[t], 'manual'
        elif lw in D.MANUAL:
            novo, fonte = G.igualar_caixa(t, D.MANUAL[lw]), 'manual'
        elif lw in ('á', 'ás', 'áquelle', 'áquella', 'áquelles', 'áquellas', 'áquillo'):
            novo, fonte = D.crase(t, seg, ant), 'crase'
            rel['crase'].append((onde, ant, t, seg, novo))
        elif enclise(lw):
            novo, fonte = G.igualar_caixa(t, enclise(lw)), 'enclise'
            rel['enclise'][(t, novo)] += 1
        else:
            amb = ambiguo(t)
            if amb:
                novo = D.desambiguar(t, ant, seg, amb)
                fonte = 'ambiguo'
                rel['ambiguos'][(lw, '|'.join(amb), novo.lower())].append(f'{ant} {t} {seg}')
                novo = G.igualar_caixa(t, novo)
            else:
                t0 = t
                if re.search(r'[áéíó](ra|ras|ram)$', lw) and len(re.findall(r'[áéíóúâêôãõ]', lw)) == 1:
                    t0 = re.sub(r'[áéíó](?=(ra|ras|ram|ramos)$)', lambda m: G.CAIDOS[m.group(0)], t)   # fallára, obrára: mais-que-perfeito
                novo, fonte = G.atual(t0)
                if t0 != t:                     # o esqueleto pode dar o futuro (quebrantará): fica o mais-que-perfeito
                    novo = re.sub(r'[áéíó](?=(ra|ras|ram)$)', lambda m: G.CAIDOS[m.group(0)], novo)
                novo = G.composto(novo)
        if fonte in ('SEM_PAR', 'esqueleto'):
            rel[fonte][(t, novo)] += 1
        elif novo.lower() == t.lower() and re.search(r'([bcdfglmnprt])\1|ph|th|y|ae$|aes$|eo$|eos$|^h[aeiou]|sc[ei]|ct|pt|mn|z$|oe$|ue$', t.lower()):
            rel['suspeitas'][t] += 1
        out.append(novo + ponto)
    s = ' '.join(out)
    s = re.sub(r' ([,.;:!?)])', r'\1', s)
    s = re.sub(r'\( ', '(', s)
    s = re.sub(r'(\d)\. (\d{3})', r'\1.\2', s)
    s = re.sub(r'_ (.*?) _', r'_\1_', s)
    for k in reversed(range(len(guardados))):
        g = guardados[k]
        s = s.replace(f'LATIMXX{k}XX', g if g.startswith('_') or '_LATIMXX' in s else '_' + g + '_')
    return s


def estrutura():
    """[{parte, titulo, preambulo, caps: [{n, titulo, pars: [(texto1897, onde)]}]}]"""
    blocos = juntar(linhas_1897())
    partes = []
    for b in blocos:
        if b[0] == 'titulo':
            nivel, t = b[1], b[2]
            if re.match(r'^1\.ª PARTE$', t) or re.match(r'^2\.ª Parte', t):
                partes.append({'titulo': t, 'subtitulo': '', 'pre': [], 'caps': []})
            elif nivel == 1 and partes and not partes[-1]['caps'] and partes[-1]['titulo'].startswith('2.ª'):
                partes[-1]['subtitulo'] = t
            elif nivel == 1:
                partes[-1]['cabeca'] = t
            elif t.startswith('CAPITULO'):
                n = int(re.search(r'\d+', t).group(0))
                partes[-1]['caps'].append({'n': n, 'titulo': '', 'pars': [], 'onde': b[3]})
            elif nivel == 3:
                partes[-1]['caps'][-1]['titulo'] = t
            else:
                raise ValueError(b)
        elif b[0] == 'pre':
            partes[-1]['pre'].append((b[1], b[2]))
        else:
            if not partes[-1]['caps']:
                raise ValueError(b)
            partes[-1]['caps'][-1]['pars'].append((b[1], b[2]))
    return partes


def preparar(texto, onde, rel):
    """As decisões sobre o texto de 1897, antes da grafia: marcas de Barata, erros, emendas, abreviaturas.
    Cada uma vale na página em que começa o parágrafo ou nas duas seguintes (parágrafo que passa de página)."""
    perto = lambda pag: onde[0] <= pag <= onde[0] + 2
    for pag, de, _ in D.OMITIDAS:
        if perto(pag) and de in texto:
            texto = texto.replace(de, '', 1); rel['usadas'].add(('omit', pag, de))
    for pag, de, para, _ in D.ERROS:
        if perto(pag) and de in texto:
            texto = texto.replace(de, para, 1); rel['usadas'].add(('erro', pag, de))
    for pag, de, para in D.COMPOSICAO + D.EMENDAS:
        if perto(pag) and de in texto:
            texto = texto.replace(de, para, 1); rel['usadas'].add(('comp', pag, de))
    for rx, sub in D.PRE:
        texto = re.sub(rx, sub, texto)
    return texto


def modernizado():
    rel = {'SEM_PAR': collections.Counter(), 'esqueleto': collections.Counter(), 'crase': [],
           'ambiguos': collections.defaultdict(list), 'enclise': collections.Counter(), 'usadas': set(), 'suspeitas': collections.Counter()}
    partes = estrutura()
    # os ERROS valem na página em que começa o parágrafo ou na seguinte
    for p in partes:
        p['pre_m'] = [modernizar_bloco(preparar(t, o, rel), o, rel) for t, o in p['pre']]
        p['titulo_m'] = modernizar_bloco(p['titulo'], (0, 0), rel)
        p['subtitulo_m'] = modernizar_bloco(p['subtitulo'], (0, 0), rel) if p['subtitulo'] else ''
        for c in p['caps']:
            c['titulo_m'] = modernizar_bloco(c['titulo'], c['onde'], rel) if c['titulo'] else ''
            c['pars_m'] = []
            for t, o in c['pars']:
                c['pars_m_1897'] = None
                t2 = preparar(t, o, rel)
                c['pars_m'].append(D.depois(modernizar_bloco(t2, o, rel)))
    return partes, rel


def relatorios(rel):
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    with open(os.path.join(AQUI, 'relatorios', 'sem_par.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['SEM_PAR'].items(), key=lambda x: -x[1]):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'esqueleto.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['esqueleto'].items()):
            f.write(f'{a}\t{b}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'ambiguos.tsv'), 'w', encoding='utf-8') as f:
        for (lw, fs, esc), ctx in sorted(rel['ambiguos'].items()):
            f.write(f'{lw}\t{fs}\t{esc}\t{len(ctx)}\t{" / ".join(ctx[:4])}\n')
    with open(os.path.join(AQUI, 'relatorios', 'crase.tsv'), 'w', encoding='utf-8') as f:
        for x in rel['crase']:
            f.write('\t'.join(map(str, x)) + '\n')
    with open(os.path.join(AQUI, 'relatorios', 'suspeitas.tsv'), 'w', encoding='utf-8') as f:
        for a, n in sorted(rel['suspeitas'].items()):
            f.write(f'{a}\t{n}\n')
    with open(os.path.join(AQUI, 'relatorios', 'enclise.tsv'), 'w', encoding='utf-8') as f:
        for (a, b), n in sorted(rel['enclise'].items()):
            f.write(f'{a}\t{b}\t{n}\n')


def gravar_atual(partes):
    os.makedirs(os.path.join(AQUI, 'atual'), exist_ok=True)
    for p in partes:
        for c in p['caps']:
            corpo = f'## Capítulo {c["n"]}' + (f' — {c["titulo_m"]}' if c['titulo_m'] else '') + '\n\n' + '\n\n'.join(c['pars_m'])
            open(os.path.join(AQUI, 'atual', f'cap-{c["n"]:02d}.txt'), 'w', encoding='utf-8').write(corpo + '\n')


if __name__ == '__main__':
    partes, rel = modernizado()
    relatorios(rel)
    faltam = [x for x in [('omit', a, b) for a, b, _ in D.OMITIDAS] + [('erro', a, b) for a, b, _, _ in D.ERROS] +
              [('comp', a, b) for a, b, _ in D.COMPOSICAO + D.EMENDAS] if x not in rel['usadas']]
    if faltam:
        print('NÃO APLICADAS:', faltam)
    gravar_atual(partes)
    print('sem par:', sum(rel['SEM_PAR'].values()), len(rel['SEM_PAR']), '| esqueleto:', len(rel['esqueleto']),
          '| ambíguos:', len(rel['ambiguos']), '| crase:', len(rel['crase']))
    if '--publicar' in sys.argv:
        import publicar
        publicar.gravar(partes)
