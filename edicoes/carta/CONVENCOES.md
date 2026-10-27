# Carta de Pero Vaz de Caminha: convenções da edição

Carta a el-rei D. Manuel, Porto Seguro, 1º de maio de 1500. Pedido do Gere (fila de `/admin/pedidos/`,
26/10/2026): «Sem tradução: só a ortografia e notas». Não-ficção, no esquema das obras comentadas
(`ferramentas/comentadas.py`), sem comentários: o texto na grafia de hoje (`atualizado/`) com o
original de 1500 ao lado (`original/`), a folha do manuscrito no texto (`{fl. 1v}`) e notas.

## Fontes e texto original

- Manuscrito: ANTT, Gavetas, gav. 8, mç. 2, n.º 8 (PT/TT/GAV/8/2/8), 14 folhas (1r–14r; 14v é o
  sobrescrito). Fac-símile do ANTT no Commons (`File:PT-TT-GAV-8-2-8.pdf`, 28 imagens de ~1300 ×
  1800); o digitarq recusou acesso automático (404).
- Base: a Wikisource «Carta a El Rei D. Manuel (ortografia original)», uma página por folha, linha a
  linha (`Página:Carta-caminha-folioNNx.jpg`), todas em qualidade 1 (não revistas): erros de
  digitação e linhas puladas (fl. 5r «traues», 8r «quis mais tornar do Rio pera aquem», 10r «quãto
  tijnham o bico bramco e os Rabos curtos», 13r «teerã», «aquy porque de manhaã prazendo a deos
  fazemos»).
- Conferência: o texto diplomático da _Revista de História_ (USP, v. 36, n. 73, 1968, «O
  descobrimento do Brasil através dos textos»), lido por OCR (com erros próprios: c/e/o, «trra»).
  Comparação automática pelas letras; umas 75 correções na base, conferidas uma a uma, e no
  fac-símile as duvidosas (fl. 1v, os números das sondagens; 13v «parma»; 14r «dosoiro»). As outras
  diferenças entre os dois são de grafia, de abreviatura ou erro do OCR da USP.
- Lições que ficaram contra a USP: «toruauam» (9v, «torvavam»), «lacam» (10v, lacão), «a que chamã»
  (3v). Lição da USP contra a base: «lançarãnas todas» (12v), «procuraua» (3r), «tornamos eles
  foramsse» (4v), os números de 1v («xbij xbj xb xiiij xiij xij x e ix braças», «aas x oras», «obra
  de bij ou biij»: a Wikisource misturava algarismos riscados).
- Linhas juntadas por folha; palavra partida no fim da linha, decidida pela USP. Palavra partida
  entre duas folhas vai inteira para a folha seguinte (7v «cousas», 10r «maneira», 10v «mãcebos»,
  11r «avezarem», 11v «crunho»). Abreviaturas com letra sobrescrita em caracteres sobrescritos
  (segº, Sᵒʳ, ijᶜ); «+» (12r) é a cruz, como no manuscrito. A pontuação do original é a da
  transcrição.

## Divisão

Nove partes, pelos dias que a carta narra, com títulos nossos: 1 De Lisboa à Terra de Vera Cruz
(9/3–23/4, fl. 1r–2r); 2 Porto Seguro e os dois homens a bordo (24/4); 3 Sábado: os primeiros em
terra (25/4); 4 Domingo de Pascoela: a primeira missa (26/4); 5 O conselho dos capitães e a tarde no
rio (26/4); 6 Segunda e terça: a aldeia e a cruz (27–28/4); 7 Quarta e quinta: os hóspedes
(29–30/4); 8 Sexta-feira, 1º de maio: a cruz e a missa; 9 A terra e o fim da carta. Parágrafos
nossos (o manuscrito só tem barras e pontos), os mesmos nos dois lados.

## Texto atualizado

- As palavras e a ordem de Caminha; só a grafia muda (Acordo de 1990, forma brasileira): pera →
  para, cousa → coisa, nom/nõ → não, polo → pelo, per → por, huũ → um, mui(to) → muito, asy →
  assim, homeẽs → homens, naaos → naus, frecha → flecha, fremoso → formoso, todo → tudo
  (pronome), coma → como, giolho → joelho, enxadrez → xadrez, degradado → degredado.
- Forma antiga de verbo na forma atual: poder → puder (futuro do subjuntivo), jouuemos → jazemos,
  beberam → beberão e ficaram → ficarão quando são futuro, podemos → pudemos no pretérito.
- Ficam, com nota quando atrapalham a leitura: pero, ca, obra de, senhos, al, quejando, malaves,
  aljaveira, apressão, encarna, abasta, soía, a carão de, homem (sem artigo: «a gente»), compridão,
  berberia, sobrepente, coto, mostrança, abastaria. A mesóclise de Caminha fica (ver-se-ia,
  imprimir-se-á, dar-se-á); o `comentadas.py` não a varre no texto do autor, só nas notas.
- Nomes na forma de hoje: Pedro Álvares Cabral (nunca nomeado), Nicolau Coelho, Bartolomeu Dias,
  Diogo Dias, Afonso Lopes, Afonso Ribeiro, Sancho de Tovar, Simão de Miranda, Aires Correia, Aires
  Gomes, Vasco de Ataíde, Pero Escobar, frei Henrique, João Telo, Jorge de Osório. Belém, Grã-Canária,
  São Nicolau, Monte Pascoal, Terra da Vera Cruz, Porto Seguro, Calecute, São Tomé, entre Douro e
  Minho.
- Números romanos por extenso; o ano da data final em algarismos. «.s.» = «a saber».
- Pontuação sóbria; os botões são «Original (1500)» e «Grafia atual» (`rotulos` no `obra.json`).

## Notas

50, pelas lições da Bíblia (`taioe-biblia/revisao/aprendizado.md`): pessoas, lugares, costumes,
liturgia e as palavras que caíram de uso ou mudaram de sentido; nada de interpretação. Todas sem
`revista`: só aparecem no site depois que o Gere as aprovar em `/admin/pendencias/` (tipo
«Não-ficção: tradução», pelo `comentadas.py --revisao`). As 8 decisões de leitura e de grafia
estão em `revisao.json` (tipo «Biblioteca: traduções», pelo `traducoes_revisao.py`); o texto no ar
segue a recomendação de cada uma.
