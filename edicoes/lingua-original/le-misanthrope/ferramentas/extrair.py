"""Lê o Misanthrope da edição Louandre (Charpentier, 1910) do fr.wikisource (o HTML de cada ato, pela API
action=parse) e grava cenas.json: por cena, os itens em ordem.
python3 -I extrair.py <pasta com acte-I.html … acte-V.html> <cenas.json>
Itens: ["pers", texto] (quem está em cena), ["fala", nome, indicação], ["verso", texto, recuo, número],
["rubrica", texto] (indicação sozinha numa linha)."""
import html, json, os, re, sys

def limpar(s):
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<link [^>]*/>', '', s)
    s = re.sub(r'<sup [^>]*class="reference".*?</sup>', '', s, flags=re.S)
    s = re.sub(r'<div class="references.*', '', s, flags=re.S)   # as notas de Louandre, no fim
    s = re.sub(r'<ol class="references.*', '', s, flags=re.S)
    s = re.sub(r'<span><span class="pagenum[^>]*></span></span>', '', s)
    s = re.sub(r'<span class="pagenum[^>]*></span>', '', s)
    # número de verso do Wikisource
    s = re.sub(r'<span style="visibility:hidden"><span class="OptionText"[^>]*><span class="memo"[^>]*></span>'
               r'<span style="position:absolute;margin-left:0"><span style="[^"]*">(\d+)</span></span></span></span>',
               r'⟦\1⟧', s)
    # recuo do meio-verso: o texto que fica escondido
    s = re.sub(r'<span style="visibility:hidden; color:transparent;">(.*?)</span>',
               lambda m: '⟪%d⟫' % len(html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))), s, flags=re.S)
    s = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda m: '\n@@ATO ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n', s, flags=re.S)
    s = re.sub(r'<h3[^>]*>(.*?)</h3>', lambda m: '\n@@CENA ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n', s, flags=re.S)
    s = re.sub(r'<div class="didascalie"[^>]*>(.*?)</div>',
               lambda m: '\n@@PERS ' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + '\n', s, flags=re.S)
    s = re.sub(r'<div style="text-align:center;[^"]*"><span class="personnage"[^>]*>(.*?)</span>(?:<span class="didascalie">(.*?)</span>)?</div>',
               lambda m: '\n@@FALA ' + m.group(1).strip() + '|' + re.sub(r'<[^>]+>', '', m.group(2) or '') + '\n', s, flags=re.S)
    s = re.sub(r'<span class="didascalie"[^>]*>(.*?)</span>', lambda m: '[' + re.sub(r'<[^>]+>', '', m.group(1)).strip() + ']', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</p>|<p>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('﻿', '')
    return s

def espacos(t):
    """espaços simples, com o espaço não separável antes de ; : ? ! » e depois de «, como nos outros franceses"""
    t = ' '.join(t.replace('\xa0', ' ').split())
    t = re.sub(r'(?<=[^\s;:!?])\s*([;:!?»])', '\xa0\\1', t)
    t = re.sub(r'«\s*', '«\xa0', t)
    return t


cenas = []
ato = None
for a in ['I', 'II', 'III', 'IV', 'V']:
    s = limpar(open(os.path.join(sys.argv[1], 'acte-%s.html' % a), encoding='utf-8').read())
    for l in s.split('\n'):
        l = l.rstrip()
        if not l.strip():
            continue
        if l.startswith('@@ATO '):
            ato = l[6:].strip(); continue
        if l.startswith('@@CENA '):
            cenas.append({'ato': ato, 'titulo': l[7:].strip(), 'itens': []}); continue
        if not cenas:
            continue
        it = cenas[-1]['itens']
        if l.startswith('@@PERS '):
            it.append(['pers', espacos(l[7:])]); continue
        if l.startswith('@@FALA '):
            nome, ind = l[7:].split('|', 1)
            ind = espacos(ind).lstrip(', ').strip()
            it.append(['fala', nome.strip(), ind]); continue
        num = None
        m = re.search(r'⟦(\d+)⟧', l)
        if m:
            num = int(m.group(1)); l = l.replace(m.group(0), '')
        rec = 0
        m = re.search(r'⟪(\d+)⟫', l)
        if m:
            rec = int(m.group(1)); l = l.replace(m.group(0), '')
        t = espacos(l)
        if t.startswith('Molière') and 'Édition Louandre' in t or re.match(r'Fin du (\w+ acte|Misanthrope)', t):
            continue   # o rodapé do Wikisource e o «Fin du … acte»
        if re.fullmatch(r'\[[^\]]*\]', t):
            it.append(['rubrica', t[1:-1].strip()]); continue
        it.append(['verso', t, rec, num])
json.dump(cenas, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
nv = sum(1 for c in cenas for x in c['itens'] if x[0] == 'verso' and not x[2])
print(len(cenas), 'cenas', sum(1 for c in cenas for x in c['itens'] if x[0] == 'verso'), 'linhas,', nv, 'versos (sem os meios-versos)')
