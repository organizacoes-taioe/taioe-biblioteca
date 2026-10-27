"""Confere um documento do Magistério: original e tradução com os mesmos blocos e as mesmas marcas.

    python3 edicoes/magisterio/conferir.py <documento>

Compara, bloco a bloco, o tipo (título «## », nota «¤ [n]», parágrafo), as chamadas de nota «[n]» e
as marcas de numeração «{§ n}»; procura mesóclise e restos do vatican.va («(1)» no lugar de «[1]»).
Sai com código 1 se achar problema.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-"
                       r"(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos(arq):
    linhas = open(arq, encoding='utf-8').read().replace('\r', '').split('\n')
    i = 0
    while i < len(linhas) and (linhas[i].startswith('# ') or not linhas[i].strip()):
        i += 1
    return [b.strip() for b in re.split(r'\n\s*\n', '\n'.join(linhas[i:])) if b.strip()]


def tipo(b):
    return 'titulo' if b.startswith('## ') else 'nota' if b.startswith('¤ ') else 'texto'


def marcas(b):
    return re.findall(r'\{§ [^}]+\}|\[\d+\]', b)


def main(doc):
    pasta = os.path.join(RAIZ, doc)
    o = blocos(os.path.join(pasta, 'original', doc + '.txt'))
    t = blocos(os.path.join(pasta, 'traducao', doc + '.txt'))
    erros = []
    if len(o) != len(t):
        erros.append(f'blocos: original {len(o)}, tradução {len(t)}')
    for k, (a, b) in enumerate(zip(o, t), 1):
        if tipo(a) != tipo(b):
            erros.append(f'bloco {k}: tipo {tipo(a)} × {tipo(b)}: {b[:60]!r}')
        if marcas(a) != marcas(b):
            erros.append(f'bloco {k}: marcas {marcas(a)} × {marcas(b)}')
    for nome, bl in (('original', o), ('tradução', t)):
        for k, b in enumerate(bl, 1):
            if re.search(r'(?<![\w\[])\(\d{1,3}\)', b) and tipo(b) != 'nota':
                erros.append(f'{nome}, bloco {k}: chamada «(n)» do vatican.va sem converter')
    for k, b in enumerate(t, 1):
        if MESOCLISE.search(b):
            erros.append(f'tradução, bloco {k}: mesóclise: {MESOCLISE.search(b).group(0)}')
    chamadas = [m for b in o if tipo(b) != 'nota' for m in re.findall(r'\[(\d+)\]', b)]
    notas = [re.match(r'¤ \[(\d+)\]', b).group(1) for b in o if tipo(b) == 'nota' and re.match(r'¤ \[(\d+)\]', b)]
    if sorted(chamadas, key=int) != sorted(notas, key=int):
        erros.append(f'chamadas sem nota ou notas sem chamada: {sorted(set(chamadas) ^ set(notas), key=int)}')
    secoes = [m for b in o for m in re.findall(r'\{§ (\d+)\}', b)]
    if secoes and [int(x) for x in secoes] != list(range(int(secoes[0]), int(secoes[0]) + len(secoes))):
        erros.append(f'numeração {{§ n}} fora de ordem ou com buraco: {secoes}')
    print(f'{doc}: {len(o)} blocos, {len(notas)} notas, {len(secoes)} números {{§}}')
    for e in erros:
        print('  ✗', e)
    return 1 if erros else 0


if __name__ == '__main__':
    sys.exit(max(main(d) for d in sys.argv[1:]))
