# Magistério na Biblioteca (desde 2026-10-26)

Pedido do Gere: os documentos do Magistério em domínio público, dentro de «Igreja Católica», dentro
do Catolicismo; do mais recente livre (Pio XI) para o mais antigo. Começa pelos 10 que já têm
português no vatican.va: essas traduções são protegidas (© Dicastério para a Comunicação), então a
nossa é nova, do texto oficial. A fila e o resto da lista estão em `taioe.com.br/admin/sugestoes/`
(categoria «Catolicismo: Magistério»; rotina em `../../../rotinas/sugestoes.md`).

## Decisões (com o Gere, 26/10)

- Autor «Igreja Católica» (`igreja-catolica`, coletivo), gênero «Magistério»; na página do gênero, os
  documentos por data, sob o nome do papa (`grupo`). Cada documento abre direto na leitura
  (`documento: True`), com «Anterior» e «Seguinte» entre eles.
- Tradução com o original ao lado (latim; italiano na *Tra le sollecitudini*); só as notas do próprio
  documento; sem comentários. Numeração: a da versão inglesa do vatican.va (marcas `{§ n}`), salvo
  quando o documento tem a sua.
- Termos fixos em `CONVENCOES.md`, sem fila de revisão para o Gere.

## Como se faz um documento

1. Original e tradução em `<doc>/original/<doc>.txt` e `<doc>/traducao/<doc>.txt` (um subagente
   forte por documento; notas do tradutor em `traducao/notas-<doc>.md`).
2. `python3 edicoes/magisterio/conferir.py <doc>` sem ✗; leitura de conferência pelo principal.
3. Correções do texto de base em `CORRECOES` de `obras.py`; `python3 edicoes/magisterio/obras.py <doc>`.
4. `python3 ferramentas/traducoes.py magisterio/<doc>`, `node ferramentas/site/gerar.mjs`,
   `node ferramentas/site/conferir.mjs`; PR com `public/`, `enderecos.json` e `obras.sql`; Catálogo
   `ferramentas/sql/obras.sql` no teste e na produção; merge; conferir no site.
5. Na página de sugestões, o pedido sai de «Pedidos» quando entra no ar.

## Os 10 primeiros (pedidos de 26/10)

| ordem | documento | papa | data | língua | palavras | estado |
|---|---|---|---|---|---|---|
| 1 | *Divini Redemptoris* | Pio XI | 1937 | latim | ~11 mil | no ar (PR #43) |
| 2 | *Quadragesimo Anno* | Pio XI | 1931 | latim | ~14,7 mil | no ar (2º lote) |
| 3 | *Divini Illius Magistri* | Pio XI | 1929 | latim | ~10,8 mil | no ar (PR #43) |
| 4 | *Mortalium Animos* | Pio XI | 1928 | latim | ~3,3 mil | no ar (PR #43) |
| 5 | *Maximum Illud* | Bento XV | 1919 | latim | ~4,3 mil | no ar (PR #43) |
| 6 | *Pascendi Dominici Gregis* | São Pio X | 1907 | latim | ~14,8 mil | no ar (2º lote) |
| 7 | *Tra le sollecitudini* | São Pio X | 1903 | italiano | ~3,2 mil | no ar (PR #43) |
| 8 | *Rerum Novarum* | Leão XIII | 1891 | latim | ~9,5 mil | no ar (2º lote) |
| 9 | *Immortale Dei* | Leão XIII | 1885 | latim | ~6,5 mil | no ar (2º lote) |
| 10 | *Humanum Genus* | Leão XIII | 1884 | latim | ~5,5 mil | no ar (2º lote) |

## Pedidos de 29/10 (3º lote)

| documento | papa | data | língua | palavras | estado |
|---|---|---|---|---|---|
| *Mit brennender Sorge* | Pio XI | 1937 | alemão | ~8 mil | no ar (3º lote); numeração do texto alemão (1–53) |
| *Casti Connubii* | Pio XI | 1930 | latim | ~13 mil | no ar (3º lote); parágrafos das _Acta_ |
| *Quas Primas* | Pio XI | 1925 | latim | ~5 mil | no ar (3º lote) |
| *Spiritus Paraclitus* | Bento XV | 1920 | latim | ~10 mil | no ar (3º lote) |

Uma decisão de cada nas pendências («Biblioteca: traduções»): `revisao-<documento>.json` nesta pasta.

## Depois

Os próximos vêm da lista do Magistério em `/admin/sugestoes/`, quando o Gere pedir. O levantamento
(fontes, PDFs das *Acta*, dúvidas, reserva) está em `../../../anexos/sugestoes-pesquisa.md`, parte 2.
Os concílios gregos pedem o texto do Mansi (o latim on-line é de edição moderna).

## Armadilhas

- O vatican.va responde HTTP 200 a qualquer língua, mesmo sem tradução: conferir o texto da página.
- O texto do vatican.va vem de OCR das *Acta* e tem erros («f.. r.», «A. A. 5.»): corrigir só o evidente.
- O vatican.va às vezes põe parágrafos fora de `<p>`: o extrator os dá como `<solto>` desde 29/10 (a
  *Quas Primas* perdia o § 5). Os 10 primeiros foram conferidos: nada faltava.
- Texto que não é latim nem italiano: a língua entra em `ADJETIVO` (`obras.py`) e em `LINGUAS` (`gerar.mjs`).
- O Catecismo (PR #7, rascunho) também cria o autor `igreja-catolica`: ao juntar, ficar com uma
  entrada só em `conteudo/autores.js`.
