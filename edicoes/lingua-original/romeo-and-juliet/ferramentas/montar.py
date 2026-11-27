"""cenas.json (Cambridge 1865) → os arquivos das partes do Romeo and Juliet, no formato da língua original.
python3 -I montar.py cenas.json <pasta de saída>"""
import json, os, re, sys
c = json.load(open(sys.argv[1], encoding='utf-8'))
saida = sys.argv[2]
FALAS = {'Rom.': 'Romeo', 'Jul.': 'Juliet', 'Nurse.': 'Nurse', 'Ben.': 'Benvolio', 'Mer.': 'Mercutio',
 'Cap.': 'Capulet', 'Fri. L.': 'Friar Laurence', 'Fr. L.': 'Friar Laurence', 'Fri.': 'Friar Laurence',
 'La. Cap.': 'Lady Capulet', 'Par.': 'Paris', 'Sam.': 'Sampson', 'Tyb.': 'Tybalt', 'Gre.': 'Gregory',
 'Bal.': 'Balthasar', 'Pet.': 'Peter', 'Peter.': 'Peter', 'Prince.': 'Prince', 'Prin.': 'Prince',
 'Mon.': 'Montague', 'Serv.': 'Servant', 'First Serv.': 'First Servant', 'Sec. Serv.': 'Second Servant',
 'Third Serv.': 'Third Servant', 'First Mus.': 'First Musician', 'Sec. Mus.': 'Second Musician',
 'Third Mus.': 'Third Musician', 'First Watch.': 'First Watchman', 'Sec. Watch.': 'Second Watchman',
 'Abr.': 'Abraham', 'Ap.': 'Apothecary', 'Fri. J.': 'Friar John', 'Page.': 'Page', 'Chor.': 'Chorus',
 'La. Mon.': 'Lady Montague', 'Sec. Cap.': 'Second Capulet', 'First Cit.': 'First Citizen',
 'First Off.': 'First Officer'}
ABREV = {'Fri. L.': 'Friar Laurence', 'First Serv.': 'First Servant', 'Sec. Serv.': 'Second Servant', 'Rom.': 'Romeo', 'Jul.': 'Juliet', 'Ben.': 'Benvolio', 'Mer.': 'Mercutio', 'Cap.': 'Capulet',
 'La. Cap.': 'Lady Capulet', 'Tyb.': 'Tybalt', 'Par.': 'Paris'}
# (cena, começo do texto) → True: continua o verso anterior; False: verso novo
FORCAR = {(8, 'A thousand times good night'): True, (17, '[_Within_] Ho, daughter'): True,
 (25, '[_Within_] Lead, boy'): True}
# erros da transcrição do PG (colação com a Globe do MIT) e abreviações nas rubricas de dentro da fala
CORRIGIR = [('rather than many Paris', 'rather than marry Paris'), ('[Exit First Serv.]', '[Exit First Servant.]'),
 ('[Exit Sec. Serv.]', '[Exit Second Servant.]'), ('[Exit Sec. Servant.]', '[Exit Second Servant.]')]
# (cena, começo do texto): a linha que o PG quebrou e que, pela numeração da edição, é um verso só, junta-se à anterior
JUNTAR = {(3, 'the county stays.'), (25, 'that:')}
# (cena, texto inteiro, onde partir): a linha de prosa que o PG juntou e que, pela numeração, são duas
DIVIDIR = {(10, "Romeo, will you come to your father's? we'll to dinner thither."): "father's? "}
ROMANOS = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8}

def nomes(s):
    # DUNCAN → Duncan; LADY MACBETH → Lady Macbeth
    return re.sub(r"\b([A-Z])([A-Z']+)\b", lambda m: m.group(1) + m.group(2).lower(), s)

def rubrica(s):
    s = s.replace('_', '').strip()
    s = s.lstrip('[').strip()
    for a, b in ABREV.items():
        s = s.replace('to ' + a, 'to ' + b)
        s = re.sub(r'^Exit ' + re.escape(a) + '$', 'Exit ' + b + '.', s)
    s = nomes(s)
    s = re.sub(r'\bLady M\.$', 'Lady Macbeth.', s)   # III.4: «Exeunt all but MACBETH and LADY M.»
    return ' '.join(s.split())

def continua(k, x):
    _, fala, ind, esp, lead, t, num, dl = x
    for (cena, ini), v in FORCAR.items():
        if cena == k and t.startswith(ini):
            return v
    # o recuo i2 (e os das canções, i8–i14) é o das rimas alternadas, não meio-verso
    return bool((fala and esp > 3) or (not fala and (ind > 20 or lead > 0)))

os.makedirs(saida, exist_ok=True)
partes = []; avisadas = set()
for k, s in enumerate(c):
    if s['ato'] == 'PROLOGUE':
        ato, cena, romano, local = 0, 0, None, None
    else:
        romano = re.match(r'ACT ([IVX]+)', s['ato']).group(1)
        ato = ROMANOS[romano]
        m = re.match(r'SCENE ([IVX]+)\.\s*(.*)$', s['titulo'], re.S)
        if m:
            cena = ROMANOS[m.group(1)]
            local = rubrica(m.group(2))
            if local.isupper():
                local = local[:1] + local[1:].lower()   # III.5: o título em versalete no PG
                local = local.replace('capulet', 'Capulet')
        else:
            cena, local = 0, None   # o prólogo do Ato II
    out = ['::rubrica ' + local, ''] if local else []
    n = 0; ultimo = None   # (indentação, texto) do último verso, para os meios-versos
    numeros = {}; hist = []
    itens = []
    for x in s['itens']:
        if x[0] == 'linha' and not x[1] and (k, x[5]) in JUNTAR and itens and itens[-1][0] == 'linha':
            y = list(itens[-1]); y[5] = y[5] + ' ' + x[5]; y[6] = x[6] if x[6] is not None else y[6]; y[7] = x[7] or y[7]
            itens[-1] = y; continue
        if x[0] == 'linha' and (k, x[5]) in DIVIDIR:
            corte = x[5].index(DIVIDIR[(k, x[5])]) + len(DIVIDIR[(k, x[5])])
            a = list(x); a[5] = x[5][:corte].rstrip(); a[6] = None; a[7] = None
            b = list(x); b[1] = None; b[3] = 0; b[4] = 0; b[5] = x[5][corte:]
            itens += [a, b]; continue
        itens.append(x)
    for j, x in enumerate(itens):
        if x[0] == 'quebra':
            continue
        if x[0] == 'rubrica':
            if out and out[-1] != '':
                out.append('')
            out.append('::rubrica ' + rubrica(x[2]))
            out.append('')
            continue
        _, fala, ind, esp, lead, t, num, dl = x
        t = t.replace('_', '')
        t = re.sub(r'\[([^\]]*)', lambda mm: '[' + mm.group(1), t)
        for a, b in ABREV.items():
            t = t.replace('Aside to ' + a, 'Aside to ' + b)
        if fala == 'Macb.' and t == '}':
            continue   # a fala conjunta de Macbeth e Lennox (II.3): vem na linha seguinte
        if fala == 'Len.' and t.startswith('}'):
            fala = 'Macbeth, Lennox'; t = t.lstrip('}').strip(); x = list(x); x[3] = 21; x[5] = t
        if fala == 'Fri.' and t.startswith('L. '):
            fala = 'Fri. L.'; t = t[3:]   # II.3: «Fri.» em itálico e «L.» fora, no PG
            x = list(x); x[5] = t
        for a, b in CORRIGIR:
            t = t.replace(a, b)
        cont = continua(k, x)
        if fala:
            if out and out[-1] != '':
                out.append('')
            out.append('::fala ' + FALAS.get(fala, fala))
        if not cont:
            n += 1; ind_txt = 0
        else:
            ind_txt = ultimo[0] + len(ultimo[1]) + 1 if ultimo else 4
        hist.append((n, cont, fala or '', ind, esp, lead, t[:40]))
        if num is not None and num - n != numeros.get(k, 0):
            numeros[k] = num - n
            print('numeração: %d.%d cena %d: esperava %d, deu %d: %s' % (ato, cena, k, num, n, t))
            for h in hist[-12:]: print('     ', h)
        if dl:
            t = t + ' [' + rubrica(dl) + ']'
            for a, b in CORRIGIR:
                t = t.replace(a, b)
        out.append(' ' * ind_txt + t)
        ultimo = (ind_txt, t if not dl else t[:t.rfind(' [')])
    while out and out[-1] == '':
        out.pop()
    nome = '0-prologo.txt' if ato == 0 else '%d-%d.txt' % (ato, cena)
    with open(os.path.join(saida, nome), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    titulo = 'Prólogo' if ato == 0 else 'Ato %s, prólogo' % romano if cena == 0 else 'Ato %s, cena %d' % (romano, cena)
    partes.append({'titulo': titulo, 'arquivo': 'partes/' + nome, 'versos': n})
json.dump(partes, open(os.path.join(sys.argv[3] if len(sys.argv) > 3 else os.path.join(saida, '..'), 'partes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(partes), 'partes,', sum(p['versos'] for p in partes), 'versos')
