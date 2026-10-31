# Vocabulário: as palavras raras em português com nota

Pedido do Gere (31/10/2026), com o piloto aprovado no mesmo dia (*Vidas Secas*): nas obras em
português, as palavras raras ficam sublinhadas (pontilhado discreto) e um toque abre uma definição
curta. **É a regra para todo livro novo em português**, original ou tradução nossa: ele entra no ar
já com o seu arquivo aqui. Vai direto ao site, sem passar pelas pendências.

Um arquivo por obra, por coletânea de contos ou, na poesia, por autor: `edicoes/vocabulario/<nome>.json`
(formato abaixo). O `ferramentas/site/gerar.mjs` marca as formas no lado em português (nas páginas
bilíngues, o original fica de fora), e o `js/notas.js` abre a nota.

Ferramenta, na raiz do repositório: `node ferramentas/vocabulario.mjs texto|candidatos|conferir|ocorrencias …`
(o topo do arquivo explica). `conferir` tem de dar `ok` antes do PR; as palavras de duplo sentido se
conferem com `ocorrencias`.

## O que marcar
Palavras que um leitor brasileiro adulto de hoje, com escolaridade média e criado na cidade,
provavelmente não conhece ou entende errado:
- regionalismos, termos de ofício, de lugar e de época (do sertão, do campo, de Portugal, da corte do
  Império, da Igreja antiga, da navegação, da guerra);
- palavras raras, eruditas ou antigas (arcaísmos, latinismos, termos de mitologia que o texto usa
  como palavra comum);
- **sobretudo** as palavras comuns num sentido antigo ou regional que o leitor de hoje lê errado
  (no piloto: cabra = homem do povo, amo = patrão, quarto = quadril, cristão = pessoa, cobre =
  dinheiro); em Eça, por exemplo, rapariga = moça, fato = roupa, comboio = trem; em Machado, moço =
  criado, chácara, sege, moleque etc. Nenhuma lista de frequência pega essas.
Não marcar: o que o leitor médio conhece, nomes próprios, palavras que se adivinham pela raiz ou
pelo contexto imediato. Na dúvida sobre se é rara, não marque: o texto não pode virar um mar de
sublinhados. Ordem de grandeza do piloto: ~7 palavras por mil palavras de texto num romance
regional; num texto urbano e moderno, bem menos; num texto antigo (Camões, Gil Vicente), mais.
Prefira ficar abaixo.

## Como definir
- `def`: no máximo uns 20 palavras, **no sentido em que a palavra aparece ali**, escrita por você, em
  linguagem simples; sem exemplos, sem etimologia, sem ponto final. Para locução, comece por ela
  («de chofre: de repente»), como no piloto.
- `classe`: curto («substantivo masculino», «adjetivo», «verbo», «regionalismo, substantivo feminino»,
  «antigo, advérbio»).
- Confira em fontes livres: Wiktionary em português, dicionários antigos em domínio público (Cândido
  de Figueiredo, 1913; Morais; Bluteau). NÃO copie nem parafraseie de perto o Houaiss, o Aulete, o
  Michaelis ou o Priberam (protegidos); pode consultá-los para conferir o sentido, e escreve com suas
  palavras.
- Português do Brasil, sem mesóclise nas definições.
- Mesma forma com dois sentidos no mesmo arquivo: registre só o raro, e diga onde ele vale com
  `so_capitulos` (números das partes) e, nos arquivos de várias obras, `so_obras` (ids). Se os dois
  sentidos aparecem na mesma parte da mesma obra, deixe de fora.
- Formas: todas as formas exatas, em minúsculas, em que a palavra aparece (plural, feminino, flexões
  do verbo). Verbo com pronome pendurado («derreava-se», «apear-se-ia») entra só com a forma do
  verbo («derreava», «apear»): o site marca o verbo e deixa o pronome fora. Compostos com hífen
  entram inteiros («guarda-peito»). Locuções de várias palavras não são marcadas: marque a palavra
  rara dela e defina a locução («fábrica» → «cavalo de fábrica: …»).
- Uma forma não pode estar em duas entradas do mesmo arquivo.

## Formato
```
{"obra": "<id>",            ← ou, num arquivo de várias obras: "obras": ["id1", "id2", …]
 "palavras": [
  {"lema": "alpercata", "formas": ["alpercata", "alpercatas"], "classe": "substantivo feminino",
   "def": "sandália de couro cru, presa ao pé por tiras", "exemplo": "<trecho da 1ª ocorrência>",
   "capitulo": 1, "obra_ex": "<id, nos arquivos de várias obras>", "so_capitulos": [..], "so_obras": [..]}
 ]}
```
`exemplo`, `capitulo` e `obra_ex` são para conferência e não vão ao site. Ordem: a da primeira ocorrência.
