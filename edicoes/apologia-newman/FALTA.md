# Apologia pro Vita Sua (Newman): o que está feito e o que falta

Branch `pedido-apologia-newman`. Leia antes: `CONVENCOES.md` (com as decisões da uniformização) e `original/LEIAME.md`.

## Feito (2026-11-16)

- Original inglês (Gutenberg #22088, Longmans 1890, forma final) em 21 arquivos, por `original/montar.py`, com o grego
  em letras gregas, «Christmas Day» corrigido e a nota de quatro parágrafos do cap. II montada inteira (LEIAME).
- `obra.py` e o autor `sao-john-henry-newman` em `conteudo/autores.js`.
- **Tradução completa**: os 21 arquivos, ~132.700 palavras, o mesmo número de parágrafos do original em todos, com as
  chamadas `[n]`, os `¤`, os `##` e as linhas `| ` no lugar (preparador e quatro tradutores em paralelo; notas de cada
  lote em `traducao/notas-*.md`).
- Uniformização: os termos do principal (alocução, Vossa Excelência, inverdade × mentira, falta de veracidade,
  equívoco, Igreja estabelecida, Dissidência, lugar de Fellow, Ver / ver acima, grego) e a coerência da tabela do
  `CONVENCOES.md` conferidos termo a termo, original × tradução, parágrafo a parágrafo; decisões novas registradas lá.
- `revisao.json`: 10 decisões para o Gere (`python3 ferramentas/traducoes_revisao.py` dá ok).

## Falta (principal)

- `edicoes/vocabulario/apologia-newman.json` (palavras raras com nota) e as notas gerais na fila.
- `python3 ferramentas/traducoes.py apologia-newman`, gerar e publicar.
- Versos: nenhuma estrofe inglesa; só versos soltos citados na frase (caps. I, II e V, Nota A), em prosa literal entre
  aspas, listados nas `notas-*.md` dos lotes. Por isso não há `VERSOS.md`. Os dois trechos latinos ficam em latim.

## Ficou por conferir (sugestão)

- Releitura corrida de cada arquivo: a uniformização foi por termo, não frase a frase.
- Nota D: o calendário foi traduzido por script e revisto linha a linha pelo tradutor (`notas-14-nota-d.md`); os erros
  do impresso ficaram (Willam, Ceofrid…).
- Pequenas escolhas dos tradutores que o principal pode rever:
  - Nota G § 20: «no sentido inglês de _apology_, desculpa» (a palavra «desculpa» é acréscimo, para o jogo se entender).
  - cap. IV, 1ª parte, § 49: «vocês» no desabafo contra os curiosos («Covardes!»), e não «os senhores».
  - Nota B § 24: _a fervent record_ ficou literal (talvez _recent_; conferir na imagem da página).
  - «: —» do original mantido no cap. I, § 16 (antes da conclusão, não de citação).
