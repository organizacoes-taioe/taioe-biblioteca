# Macunaíma: o que falta (estado em 2026-11-02, rodada de pedidos)

Pronto: as fontes e o confronto em rascunho (`config.py`), a proposta de grafia (`CONVENCOES.md`),
`decisoes.py` e `notas.py` vazios. Nada publicado: sem `conteudo/`, autor, `obras.json` nem vocabulário.

## Achados que mudam o trabalho
1. **O Wikisource «Macunaíma (1928)» não é todo de 1928.** As páginas revisadas (nível 3/4: caps. I,
   XII–XVIII e epílogo, pp. 7–12 e 167–283 do índice) reproduzem o impresso (heroi, tambem, porêm,
   frexa, tribu). As do nível 1 (caps. II–XI, pp. 13–165, «Giro bot») trazem o texto de uma edição
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
- Base `b28`: o Wikisource revisado nos caps. I, XII–XVIII e epílogo; o OCR ABBYY do IA (`or182096`)
  nos caps. de `DO_OCR` (II–XI), posto na divisão do Wikisource por `ocr.estrutura_como`.
- `t28`: Tesseract (por, `--psm 6`, 300 dpi) das páginas do PDF do IA, também só nos caps. II–XI.
  Os .txt ficam em `ferramentas/cache/macunaima/tess/` (fora do git; 184 das 253 páginas, o
  bastante até o cap. XI). Para refazer: baixar `https://archive.org/download/or182096/or182096.pdf`,
  `pdftoppm -r 300 -gray -png` e o Tesseract de `~/.cache/tesseract-local/raiz` (ver
  `edicoes/sao-bernardo/tesseract.py`) com `-l por --psm 6`, um .txt por página, nomes em ordem.
- `ws`: o Wikisource inteiro (no voto dos caps. II–XI ele desempata palavra igual; nas formas de 1928
  os dois OCRs o vencem).
- Resultado: 19 partes, 1.308 parágrafos, ~45,8 mil palavras; 2.500 sítios por maioria e **549 sem
  maioria** (todos nos caps. II–XI), onde vale o ABBYY e quase sempre há lixo de OCR («ai'omava ° s»,
  «enchen — le», «M A G U N A í M A 77», «Por - isso»).

## Próximos passos
1. `rever(tr, md, sitios)` no config, como em São Bernardo/Insônia: nos 549 sem maioria, limpar os
   dois OCRs (cabeços «MARIO DE ANDRADE»/«MACUNAÍMA» com número, « - » de hífen, símbolos soltos) e,
   se um deles então coincidir com outro ou com o `ws` (descontados acentos), ficar com ele; se o `ws`
   for palavra do léxico a distância ≤ 2 de ambos e nenhum OCR for palavra, ficar com o `ws` **só se
   a diferença não for de grafia** (x/ch, s/ç/ss, u/o, e/i, l/r: aí vale o OCR). O resto vai para a
   conferência nas imagens (`conferencia.json`, como em Caetés).
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
