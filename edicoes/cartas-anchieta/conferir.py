"""Cartas de Anchieta — pranchas para a conferência nas imagens das linhas duvidosas do rascunho.

  python3 edicoes/cartas-anchieta/conferir.py [PASTA]

Lê rascunho/<folha>.txt e rascunho/<folha>.json (a caixa de cada linha na imagem endireitada png/<folha>.png),
escolhe as linhas com dúvida (⟦…⟧ ou ⟨…⟩ do voto, palavra fora do léxico, número solto) e grava em PASTA/pranchas/
NNN.png (até 10 linhas recortadas, numeradas, com a de cima e a de baixo em cinza claro para o contexto) e
NNN.txt («k<TAB>folha<TAB>linha<TAB>texto atual»). A decisão de cada linha vai para conferencia.tsv
(folha, linha, texto corrigido), que o rascunho.py aplica.
"""
import json
import os
import re
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pecas  # noqa: E402

PASTA = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/.cache/claude-pedidos-0511/cartas-anchieta')
AQUI = os.path.dirname(os.path.abspath(__file__))
POR_PRANCHA = 10


def suspeitas(linha, lex_ok):
    if '⟦' in linha or '⟨' in linha:
        return True
    for w in re.findall(r"[A-Za-zÀ-ÿ]+", linha):
        if not lex_ok(w):
            return True
    if re.search(r'\d', re.sub(r'\(\d{1,3}\)|\b1[5-9]\d\d\b', '', linha)):
        return True
    return False


def main(lex_ok):
    os.makedirs(os.path.join(PASTA, 'pranchas'), exist_ok=True)
    lista = []
    for f in pecas.folhas():
        linhas = open(os.path.join(PASTA, 'rascunho', f'{f}.txt'), encoding='utf-8').read().splitlines()
        caixas = json.load(open(os.path.join(PASTA, 'rascunho', f'{f}.json')))
        for k, l in enumerate(linhas):
            if suspeitas(l, lex_ok):
                lista.append((f, k, l, caixas[k]))
    n = 0
    for i in range(0, len(lista), POR_PRANCHA):
        grupo = lista[i:i + POR_PRANCHA]
        recortes = []
        for f, k, l, (x0, y0, x1, y1) in grupo:
            im = Image.open(os.path.join(PASTA, 'png', f'{f}.png'))
            r = im.crop((max(0, x0 - 30), max(0, y0 - 45), min(im.width, x1 + 30), min(im.height, y1 + 45)))
            recortes.append(r)
        larg = max(r.width for r in recortes) + 70
        alt = sum(r.height + 12 for r in recortes)
        pr = Image.new('L', (larg, alt), 255)
        d = ImageDraw.Draw(pr)
        y = 0
        txt = []
        for j, (r, (f, k, l, _)) in enumerate(zip(recortes, grupo), 1):
            pr.paste(r, (70, y))
            d.text((8, y + r.height // 2 - 8), str(j), fill=0)
            d.line((0, y + r.height + 6, larg, y + r.height + 6), fill=120)
            y += r.height + 12
            txt.append(f'{j}\t{f}\t{k}\t{l}')
        n += 1
        pr.save(os.path.join(PASTA, 'pranchas', f'{n:03d}.png'))
        open(os.path.join(PASTA, 'pranchas', f'{n:03d}.txt'), 'w', encoding='utf-8').write('\n'.join(txt) + '\n')
    print(len(lista), 'linhas em', n, 'pranchas')


if __name__ == '__main__':
    import lexico
    main(lexico.ok)
