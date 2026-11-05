# Lira dos Vinte Anos (Álvares de Azevedo): o que está feito e o que falta

## Feito (2026-11-02)
- Obra `lira-dos-vinte-anos` (Literatura, autor `alvares-de-azevedo`), montada por `montar.py` a partir de `texto/`
  (um arquivo por poema, formato do corpus do Versificador; o corpus não foi tocado): Dedicatória (com as epígrafes
  do livro), 1ª parte (36 poemas), 2ª parte (Prefácio em prosa, `texto/prefacio-segunda-parte.txt`, e 10 poemas) e
  3ª parte (39 poemas): 87 partes, 5.408 linhas de verso, 32.819 palavras. Endereços `primeira-parte-<poema>` etc.
- Edições: 1ª e 2ª parte pela **1853** (vol. I das *Obras*, Typ. Americana; fac-símile Brasiliana USP servido pela UFSC);
  3ª pela **1862**, t. III (Garnier, org. Jaci Monteiro: «Lyra dos vinte annos — continuação», 1ª publicação).
  Fora: *Poesias diversas*, notas do editor e o texto «São os primeiros cantos…» das edições modernas (não está em
  1853 nem em 1862).
- Método: `rascunho.py` (em `~/.cache/claude-pedidos-0211b/poesia-0211/scr/`, só neste PC) alinha palavra a palavra a
  camada de texto da base com o Tesseract do mesmo exemplar, com a outra edição/exemplar (1862 t. I Mindlin; 1862 t. III
  Google) e com um texto moderno (NEAD/UNAMA, grafia de 1943, só detector); a grafia de hoje vem do texto moderno
  quando o esqueleto bate, ou de um léxico. Os 48 poemas novos e o prefácio foram conferidos verso a verso nas imagens
  por 5 subagentes (Sonnet), com as regras em `~/.cache/claude-pedidos-0211b/poesia-0211/INSTRUCOES-LIRA.md`; cada
  decisão está nas linhas `# nota:` do arquivo do poema. Os 37 poemas do corpus foram confrontados com a base:
  3 leituras corrigidas pelo impresso (56 «deceçam» → decepção; 60 «fenice» → fenece; 69 «acabara» → acabava).
- Grafia no `montar.py`: contrações com forma de hoje (num, dela, nessa, outrora…), «por que» nas perguntas, cousa/dous/
  doudo → coisa/dois/doido, «langor» → «languor» (forma do autor). Ficam oiro, loiro, inda, per, seiba, elisões.
- Avulsos: `OBRAS_PROPRIAS['alvares-de-azevedo'] = ('lira-dos-vinte-anos--',)`; saíram os 37 de
  `conteudo/alvares-de-azevedo/poesia.js` (fica *Se eu morresse amanhã*, das Poesias diversas). `redirects.txt`: os 37
  endereços antigos → o poema na obra (301).
- Vocabulário: `edicoes/vocabulario/lira-dos-vinte-anos.json`, 214 palavras (107 do arquivo do autor, já revisadas, e
  107 novas, feitas por subagente; `conferir` ok); o do autor ficou com 1 obra e 1 palavra.

## Ao publicar (o principal)
- `public/_redirects`: as 37 linhas de `redirects.txt`; Catálogo `obras.sql` (saem 37 avulsos, entra a obra).
- Cards: nenhum texto aponta para esses endereços. Tirar a *Lira* dos pedidos (Catálogo `sugestoes`).

## Falta / dúvidas (leituras mantidas como impressas, que podem ser erro de composição)
- 74 «Eu não o ideal» (moderno: «sou»); 82 «nos solidões»; 78 «Do pessegueiro um flor»; 65 «entre as poleiras»
  (moderno: «palmeiras»); 17 «Faceva tudo rider» (Dante, por «tutto»). Conferir nas imagens se quiser emendar.
- Vocabulário novo menos seguro: irerê, poupa (= popa), sota, lia, olhas, escudos, almo, dulias, transverbera.
- Filetes (traços) entre seções viraram linha em branco; falas narrativas sem nome no *Um cadáver de poeta* ficam
  depois da última `@ fala` (o site as mostra como verso comum).
