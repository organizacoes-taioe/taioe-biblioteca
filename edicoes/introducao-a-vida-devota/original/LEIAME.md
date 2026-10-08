# Introdução à vida devota (Filoteia), de São Francisco de Sales: texto francês de trabalho

Arquivos: `00-oracao-e-prefacio.txt` a `05-quinta-parte.txt`. São 8 arquivos em UTF-8, com cabeçalho `# chave: valor` e parágrafos separados por uma linha em branco. Nada foi traduzido.

## Fonte e edição

- **Texto pedido: o de 1619.** É a «dernière édition, revue, corrigée et augmentée par l'Autheur» (Paris, Joseph Gottereau, 1619), a última revista pelo santo. A primeira edição saiu em Lyon no fim de 1608, com data de 1609. O texto foi muito ampliado em 1609–1610 e retocado até 1619.
- **Edição de base:** *Introduction à la vie dévote*, texte intégral publié d'après l'édition de 1619, par l'abbé Fernand Boulenger (Paris, Vve Ch. Poussielgue, 1909).
  - Boulenger reproduz o texto de 1619 com a **ortografia modernizada**. Mantém o vocabulário e a sintaxe do século XVII: *ès*, *icelui*, *meshui*, *ains*, *voirement*.
- **Fonte digital:** Wikisource em francês, «Introduction à la vie dévote (Boulenger)», página «Texte entier», https://fr.wikisource.org/wiki/Introduction_%C3%A0_la_vie_d%C3%A9vote_(Boulenger)/Texte_entier.
  - É uma transcrição feita sobre o fac-símile da edição de 1909, o arquivo «De Sales - Introduction à la vie dévote, 1619, édition Boulenger, 1909.pdf».
  - A página bruta está em `ferramentas/cache/filoteia/entier.html`.
- **Conferência:** *Œuvres de saint François de Sales*, Édition complète (dita «d'Annecy»), t. III, *Introduction à la vie dévote* (Annecy, 1893), no Internet Archive: https://archive.org/details/oeuvresdesaintfr03fran.
  - Usamos o OCR (`annecy3.txt`) só para conferir. O aparato crítico de Annecy não foi usado nem copiado.
  - Annecy dá o texto de 1619 com a grafia original.

### Conferência com Annecy (1893)

O script `colacao.py` normaliza a grafia dos dois lados do mesmo jeito: tira acentos e consoantes dobradas, reduz *oi*/*ai*, *y*/*i* etc. Depois procura trechos de 8 palavras ou mais de um lado sem par no outro.

- **Do lado de Boulenger,** não há trecho sem par que não se explique por diferença de grafia. **Não há omissões.**
- **Do lado de Annecy,** o que sobra (`colacao.out`) é aparato crítico: variantes dos manuscritos e das edições de 1609–1616, notas e cabeçalhos do volume.
- Duas lições de pontuação de Boulenger, que encerravam com vírgula um parágrafo terminado em ponto, foram corrigidas por Annecy (`CORRECOES` em `preparar.py`):
  - «comme vaines et superflues.»
  - «car Dieu n'en est point offensé.»

## O que foi limpo

O script é `ferramentas/cache/filoteia/preparar.py`. Para reproduzir:

```
python preparar.py
```

- **Retirados:**
  - as notas de rodapé de Boulenger, que são glosas de vocabulário («meshui : désormais» etc.) e não do autor;
  - o léxico do fim do volume e o estudo introdutório de Boulenger;
  - as chamadas de nota e os números de página do Wikisource;
  - os filetes («______») e o «FIN».
- **Itálico** do Wikisource conservado como `_..._`. Isso inclui os subtítulos internos das meditações (*Préparation*, *Considérations*, *Affections et résolutions*, *Conclusion*, *Faites un bouquet...*), que ficaram como parágrafos próprios, em itálico, como no livro.
- **Sumários das partes:** o sumário de cada parte («_Contenant les avis et exercices..._») abre o arquivo da parte, como parágrafo em itálico.
- **Versalete** convertido em maiúsculas («VIVE JÉSUS»).
- **Versos** citados com `| `, um por linha. São dois dísticos:
  - «En son beau vêtement de drap d'or recamé...», em III.1;
  - «A cause des biens que j'attends...», em V.18.

  Na tradução, vão em verso pelo método do Versificador.
- **Títulos de capítulo** no formato `## Chapitre N — Título`, com o título por extenso tirado do índice do livro.
  - Os números de parágrafo das meditações («1.», «2.» ...) são do autor e ficaram.
- **Apóstrofo:** o apóstrofo reto que sobrava em 22 lugares virou tipográfico (’), como no resto do texto.
- Nada foi modernizado além do que Boulenger já modernizara.

## Convenção das marcas

`[I.1]` = parte (romano) e capítulo (arábico), na numeração do autor. Fica no começo do primeiro parágrafo de cada capítulo.

| Parte | Capítulos | Marcas |
|---|---:|---|
| Primeira | 24 | `[I.1]`…`[I.24]` |
| Segunda | 21 | `[II.1]`…`[II.21]` |
| Terceira | 41 | `[III.1]`…`[III.41]` |
| Quarta | 15 | `[IV.1]`…`[IV.15]` |
| Quinta | 18 | `[V.1]`…`[V.18]` |

A Oraison dédicatoire e a Préface não têm marca.

Não há notas do autor nesta edição; por isso o arquivo não tem `[n]` nem `¤`.

## Contagens

Palavras contadas por espaços, sem cabeçalho, marcas e prefixos.

| arquivo | conteúdo | parágrafos | títulos `##` | marcas | palavras |
|---|---|---:|---:|---:|---:|
| 00-oracao-e-prefacio.txt | Oraison dédicatoire; Préface | 13 | 2 | 0 | 1.990 |
| 01-primeira-parte.txt | 1ª parte, cap. I–XXIV | 208 | 24 | 24 | 13.705 |
| 02-segunda-parte.txt | 2ª parte, cap. I–XXI | 105 | 21 | 21 | 14.105 |
| 03-terceira-parte-a.txt | 3ª parte, cap. I–XIII | 90 | 13 | 13 | 15.453 |
| 03-terceira-parte-b.txt | 3ª parte, cap. XIV–XXVII | 89 | 14 | 14 | 13.155 |
| 03-terceira-parte-c.txt | 3ª parte, cap. XXVIII–XLI | 101 | 14 | 14 | 14.482 |
| 04-quarta-parte.txt | 4ª parte, cap. I–XV | 89 | 15 | 15 | 13.472 |
| 05-quinta-parte.txt | 5ª parte, cap. I–XVIII | 81 | 18 | 18 | 7.018 |
| **total** | | **776** | **121** | **119** | **93.380** |

## O texto pode ir ao lado da tradução?

Sim (`original_ao_lado = True`). É uma transcrição do Wikisource sobre fac-símile, conferida com Annecy.

## Problemas e dúvidas

1. **Ortografia de Boulenger.** A ortografia modernizada é obra do editor, o abade Fernand Boulenger. Não verificamos a data da morte dele. Uma simples atualização de grafia de um texto em domínio público dificilmente gera direito autoral, mas, se o Gere preferir eliminar o risco, o caminho é Annecy (1893), com a grafia de 1619. Nesse caso, o texto teria de ser preparado de novo a partir do OCR de Annecy, com bem mais trabalho. Não usamos nada mais de Boulenger: nem estudo, nem notas, nem léxico.
2. **Wikisource:** a transcrição pode conter erros pontuais. A conferência com Annecy pega omissões e acréscimos, não erros de uma letra.
3. **Arquivos longos:** os arquivos da 3ª parte têm entre 13 e 15,5 mil palavras. Convém dividir a tradução por capítulos, se preciso.
