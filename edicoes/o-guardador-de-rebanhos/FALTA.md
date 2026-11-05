# O Guardador de Rebanhos (Alberto Caeiro): o que está feito e o que falta

## Feito (2026-11-05)
- Obra `o-guardador-de-rebanhos` (Literatura, autor `fernando-pessoa`, seção «Livros» da página do autor), os 49
  poemas, 1.019 versos, 7.331 palavras; montada por `montar.py` (`conteudo/fernando-pessoa/o-guardador-de-rebanhos.js`)
  a partir de `texto/NN.txt` (um arquivo por poema, na grafia de hoje mas com «cousa», que o `montar.py` troca por
  «coisa»; o «porque» das 3 perguntas diretas sai «por que»). O corpus do Versificador não foi tocado.
  Cada poema é uma parte sem título, `n` = número romano (endereços `/o-guardador-de-rebanhos/i/` … `/xlix/`).
- Edição: os 23 poemas da *Athena* n.º 4 (jan. 1925; fac-símile do Commons, `File:Athena, 4.pdf`, pp. 145–156 = pp.
  23–34 do PDF) seguem a revista, lida nas imagens verso a verso (`# base: athena`; cada diferença com a Ática numa
  linha `# nota:`); os outros 26 seguem *Poemas de Alberto Caeiro* (Ática, 1946) pela transcrição do Arquivo Pessoa,
  conferida com o Wikisource (`# base: atica`); XVI e XLIV pelo Wikisource, porque o Arquivo Pessoa dá ali a versão
  da ed. Sobral Cunha (1994). «Sobre esta edição» em `edicao.json` (1 erro da *Athena*, 33 lições da revista × 1946).
- `revisao.json`: 3 decisões, todas com a recomendação aplicada (base dos 23; «cousa» → «coisa»; o poema VIII fica).
- Avulsos: `OBRAS_PROPRIAS['fernando-pessoa']` ganhou `alberto-caeiro--01-`, `--02-`, `--03-` (= XXXIV) e `--06-`
  (= III); `poesia.py --fonte ~/Geremias/Solar/producao/versificador` tirou os 4 de `conteudo/…/poesia.js`. Ficam
  avulsos os 2 dos *Poemas Inconjuntos* («A espantosa realidade das cousas», «Dizem que em cada coisa…»).
- Vocabulário: `edicoes/vocabulario/o-guardador-de-rebanhos.json`, 28 palavras (5 vindas do arquivo do autor, que
  ficou com 46 palavras em 54 obras); `conferir` ok nos dois.

## Ao publicar (o principal)
- `public/_redirects`: as 8 regras exatas de `redirects.txt`, antes da primeira regra com `/*`.
- Catálogo `obras.sql` (saem 4 avulsos, entra a obra); tirar o pedido da fila (Catálogo `sugestoes`);
  `traducoes_revisao.py --revisao` para as 3 decisões. Cards: nenhum texto aponta para esses endereços.

## Dúvidas que ficaram
- As estrofes dos 26 poemas da Ática são as da transcrição do Arquivo Pessoa, sem fac-símile livre em que
  conferi-las (nos poemas da *Athena*, o Arquivo Pessoa errou duas: IX e XXV). O fac-símile da Ática não foi achado;
  a Hemeroteca de Lisboa e o Domínio Público bloqueiam acesso automático; a *Presença* n.º 30 (poema VIII, 1931)
  não está no Commons.
- XXV: a quebra de página da *Athena* depois de «filosofia toda.» foi lida como sem estrofe nova.

Rascunhos (downloads, OCR da *Athena*, comparações) em `~/.cache/claude-pedidos-0511/guardador-de-rebanhos/`, só no desktop.
