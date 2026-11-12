"""Lê o Macbeth da Cambridge (1865, PG 47715, HTML) e grava cenas.json: por cena, os itens em ordem."""
import html, json, re, sys
src = open(sys.argv[1], encoding='utf-8').read()
# tira notas de rodapé (âncoras), números de página
src = re.sub(r'<a id="FNanchor_[^"]*"></a>', '', src)
src = re.sub(r'<a class="fnanchor[^>]*>\[\d+\]</a>', '', src)
src = re.sub(r'<span class="pagenum">.*?</span>', '', src)
src = re.sub(r'<div class="footnotes">.*?</div></div>\s*(?=<hr|<h2|$)', '', src, flags=re.S)
# corta os rodapés de outro jeito: tudo entre <div class="footnotes"> e o próximo <h2> ou fim
src = re.sub(r'<div class="footnotes">.*?(?=<h2>|\Z)', '', src, flags=re.S)
def limpo(s):
    s = re.sub(r'<span class="smcap">(.*?)</span>', lambda m: m.group(1).upper(), s, flags=re.S)
    s = re.sub(r'</?i>', '_', s)
    s = re.sub(r'<br\s*/?>', '', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = s.replace('__', '')
    return s
cenas = []; ato = None
tok = re.compile(r'<h2>(.*?)</h2>|<h3>(.*?)</h3>|<p class="(directcenter|directright)">(.*?)</p>|<span class="i(\d+)">(.*?)<br>\s*</span>(?:</span>)?|(</div><div class="stanza">)', re.S)
for m in tok.finditer(src):
    if m.group(1) is not None:
        ato = limpo(m.group(1)).strip(); continue
    if m.group(2) is not None:
        cenas.append({'ato': ato, 'titulo': limpo(m.group(2)).strip(), 'itens': []}); continue
    if not cenas: continue
    it = cenas[-1]['itens']
    if m.group(3):
        it.append(['rubrica', m.group(3), ' '.join(limpo(m.group(4)).split())]); continue
    if m.group(7):
        it.append(['quebra']); continue
    ind = int(m.group(5)); corpo = m.group(6)
    num = None
    mm = re.search(r'\s*<span class="linenum">(\d+)</span>', corpo)
    if mm:
        num = int(mm.group(1)); corpo = corpo[:mm.start()] + corpo[mm.end():]
    dl = None
    mm = re.search(r'\s*<span class="directline">(.*)$', corpo, re.S)
    if mm:
        dl = ' '.join(limpo(mm.group(1)).split()); corpo = corpo[:mm.start()]
    fala = None
    mm = re.match(r'<i>([^<]*?\.)</i>( *)', corpo)
    if mm:
        fala = mm.group(1); esp = len(mm.group(2)); corpo = corpo[mm.end():]
    else:
        esp = 0
    t = limpo(corpo).rstrip()
    lead = len(t) - len(t.lstrip(' ')); t = t.strip()
    it.append(['linha', fala, ind, esp, lead, t, num, dl])
json.dump(cenas, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(cenas), 'cenas', sum(1 for c in cenas for x in c['itens'] if x[0]=='linha'), 'linhas')
