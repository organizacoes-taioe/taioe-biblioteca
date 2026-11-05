"""Todas as ocorrências de uma chave no Macbeth, com o verso (para decidir se pede outro sentido, «chave#2»).
python3 edicoes/lingua-original/macbeth/ferramentas/ocorrencias.py <chave> [<chave> ...]"""
import os, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import lingua_original as L
mb = L.achar('macbeth')
g = L.ler_glossario('macbeth') or {'verbetes': {}, 'ocorrencias': {}}
oc = g.get('ocorrencias', {})
for alvo in sys.argv[1:]:
    print('### ' + alvo)
    for kp, x in L.partes_de(mb, True):
        linhas = {n: t for n, t, _i, _d in L.linhas_do_poema(mb, kp)}
        nome = os.path.splitext(os.path.basename(x['arquivo']))[0]
        for ref, pal, n, *_r in L.ocorrencias(mb, kp):
            k = oc.get(ref, L.chave(pal))
            if k.split('#')[0] == alvo.split('#')[0]:
                print('  %-9s %-5s [%s] %s' % (ref, nome, k, linhas[n].strip()))
