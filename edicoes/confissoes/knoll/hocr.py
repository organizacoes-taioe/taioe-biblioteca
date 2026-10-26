"""lê um hOCR do Internet Archive: páginas -> linhas (bbox, x_size, palavras com bbox)"""
import re, html
def paginas(arq):
    s = open(arq, encoding='utf-8').read()
    for pm in re.finditer(r'<div class="ocr_page"[^>]*title="([^"]*)"[^>]*>(.*?)(?=<div class="ocr_page"|\Z)', s, re.S):
        tit, corpo = pm.group(1), pm.group(2)
        num = re.search(r'ppageno (\d+)', tit)
        bb = re.search(r'bbox (\d+) (\d+) (\d+) (\d+)', tit)
        linhas = []
        for lm in re.finditer(r'<span class="ocr_line"[^>]*title="([^"]*)"[^>]*>(.*?)</span>\s*(?=<span class="ocr_line"|</p>|</div>)', corpo, re.S):
            lt = lm.group(1)
            b = tuple(map(int, re.search(r'bbox (\d+) (\d+) (\d+) (\d+)', lt).groups()))
            xs = re.search(r'x_size ([\d.]+)', lt); xf = re.search(r'x_fsize ([\d.]+)', lt)
            ws = []
            for wm in re.finditer(r'<span class="ocrx_word"[^>]*title="bbox (\d+) (\d+) (\d+) (\d+)[^"]*"[^>]*>(.*?)</span>', lm.group(2), re.S):
                t = html.unescape(re.sub(r'<[^>]+>', '', wm.group(5)))
                ws.append((t, tuple(map(int, wm.groups()[:4]))))
            linhas.append({'bbox': b, 'xs': float(xs.group(1)) if xs else 0, 'fs': float(xf.group(1)) if xf else 0, 'w': ws})
        yield (int(num.group(1)) if num else None), (tuple(map(int, bb.groups())) if bb else None), linhas
