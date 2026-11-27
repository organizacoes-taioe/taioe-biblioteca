"""Vida de D. Frei Bertolameu dos Mártires — voto dos testemunhos alinhados (colacao.py) palavra a palavra.

  python3 -I edicoes/vida-de-frei-bartolomeu/votar.py      # grava PASTA/voto.json e PASTA/relatorios/*.tsv

Unidade de voto: uma palavra da referência (1619, BNP) ou o vão antes dela (palavra que a referência não
leu); unidades se juntam quando algum testemunho lê junto o que outro separa. Dois grupos:
  1619: bnp (1), ia (1), ga (0,5)          Lisboa: r185 (1), r1818 (1), gr185 (0,6), gr1818 (0,6)
Regras (ver decidir()): os dois grupos concordam → aceita, na forma de Lisboa (sem ſ e sem abreviaturas);
cada grupo firme mas diferentes → variante (fica 1619; relatorios/variantes.tsv); resto → maioria geral
com apoio dos dois lados, ou dúvida (relatorios/duvidas.tsv), para a conferência nas imagens.
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

PESO = {'bnp': 1.0, 'ia': 1.0, 'ga': 0.5, 'r185': 1.0, 'r1818': 1.0, 'gr185': 0.6, 'gr1818': 0.6}
G1619 = ('bnp', 'ia', 'ga')
GLIS = ('r185', 'r1818', 'gr185', 'gr1818')
ORDEM_FORMA = ('r185', 'r1818', 'gr185', 'gr1818', 'bnp', 'ia', 'ga')
SEM_COBERTURA = 12        # 'del' maior que isto: o testemunho não tem o trecho (página que falta), não vota


def carregar():
    col = os.path.join(T.PASTA, 'colacao')
    ref = json.load(open(os.path.join(col, 'bnp.json')))
    tests = {}
    for nome in PESO:
        if nome == 'bnp':
            continue
        f = os.path.join(col, nome + '.json')
        if os.path.exists(f):
            tests[nome] = json.load(open(f))
    return ref, tests


def unidades(n, tests):
    """Fronteiras: junta as palavras da referência que algum testemunho cobre com um só grupo."""
    liga = [False] * (n + 1)          # liga[i]: a palavra i se junta à i-1
    for d in tests.values():
        for i0, i1, j0, j1, tp in d['blocos']:
            if tp == 'grp':
                for i in range(i0 + 1, i1):
                    liga[i] = True
    uns = []
    i = 0
    while i < n:
        k = i + 1
        while k < n and liga[k]:
            k += 1
        uns.append((i, k))
        i = k
    return uns


def leituras(n, tests, uns):
    """Para cada testemunho: texto que dá a cada unidade (lista de palavras; [] = nada; None = não cobre) e
    o que insere antes de cada unidade."""
    de_unidade = {}
    for u, (a, b) in enumerate(uns):
        for i in range(a, b):
            de_unidade[i] = u
    out = {}
    for nome, d in tests.items():
        pal = d['palavras']
        txt = [None] * len(uns)
        ins = collections.defaultdict(list)
        for i0, i1, j0, j1, tp in d['blocos']:
            if tp in ('eq', 'sub', 'grp'):
                u = de_unidade[i0]
                if txt[u] is None:
                    txt[u] = []
                txt[u] += [pal[j]['t'] for j in range(j0, j1)]
            elif tp == 'del':
                if i1 - i0 <= SEM_COBERTURA:
                    for i in range(i0, i1):
                        u = de_unidade[i]
                        if txt[u] is None:
                            txt[u] = []
            elif tp == 'ins':
                if j1 - j0 <= SEM_COBERTURA and i0 < n:
                    ins[de_unidade[i0]] += [pal[j]['t'] for j in range(j0, j1)]
        # cobertura: unidades entre o primeiro e o último bloco casado
        casadas = [u for u, t in enumerate(txt) if t]
        out[nome] = {'txt': txt, 'ins': ins, 'de': casadas[0] if casadas else 0, 'ate': casadas[-1] if casadas else -1}
    return out


def k_de(palavras):
    return ' '.join(k for k in (C.chave(t) for t in palavras) if k)


def votos(lido, grupo):
    v = collections.Counter()
    formas = {}
    for nome, txt in lido.items():
        if nome in grupo and txt is not None:
            k = k_de(txt)
            v[k] += PESO[nome]
            formas.setdefault(k, {})[nome] = txt
    return v, formas


def firme(v, minimo=1.5):
    if not v:
        return None
    k, p = v.most_common(1)[0]
    segundo = v.most_common(2)[1][1] if len(v) > 1 else 0
    return k if p >= minimo and p > segundo else None


def decidir(lido):
    """lido: {testemunho: [palavras] ou None}. Devolve (chave escolhida, situação)."""
    v16, _ = votos(lido, G1619)
    vl, _ = votos(lido, GLIS)
    k16, kl = firme(v16), firme(vl, 1.5 if sum(vl.values()) > 1.6 else 1.0)
    if k16 is not None and kl is not None:
        if k16 == kl:
            return k16, 'ok'
        return k16, 'var'
    tudo = v16 + vl
    if not tudo:
        return None, 'nada'
    k, p = tudo.most_common(1)[0]
    lados = (k in v16) + (k in vl)
    if p >= 2.0 and lados == 2 and (len(tudo) == 1 or p > 1.5 * tudo.most_common(2)[1][1]):
        return k, 'ok'
    if k16 is not None and not vl:           # Lisboa não cobre (páginas que faltam nas duas edições)
        return k16, 'ok1619'
    return k, 'duv'


def forma(lido, k):
    for nome in ORDEM_FORMA:
        t = lido.get(nome)
        if t is not None and k_de(t) == k:
            return t, nome
    return None, None


def main():
    ref, tests = carregar()
    pal = ref['palavras']
    n = len(pal)
    uns = unidades(n, tests)
    L = leituras(n, tests, uns)
    saida = []
    cont = collections.Counter()
    for u, (a, b) in enumerate(uns):
        # vão antes da unidade: palavras que algum testemunho tem e a referência não
        lido_ins = {'bnp': []}
        for nome, d in L.items():
            if d['de'] <= u <= d['ate'] and d['txt'][u] is not None:
                lido_ins[nome] = d['ins'].get(u, [])
        if any(lido_ins.values()):
            k, sit = decidir(lido_ins)
            if k:
                f, quem = forma(lido_ins, k)
                cont['ins-' + sit] += 1
                saida.append({'u': u, 'i': a, 'vao': True, 'f': f, 'quem': quem, 'sit': sit,
                              'lido': {x: ' '.join(y) for x, y in lido_ins.items()}})
            elif sit != 'nada':
                cont['ins-sem'] += 1
        lido = {'bnp': [pal[i]['t'] for i in range(a, b)]}
        for nome, d in L.items():
            if d['de'] <= u <= d['ate']:
                lido[nome] = d['txt'][u]
        k, sit = decidir(lido)
        f, quem = forma(lido, k)
        cont[sit] += 1
        saida.append({'u': u, 'i': a, 'n': b - a, 'f': f, 'quem': quem, 'sit': sit,
                      'lido': {x: (' '.join(y) if y is not None else None) for x, y in lido.items()}})
    json.dump(saida, open(os.path.join(T.PASTA, 'voto.json'), 'w'), ensure_ascii=False)
    print(dict(cont))


if __name__ == '__main__':
    main()
