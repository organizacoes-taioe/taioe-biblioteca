"""Monta edicoes/vidas-alexandre-cesar/original/ a partir do Perseus (Perrin 1919), com as correções do fac-símile.
Uso: montar.py <pasta-trabalho> <pasta-obra>"""
import json, os, re, sys, unicodedata as u
B, OBRA = sys.argv[1:3]
ACU, GRA = '́', '̀'
# correções conferidas no fac-símile (IA plutarchslives07plut) ou evidentes; (vida, seção, antes, depois)
CORR = [
    ('Alex', '2.1', 'ἐν θρᾴκῃ', 'ἐν Σαμοθρᾴκῃ'),
    ('Alex', '6.1', 'Φιλονίκου', 'Φιλονείκου'),
    ('Alex', '10.1', 'Πιξόδαρος', 'Πιξώδαρος'),
    ('Alex', '10.2', 'Πιξοδάρῳ', 'Πιξωδάρῳ'),
    ('Alex', '14.5', 'ʽἦν δὲ κυπαρίττινον?ʼ', '(ἦν δὲ κυπαρίττινον)'),
    ('Alex', '14.5', 'ποχὺν', 'πολὺν'),
    ('Alex', '16.2', 'οἱ βασιλεῖ τῶν', 'οἱ βασιλεῖς τῶν'),
    ('Alex', '23.4', 'κόλαζι', 'κόλαξι'),
    ('Alex', '33.3', 'συμμεμῖξαι', 'συμμῖξαι'),
    ('Alex', '35.1', 'τὸν πυρὸς', 'τοῦ πυρὸς'),
    ('Alex', '35.6', 'πυριγονοῦντα', 'πυριμανοῦντα'),
    ('Alex', '35.6', 'ἢ γένεσις ⟦gap⟧', 'ἡ γένεσις …'),
    ('Alex', '42.3', 'ἀνυδρίον', 'ἀνυδρίαν'),
    ('Alex', '47.2', 'μαρτνράμενος', 'μαρτυράμενος'),
    ('Alex', '47.2', 'προσαχθῆναι', 'προαχθῆναι'),
    ('Alex', '49.4', 'ὑπεροψίαν', 'ὑποψίαν'),
    ('Alex', '49.4', 'τὸν Λίμνου', 'τὸν Λίμνον'),
    ('Alex', '53.4', 'τῆς παλινῳδίαν', 'τὴν παλινῳδίαν'),
    ('Alex', '54.1', 'Καλλισθένη συνέντα', 'Καλλισθένην συνέντα'),
    ('Alex', '55.1', 'ὑπογινομένης', 'ὑπογενομένης'),
    ('Alex', '63.2', 'τ ὁ', 'τὸ'),
    ('Alex', '68.4', 'τρισχίλαι', 'τρισχίλια'),
    ('Alex', '70.3', 'εἶτʼ ἐφωράθη', 'εἶτα ἐφωράθη'),
    ('Alex', '76.4', 'Σεραπεῖον', 'Σαραπεῖον'),
    ('Caes', '2.4', 'ʽἦν γὰρ οὐκ ὀλίγα καὶ', '(ἦν γὰρ οὐκ ὀλίγα) καὶ'),
    ('Caes', '8.3', 'οἶ δα', 'οἶδα'),
    ('Caes', '15.2', 'τ?ε', 'τε'),
    ('Caes', '41.2', 'σύκων Διὰ', 'σύκων διὰ'),
    ('Caes', '41.2', 'ʽ νεωστὶ γὰρ ἐξ Ἰβηρίας ἀφῖκτο κακῶς στρατηγήσασʼ', '(νεωστὶ γὰρ ἐξ Ἰβηρίας ἀφῖκτο κακῶς στρατηγήσας)'),
    ('Caes', '41.2', 'ἠρώτα Διὰ τί', 'ἠρώτα διὰ τί'),
    ('Caes', '41.2', 'ἐπαρχίας, ἐκ', 'ἐπαρχίας. ἐκ'),
    ('Caes', '10.4', 'τοῦ Κλώδιον', 'τοῦ Κλωδίου'),
    ('Caes', '12.1', 'Καλαϊκοὺς', 'Καλλαϊκοὺς'),
    ('Caes', '15.2', 'Μετέλλονς', 'Μετέλλους'),
    ('Caes', '42.1', 'Ῥωμαίων, ⟦gap⟧', 'Ῥωμαίων, …'),
    ('Caes', '66.3', 'ἐντυχάνοντι', 'ἐντυγχάνοντι'),
    ('Caes', '68.4', 'Βροῦτον γέγραπται', 'Βρούτου γέγραπται'),
    ('Caes', '69.7', 'ὂψομαι', 'ὄψομαι'),
]
# agudo → grave onde o fac-símile tem grave (colação com o OCR)
GRAVES = {}
for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'acentos.tsv'), encoding='utf-8'):
    if not l.strip(): continue
    nome, p, o, ctx = l.rstrip('\n').split('\t')
    P = u.normalize('NFD', p.replace('ʼ', '’')); O = u.normalize('NFD', o.replace('᾽', '’'))
    if P.replace(ACU, GRA) == O and P.count(ACU) == 1 and P.rfind(ACU) > len(P) - 4:
        GRAVES.setdefault((nome.split()[0], nome.split()[1]), []).append(p)
def capitular(t):
    i = next(k for k, c in enumerate(t) if c.isalpha())
    return t[:i] + t[i].upper() + t[i+1:]
VIDAS = {
    'Alex': ('alex.json', 'alexandre', 'ΑΛΕΞΑΝΔΡΟΣ', [(1, 8), (9, 14), (15, 21), (22, 30), (31, 38), (39, 47), (48, 55), (56, 67), (68, 77)]),
    'Caes': ('caes.json', 'cesar', 'ΚΑΙΣΑΡ', [(1, 4), (5, 14), (15, 21), (22, 27), (28, 35), (36, 46), (47, 56), (57, 61), (62, 69)]),
}
# correções no texto montado (arquivo, antes, depois): restos soltos e erros de digitação do Perseus
FINAL = [
    ('alexandre-1-8.txt', 'καὶ Τὴν ὑγρότητα', 'καὶ τὴν ὑγρότητα'),
    ('alexandre-1-8.txt', 'ἐμιμήσατο Τὴν χρόαν', 'ἐμιμήσατο τὴν χρόαν'),
    ('alexandre-1-8.txt', 'καὶ Τὴν σάρκα', 'καὶ τὴν σάρκα'),
    ('alexandre-1-8.txt', 'τῶν δὲ ἀλλων', 'τῶν δὲ ἄλλων'),
    ('alexandre-15-21.txt', 'εἱώθεισαν', 'εἰώθεισαν'),
    ('alexandre-15-21.txt', 'πεσεῖν,’ πρὸς', 'πεσεῖν, πρὸς'),
    ('alexandre-15-21.txt', 'τοῦ μὲν ἀν ἀναγινώσκοντος', 'τοῦ μὲν ἀναγινώσκοντος'),
    ('alexandre-22-30.txt', '[22.4] ἢν δὲ', '[22.4] ἦν δὲ'),
    ('alexandre-22-30.txt', 'κύλικος, ἀει μακρόν', 'κύλικος, ἀεὶ μακρόν'),
    ('alexandre-22-30.txt', 'Ἀθηνοδορῳ', 'Ἀθηνοδώρῳ'),
    ('alexandre-22-30.txt', '[26.6] πται πρὸς τὴν ἤπειρον. ', '[26.6] '),
    ('alexandre-22-30.txt', 'φασιν οἳ πλεῖστοι', 'φασιν οἱ πλεῖστοι'),
    ('alexandre-56-67.txt', 'προσάγειν; καὶ γάρ ποταμὸς', 'προσάγειν (καὶ γὰρ ποταμὸς'),
    ('alexandre-31-38.txt', 'στενωπὸν ἐλαφρῶ τῷ', 'στενωπὸν ἐλαφρῷ τῷ'),
    ('alexandre-48-55.txt', 'ὁ ῝ Ἕρμιππός', 'ὁ Ἕρμιππός'),
    ('alexandre-56-67.txt', 'πρὸς αὐτῇ βαθὺσ’ ἐπιστὰς', 'πρὸς αὐτῇ βαθύς) ἐπιστὰς'),
    ('alexandre-56-67.txt', 'ἑαυτὸν εἷς μέσους', 'ἑαυτὸν εἰς μέσους'),
    ('alexandre-56-67.txt', 'τοὺς ἓν δόξῃ', 'τοὺς ἐν δόξῃ'),
    ('alexandre-68-77.txt', 'Πέρσαις ι πρῶτον', 'Πέρσαις πρῶτον'),
    ('alexandre-68-77.txt', 'τοῦτο δὲ · Ἡφαιστίωνος', 'τοῦτο δὲ Ἡφαιστίωνος'),
    ('alexandre-68-77.txt', 'βέλους εἷς τὸν ὀφθαλμόν', 'βέλους εἰς τὸν ὀφθαλμόν'),
    ('alexandre-68-77.txt', 'πολεμίους εἷς τὸ τεῖχος', 'πολεμίους εἰς τὸ τεῖχος'),
    ('cesar-47-56.txt', 'εἴτε καὶ σπουδῇ τὸν οἰωνὸν οἰκειούμενος, εἴτε καὶ σπουδῇ τὸν οἰωνὸν οἰκειούμενος,', 'εἴτε καὶ σπουδῇ τὸν οἰωνὸν οἰκειούμενος,'),
    ('cesar-57-61.txt', 'σεαυτόν;” λαμπρῶς, ὦ', 'σεαυτόν;”'),
]
usadas = set(); ngr = 0
os.makedirs(os.path.join(OBRA, 'original'), exist_ok=True)
for vida, (arq, nome, titulo, grupos) in VIDAS.items():
    d = json.load(open(os.path.join(B, arq), encoding='utf-8'))
    caps = {}
    for c, secs in d['caps']:
        blocos, cur = [], ''
        for s, t in secs:
            ref = f'{c}.{s}'
            t = t.replace('⟦n⟧', '')
            t = re.sub(r'\s*⟦l⟧\s*', '\n| ', t); t = re.sub(r'\s*⟦/l⟧\s*', '\n', t)
            for k, (v, r, a, b) in enumerate(CORR):
                if v == vida and r == ref:
                    if a not in t: sys.exit(f'correção não aplicada: {vida} {ref} {a}')
                    t = t.replace(a, b); usadas.add(k)
            for w in GRAVES.get((vida, ref), []):
                novo = u.normalize('NFC', u.normalize('NFD', w).replace(ACU, GRA))
                t2 = re.sub(r'(?<![\ẁ-ͯ])' + re.escape(w) + r'(?![\ẁ-ͯ])', novo, t, count=1)
                if t2 != t: ngr += 1
                t = t2
            t = t.replace('ʼ', '’').replace('ʽ', '‘')
            if '⟦' in t or '?' in t: sys.exit(f'sobrou marca: {vida} {ref}: {t[:80]}')
            partes = re.split(r'\n', t)
            texto = f'[{c}.{s}] '
            for p in partes:
                p = p.strip()
                if not p: continue
                if p.startswith('| '):
                    if not (blocos and blocos[-1].startswith('| ')) and cur.strip():
                        blocos.append(cur.strip()); cur = ''
                    if blocos and blocos[-1].startswith('| ') and not cur.strip():
                        blocos[-1] += '\n' + p
                    else:
                        if cur.strip(): blocos.append(cur.strip()); cur = ''
                        blocos.append(p)
                else:
                    if blocos and blocos[-1].startswith('| ') and not cur:
                        cur = texto + p if texto else p
                    else:
                        cur += (' ' if cur else '') + (texto + p if texto else p)
                    texto = ''
            if texto:  # seção que só tem verso: a marca vai no texto seguinte
                cur += (' ' if cur else '') + texto.strip()
        if cur.strip(): blocos.append(cur.strip())
        blocos[0] = re.sub(r'^(\[\d+\.\d+\] )(.)', lambda m: m.group(1) + m.group(2).upper(), blocos[0]) if blocos[0][len(f'[{c}.1] '):][:1].isalpha() else blocos[0]
        blocos[0] = blocos[0][:len(f'[{c}.1] ')] + capitular(blocos[0][len(f'[{c}.1] '):])
        caps[int(c)] = blocos
    for k, (a, b) in enumerate(grupos):
        cab = [f'# titulo: Πλουτάρχου Βίοι Παράλληλοι, {titulo} {a}–{b}',
               '# fonte: Perseus Digital Library, tlg0007.' + ('tlg047' if vida == 'Alex' else 'tlg048') + '.perseus-grc2 (CC BY-SA 4.0), https://github.com/PerseusDL/canonical-greekLit',
               '# edicao: Bernadotte Perrin, Plutarch\'s Lives, vol. VII (Loeb, Londres e Cambridge, Mass., 1919); conferido com o fac-símile do Internet Archive (plutarchslives07plut); ver LEIAME.md',
               '# marcas: «[1.1]» = capítulo.seção, a numeração usual; um parágrafo por capítulo', '']
        corpo = []
        if k == 0: corpo.append(titulo)
        for c in range(a, b + 1): corpo += caps[c]
        arq = f'{nome}-{a}-{b}.txt'; texto = '\n\n'.join(corpo)
        for f_, x, y in FINAL:
            if f_ == arq:
                if texto.count(x) != 1: sys.exit(f'{arq}: «{x}» aparece {texto.count(x)} vezes')
                texto = texto.replace(x, y)
        open(os.path.join(OBRA, 'original', arq), 'w', encoding='utf-8').write('\n'.join(cab) + '\n' + texto + '\n')
falta = [CORR[k] for k in range(len(CORR)) if k not in usadas]
print('graves', ngr, 'correções', len(usadas), 'não usadas', falta)
