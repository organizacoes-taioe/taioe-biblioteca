# Notas gerais: as notas de contexto dos livros em português

Pedido do Gere (04/11/2026): notas em todos os livros em português da Biblioteca, originais e
traduções nossas, «seguindo os critérios das outras notas: dar contexto que ajude a entender o
texto». Cada nota passa pela aprovação dele, uma por uma, em `taioe.com.br/admin/notas/`; **só a
nota aprovada (`"revista": true`) vai ao site**. Feitas **por lotes**: as respostas de cada lote
calibram o seguinte (as lições ficam em `APRENDIZADO.md`, nesta pasta).

Ficam de fora: as obras comentadas (*Apologia*, *Carta* de Caminha), que têm as notas delas no
`obra.json`, e as obras na língua original, que têm o glossário.

## O critério (o das notas da Bíblia, `../../../biblia/revisao/aprendizado.md`)
Entram: quem é a pessoa, quando o leitor pode não saber; lugar pouco conhecido; fato histórico;
instituição, cargo, costume, objeto ou moeda de época; alusões que passariam despercebidas
(mitologia, Bíblia, clássicos, ditos célebres); o ponto importante que o leitor não perceberia; a
tradução de frase em outra língua citada pelo autor (decisão dele, 04/11); o uso marcante na
liturgia da Missa.

Não entram: definição de palavra (é o vocabulário, `../vocabulario/`, que vai direto ao site) e
notas de língua; análise, interpretação, enredo, ironia explicada; o que o texto já diz ou o leitor
já sabe; o que volta sempre (só a primeira vez); associações dispensáveis; notas vagas, genéricas ou
preciosistas; variantes de edição.

Poucas e certeiras: em média uma a cada mil palavras (menos em texto moderno; mais em texto antigo
ou cheio de alusões). Uma a três frases curtas e simples; só fato seguro. Sem mesóclise; aspas « ».

## Formato
Um arquivo por obra, por coletânea ou, na poesia avulsa, por autor: `<nome>.json`.
```
{"obra": "<id>",                ← ou "obras": [ids], e então cada nota leva "obra"
 "notas": [
  {"id": "itaguai", "parte": 1, "apos": "vila de Itaguaí", "ocorrencia": 2, "texto": "…",
   "lote": 1, "porque": "…", "revista": true}
 ]}
```
- `parte`: o número da parte (1, 2…), como no vocabulário; `apos`: o trecho exato do texto cru
  depois do qual entra a letra (único na parte, ou com `ocorrencia`); `porque` é só para o nosso
  registro (não vai à revisão nem ao site); `revista` só depois da aprovação dele.
- O `gerar.mjs` põe a letra depois do `apos` (ou do fim do itálico) e a lista «Notas» no fim da
  parte; o `notas.js` a abre junto da linha. Nota aprovada que não acha o seu lugar para o gerador.

## Ferramenta (na raiz do repositório)
```
node ferramentas/notas.mjs texto <id…>              o texto cru de cada parte, em ~/.cache/taioe-notas/textos/
node ferramentas/notas.mjs conferir [arquivo…]      tem de dar «ok» antes do PR
node ferramentas/notas.mjs revisao ../infra/dados/paginas   grava notas.json (as notas sem «revista»)
node ferramentas/notas.mjs aplicar <respostas.json> aprovar/alterar → revista; excluir → sai
```

## Fluxo de um lote
1. Escolher as obras do lote (ordem em `LOTES.md`). Um subagente por obra, com as instruções de
   `~/.cache/taioe-notas/BRIEF.md` (só neste PC; o critério é o desta página e do `APRENDIZADO.md`),
   gravando em `~/.cache/taioe-notas/lote<L>/`. O principal revisa cada nota (tira, corta, confere
   fatos) e copia para esta pasta.
2. `conferir`, PR com os arquivos (as notas ainda não aparecem no site), merge.
3. `revisao ../infra/dados/paginas`, `python3 dados/paginas/gerar.py dados/paginas/notas.json` no
   infra, commit e Catálogo `dados/paginas/notas.sql` no teste e na produção.
4. Quando ele responder: `bash ../rotinas/respostas.sh notas exportar`, `aplicar`, lições novas no
   `APRENDIZADO.md`, `gerar.mjs` e `conferir.mjs`, PR, merge; `revisao` de novo (a página fica só
   com o que falta), Catálogo e `bash ../rotinas/respostas.sh notas marcar <…aplicadas.json>`.
5. Lote seguinte só depois das respostas do anterior (pedido dele: calibrar a cada lote).
