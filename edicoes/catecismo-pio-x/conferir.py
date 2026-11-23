"""Confere a tradução do Catecismo Maior contra o original, arquivo por arquivo.

    python3 edicoes/catecismo-pio-x/conferir.py [arquivo ...]     (sem nomes: todos os traduzidos)

Para cada arquivo de traducao/: o mesmo número de blocos que o original; em cada bloco o mesmo tipo (título de
capítulo com o mesmo número, título de § com o mesmo número, pergunta com o mesmo número e em negrito, resposta,
lista com o mesmo número de linhas «| »); a marca [parte.n] no mesmo bloco; itálico fechado; nenhuma mesóclise;
nenhum «R.» ou «D.» no começo da resposta. Diz «ok» quando está tudo certo.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-"
                       r"(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos(arq):
    linhas = open(arq, encoding='utf-8').read().replace('\r', '').split('\n')
    i = 0
    while i < len(linhas) and (linhas[i].startswith('# ') or not linhas[i].strip()):
        i += 1
    return [b.strip() for b in re.split(r'\n\s*\n', '\n'.join(linhas[i:])) if b.strip()]


def assinatura(b):
    marca = re.match(r'\[([IVX]+\.\d+)\]\n', b)
    corpo = b[marca.end():] if marca else b
    m = re.match(r'## (§ )?(\d+)\. \S', corpo)
    if m:
        tipo = ('§' if m.group(1) else 'cap') + m.group(2)
    elif corpo.startswith('## '):
        tipo = 'título'
    elif re.match(r'\*\*(\d+)\. .+\*\*$', corpo, re.S):
        tipo = 'P' + re.match(r'\*\*(\d+)\.', corpo).group(1)
    elif corpo.startswith('| '):
        linhas = corpo.split('\n')
        tipo = 'L%d' % len(linhas) if all(l.startswith('| ') for l in linhas) else 'lista-mista'
    else:
        tipo = 'R'
    return (marca.group(1) if marca else None, tipo)


def conferir(nome):
    orig, trad = os.path.join(AQUI, 'original', nome), os.path.join(AQUI, 'traducao', nome)
    erros = []
    bo, bt = blocos(orig), blocos(trad)
    if len(bo) != len(bt):
        erros.append(f'{len(bo)} blocos no original e {len(bt)} na tradução')
    for k, (a, b) in enumerate(zip(bo, bt)):
        sa, sb = assinatura(a), assinatura(b)
        if sa != sb:
            erros.append(f'bloco {k + 1}: original {sa}, tradução {sb}: «{b[:70]}»')
            if len(erros) > 8:
                break
    texto = open(trad, encoding='utf-8').read()
    for k, b in enumerate(bt):
        if b.count('**') % 2 or re.sub(r'\*\*', '', b).count('_') % 2:
            erros.append(f'bloco {k + 1}: negrito ou itálico sem fechar: «{b[:70]}»')
        if re.match(r'(R|D|P)\.\s', b):
            erros.append(f'bloco {k + 1}: começa com «{b[:2]}»')
    for m in MESOCLISE.finditer(texto):
        erros.append('mesóclise: ' + m.group(0))
    if not texto.startswith('# titulo:'):
        erros.append('falta «# titulo:» na primeira linha')
    return erros


if __name__ == '__main__':
    nomes = sys.argv[1:] or sorted(f for f in os.listdir(os.path.join(AQUI, 'traducao')) if f.endswith('.txt'))
    ruim = 0
    for n in nomes:
        n = os.path.basename(n)
        e = conferir(n)
        print(f'{n}: ' + ('ok' if not e else '\n  ' + '\n  '.join(e)))
        ruim += bool(e)
    sys.exit(1 if ruim else 0)
