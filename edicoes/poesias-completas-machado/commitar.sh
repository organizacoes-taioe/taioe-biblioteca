#!/bin/bash
# Uso: bash edicoes/poesias-completas-machado/commitar.sh "mensagem" arquivo...   (na raiz da worktree)
# Várias conversas commitam nesta worktree ao mesmo tempo: espera o index.lock e tenta de novo.
msg="$1"; shift
for t in $(seq 1 30); do
  if git add -- "$@" 2>/dev/null && git commit -q -m "$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- "$@" 2>/tmp/commitar.$$; then
    for u in $(seq 1 10); do git push -q -u origin pedido-poesias-completas-machado 2>/dev/null && { echo "commit e push ok"; rm -f /tmp/commitar.$$; exit 0; }; sleep $((RANDOM % 5 + 2)); done
    echo "commit ok, push falhou (tente de novo depois)"; exit 0
  fi
  grep -q "nothing to commit\|nada a submeter\|no changes added" /tmp/commitar.$$ 2>/dev/null && { echo "nada a commitar"; rm -f /tmp/commitar.$$; exit 0; }
  sleep $((RANDOM % 4 + 1))
done
cat /tmp/commitar.$$; rm -f /tmp/commitar.$$; exit 1
