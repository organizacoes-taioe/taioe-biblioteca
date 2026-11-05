# Minha Formação: estado (2026-11-05)

**Pronto para publicar.** Texto estabelecido, `texto.py minha-formacao --publicar` feito
(`conteudo/joaquim-nabuco/minha-formacao.js`, linha no `index.html`), autor novo `joaquim-nabuco` em
`conteudo/autores.js` com `area: 'nao-ficcao'` (a obra cai na Não-ficção, gênero «Autobiografia», sem
comentários), vocabulário (`edicoes/vocabulario/minha-formacao.json`, 194 verbetes, `conferir` ok),
`revisao.json` (2 decisões; com a recomendação, nada muda). `gerar.mjs` e `conferir.mjs` sem erro.

Falta só o do principal: juntar a branch, gerar o site, PR, Catálogo `obras` no teste e na produção, merge,
`traducoes_revisao.py --revisao` (Catálogo `traducoes`), tirar o pedido de `sugestoes.json` (Catálogo
`sugestoes`). Notas gerais: na fila dos lotes, como os outros. Nenhuma regra de `_redirects`.

## Como foi feito (para refazer)
- Cache em `ferramentas/cache/minha-formacao/` (só no desktop; cópia em `~/.cache/claude-pedidos-0511/minha-formacao/bkp/`):
  `pg76030.txt` (Gutenberg 76030, transcrição humana de 1900 sobre o exemplar de Toronto), `ia_djvu.xml`
  (OCR ABBYY do Internet Archive, `minhaformao00nabuuoft`), `ia.pdf` (fac-símile de Toronto, para os recortes),
  `harvard.txt` (djvutxt página a página do DjVu do Commons, exemplar de Harvard/HathiTrust, `@@PAGINA n@@`;
  djvulibre em `~/.cache/djvu-local/raiz`), `ws/wikisource_paginas.json` (páginas do Wikisource: texto
  moderno posto por robô, ortografia de 1971, só serve de grafia), `ob1949.pdf/.txt` (Obras Completas 1949, BBM 4743).
- `python3 ferramentas/texto.py minha-formacao [--publicar]`. O voto (pg + ia + hv) só aponta pontos: o
  `config.rever` fica sempre com o Gutenberg, que é fiel a 1900 até nos erros; as correções conferidas no
  fac-símile vão em `decisoes.EMENDAS` ('ocr': erro do Gutenberg; 'erro': erro de 1900, vai à «Sobre»);
  erro de 1900 que o Gutenberg corrigiu calado vai em `notas.ERROS_ANTERIORES` («das costumes»).
- Grafia (`config.modernizar`): Wikisource primeiro; onde falta, Obras de 1949 pelo léxico (`grafia1990` de
  São Bernardo), só palavra inteira; crase sempre a de 1900 (á → à; a fica a); trechos em francês/inglês
  protegidos (`estrangeiro`); junções falsas recusadas («dainfância»); romanos intactos. `decisoes.MANUAL`
  corrige o que o Wikisource estropia (nomes estrangeiros, «Fransisco», «Gambeta», «Witehall»…).
- Notas do autor: fora do fluxo (`_sem_rodape` tira o rodapé dos OCRs), em `notas-autor.txt` na grafia de
  hoje; `arrumar` as põe no fim do capítulo com a chamada [1], repõe os separadores `* * *` e arruma o quadro
  do «Caminho de ferro subterrâneo» (cap. XXI).
- Conferência: `ferramentas/` desta pasta (`recorte.py saida.png 'trecho' …` recorta o fac-símile de Toronto
  pelas palavras do OCR do IA; `ver.py` mostra as linhas dos dois OCRs; `lexcheck.py` lista as palavras do
  texto pronto fora do léxico; `filtro_modernas.py` e `triagem.py` filtram os relatórios). Caminhos absolutos
  deste PC no topo de cada um.

## Deixado como está (de propósito)
- «bailada», «cravado» (nas pendências), «inda», «conservatismo», «voadura», «menagem»; «Lords», «club(s)» e
  as citações estrangeiras como em 1900.
- A nota do cap. XX (chamada no título em 1900) vai sem chamada no texto.
- Pontuação: a do Gutenberg; o `pontuacao.tsv` (137 pontos em que as modernas concordam contra ela) não foi
  revisto um a um: as modernas mudam a pontuação de 1900.
