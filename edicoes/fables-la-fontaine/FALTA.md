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
- Traduções ao lado: Bocage na Cigarra e no Corvo (Obras poéticas, vol. III, 1875, conferidas nas
  imagens do IA) e Machado de Assis nos Animais (Poesias completas, 1901, Wikisource). As outras nove
  ficam sem (Filinto Elísio é pesado; Curvo Semedo é livre; Paranapiacaba e a coletânea de 1886 sem
  cópia digital ao alcance). `revisao.json` com 8 escolhas (conferido pelo `traducoes_revisao.py`).

- Glossários das 12 (1.925 verbetes; `conferir` dá «tudo certo»), feitos pelo principal (os
  subagentes não puderam ser lançados: limite de concorrência), com os verbetes partilhados em
  `glossario/m1–m6.py`, a escolha por ocorrência em `glossario/escolhas.py` e
  `python3 edicoes/fables-la-fontaine/glossario/montar.py gravar`. Definições escritas no padrão do
  fr.wiktionary (lema = página dele), sem conferência verbete a verbete no próprio Wiktionary: o
  download do cache (`ferramentas/cache/wiktionary/fr/c2`) estava lento por limite da API.
- `conteudo/jean-de-la-fontaine/lingua-original.js` e `conteudo/lingua-original.js` gravados pelo
  `lingua_original.py publicar`.

## Falta
- Pronto para o principal juntar e publicar: gerar o site, Catálogo `obras` (12 obras novas), PR,
  `traducoes_revisao.py --revisao` (8 escolhas novas). Sem regras de `_redirects` (endereços novos).
- Conferência dos lemas no fr.wiktionary: `~/.cache/claude-pedidos-0511/fabulas-la-fontaine/scripts/lemas.py`
  (só neste PC); resultado no relatório da rodada.
- Depois das respostas do Gere ao `revisao.json`: aplicar (travessões, «Hé ! bonjour», maiúsculas…)
  em `edicoes/lingua-original/<pasta>/poema.txt` e rodar `glossario/montar.py gravar` (as posições
  das palavras mudam se o texto mudar: conferir `escolhas.py`).
