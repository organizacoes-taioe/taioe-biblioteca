# Vida de Santo Agostinho (Possídio): texto latino

Arquivos: `prefacio.txt` (Praefatio) e `vita.txt` (caps. 1–31, `[n]` no primeiro parágrafo de cada capítulo).
Gerados por `texto/scripts/montar_original.py` a partir das colunas conferidas em `texto/colunas/`: corrigir
lá e rodar o script, não aqui.

## Edição
- **Base:** o texto dos Maurinos (Paris, 1679–1700) na *Patrologia Latina* 32 (Migne, Paris, 1841), col. 33–66.
  Domínio público. Sem as notas, as chamadas de nota, os sumários dos capítulos e as referências bíblicas que os
  editores puseram entre parênteses no texto (lista em `texto/colunas/refs.tsv`, usada nas referências da tradução).
- **Cap. 30:** a PL 32 copia a carta de Agostinho a Honorato só até «necessarium propter vos» e remete à carta 228
  («Caetera videre est in tomo secundo, epist. 228, nn. 10, 11, 12, 13 et 14»). O resto (§§ 10–14, de «Hic forte quis
  dicat» a «minime defecerunt») vem da PL 33 (1845), col. 1017–1019, sem os números de seção; cada seção é um
  parágrafo. É o texto da carta nas obras de Agostinho, não o que Possídio copiou: Weiskotten, que segue os
  manuscritos da *Vita*, traz pequenas diferenças (ex.: «Hic fortasse» por «Hic forte»). Decisão no `revisao.json`.
- **Weiskotten** (Princeton, 1919): edição crítica; o autor não tem data de morte achada, e a edição não serve de
  base. Usada só como esqueleto do alinhamento e para comparar.

## Como foi estabelecido (2026-11-16)
1. Quatro leituras automáticas (ABBYY do Internet Archive, com coordenadas, `*_djvu.xml`) de três tiragens da PL 32:
   1845 (`bim_…_1845_32`), 1841 (`sanctiaureliiau1v2augu`, t. 1–2, e `sanctiaureliiau01augu`, t. 1) e 1844
   (`patrologiaecurs157unkngoog`, Google, leitura ruim, peso menor); duas de Weiskotten (`sanctiaugustiniv00possrich`,
   `cu31924029266513`). Na carta, a PL 33 de 1845 (`bim_…_1845_33`) e a de 1841 (t. 2 do mesmo `1v2augu`).
2. As leituras do PL alinhadas palavra a palavra com Weiskotten (`alinhar.py`) e votadas (`votar.py`, `compor.py`):
   onde duas leituras do PL concordam contra Weiskotten, fica o PL; trocas típicas de OCR (t/l, c/e, ſ/f…) e formas
   fora de um léxico latino (Vulgata Clementina, Perseus, os latins da Biblioteca) resolvidas pela outra leitura.
3. O resultado dividido pelas colunas impressas (`colunas.py`) e **conferido coluna por coluna nas imagens da tiragem
   de 1845** (recortes IIIF, `texto/colunas/urls.tsv`), por um subagente; registro em `texto/colunas/CONFERENCIA.md`.
   Grafia como impressa (j, v, ae por æ, oe por œ; sem acentos); palavra partida no fim da linha, inteira.
4. Os dois dísticos (cap. 22, a inscrição da mesa; cap. 31, o epitáfio) em versos (`| `), como impressos.

## Leituras a notar
- Impressos assim e mantidos: «collaetantibus» (7), «juste» (13; a nota de Migne dá «injusti»), «Quanquam» (carta),
  «Hipponensium-Regiorum» (28).
- Imagem pouco nítida, lido «earumdem» (16), «quorumdam», «spiritualibus», «denuntiabat» (24), «cuncta» (17).
- Saíram «(non exstat)», inserção editorial (28), e as letras de nota «(a)», «(b)».
