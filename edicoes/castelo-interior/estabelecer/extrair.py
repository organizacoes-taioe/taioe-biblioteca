"""Tira o corpo do texto das Moradas de um .pag.json (sem cabeço nem notas de rodapé) -> lista de linhas
com marcas: cada linha 'P|' (parágrafo novo) ou 'C|' (continua), e 'PG|n' (página)."""
import json, re, sys, statistics

def corpo(arq):
    ps = json.load(open(arq))
    # início: página com «Pocas cosas que me ha mandado»; fim: «víspera de San Andrés»
    ini = fim = None
    for i, p in enumerate(ps):
        tx = ' '.join(l['t'] for l in p['linhas'])
        if ini is None and re.search(r'Pocas\s+cosas\s+que\s+me\s+ha\s+mandado', tx):
            ini = i
        if ini is not None and re.search(r'v[ií]spera\s+de\s+San\s+Andr', tx):
            fim = i; break
    # voltar uma página se o título «ESTE TRATADO» estiver na anterior
    out = []
    todas = sorted(l['h'] for i in range(ini, fim + 1) for l in ps[i]['linhas'] if len(l['t']) > 30)
    HG = todas[len(todas) // 2]
    for i in range(ini - 1, fim + 1):
        p = ps[i]; L = p['linhas']
        if not L: continue
        lg = [l for l in L if len(l['t']) > 30]
        if lg:
            cL = sorted(l['x0'] for l in lg)[len(lg)//2]; cR = sorted(l['x1'] for l in lg)[len(lg)//2]
            L = [l for l in L if l['x0'] < cR - 150 and l['x1'] > cL + 60 and (l['x1'] - l['x0']) > 1.5 * l['h']]
        if not L: continue
        hs = sorted(l['h'] for l in L); med = hs[len(hs) // 2]
        # altura do corpo: mediana das linhas mais altas que 0.8 do máximo comum
        Hb = HG
        # cabeço: 1ª linha, se no alto e pequena ou com número
        k0 = 0
        if L and (L[0]['h'] < 0.88 * Hb or re.search(r'^\W*\d+\s|\s\d+\W*$|CASTILLO|MORADAS|CAP[IÍ]TULO', L[0]['t'])) and L[0]['top'] < 0.1 * p['H']:
            # cuidado: título de capítulo no alto da página não tem número
            if re.search(r'\d', L[0]['t']) or 'CASTILLO INTERIOR' in L[0]['t'] or len(L) > 1 and L[1]['top'] - L[0]['bot'] > 1.5 * Hb:
                k0 = 1
        # rodapé: linhas pequenas no fim, depois da última linha de corpo
        k1 = len(L)
        ultimo_corpo = max((j for j, l in enumerate(L) if l['h'] >= 0.86 * Hb and len(l['t']) > 25), default=len(L) - 1)
        difs = sorted(L[j]['top'] - L[j - 1]['top'] for j in range(max(1, k0 + 1), ultimo_corpo + 1) if L[j]['h'] >= 0.86 * Hb and L[j - 1]['h'] >= 0.86 * Hb)
        esp = difs[len(difs) // 2] if difs else 2 * Hb
        for j in range(ultimo_corpo + 1, len(L)):
            if L[j]['top'] - L[j - 1]['top'] > 1.45 * esp or (L[j]['h'] < 0.86 * Hb and len(L[j]['t']) > 20):
                k1 = j; break
        # chamada de nota no começo da linha, na metade de baixo: começa o rodapé
        for j in range(k0, k1):
            if L[j]['top'] > 0.45 * p['H'] and re.match(r'^[0-9]{1,2}\s+[A-ZÁÉÍÓÚ¿¡«/]', L[j]['t']) and L[j]['h'] < 0.95 * Hb:
                k1 = j; break
        body = L[k0:k1]
        if not body: continue
        xs = sorted(l['x0'] for l in body if len(l['t']) > 30)
        esq = xs[len(xs) // 5] if xs else min(l['x0'] for l in body)
        dirs = sorted(l['x1'] for l in body if len(l['t']) > 30)
        dir_ = dirs[len(dirs) * 4 // 5] if dirs else max(l['x1'] for l in body)
        out.append(f'PG|{i}')
        prev = None
        for jj, l in enumerate(body):
            viz = [b['x0'] for b in body[max(0, jj - 4):jj] + body[jj + 1:jj + 5] if len(b['t']) > 30]
            ref = sorted(viz)[len(viz) // 2] if len(viz) >= 3 else esq
            ref = min(ref, sorted(viz)[0] + 0.5 * Hb) if viz else ref
            ind = l['x0'] - ref
            novo = ind > 0.6 * Hb and (prev is None or prev['x1'] < dir_ - 1.2 * Hb or ind > 2.2 * Hb)
            if prev is not None and prev['t'].rstrip().endswith('-'):
                novo = False
            if prev is not None and l['top'] - prev['bot'] > 1.6 * Hb:
                novo = True
            out.append(('P|' if novo else 'C|') + l['t'] + f"\t{i},{l['top']},{l['bot']}")
            prev = l
    return out

if __name__ == '__main__':
    linhas = corpo(sys.argv[1])
    open(sys.argv[2], 'w').write('\n'.join(linhas) + '\n')
    print(sys.argv[2], len(linhas))
