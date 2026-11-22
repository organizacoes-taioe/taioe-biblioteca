"""Representação sobre a escravatura: grava conteudo/jose-bonifacio/representacao-sobre-a-escravatura.js
(chamado por montar.py --publicar). Quatro partes; as notas do impresso vão no fim de cada parte."""
import json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
SAIDA = os.path.join(RAIZ, 'conteudo', 'jose-bonifacio', 'representacao-sobre-a-escravatura.js')

APRESENTACAO = """**Texto-base.** Esta edição reproduz a primeira edição da _Representação à Assembleia Geral Constituinte e Legislativa do Império do Brasil sobre a escravatura_, impressa em Paris, na tipografia de Firmin Didot, em 1825. José Bonifácio a escreveu em 1823 para a Constituinte, que foi dissolvida em 12 de novembro daquele ano, antes de recebê-la; o autor foi preso e deportado. Uma cópia ficou com quem a guardava, e o editor, que assina A. D., a publicou sem poder consultá-lo, com uma advertência datada de 4 de outubro de 1825. São dele a advertência e as duas notas de rodapé assinadas A. D.

**Como foi estabelecido.** O ponto de partida foi a transcrição do Wikisource, conferida página por página nas imagens do exemplar do Internet Archive, com as leituras por OCR de dois exemplares de 1825 para apontar as divergências. A conferência fez 31 correções à transcrição; os erros do próprio impresso estão listados abaixo.

**Divisão.** O impresso corre sem partes numeradas: a advertência, a representação, os 32 artigos do projeto de lei e o fecho, que segue o último artigo sem título. A divisão em quatro partes e o título «Conclusão» são nossos.

**Grafia.** Ortografia de hoje (Acordo de 1990, forma brasileira), com as palavras e a ordem do impresso: hum → um, he → é, commercio → comércio, Deos → Deus, assucar → açúcar, cativão → cativam. As formas em -ão do passado passam a -am (levantárão → levantaram, nascêrão → nasceram), e as do futuro ficam (serão, tornarão). A crase segue o uso de hoje (á favor → a favor). As maiúsculas do autor ficam (Nação, Religião, Senhores), e também «pela mor parte». As citações em francês de M. de Pradt ficam como no impresso. Os números e as frações do Art. IV são os de 1825."""

ERROS = [
    ('Advertência', 'nenuma', 'nenhuma'),
    ('Representação', 'escrivadão', 'escravidão'),
    ('Representação', 'me empego', 'me emprego'),
    ('Representação, nota', 'nenuma', 'nenhuma'),
    ('Representação', 'En vou', 'Eu vou'),
    ('Artigos, art. IV', 'dois 3', 'dois 3.os'),
    ('Artigos, art. XVIII', 'servicos', 'serviços'),
    ('Artigos, art. XIX', 'proporcão', 'proporção'),
    ('Artigos, art. XIX', 'ficarâ', 'ficará'),
    ('Artigos, art. XXXII', 'summariameute', 'sumariamente'),
    ('Conclusão', 'da Razão e da Moral', 'da Razão e da Moral.'),
]
FONTES = [
    {'nome': 'Representação à Assembleia Geral Constituinte e Legislativa do Império do Brasil sobre a escravatura (Paris, 1825), exemplar do Internet Archive (fac-símile)',
     'url': 'https://archive.org/details/representaoassem00boni', 'nota': 'texto-base, conferido nas imagens'},
    {'nome': 'A mesma edição, outro exemplar (Internet Archive)', 'url': 'https://archive.org/details/DELTA53975FA', 'nota': 'segunda leitura do OCR'},
    {'nome': 'Wikisource em português, transcrição da edição de 1825',
     'url': 'https://pt.wikisource.org/wiki/Representa%C3%A7%C3%A3o_de_Jos%C3%A9_Bonif%C3%A1cio_sobre_a_escravatura', 'nota': 'ponto de partida da transcrição'},
]

def js_texto(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

def gravar(mb, mn):
    i_adv = mb.index('Advertência.'); i_rep = mb.index('Representação.')
    i_art = mb.index('**Art. I.**'); i_fim = next(i for i, x in enumerate(mb) if x.startswith('Eis aqui tendes'))
    cortes = [('Advertência', mb[i_adv + 1:i_rep]), ('Representação', mb[i_rep + 1:i_art]), ('Artigos', mb[i_art:i_fim]), ('Conclusão', mb[i_fim:])]
    blocos = []
    usadas = 0
    for k, (titulo, ps) in enumerate(cortes):
        mapa = {}
        def chama(m):
            g = int(m.group(1))
            mapa.setdefault(g, len(mapa) + 1)
            return f'[{mapa[g]}]'
        ps = [re.sub(r'\[(\d+)\]', chama, p) for p in ps]
        notas = [f'¤ [{v}] {mn[g - 1]}' for g, v in mapa.items()]
        usadas += len(notas)
        blocos.append({'n': str(k + 1), 'titulo': titulo, 'texto': '\n\n'.join(ps + notas)})
    if usadas != len(mn):
        raise SystemExit(f'notas: {usadas} usadas de {len(mn)}')
    edicao = {'base': '1825', 'apresentacao': APRESENTACAO,
              'secoes': {'erros': {'titulo': 'Erros do impresso de 1825 corrigidos', 'explica': 'Grafia de 1825 na primeira coluna.', 'de': '1825', 'para': 'Corrigido'}},
              'erros': [{'cap': c, 'de': d, 'para': p} for c, d, p in ERROS], 'fontes': FONTES}
    meta = {'id': 'representacao-sobre-a-escravatura', 'autor': 'jose-bonifacio', 'titulo': 'Representação sobre a escravatura', 'ano': 1823, 'genero': 'Política',
            'divisao': {'singular': 'parte', 'plural': 'partes', 'rotulo': 'nome', 'marcas': False},
            'descricao': 'A representação preparada para a Assembleia Constituinte de 1823, pelo fim do tráfico e pela emancipação gradual dos escravos, com um projeto de lei em 32 artigos.'}
    L = ['/* Representação sobre a escravatura — José Bonifácio', '   Gerado por edicoes/representacao-escravatura/montar.py --publicar a partir de 1825/.',
         '   Não edite à mão: corrija as decisões e rode de novo. */', 'BIBLIOTECA.obra({']
    L += [f'  {c}: {json.dumps(v, ensure_ascii=False)},' for c, v in meta.items()]
    L.append('  edicao: ' + json.dumps(edicao, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ',')
    L.append('  partes: [')
    for i, b in enumerate(blocos):
        L.append(f'    {{ n: {json.dumps(b["n"])}, titulo: {json.dumps(b["titulo"], ensure_ascii=False)}, texto: `{js_texto(b["texto"])}` }}' + (',' if i + 1 < len(blocos) else ''))
    L += ['  ]', '});']
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('gravado', os.path.relpath(SAIDA, RAIZ), [(b['titulo'], len(b['texto'].split())) for b in blocos])
    idx = os.path.join(RAIZ, 'index.html'); h = open(idx, encoding='utf-8').read()
    linha = '<script defer src="conteudo/jose-bonifacio/representacao-sobre-a-escravatura.js"></script>'
    if linha not in h:
        open(idx, 'w', encoding='utf-8').write(h.replace('</head>', linha + '\n</head>', 1))
