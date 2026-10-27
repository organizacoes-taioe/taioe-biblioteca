# Os Lusíadas: convenções da edição

Texto da 1ª edição (1572) na grafia brasileira de hoje. Montagem em `montar.py` (o passo a passo está
no começo do arquivo); fontes em `ferramentas/cache/os-lusiadas/` (fora do git).

## Lição

- Vale a 1ª edição (Gutenberg 27236). O Wikisource dá a pontuação, a quebra dos versos e a grafia.
- Erro evidente de 1572 (ſ por f, n por u, letra trocada, palavra repetida) → corrige-se, e entra na
  lista «Erros da 1ª edição corrigidos» da página «Sobre».
- Dúvida entre as duas → a rima da oitava decide (`rimas.py`); sem rima, fica 1572.
- O Wikisource tem erros próprios: «o» por «e» (18 vezes), «amigo» por «imigo», «faina», «inundo»,
  «Rene», «vale», «terrestre», quebras de verso erradas em X,13 e X,94 (`linhas.json`).

## Grafia (decisão do Gere, 27/10/2026: «mantenha as formas antigas que mudam o número de sílabas (imigo, pera etc.)»)

- Muda só a maneira de escrever: ſ, u/v, i/j, y, ph/th/ch, letras dobradas, h mudo, til (hũa → uma,
  -ão/-am), ct/pt mudos, acentos do Acordo de 1990 na norma brasileira (Netuno, Vênus, Europeias, veem).
- A forma da palavra fica: pera, polo, imigo, despois, fermoso, milhor, dous, cousa, inda, mui, assi,
  mi, quási, baxo, pexe, sospeita, sojeito, cubiça, custume, insinar, menhã, reposta, lião, dões.
- Exceções, tratadas como grafia: antigua → antiga; fea/chea/area → feia/cheia/areia.
- Contrações: co'o, co'a, co'os, co'as, c'um, c'uma; «co» só antes de pronome (co ele, co isto).
  Elisões com apóstrofo: d'alta, d'esforço, n'água.
- Sprito → esprito (duas sílabas).

As escolhas acima que estão em `revisao.json` esperam a resposta do Gere em /admin/pendencias/.
