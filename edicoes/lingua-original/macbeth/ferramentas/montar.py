"""cenas.json (Cambridge 1865) → os arquivos das partes do Macbeth, no formato da língua original.
python3 -I montar.py cenas.json <pasta de saída>"""
import json, os, re, sys
c = json.load(open(sys.argv[1], encoding='utf-8'))
saida = sys.argv[2]
FALAS = {'Macb.': 'Macbeth', 'Macd.': 'Macduff', 'Lady M.': 'Lady Macbeth', 'Lady Macb.': 'Lady Macbeth',
 'Mal.': 'Malcolm', 'Ross.': 'Ross', 'Ban.': 'Banquo', 'First Witch.': 'First Witch', 'Sec. Witch.': 'Second Witch',
 'Third Witch.': 'Third Witch', 'Len.': 'Lennox', 'Doct.': 'Doctor', 'L. Macd.': 'Lady Macduff', 'Dun.': 'Duncan',
 'First Mur.': 'First Murderer', 'Sec. Mur.': 'Second Murderer', 'Third Mur.': 'Third Murderer', 'Mur.': 'Murderer',
 'Both Mur.': 'Both Murderers', 'Son.': 'Son', 'All.': 'All', 'Gent.': 'Gentlewoman', 'Siw.': 'Siward',
 'Yo. Siw.': 'Young Siward', 'Mess.': 'Messenger', 'Serv.': 'Servant', 'Ment.': 'Menteith', 'Old M.': 'Old Man',
 'Sey.': 'Seyton', 'Scy.': 'Seyton', 'Ser.': 'Sergeant', 'Ang.': 'Angus', 'Aug.': 'Angus', 'Port.': 'Porter',
 'Porter.': 'Porter', 'Don.': 'Donalbain', 'Lords.': 'Lords', 'Lord.': 'Lord', 'Caith.': 'Caithness',
 'Fle.': 'Fleance', 'Hec.': 'Hecate', 'First App.': 'First Apparition', 'Sec. App.': 'Second Apparition',
 'Third App.': 'Third Apparition', 'Attend.': 'Attendant', 'Soldiers.': 'Soldiers'}
ABREV = {'Don.': 'Donalbain', 'Mal.': 'Malcolm', 'Macb.': 'Macbeth', 'Lady M.': 'Lady Macbeth', 'Macd.': 'Macduff',
 'Ban.': 'Banquo', 'Len.': 'Lennox'}
# (cena, começo do texto) → True: continua o verso anterior; False: verso novo
FORCAR = {(2, 'And for an earnest of a greater'): False, (6, 'How now! what news?'): True,
 (8, "[_Within_] Who's there? what, ho!"): True, (14, 'Good night; and better health'): True,
 (17, "What's your grace's will?"): True, (2, '[_Aside_] Glamis, and thane'): True,
 (9, 'Look to the lady.'): True, (2, '[_Aside_] Come what come may'): True, (2, '[_Aside_] Two truths are told'): True, (17, 'Ay, my good lord.'): True}
ROMANOS = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8}

def nomes(s):
    # DUNCAN → Duncan; LADY MACBETH → Lady Macbeth
    return re.sub(r"\b([A-Z])([A-Z']+)\b", lambda m: m.group(1) + m.group(2).lower(), s)

def rubrica(s):
    s = s.replace('_', '').strip()
    s = s.lstrip('[').strip()
    for a, b in ABREV.items():
        s = s.replace('to ' + a, 'to ' + b)
    s = nomes(s)
    s = re.sub(r'\bLady M\.$', 'Lady Macbeth.', s)   # III.4: «Exeunt all but MACBETH and LADY M.»
    return ' '.join(s.split())

def continua(k, x):
    _, fala, ind, esp, lead, t, num, dl = x
    for (cena, ini), v in FORCAR.items():
        if cena == k and t.startswith(ini):
            return v
    return bool((fala and esp > 1) or (not fala and (ind > 1 or lead > 0)))

os.makedirs(saida, exist_ok=True)
partes = []; avisadas = set()
for k, s in enumerate(c):
    ato = ROMANOS[re.match(r'ACT ([IVX]+)', s['ato']).group(1)]
    m = re.match(r'SCENE ([IVX]+)\.\s*(.*)$', s['titulo'])
    cena = ROMANOS[m.group(1)]
    local = rubrica(m.group(2))
    out = ['::rubrica ' + local, '']
    n = 0; ultimo = None   # (indentação, texto) do último verso, para os meios-versos
    numeros = {}; hist = []
    itens = s['itens']
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
        cont = continua(k, x)
        if fala:
            if out and out[-1] != '':
                out.append('')
            out.append('::fala ' + FALAS.get(fala, fala))
        if not cont:
            n += 1; ind_txt = 0
        else:
            ind_txt = ultimo[0] + len(ultimo[1]) + 1 if ultimo else 4
        hist.append((n, cont, t[:45]))
        if num is not None and num != n and k not in avisadas:
            avisadas.add(k)
            print('numeração: %d.%d cena %d: esperava %d, deu %d: %s' % (ato, cena, k, num, n, t))
            for h in hist[-9:]: print('     ', h)
        if dl:
            t = t + ' [' + rubrica(dl) + ']'
        out.append(' ' * ind_txt + t)
        ultimo = (ind_txt, t if not dl else t[:t.rfind(' [')])
    while out and out[-1] == '':
        out.pop()
    nome = '%d-%d.txt' % (ato, cena)
    with open(os.path.join(saida, nome), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    partes.append({'titulo': 'Ato %s, cena %d' % (m and re.match(r'ACT ([IVX]+)', s['ato']).group(1), cena), 'arquivo': 'partes/' + nome, 'versos': n})
json.dump(partes, open(os.path.join(saida, '..', 'partes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(partes), 'partes,', sum(p['versos'] for p in partes), 'versos')
