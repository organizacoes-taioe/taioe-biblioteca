"""Extrai um livro do grego de Godley (Perseus tlg0016.tlg001.perseus-grc2) por capítulo e seção.
Uso: extrair.py <xml> <livro> <saida.json>
Marcas: ⟦n⟧ nota de Godley (o Perseus só guarda o número), ⟦gap⟧ lacuna, [ … ] o texto que Godley põe entre
colchetes (<del>), “ … ” as falas (<q>; rend="merge" continua a fala anterior), ⟦l⟧…⟦/l⟧ os versos."""
import json, re, sys
import xml.etree.ElementTree as ET
NS = '{http://www.tei-c.org/ns/1.0}'
src, livro, out = sys.argv[1], sys.argv[2], sys.argv[3]
root = ET.parse(src).getroot()
lv = next(d for d in root.iter(f'{NS}div') if d.get('subtype') == 'book' and d.get('n') == livro)
qs = [q for q in lv.iter(f'{NS}q')]
seguinte_merge = {id(q): (k + 1 < len(qs) and qs[k + 1].get('rend') == 'merge') for k, q in enumerate(qs)}
notas, caps = [], []
def texto(el, ctx):
    s = el.text or ''
    for ch in el:
        tag = ch.tag.replace(NS, '')
        if tag == 'note':
            notas.append({'ref': ctx, 'nota': ''.join(ch.itertext()).strip()})
            s += '⟦n⟧'
        elif tag == 'gap':
            s += ' ⟦gap⟧ '
        elif tag == 'del':
            s += '[' + texto(ch, ctx) + ']'
        elif tag == 'q':
            s += ('' if ch.get('rend') == 'merge' else '“') + texto(ch, ctx) + ('' if seguinte_merge[id(ch)] else '”')
        elif tag == 'l':
            s += '⟦l⟧' + texto(ch, ctx).strip() + '⟦/l⟧'
        else:
            s += texto(ch, ctx)
        s += ch.tail or ''
    return s
for cap in lv:
    if cap.get('subtype') != 'chapter':
        continue
    c = cap.get('n'); secs = []
    for sec in cap:
        if sec.get('subtype') != 'section':
            continue
        t = texto(sec, f"{c}.{sec.get('n')}")
        t = re.sub(r'\s+', ' ', t).strip()
        secs.append([sec.get('n'), t])
    caps.append([c, secs])
json.dump({'caps': caps, 'notas': notas}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(caps), 'capítulos,', sum(len(s) for _, s in caps), 'seções,', len(notas), 'notas,',
      sum(len(t.split()) for _, s in caps for _, t in s), 'palavras')
