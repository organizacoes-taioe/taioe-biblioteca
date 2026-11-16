# São Francisco de Assis, de G. K. Chesterton: texto inglês

Arquivos: `capitulo-1.txt` a `capitulo-10.txt`, gerados por `../montar.py` (não editar à mão: mudar as
`EMENDAS` do script e rodar de novo). UTF-8, cabeçalho `# chave: valor`, parágrafos separados por linha em
branco; os quatro versos de Belloc (cap. III) num bloco `| `. Itálicos como `_assim_`.

## Edição e testemunhos

- **Base: a 1ª edição**, *St. Francis of Assisi* (London, Hodder and Stoughton, 1923; coleção «Hodder and
  Stoughton's People's Library», dir. Sidney Dark), 185 páginas, impressa por Richard Clay & Sons, Bungay.
  Domínio público no Brasil (autor †1936) e nos EUA (publicada em 1923).
- **Transcrição de trabalho**: Project Gutenberg nº 63084, que transcreve essa mesma edição, com os
  itálicos marcados (`_..._`). Nota do transcritor: «obvious printer errors have been corrected.
  Hyphenation has been rationalised». Cópia em `ferramentas/cache/sao-francisco-de-assis/pg63084.txt`
  (fora do git; baixada do espelho `gutenberg.pglaf.org/6/3/0/8/63084/`, porque o gutenberg.org estava em
  manutenção em 16/11/2026).
- **Conferência**: as leituras OCR (`_djvu.xml`) de três exemplares de 1923 no Internet Archive:
  `stfrancisofassis00chesuoft` (Robarts, Toronto), `francisofassisi00chesuoft` (Kelly, Toronto) e
  `stfrancisofassis01ches` (Harold B. Lee Library, BYU). Cada palavra do Gutenberg foi alinhada com as três
  leituras; toda palavra que nenhuma leitura apoiava, e todo hífen interno e toda pontuação em que as três
  concordavam contra o Gutenberg, foi conferida na imagem da página. Os recortes e os scripts ficaram em
  `~/.cache/claude-pedidos-0511/sao-francisco-chesterton/` (só neste PC).

## Emendas ao Gutenberg (fica a lição de 1923)

| cap. | Gutenberg | 1923 |
|---|---|---|
| I | the hearth and the _firefight_ | firelight |
| II | spirit of antiquity_:_ the republic | antiquity; |
| III | across the _market place_ (p. 44) | market-place (na p. 43, «market place», como está) |
| V | his city _upside down_ | upside-down |
| IX | the _fingering_ of a shadow | lingering |

## Erros de 1923 que o Gutenberg corrigiu (fica a correção)

- cap. I, p. 10: «pyschological» → psychological.
- Pontos que faltam na impressão (tipo quebrado ou caído), conferidos na imagem: cap. IV «cross.» (p. 69);
  cap. V «St.» (p. 82); cap. VI «poets.» (p. 101), «grammar.» e «St.» (p. 103), «St.» (p. 106), «civil.»
  (p. 108), «St.» e «possessed.» (p. 109), «pity.» (p. 111).

## O mais

- Ligaduras «æ» (Cæsar, anæsthetic) como no Gutenberg e na impressão.
- A grafia é a britânica da edição (civilisation, realise).
- A divisão em dez capítulos é a do autor; não há numeração de parágrafos.

## Contagens

| arquivo | capítulo | parágrafos | palavras |
|---|---|---:|---:|
| capitulo-1.txt | The Problem of St. Francis | 7 | 2.753 |
| capitulo-2.txt | The World St. Francis Found | 20 | 5.374 |
| capitulo-3.txt | Francis the Fighter | 14 | 4.429 |
| capitulo-4.txt | Francis the Builder | 15 | 3.870 |
| capitulo-5.txt | Le Jongleur de Dieu | 16 | 4.969 |
| capitulo-6.txt | The Little Poor Man | 14 | 4.869 |
| capitulo-7.txt | The Three Orders | 14 | 5.011 |
| capitulo-8.txt | The Mirror of Christ | 13 | 4.766 |
| capitulo-9.txt | Miracles and Death | 16 | 4.490 |
| capitulo-10.txt | The Testament of St. Francis | 10 | 3.281 |
