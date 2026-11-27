"""Vida de D. Frei Bertolameu dos Mártires — OCR próprio (Tesseract) dos fac-símiles.

  python3 edicoes/vida-de-frei-bartolomeu/ocr.py bnp1619 [de [até]]   # 1619, exemplar da BNP (res-33-a), 2 colunas
  python3 edicoes/vida-de-frei-bartolomeu/ocr.py r1850v1 | r1853v2 | r1818v1 | ia1619

PASTA = /mnt/arquivos/claude-tmp/pedidos-2711b/vida-de-frei-bartolomeu (variável VIDA_PASTA), com os PDFs em
dl/<nome>.pdf. Grava tess-<nome>/<página do PDF>[a|b].tsv (a, b = colunas de 1619) e <n>.json (recorte).
Imagens: a camada de texto (máscara de 1 bit) que o próprio PDF traz (pdfimages), sem reamostrar.
No máximo 2 processos (regra de RAM da rodada).
"""
import json
import os
import subprocess
import sys
import tempfile
from multiprocessing import Pool

PASTA = os.environ.get('VIDA_PASTA', '/mnt/arquivos/claude-tmp/pedidos-2711b/vida-de-frei-bartolomeu')
RAIZ_T = os.path.expanduser('~/.cache/tesseract-local/raiz')


def ambiente():
    env = dict(os.environ, OMP_THREAD_LIMIT='1', LD_LIBRARY_PATH=os.path.join(RAIZ_T, 'usr/lib/x86_64-linux-gnu'),
               TESSDATA_PREFIX=os.path.join(RAIZ_T, 'usr/share/tesseract-ocr/5/tessdata'))
    return os.path.join(RAIZ_T, 'usr/bin/tesseract'), env


def imagem(nome, n, tmp):
    """A maior imagem de 1 bit da página (a máscara do texto na BNP; a página inteira nos do Google)."""
    subprocess.run(['pdfimages', '-f', str(n), '-l', str(n), '-png', os.path.join(PASTA, 'dl', nome + '.pdf'),
                    os.path.join(tmp, 'p')], check=True)
    from PIL import Image
    melhor = None
    for f in sorted(os.listdir(tmp)):
        im = Image.open(os.path.join(tmp, f))
        if melhor is None or (im.mode == '1', im.size[0] * im.size[1]) > (melhor.mode == '1', melhor.size[0] * melhor.size[1]):
            melhor = im
    im = melhor.convert('L')
    from PIL import ImageOps, ImageStat
    if ImageStat.Stat(im).mean[0] < 128:          # máscara invertida (fundo preto)
        im = ImageOps.invert(im)
    return im


def colunas(im):
    """Divide a página de 1619 nas duas colunas pelo vão central (perfil vertical do meio da página)."""
    from PIL import Image
    w, h = im.size
    corpo = im.crop((0, int(h * 0.08), w, int(h * 0.95)))
    faixa = corpo.resize((w // 2, 1), Image.BOX)          # média de cada coluna de pixels (255 = branco)
    perfil = [255 - v for v in faixa.get_flattened_data()]
    lo, hi = int(w * 0.38) // 2, int(w * 0.62) // 2
    jan = 8
    sm = [sum(perfil[i - jan:i + jan]) for i in range(lo, hi)]
    x = (lo + sm.index(min(sm))) * 2
    return [(0, 0, x + 8, h), (x - 8, 0, w, h)]


# páginas de 1619 a uma coluna (dedicatória): o OCR vai à página inteira
UMA_COLUNA = {'bnp1619': range(15, 18), 'ia1619': range(10, 13)}


def largura_inteira(im):
    """Página de 1619 com texto de margem a margem (documentos latinos, cabeços de livro): em quantas de dez
    faixas o vão do meio tem tinta. Três ou mais: o Tesseract lê a página inteira, achando ele as colunas."""
    from PIL import Image
    w, h = im.size
    tot = 0
    for k in range(10):
        y0 = int(h * (0.08 + 0.085 * k))
        faixa = im.crop((0, y0, w, int(y0 + h * 0.085))).resize((w // 4, 1), Image.BOX)
        p = [255 - v for v in faixa.get_flattened_data()]
        lo, hi = int(len(p) * 0.40), int(len(p) * 0.60)
        tot += min(sum(p[i - 2:i + 3]) for i in range(lo, hi)) > 40
    return tot >= 3


def uma(args):
    nome, n = args
    saida = os.path.join(PASTA, 'tess-' + nome)
    os.makedirs(saida, exist_ok=True)
    marca = os.path.join(saida, f'{n}.json')
    if os.path.exists(marca):
        return n
    exe, env = ambiente()
    with tempfile.TemporaryDirectory(dir=PASTA) as tmp:
        im = imagem(nome, n, tmp)
        psm = '4'
        if nome.endswith('1619') and n not in UMA_COLUNA.get(nome, ()):
            if largura_inteira(im):
                caixas, psm = [(0, 0, im.size[0], im.size[1])], '3'
            else:
                caixas = colunas(im)
        else:
            caixas = [(0, 0, im.size[0], im.size[1])]
        info = {'tamanho': im.size, 'caixas': caixas, 'psm': psm}
        for k, cx in enumerate(caixas):
            suf = 'ab'[k] if len(caixas) > 1 else ''
            png = os.path.join(tmp, f'c{k}.png')
            im.crop(cx).save(png)
            subprocess.run([exe, png, os.path.join(saida, f'{n}{suf}'), '-l', 'por', '--psm', psm, 'tsv'],
                           check=True, env=env, stderr=subprocess.DEVNULL)
    json.dump(info, open(marca, 'w'))
    return n


if __name__ == '__main__':
    nome = sys.argv[1]
    total = int(subprocess.run(['pdfinfo', os.path.join(PASTA, 'dl', nome + '.pdf')], capture_output=True, text=True)
                .stdout.split('Pages:')[1].split()[0])
    de = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    ate = int(sys.argv[3]) if len(sys.argv) > 3 else total
    with Pool(2) as p:
        for n in p.imap_unordered(uma, [(nome, n) for n in range(de, ate + 1)]):
            print(n, end=' ', flush=True)
    print()
