# Apologia de Sócrates: convenções da edição comentada

Primeira obra da Não-ficção (pedido do Gere, 23/10/2026), no esquema da Bíblia Taioé: tradução
nossa com o grego ao lado, a paginação de Stephanus no texto, notas e comentários por tema. A
ferramenta é `ferramentas/comentadas.py`; o gerador do site trata as obras com `comentada: true`.

## Texto

- Grego de Burnet (OCT, 1900), pela Perseus (CC BY-SA na digitação); `original/parte-N.txt`.
  Corrigidos quatro erros de digitação da Perseus, conferidos no grego: 28d «μὴ αὐτὸν οἴει» (estava
  «ὴ»), 31c (espaço antes da vírgula), 36b «τί ἄξιος» (sobrava um «τ»), 36c «τῷ ὄντι» (faltava o «τ»).
- `traducao/parte-N.txt`: um parágrafo para cada parágrafo de Burnet, a marca `{St 17a}` no mesmo
  parágrafo nos dois lados (o `comentadas.py` confere). No interrogatório de Meleto, cada fala é um
  parágrafo com travessão.
- Nove partes, cortadas no começo da frase: 17a–18a, 18a–18e, 18e–24b, 24b–28a, 28a–34b,
  34b–35d, 35e–38b, 38c–39d, 39e–42a. Trechos com subtítulo nas partes 3, 4 e 5 (`obra.json`).

## Escolhas (aprovadas pelo Gere em 24/10/2026: as oito recomendadas, a divisão e as notas)

- Tratamento: «vocês» (e «você» com Meleto); *ō ándres Athēnaîoi* = «atenienses»; *ō ándres* =
  «senhores»; «juízes» só em 40a–41d, onde Sócrates o diz.
- *daimónia* = «coisas divinas»; *daímones* = «divindades»; o sinal = «o sinal divino» (31d «algo
  divino, que vem de uma divindade»). Nunca «demônio» na tradução (nos comentários, conforme o autor).
- *ho theós* = «o deus», minúscula. *aretḗ* = «virtude»; *psychḗ* = «alma»; *mýōps* = «moscardo».
- 30b pela leitura de Burnet: «é pela virtude que as riquezas e todas as outras coisas se tornam bens».
- 38a: «a vida sem exame não vale a pena ser vivida pelo homem». 30e: «moscardo» (não «mutuca»).
- Termos para os próximos livros de Platão: *aretḗ* = «virtude»; *psychḗ* = «alma»; *sophía* =
  «sabedoria»; *philosopheîn* = «filosofar»; *exetázein* = «examinar»; *elénchein* = «pôr à prova»,
  «refutar»; *kalòs kagathós* = «homem de bem»; *deinòs légein* = «hábil no falar»; *tòn héttō lógon
  kreíttō poieîn* = «fazer da razão mais fraca a mais forte»; *mýōps* = «moscardo».
- A nota do juramento «pelo cão» (22a) saiu: «suposição que acrescenta pouco» (o Gere, 24/10).

## Notas e comentários

- Notas pelas lições da Bíblia (`taioe-biblia`, `revisao/aprendizado.md`): poucas, contexto
  histórico; `obra.json`, com `apos` (e `ocorrencia`, se a expressão se repete).
- Comentários: só domínio público no Brasil (autor morto até 1955), tradução nossa do original.
  Pesquisa em `pesquisa/` (os achados de três frentes: cristãos, antigos, modernos; os originais
  baixados ficaram fora do git). A escolha e a ordem estão em `temas.json`;
  `python3 ferramentas/comentadas.py --montar apologia-de-socrates` grava `comentarios.json`, que
  daí em diante é a fonte (as respostas do Gere se aplicam nele).
- Críticas a Sócrates entram quando acrescentam algo e são respeitáveis (pedido do Gere, 23/10).
