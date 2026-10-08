"""Confere a tradução do Beowulf contra o original, arquivo por arquivo.

Uso: python edicoes/beowulf/conferir.py [01 02 ... finnsburh]   (sem argumentos: todos)

Erros (o arquivo não passa): falta o arquivo ou o «# titulo:»; número de versos diferente do original;
linha em branco no meio; cesura (tabulação) onde o original não tem, ou faltando onde tem, ou mais de
uma; aspas que não fecham; mesóclise.
Avisos (estimativas para a releitura): meio-verso com menos de 3 ou mais de 10 sílabas (contagem
aproximada, sem elisões); passagem de cinco versos seguidos sem aliteração entre as metades.
"""
import os
import re
import sys
import unicodedata

PASTA = os.path.dirname(os.path.abspath(__file__))
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-"
                       r"(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b")
ATONAS = set('''a o as os um uma uns umas de do da dos das dum duma em no na nos nas num numa ao aos à às
por pelo pela pelos pelas para pra com sem sob sobre entre até após ante e ou nem mas que se como quando
onde porque pois já não lhe lhes me te nos vos o lo la seu sua seus suas meu minha meus minhas teu tua
teus tuas nosso nossa vosso vossa ele ela eles elas eu tu nós vós isso isto aquilo esse essa este esta
aquele aquela tão tal mais muito bem também cada quem qual'''.split())


def ler(arq):
    linhas = open(arq, encoding='utf-8').read().replace('\r', '').split('\n')
    cab, i = {}, 0
    while i < len(linhas) and (linhas[i].startswith('# ') or not linhas[i].strip()):
        m = re.match(r'# ([\w-]+):\s?(.*)$', linhas[i])
        if m:
            cab[m.group(1)] = m.group(2).strip()
        i += 1
    corpo = linhas[i:]
    while corpo and not corpo[-1].strip():
        corpo.pop()
    return cab, corpo


def silabas(s):
    s = unicodedata.normalize('NFC', s.lower())
    s = re.sub(r"[^a-zà-ÿæ ]", ' ', s)
    n = 0
    for w in s.split():
        w = re.sub(r'(qu|gu)(?=[eiéí])', 'k', w)
        w = re.sub(r'[aeoáéóâêô][iu](?![aeiouáéíóú])', 'a', w)   # ditongo decrescente
        w = re.sub(r'(ão|õe|ãe)', 'a', w)
        n += max(1, len(re.findall(r'[aeiouáéíóúâêôãõæy]+', w)))
    return n


def som(w):
    w = unicodedata.normalize('NFC', w.lower())
    w = w[1:] if w.startswith('h') else w
    if not w:
        return ''
    if re.match(r'[aeiouáéíóúâêôãõæ]', w):
        return 'V'
    if w.startswith('qu') or re.match(r'c[aouáóú]', w) or w.startswith('k'):
        return 'k'
    if re.match(r'c[eiéí]|ç|s|z', w):
        return 's'
    if w.startswith('ch') or w.startswith('x'):
        return 'x'
    if re.match(r'g[eiéí]|j', w):
        return 'j'
    if w.startswith('gu') or w.startswith('g'):
        return 'g'
    if w.startswith('rr') or w.startswith('r'):
        return 'r'
    return w[0]


def iniciais(meio):
    ws = re.findall(r"[A-Za-zÀ-ÿæÆ]+", meio)
    return {som(w) for w in ws if w.lower() not in ATONAS and len(w) > 2}


def conferir(nome):
    erros, avisos = [], []
    a_orig = os.path.join(PASTA, 'original', nome + '.txt')
    a_trad = os.path.join(PASTA, 'traducao', nome + '.txt')
    if not os.path.exists(a_trad):
        return [f'falta traducao/{nome}.txt'], []
    _, orig = ler(a_orig)
    cab, trad = ler(a_trad)
    if not cab.get('titulo'):
        erros.append('falta «# titulo:»')
    if len(orig) != len(trad):
        erros.append(f'versos: original {len(orig)}, tradução {len(trad)}')
    texto = '\n'.join(trad)
    for m in MESOCLISE.finditer(texto):
        erros.append(f'mesóclise: {m.group(0)}')
    if texto.count('“') != texto.count('”'):
        erros.append(f'aspas: {texto.count("“")} “ e {texto.count("”")} ”')
    if '"' in texto:
        erros.append('aspas retas (") no texto')
    sem = 0
    for k, (o, t) in enumerate(zip(orig, trad), 1):
        if not t.strip():
            erros.append(f'v. {k}: linha em branco')
            continue
        if t.count('\t') > 1:
            erros.append(f'v. {k}: mais de uma cesura')
        if ('\t' in o) != ('\t' in t):
            erros.append(f'v. {k}: cesura ' + ('faltando' if '\t' in o else 'a mais'))
        if '\t' in t:
            a, b = t.split('\t', 1)
            for lado, meio in (('1.º', a), ('2.º', b)):
                if '. .' in meio:
                    continue
                n = silabas(meio)
                if n < 3 or n > 10:
                    avisos.append(f'v. {k}: {lado} meio-verso com ~{n} sílabas: {meio.strip()}')
            if iniciais(a) & iniciais(b):
                sem = 0
            else:
                sem += 1
                if sem == 5:
                    avisos.append(f'v. {k - 4}–{k}: cinco versos sem aliteração entre as metades')
    return erros, avisos


def main():
    nomes = sys.argv[1:] or sorted(f[:-4] for f in os.listdir(os.path.join(PASTA, 'original')) if f.endswith('.txt'))
    ok = True
    for n in nomes:
        n = n.zfill(2) if n.isdigit() else n
        erros, avisos = conferir(n)
        print(f'{n}: ' + ('ok' if not erros else 'ERROS') + (f' ({len(avisos)} avisos)' if avisos else ''))
        for e in erros:
            print('  ERRO ' + e)
        for a in avisos:
            print('  aviso ' + a)
        ok = ok and not erros
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
