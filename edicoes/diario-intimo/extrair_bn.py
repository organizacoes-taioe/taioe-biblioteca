"""Diário Íntimo (Lima Barreto): passa a transcrição da Fundação Biblioteca Nacional (2002), tal como a Biblioteca
Virtual Miguel de Cervantes a publica em HTML (três páginas, _2, _3, _4), a um texto em blocos, um por parágrafo.

Uso: python3 -I extrair_bn.py <pasta com p2.html p3.html p4.html> > bn2002.txt

Blocos (separados por linha em branco):
  #ANO 1900          título de ano (h2)
  ## texto           linha centrada (data, título) ou h3
  >> texto           linha alinhada à direita (assinatura, data no fim, aviso)
  * * *              separador entre notas
  ....               lacuna (linha de pontos)
  q: texto           parágrafo citado (blockquote)
  | verso            versos (um por linha; «|» sozinho separa estrofes)
  = texto            fonte de uma citação (div.cita)
  - texto            item de lista (mais «-» = mais fundo)
  t: a | b           linha de tabela
  texto              parágrafo
Itálico entre _sublinhados_."""
import html, re, sys
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocos = []      # (tipo, texto)
        self.pilha = []       # (tag, classe)
        self.buf = None       # (tipo, [pedaços])
        self.em = 0
        self.dentro = False   # dentro do div#obra, depois do título
        self.quote = 0
        self.lista = 0
        self.linha_tab = None
        self.ignorar = 0

    def abre(self, tipo):
        self.fecha()
        self.buf = (tipo, [])

    def fecha(self):
        if self.buf:
            tipo, ps = self.buf
            t = ''.join(ps)
            t = re.sub(r'[ \t\r\n]+', ' ', t).strip()
            t = t.replace('\x00', '\n')
            t = re.sub(r' *\n *', '\n', t).strip()
            if t:
                self.blocos.append((tipo, t))
        self.buf = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '') or ''
        self.pilha.append((tag, cls))
        if tag == 'h1' and 'tit' in cls:
            self.dentro = True
            self.ignorar += 1
            return
        if not self.dentro:
            return
        if tag in ('ul',) and 'saltos' in cls:
            self.ignorar += 1
            return
        if tag == 'small' or (tag == 'span' and 'glyphicon' in cls):
            self.ignorar += 1
            return
        if self.ignorar:
            return
        if tag == 'h2':
            self.abre('ANO')
        elif tag == 'h3':
            self.abre('##')
        elif tag == 'blockquote':
            self.quote += 1
        elif tag == 'p':
            if 'centrado' in cls:
                self.abre('##')
            elif 'derecha' in cls:
                self.abre('>>')
            elif any(t == 'div' and 'cita' in c for t, c in self.pilha[:-1]):
                self.abre('=')
            elif self.quote:
                self.abre('q:')
            else:
                self.abre('')
        elif tag == 'div' and cls == 'verso':
            self.abre('|')
        elif tag == 'div' and cls == 'poema':
            if self.blocos and self.blocos[-1][0] == '|':
                self.blocos.append(('|', ''))
        elif tag == 'ul':
            self.lista += 1
        elif tag == 'li':
            self.abre('-' * self.lista)
        elif tag == 'tr':
            self.fecha()
            self.linha_tab = []
        elif tag == 'td':
            self.linha_tab.append('')
        elif tag == 'em':
            if self.buf:
                self.buf[1].append('_')
            self.em += 1
        elif tag == 'br':
            if self.buf and self.buf[0] not in ('|',):
                self.buf[1].append('\x00')

    def handle_endtag(self, tag):
        while self.pilha:
            t, cls = self.pilha.pop()
            if t == tag:
                break
        else:
            return
        if tag == 'h1' and 'tit' in cls:
            self.ignorar -= 1
            return
        if tag == 'ul' and 'saltos' in cls or tag == 'small' or (tag == 'span' and 'glyphicon' in cls):
            self.ignorar = max(0, self.ignorar - 1)
            return
        if not self.dentro or self.ignorar:
            return
        if tag in ('h2', 'h3', 'p', 'li') or (tag == 'div' and cls == 'verso'):
            self.fecha()
        elif tag == 'blockquote':
            self.fecha()
            self.quote -= 1
        elif tag == 'ul':
            self.fecha()
            self.lista -= 1
        elif tag == 'tr':
            cel = [re.sub(r'\s+', ' ', c).strip() for c in self.linha_tab]
            self.blocos.append(('t:', ' | '.join(cel)))
            self.linha_tab = None
        elif tag == 'em':
            self.em -= 1
            if self.buf:
                self.buf[1].append('_')
        elif tag == 'div' and cls == 'fragmento':
            self.fecha()

    def handle_data(self, d):
        if not self.dentro or self.ignorar:
            return
        if self.linha_tab is not None:
            self.linha_tab[-1] += d
        elif self.buf:
            self.buf[1].append(d)
        elif d.strip():
            self.abre('')
            self.buf[1].append(d)

def limpa(t):
    t = re.sub(r'_(\s*)_', r'\1', t)              # itálico vazio ou colado
    t = re.sub(r'_\s+', lambda m: ' _' if False else m.group(0), t)
    t = re.sub(r'(^|[\s(«"\'—])_\s+', r'\1_', t)
    t = re.sub(r'\s+_([\s.,;:!?»)]|$)', r'_\1', t)
    return t

def main(pasta):
    saida = []
    for n in (2, 3, 4):
        p = P()
        p.dentro = n != 2
        s = open(f'{pasta}/p{n}.html', encoding='utf-8', errors='replace').read()
        i = s.find('<div id="obra"')
        s = s[i:s.find('One fine body', i)]
        s = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
        p.feed(s)
        p.fecha()
        for tipo, t in p.blocos:
            if t.startswith('Biblioteca Virtual Miguel de Cervantes') or t in ('Nota', '×'):
                continue
            saida.append((tipo, limpa(t)))
    linhas = []
    for tipo, t in saida:
        if tipo == 'ANO':
            linhas.append('#ANO ' + t)
        elif tipo == '|':
            if linhas and linhas[-1].startswith('|'):
                linhas[-1] += '\n| ' + t if t else '\n|'
            else:
                linhas.append('| ' + t)
        elif tipo == 't:':
            if linhas and linhas[-1].startswith('t:'):
                linhas[-1] += '\nt: ' + t
            else:
                linhas.append('t: ' + t)
        elif tipo == '##' and re.fullmatch(r'\*[ *]*', t):
            linhas.append('* * *')
        elif tipo == '##' and re.fullmatch(r'\.{4,}', t):
            linhas.append('....')
        elif tipo == '':
            linhas.append(t)
        else:
            linhas.append(tipo + ' ' + t)
    print('\n\n'.join(linhas))

if __name__ == '__main__':
    main(sys.argv[1])
