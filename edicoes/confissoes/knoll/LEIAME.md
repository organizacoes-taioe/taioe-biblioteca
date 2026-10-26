# O latim de Knöll (CSEL 33, 1896) nas Confissões

`original-knoll/` é o texto que vai ao lado da tradução (`obra.py`, `pasta_original`). `original/`
continua o texto de trabalho (O'Donnell), que deu a divisão e serviu de base à tradução.

Como foi feito (2026-10-26), com os arquivos desta pasta:

1. Os hOCR de três escaneamentos do volume no Internet Archive (`corpusscriptoru11wiengoog`,
   `corpusscriptorum0033unse`, `sanctiaureliaugu33augu`), baixados em `~/.cache` (fora do git).
   `hocr.py` lê as linhas; `knoll.py` fica só com o corpo do texto (a letra maior: sem aparato,
   testemunhos nem cabeço), junta as palavras partidas e alinha cada OCR ao texto de trabalho.
2. Votação palavra a palavra: dois OCRs de acordo valem como a leitura de Knöll (conferido nas
   imagens: três de acordo são sempre Knöll, e dois quase sempre); palavra que falta nos três
   é palavra que Knöll não tem; sem acordo, fica a do texto de trabalho, na grafia de Knöll.
3. `revisar.py` monta pranchas com o recorte de cada caso duvidoso; as decisões estão em
   `decisoes.txt` (número do item de `itens.json`: `K` Knöll, `O` o texto de trabalho, `=x /n`
   troca n palavras por x). Uns 200 casos vistos nas imagens.
4. `knoll_final.py` limpa o resto do OCR (acentos, números de linha) e grava `original-knoll/`.

```bash
ITENS=itens.json DECISOES=decisoes.txt python3 -I knoll.py ../original <pasta-dos-hocr> <saida>
python3 -I knoll_final.py <saida> ../original-knoll
```
