"""Ferramenta da tradução do Diálogo de Santa Catarina de Sena, capítulo a capítulo.

  python3 edicoes/dialogo-catarina/trechos.py mostrar 26 [27]   # blocos do original dos capítulos 26 a 27, numerados
  python3 edicoes/dialogo-catarina/trechos.py conferir [26 [40]] # confere traducao/capitulos/026.txt … (sem número: todos)
  python3 edicoes/dialogo-catarina/trechos.py estado             # o que já está traduzido, por tratado
  python3 edicoes/dialogo-catarina/trechos.py juntar             # grava traducao/<parte>.txt dos tratados completos

O original fica em original/<parte>.txt (um arquivo por tratado). Cada capítulo traduzido fica em
traducao/capitulos/<nnn>.txt (000 = o cabeçalho antes do capítulo 1), com os blocos do capítulo na mesma
ordem: o título «## n. …» traduzido, o 1º parágrafo com a marca «[II.26]» igual, e um bloco traduzido para
cada bloco do original, separados por linha em branco. Sem linha de cabeçalho «# » nos capítulos.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PARTES = [('I', 'prologo', 1, 8), ('II', 'discricao', 9, 64), ('III', 'oracao', 65, 134),
          ('IV', 'providencia', 135, 153), ('V', 'obediencia', 154, 167)]
TITULOS = {'I': 'Prólogo', 'II': 'Tratado da discrição', 'III': 'Tratado da oração',
           'IV': 'Tratado da providência', 'V': 'Tratado da obediência'}
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)")


def blocos_txt(t):
    t = t.replace('\r', '')
    return [b.strip('\n') for b in re.split(r'\n[ \t]*\n', t) if b.strip() and not b.startswith('# ')]


def parte_de(n):
    for p in PARTES:
        if p[2] <= n <= p[3]:
            return p
    return PARTES[0] if n == 0 else None


def capitulos(arq_parte):
    """{n: [blocos]} de um arquivo de tratado; o que vem antes do 1º título é o capítulo 0."""
    bl = blocos_txt(open(arq_parte, encoding='utf-8').read())
    caps, atual = {}, 0
    for b in bl:
        m = re.match(r'^## (\d+)\. ', b)
        if m:
            atual = int(m.group(1))
        caps.setdefault(atual, []).append(b)
    return caps


def original(n):
    p = parte_de(n)
    return capitulos(os.path.join(AQUI, 'original', p[1] + '.txt')).get(n, [])


def arq_trad(n):
    return os.path.join(AQUI, 'traducao', 'capitulos', f'{n:03d}.txt')


def conferir(n, falar=True):
    orig = original(n)
    arq = arq_trad(n)
    if not os.path.exists(arq):
        return None
    t = open(arq, encoding='utf-8').read()
    tr = blocos_txt(t)
    erros = []
    if len(tr) != len(orig):
        erros.append(f'{len(tr)} blocos na tradução, {len(orig)} no original')
    for i, (a, b) in enumerate(zip(orig, tr)):
        ma, mb = re.match(r'^(## \d+\. |\[[IVX]+\.\d+\] )', a), re.match(r'^(## \d+\. |\[[IVX]+\.\d+\] )', b)
        if (ma and ma.group(1)) != (mb and mb.group(1)):
            erros.append(f'bloco {i + 1}: marca {ma and ma.group(1)!r} no original, {mb and mb.group(1)!r} na tradução')
        if b.count('—') % 2 != a.count('—') % 2 and falar == 'tudo':
            erros.append(f'bloco {i + 1}: número de travessões com paridade diferente')
        ra, rb = len(a.split()), len(b.split())
        if ra > 25 and not (0.75 * ra <= rb <= 1.6 * ra):
            erros.append(f'bloco {i + 1}: {rb} palavras na tradução, {ra} no original')
    for m in MESOCLISE.finditer(t):
        erros.append('mesóclise: ' + m.group(0))
    for c in '«»':
        if c in t:
            erros.append(f'aspas {c} na tradução (use “ ”)')
            break
    if falar:
        print(f'cap. {n}: ' + ('ok' if not erros else '; '.join(erros)))
    return not erros


def mostrar(a, b):
    for n in range(a, b + 1):
        for i, bl in enumerate(original(n), 1):
            print(f'[{n}:{i}] {bl}\n')


def estado():
    for sig, nome, a, b in PARTES:
        feitos = [n for n in range(a if a > 1 else 0, b + 1) if os.path.exists(arq_trad(n))]
        tot = b - (a if a > 1 else 0) + 1
        print(f'{sig} {TITULOS[sig]}: {len(feitos)}/{tot}' + (f' (faltam {[n for n in range(a if a > 1 else 0, b + 1) if n not in feitos][:8]}…)' if len(feitos) < tot else ''))


def juntar():
    for sig, nome, a, b in PARTES:
        ns = list(range(0 if a == 1 else a, b + 1))
        if not all(os.path.exists(arq_trad(n)) for n in ns):
            print(f'{nome}: incompleto, não juntado')
            continue
        ruins = [n for n in ns if not conferir(n, falar=False)]
        if ruins:
            print(f'{nome}: capítulos com erro {ruins}, não juntado')
            continue
        corpo = '\n\n'.join('\n\n'.join(blocos_txt(open(arq_trad(n), encoding='utf-8').read())) for n in ns)
        cab = f'# titulo: {TITULOS[sig]} (Parte {sig})\n\n'
        open(os.path.join(AQUI, 'traducao', nome + '.txt'), 'w', encoding='utf-8').write(cab + corpo + '\n')
        print(f'{nome}: juntado ({len(ns)} capítulos)')


if __name__ == '__main__':
    cmd, args = sys.argv[1], [int(x) for x in sys.argv[2:]]
    if cmd == 'mostrar':
        mostrar(args[0], args[1] if len(args) > 1 else args[0])
    elif cmd == 'conferir':
        a = args[0] if args else 0
        b = args[1] if len(args) > 1 else (args[0] if args else 167)
        ok = [conferir(n, falar='tudo') for n in range(a, b + 1) if os.path.exists(arq_trad(n))]
        print(f'{sum(1 for x in ok if x)}/{len(ok)} ok')
    elif cmd == 'estado':
        estado()
    elif cmd == 'juntar':
        juntar()
