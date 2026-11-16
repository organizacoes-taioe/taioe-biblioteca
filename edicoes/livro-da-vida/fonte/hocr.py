"""Lê o hOCR do Internet Archive em páginas e linhas: [(pagina, [(x0,y0,x1,y1,texto,par_id)])]."""
import re, html, sys, json
def ler(arq):
    pags = []; cur = None; par = None; line = None
    rx_page = re.compile(r'class="ocr_page" id="page_(\d+)"')
    rx_par = re.compile(r'class="ocr_par" id="(par_[\d_]+)"')
    rx_line = re.compile(r'class="ocr_(?:line|caption|textfloat|header)" title="bbox (\d+) (\d+) (\d+) (\d+)')
    rx_word = re.compile(r'class="ocrx_word"[^>]*title="bbox (\d+) (\d+) (\d+) (\d+)[^"]*">([^<]*)</span>')
    for l in open(arq, encoding='utf-8'):
        m = rx_page.search(l)
        if m:
            cur = [int(m.group(1)), []]; pags.append(cur); continue
        m = rx_par.search(l)
        if m: par = m.group(1); continue
        m = rx_line.search(l)
        if m:
            line = [*map(int, m.groups()), [], par]; cur[1].append(line); continue
        for m in rx_word.finditer(l):
            line[4].append(html.unescape(m.group(5)).strip())
    out = []
    for p, ls in pags:
        out.append((p, [(a, b, c, d, ' '.join(w for w in ws if w), par) for a, b, c, d, ws, par in ls]))
    return out
if __name__ == '__main__':
    pags = ler(sys.argv[1])
    json.dump(pags, open(sys.argv[2], 'w'), ensure_ascii=False)
    print(len(pags))
