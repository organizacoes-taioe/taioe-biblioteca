"""Junta as colunas conferidas em original/vita.txt."""
import glob, re, os
D = os.path.dirname(os.path.abspath(__file__)) + '/../colunas'
fs = sorted(glob.glob(D + '/[0-9][0-9]-*.txt'))
t = ''
for f in fs:
    s = open(f, encoding='utf-8').read().strip()
    novo = s.startswith('[') or os.path.basename(f).startswith('32-')
    t = (t.rstrip() + ('\n\n' if novo else ' ') + s) if t else s
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'\n{3,}', '\n\n', t)
# [n] sempre abre parágrafo
t = re.sub(r'\s*(\[\d+\])', r'\n\n\1', t).strip()
cab = ('# titulo: Vita Sancti Augustini\n'
       '# edicao: Patrologia Latina 32 (Migne, Paris, 1841; texto dos Maurinos), col. 33–66; no cap. 30, o fim da carta a Honorato pela PL 33, Ep. 228, nn. 10–14, col. 1017–1019\n'
       '# marcas: «[n]» = capítulo (o prefácio está em prefacio.txt)\n\n')
pre, resto = t.split('\n\n[1]', 1)
assert pre.startswith('[0] ')
open(os.path.dirname(D) + '/../original/prefacio.txt', 'w', encoding='utf-8').write(
    '# titulo: Praefatio\n# edicao: Patrologia Latina 32 (Migne, Paris, 1841), col. 33–34\n\n' + pre[4:] + '\n')
open(os.path.dirname(D) + '/../original/vita.txt', 'w', encoding='utf-8').write(cab + '[1]' + resto + '\n')
ps = [p for p in t.split('\n\n') if p.strip()]
print(len(ps), 'parágrafos;', len(t.split()), 'palavras;', re.findall(r'\[(\d+)\]', t))
