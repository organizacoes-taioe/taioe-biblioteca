# Carta de São Clemente aos Coríntios: texto grego

Base: Kirsopp Lake, *The Apostolic Fathers*, vol. 1 (Loeb, 1912), p. 8–121, na digitalização do
First1KGreek (`tlg1271.tlg001.1st1K-grc1.xml`, CC BY-SA 4.0; baixado em 2026-11-16).

Como foi montado: do XML saíram as notas e as referências bíblicas de margem (`note`, `bibl`), um
versículo por linha (`fonte-versiculos.txt`, já com δἰ → δι’, παῤ → παρ’, a coronis final → ’ e os
dois-pontos → ponto alto); `python3 montar.py fonte-versiculos.txt correcoes.tsv` aplica as correções
e grava os doze arquivos: a saudação sem número, depois um parágrafo por capítulo, com os versículos
`[c.v]`; a subscrição («Ἐπιστολὴ τῶν Ῥωμαίων πρὸς τοὺς Κορινθίους») num parágrafo à parte, no fim.

Erros de digitalização corrigidos: os 91 de `correcoes.tsv` (referência, errado, certo, se o
fac-símile confirma, observação). 82 foram confirmados no OCR do fac-símile do Internet Archive
(`apostolicfathers01lake`, reimpressão de 1919); nos outros 9 o OCR não distingue e a correção é de
acentuação evidente. São só erros de digitação (espírito e acento trocados, Λ por Α, palavras coladas
ou partidas, ponto no lugar de vírgula no meio do período, o artigo de 32.4, que tinha virado «??»).

Mantido como Lake imprime (lições de manuscrito, iguais no fac-símile): διὰ ζῆλος (4.8 etc.), τοῦ
ζήλους (63.2), τῶν μιαρὸν (45.4), εὐαριστείτω (41.1), πανπληθῆ (20.4), τοῦ τοῦ Ναυὴ (12.2), ἥδε
(12.4), as reticências da lacuna em 59.3. Por conferir no impresso: 37.3 ἑκατόνταρχαι (o OCR lê
ἑκατόναρχαι) e o acento de 45.1 ἔστε (Lake traduz como indicativo, «sois», e dá o imperativo em nota).
