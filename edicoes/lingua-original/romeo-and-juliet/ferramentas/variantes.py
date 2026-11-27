"""As variantes («chave#2»…) do glossário que nenhuma ocorrência aponta (criadas e esquecidas).
python3 edicoes/lingua-original/romeo-and-juliet/ferramentas/variantes.py"""
import os, sys
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import lingua_original as L
g = L.ler_glossario('romeo-and-juliet')
usadas = set(g.get('ocorrencias', {}).values())
soltas = [k for k in g['verbetes'] if '#' in k and k not in usadas]
print('\n'.join(soltas) if soltas else 'nenhuma variante solta')
