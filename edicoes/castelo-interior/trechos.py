"""Ferramenta da tradução por capítulos do Castelo interior.

  python3 edicoes/castelo-interior/trechos.py mostrar I 1     # blocos do original, numerados (0 = prólogo, 8 = epílogo: «mostrar 0 0»)
  python3 edicoes/castelo-interior/trechos.py conferir I 1    # confere traducao/trechos/I-01.txt
  python3 edicoes/castelo-interior/trechos.py estado          # o que já está traduzido
  python3 edicoes/castelo-interior/trechos.py juntar          # grava traducao/<arquivo>.txt dos arquivos completos

Cada arquivo do original (00-prologo, 01-primeiras-moradas … 08-epilogo) se divide em trechos: o que vem
antes do primeiro «## » é o trecho 0 da morada (título de arquivo «# titulo:» à parte e a linha «Hay en
ellas…»); cada «## Capítulo» abre um trecho n. A tradução de cada trecho fica em
traducao/trechos/<morada>-<nn>.txt (morada: P = prólogo, I…VII, E = epílogo), com os mesmos blocos na
mesma ordem, separados por linha em branco; a primeira linha do arquivo de trecho 0 é «# titulo: …».
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ARQS = ['00-prologo', '01-primeiras-moradas', '02-segundas-moradas', '03-terceiras-moradas', '04-quartas-moradas',
        '05-quintas-moradas', '06-sextas-moradas', '07-setimas-moradas', '08-epilogo']
SIGLA = ['P', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'E']
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos(arq):
    t = open(arq, encoding='utf-8').read().replace('\r', '')
    return [b.strip('\n') for b in re.split(r'\n[ \t]*\n', t) if b.strip()]


def trechos(sigla):
    """{n: [blocos]} do original; 0 = o que vem antes do primeiro capítulo (com «# titulo:»)."""
    bl = blocos(os.path.join(AQUI, 'original', ARQS[SIGLA.index(sigla)] + '.txt'))
    caps, atual = {0: []}, 0
    for b in bl:
        if b.startswith('## '):
            atual += 1; caps[atual] = []
        caps[atual].append(b)
    if not caps[0]:
        del caps[0]
    return caps


def arq_trad(sigla, n):
    return os.path.join(AQUI, 'traducao', 'trechos', f'{sigla}-{n:02d}.txt')


def conferir(sigla, n, falar=True):
    orig = trechos(sigla)[n]
    arq = arq_trad(sigla, n)
    if not os.path.exists(arq):
        return None
    tr = blocos(arq)
    erros = []
    if len(tr) != len(orig):
        erros.append(f'{len(tr)} blocos na tradução, {len(orig)} no original')
    for i, (o, t) in enumerate(zip(orig, tr)):
        for pre in ('## ', '# titulo:', '| ', '_'):
            if o.startswith(pre) != t.startswith(pre):
                erros.append(f'bloco {i}: «{pre}» num e não no outro')
        mo, mt = re.match(r'^\[([IV]+\.\d+)\]', o), re.match(r'^\[([IV]+\.\d+)\]', t)
        if (mo and mo.group(1)) != (mt and mt.group(1)):
            erros.append(f'bloco {i}: marca {mo and mo.group(1)} × {mt and mt.group(1)}')
        r = len(t.split()) / max(1, len(o.split()))
        if len(o.split()) > 25 and not 0.8 <= r <= 1.35:
            erros.append(f'bloco {i}: tamanho estranho ({len(o.split())} → {len(t.split())} palavras): «{t[:50]}…»')
    for i, t in enumerate(tr):
        for m in MESOCLISE.finditer(t):
            erros.append(f'bloco {i}: mesóclise «{m.group(0).strip()}»')
    if falar:
        print(f'{sigla}.{n}:', 'ok' if not erros else '\n  ' + '\n  '.join(erros))
    return not erros


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'estado'
    if cmd == 'mostrar':
        sig, n = sys.argv[2], int(sys.argv[3])
        sig = {'0': 'P', '8': 'E'}.get(sig, sig)
        for i, b in enumerate(trechos(sig)[n]):
            print(f'<<{i}>>\n{b}\n')
    elif cmd == 'conferir':
        sys.exit(0 if conferir(sys.argv[2], int(sys.argv[3])) else 1)
    elif cmd == 'estado':
        for s in SIGLA:
            for n, bl in trechos(s).items():
                r = conferir(s, n, falar=False)
                print(f'{s}.{n}\t{sum(len(b.split()) for b in bl)} palavras\t' + ('falta' if r is None else 'ok' if r else 'COM ERRO'))
    elif cmd == 'juntar':
        for s, a in zip(SIGLA, ARQS):
            caps = trechos(s)
            if not all(conferir(s, n, falar=False) for n in caps):
                print(f'{a}: incompleto, não gravado'); continue
            corpo = '\n\n'.join('\n\n'.join(blocos(arq_trad(s, n))) for n in caps)
            open(os.path.join(AQUI, 'traducao', a + '.txt'), 'w', encoding='utf-8').write(corpo + '\n')
            print(f'{a}: gravado')


if __name__ == '__main__':
    main()
