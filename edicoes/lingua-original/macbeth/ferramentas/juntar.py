"""Junta um lote de verbetes ao glossario.json do Macbeth e confere as partes.
python3 edicoes/lingua-original/macbeth/ferramentas/juntar.py <lote.json> [<parte> ...]
O lote: {"verbetes": {chave: verbete}, "ocorrencias": {ref: chave}, "substituir": [chaves]} (substituir:
as chaves que já existem e o lote refaz). As elisões i', o' e th' (in, of/on, the) recebem sozinhas as
chaves «i'», «o'» e «th'»."""
import json, os, re, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import lingua_original as L

ARQ = os.path.join(L.EDICAO, 'macbeth', 'glossario.json')
g = L.ler_glossario('macbeth') or {'verbetes': {}, 'ocorrencias': {}}
lote = json.load(open(sys.argv[1], encoding='utf-8'))
subst = set(lote.get('substituir', []))
erros = []
for k, v in lote.get('verbetes', {}).items():
    if k in g['verbetes'] and k not in subst and g['verbetes'][k] != v:
        erros.append('a chave «%s» já existe (ponha em "substituir" para refazer)' % k)
    g['verbetes'][k] = v
g.setdefault('ocorrencias', {}).update(lote.get('ocorrencias', {}))
# elisões
mb = L.achar('macbeth')
for kp, x in L.partes_de(mb, True):
    linhas = {}
    for n, t, i, d in L.linhas_do_poema(mb, kp):
        linhas[n] = t
    for ref, pal, n, i, a, b in L.ocorrencias(mb, kp):
        t = linhas[n]
        # a posição a, b é dentro do texto da linha (sem o «::marca»)
        if pal.lower() in ('i', 'o', 'th') and t[b:b + 1] == "'" and not t[b + 1:b + 2].isalpha():
            g['ocorrencias'].setdefault(ref, pal.lower() + "'")
g['verbetes'] = dict(sorted(g['verbetes'].items(), key=lambda kv: kv[0]))
g['ocorrencias'] = dict(sorted(g['ocorrencias'].items(), key=lambda kv: [int(x) if x.isdigit() else x for x in re.split(r'[:.]', kv[0])]))
if erros:
    print('\n'.join(erros))
    sys.exit('nada gravado')
with open(ARQ, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(g, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('glossário: %d verbetes, %d ocorrências marcadas' % (len(g['verbetes']), len(g['ocorrencias'])))
ok = True
for parte in sys.argv[2:]:
    probs = L.conferir('macbeth', parte=parte)
    probs = [p for p in probs if 'não é usado' not in p]
    for p in probs[:30]:
        print('  ' + p)
    if len(probs) > 30:
        print('  … e mais %d' % (len(probs) - 30))
    ok = ok and not probs
sys.exit(0 if ok else 1)
