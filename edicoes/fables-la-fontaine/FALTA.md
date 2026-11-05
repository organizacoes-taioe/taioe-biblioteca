# Fables de La Fontaine (seleção): o que falta

Pedido de 05/11/2026 (branch `pedido-fabulas-la-fontaine`). 12 fábulas na língua original, cada uma um
poema de `edicoes/lingua-original/<pasta>/` sob o autor novo `jean-de-la-fontaine`, agrupadas no livro
«Fables (seleção)» (`livro` em `obras.json`), com o número no campo `n` («I, 1»; o
`lingua_original.py` passou a levá-lo ao `conteudo/`).

## Feito
- Texto das 12 (`poema.txt`), 362 versos: palavras e pontuação da edição de 1678 (Thierry e Barbin,
  tomos 1–3, Wikisource validado), na ortografia de hoje, conferidas palavra por palavra com a de 1678 e
  com a de 1874 (script em `~/.cache/claude-pedidos-0511/fabulas-la-fontaine/scripts/comparar.py`, só
  neste PC). Regras em `CONVENCOES.md`.
- Autor em `conteudo/autores.js`.

## Falta
- Glossários (`glossario.json` de cada pasta), por subagentes Sonnet; depois revisão das notas
  difíceis; `python3 ferramentas/lingua_original.py conferir` sem problemas.
- Traduções ao lado (`traducao.txt` + campo `traducao` em `obras.json`), fábula por fábula.
- `revisao.json` desta pasta (as escolhas duvidosas).
- `publicar --provisorio` só para ver; gerar e conferir o site na worktree; não commitar `public/`.
