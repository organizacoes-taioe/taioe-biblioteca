#!/bin/bash
cd ~/.cache/claude-pedidos-0511/vida-de-santo-agostinho
while IFS=$'\t' read -r f u; do
  [ -s "$f" ] && file "$f" | grep -q JPEG && continue
  for t in 1 2 3 4; do
    c=$(curl -s -L -m 60 -A "TaioeBiblioteca/1.0" -o "$f" -w '%{http_code}' "$u"); [ "$c" = 200 ] && break; sleep 3
  done
  echo "$f $c"
done < conf/urls.tsv
