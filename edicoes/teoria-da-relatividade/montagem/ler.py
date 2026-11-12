"""Mostra os blocos i..j de um arquivo do original (sem o cabeçalho), numerados. Uso: ler.py arq i j"""
import sys
t = open(sys.argv[1], encoding='utf-8').read().split('\n\n')
bl = [b for b in t if b.strip() and not b.startswith('# ')]
i, j = int(sys.argv[2]), int(sys.argv[3])
print('total', len(bl))
for k in range(i, min(j + 1, len(bl))): print(f'[{k}]', bl[k]); print()
