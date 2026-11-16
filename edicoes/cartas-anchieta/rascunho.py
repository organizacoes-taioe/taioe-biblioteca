"""Cartas de Anchieta — do voto ao rascunho e do rascunho conferido à transcrição de 1933.

  python3 edicoes/cartas-anchieta/rascunho.py [PASTA]           # voto → PASTA/rascunho/<folha>.txt e .json
  python3 edicoes/cartas-anchieta/rascunho.py [PASTA] --aplicar  # + conferencia.tsv → 1933/<folha>.txt

O rascunho tira o cabeço da página (o título corrido), o número da página, na primeira folha da peça o que vem
antes do texto (número, título e sumário de 1933: pecas.INICIO dá o começo do texto) e, na última, as notas
(da linha «NOTAS» em diante). A conferência nas imagens (conferir.py, pranchas) grava em conferencia.tsv a
leitura certa de cada linha duvidosa: folha<TAB>linha<TAB>texto (texto «-» apaga a linha).
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import pecas  # noqa: E402

APLICAR = '--aplicar' in sys.argv[1:]
args = [a for a in sys.argv[1:] if not a.startswith('--')]
PASTA = os.path.expanduser(args[0] if args else '~/.cache/claude-pedidos-0511/cartas-anchieta')
sys.argv = [sys.argv[0], PASTA]
import voto  # noqa: E402

CABECO = re.compile(r'^[¶ ]*(?:[⟦\[|]?\S{0,6}[.,]?\s*[—–-]+\s*(CARTA|INFORMA|SERM)|JOSEPH|JOSEPI|JOSEPII|[IVXLT1]+\.? ?[—–-] )', re.I)


def limpar(f, linhas, caixas, peca):
    pares = list(zip(linhas, caixas))
    if pares and (CABECO.search(pares[0][0]) or re.match(r'^[¶ ]*[IVXL]+\.?\s*$', pares[0][0])):
        pares = pares[1:]
    while pares and re.match(r'^[¶ ⟦⟧|\d\W]*$', pares[-1][0]):      # número da página, sujeira
        pares = pares[:-1]
    if f == peca[1]:
        inicio = pecas.INICIO[peca[0]]
        k = next((i for i, (l, _) in enumerate(pares) if inicio in l.replace('¶ ', '')), None)
        if k is None:
            raise SystemExit(f'folha {f}: não achei o início «{inicio}»')
        pares = pares[k:]
    if f == peca[2]:
        k = next((i for i, (l, _) in enumerate(pares) if re.match(r'^[¶ ]*NOTAS?\b', l)), None)
        if k is not None:
            pares = pares[:k]
    return [l for l, _ in pares], [c for _, c in pares]


UNICO = re.compile(r'⟦([^|⟧]*)⟧[^\s]*')


def sem_ruido(l):
    """Tira das pontas da linha o que só uma leitura viu e é curto (sujeira da margem: ⟦a⟧, ⟦4⟧, ⟦am⟧)."""
    pal = l.split(' ')
    while pal and UNICO.fullmatch(pal[-1]) and len(UNICO.fullmatch(pal[-1]).group(1)) <= 3:
        pal.pop()
    ini = 1 if pal and pal[0] == '¶' else 0
    while len(pal) > ini and UNICO.fullmatch(pal[ini]) and len(UNICO.fullmatch(pal[ini]).group(1)) <= 3:
        pal.pop(ini)
    return ' '.join(pal)


DUVIDA = re.compile(r'⟦([^⟧]*)⟧')


def decidir(l):
    """⟦a|b|c⟧: se uma só das leituras (sem pontuação) é palavra do léxico, fica ela."""
    import lexico

    def um(m):
        cands = m.group(1).split('|')
        boas = {c for c in cands if re.sub(r'[^A-Za-zÀ-ÿ’\'-]', '', c) and lexico.ok(re.sub(r'[^A-Za-zÀ-ÿ’\'-]', '', c))}
        nomes = {c for c in boas if c[:1].isupper()}
        if len(boas) == 1 and not nomes:
            return boas.pop()
        return m.group(0)
    return DUVIDA.sub(um, l)


FIM_DE_FRASE = re.compile(r'[.!?:”)]\S*$|Amen\.?$')


def paragrafos(seq, direita):
    """Refaz os «¶» de uma peça pela forma das linhas: abre parágrafo a linha que vem depois de uma linha que
    acaba frase e é curta (não chega à margem direita da folha) ou que, ela mesma, começa recuada (o «¶» do voto;
    o recuo sozinho engana nas páginas tortas). A linha conferida nas pranchas fica com o «¶» que a conferência
    deu. seq: [[folha, texto, caixa, conferida]] na ordem; muda os textos no lugar."""
    for i, x in enumerate(seq):
        f, l, cx, conf = x
        recuo = l.startswith('¶ ')
        corpo = l[2:] if recuo else l
        if i == 0:
            x[1] = '¶ ' + corpo
            continue
        if conf:
            continue
        pf, pl, pc, _ = seq[i - 1]
        curta = pc[2] < direita[pf] - 90
        acaba = bool(FIM_DE_FRASE.search(pl.rstrip()))
        x[1] = ('¶ ' if acaba and (curta or recuo) else '') + corpo


def rascunho():
    os.makedirs(os.path.join(PASTA, 'rascunho'), exist_ok=True)
    total = 0
    for p in pecas.PECAS:
        folhas = []
        for f in pecas.folhas_de(p):
            linhas, d, caixas = voto.pagina(f)
            linhas, caixas = limpar(f, [decidir(sem_ruido(l)) for l in linhas], caixas, p)
            total += sum(l.count('⟦') + l.count('⟨') for l in linhas)
            folhas.append((linhas, caixas))
        for f, (linhas, caixas) in zip(pecas.folhas_de(p), folhas):
            open(os.path.join(PASTA, 'rascunho', f'{f}.txt'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
            json.dump(caixas, open(os.path.join(PASTA, 'rascunho', f'{f}.json'), 'w'))
    print('dúvidas do voto:', total)


def aplicar():
    conf, novas = {}, {}
    arq = os.path.join(AQUI, 'conferencia.tsv')
    for l in open(arq, encoding='utf-8').read().splitlines():
        if l.strip() and not l.startswith('#'):
            f, k, t = l.split('\t', 2)
            if k.endswith('+'):                    # linha que a leitura perdeu: entra depois da linha k
                if t.strip() != '-':
                    novas.setdefault((int(f), int(k[:-1])), []).append(t)
            else:
                conf[(int(f), int(k))] = t
    os.makedirs(os.path.join(AQUI, '1933'), exist_ok=True)
    restam = []
    for p in pecas.PECAS:
        seq, direita = [], {}
        for f in pecas.folhas_de(p):
            linhas = open(os.path.join(PASTA, 'rascunho', f'{f}.txt'), encoding='utf-8').read().splitlines()
            caixas = json.load(open(os.path.join(PASTA, 'rascunho', f'{f}.json')))
            direita[f] = sorted(c[2] for c in caixas)[len(caixas) * 3 // 4] if caixas else 0
            for t in novas.get((f, -1), []):
                seq.append([f, t, [0, 0, direita[f], 0], True])
            for k, (l, cx) in enumerate(zip(linhas, caixas)):
                t = conf.get((f, k), l)
                if not (t.strip() in ('-', '', '¶') or (f, k) not in conf and CABECO.search(t)
                        or re.match(r'^(¶ )?[IVXL]+\.? ?— ?(CARTA|INFORMA|SERM)', t)):
                    if '⟦' in t or '⟨' in t:
                        restam.append((f, k, t))
                    for parte in t.split(' ⏎ '):           # «⏎» na conferência: a linha vira duas
                        seq.append([f, parte, cx, (f, k) in conf])
                for t2 in novas.get((f, k), []):           # linhas perdidas pela leitura, conferidas
                    seq.append([f, t2, [0, cx[1], direita[f], cx[3]], True])
        paragrafos(seq, direita)
        for f in pecas.folhas_de(p):
            out = [x[1] for x in seq if x[0] == f]
            open(os.path.join(AQUI, '1933', f'{f}.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('linhas conferidas:', len(conf), '| ainda com dúvida:', len(restam))
    for x in restam[:30]:
        print(*x, sep='\t')


if __name__ == '__main__':
    if APLICAR:
        aplicar()
    else:
        rascunho()
