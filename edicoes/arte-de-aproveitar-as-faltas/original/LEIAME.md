# A arte de aproveitar as próprias faltas, de Joseph Tissot: texto francês de trabalho

Arquivos: `00-avant-propos.txt` a `02-segunda-parte-b.txt`. São 4 arquivos em UTF-8, com cabeçalho `# chave: valor` e parágrafos separados por uma linha em branco. A tradução está em `../traducao/`.

O texto foi estabelecido por nós a partir de um scan. Não há transcrição digital confiável disponível.

## Fonte e edição

- **Edição de base:** *L'Art d'utiliser ses fautes d'après saint François de Sales*, par le P. Joseph Tissot, supérieur général des Missionnaires de Saint-François de Sales.
  - «Sixième édition, revue, augmentée».
  - Paris/Poitiers, Librairie religieuse H. Oudin; Annecy, Abry, 1894.
  - Imprimatur de Poitiers, 22 de maio de 1894. O avant-propos é datado de Annecy, «1er vendredi d'avril 1894».
- **Scan:** Bibliothèque municipale de Lyon, Numelyo, cote SJ A 348/185, digitalização Google, «Domaine public, Licence Ouverte», https://numelyo.bm-lyon.fr/f_view/BML:BML_00GOO0100137001103793597.
  - O PDF, o EPUB e as imagens de página estão em `ferramentas/cache/faltas/` (`t1894.*`, `img/`).
- **Por que a 6e (1894):** Tissot morreu em 1894. É a última edição revista pelo autor e a mais completa. No avant-propos, ele diz que nada retirou do texto anterior, acrescentou citações e introduziu as divisões de capítulos e os números de parágrafo.
- **Edições anteriores no Numelyo, consultadas para comparar e não usadas como base:**
  - 1ª edição, Poitiers/Paris, Oudin frères, 1879, cote SJ A 348/184: https://numelyo.bm-lyon.fr/f_view/BML:BML_00GOO0100137001103793555;
  - «deuxième édition revue, augmentée», Oudin frères / Annecy, Abry, 1880, cote SJ A 348/192: https://numelyo.bm-lyon.fr/f_view/BML:BML_00GOO0100137001103794058.

  Têm o mesmo texto de base, sem os números de parágrafo, em outra paginação.
- **Domínio público:** Tissot (1840–1894) está em domínio público.

## Como o texto foi estabelecido

1. **Dois OCRs** de cada página (págs. xi a 165): o do Numelyo/EPUB e o do Windows (`winocr.ps1`). Foram fundidos por alinhamento (`etapa2.py`, `fundir.py`, `etapa3.py`) e deram os rascunhos por página (`rascunhos.py`).
2. **Revisão integral, página por página, contra a imagem.** O resultado está em `revisado/001.txt` a `041.txt`, com a página, os parágrafos, as chamadas e as notas de cada página.
3. **Montagem** (`montar.py`). Para reproduzir:

   ```
   python montar.py
   ```

### O que foi limpo ou mudado

- **Retirados:** os cabeçalhos correntes, os números de página e as assinaturas de caderno.
- **Hifenização:** retirado o hífen de fim de linha. Os parágrafos partidos na virada de página foram unidos.
- **Notas do autor:**
  - No livro, a numeração recomeça em cada página; aqui, a chamada vira `[n]`, numerada em sequência dentro do arquivo.
  - A nota vem como `¤ [n] ...`, logo depois do parágrafo que a chama.
  - São 322 notas, todas com chamada. Na pág. 129 do livro, a chamada faltava no impresso e foi reposta.
- **Itálico** do livro marcado como `_..._`: títulos de obras, palavras latinas, ênfases.
- **Títulos dos capítulos:** na forma `## Chapitre N — Título`, com o título em caixa normal. No livro, estão em versalete.
- **Números de parágrafo:** os números «1. —», «2. —» são do autor (6e éd.) e ficaram.
- **Grafias do impresso mantidas:** *Evêques* sem acento na maiúscula; *A* por *À*; aspas francesas; apóstrofo reto.
- **Não incluídos:** são do editor ou de terceiros.
  - as «Lettres approbatives» (cardeal-vigário de Roma, cardeal Caverot, arcebispo de Chambéry etc.);
  - o imprimatur;
  - a página de rosto;
  - o índice.

  A epígrafe da página de rosto, *Misericordias Domini in æternum cantabo* (Ps. LXXXVIII), entra no começo de `00-avant-propos.txt`, antes do título, como parágrafo próprio (decisão da harmonização; `montar.py` a acrescenta).
- **Erros de impressão corrigidos:** cerca de 50, mais dois acertados na harmonização da tradução (*Puits-d'Ordre* → *Puits-d'Orbe*, nota da pág. 36; *disentils* → *disent-ils*, pág. 58–59, hífen perdido pela montagem na virada de página), todos registrados com a página em `ferramentas/cache/faltas/revisado/emendas.txt`. Exemplos:
  - *extraordiraire* → *extraordinaire*;
  - *pesque* → *presque*;
  - *Osannam* → *Ozanam*;
  - *Bernières-Souvigny* → *Bernières-Louvigny*.

  Quatro emendas são conjecturais ou incertas e estão marcadas como tais:
  - «dérouler» por «découler», na pág. 53;
  - «Passion.», na nota da pág. 50;
  - «Anoméens», na nota da pág. 60;
  - o fim da nota 3 da pág. 117.

  Referências erradas do impresso foram mantidas e anotadas: Gen. VI, 13 (é IV, 13); Luc III, 43; Job XXX, 33. A harmonização da tradução registrou as demais no fim do `emendas.txt` (Hebr. VI, 12; Eccl. XVII, 6; Prov. XXX, 13; Ps. LXVI, 11; Rom. VIII, 24; I Cor. XII, 9; Luc. VII, 48; Luc, VII, 35; Ps. LXXXIII; a numeração 1, 2, 2, 3, 5 do cap. VIII).

## Convenção das marcas

`[I.1]` = parte (romano) e capítulo (arábico), na divisão do autor. Fica no começo do primeiro parágrafo de cada capítulo.

- Primeira parte, 3 capítulos: `[I.1]`…`[I.3]`.
- Segunda parte, 8 capítulos: `[II.1]`…`[II.8]`.

O Avant-propos não tem marca.

## Contagens

Palavras contadas por espaços, sem cabeçalho, marcas e chamadas. «Parágrafos» = blocos de texto, sem títulos nem notas.

| arquivo | conteúdo | parágrafos | títulos `##` | marcas | notas | palavras (texto) | palavras (notas) |
|---|---|---:|---:|---:|---:|---:|---:|
| 00-avant-propos.txt | epígrafe do rosto e Avant-propos (1894) | 12 | 1 | 0 | 0 | 379 | 0 |
| 01-primeira-parte.txt | 1ª parte, cap. I–III (não se espantar, não se perturbar, não desanimar) | 110 | 3 | 3 | 99 | 10.471 | 896 |
| 02-segunda-parte-a.txt | 2ª parte, cap. I–IV (humildade, amor da própria abjeção, confiança) | 141 | 4 | 4 | 119 | 14.408 | 1.160 |
| 02-segunda-parte-b.txt | 2ª parte, cap. V–VIII (perseverança, fervor, satisfação, Virgem Maria) | 136 | 4 | 4 | 104 | 11.797 | 989 |
| **total** | | **399** | **12** | **11** | **322** | **37.055** | **3.045** |

## O texto pode ir ao lado da tradução?

Sim (`original_ao_lado = True`). Foi revisado inteiro contra a imagem.

## Problemas e dúvidas

1. **Remissões a páginas de outros livros e de edições antigas.**
   - «Voir le _Pouvoir de saint François de Sales_, page 284» remete a outra obra de Tissot.
   - «Pages 84 et 190», na nota 58 de `02-segunda-parte-b.txt`, remete à paginação de uma edição anterior: nesta, o livro tem 165 páginas.

   Na tradução, as duas ficaram: a segunda como «Páginas 84 e 190», com uma nota «[Trad.: ...]» que indica os lugares prováveis (I, cap. III, n.º 7, e II, cap. IV, n.º 2, em nota).
2. **Citações de São Francisco de Sales:** Tissot cita as cartas pela numeração da coleção Blaise («Lettre 793e ; collect. Blaise») e o *Esprit* de Camus. Essas referências se traduzem como estão. Não há equivalência com a numeração de Annecy.
3. **Remissões à Filoteia:** muitas citações são da *Introduction à la vie dévote*, que a Biblioteca também vai traduzir. Na harmonização, essas passagens seguiram a redação da nossa Filoteia, ajustada ao texto que Tissot cita; as dos capítulos III.1–13, ainda em tradução, ficaram listadas em `../traducao/HARMONIZACAO.md` para conferir depois.
