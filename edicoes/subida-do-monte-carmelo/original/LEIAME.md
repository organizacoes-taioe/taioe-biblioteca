# Texto espanhol da _Subida del Monte Carmelo_ (e da _Noche oscura_)

## Fonte

P. Silverio de Santa Teresa, C. D., _Obras de San Juan de la Cruz, Doctor de la Iglesia_, t. II: _Subida y Noche
oscura_ (Burgos, Tipografía de «El Monte Carmelo», 1929; Biblioteca Mística Carmelitana, 11). Em domínio público
(Silverio morreu em 1954; a edição tem 97 anos). Fac-símile no Internet Archive:
https://archive.org/details/obrasdesanjuande02john (outra digitalização do mesmo exemplar:
`BMC11ObrasDeSanJuanDeLaCruzTomoIISubidaYNocheOscura`).

Divisão e títulos de Silverio: Subida = argumento, canções, prólogo e 3 livros (15, 32 e 45 capítulos); Noite =
declaração, prólogo, canções e 2 livros (14 e 25 capítulos). Os capítulos I do livro II e do livro III da Subida não
têm título na edição (ficam «## 1.»).

## Arquivos

| arquivo | conteúdo | páginas de 1929 |
|---|---|---|
| `0-argumento-e-prologo.txt` | argumento, canções, prólogo | 3–11 |
| `1-livro-primeiro.txt` | livro I, cap. 1–15 | 12–66 |
| `2-livro-segundo-a.txt` / `-b` / `-c` | livro II, cap. 1–12 / 13–21 / 22–32 | 66–238 |
| `3-livro-terceiro-a.txt` / `-b` | livro III, cap. 1–23 / 24–45 | 239–362 |
| `../../noite-escura/original/*.txt` | a Noite (mesmo método, mesmo script) | 363–512 |

## Método (`montar.py`, `emendas.py`)

`python3 -I montar.py --fontes ~/.cache/claude-pedidos-1611/tmp-subida-noite-escura --obra subida|noche --livro N --gravar`
(os downloads ficam fora do repositório; ver o docstring do script).

1. Três leituras do mesmo fac-símile: o OCR do Internet Archive, o da outra digitalização (BMC) e o Tesseract 5
   (spa) sobre as imagens; decisão palavra a palavra por maioria, e sem maioria pela lista de frequência do espanhol.
2. Saem as notas e variantes de Silverio (letra menor), as chamadas de nota, cabeços e números de página. Páginas
   em que o classificador errou estão corrigidas à mão no script (`NOTAS_DESDE`, `CLASSE_FORCADA`,
   `NUMERO_FORCADO`, conferidas na imagem).
3. Parágrafos pelos números de Silverio: `[II.5]` no primeiro parágrafo do capítulo, `[n]` nos outros. Silverio
   pula números em dois lugares (Subida III,15 vai de 1 a 3; III,19 de 10 a 12): ficou como ele imprimiu.
4. Só na Subida, livros II e III: a transcrição do Documenta Catholica Omnia (texto de Silverio, sem as notas) serve
   de segundo testemunho para **limpar o OCR**: troca só palavra ilegível ou inexistente por palavra parecida que
   está no mesmo lugar do testemunho (cerca de 140 trocas). O Documenta não tem a Noite.
5. Acentuação de hoje (así, más, fue, dio, quedeme); as formas do autor ficam (aqueste, esotro, substancia,
   habemos, decirse ha).
6. `emendas.py`: correções conferidas na imagem ou pelo contexto (livros 0 e I da Subida, revistos dúvida por
   dúvida; nos demais, os trechos embaralhados, notas que vazaram para o texto, títulos e as palavras com sinais
   estranhos). A errata do fim do volume está aplicada.
7. Segunda rodada de emendas (2026-11-16, bloco `NOVAS` no fim de `emendas.py`): as listas «OCR» que os tradutores
   deixaram em `traducao/notas-*.md` das duas obras e em `noite-escura/traducao/notas-ocr.md`. São 623 emendas (688
   trocas): Subida I 21, II 281, III 142; Noite I 64, II 115; e cinco emendas antigas da Noite que repetiam a
   sílaba («satisfecha, tisfecha», «suspensión pensión», «estado tado», «salmo: mo:», «Que Que») corrigidas. Entram
   letra trocada, palavra partida, latim refeito pela Vulgata na forma que o impresso traz (_ejus_, _coelo_),
   pontuação solta ou que faltava (fim de parágrafo sem ponto), acentuação de hoje que a regra não alcançou
   («por vía», «discípulo»), `habernos` → `habemos` (35 vezes, todas a forma do autor), chamadas «(1)» e números de
   parágrafo vazados. Saíram do texto as notas e variantes de Silverio que tinham vazado (Subida II,5,6; II,7,13;
   II,21,11; II,30,1; III,31,8; III,39,3 «1 Así»; Noite I,4,8; II,18,4; II,23,3 «4.»).
   **Estrutura** (no original e na tradução): separados Subida III,26,[8] e Noite II,1,[3], que o OCR juntara;
   juntado Subida II,31,2, partido na virada da página; tirado o fim do título de Noite I,9 que tinha virado
   parágrafo. `palavras-raras.tsv` refeito depois (as linhas mudaram).

## Conferido na imagem (2026-11-16)

Emendado pelo que a página mostra (marcado `# img` em `emendas.py`): Subida I,10,3 «no mortificados»; II,1,2
«encubierta al demonio camina»; II,7,11 «resuelto»; II,8,5 «escultura el oficial»; II,17,3 «el bajo y fin
extremo»; II,19,1 «siendo ellas»; II,21,5 _facere_ (a Vulgata tem _agere_; o impresso traz _facere_, e fica);
III,1,1 o fim do parágrafo que o OCR cortou («…dependen de las otras.»); III,16,1 (Santiago, tratar, se escribe,
toda tu ánima, se contiene… espiritual); III,18,6 «no la tuviese»; III,19,7 (pecados mortales por la codicia… su
hacedor… este grado); III,25,1 «de éste»; III,25,6 «trasvierten»; III,26,4 (las unas… las otras… crecían…
perfeccionándose el espíritu, que es la porción superior del alma… sólo); III,31,8–10; III,39,3. Noite I,8,3
«refrenados» (já conferida pelo tradutor); I,11, título «Decláranse»; I,9, título; II,1,3; II,2,2 «clarifique»;
II,5,4 «malas» (tipo quebrado, lê-se «mafas»); II,12,7 ponto final depois da chamada; II,17,6 «ni menos declarar con
términos humanos ni vulgares»; II,23,12 «entró pidiendo»; II,24,3 _regalibus sedibus_.

Confere com o impresso e **fica como está** (erro ou descuido do autor ou do editor, ou leitura certa que parecia
errada): Subida I,6,1 «privación y positivo» (não «privativo»); II,11,4 «corporal o espiritual»; II,26,11
«conociendo otra cosa en la cosa»; III,2,8 «perfeccionando… hasta perderlas»; III,2,14 «que otros acordarse»;
III,13,8 «en aquel que hizo al alma»; III,15,2 «en el capítulo del primer libro» (sem número); III,16,1 «enterarla»;
III,18,4 «doblado hijos de perdición que fueron ellos»; III,18,6 a última frase, sintaxe do autor; III,22,2 «mas
debe vivir… en la flaqueza del sentido que en la fuerza del espíritu» (sem «más»). Noite I,11,1 «uviado» (palavra
antiga; nota de Silverio); I,12,2 «tiene más de veras éstas»; I,12,4 a pontuação de «hace entender Dios cómo»;
I,13,15 «llama el Señor su casa»; II,6,1 «destrica y descuece» (Silverio anota as variantes dos códices); II,11,5
«digresiones» (idem).

## O que ficou duvidoso

- `palavras-raras.tsv`: palavras fora da lista de frequência (arquivo, linha). A maioria é latim, nome próprio ou
  forma antiga; algumas são erro de OCR que a votação não pegou (ex.: letra trocada que forma outra palavra). Nos
  livros II–III da Subida e na Noite só se emendou o que os tradutores apontaram (rodada de 2026-11-16); a lista
  inteira **não** foi conferida uma a uma na imagem. O que ficou em aberto: `../FALTA-original.md`.
- Erros de OCR que formam palavra válida (del/dal, como/cómo) não aparecem em lista nenhuma; a comparação com o
  Documenta corrigiu parte disso só quando a palavra era rara.
- Lugares em que o Documenta tem texto que o OCR não tem e não se achou a causa: nenhum grande (a página 229 da
  Subida, que tinha sumido, foi recuperada).
