"""Ferramenta da tradução por capítulos da Autobiografia de Franklin.

  python3 edicoes/autobiografia-franklin/trechos.py mostrar III 3   # blocos do original, numerados
  python3 edicoes/autobiografia-franklin/trechos.py conferir III 3  # confere traducao/trechos/III-03.txt
  python3 edicoes/autobiografia-franklin/trechos.py estado          # o que já está traduzido
  python3 edicoes/autobiografia-franklin/trechos.py juntar          # grava traducao/parte-N.txt das partes completas

Cada capítulo traduzido fica em traducao/trechos/<parte>-<nn>.txt (parte IV: IV-01.txt), com os blocos do
capítulo do original na mesma ordem: o título «## n. …» traduzido, o 1º parágrafo com a marca «[III.3]»,
e um bloco traduzido para cada bloco do original, separados por linha em branco.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROM = ['I', 'II', 'III', 'IV']
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos(arq):
    t = open(arq, encoding='utf-8').read().replace('\r', '')
    bl = [b.strip('\n') for b in re.split(r'\n[ \t]*\n', t) if b.strip()]
    return [b for b in bl if not b.startswith('# ')]


def capitulos(parte):
    """{n: [blocos]} do original da parte; parte IV, que não tem capítulos, é o capítulo 1."""
    bl = blocos(os.path.join(AQUI, 'original', f'parte-{ROM.index(parte) + 1}.txt'))
    caps, atual = {}, None
    for b in bl:
        m = re.match(r'^## (\d+)\. ', b)
        if m:
            atual = int(m.group(1))
            caps[atual] = []
        if atual is None:
            atual = 1
            caps[1] = []
        caps[atual].append(b)
    return caps


def arq_trad(parte, n):
    return os.path.join(AQUI, 'traducao', 'trechos', f'{parte}-{n:02d}.txt')


def conferir(parte, n, falar=True):
    orig = capitulos(parte)[n]
    arq = arq_trad(parte, n)
    if not os.path.exists(arq):
        return None
    tr = blocos(arq)
    erros = []
    if len(tr) != len(orig):
        erros.append(f'{len(tr)} blocos na tradução, {len(orig)} no original')
    for i, (o, t) in enumerate(zip(orig, tr)):
        if o.startswith('## ') != t.startswith('## '):
            erros.append(f'bloco {i}: título num e não no outro')
        mo, mt = re.match(r'^\[([IV]+\.\d+)\]', o), re.match(r'^\[([IV]+\.\d+)\]', t)
        if (mo and mo.group(1)) != (mt and mt.group(1)):
            erros.append(f'bloco {i}: marca {mo and mo.group(1)} × {mt and mt.group(1)}')
        if o.startswith('| ') != t.startswith('| '):
            erros.append(f'bloco {i}: verso/lista («| ») num e não no outro')
        if o.startswith('[_') != t.startswith('[_'):
            erros.append(f'bloco {i}: nota entre colchetes num e não no outro')
        r = len(t.split()) / max(1, len(o.split()))
        if len(o.split()) > 25 and not 0.75 <= r <= 1.6:
            erros.append(f'bloco {i}: tamanho estranho ({len(o.split())} → {len(t.split())} palavras): «{o[:50]}…»')
    for i, t in enumerate(tr):
        for m in MESOCLISE.finditer(t):
            erros.append(f'bloco {i}: mesóclise «{m.group(0).strip()}»')
    if falar:
        print(f'{parte}.{n}:', 'ok' if not erros else '\n  ' + '\n  '.join(erros))
    return not erros


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'estado'
    if cmd == 'mostrar':
        parte, n = sys.argv[2], int(sys.argv[3])
        for i, b in enumerate(capitulos(parte)[n]):
            print(f'<<{i}>>\n{b}\n')
    elif cmd == 'conferir':
        parte, n = sys.argv[2], int(sys.argv[3])
        sys.exit(0 if conferir(parte, n) else 1)
    elif cmd == 'estado':
        for p in ROM:
            for n, bl in capitulos(p).items():
                r = conferir(p, n, falar=False)
                pal = sum(len(b.split()) for b in bl)
                print(f'{p}.{n}\t{pal} palavras\t' + ('falta' if r is None else 'ok' if r else 'COM ERRO'))
    elif cmd == 'juntar':
        for k, p in enumerate(ROM, 1):
            caps = capitulos(p)
            if not all(conferir(p, n, falar=False) for n in caps):
                print(f'parte {p}: incompleta, não gravada')
                continue
            cab = open(os.path.join(AQUI, 'original', f'parte-{k}.txt'), encoding='utf-8').read().split('\n\n')[0]
            tit = {1: 'Twyford, 1771', 2: 'Passy, 1784', 3: 'Filadélfia, 1788', 4: 'Filadélfia, 1789–1790'}[k]
            corpo = '\n\n'.join('\n\n'.join(blocos(arq_trad(p, n))) for n in caps)
            with open(os.path.join(AQUI, 'traducao', f'parte-{k}.txt'), 'w', encoding='utf-8') as f:
                f.write(f'# titulo: Autobiografia, parte {p} ({tit})\n\n' + corpo + '\n')
            print(f'parte {p}: gravada')


if __name__ == '__main__':
    main()
