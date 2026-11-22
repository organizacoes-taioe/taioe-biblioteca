"""Passa as páginas do Wikisource (edição de Paris, 1825) a 1825/NNN.txt, uma por página do PDF do Wikisource.
Uso: python3 -I extrair.py <pasta ws>. Corpo primeiro; depois de «---», as notas de rodapé da página."""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
WS = sys.argv[1]

def desfaz(s):
    s = re.sub(r'<noinclude>.*?</noinclude>', '', s, flags=re.S)
    s = s.replace('՚', "'").replace("'''", '')
    s = re.sub(r'\{\{corr\|[^|{}]*\|([^{}]*)\}\}', r'\1', s)
    s = re.sub(r'\{\{(?:dhr|rule|nop|page break|gap)[^{}]*\}\}', '\n', s)
    for _ in range(5):
        s = re.sub(r'\{\{lsp\|\|([^{}]*)\}\}', r'\1', s)
        s = re.sub(r'\{\{(?:c|t2|sc|small|smaller|larger|right|left|d|capitular|gcapitular)\|([^{}]*)\}\}', r'\1', s)
    s = re.sub(r'<sup>(.*?)</sup>', r'\1', s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    return s

for n in range(11, 51):
    bruto = open(os.path.join(WS, f'{n:03d}.txt'), encoding='utf-8').read()
    t = desfaz(bruto)
    notas = []
    def nota(m):
        attrs, corpo = m.group(1) or '', m.group(2).strip()
        if 'follow' in attrs:
            notas.append('(continua) ' + corpo)
            return ''
        notas.append(corpo)
        return f'[{len([x for x in notas if not x.startswith("(continua)")])}]'
    t = re.sub(r'<ref(\s[^>]*)?>(.*?)</ref>', nota, t, flags=re.S)
    t = re.sub(r'\{\{cabeçalho[^{}]*\}\}', '', t)
    t = re.sub(r'[ \t]+\n', '\n', t)
    t = re.sub(r'\n{3,}', '\n\n', t).strip()
    saida = t
    if notas:
        saida += '\n---\n' + '\n'.join(re.sub(r'\s*\n\s*', ' ', x) for x in notas)
    open(os.path.join(AQUI, '1825', f'{n:03d}.txt'), 'w', encoding='utf-8').write(saida + '\n')
