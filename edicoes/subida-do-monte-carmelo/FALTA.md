# Subida do Monte Carmelo (e Noite Escura): o que falta

Branch `pedido-subida-noite-escura`. Situação em 2026-11-16.

## Feito

- Texto espanhol completo das duas obras (Silverio, 1929): `original/` aqui e em `../noite-escura/original/`; método,
  fontes e dúvidas em `original/LEIAME.md`.
- `obra.py` das duas; `CONVENCOES.md` (vale para as duas); `VERSOS.md` (aqui e na Noite).
- Tradução-modelo: `traducao/0-argumento-e-prologo.txt` (inteiro) e `traducao/1-livro-primeiro.txt` (sumário e cap.
  1–5), com `traducao/notas-*.md`.

## Arquivos e palavras (espanhol)

| arquivo | palavras | tradução |
|---|---|---|
| `0-argumento-e-prologo.txt` | 1.875 | pronta (versos literais provisórios) |
| `1-livro-primeiro.txt` | 15.352 | cap. 1–5 prontos (5.460); faltam cap. 6–15 (9.892) |
| `2-livro-segundo-a.txt` (cap. 1–12) | 15.321 | falta |
| `2-livro-segundo-b.txt` (cap. 13–21) | 18.247 | falta |
| `2-livro-segundo-c.txt` (cap. 22–32) | 16.317 | falta |
| `3-livro-terceiro-a.txt` (cap. 1–23) | 18.352 | falta |
| `3-livro-terceiro-b.txt` (cap. 24–45) | 16.833 | falta |
| Noite: `0-prologo-e-cancoes.txt` | 518 | falta |
| Noite: `1-livro-primeiro.txt` | 14.626 | falta |
| Noite: `2-livro-segundo-a.txt` (cap. 1–12) | 13.000 | falta |
| Noite: `2-livro-segundo-b.txt` (cap. 13–25) | 14.995 | falta |

Falta traduzir ≈ 138 mil palavras.

## Divisão em 5 lotes (tradutores em paralelo)

Cada lote lê `CONVENCOES.md` e a tradução-modelo; usa nos versos repetidos a mesma tradução literal das canções
(`traducao/0-argumento-e-prologo.txt`; na Noite, a do lote 4) e registra versos novos em `VERSOS.md`.

| lote | arquivos | palavras |
|---|---|---|
| 1 | Subida `1-livro-primeiro.txt` cap. 6–15 (completar o arquivo) + `2-livro-segundo-b.txt` | ≈ 28.100 |
| 2 | Subida `2-livro-segundo-a.txt` + Noite `2-livro-segundo-b.txt` | ≈ 30.300 |
| 3 | Subida `2-livro-segundo-c.txt` + Noite `1-livro-primeiro.txt` | ≈ 30.900 |
| 4 | Subida `3-livro-terceiro-a.txt` + Noite `0-prologo-e-cancoes.txt`; e conferir no fac-símile `../noite-escura/original/palavras-raras.tsv` | ≈ 18.900 + conferência |
| 5 | Subida `3-livro-terceiro-b.txt` + Noite `2-livro-segundo-a.txt` | ≈ 29.800 |

Ordem sugerida dentro de cada lote: primeiro conferir no fac-símile as palavras do seu arquivo em
`original/palavras-raras.tsv` que não forem latim nem nome (emendar em `original/emendas.py` e regravar com
`montar.py --gravar`, ou anotar nas notas); depois traduzir.

## Por conferir

- Texto espanhol dos livros II e III da Subida e da Noite: limpo por votação de três OCR, pelo segundo testemunho
  (só a Subida) e por emendas nos pontos embaralhados, mas **não conferido palavra a palavra** na imagem. As
  palavras raras estão listadas; os erros que formam palavra válida, não.
- Noite I, cap. 8 (p. 387 de 1929): página apagada, refeita por emendas; reconferir.
- Silverio pula números de parágrafo em Subida III,15 (1→3) e III,19 (10→12): conferido na imagem, ficou assim.
- Autor: `sao-joao-da-cruz` em `conteudo/autores.js` não tem `area: 'catolicismo'` nem `ordem` (está como autor da
  Literatura, pelo poema na língua original). O principal decide se a área precisa de ajuste para receber estas
  duas obras do Catolicismo.
- Versos: decidir com o Gere se as canções usam a tradução de Teófilo Braga, que já está no site (`VERSOS.md`).
- `revisao.json` (decisões delicadas para `/admin/pendencias/`): ainda não feito; candidatas nas notas.
