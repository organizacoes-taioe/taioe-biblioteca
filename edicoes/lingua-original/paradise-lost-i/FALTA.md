# Paradise Lost, livro I: o que falta

- [x] Texto (`poema.txt`): palavras da 2ª ed. (1674), conferidas com o TCP A50924 e nas imagens do exemplar do
  Commons; grafia e pontuação do Gutenberg 26; 14 parágrafos pelos recuos de 1674; «Argument» de 1674 na grafia
  de hoje. Autor novo `john-milton` e entrada em `obras.json`.
- [ ] Glossário: 2.159 chaves, em 8 partes por subagentes Sonnet (`partes/glossario-N.json`, chaves em
  `~/.cache/claude-pedidos-0511/paradise-lost-i/chaves-N.txt`, instruções em `.../pl-instrucoes.md`); depois
  juntar em `glossario.json` (`.../scripts/juntar.py`), revisar as notas difíceis e `conferir` até «tudo certo».
- [ ] Tradução ao lado: Lima Leitão (Lisboa, Santos & Vieira, s. d., Commons), confrontada com o Wikisource,
  AO1990 com os acentos de Portugal, regrupada nos 14 parágrafos de Milton; `traducao` em `obras.json`;
  `revisao.json` com a pergunta (manter / trocar / tirar). Targini (1823): só o vol. 2 está digitalizado.
- [ ] `publicar`, `gerar.mjs`, `conferir.mjs`, olhar a página; reverter `public/` etc. antes do commit.

Números de verso à margem: o gerador não os aceita nos textos com nota em cada palavra (`{e N}` só passa no
`inline`, e o `lingua_original.py` contaria o «e» como palavra). Fica para o principal decidir.
