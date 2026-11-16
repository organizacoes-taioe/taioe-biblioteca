# Apologia pro Vita Sua (Newman): o que está feito e o que falta

Branch `pedido-apologia-newman`. Leia antes: `CONVENCOES.md`, `original/LEIAME.md`, e os modelos de tom
`traducao/00-prefacio.txt` e `traducao/01-capitulo-1.txt` (com `traducao/notas-*.md`).

## Feito (2026-11-16, preparador)

- Original inglês (Gutenberg #22088, Longmans 1890, forma final) em 21 arquivos, por `original/montar.py`.
- `obra.py` (META, apresentação, PARTES) e o autor `sao-john-henry-newman` em `conteudo/autores.js`.
- `CONVENCOES.md` (tratamento, termos, Oxford, nomes, títulos, latim, datas, a Nota D).
- Traduzidos: o prefácio inteiro e o capítulo I até o parágrafo 20.

## Arquivos

Palavras do original (sem cabeçalho); parágrafos contam as notas do autor (`¤`).

| arquivo | parágrafos | palavras | situação |
|---|---:|---:|---|
| 00-prefacio.txt | 44 | 6.657 | traduzido |
| 01-capitulo-1.txt | 68 | 11.911 | traduzido (lote 1) |
| 02-capitulo-2a.txt | 37 | 9.499 | traduzido (lote 1) |
| 03-capitulo-2b.txt | 88 | 9.353 | traduzido (lote 1) |
| 04-capitulo-3a.txt | 53 | 9.015 | por traduzir |
| 05-capitulo-3b.txt | 84 | 9.672 | por traduzir |
| 06-capitulo-4a.txt | 66 | 10.151 | por traduzir |
| 07-capitulo-4b.txt | 94 | 12.006 | por traduzir |
| 08-capitulo-4c.txt | 101 | 9.227 | por traduzir |
| 09-capitulo-5a.txt | 34 | 10.891 | por traduzir |
| 10-capitulo-5b.txt | 49 | 4.958 | por traduzir |
| 11-nota-a.txt | 59 | 3.952 | traduzido (lote 1) |
| 12-nota-b.txt | 30 | 3.744 | por traduzir |
| 13-nota-c.txt | 27 | 4.646 | por traduzir |
| 14-nota-d.txt | 128 | 4.777 | por traduzir (calendário: CONVENCOES § 8) |
| 15-nota-e.txt | 4 | 1.355 | por traduzir |
| 16-nota-f.txt | 12 | 1.410 | por traduzir |
| 17-nota-g.txt | 49 | 5.055 | por traduzir |
| 18-carta-do-bispo.txt | 18 | 1.413 | por traduzir |
| 19-cartas-do-clero-e-leigos.txt | 98 | 2.961 | por traduzir |
| 20-notas-adicionais.txt | 100 | 6.337 | por traduzir |
| **total** | | **138.990** | traduzidas 8.906; faltam **130.084** |

## Proposta de lotes (4 tradutores em paralelo, ~32 mil palavras cada)

| lote | arquivos | palavras |
|---|---|---:|
| 1 | `01-capitulo-1.txt` (§§ 21–68, acrescentando ao arquivo já começado), `02-capitulo-2a.txt`, `03-capitulo-2b.txt`, `11-nota-a.txt` (o liberalismo, citada no cap. I) | 32.466 |
| 2 | `04-capitulo-3a.txt`, `05-capitulo-3b.txt`, `06-capitulo-4a.txt`, `12-nota-b.txt` (milagres) | 32.582 |
| 3 | `07-capitulo-4b.txt`, `08-capitulo-4c.txt`, `13-nota-c.txt` (o sermão), `14-nota-d.txt` (as vidas dos santos, citada no cap. IV), `19-cartas-do-clero-e-leigos.txt` | 33.617 |
| 4 | `09-capitulo-5a.txt`, `10-capitulo-5b.txt`, `15-nota-e.txt`, `16-nota-f.txt` (a economia), `17-nota-g.txt` (a mentira), `18-carta-do-bispo.txt`, `20-notas-adicionais.txt` | 31.419 |

Cada tradutor grava `traducao/notas-<arquivo>.md`, commita e dá push a cada arquivo, e anota aqui o que terminou.
Termos novos que valham para o livro todo: propor nas notas e na lista abaixo (o guia só muda pelo principal).

## Depois da tradução (principal)

- `revisao.json` com as ~8 decisões delicadas para o Gere. Candidatas: _Untruthfulness_ → «falta de veracidade»;
  _equivocation_ → «equívoco»; _Establishment_ → «Igreja estabelecida»; Fellow/Tutor/Provost em inglês; _my
  Accuser_ com maiúscula; títulos das obras inglesas sem tradução; a omissão dos suplementos I e II (abaixo); o título
  da Nota G («A mentira e o equívoco»).
- `edicoes/vocabulario/apologia-newman.json` (regra do vocabulário: livro novo em português) e as notas gerais na fila.
- `python3 ferramentas/traducoes.py apologia-newman`. Formato conferido em 16/11 com cópias provisórias do original
  no lugar das traduções que faltam: 21 partes aceitas, original e tradução alinhados. **Atenção:** o script só
  confere se o arquivo existe; o `01-capitulo-1.txt` já existe com 20 de 68 parágrafos, então conferir a contagem
  de parágrafos de todos os arquivos antes de publicar.

## Dúvidas (com sugestão)

1. **Suplementos I e II** (lista cronológica das cartas citadas, com as páginas de 1890; lista das obras do autor):
   ficaram fora do original. Sugestão: manter fora (aparato da edição inglesa, sem uso no site); se o Gere quiser, a
   lista de obras entra fácil como arquivo 18a (o `montar.py` já tem o ponto de corte).
2. **Remissões a páginas da edição inglesa** («Note A, on page 14», «p. 228», «Vide supr. p. 219»): mantidas como
   no original, sem ajuste. Sugestão: manter (a apresentação avisa); a alternativa seria trocar por remissão ao
   capítulo, o que é acréscimo nosso.
3. **Capítulo IV em 3 partes** com o «§ 2.» do autor no meio da 2ª: o corte em § 2 daria uma parte de 15 mil
   palavras. Sugestão: manter assim.

## Lote 1 (2026-11-16): dúvidas para o principal

4. **`03-capitulo-2b.txt`, §§ 74–76**: no impresso são a continuação da nota do autor [2] (desafio aos evangélicos e
   as duas fórmulas de absolvição), mas o `montar.py` os deixou no corpo. Original e tradução estão iguais (88
   parágrafos). Sugestão: juntá-los ao `¤ [2]` nos dois arquivos de uma vez.
5. **`[Greek: …]`** (cap. I § 55, cap. II-a §§ 27 e 35, Nota A § 56): ficaram como no Gutenberg. Sugestão: trocar
   pelo grego (δαιμόνια; τῷ τέλει πίστιν φέρων; ὁ μέγας; α, β, γ, δ, ε, ζ) no original e na tradução.
6. **Versos ingleses de um verso só**, citados na frase (cap. I §§ 35, 53, 60, 61; cap. II-a §§ 22, 34; Nota A § 57):
   ficaram em prosa literal entre aspas, sem `| `; lista em `traducao/notas-*.md`. Sugestão: deixar assim.
7. _Charge_ (carta pastoral do bispo) → «_Charge_», em itálico: proposta para o livro todo.
