# Vidas paralelas, Alexandre e César: o que falta

Branch `pedido-vidas-alexandre-cesar` do `taioe-biblioteca`. Regras da rodada: `~/.cache/claude-pedidos-0511/BRIEF.md`.

## Feito
- Grego de Perrin (1919) montado e conferido com o fac-símile (`original/`, `original/LEIAME.md`; scripts em
  `ferramentas/`, rodar de `~/.cache/claude-pedidos-0511/vidas-alexandre-cesar/`, onde estão os downloads).
- `CONVENCOES.md`, `obra.py` (18 partes: 9 de cada vida, agrupadas por `divisao.agrupar`).

## Falta
- Traduzir (um arquivo de `traducao/` por arquivo de `original/`, mesmo número de blocos):
  Alexandre: 1-8, 9-14, 15-21, 22-30, 31-38, 39-47, 48-55, 56-67, 68-77;
  César: 1-4, 5-14, 15-21, 22-27, 28-35, 36-46, 47-56, 57-61, 62-69.
- Uniformizar nomes e termos (ler as `traducao/notas-*.md`), varrer mesóclise.
- `revisao.json` (~8 decisões), «Sobre» (`apresentacao` em `obra.py`, dizer que a synkrisis se perdeu e que o
  começo de César talvez também), autor novo `plutarco` em `conteudo/autores.js` (área nao-ficcao),
  `edicoes/vocabulario/vidas-alexandre-cesar.json`.
- `python3 ferramentas/traducoes.py vidas-alexandre-cesar`, gerar/conferir o site, limpar `public/` etc., commit.
