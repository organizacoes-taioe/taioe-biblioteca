# Texto espanhol da _Subida del Monte Carmelo_ (e da _Noche oscura_)

## Fonte

P. Silverio de Santa Teresa, C. D., _Obras de San Juan de la Cruz, Doctor de la Iglesia_, t. II: _Subida y Noche
oscura_ (Burgos, Tipografía de «El Monte Carmelo», 1929; Biblioteca Mística Carmelitana, 11). Em domínio público
(Silverio morreu em 1954; a edição tem 97 anos). Fac-símile no Internet Archive:
https://archive.org/details/obrasdesanjuande02john (outra digitalização do mesmo exemplar:
`BMC11ObrasDeSanJuanDeLaCruzTomoIISubidaYNocheOscura`).

Divisão e títulos de Silverio: Subida = argumento, canções, prólogo e 3 livros (15, 32 e 45 capítulos); Noite =
declaração, prólogo, canções e 2 livros (14 e 25 capítulos). Os capítulos I do livro II e do livro III da Subida não
têm título na edição (ficam «## 1.»).

## Arquivos

| arquivo | conteúdo | páginas de 1929 |
|---|---|---|
| `0-argumento-e-prologo.txt` | argumento, canções, prólogo | 3–11 |
| `1-livro-primeiro.txt` | livro I, cap. 1–15 | 12–66 |
| `2-livro-segundo-a.txt` / `-b` / `-c` | livro II, cap. 1–12 / 13–21 / 22–32 | 66–238 |
| `3-livro-terceiro-a.txt` / `-b` | livro III, cap. 1–23 / 24–45 | 239–362 |
| `../../noite-escura/original/*.txt` | a Noite (mesmo método, mesmo script) | 363–512 |

## Método (`montar.py`, `emendas.py`)

`python3 -I montar.py --fontes ~/.cache/claude-pedidos-1611/tmp-subida-noite-escura --obra subida|noche --livro N --gravar`
(os downloads ficam fora do repositório; ver o docstring do script).

1. Três leituras do mesmo fac-símile: o OCR do Internet Archive, o da outra digitalização (BMC) e o Tesseract 5
   (spa) sobre as imagens; decisão palavra a palavra por maioria, e sem maioria pela lista de frequência do espanhol.
2. Saem as notas e variantes de Silverio (letra menor), as chamadas de nota, cabeços e números de página. Páginas
   em que o classificador errou estão corrigidas à mão no script (`NOTAS_DESDE`, `CLASSE_FORCADA`,
   `NUMERO_FORCADO`, conferidas na imagem).
3. Parágrafos pelos números de Silverio: `[II.5]` no primeiro parágrafo do capítulo, `[n]` nos outros. Silverio
   pula números em dois lugares (Subida III,15 vai de 1 a 3; III,19 de 10 a 12): ficou como ele imprimiu.
4. Só na Subida, livros II e III: a transcrição do Documenta Catholica Omnia (texto de Silverio, sem as notas) serve
   de segundo testemunho para **limpar o OCR**: troca só palavra ilegível ou inexistente por palavra parecida que
   está no mesmo lugar do testemunho (cerca de 140 trocas). O Documenta não tem a Noite.
5. Acentuação de hoje (así, más, fue, dio, quedeme); as formas do autor ficam (aqueste, esotro, substancia,
   habemos, decirse ha).
6. `emendas.py`: correções conferidas na imagem ou pelo contexto (livros 0 e I da Subida, revistos dúvida por
   dúvida; nos demais, os trechos embaralhados, notas que vazaram para o texto, títulos e as palavras com sinais
   estranhos). A errata do fim do volume está aplicada.

## O que ficou duvidoso

- `palavras-raras.tsv`: palavras fora da lista de frequência (arquivo, linha). A maioria é latim, nome próprio ou
  forma antiga; algumas são erro de OCR que a votação não pegou (ex.: letra trocada que forma outra palavra). Nos
  livros II–III da Subida e na Noite elas **não** foram conferidas uma a uma na imagem; quem traduz deve conferir a
  palavra estranha no fac-símile (página do cabeçalho do arquivo).
- Erros de OCR que formam palavra válida (del/dal, como/cómo) não aparecem em lista nenhuma; a comparação com o
  Documenta corrigiu parte disso só quando a palavra era rara.
- Lugares em que o Documenta tem texto que o OCR não tem e não se achou a causa: nenhum grande (a página 229 da
  Subida, que tinha sumido, foi recuperada).
