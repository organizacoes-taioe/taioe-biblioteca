# O que falta (Vida de Santo Agostinho, São Possídio)

Pronta na branch `pedido-vida-de-santo-agostinho`: latim (`original/prefacio.txt`, `original/vita.txt`, montados por
`texto/scripts/montar_original.py` das colunas conferidas em `texto/colunas/`), tradução, `obra.py`, `CONVENCOES.md`,
`original/LEIAME.md`, `revisao.json` (7 decisões), vocabulário `edicoes/vocabulario/vida-de-santo-agostinho.json`
(25), autor `sao-possidio` em `conteudo/autores.js`, `conteudo/` gravado por `traducoes.py`; site gerado e conferido
na worktree (`tudo certo`).

Falta só o do principal: juntar, gerar `public/`, Catálogo `obras`, PR, merge, `traducoes_revisao.py --revisao` e tirar
dos pedidos. Sem regras de `_redirects`.

Para refazer o latim do zero: os scripts de `texto/scripts/` leem os OCRs do Internet Archive (identificadores no
`original/LEIAME.md`), que foram apagados de `~/.cache/claude-pedidos-0511/vida-de-santo-agostinho/` depois do uso.
