"""Confere a tradução do Beowulf (verso livre, em traducao/) contra o original, arquivo por arquivo.

Uso: python edicoes/beowulf/conferir.py [01 02 ... finnsburh]   (sem argumentos: todos)

Erros (o arquivo não passa): falta o arquivo ou o «# titulo:»; número de versos diferente do original;
linha em branco no meio; tabulação (a tradução não tem cesura); aspas retas, aspas que abrem dentro de
uma fala aberta ou fecham sem abrir; mesóclise.
Aviso: fala aberta no fim do arquivo (o guia, § 6, manda fechar as aspas no fim de um arquivo e reabrir
no seguinte).
O ritmo se confere com o Versificador (CONVENCOES.md, § 2).
"""
import os
import re
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
MESOCLISE = re.compile(r"[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-"
                       r"(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b")


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
    if '"' in texto:
        erros.append('aspas retas (") no texto')
    aberta = False
    for k, t in enumerate(trad, 1):
        if not t.strip():
            erros.append(f'v. {k}: linha em branco')
        if '\t' in t:
            erros.append(f'v. {k}: tabulação')
        for ch in t:
            if ch == '“':
                if aberta:
                    erros.append(f'v. {k}: “ dentro de uma fala aberta')
                aberta = True
            elif ch == '”':
                if not aberta:
                    erros.append(f'v. {k}: ” sem abrir')
                aberta = False
    if aberta:
        avisos.append('fala aberta no fim do arquivo')
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
