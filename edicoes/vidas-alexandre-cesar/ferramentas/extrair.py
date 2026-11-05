"""Extrai o grego de Perrin (Perseus grc2) por capítulo e seção. Uso: extrair.py <xml> <saida.json>"""
import json, re, sys
import xml.etree.ElementTree as ET
NS = '{http://www.tei-c.org/ns/1.0}'
src, out = sys.argv[1], sys.argv[2]
root = ET.parse(src).getroot()
body = root.find(f'.//{NS}body')
notas, caps = [], []
def texto(el, ctx):
    s = el.text or ''
    for ch in el:
        tag = ch.tag.replace(NS, '')
        if tag == 'note':
            notas.append({'ref': ctx, 'nota': ''.join(ch.itertext()).strip()})
            s += '⟦n⟧'
        elif tag == 'pb' or tag == 'milestone':
            pass
        elif tag == 'gap':
            s += ' ⟦gap⟧ '
        elif tag == 'q':
            s += '“' + texto(ch, ctx) + '”'
        elif tag == 'l':
            s += '⟦l⟧' + texto(ch, ctx).strip() + '⟦/l⟧'
        else:
            s += texto(ch, ctx)
        s += ch.tail or ''
    return s
for cap in body.iter(f'{NS}div'):
    if cap.get('subtype') != 'chapter':
        continue
    c = cap.get('n'); secs = []
    for sec in cap:
        if sec.get('subtype') != 'section':
            continue
        t = texto(sec, f"{c}.{sec.get('n')}")
        t = re.sub(r'\s+', ' ', t)
        t = re.sub(r'[ \t]+', ' ', t).strip()
        secs.append([sec.get('n'), t])
    caps.append([c, secs])
json.dump({'caps': caps, 'notas': notas}, open(out, 'w'), ensure_ascii=False, indent=0)
print(len(caps), 'capítulos,', sum(len(s) for _, s in caps), 'seções,', len(notas), 'notas')
