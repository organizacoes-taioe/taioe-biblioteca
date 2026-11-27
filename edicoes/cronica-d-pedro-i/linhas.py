"""Crónica de D. Pedro I — passo 1: as linhas de cada página do hOCR do Internet Archive.

    python3 -I edicoes/cronica-d-pedro-i/linhas.py <arquivo.hocr> <saida.tsv>

Grava uma linha por linha de OCR: página, y0, y1, x0, x1, x_size, texto. O hOCR fica fora do git
(em /mnt/arquivos/claude-tmp/…); o .tsv também.
"""
import html
import re
import sys

PAG = re.compile(r'<div class="ocr_page"[^>]*title="[^"]*ppageno (\d+)')
LIN = re.compile(r'<span class="ocr_line"[^>]*title="bbox (\d+) (\d+) (\d+) (\d+); x_size ([\d.]+)[^"]*"[^>]*>(.*?)</span>\s*</span>', re.S)
PAL = re.compile(r'<span class="ocrx_word"[^>]*>(.*?)</span>', re.S)


def main(entrada, saida):
    h = open(entrada, encoding='utf-8').read()
    cortes = [(m.start(), int(m.group(1))) for m in PAG.finditer(h)] + [(len(h), -1)]
    with open(saida, 'w', encoding='utf-8') as f:
        for (ini, p), (fim, _) in zip(cortes, cortes[1:]):
            for m in LIN.finditer(h, ini, fim):
                x0, y0, x1, y1, xs, corpo = m.groups()
                txt = ' '.join(html.unescape(re.sub('<[^>]+>', '', w)).strip() for w in PAL.findall(corpo + '</span>'))
                txt = re.sub(r'\s+', ' ', txt).strip()
                if txt:
                    f.write(f'{p}\t{y0}\t{y1}\t{x0}\t{x1}\t{float(xs):.0f}\t{txt}\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
