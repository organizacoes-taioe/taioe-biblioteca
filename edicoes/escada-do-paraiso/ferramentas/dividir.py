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
if os.path.exists(EST):
    e = json.load(open(EST, encoding='utf-8'))
    pares = {int(k): (bloco_de(v[0]), bloco_de(v[1])) for k, v in e.items()}
    cab = [pares[k][0] for k in sorted(pares)]; esc = [pares[k][1] for k in sorted(pares)]
SO = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
pasta = sys.argv[1]
GREGO_NUM = 'α β γ δ ε ϛ ζ η θ ι ια ιβ ιγ ιδ ιε ιϛ ιζ ιη ιθ κ κα κβ κγ κδ κε κϛ κζ κη κθ λ'.split()
for n, i in (sorted((k, v[0]) for k, v in pares.items()) if os.path.exists(EST) else enumerate(cab, 1)):
    if SO and n not in SO: continue
    fim = pares[n][1] if os.path.exists(EST) else min([e for e in esc if e > i] + [cab[n] if n < len(cab) else len(blocos)])
    corpo = blocos[i + 2:fim]          # i = ΛΟΓΟΣ, i+1 = título Περὶ …
    # palavras com id, mantendo as marcas de coluna
    paras = []
    marcas_ini = re.findall(r'\{PG[^}]*\}', blocos[i]['texto'] + blocos[i + 1]['texto'])
    for b in corpo:
        paras.append([tuple(x) for x in b['pal']])
    chave = str(n)
    if chave not in cortes:     # primeira vez: cortes novos
        ini = []
        for seq in paras:
            cont = 0; abre = True
            for k, (p, tid) in enumerate(seq):
                if tid is None: continue
                if abre: ini.append(tid); abre = False; cont = 0
                cont += 1
                resto = sum(1 for q in seq[k + 1:] if q[1])
                prox = next((q[0] for q in seq[k + 1:] if q[1]), '')
                if cont >= ALVO and re.search(r'[.;]$', p) and resto >= 15 and prox.lstrip('«“(᾿’\'').strip()[:1].isupper(): abre = True
        cortes[chave] = ini
    ini = set(cortes[chave])
    saida, cur = [], []
    pend = list(marcas_ini)
    for seq in paras:
        for p, tid in seq:
            if tid is None: pend.append(p); continue
            if tid in ini and cur: saida.append(cur); cur = []
            cur.extend(pend); pend = []
            cur.append(p)
    if cur: saida.append(cur + pend)
    linhas = ['# titulo: ' + TITULOS[chave],
              '# fonte: Migne, Patrologia Graeca 88 (Paris, 1860), texto de M. Rader (1633); ver LEIAME.md', '',
              TITULOS[chave], '']
    for k, c in enumerate(saida, 1):
        t = ' '.join(c)
        linhas.append('[%d.%d] %s' % (n, k, t)); linhas.append('')
    open(os.path.join(pasta, 'degrau-%02d.txt' % n), 'w', encoding='utf-8').write('\n'.join(linhas).rstrip() + '\n')
    print(n, len(saida), 'blocos', sum(len(c) for c in saida), 'palavras')
json.dump(cortes, open(CORTES, 'w', encoding='utf-8'), ensure_ascii=False)
