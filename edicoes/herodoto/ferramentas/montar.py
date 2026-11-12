"""Monta edicoes/herodoto/original/ a partir do Perseus (Godley 1920), com as correções do fac-símile.
Uso: montar.py <pasta-trabalho> <pasta-obra>
Ordem: extrair.py (l1.json) → graves.py (regras dos acentos) → colacao.py → acentos.py → este script, que aplica
CORR (letras, conferidas nas imagens), os acentos aceitos (acentos-aceitos.tsv, copiado em ferramentas/) e ACENTOS
(os conferidos à mão)."""
import json, os, re, sys, unicodedata as u
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graves import corrigir
B, OBRA = sys.argv[1:3]
AQUI = os.path.dirname(os.path.abspath(__file__))
# letras: (seção, antes, depois), conferidas no fac-símile de 1921 (pranchas da colação)
CORR = [
    ('32.7', 'ἔτι τελευτήσῃ', 'ἔτι τελευτήσει'), ('46.2', 'μαντείων', 'μαντηίων'), ('50.2', 'ἐπὶ μὰν', 'ἐπὶ μὲν'),
    ('55.1', 'μαντείου', 'μαντηίου'), ('60.5', 'Ἀηθναίη', 'Ἀθηναίη'), ('63.1', 'τρέπουσι', 'τράπουσι'),
    ('68.5', 'Λακεδαιμονίοσσι', 'Λακεδαιμονίοισι'), ('74.2', 'τῇ ἡμέρης', 'τῆς ἡμέρης'),
    ('80.5', 'ὤσφροντο', 'ὤσφραντο'), ('82.3', 'ἀπαμύνοιεν', 'ἐπαμύνοιεν'), ('116.3', 'ὁ Ἀστυάγεος', 'ὁ Ἀστυάγης'),
    ('117.2', 'τρέπεται', 'τράπεται'), ('119.2', 'ἐκπέμπεν', 'ἐκπέμπει'), ('134.3', 'ἀρχὸν τῶν', 'ἀρχόντων'),
    ('164.3', 'τὰ ἐν τῶν', 'τὰ ἐκ τῶν'), ('164.3', 'εἰσβάντες', 'ἐσβάντες'), ('165.1', 'Φωκαίες', 'Φωκαιέες'),
    ('170.3', 'περ ἐς δῆμοι', 'περ εἰ δῆμοι'), ('172.2', 'χέασθαι', 'χρᾶσθαι'), ('176.3', 'ἐκδημέουσι', 'ἐκδημέουσαι'),
    ('179.2', 'τάφου', 'τάφρου'), ('193.5', 'τὸν φοινίκων', 'τῶν φοινίκων'), ('199.1', 'ἀξιούμεναι', 'ἀξιεύμεναι'),
    ('199.5', 'ὅσσαι', 'ὅσαι'), ('202.2', 'ὀσμῇ', 'ὀδμῇ'), ('205.1', 'Μασαγετέων', 'Μασσαγετέων'),
    ('216.3', 'ἀλλʼ γῇ', 'ἀλλὰ γῇ'), ('173.3', 'καὶ νυν ἔτι', 'καὶ νῦν ἔτι'), ('42.2', 'χρηστοῖσἰ', 'χρηστοῖσι'),
]
# acentos e espíritos conferidos à mão (seção, forma do Perseus depois de graves.py, forma de Godley)
ACENTOS = [
    ('5.2', 'νέος', 'νεός'), ('7.4', 'γενεᾶς', 'γενεὰς'), ('10.2', 'νοῶ', 'νόῳ'), ('11.3', 'σε', 'σὲ'),
    ('19.1', 'ἅφθη', 'ἄφθη'), ('22.2', 'εἶπας', 'εἴπας'), ('86.5', 'εἶπας', 'εἴπας'), ('122.1', 'εἶπας', 'εἴπας'),
    ('128.2', 'εἶπας', 'εἴπας'), ('27.4', 'ὓπερ', 'ὑπὲρ'), ('31.1', 'ὀλβία', 'ὄλβια'), ('42.1', 'ἶσχον', 'ἴσχον'),
    ('44.1', 'τῳ', 'τῷ'), ('52.1', 'τῳ', 'τῷ'), ('47.3', 'ἃμʼ', 'ἅμʼ'), ('59.2', 'δευτέρα', 'δεύτερα'),
    ('112.2', 'δευτέρα', 'δεύτερα'), ('134.2', 'δευτέρα', 'δεύτερα'), ('179.2', 'δευτέρα', 'δεύτερα'),
    ('204.2', 'δευτέρα', 'δεύτερα'), ('61.2', 'οὒ', 'οὔ'), ('67.4', 'ἒνθʼ', 'ἔνθʼ'), ('68.1', 'ὀρέων', 'ὁρέων'),
    ('73.3', 'εἴλῃ', 'εἴλη'), ('82.2', 'χώρῇ', 'χώρῃ'), ('109.3', 'ἅπαις', 'ἄπαις'), ('111.3', 'πὸλλʼ', 'πόλλʼ'),
    ('114.1', 'αὑτὸν', 'αὐτὸν'), ('124.2', 'περὶ', 'πέρι'), ('125.2', 'Πέρσεων', 'Περσέων'), ('126.5', 'πείθεσθαί', 'πείθεσθαι'),
    ('136.2', 'ἰππεύειν', 'ἱππεύειν'), ('140.3', 'τἆλλα', 'τἄλλα'), ('141.2', 'ἐπεῖ', 'ἐπεὶ'), ('142.4', 'σφισι', 'σφίσι'),
    ('151.3', 'νῦν', 'νυν'), ('164.1', 'προισχόμενος', 'προϊσχόμενος'), ('164.2', 'δουλοσύνη', 'δουλοσύνῃ'),
    ('167.1', 'τῶ', 'τῷ'), ('176.1', 'ἀρετᾶς', 'ἀρετὰς'), ('183.2', 'μούνα', 'μοῦνα'), ('186.2', 'τούτω', 'τούτῳ'),
    ('187.1', 'ὕπερ', 'ὑπὲρ'), ('187.4', 'ὕπερ', 'ὑπὲρ'), ('188.1', 'προβάτοῖσι', 'προβάτοισι'), ('192.3', 'μυρίαι', 'μύριαι'),
    ('202.2', 'δίαιτᾳ', 'δίαιτα'), ('210.2', 'ἐστί', 'ἔστι'),
]
for l in open(os.path.join(AQUI, 'acentos-aceitos.tsv'), encoding='utf-8'):
    if not l.strip(): continue
    r = l.rstrip('\n').split('\t')
    novo = 'χώρῃ' if r[1] == 'χωρῇ' else r[2].replace('᾽', 'ʼ').replace('’', 'ʼ')
    if novo[:1] != r[1][:1] and novo[:1].lower() == r[1][:1]: novo = novo[0].lower() + novo[1:]
    if novo == 'ἢ' and r[1] == 'ἡ': novo = 'ἣ'
    ACENTOS.append((r[0], r[1], novo))
PARTES = [((1, 5), 'Proêmio: os raptos'), ((6, 14), 'Candaules e Giges'), ((15, 25), 'Os reis da Lídia e Árion'),
          ((26, 45), 'Creso, Sólon e Átis'), ((46, 58), 'Creso consulta os oráculos'), ((59, 70), 'Atenas e Esparta'),
          ((71, 84), 'A guerra com Ciro e a tomada de Sardes'), ((85, 94), 'Creso na fogueira; os lídios'),
          ((95, 106), 'Os medos'), ((107, 122), 'O nascimento de Ciro'), ((123, 130), 'Ciro contra Astíages'),
          ((131, 140), 'Os costumes dos persas'), ((141, 161), 'Os jônios e Pactias'),
          ((162, 176), 'Hárpago na Jônia, na Cária e na Lícia'), ((177, 187), 'Babilônia e as suas rainhas'),
          ((188, 200), 'Ciro toma Babilônia; os costumes dos babilônios'), ((201, 216), 'Tômiris e a morte de Ciro')]
PAL = re.compile(r'[\ẁ-ͯʼ]+')
def troca_palavra(t, a, b):
    for m in PAL.finditer(t):
        if m.group() == a:
            return t[:m.start()] + b + t[m.end():], True
    return t, False
def capitular(t):
    i = next(k for k, c in enumerate(t) if c.isalpha())
    return t[:i] + t[i].upper() + t[i + 1:]
d = json.load(open(os.path.join(B, 'l1.json'), encoding='utf-8'))
usadas, ac_usados, ngr, ndu = set(), set(), 0, 0
caps = {}
for c, secs in d['caps']:
    blocos, cur = [], ''
    for s, t in secs:
        ref = f'{c}.{s}'
        for k, (r, a, b) in enumerate(CORR):
            if r == ref:
                if t.count(a) != 1: sys.exit(f'correção {ref} «{a}» aparece {t.count(a)} vezes')
                t = t.replace(a, b); usadas.add(k)
        t, g1, g2 = corrigir(t); ngr += g1; ndu += g2
        for k, (r, a, b) in enumerate(ACENTOS):
            if r == ref:
                t, ok = troca_palavra(t, a, b)
                if not ok: sys.exit(f'acento {ref} «{a}» não achado')
                ac_usados.add(k)
        t = t.replace('⟦n⟧', '')
        t = re.sub(r'\s*⟦gap⟧\s*', ' … ', t)
        t = t.replace('ʼ', '’')
        t = re.sub(r'\s*⟦l⟧\s*', '\n| ', t); t = re.sub(r'\s*⟦/l⟧\s*', '\n', t)
        t = re.sub(r' +([.,·;])', r'\1', t)
        if '⟦' in t: sys.exit(f'sobrou marca: {ref}')
        texto = f'[{c}.{s}] '
        for p in t.split('\n'):
            p = p.strip()
            if not p: continue
            if p.startswith('| '):
                if cur.strip(): blocos.append(cur.strip()); cur = ''
                if blocos and blocos[-1].startswith('| ') and not cur: blocos[-1] += '\n' + p
                else: blocos.append(p)
            else:
                cur += (' ' if cur else '') + (texto + p if texto else p); texto = ''
        if texto:
            cur += (' ' if cur else '') + texto.strip()
    if cur.strip(): blocos.append(cur.strip())
    # maiúscula no começo do capítulo, como em Godley
    m = re.match(r'(\[\d+\.\d+\] )(.*)$', blocos[0], re.S)
    blocos[0] = m.group(1) + capitular(m.group(2))
    caps[int(c)] = blocos
falta = [CORR[k] for k in range(len(CORR)) if k not in usadas] + [ACENTOS[k] for k in range(len(ACENTOS)) if k not in ac_usados]
if falta: sys.exit(f'não aplicadas: {falta}')
os.makedirs(os.path.join(OBRA, 'original'), exist_ok=True)
for k, ((a, b), tit) in enumerate(PARTES):
    cab = [f'# titulo: Ἡροδότου Ἱστορίαι Α, {a}–{b}',
           '# fonte: Perseus Digital Library, tlg0016.tlg001.perseus-grc2 (CC BY-SA 4.0), https://github.com/PerseusDL/canonical-greekLit',
           '# edicao: A. D. Godley, Herodotus, vol. I (Loeb, Londres e Nova York, 1920); conferido com o fac-símile da impressão de 1921 (Internet Archive herodotud0000adgo); ver LEIAME.md',
           '# marcas: «[1.1]» = capítulo.seção do livro I, a numeração usual; um parágrafo por capítulo', '']
    corpo = ['Α · ΚΛΕΙΩ'] if k == 0 else []
    for c in range(a, b + 1): corpo += caps[c]
    open(os.path.join(OBRA, 'original', f'livro1-{a}-{b}.txt'), 'w', encoding='utf-8').write('\n'.join(cab) + '\n' + '\n\n'.join(corpo) + '\n')
print('graves', ngr, 'acentos duplos', ndu, 'letras', len(usadas), 'acentos', len(ac_usados))
