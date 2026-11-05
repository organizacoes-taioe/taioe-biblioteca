"""ver.py 'palavra1 palavra2 ...' : mostra as linhas do OCR de Toronto (ia) e de Harvard (hv) com essas
palavras (busca sem acento, as palavras na ordem, até 3 de distância)."""
import re, sys, unicodedata, html
C = '/home/geremias/.cache/claude-wt5-minha-formacao/ferramentas/cache/minha-formacao/'
def k(w):
    w = unicodedata.normalize('NFD', w.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in w if unicodedata.category(c) != 'Mn'))
def paginas_ia():
    s = open(C + 'ia_djvu.xml', encoding='utf-8').read()
    for n, obj in enumerate(re.findall(r'<OBJECT.*?</OBJECT>', s, re.S)):
        yield n, [html.unescape(' '.join(w.strip() for w in re.findall(r'<WORD[^>]*>(.*?)</WORD>', l)))
                  for l in re.findall(r'<LINE>(.*?)</LINE>', obj, re.S)]
def paginas_hv():
    s = open(C + 'harvard.txt', encoding='utf-8').read()
    for p in re.split(r'(?m)^@@PAGINA (\d+)@@$', s)[1:]:
        pass
    partes = re.split(r'(?m)^@@PAGINA (\d+)@@$', s)
    for i in range(1, len(partes), 2):
        yield int(partes[i]), partes[i + 1].split('\n')
def busca(pags, alvo):
    for n, ls in pags:
        texto = re.sub(r'-\s*\n\s*', '', '\n'.join(ls))
        toks = [k(w) for w in re.split(r'[\s\-—]+', texto)]
        toks2 = [t for t in toks if t]
        joined = ' '.join(toks2)
        for i in range(len(toks2)):
            if toks2[i] == alvo[0] and all(a in toks2[i + 1:i + 1 + 3 * len(alvo)] for a in alvo[1:]):
                # mostra as linhas em volta
                for j, l in enumerate(ls):
                    if any(k(w) == alvo[0] or alvo[0].startswith(k(w)) and len(k(w)) > 2 for w in re.split(r'[\s\-—]+', l)[-1:] + re.split(r'[\s\-—]+', l)):
                        yield n, ls[max(0, j - 1):j + 3]
                        break
                break
for alvo in sys.argv[1:]:
    a = [k(w) for w in alvo.split()]
    print('#####', alvo)
    for nome, f in (('ia', paginas_ia), ('hv', paginas_hv)):
        for n, ls in busca(f(), a):
            print(f'  {nome} p.{n}: ' + ' / '.join(l.strip() for l in ls))
