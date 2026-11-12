"""Classifica a lista col-acentos.tsv da colação (as duas leituras do fac-símile iguais entre si, letras iguais às do
Perseus, sinais diferentes). Uso: acentos.py <pasta-trabalho>  → acentos-aceitos.tsv, acentos-ver.tsv
Aceitos sem ver (classes em que o OCR acerta): troca de agudo e grave na última sílaba; o agudo que a enclítica
acrescenta na última sílaba (πείθεσθαί μοι); ὁ/ἡ/οἱ/αἱ → ὃ/ἣ/οἳ/αἳ (o OCR não inventa um acento que não está lá);
τοὶ → τοι; χωρῇ → χώρῃ. Recusados sem ver (classes em que o OCR erra): espírito da maiúscula lido como apóstrofo,
apóstrofo solto, ὦν → ὧν e ἦν → ἣν (o espírito é ilegível no fac-símile e o OCR o troca em série), acento que
falta na leitura (o OCR perde sinais pequenos). O resto vai para acentos-ver.tsv, para conferir nas imagens."""
import sys, unicodedata as u
B = sys.argv[1]
ACU, GRA, CIRC, LEN, ASP = '́', '̀', '͂', '̓', '̔'
def sinais(w):
    return [c for c in u.normalize('NFD', w) if u.combining(c)]
def base(w):
    return ''.join(c for c in u.normalize('NFD', w) if not u.combining(c))
def ult_vogal(d):
    return max(i for i, c in enumerate(d) if not u.combining(c) and c.lower() in 'αεηιουω')
def classe(p, o):
    o = o.replace('᾽', '’'); p2 = p.replace('ʼ', '’')
    if any(ch in o for ch in "᾿'’") and not any(ch in p2 for ch in "’"): return 'recusa'
    if o[:1] in '᾿῾᾽': return 'recusa'
    if base(p).lower() != base(o).lower(): return 'ver'
    sp, so = sinais(p), sinais(o)
    if p in ('ὦν', 'ὧν') or (p == 'ἦν' and o == 'ἣν') or (p == 'ἢν' and o == 'ἣν'): return 'recusa'
    if p == 'χωρῇ': return 'aceita'
    if p == 'τοὶ' and o == 'τοι': return 'aceita'
    if len(so) < len(sp): return 'recusa' if [c for c in sp if c not in (ACU, GRA)] == so or (p[0].isupper()) else 'ver'
    if p in ('ὁ', 'ἡ', 'οἱ', 'αἱ') and len(so) == 2 and GRA in so: return 'aceita'
    dp, do = u.normalize('NFD', p), u.normalize('NFD', o)
    # troca de agudo e grave na última sílaba, resto igual
    if len(dp) == len(do):
        dif = [i for i in range(len(dp)) if dp[i] != do[i]]
        if len(dif) == 1 and {dp[dif[0]], do[dif[0]]} == {ACU, GRA}:
            i = dif[0]
            if not any(c.lower() in 'αεηιουω' for c in dp[i + 1:] if not u.combining(c)): return 'aceita'
    # agudo a mais na última vogal (enclítica)
    if len(do) == len(dp) + 1 and so.count(ACU) == sp.count(ACU) + 1:
        j = ult_vogal(do)
        k = j + 1
        while k < len(do) and u.combining(do[k]) and do[k] != ACU: k += 1
        if k < len(do) and do[k] == ACU and do[:k] + do[k + 1:] == dp: return 'aceita'
    return 'ver'
ac, ver, rec = [], [], 0
for l in open(B + '/col-acentos.tsv', encoding='utf-8'):
    if not l.strip(): continue
    r = l.rstrip('\n').split('\t')
    c = classe(r[1], r[2])
    if c == 'aceita': ac.append(r)
    elif c == 'ver': ver.append(r)
    else: rec += 1
open(B + '/acentos-aceitos.tsv', 'w', encoding='utf-8').write(''.join('\t'.join(r) + '\n' for r in ac))
open(B + '/acentos-ver.tsv', 'w', encoding='utf-8').write(''.join('\t'.join(r) + '\n' for r in ver))
print('aceitos', len(ac), 'a ver', len(ver), 'recusados', rec)
