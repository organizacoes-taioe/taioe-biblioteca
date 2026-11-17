"""Escolhe, do linhas.json, as linhas do texto de Clímaco (sem escólios, notas de pé, latim nem títulos lidos pelo
OCR) e põe no lugar dos títulos uma linha falsa ⟪H:chave⟫. Grava linhas-inicio.json e linhas-pastor.json.
Regras conferidas nas imagens (2026-11-16). Linhas a tirar depois da conferência: tirar.tsv (folha:idx)."""
import json, os, copy
AQUI = os.path.expanduser('~/.cache/claude-pedidos-0511/escada-2')
# parte: [(folha, [(de, até)], {idx_antes_do_qual_vem_um_título: chave})]
REGRAS = {
    'inicio': [
        (311, [(8, 33), (35, 36)], {8: 'ep1'}),
        (312, [(0, 39)], {16: 'resp'}),
        (313, [(0, 35), (38, 50)], {38: 'prol1'}),
        (315, [(3, 7)], {3: 'prol2'}),
    ],
    'pastor': [
        (582, [(2, 6), (15, 31)], {2: 'proem', 15: 'k1'}),
        (583, [(0, 20), (39, 44)], {39: 'k2'}),
        (584, [(0, 38)], {}),
        (585, [(30, 44)], {30: 'k3'}),
        (586, [(0, 9)], {0: 'k4'}),
        (588, [(1, 23), (25, 31)], {1: 'k5', 25: 'k6'}),
        (589, [(0, 19)], {}),
        (590, [(26, 45)], {26: 'k7'}),
        (591, [(0, 16), (18, 37), (40, 42)], {18: 'k8', 40: 'k9'}),
        (592, [(0, 31), (43, 44)], {12: 'k10', 43: 'k11'}),
        (593, [(0, 22)], {}),
        (594, [(0, 51)], {0: 'k12'}),
        (595, [(0, 12), (23, 24)], {23: 'k13'}),
        (596, [(0, 40)], {}),
        (597, [(0, 49)], {}),
        (598, [(25, 38)], {25: 'k14'}),
        (599, [(0, 54)], {}),
        (600, [(0, 23), (26, 46)], {26: 'k15'}),
        (601, [(0, 55)], {}),
        (602, [(0, 53)], {}),
        (603, [(0, 11)], {}),
    ],
}
tirar = set()
t = os.path.join(AQUI, 'tirar.tsv')
if os.path.exists(t):
    tirar = {l.split('\t')[0].strip() for l in open(t, encoding='utf-8') if l.strip()}
pags = {p['folha']: p for p in json.load(open(os.path.join(AQUI, 'linhas.json'), encoding='utf-8'))
        if not (p['folha'] == 588 and p['ci'] == 1) and p['folha'] != 587}
for parte, regras in REGRAS.items():
    saida = []
    for folha, faixas, tit in regras:
        p = copy.deepcopy(pags[folha])
        novas = []
        for de, ate in faixas:
            for i in range(de, ate + 1):
                if i in tit:
                    novas.append({'y': 0, 'y1': 0, 'x0': 0, 'rec': 999, 'id': None,
                                  'toks': [['⟪H:%s⟫' % tit[i], 99, 0, 900000 + i, 0, 900000 + i]]})
                l = p['linhas'][i]
                l['id'] = '%d:%d' % (folha, i)
                if l['id'] in tirar: continue
                if i in tit: l['rec'] = 999
                novas.append(l)
        p['linhas'] = novas
        saida.append(p)
    json.dump(saida, open(os.path.join(AQUI, 'linhas-%s.json' % parte), 'w', encoding='utf-8'), ensure_ascii=False)
    print(parte, sum(len(p['linhas']) for p in saida), 'linhas')
