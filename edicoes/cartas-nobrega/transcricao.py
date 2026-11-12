"""Cartas do Brasil (Nóbrega) — do voto das três leituras (voto.py) à transcrição de 1886 por página
(1886/<p>.txt, p = página do PDF da Brasiliana; página impressa = p − 16).

  python3 -I edicoes/cartas-nobrega/transcricao.py [PASTA]

Tira o cabeçalho corrente (linhas «H») e as notas de rodapé de Valle Cabral (linhas «N»), resolve cada
⟦a|b|c⟧ pela palavra que aparece inteira, sem dúvida, em outros pontos do volume (freqüência) e, no empate, pela
primeira leitura (Tesseract 450 dpi), e cada ⟨x/y/z⟩ (pontuação) pela maioria. Sobra em relatorios/duvidas.tsv o que
nenhuma leitura sustenta (a conferir na imagem). Os títulos e sumários das cartas, que a máscara do PDF perde
em parte, não vêm daqui: ficam em cartas.py.
"""
import collections
import os
import re
import sys
import unicodedata

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-nobrega')
AQUI = os.path.dirname(os.path.abspath(__file__))
PAGINAS = range(62, 201)
DUV = re.compile(r'⟦([^⟧]*)⟧')
PONT = re.compile(r'⟨([^⟩]*)⟩')
PAL = re.compile(r"[A-Za-zÀ-ÿ]+")


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def ler_paginas():
    out = {}
    for p in PAGINAS:
        out[p] = open(os.path.join(PASTA, 'voto', f'{p}.txt'), encoding='utf-8').read().splitlines()
    return out


def separar(l):
    """«H »/«N »/«¶ » + texto + TAB + recuo (px, 450 dpi) → (marca, texto, recuo)."""
    txt, _, rec = l.rpartition('\t')
    m = re.match(r'^(H |N |¶ )?(.*)$', txt, re.S)
    return (m.group(1) or '').strip(), re.sub(r'^¶ ', '', m.group(2)), int(rec) if rec.isdigit() else 0


def frequencia(pags):
    f = collections.Counter()
    for linhas in pags.values():
        for l in linhas:
            if l[:2] in ('H ', 'N '):
                continue
            l = DUV.sub(' ', separar(l)[1])
            for w in PAL.findall(l):
                f[w.lower()] += 1
    return f


def escolher(cands, f, duv, onde):
    pontos = []
    for i, c in enumerate(cands):
        ws = PAL.findall(c)
        # só conta a palavra inteira (cada candidato é uma palavra com pontuação)
        pts = sum(f.get(w.lower(), 0) for w in ws) if ws else 0
        pontos.append((pts, -i))
    melhor = max(range(len(cands)), key=lambda i: pontos[i])
    escolha = cands[melhor]
    pts = sorted(p[0] for p in pontos)
    # duvidosa: nenhuma leitura é conhecida, ou duas conhecidas que diferem além de acento/caixa
    conhecidas = [c for c, p in zip(cands, pontos) if p[0] >= 2]
    difere = {sem_acento(c.lower()) for c in conhecidas}
    if not conhecidas or len(difere) > 1:
        duv.append((onde, '|'.join(cands), escolha))
    return escolha


def resolver(l, f, duv, onde):
    l = DUV.sub(lambda m: escolher(m.group(1).split('|'), f, duv, onde), l)

    def pont(m):
        c = m.group(1).split('/')
        n = collections.Counter(c)
        v, k = n.most_common(1)[0]
        return v if k >= 2 else c[0]
    return PONT.sub(pont, l)


def main():
    pags = ler_paginas()
    f = frequencia(pags)
    duv = []
    os.makedirs(os.path.join(AQUI, '1886'), exist_ok=True)
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    cab = []
    for p, linhas in pags.items():
        saida = []
        sep = [separar(l) for l in linhas]
        corpo = sorted(r for m, t, r in sep if m not in ('H', 'N') and r)
        mediana = corpo[len(corpo) // 2] if corpo else 0
        # nota de rodapé também pela numeração: a primeira linha de depois de 30% da página que começa por «N) »
        n_ini = next((k for k, (m, t, r) in enumerate(sep) if m != 'H' and k >= 0.3 * len(sep) and
                      re.match(r'^\s*\(?\d{1,3}\)\s*\S', re.sub(r'⟦([^|⟧]*)[^⟧]*⟧', r'\1', t))), None)
        for k, (marca, txt, rec) in enumerate(sep):
            if n_ini is not None and k >= n_ini and marca != 'H' and not re.match(r'^\(?(Da|De|Desta|Deste)\b.{0,50}(15\d\d|Bahia\.\))', txt):
                continue
            if marca == 'H':
                if len(txt) > 45 and not re.search(r'NOBREGA|NÓBREGA|BRASIL|CARTAS', txt):
                    cab.append((p, txt))
                continue
            if marca == 'N' and not re.match(r'^\(?(Da|De|Desta|Deste)\b.{0,50}(15\d\d|Bahia\.\))', txt):
                continue            # (a data e o lugar do fim da carta, que o tamanho da letra confunde com nota, ficam)
            ini = '¶ ' if rec > mediana + 45 else ''
            saida.append(ini + resolver(txt, f, duv, (p, k + 1)))
        open(os.path.join(AQUI, '1886', f'{p}.txt'), 'w', encoding='utf-8').write('\n'.join(saida) + '\n')
    with open(os.path.join(AQUI, 'relatorios', 'duvidas.tsv'), 'w', encoding='utf-8') as fo:
        for (p, k), c, e in duv:
            fo.write(f'{p}\t{k}\t{c}\t{e}\n')
    print('dúvidas sem solução:', len(duv), '| cabeçalhos suspeitos:', cab[:5])


if __name__ == '__main__':
    main()
