"""Lê as páginas do Wikisource (transcrição de 1769) e grava ws1769.json:
[{pag, nivel, versos:[...], notas:[{nome, segue, texto}]}]. Âncoras de nota no verso: ⟦k⟧ (k = índice da nota na página)."""
import json, os, re, glob, html
D = os.environ.get('URAGUAI_CACHE') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ferramentas', 'cache', 'o-uraguai') + '/'
def limpa(s):
    s = re.sub(r'<noinclude>.*?</noinclude>', '', s, flags=re.S)
    s = re.sub(r'\{\{(?:[Gg]capitular)\|(\w)\}\}', r'\1', s)
    s = re.sub(r'<font[^>]*>(\w)</font>', r'\1', s)
    s = re.sub(r'\{\{sc2?\|([^{}]*)\}\}', r'\1', s)
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = s.replace('&#771;', '̃').replace('&nbsp;', ' ')
    s = html.unescape(s)
    return s
def inline(s):
    s = re.sub(r"'''(.*?)'''", r'\1', s)
    s = re.sub(r"''(.*?)''", r'_\1_', s)
    s = re.sub(r'\{\{[^{}]*\}\}', '', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'[ \t]+', ' ', s).strip()
out = []
for f in sorted(glob.glob(D + 'ws1769/*.txt')):
    raw = open(f).read()
    pag = int(os.path.basename(f)[:3])
    m = re.search(r'pagequality level="(\d)"', raw); nivel = int(m.group(1)) if m else 0
    s = limpa(raw)
    notas = []
    def ref(m):
        attrs, txt = m.group(1) or '', m.group(2)
        nome = re.search(r'name="([^"]*)"', attrs); segue = re.search(r'follow="([^"]*)"', attrs)
        notas.append({'nome': nome.group(1) if nome else '', 'segue': segue.group(1) if segue else '', 'texto': inline(txt.replace('\n', ' '))})
        return '⟦%d⟧' % (len(notas) - 1) if not segue else ''
    s = re.sub(r'<ref([^>/]*)>(.*?)</ref>', ref, s, flags=re.S)
    s = re.sub(r'<ref[^>]*/>', '', s)
    versos = []
    for bloco in re.findall(r'<poem[^>]*>(.*?)</poem>', s, flags=re.S):
        for l in bloco.split('\n'):
            l2 = inline(l)
            if l2: versos.append(l2)
    out.append({'pag': pag, 'nivel': nivel, 'versos': versos, 'notas': notas, 'resto': inline(re.sub(r'<poem[^>]*>.*?</poem>', '', s, flags=re.S))[:300]})
json.dump(out, open(D + 'ws1769.json', 'w'), ensure_ascii=False, indent=0)
tot = 0
for p in out:
    tot += len(p['versos'])
    print(p['pag'], p['nivel'], len(p['versos']), len(p['notas']), p['resto'][:80] if not p['versos'] else '')
print('versos', tot)
