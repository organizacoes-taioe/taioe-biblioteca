# Confissão (Tolstói): o que falta

Branch `pedido-confissao-tolstoi`. **Pronta para publicar** (05/11): original conferido, tradução dos 16
capítulos revisada contra o russo, `CONVENCOES.md`, `revisao.json` (8 decisões), vocabulário
(`edicoes/vocabulario/confissao.json`, 26 verbetes), `conteudo/` gravado por `traducoes.py confissao-tolstoi`.

Para o principal:
- `ferramentas/site/gerar.mjs` ganhou `ru: { nome: 'Russo', slug: 'russo' }` em `LINGUAS` (sem isso o
  gerador quebra com «Cannot read properties of undefined (reading 'slug')»). Juntar com as outras branches.
- Autor novo `liev-tolstoi` em `conteudo/autores.js` (depois de `seneca`): resolver por união.
- Gerar, PR, Catálogo `obras`, merge; `traducoes_revisao.py --revisao` para as 8 decisões; tirar dos pedidos.
- Notas gerais: ficam para os lotes (não feitas, como manda o brief).
