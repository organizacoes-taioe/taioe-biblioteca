# A alma de todo apostolado, de Dom Chautard: texto francês de trabalho

Arquivos: `00-preludio.txt` a `06-epilogo.txt`. São 11 arquivos em UTF-8, com cabeçalho `# chave: valor` e parágrafos separados por uma linha em branco. Nada foi traduzido.

O texto foi estabelecido por nós a partir de um scan. Não há transcrição digital confiável disponível.

## Fonte e edição

- **Edição de base:** *L'Âme de tout apostolat*, «douzième édition (150e mille)».
  - Abbaye de Sept-Fons, par Dompierre-sur-Besbre (Allier); Lyon, Em. Vitte; Paris, P. Téqui, 1927.
  - O autor assina «Dom J.-B. Chautard, O.C.R.».
  - Imprimatur de Moulins, 2 de agosto de 1912; cartas de aprovação do cardeal Arcoverde, de Mgr Penon e do abade-geral dos cistercienses reformados.
- **Scan:** Internet Archive, identificador `lamedetoutaposto0000unse`, https://archive.org/details/lamedetoutaposto0000unse. É o exemplar da Graduate Theological Union Library, digitalizado em 2025.
  - O PDF (`ia1927.pdf`) e o OCR do próprio Internet Archive (`ia1927_djvu.xml`) estão em `ferramentas/cache/alma/`.
- **Segundo testemunho, só para conferência:** OCR da 15e édition, Internet Archive `l-ame-de-tout-apostolat-000001218`, https://archive.org/details/l-ame-de-tout-apostolat-000001218. Arquivos `iaX.txt` e `iaX_djvu.xml`.
  - A paginação dessa edição é outra; a composição é quase idêntica.
  - Serviu para votar palavras duvidosas e para ler notas de rodapé mal impressas no scan de 1927.
  - Nenhuma lição da 15e entrou no texto sem ser confirmada na imagem de 1927.
- **Domínio público:** Chautard morreu em 1935, e a obra está em domínio público no Brasil e na França.

### Por que a 12e édition, e não a primeira

O pedido era a edição completa mais antiga disponível livremente. A história do livro, como ele mesmo a deixa ver, é esta:

- Houve um primeiro exposto, mais curto. A carta de Mgr Penon fala do «premier exposé de votre thèse fondamentale».
- Depois veio a forma definitiva, com o título atual e imprimatur de 1912. O autor continuou a ampliá-la. Exemplos:
  - O capítulo IV.1 e) diz de si mesmo «ce chapitre ajouté aux premières éditions».
  - A seção IV.1 f) cita *L'Ami du Clergé* de 20 de janeiro de 1921.
  - A 2ª parte fala da «guerre qui sévit en ce moment».

Nas buscas feitas, não achamos digitalização livre das primeiras edições (1907–1912) nem da primeira edição com o título atual. A de 1927 é a mais antiga que achamos em scan completo e legível, já com o texto ampliado: 292 páginas, Prélude, cinco partes e Épilogue, conforme o índice do próprio livro, que foi conferido.

Edições dos anos 1930 (a 15e e seguintes) podem trazer retoques. A comparação palavra a palavra com o OCR da 15e mostrou o mesmo texto, salvo a paginação, mas não foi feita uma colação sistemática de variantes.

## Como o texto foi estabelecido

1. **Páginas do PDF 16 a 309** (págs. 1 a 292 do livro, mais a prancha fora de texto): cada página foi rasterizada e passou pelo OCR do Windows (`img/iNNN.png.json`).
2. **Votação palavra a palavra** entre três OCRs: Windows, Internet Archive do mesmo scan e Internet Archive da 15e. Foi feita por alinhamento (`etapa1.py`, `etapa2.py`), com um dicionário francês e o vocabulário dos outros dois textos já limpos da Biblioteca. Saíram as páginas `base/NNN.txt`. As notas de rodapé foram trocadas pela leitura da 15e quando havia correspondência segura (`notas_x.py`).
3. **Revisão integral, página por página, contra a imagem** (`rev/NNN.png`).
   - As correções estão em `revisado/patches-001.txt` a `patches-054.txt`: substituições exatas, conferidas por `aplicar.py`, que acusa qualquer correção que não case exatamente uma vez.
   - As páginas reescritas por inteiro estão em `revisado/full/`.
   - O resultado são as páginas `final/NNN.txt`.
4. **Montagem** (`montar.py`): junta as páginas, os parágrafos partidos na virada de página e as notas. Divide em arquivos e põe as marcas. Para reproduzir:

   ```
   python aplicar.py && python montar.py -v
   ```

   A opção `-v` lista as hifenizações de fim de página resolvidas.

### O que foi limpo ou mudado

- **Retirados:**
  - os cabeçalhos correntes («L'AME DE TOUT APOSTOLAT»), os números de página e as assinaturas de caderno («12e-16»);
  - o hífen de fim de linha, salvo nos compostos (*Notre-Seigneur*, *c'est-à-dire*);
  - os erros de OCR (centenas por página nas notas, poucos no corpo).
- **Notas do autor:**
  - No livro, a numeração recomeça em cada página; aqui, a chamada vira `[n]`, numerada em sequência dentro do arquivo.
  - A nota vem como parágrafo `¤ [n] ...` logo depois do parágrafo que a chama. É o mesmo formato do Tissot e o que `js/app.js` reúne no fim da parte.
  - Quando a nota tem mais de um parágrafo, os seguintes vêm como `¤ ...`, sem número.
  - Notas que no livro continuam no pé da página seguinte foram unidas.
  - Na pág. 168 do livro, duas chamadas «(1)» remetem à mesma nota (Ps. XXXVI); as duas ficaram com o mesmo número.
  - As notas longas foram mantidas inteiras: a lista de livros sobre direção espiritual, as «dix manières» do P. Rigoleuc, o «Apostolat ou scandale» etc.
- **Títulos:** todos começam com `## `: partes, capítulos (1., 2. ...), seções (a), b) ... e I., II. ...), as nove classes de almas da direção espiritual, «Convictions», «Principes», «Video», «Sitio» etc.
- **Separação de trecho:** o asterismo do autor (`* * *`) virou `## * * *`.
- **Prancha:** a prancha fora de paginação, entre as págs. 50 e 51, foi para o fim de `06-epilogo.txt`, depois do Épilogue que a comenta. Ela traz a «gravure byzantine» com o título «Regina Apostolorum», a legenda latina em quatro saudações («Salve...») e a nota sobre a Panaghia Parthenos. No lugar original, ela cortaria um parágrafo ao meio.
- **Não incluídos:** são peças de terceiros ou do editor, não do autor.
  - o anúncio «Cet ouvrage peut servir...»;
  - a legenda do frontispício (Eugênio III recebe o *De Consideratione*);
  - as cartas de aprovação, o *nihil obstat* e o imprimatur;
  - o índice (págs. 293–295).

  **Atenção:** a página de rosto traz a epígrafe «Jésus doit être la Vie de mes œuvres. Sinon... (Card. Mermillod)». Ela também ficou fora. Convém decidir se entra na tradução, no começo do Prélude.
- **Mantidos como no impresso:**
  - A grafia sem acento nas maiúsculas: *Eglise*, *Evangile*, *Ecriture*, *A* por *À*, *MEME* em versalete.
  - O *Etats-Unis* e as aspas francesas.
  - O apóstrofo reto.
  - As maiúsculas de reverência: *Vous*, *Votre* dirigidos a Deus no Prélude; *Lui*, *Elle* (Maria) etc.
- **Itálico:** **não foi marcado.** O OCR não o distingue, e marcá-lo à mão em 292 páginas ficou fora do escopo. Os trechos latinos e as citações estão em itálico no livro, e o tradutor deve tratá-los como tais. Em caso de dúvida sobre o grifo de uma frase francesa, convém ver o scan.
- **Versalete:**
  - No corpo, palavras em versalete viraram maiúsculas: *MULTIPLIER*, *PAR L'EXEMPLE*, *SCANDALE*. São ênfase do autor.
  - Nas notas, os nomes de autor em versalete aparecem ora em maiúsculas («S. AUG.»), ora em caixa normal («S. Aug.»). Na tradução, convém padronizar.

### Erros de impressão corrigidos

O registro está em `ferramentas/cache/alma/revisado/emendas.txt`. Nas páginas anteriores à 168 do livro, as poucas gralhas evidentes foram corrigidas na revisão sem registro individual; a partir dela, cada uma foi anotada. Exemplos:

- *catholiqnes* → *catholiques*;
- na nota da pág. 179: *Saudrau* → *Saudreau*, *Schievers* → *Schrijvers*;
- na nota da pág. 213: *vertus infuse* → *vertus infuses*.

Referências bíblicas e remissões internas ficaram como no impresso, mesmo quando o lugar exato é outro. Exemplo: «Is., LII, 12» para Is 52,11.

## Convenção das marcas

`[I.1]` = parte (romano) e capítulo (arábico), na numeração do autor. Fica no começo do primeiro parágrafo de cada capítulo.

| Parte | Capítulos | Marcas |
|---|---|---|
| Première partie | 7 | `[I.1]`…`[I.7]` |
| Deuxième partie | 5 | `[II.1]`…`[II.5]` |
| Troisième partie | 3 | `[III.1]`…`[III.3]` |
| Quatrième partie | um só capítulo, com as seções a) a g) | `[IV.1]` |
| Cinquième partie | 5 | `[V.1]`…`[V.5]` |

O Prélude, o Épilogue e a prancha não têm marca. Dois arquivos não começam capítulo e por isso não têm marca: `04-quarta-parte-b.txt` (IV.1, seções d) a g)) e `05-quinta-parte-c.txt` (V.3, seções IV e V). Neles, os títulos `## ` servem de âncora.

## Contagens

Palavras contadas por espaços, sem cabeçalho, marcas e chamadas. «Parágrafos» = blocos de texto, sem títulos nem notas. «Notas» = notas numeradas; os parágrafos de continuação contam nas palavras.

| arquivo | parágrafos | títulos `##` | marcas | notas | palavras (texto) | palavras (notas) |
|---|---:|---:|---:|---:|---:|---:|
| 00-preludio.txt | 18 | 3 | 0 | 3 | 578 | 23 |
| 01-primeira-parte.txt | 156 | 9 | 7 | 48 | 9.838 | 939 |
| 02-segunda-parte.txt | 82 | 7 | 5 | 40 | 4.929 | 971 |
| 03-terceira-parte.txt | 124 | 11 | 3 | 44 | 9.224 | 1.163 |
| 04-quarta-parte-a.txt | 120 | 6 | 1 | 59 | 9.212 | 706 |
| 04-quarta-parte-b.txt | 158 | 16 | 0 | 20 | 10.994 | 788 |
| 05-quinta-parte-a.txt | 96 | 20 | 2 | 20 | 4.303 | 2.182 |
| 05-quinta-parte-b.txt | 107 | 13 | 1 | 46 | 5.955 | 2.303 |
| 05-quinta-parte-c.txt | 99 | 12 | 0 | 26 | 5.120 | 752 |
| 05-quinta-parte-d.txt | 95 | 8 | 2 | 17 | 5.451 | 740 |
| 06-epilogo.txt | 15 | 2 | 0 | 0 | 541 | 0 |
| **total** | **1.070** | **107** | **21** | **323** | **66.145** | **10.567** |

O que cada arquivo cobre:

| arquivo | conteúdo | págs. do livro |
|---|---|---|
| `00-preludio.txt` | Prélude (oração à Trindade e ao Espírito Santo) | 1–3 |
| `01-primeira-parte.txt` | I. Dieu veut les Œuvres et la Vie intérieure, cap. 1–7 | 4–46 |
| `02-segunda-parte.txt` | II. Union de la Vie active et de la Vie intérieure, cap. 1–5 | 47–69 |
| `03-terceira-parte.txt` | III. La Vie active dangereuse sans la Vie intérieure..., cap. 1–3, com a)–f) | 70–108 |
| `04-quarta-parte-a.txt` | IV. Fécondité des Œuvres par la Vie intérieure, a)–c) | 109–148 |
| `04-quarta-parte-b.txt` | IV, d)–g) (eloquência, vida interior que gera vida interior, elites e direção espiritual, Eucaristia) | 148–194 |
| `05-quinta-parte-a.txt` | V. Quelques Principes et Avis pour la Vie intérieure, cap. 1 (conselhos) e 2 (oração) | 195–216 |
| `05-quinta-parte-b.txt` | V.3, Vida litúrgica, I–III | 217–245 |
| `05-quinta-parte-c.txt` | V.3, IV–V | 245–267 |
| `05-quinta-parte-d.txt` | V.4, Guarda do coração; V.5, Devoção a Maria Imaculada | 268–290 |
| `06-epilogo.txt` | Épilogue; prancha «Regina Apostolorum» | 291–292 |

## O texto pode ir ao lado da tradução?

Sim (`original_ao_lado = True`). Ele foi revisado inteiro contra a imagem, e o que falta é só o itálico.

## Problemas e dúvidas

1. **Não é a primeira edição.** É a 12e (1927), com o texto já ampliado (ver acima). As primeiras edições não foram achadas em acesso livre.
2. **Itálico não marcado** (ver acima).
3. **Remissões internas** à paginação desta edição: «Voir note, page 17», «indiqués pag. 60», «2e partie, chap. II, pag. 56», «cité page 77». Na tradução, convém trocar por remissão a capítulo ou retirar o número da página, com registro nas notas.
4. **Notas em latim longas**, sem tradução do autor: Pio X, *Exhortatio ad clerum*; De Lugo; Pedro Damião; Bossuet etc. Decidir se se traduzem (sugestão: traduzir, mantendo o latim só quando o autor o deixa sem tradução no corpo).
5. **Epígrafe de Mermillod e cartas de aprovação** ficaram fora (ver acima).
6. A prancha mudou de lugar (ver acima).
7. **Notas e a 15e:** nas notas de rodapé, em corpo pequeno e com o OCR mais fraco, a leitura da 15e serviu de rascunho. Toda nota foi conferida na imagem de 1927. Onde as duas edições divergem, vale a de 1927; é o caso de «cité page 77» na de 1927 contra «page 75» na 15e.
