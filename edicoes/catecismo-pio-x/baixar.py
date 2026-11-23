"""Baixa do it.wikisource as páginas transcritas do Compendio della dottrina cristiana (Roma, 1905), as do
Catechismo maggiore (djvu 80-329, com folga), com o nível de revisão de cada uma.

    python3 edicoes/catecismo-pio-x/baixar.py <pasta>      → <pasta>/pag/NNN.json ({n, q, t})

Depois: python3 edicoes/catecismo-pio-x/montar.py <pasta>. A pasta fica fora do repositório
(ex.: ~/.cache/claude-pedidos-2311/tmp-catecismo-pio-x).
"""
import json
import os
import sys
import urllib.parse
import urllib.request

API = 'https://it.wikisource.org/w/api.php'
INDICE = 'Compendio della dottrina cristiana, Roma, 1905.djvu'

if __name__ == '__main__':
    destino = os.path.join(sys.argv[1], 'pag')
    os.makedirs(destino, exist_ok=True)
    for a in range(80, 330, 50):
        titulos = '|'.join(f'Pagina:{INDICE}/{n}' for n in range(a, a + 50))
        q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions|proofread', 'rvprop': 'content',
                                    'rvslots': 'main', 'format': 'json', 'titles': titulos, 'formatversion': '2'})
        req = urllib.request.Request(API, data=q.encode(), headers={'User-Agent': 'biblioteca-taioe/1.0'})
        d = json.load(urllib.request.urlopen(req, timeout=60))
        for p in d['query']['pages']:
            if p.get('missing'):
                continue
            n = int(p['title'].rsplit('/', 1)[1])
            with open(os.path.join(destino, f'{n:03d}.json'), 'w', encoding='utf-8') as f:
                json.dump({'n': n, 'q': p.get('proofread', {}).get('quality'),
                           't': p['revisions'][0]['slots']['main']['content']}, f, ensure_ascii=False)
    print(len(os.listdir(destino)), 'páginas em', destino)
