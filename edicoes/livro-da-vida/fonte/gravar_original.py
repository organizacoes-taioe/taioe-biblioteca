"""Grava edicoes/livro-da-vida/original/NN.txt a partir de dl/bmc_corr.json e dl/titulos.json."""
import json, os, re, sys
S = json.load(open('dl/bmc_corr.json')); T = json.load(open('dl/titulos.json'))
DEST = sys.argv[1]
os.makedirs(DEST, exist_ok=True)
ROM = ['', 'PRIMERO'] + [None] * 40
def rom(n):
    v = [(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]; o = ''
    for a, b in v:
        while n >= a: o += b; n -= a
    return o
CAB = ('# edicao: Silverio de Santa Teresa, Obras de Santa Teresa de Jesús, t. I: Libro de la Vida (Burgos, El Monte Carmelo, 1915; Biblioteca Mística Carmelitana, 1); ver LEIAME.md\n'
       '# fonte: OCR do Internet Archive (BMC1ObrasDeSantaTeresaDeJessTomoILibroDeLaVida), corrigido com a BAE 53 de Vicente de la Fuente (1861/1877) e a edição Heitz\n'
       '# marcas: «[c.p]» = capítulo.parágrafo (os parágrafos da edição de 1915, numerados por nós)\n')
for s in S:
    pars = [p for p, _ in s['pars']]
    if s['id'] == 'prologo':
        nome, tit, cab = '00.txt', 'Prólogo', ['## La vida de la santa madre Teresa de Jesús y algunas de las mercedes que Dios le hizo, escritas por ella misma por mandado de su confesor, a quien lo envía y dirige, y dice ansí:', 'Jhs.']
        corpo = pars
    elif s['id'] == 'epilogo':
        nome, tit, cab = '41.txt', 'Epílogo', ['## Carta que la Santa escribió al padre García de Toledo, remitiéndole la Vida', 'Jhs.']
        corpo = pars
    else:
        n = s['id']; nome, tit = f'{n:02d}.txt', f'Capítulo {rom(n)}'
        cab = ['## ' + T[n - 1]]
        corpo = [f'[{n}.{k}] {p}' for k, p in enumerate(pars, 1)]
    with open(os.path.join(DEST, nome), 'w', encoding='utf-8') as f:
        f.write(f'# titulo: {tit}\n' + CAB + '\n' + '\n\n'.join(cab + corpo) + '\n')
print('ok', len(S))
