import csv, sys, unicodedata, re
def k(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]', '', s).split()
arq = sys.argv[1]
n = 0
for r in csv.reader(open(arq, encoding='utf-8'), delimiter='\t'):
    if r[0] == 'diferem' or 'ob' not in r[0]:
        continue
    este, mods = r[2], r[3]
    if len(este) > 200:
        continue
    m = dict(x.split(': ', 1) if ': ' in x else (x.rstrip(':'), '') for x in mods.split(' || '))
    ob = m.get('ob', '')
    ws = m.get('ws', '')
    if k(ob) == k(este):
        continue
    if 'ws' in r[0] and k(ws) != k(ob):
        flag = 'ob'
    else:
        flag = 'ws=ob'
    n += 1
    print(f"{flag}\t…{r[1][-40:]} [{este}] {r[4][:30]}…\tws: {ws} | ob: {ob}")
print(n, file=sys.stderr)
