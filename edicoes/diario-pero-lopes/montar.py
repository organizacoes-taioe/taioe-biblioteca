"""Diário da navegação (Pero Lopes de Sousa) — da transcrição de 1839 (1839/NN.txt, conferida nas imagens)
ao texto na grafia de hoje.

  python3 edicoes/diario-pero-lopes/montar.py              # grava atual/ e relatorios/ (fora do git)
  python3 edicoes/diario-pero-lopes/montar.py --publicar   # e conteudo/pero-lopes-de-sousa/diario-da-navegacao.js

Grafia: `edicoes/sao-bernardo/grafia1990.py` (léxico do sistema) mais as decisões de `decisoes.py`.
"""
import collections
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'edicoes', 'sao-bernardo'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, AQUI)
import grafia1990 as G  # noqa: E402
import decisoes as D  # noqa: E402

CLITICOS = {'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas', 'me', 'te', 'se', 'lhe', 'lhes', 'vos', 'o', 'a',
            'os', 'as', 'mo', 'ma', 'lho', 'lha', 'lhos', 'lhas', 'mos'}
PAL = r"[A-Za-zÀ-ÿẽũ'’º]"


def nfc(s):
    return unicodedata.normalize('NFC', s)


def paginas():
    """Linhas impressas de pp. 3–59 (uma linha por linha)."""
    L = []
    for p in range(3, 60):
        L += [nfc(l.rstrip()) for l in open(os.path.join(AQUI, '1839', f'{p:02d}.txt'), encoding='utf-8') if l.strip()]
    return L


def juntar(L):
    """Texto corrido; desfaz a hifenização de fim de linha (o hífen fica se for de «demorava-me»)."""
    t = '\n'.join(L)
    t = re.sub(r'-\n(?=\w)', '¬', t).replace('\n', ' ')
    t = re.sub(r'\s+', ' ', t)
    todas = set(re.findall(r"[A-Za-zÀ-ÿẽũ'’-]+", t.replace('¬', '')))

    def f(m):
        a, b = m.group(1), m.group(2)
        if (a + '-' + b).lower() in D.COM_HIFEN:
            return a + '-' + b
        if (a + b) in todas or (a + b).lower() in D.JUNTAR:
            return a + b
        if a + '-' + b in todas or b.lower() in CLITICOS:
            return a + '-' + b
        return a + b
    t = re.sub(r"(%s+)¬(%s+)" % (PAL, PAL), f, t)
    return t.replace('¬', '-')


def entradas(t):
    """Uma entrada por dia: começa no nome do dia da semana (ou na data solta)."""
    pat = r'(?=(?:Domingo|Segundafeira|Terçafeira|Quartafeira|Quintafeira|Sestafeira|Sabado) |Aos cinco dias do mes de febreiro)'
    return [x.strip() for x in re.split(pat, t) if x.strip()]


def atual_token(t, seg, rel):
    if t in D.MANUAL_EXATO:
        return D.MANUAL_EXATO[t]
    lw = t.lower()
    if lw in D.MANUAL:
        return G.igualar_caixa(t, D.MANUAL[lw])
    if '-' in t:
        ps = t.split('-')
        return '-'.join(p if k and p.lower() in CLITICOS else atual_token(p, '', rel) for k, p in enumerate(ps))
    novo, fonte = G.atual(t)
    rel[fonte][(t, novo)] += 1
    return novo


def modernizar(texto, rel):
    for de, para in D.PRE:
        texto = re.sub(de, para, texto)
    out = []
    toks = re.findall(r"[A-Za-zÀ-ÿẽũº]+(?:['’\-][A-Za-zÀ-ÿẽũ]+)*|\d+|\.\.\.|[^\sA-Za-zÀ-ÿ0-9]", texto)
    for i, t in enumerate(toks):
        if not re.match(r'[A-Za-zÀ-ÿẽũ]', t):
            out.append(t)
            continue
        seg = toks[i + 1] if i + 1 < len(toks) else ''
        out.append(atual_token(t, seg, rel))
    s = ' '.join(out)
    s = re.sub(r' ([,.;:!?)»])', r'\1', s)
    s = re.sub(r'([«(]) ', r'\1', s)
    for de, para in D.POS:
        s = re.sub(de, para, s)
    return s


def estrutura():
    t = juntar(paginas())
    es = entradas(t)
    return es


def gerar():
    rel = {'SEM_PAR': collections.Counter(), 'esqueleto': collections.Counter(), 'lexico': collections.Counter(),
           'manual': collections.Counter()}
    es = estrutura()
    mod = [D.corrigir(e) for e in es]
    mod = [modernizar(e, rel) for e in mod]
    return es, mod, rel


if __name__ == '__main__':
    es, mod, rel = gerar()
    os.makedirs(os.path.join(AQUI, 'relatorios'), exist_ok=True)
    with open(os.path.join(AQUI, 'relatorios', 'trocas.tsv'), 'w', encoding='utf-8') as f:
        for k in ('SEM_PAR', 'esqueleto', 'lexico'):
            for (a, b), n in sorted(rel[k].items()):
                if a != b or k == 'SEM_PAR':
                    f.write(f'{k}\t{a}\t{b}\t{n}\n')
    open(os.path.join(AQUI, 'relatorios', 'atual.txt'), 'w', encoding='utf-8').write('\n\n'.join(mod))
    print(len(es), 'entradas;', sum(len(m.split()) for m in mod), 'palavras; sem par:', len(rel['SEM_PAR']))
    if '--publicar' in sys.argv:
        import publicar
        publicar.gravar(es, mod)
