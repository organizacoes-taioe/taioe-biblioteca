"""Lê o djvu.xml do Internet Archive: páginas -> linhas -> palavras com coordenadas."""
import re, sys, html
def paginas(path, ate=None):
    txt = open(path, encoding='utf-8', errors='replace').read()
    objs = re.split(r'<OBJECT ', txt)[1:]
    out = []
    for i, o in enumerate(objs):
        if ate and i >= ate: break
        m = re.search(r'width="(\d+)" height="(\d+)"', o)
        W, H = (int(m.group(1)), int(m.group(2))) if m else (0, 0)
        linhas = []
        for ln in re.findall(r'<LINE>(.*?)</LINE>', o, re.S):
            ws = []
            for c, w in re.findall(r'<WORD coords="([^"]+)"[^>]*>(.*?)</WORD>', ln, re.S):
                x1, y2, x2, y1 = [int(v) for v in c.split(',')[:4]]
                ws.append((x1, y1, x2, y2, html.unescape(w.strip())))
            if ws: linhas.append(ws)
        out.append((W, H, linhas))
    return out
