# Castillo interior: texto castelhano de trabalho

Arquivos `00-prologo.txt` … `08-epilogo.txt`, UTF-8, parágrafos separados por linha em branco.

## Edição

- **Base**: Silverio de Santa Teresa (ed.), *Obras de Santa Teresa de Jesús*, t. IV, *Moradas, Conceptos,
  Exclamaciones* (Burgos, Tip. de «El Monte Carmelo», 1917), pp. 1–210: o texto do autógrafo de Sevilha, com a
  ortografia atualizada pelo editor e as formas da língua de Teresa (*ansí*, *mesmo*, *inorancia*, *terná*,
  *mirá*). Silverio deixa de fora as emendas de Gracián e de outros e põe entre colchetes as letras ou palavras
  que faltam no autógrafo (*quita[r]*, *mes[mo]*); os colchetes ficaram. As notas de rodapé dele (variantes do
  autógrafo, emendas de Gracián, lições de Fr. Luis de León, remissões) ficaram de fora, e com elas as chamadas
  «(1)». O título da obra («El castillo interior») e o cabeço «JHS» de Teresa ficam no prólogo.
- Domínio público: Teresa †1582; Silverio de Santa Teresa (Julián Gómez Fernández) †1954 (no Brasil, livre desde
  2025); publicado em 1917 (livre também nos EUA).
- Grafia, acentos e maiúsculas como na edição de 1917 (*fué*, *dió*, *Él*, *Su Majestad*). As ementas dos
  capítulos, que a edição compõe em versal sem acentos, foram passadas a caixa baixa com os acentos do resto do
  texto (conferidas à mão).

## Como foi estabelecido

Quatro exemplares digitalizados da edição de 1917 no Internet Archive: `obrasdestateresa04tere` e
`obrasdesantatere04tere` (OCR ABBYY) e `bwb_Y0-AAF-301` e `bwb_C0-ANN-573` (OCR Tesseract). Scripts em `../estabelecer/`
(rodavam em `~/.cache/claude-pedidos-0511/castelo-interior/`, com `dl/` = os djvu.xml e `trab/` = o trabalho):

1. `paginas.py` lê o `_djvu.xml` (linhas com coordenadas); `extrair.py` tira o corpo de cada página (sem cabeço,
   sem rodapé: altura da letra das notas, menor, e a linha que começa com o número da nota) e marca os
   parágrafos pelo recuo (comparado com as linhas vizinhas, por causa da inclinação das páginas);
2. `alinhar.py` alinha as quatro leituras palavra a palavra; `votar2.py` vota, depois de limpar cada leitura
   (tiques de composição antes das palavras, *fi* → *ñ*, *g* → *y*);
3. as divergências que o voto não resolve (empates entre palavras que existem, acentos de *mi/mí*, *si/sí*,
   *esta/está*, *cuan/cuán*, *rn/m* em *ternéis/teméis*) e as palavras que não aparecem em mais nenhum lugar
   foram conferidas nas imagens (`pranchas.py`, ~110 pontos; decisões em `decisoes-ctx.json`; as ementas, que a edição dá em versal sem acento, em `ementas.json`; sinais de caderno
   e sobras de cabeço em `remendos.json`);
4. `montar.py` grava os arquivos (ementas, marcas `[I.1]`, títulos).

Para conferência de sentido, o texto de Fr. Luis de León na edição Nelson (*Obras escogidas*, Londres, 1912,
`obrasescogidasd00tere`), que segue outra tradição (com as emendas), e o fac-símile do autógrafo (Sevilha, 1882,
`elcastillointeri00tere`).
