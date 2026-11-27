# Diário Íntimo (Lima Barreto): estado (2026-11-27)

Literatura, autor `lima-barreto` (já existia), gênero «Diário», `datas: 1900–1921`, `ano: 1953` (1ª publicação).
**Pronto.** 18 partes (anos; 1906–07, 1912–15 e 1920–21 juntos; a 1ª versão de *Clara dos Anjos*, 1904, nas 4 últimas),
~58 mil palavras; vocabulário com 128 verbetes (`conferir` ok); 5 decisões em `revisao.json`. Fora: notas gerais (fila dos lotes).

## Gravar `conteudo/` (na raiz do repositório)
```
python3 -I edicoes/diario-intimo/montar.py --publicar     # grava conteudo/lima-barreto/diario-intimo.js e a linha do index.html
node ferramentas/site/gerar.mjs && node ferramentas/site/conferir.mjs
```

## Fontes (fora do git, em /mnt/arquivos/claude-tmp/pedidos-2711b/diario-intimo/; baixar de novo se sumirem)
- Base: *Obras de Lima Barreto*, vol. XIV (Brasiliense, 1956), fac-símile no Internet Archive
  `barreto-l.-diario-intimo_202302` (`ia/1956.pdf`, 310 p.; página impressa ≈ PDF + 3) e o OCR dele (`ia/b.txt`, o `_djvu.txt`).
  Segunda leitura nossa: `tesseract.py ia/1956.pdf tess 1-310` (TSV + PNG a 300 dpi por página).
- Ponto de partida: a transcrição da Fundação Biblioteca Nacional (2002) na Cervantes Virtual (espelho
  letrasdehonduras.com, sem Cloudflare: `…/obra-visor/diario-intimo--0/html/ffcf0106-82b1-11df-acc7-002185ce6064_{2,3,4}.html`),
  extraída por `extrair_bn.py` para `fontes/bn2002.txt` (no git; é o texto sobre o qual correm as correções).
  O Wikisource (página indicada no pedido) é a mesma transcrição, colada de um PDF, sem divisão: não foi usado.

## Como foi feito
- `colacao.py ia/b.txt tess colacao.tsv`: palavra a palavra, 2002 × as duas leituras de 1956 (cabeços tirados).
  `pontuacao.py` (a pontuação depois de cada palavra), `italico.py` (inclinação das letras; roda com
  `~/.venvs/diagramador/bin/python3`, que tem numpy). `conferir.py` faz as pranchas para olhar nas imagens.
- Toda decisão está em `correcoes.tsv` (bloco de `bn2002.txt`, posição, de, para, motivo): `1956` = lição de 1956
  reposta; `erro1956` = erro do impresso de 1956 (bloco `-`: só vai à lista da «Sobre»). Regras gerais em
  `montar.pontuacao_1956` («?». → «?», «etc., etc.» → «etc. etc.», «III.-» → «III —»).
- Grafia: `edicao.grafia.ao1990` palavra a palavra + `HIFEN` (semi-, anti-, contra-…) e `FICA` (Méier, Raul Pompéia);
  citações em outras línguas não passam pelo Acordo.
- Fica de fora o que é do organizador: prefácio (Gilberto Freyre), nota prévia, notas de cada ano e as chamadas,
  «Sem data», o subtítulo «Primeira versão incompleta». Ficam as marcas de leitura dele ([...], [ilegível], [?], C...).

## O que não ficou conferido
- Só se olharam nas imagens os pontos em que as duas leituras de 1956 concordavam contra 2002; onde uma leitura de 1956
  errou, uma diferença de 2002 pode ter passado.
- Pontuação: conferidos só ~80 pontos (as trocas de sinal); 1956 tem mais vírgulas que 2002 em vários lugares e isso
  não foi revisto um a um. Aspas «» como nos outros livros (1956 usa “”).
- Itálicos: os de 2002 mais 19 achados pela inclinação; outros podem faltar (nomes de jornais, palavras estrangeiras).
- Tabelas (orçamentos, idades de Gonzaga de Sá, Clara dos Anjos) viram linhas com « — » entre as colunas.
- Vocabulário (Sonnet) menos seguro: trepar (gíria dos estudantes), consignação (dois sentidos num verbete), ganchos, mó.

## Direitos (para o advogado)
Texto de Lima Barreto (†1922): livre. A seleção, a ordem das notas sem data e a inclusão dos esboços e da 1ª versão
de *Clara dos Anjos* são do organizador, Francisco de Assis Barbosa (†1991): podem ser protegidas como compilação
(Lei 9.610, art. 7º, XIII) até 2062. Não há como refazer pelos manuscritos (BN, Coleção Lima Barreto) daqui.
A FBN publicou o mesmo texto em 2002 como livre. Decisão nas pendências (`organizador`).
