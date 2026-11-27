"""Farsa de Inês Pereira: grafia de hoje, palavra por palavra, sobre o texto de 1834 passado a limpo.

Passo 1 do texto (o 2º é `montar.py`, que aplica as lições de 1562). Lê colacao/v1834-A.txt e -B.txt e
grava colacao/moderno-1834.txt. Muda só a maneira de escrever (he → é, hum → um, ella → ela, ph/th,
letras dobradas, -ão átono → -am, z/s, acentos); a forma da palavra fica (pera, assi, cousa, mi, dous).
Cada palavra passa pela tabela GRAFIA (decisões à mão) e, se não estiver nela, por regras conferidas
no léxico (/usr/share/dict/brazilian + os textos das duas Barcas). O que nenhuma regra resolve sai em
colacao/sem-decisao.txt: decidir e pôr na tabela, até o arquivo ficar vazio.

uso: python3 edicoes/farsa-de-ines-pereira/modernizar.py
"""
import os
import re
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.join(AQUI, 'colacao')
RAIZ = os.path.join(AQUI, '..', '..')

import sys  # noqa: E402
sys.path.insert(0, AQUI)
from grafia import GRAFIA, MANTER  # noqa: E402  (tabela à mão, ao lado)


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))


def lexico():
    lex = set()
    for l in open('/usr/share/dict/brazilian', encoding='utf-8', errors='ignore'):
        lex.add(l.strip().lower())
    for obra in ('barca-do-inferno', 'barca-do-purgatorio'):
        t = open(os.path.join(RAIZ, 'edicoes', obra, 'texto.txt'), encoding='utf-8').read()
        lex.update(w.lower() for w in re.findall(r"[A-Za-zÀ-ÿũŨẽ]+", t))
    idx = {}
    for w in lex:
        idx.setdefault(sem_acento(w), set()).add(w)
    return lex, idx


LEX, IDX = lexico()


def caixa(modelo, w):
    if modelo.isupper() and len(modelo) > 1:
        return w.upper()
    if modelo[:1].isupper():
        return w[:1].upper() + w[1:]
    return w


def candidatos(w):
    """Formas possíveis de hoje para a palavra de 1834 (minúscula)."""
    c = w
    c = c.replace('ph', 'f').replace('th', 't').replace('y', 'i')
    c = re.sub(r'ch(?=[rl])', 'c', c)
    c = re.sub(r'([bcdfglmnpt])\1', r'\1', c)
    c = re.sub(r'(?<=[aeiou])ct', 't', c)
    c = re.sub(r'(?<=[aeiouâ])nct', 'nt', c)
    c = re.sub(r'^capt', 'cat', c)
    c = re.sub(r'mpt', 'nt', c)
    out = [c]
    if c.endswith('ão'):
        out.append(c[:-2] + 'am')
    if c.endswith('eo'):
        out.append(c[:-2] + 'eu')
    if c.endswith('io'):
        out.append(c[:-2] + 'iu')
    more = []
    for x in out:
        if 'z' in x:
            more.append(re.sub(r'(?<=[aeiouãõâêô])z(?=[aeiou])', 's', x))
            more.append(re.sub(r'z$', 's', x))
        if re.search(r'(?<=[aeiou])c(?=[ei])', x):
            more.append(re.sub(r'(?<=[aeiou])c(?=[ei])', 'sc', x))
        if 's' in x:
            more.append(re.sub(r'(?<=[aeiou])s(?=[aeiou])', 'z', x))
    return out + more


AUTO = {}


def resolver(w):
    lw = w.lower()
    if lw in ('ó', 'á', 'ás'):            # 1834: ó = ao, á = à (o «Ó» do vocativo vem em maiúscula)
        return {'ó': 'ò', 'á': 'à', 'ás': 'às'}[lw] if w == lw else w, True
    if lw in GRAFIA:
        return caixa(w, GRAFIA[lw]), True
    if lw in MANTER:
        return w, True
    if lw in LEX and lw not in ('ella', 'elle'):
        return w, True
    for c in candidatos(lw):
        if c in LEX:
            AUTO[lw] = c
            return caixa(w, c), True
        achados = IDX.get(sem_acento(c), set())
        if len(achados) == 1:
            AUTO[lw] = next(iter(achados))
            return caixa(w, AUTO[lw]), True
    return w, False


# castelhano: as falas do Ermitão e os versos das cantigas castelhanas ficam como em 1834
CASTELHANO = re.compile(r'^\| (Mal herida|Sola va|Mal me quieren)')
PALAVRA = re.compile(r"[A-Za-zÀ-ÿũŨẽ]+")


def modernizar_linha(l, faltam, n):
    def troca(m):
        novo, ok = resolver(m.group())
        if not ok:
            faltam.setdefault(m.group().lower(), []).append(n)
        return novo
    if l.startswith('@ '):
        return l
    return PALAVRA.sub(troca, l)


def main():
    linhas = []
    for parte in ('A', 'B'):
        linhas += open(os.path.join(COL, f'v1834-{parte}.txt'), encoding='utf-8').read().rstrip('\n').split('\n')
        linhas.append('')
    faltam = {}
    out, quem = [], None
    for i, l in enumerate(linhas):
        if l.startswith('@ '):
            quem = l[2:].strip()
        elif l.startswith('_'):
            quem = None
        cast = (quem == 'Ermitão' and l.startswith('| ')) or CASTELHANO.search(l)
        out.append(l if cast else modernizar_linha(l, faltam, i + 1))
    texto = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip() + '\n'
    open(os.path.join(COL, 'moderno-1834.txt'), 'w', encoding='utf-8').write(texto)
    with open(os.path.join(COL, 'sem-decisao.txt'), 'w', encoding='utf-8') as f:
        for w, ns in sorted(faltam.items()):
            f.write(f'{w}\t{len(ns)}\t{linhas[ns[0] - 1].strip()}\n')
    with open(os.path.join(COL, 'automaticas.txt'), 'w', encoding='utf-8') as f:
        for a, b in sorted(AUTO.items()):
            f.write(f'{a}\t{b}\n')
    print(len(faltam), 'palavras sem decisão;', len(AUTO), 'trocas automáticas (conferir em automaticas.txt)')


if __name__ == '__main__':
    main()
