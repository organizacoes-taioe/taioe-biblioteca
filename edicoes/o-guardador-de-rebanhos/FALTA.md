# O Guardador de Rebanhos (Alberto Caeiro): o que está feito e o que falta

Obra própria `o-guardador-de-rebanhos` (Literatura, autor `fernando-pessoa`), os 49 poemas, montada por
`montar.py` a partir de `texto/NN.txt` (um arquivo por poema, na grafia de hoje mas com «cousa», que o
`montar.py` troca por «coisa»; o corpus do Versificador não foi tocado).

## Edição
- Os 23 poemas que Pessoa publicou na *Athena* n.º 4 (jan. 1925; fac-símile no Commons, `File:Athena, 4.pdf`,
  pp. 145–156 da revista = pp. 23–34 do PDF): base a *Athena*, lida nas imagens verso a verso (`# base: athena`).
- Os outros 26: a 1ª edição em livro, *Poemas de Alberto Caeiro* (Ática, 1946), pela transcrição do Arquivo
  Pessoa (arquivopessoa.net, que segue a Ática), conferida com o Wikisource (`# base: atica`). XVI e XLIV: o
  Arquivo Pessoa dá a versão da ed. Sobral Cunha (1994, protegida); vale a da Ática (Wikisource).

## Feito
- 2026-11-05: os 23 poemas da *Athena* em `texto/` (cada diferença com o Arquivo Pessoa numa linha `# nota:`).

## Falta
- os 26 poemas da Ática em `texto/`; `montar.py`, `edicao.json`, `revisao.json`, vocabulário, `poesia.py`
  (`OBRAS_PROPRIAS`) e `redirects.txt`.

Rascunhos (downloads, OCR, comparações) em `~/.cache/claude-pedidos-0511/guardador-de-rebanhos/`, só no desktop.
