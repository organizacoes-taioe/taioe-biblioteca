# Mensagem: o que falta (2026-11-02)

Pronto: a obra `mensagem` (`conteudo/fernando-pessoa/mensagem.js`, gerado por `montar.py` desta pasta a
partir de `texto.json`): os 44 poemas da 1ª edição (1934), com as partes, as epígrafes e as seções do
livro; «Sobre esta edição»; vocabulário (`edicoes/vocabulario/mensagem.json`, 16 palavras, `conferir` ok).
Cada poema tem endereço pelo título (`/biblioteca/fernando-pessoa/mensagem/o-dos-castelos/`).
Os 44 poemas saíram dos avulsos do autor (`OBRAS_PROPRIAS` em `ferramentas/poesia.py`, prefixo
`mensagem--` do corpus; `conteudo/poesia.js` e `conteudo/fernando-pessoa/poesia.js` regenerados com
`python3 ferramentas/poesia.py --fonte /mnt/arquivos/Geremias/Solar/producao/versificador`; só a
Mensagem mudou) e do `fernando-pessoa-poesia.json` (51 palavras em 58 poemas, `conferir` ok).

Ao publicar (o principal):
- `OBRAS_PROPRIAS`: a branch `pedido-primeiros-cantos` cria a mesma lista, na mesma forma; no merge,
  ficar com os dois itens (`'fernando-pessoa': ('mensagem--',)` e `'goncalves-dias': ('primeiros-cantos--',)`)
  e rodar o `poesia.py` de novo;
- acrescentar ao `public/_redirects` as 44 linhas de `redirects.txt` (endereço antigo
  `/biblioteca/fernando-pessoa/mensagem-<poema>/` → o poema na obra, 301);
- `enderecos.json`: o gerador só acrescenta (parte do arquivo congelado e soma o novo; nunca apaga
  linha). Os avulsos são obras de uma parte só e não têm linha ali, então nada some; a obra nova
  entra com 44 linhas;
- Catálogo `obras.sql` no teste e na produção: as 44 obras avulsas saem e entra `mensagem` (a posição
  de leitura de quem lia um poema avulso se perde);
- Cards: nenhum texto aponta para esses endereços (conferido em `taioe-cards`, `origin/main`,
  `data/textos-pt.json` e `fonte/textos/pt/`);
- tirar a Mensagem dos pedidos (Catálogo `sugestoes`).

Falta: nada do texto. A conferência foi Wikisource × OCR próprio do fac-símile × imagens nos pontos
de divergência; um ponto que os dois testemunhos errassem do mesmo jeito passaria (improvável).
