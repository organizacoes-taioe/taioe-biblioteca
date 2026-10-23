# Apologia de Sócrates: convenções da edição comentada

Primeira obra da Não-ficção (pedido do Gere, 23/10/2026), no esquema da Bíblia Taioé: tradução
nossa com o grego ao lado, a paginação de Stephanus no texto, notas e comentários por tema. A
ferramenta é `ferramentas/comentadas.py`; o gerador do site trata as obras com `comentada: true`.

## Texto

- Grego de Burnet (OCT, 1900), pela Perseus (CC BY-SA na digitação); `original/parte-N.txt`.
  Corrigidos quatro erros de digitação da Perseus (28d, 31c, 36b, 36c; ver `obra.json`, registro).
- `traducao/parte-N.txt`: um parágrafo para cada parágrafo de Burnet, a marca `{St 17a}` no mesmo
  parágrafo nos dois lados (o `comentadas.py` confere). No interrogatório de Meleto, cada fala é um
  parágrafo com travessão.
- Nove partes, cortadas no começo da frase: 17a–18a, 18a–18e, 18e–24b, 24b–28a, 28a–34b,
  34b–35d, 35e–38b, 38c–39d, 39e–42a. Trechos com subtítulo nas partes 3, 4 e 5 (`obra.json`).

## Escolhas (as recomendadas, à espera da revisão do Gere em /admin/nao-ficcao/)

- Tratamento: «vocês» (e «você» com Meleto); *ō ándres Athēnaîoi* = «atenienses»; *ō ándres* =
  «senhores»; «juízes» só em 40a–41d, onde Sócrates o diz.
- *daimónia* = «coisas divinas»; *daímones* = «divindades»; o sinal = «o sinal divino» (31d «algo
  divino, que vem de uma divindade»). Nunca «demônio» na tradução (nos comentários, conforme o autor).
- *ho theós* = «o deus», minúscula. *aretḗ* = «virtude»; *psychḗ* = «alma»; *mýōps* = «moscardo».
- 30b pela leitura de Burnet: «é pela virtude que as riquezas e todas as outras coisas se tornam bens».
- 38a: «a vida sem exame não vale a pena ser vivida pelo homem».

## Notas e comentários

- Notas pelas lições da Bíblia (`taioe-biblia`, `revisao/aprendizado.md`): poucas, contexto
  histórico; `obra.json`, com `apos` (e `ocorrencia`, se a expressão se repete).
- Comentários: só domínio público no Brasil (autor morto até 1955), tradução nossa do original.
  Pesquisa em `pesquisa/` (os achados de três frentes: cristãos, antigos, modernos; os originais
  baixados ficaram fora do git). A escolha e a ordem estão em `temas.json`;
  `python3 ferramentas/comentadas.py --montar apologia-de-socrates` grava `comentarios.json`, que
  daí em diante é a fonte (as respostas do Gere se aplicam nele).
- Críticas a Sócrates entram quando acrescentam algo e são respeitáveis (pedido do Gere, 23/10).
