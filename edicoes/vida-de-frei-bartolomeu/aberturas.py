"""Vida de D. Frei Bartolomeu dos Mártires — recortes do começo de cada capítulo (título e primeiras linhas, onde
o OCR erra a capitular e o itálico), para a conferência nas imagens de 1619.

  python3 -I edicoes/vida-de-frei-bartolomeu/aberturas.py <pasta-de-saída>

Grava <saída>/lL-cNN.png e lista.tsv (livro, capítulo, título da Taboada, título e começo como estão).
"""
import json
import os
import sys

from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import montar as M  # noqa: E402
import testemunhos as T  # noqa: E402


def main():
    saida = sys.argv[1]
    os.makedirs(saida, exist_ok=True)
    ref = json.load(open(os.path.join(T.PASTA, 'colacao', 'bnp.json')))['palavras']
    fl = M.fluxo([])
    caps, _ = M.capitulos(fl)
    linhas = []
    for c in caps:
        ini = c['ini'] if c['ini'] is not None else c['s']
        ids = sorted({fl[k]['i'] for k in range(max(0, ini - 3), min(len(fl), c['e'] + 40))})
        grupos = {}
        for i in ids:
            w = ref[i]
            grupos.setdefault((w['p'], w.get('c', '')), []).append(w)
        recs = []
        for (p, col), ws in sorted(grupos.items(), key=lambda g: (g[0][0], g[0][1])):
            if len(ws) < 3:
                continue
            im = Image.open(os.path.join(T.PASTA, 'pag', f'{p}.png')).convert('L')
            x0 = min(w['x0'] for w in ws) - 60
            x1 = max(w['x1'] for w in ws) + 40
            y0 = min(w['y0'] for w in ws) - 120
            y1 = max(w['y1'] for w in ws) + 30
            recs.append(im.crop((max(0, x0), max(0, y0), min(im.size[0], x1), min(im.size[1], y1))))
        if not recs:
            continue
        L = max(r.size[0] for r in recs)
        A = sum(r.size[1] + 20 for r in recs)
        fol = Image.new('L', (L, A), 255)
        y = 0
        for r in recs:
            fol.paste(r, (0, y))
            y += r.size[1] + 20
        if fol.size[1] > 2400:
            fol = fol.resize((fol.size[0] * 2400 // fol.size[1], 2400))
        nome = f"l{c['livro']}-c{c['cap']:02d}"
        fol.save(os.path.join(saida, nome + '.png'))
        tit = ' '.join(fl[k]['t'] for k in range(c['s'], c['e'] + 1)) if c['s'] is not None else ''
        com = ' '.join(w['t'] for w in c['corpo'][:25])
        linhas.append('\t'.join([str(c['livro']), str(c['cap']), nome, c['titulo'], tit, com]))
    open(os.path.join(saida, 'lista.tsv'), 'w', encoding='utf-8').write(
        'livro\tcap\timagem\ttitulo_taboada\ttitulo_ocr\tcomeco_ocr\n' + '\n'.join(linhas) + '\n')
    print(len(linhas), 'capítulos')


if __name__ == '__main__':
    main()
