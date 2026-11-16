"""Ferramenta da tradução por capítulos do Livro da Vida (modelo: autobiografia-franklin/trechos.py).

  python3 edicoes/livro-da-vida/trechos.py mostrar 11     # blocos do original/11.txt, numerados (0 = prólogo, 41 = epílogo)
  python3 edicoes/livro-da-vida/trechos.py conferir 11    # confere traducao/11.txt
  python3 edicoes/livro-da-vida/trechos.py estado         # o que já está traduzido

Cada capítulo traduzido fica em traducao/NN.txt (00 = prólogo, 41 = epílogo), com «# titulo: …» e um bloco
traduzido para cada bloco do original, na mesma ordem, separados por linha em branco: o título «## …», as
linhas «Jhs.», e cada parágrafo com a sua marca «[11.3]» no começo.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")
TITULOS = {0: 'Prólogo', 41: 'Epílogo'}


def blocos(arq):
    t = open(arq, encoding='utf-8').read().replace('\r', '')
    bl = [b.strip('\n') for b in re.split(r'\n[ \t]*\n', t) if b.strip()]
    out = []
    for b in bl:
        ls = [l for l in b.split('\n') if not l.startswith('# ')]
        if ls:
            out.append('\n'.join(ls))
    return out


def arq(pasta, n):
    return os.path.join(AQUI, pasta, f'{n:02d}.txt')


def conferir(n, falar=True):
    if not os.path.exists(arq('traducao', n)):
        return None
    orig, tr = blocos(arq('original', n)), blocos(arq('traducao', n))
    erros = []
    cab = open(arq('traducao', n), encoding='utf-8').read().split('\n')[0]
    if not cab.startswith('# titulo: '):
        erros.append('falta a linha «# titulo: …» no começo')
    if len(tr) != len(orig):
        erros.append(f'{len(tr)} blocos na tradução, {len(orig)} no original')
    for i, (o, t) in enumerate(zip(orig, tr)):
        if o.startswith('## ') != t.startswith('## '):
            erros.append(f'bloco {i}: título «## » num e não no outro')
        mo, mt = re.match(r'^\[(\d+\.\d+)\]', o), re.match(r'^\[(\d+\.\d+)\]', t)
        if (mo and mo.group(1)) != (mt and mt.group(1)):
            erros.append(f'bloco {i}: marca {mo and mo.group(1)} × {mt and mt.group(1)}')
        if len(re.findall(r'\[\d+\.\d+\]', t)) > 1:
            erros.append(f'bloco {i}: mais de uma marca')
        r = len(t.split()) / max(1, len(o.split()))
        if len(o.split()) > 25 and not 0.75 <= r <= 1.45:
            erros.append(f'bloco {i}: tamanho estranho ({len(o.split())} → {len(t.split())} palavras)')
    for i, t in enumerate(tr):
        for m in MESOCLISE.finditer(t):
            erros.append(f'bloco {i}: mesóclise «{m.group(0).strip()}»')
    if falar:
        print(f'{n:02d}:', 'ok' if not erros else '\n  ' + '\n  '.join(erros))
    return not erros


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'estado'
    if cmd == 'mostrar':
        for i, b in enumerate(blocos(arq('original', int(sys.argv[2])))):
            print(f'<<{i}>>\n{b}\n')
    elif cmd == 'conferir':
        ok = all(conferir(int(n)) for n in sys.argv[2:])
        sys.exit(0 if ok else 1)
    elif cmd == 'estado':
        tot = feito = 0
        for n in range(42):
            pal = sum(len(b.split()) for b in blocos(arq('original', n)))
            r = conferir(n, falar=False)
            tot += pal; feito += pal if r else 0
            print(f'{n:02d}\t{pal} palavras\t' + ('falta' if r is None else 'ok' if r else 'COM ERRO'))
        print(f'traduzido: {feito} de {tot} palavras')


if __name__ == '__main__':
    main()
