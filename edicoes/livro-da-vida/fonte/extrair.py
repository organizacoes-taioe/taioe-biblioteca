"""Extrai a Vida (Silverio 1915, BMC 1) do hOCR: capítulos e parágrafos, sem cabeços nem notas de rodapé."""
import json, re, sys, statistics
P = json.load(open(sys.argv[1]))
INI, FIM = 140, 511   # índices das páginas: «LA VIDA…» até o fim do epílogo
blocos = []   # (tipo, texto, pagina)
def eh_nota(l, alt):
    return re.match(r'^[1-9]\d?\s+\S', l[4]) and alt < 68
for idx in range(INI, FIM + 1):
    p, ls = P[idx]
    ls = [l for l in ls if l[4].strip()]
    corpo = []
    for l in ls:
        alt = l[3] - l[1]
        if l[1] < 430 and alt < 75:       # cabeço: número da página, título corrido
            continue
        corpo.append(l)
    # notas de rodapé: a sequência final de linhas juntas (passo < 100 px; o corpo tem ~124)
    while corpo and corpo[-1][2] - corpo[-1][0] < 200 and len(corpo[-1][4]) < 6:
        corpo = corpo[:-1]                       # assinatura de caderno, sujeira
    k = len(corpo) - 1
    while k > 0 and corpo[k][1] - corpo[k - 1][1] < 100:
        k -= 1
    if k < len(corpo) - 1:
        corpo = corpo[:k]
    elif corpo and re.match(r'^[1-9]\d?\s', corpo[-1][4]) and corpo[-1][3] - corpo[-1][1] < 70:
        corpo = corpo[:-1]
    xs = [l[0] for l in corpo if l[2] - l[0] > 1500]
    if not xs:
        for l in corpo: blocos.append(('?', l[4], p))
        continue
    esq = statistics.median(sorted(xs)[:max(1, len(xs)//2)])
    for l in corpo:
        larg = l[2] - l[0]
        recuo = l[0] - esq
        t = l[4]
        if re.match(r'^CAP[IÍ]TULO\b', t, re.I) and (recuo > 400):
            blocos.append(('CAP', t, p)); continue
        if recuo > 120 and recuo < 330 and larg > 800:
            blocos.append(('PAR', t, p))
        elif recuo > 330:
            blocos.append(('CENTRO', t, p))
        else:
            blocos.append(('LIN', t, p))
json.dump(blocos, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
print(len(blocos))
