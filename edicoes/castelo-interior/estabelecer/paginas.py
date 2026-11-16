"""Lê o djvu.xml do Internet Archive: lista de páginas, cada uma com linhas (texto, topo, base, altura)."""
import re, sys, statistics, json
import xml.etree.ElementTree as ET

def paginas(arq):
    out = []
    for ev, el in ET.iterparse(arq, events=('end',)):
        if el.tag == 'OBJECT':
            linhas = []
            H = int(el.get('height') or 0)
            for ln in el.iter('LINE'):
                ws = []
                for w in ln.iter('WORD'):
                    c = [int(x) for x in w.get('coords').split(',')[:4]]
                    ws.append(((w.text or '').strip(), c))
                if not ws: continue
                tops = [c[3] for _, c in ws]; bots = [c[1] for _, c in ws]
                hs = sorted(c[1] - c[3] for _, c in ws)
                linhas.append({'t': ' '.join(x for x, _ in ws if x), 'top': min(tops), 'bot': max(bots),
                               'h': hs[len(hs)//2], 'x0': min(c[0] for _, c in ws), 'x1': max(c[2] for _, c in ws)})
            out.append({'H': H, 'linhas': linhas})
            el.clear()
    return out

if __name__ == '__main__':
    ps = paginas(sys.argv[1])
    json.dump(ps, open(sys.argv[2], 'w'), ensure_ascii=False)
    print(len(ps))
