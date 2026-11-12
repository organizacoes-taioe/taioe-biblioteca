#!/bin/bash
# junta os trechos traduzidos (trad/p<N>-*.txt) em traducao/parte-<N>.txt e confere os blocos com o original
R=~/.cache/claude-pedidos-0511/teoria-da-relatividade; T=~/.cache/claude-wt5-teoria-da-relatividade/edicoes/teoria-da-relatividade
declare -A TIT=([1]="Primeira parte: A teoria da relatividade especial" [2]="Segunda parte: A teoria da relatividade geral" [3]="Terceira parte: Considerações sobre o universo como um todo")
for n in 1 2 3; do
  ls $R/trad/p$n-*.txt >/dev/null 2>&1 || continue
  { echo "# titulo: ${TIT[$n]}"; echo; for f in $R/trad/p$n-*.txt; do cat "$f"; echo; done; } | sed -e '/^$/N;/^\n$/D' > $T/traducao/parte-$n.txt
done
python3 -I - <<'PY'
import os,re
T=os.path.expanduser('~/.cache/claude-wt5-teoria-da-relatividade/edicoes/teoria-da-relatividade')
for f in sorted(os.listdir(T+'/traducao')):
    if not f.endswith('.txt'): continue
    bl=lambda p:[b for b in open(p).read().split('\n\n') if b.strip() and not b.startswith('# ')]
    a,b=bl(T+'/original/'+f),bl(T+'/traducao/'+f)
    n=min(len(a),len(b)); bad=[k for k in range(n) if (a[k][:2] in ('##','¤ ','| ')) != (b[k][:2] in ('##','¤ ','| ')) or re.findall(r'\[\w+\.?\d*\]',a[k])!=re.findall(r'\[\w+\.?\d*\]',b[k])]
    print(f, 'orig', len(a), 'trad', len(b), 'divergências até o fim da tradução:', bad[:5])
PY
