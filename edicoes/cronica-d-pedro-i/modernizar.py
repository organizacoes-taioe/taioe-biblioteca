"""Crónica de D. Pedro I — passo 5: a grafia de hoje (Acordo de 1990, forma brasileira), palavra por
palavra, conservando as palavras e a ordem do texto de 1816.

    python3 -I edicoes/cronica-d-pedro-i/modernizar.py <pasta>

Lê <pasta>/estab.json (estabelecer.py, com as correções de decisoes.py já aplicadas por montar.py) e
grava <pasta>/moderno.json (a forma de hoje de cada palavra) e os relatórios <pasta>/sem_par.tsv
(o que nenhuma regra resolveu) e <pasta>/trocas.tsv (todas as trocas, por tipo, para conferir).

Para cada palavra de 1816:
1. a tabela à mão (grafia.py, GRAFIA): a forma de hoje decidida por tipo; «=95» quer dizer «a
   palavra de 1895 alinhada» (para as formas de duplo sentido: maao = mão ou mau);
2. se a palavra de 1895 alinhada for a MESMA palavra (só a grafia muda: dereito/direito,
   molher/mulher, iustiça/justiça), a grafia de hoje da forma de 1895 (léxico + esqueleto, como em
   São Bernardo), com os ajustes de GRAFIA95;
3. senão, regras de grafia sobre a forma de 1816 e o léxico; o que sobrar vai para sem_par.tsv.
A edição de 1895 às vezes troca a palavra (prouguerom → aprouveram, ouro → oiro, hu → onde):
por isso o passo 2 só vale quando a chave das duas formas é a mesma (K).
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
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, AQUI)
import grafia1990 as G  # noqa: E402
from grafia import GRAFIA, GRAFIA95  # noqa: E402

# a cauda (tipos que as regras não resolveram), decidida tipo a tipo: grafia-cauda.tsv
CAUDA, OCR, LIXO = {}, {}, set()
for _l in open(os.path.join(AQUI, 'grafia-cauda.tsv'), encoding='utf-8').read().splitlines()[1:]:
    _c = (_l.split('\t') + [''] * 5)[:5]
    if _c[3] == 'lixo':
        LIXO.add(_c[0])
        continue
    if _c[1] and _c[1] != _c[0]:
        OCR[_c[0]] = _c[1]
    if _c[2]:
        CAUDA[_c[1] or _c[0]] = _c[2]
        CAUDA.setdefault(_c[0], _c[2])


def sa(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))


def K(w):
    """Chave que iguala a grafia de 1816 e a de 1895 da mesma palavra."""
    k = sa(w).lower().replace("'", '').replace('’', '').replace('-', '')
    k = k.replace('ç', 's').replace('y', 'i').replace('j', 'i').replace('h', '')
    k = re.sub(r'(ões|oes|oens|ooes|oões)$', 'OES', k)
    k = re.sub(r'(om|am|ao|aom)$', 'AM', k)
    k = re.sub(r'(oms|ams|aos)$', 'AMS', k)
    k = re.sub(r'ens$', 'es', k)
    k = re.sub(r'([a-z])\1+', r'\1', k)
    k = re.sub(r'm(?=[^aeiouAMOES])', 'n', k)
    k = k.replace('z', 's').replace('qu', 'k').replace('c', 'k')
    k = re.sub(r'k(?=[ei])', 's', k)
    k = re.sub(r'g(?=[ei])', 'i', k)
    k = k.replace('ph', 'f').replace('th', 't')
    k = k.replace('u', 'o').replace('e', 'i')
    return re.sub(r'([a-z])\1+', r'\1', k)


def caixa(modelo, w):
    if not w:
        return w
    if modelo[:1].isupper():
        return w[0].upper() + w[1:]
    return w


def de95(a):
    """A grafia de hoje de uma palavra de 1895."""
    la = a.lower().replace('’', "'")
    m = re.match(r"^([dn])'(.+)$", la)
    if m and la not in GRAFIA95:                      # d'essa → dessa, n'aquelle → naquele
        resto = GRAFIA95.get(m.group(2)) or G.atual(m.group(2))[0]
        return caixa(a, m.group(1) + resto)
    if la in GRAFIA95:
        n = GRAFIA95[la]
    else:
        n, _ = G.atual(la)
    return caixa(a, n)


REGRAS = [   # 1816 → hoje, antes do léxico (só grafia)
    (r'^huum$', 'um'), (r'^huuma$', 'uma'), (r'^huma$', 'uma'), (r'^huns$', 'uns'), (r'^humas$', 'umas'),
    (r'^nom$', 'não'), (r'uu', 'u'), (r'ee', 'e'), (r'oo', 'o'), (r'aa', 'a'), (r'ii', 'i'),
    (r'ç(?=[ei])', 'c'), (r'mj', 'mi'), (r'nj', 'ni'), (r'ij', 'i'), (r'y', 'i'),
    (r'rom$', 'ram'), (r'om$', 'ão'), (r'm(?=[^aeiouãõbp\W]|$)', 'n'), (r'll', 'l'), (r'ss(?=$)', 's'), (r'ff', 'f'), (r'tt', 't'),
    (r'^h(?=[aeiou])', ''), (r'th', 't'), (r'ph', 'f'), (r'om$', 'ão'), (r'oens$', 'ões'), (r'ooes$', 'ões'),
]


def regras(w):
    lw = w.lower()
    for a, b in REGRAS:
        lw = re.sub(a, b, lw)
    n, fonte = G.atual(lw)
    return n, fonte


def modernizar(E):
    rel_sem, trocas = collections.Counter(), collections.Counter()
    for p in E:
        for campo in ('titulo', 'corpo'):
            for x in p[campo]:
                if 'p' in x:
                    x['m'] = x['t']
                    continue
                w, a, op = x['t'], x.get('a95', ''), x.get('op')
                lw = w.lower()
                tab = GRAFIA.get(lw, CAUDA.get(lw))
                if tab is not None:
                    n = tab
                    if n == '=95':
                        n = de95(a) if a and op in ('equal', 'replace') else regras(w)[0]
                    fonte = 'tabela'
                elif a and op in ('equal', 'replace') and K(w) == K(a):
                    n, fonte = de95(a), '1895'
                else:
                    n, fonte = regras(w)
                    if fonte == 'SEM_PAR':
                        rel_sem[(lw, a.lower() if a else '#' + str(op))] += 1
                n = n if fonte == '1895' else caixa(w, n)
                x['m'] = n
                trocas[(fonte, lw, n.lower(), (a or '').lower())] += 1
    return rel_sem, trocas


def main(pasta):
    E = json.load(open(os.path.join(pasta, 'estab.json'), encoding='utf-8'))
    rel, trocas = modernizar(E)
    json.dump(E, open(os.path.join(pasta, 'moderno.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    with open(os.path.join(pasta, 'sem_par.tsv'), 'w', encoding='utf-8') as f:
        for (w, a), n in rel.most_common():
            f.write(f'{w}\t{a}\t{n}\n')
    with open(os.path.join(pasta, 'trocas.tsv'), 'w', encoding='utf-8') as f:
        for (fo, w, n, a), c in sorted(trocas.items(), key=lambda kv: -kv[1]):
            f.write(f'{fo}\t{w}\t{n}\t{a}\t{c}\n')
    print(len(rel), 'tipos sem par;', sum(rel.values()), 'ocorrências')


if __name__ == '__main__':
    main(sys.argv[1])
