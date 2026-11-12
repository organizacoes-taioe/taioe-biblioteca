"""Em cada capítulo («## »), leva as notas «¤» para o fim e as numera 1, 2… pela ordem das chamadas."""
import re, sys
for arq in sys.argv[1:]:
    t = open(arq, encoding='utf-8').read().strip()
    bl = t.split('\n\n'); caps, cur = [], []
    for b in bl:
        if b.startswith('## ') and cur: caps.append(cur); cur = []
        cur.append(b)
    caps.append(cur)
    out = []
    for c in caps:
        corpo = [b for b in c if not b.startswith('¤ ')]
        notas = {re.match(r'¤ \[(\w+)\]', b).group(1): b for b in c if b.startswith('¤ ')}
        ordem = []
        for b in corpo:
            for m in re.findall(r'\[(\w+)\]', b):
                if m in notas and m not in ordem: ordem.append(m)
        assert set(ordem) == set(notas), (arq, ordem, list(notas))
        novo = {m: str(i + 1) for i, m in enumerate(ordem)}
        corpo = [re.sub(r'\[(\w+)\]', lambda x: '[' + novo[x.group(1)] + ']' if x.group(1) in novo else x.group(0), b) for b in corpo]
        out += corpo + [re.sub(r'^¤ \[\w+\]', '¤ [' + novo[m] + ']', notas[m]) for m in ordem]
    open(arq, 'w', encoding='utf-8').write('\n\n'.join(out) + '\n')
