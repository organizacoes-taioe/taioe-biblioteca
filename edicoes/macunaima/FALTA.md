# Macunaíma: o que falta (estado em 2026-11-02, rodada de pedidos)

Pronto: as fontes e o confronto em rascunho (`config.py`), a proposta de grafia (`CONVENCOES.md`),
`decisoes.py` e `notas.py` vazios. Nada publicado: sem `conteudo/`, autor, `obras.json` nem vocabulário.

## Achados que mudam o trabalho
1. **O Wikisource «Macunaíma (1928)» não é todo de 1928.** As páginas revisadas (nível 3/4: pp. 7–12
   e 167–283 do índice, caps. XII–XVIII e epílogo e o começo do I) reproduzem o impresso (heroi,
   tambem, porêm, frexa, tribu). As do nível 1 (pp. 13–165: fim do cap. I e caps. II–XI, «Giro bot»;
   no cap. I, «Toda a tribo» onde o impresso tem «tribu») trazem o texto de uma edição
   **posterior, revista e modernizada**: flecha por frexa, tribo por tribu, pôde por poude, para por
   pra, e passagens reescritas (cap. V: onde 1928 tem «jacús jacutingas», ela lista «mutuns,
   mutum-de-vargem mutum-de-fava mutuporanga urus urumutum»). Ali o Wikisource não vota como 1928.
2. **18 capítulos em 1928**, não 17: o XI de 1928 é «As tres Normalistas» (pp. 147–165); o XII é
   «A velha Ceiucí». Nas edições posteriores há 17 (Mário juntou ou cortou; a conferir).
3. O ABBYY do IA põe acentos que o impresso não tem (herói, também, ninguém); o Tesseract não.
4. Direitos: Mário morreu em 1945, domínio público no Brasil desde 2016. Nos EUA, a 1ª edição (1928)
   está em domínio público desde 2024 (95 anos); as revisões de 1937 estariam protegidas lá até o fim
   de 2032 (se restauradas pela URAA). Mais um motivo para a base de 1928. O item de `sugestoes.json`
   não tem `aviso`.

## Como está o confronto (`python3 ferramentas/texto.py macunaima --rebaixar`)
- Base `b28`: o Wikisource revisado nos caps. XII–XVIII e epílogo; o OCR ABBYY do IA (`or182096`)
  nos caps. de `DO_OCR` (I–XI), posto na divisão do Wikisource por `ocr.estrutura_como`.
- `t28`: Tesseract (por, `--psm 6`, 300 dpi) das páginas do PDF do IA, também só nos caps. I–XI.
  Os .txt ficam em `ferramentas/cache/macunaima/tess/` (fora do git; 184 das 253 páginas, o
  bastante até o cap. XI). Para refazer: baixar `https://archive.org/download/or182096/or182096.pdf`,
  `pdftoppm -r 300 -gray -png` e o Tesseract de `~/.cache/tesseract-local/raiz` (ver
  `edicoes/sao-bernardo/tesseract.py`) com `-l por --psm 6`, um .txt por página, nomes em ordem.
- `ws`: o Wikisource inteiro (no voto dos caps. I–XI ele desempata palavra igual; nas formas de 1928
  os dois OCRs o vencem).
- `rever()` (feito): nos sítios sem maioria limpa os dois OCRs e fica com o que só tem palavras
  conhecidas; se nenhum serve, com o `ws` quando ele difere pouco e **não** por grafia (frexa/flecha,
  genipapo/jenipapo ficam como no OCR). Conferido: nenhum «flecha», «tribo» ou «jenipapo» no texto.
- Resultado: 19 partes, 1.308 parágrafos, ~45 mil palavras; 2.629 sítios por maioria, 568 sem
  maioria, dos quais **364 a conferir no fac-símile** (`ferramentas/cache/macunaima/relatorios/duvidas.tsv`;
  ex.: «aromava s» por «aromava os»).

## Próximos passos
1. Conferir nas imagens as 364 dúvidas de `duvidas.tsv` e gravar as leituras (`conferencia.json` e
   `decisoes.corrigir`, como em Caetés). Também ler `sitios.tsv` por amostra: onde ABBYY e Tesseract
   concordam contra o `ws` ganha o OCR, inclusive em erro comum aos dois.
2. Conferir no fac-símile as formas de Mário que só o OCR atesta nos caps. II–XI, e o cap. I nas
   pp. 13–15 (nível 1 no Wikisource, mas na base: conferir se também está modernizado).
3. Hífen de fim de linha no OCR: hoje se junta sem hífen; compostos partidos na linha
   («mato-/virgem») perdem o hífen: conferir os casos pela lista de compostos do texto revisado.
4. `modernizar(E, manual)` pelas regras de `CONVENCOES.md` (só acento e diferencial; manter as
   formas de Mário), com o relatório `sem_par.tsv`. Pode partir de `edicoes/caetes/grafia1990.py`,
   **sem** o passo de esqueleto (que trocaria frexa por flecha, mãi por mãe).
5. Decidir com o Gere: 1928 inteiro com «As tres Normalistas» (recomendado: é o texto da edição-base,
   e a «Sobre» explica que o capítulo saiu depois) e as dúvidas de grafia de `CONVENCOES.md`.
6. `notas.py` («Sobre esta edição»), autor novo em `conteudo/autores.js` (`mario-de-andrade`,
   1893–1945), `obras.json`, link na página da Literatura, `--publicar`, `gerar.mjs` e `conferir.mjs`.
7. Vocabulário (`edicoes/vocabulario/macunaima.json`): muito tupi e afro-brasileiro (girau, paxiúba,
   cunhatã, piá, murúa, poracê, cachirí, macumba, Exu, Ogum…); só definição de fonte segura
   (Houaiss/Aulete, A. G. Cunha, Cascudo, Cavalcanti Proença, *Roteiro de Macunaíma*); conferir com
   `node ferramentas/vocabulario.mjs … conferir`.
