"""Dos blocos (blocos.json) aos arquivos da obra: acha os 30 degraus (título ΛΟΓΟΣ), corta os escólios (ΣΧΟΛΙΑ… até o
degrau seguinte), divide os parágrafos longos de Rader em fins de frase e grava original/degrau-NN.txt na pasta da obra.
Os cortes ficam em cortes.json (id da palavra que abre cada bloco), para que a divisão não mude quando as palavras
forem corrigidas. Uso: dividir.py <pasta original/ da obra> [--estrutura]"""
import sys, os, re, json
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso')
blocos = json.load(open(os.path.join(AQUI, 'blocos.json'), encoding='utf-8'))
CORTES = os.path.join(AQUI, 'cortes.json')
cortes = json.load(open(CORTES, encoding='utf-8')) if os.path.exists(CORTES) else {}
TITULOS = json.load(open(os.path.join(AQUI, 'titulos.json'), encoding='utf-8'))   # "1": "ΛΟΓΟΣ Α΄. Περὶ …"
ALVO = 45

def limpo(t):
    return re.sub(r'\{PG[^}]*\}\s*', '', t).strip()

# estrutura
cab = [i for i, b in enumerate(blocos) if re.match(r'^[ΛΔΑ]\.?[ΟΘ][ΓΙΤ]\S*\s*Σ\b|^[ΛΔ]ΟΓ', limpo(b['texto'])) and len(limpo(b['texto']).split()) <= 4]
esc = [i for i, b in enumerate(blocos) if re.match(r'^ΣΧΟ[ΛΑ]', limpo(b['texto']))]
if '--estrutura' in sys.argv:
    pid = lambda i: next(x[1] for x in blocos[i]['pal'] if x[1])
    for i in cab: print('cab', i, pid(i), limpo(blocos[i]['texto'])[:40], '|', limpo(blocos[i + 1]['texto'])[:50])
    for i in esc: print('esc', i, pid(i), limpo(blocos[i]['texto'])[:50])
    sys.exit()
EST = os.path.join(AQUI, 'estrutura.json')     # {"1": [id do bloco ΛΟΓΟΣ, id do 1º bloco depois do texto], …} conferidos à mão
def bloco_de(tid):
    for i, b in enumerate(blocos):
        if any(x[1] == tid for x in b['pal']): return i
    raise KeyError(tid)

SO = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
pasta = sys.argv[1]
GREGO_NUM = 'α β γ δ ε ϛ ζ η θ ι ια ιβ ιγ ιδ ιε ιϛ ιζ ιη ιθ κ κα κβ κγ κδ κε κϛ κζ κη κθ λ'.split()
# sequência plana: (palavra, id, nº do bloco)
plano = []
for bi, b in enumerate(blocos):
    for w, tid in b['pal']: plano.append((w, tid, bi))
pos = {tid: k for k, (w, tid, bi) in enumerate(plano) if tid}
e = json.load(open(EST, encoding='utf-8'))
for n in sorted(int(x) for x in e):
    if SO and n not in SO: continue
    paras = []
    for sl in e[str(n)]:
        a, z = pos[sl[0]], pos[sl[1]]
        while a > 0 and plano[a - 1][1] is None: a -= 1      # marcas de coluna logo antes do começo entram
        if len(sl) > 2: paras.append([(sl[2], 'SUB')])
        cur, blo = [], None
        for w, tid, bi in plano[a:z]:
            if tid and blo is not None and bi != blo and cur: paras.append(cur); cur = []
            if tid: blo = bi
            cur.append((w, tid))
        if cur: paras.append(cur)
    marcas_ini = []
    chave = str(n)
    if chave not in cortes:     # primeira vez: cortes novos
        ini = []
        for seq in paras:
            cont = 0; abre = True
            for k, (p, tid) in enumerate(seq):
                if tid is None or tid == 'SUB': continue
                if abre: ini.append(tid); abre = False; cont = 0
                cont += 1
                resto = sum(1 for q in seq[k + 1:] if q[1])
                prox = next((q[0] for q in seq[k + 1:] if q[1]), '')
                if cont >= ALVO and re.search(r'[.;]$', p) and resto >= 15 and prox.lstrip('«“(᾿’\'').strip()[:1].isupper(): abre = True
        cortes[chave] = ini
    ini = set(cortes[chave])
    saida, cur = [], []
    pend = []
    for seq in paras:
        for p, tid in seq:
            if tid == 'SUB':
                if cur: saida.append(cur); cur = []
                saida.append(['SUB', p]); continue
            if tid is None: pend.append(p); continue
            if tid in ini and cur: saida.append(cur); cur = []
            cur.extend(pend); pend = []
            cur.append(p)
    if cur: saida.append(cur + pend)
    linhas = ['# titulo: ' + TITULOS[chave],
              '# fonte: Migne, Patrologia Graeca 88 (Paris, 1860), texto de M. Rader (1633); ver LEIAME.md', '',
              TITULOS[chave], '']
    k = 0
    for c in saida:
        if c[0] == 'SUB': linhas.append(c[1]); linhas.append(''); continue
        k += 1
        linhas.append('[%d.%d] %s' % (n, k, ' '.join(c))); linhas.append('')
    open(os.path.join(pasta, 'degrau-%02d.txt' % n), 'w', encoding='utf-8').write('\n'.join(linhas).rstrip() + '\n')
    print(n, k, 'blocos', sum(len(c) for c in saida if c[0] != 'SUB'), 'palavras')
json.dump(cortes, open(CORTES, 'w', encoding='utf-8'), ensure_ascii=False)
