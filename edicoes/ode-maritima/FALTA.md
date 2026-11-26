# Ode Marítima (Álvaro de Campos): o que está feito e o que falta

## Feito (2026-11-26)
- Obra `ode-maritima` (Literatura, autor `fernando-pessoa`, seção «Livros», gênero Poesia, 1915), poema inteiro numa
  página só (904 versos, 119 estrofes, 7.869 palavras; obra comum com uma parte, não `documento`: este leva ao
  gênero «Poesia» de Pessoa, que não existe, e quebra o link). Marca `{v N}` a cada 10 versos. `montar.py` gera
  `conteudo/fernando-pessoa/ode-maritima.js` a partir de `texto/ode.txt`; `index.html` ganhou a linha do script.
- Base: transcrição do *Orpheu* n.º 2 (abr.–jun. 1915) do Projeto Gutenberg (ebook 23621, 2007) em
  `texto/orpheu-1915.txt`, na grafia da época; conferida com o Wikisource pt (só para comparar). `modernizar.py` leva
  `orpheu-1915.txt` a `texto/ode.txt` (grafia brasileira de hoje, dicionário palavra por palavra, `--` vira `—`,
  correções à mão listadas no próprio script). Não editar `ode.txt` à mão: mexer no `modernizar.py` e rodar de novo.
- `edicao.json` («Sobre»: 3 erros da transcrição corrigidos, 12 pontos em que o Orpheu e o Wikisource divergem);
  `revisao.json` (3 decisões, recomendação aplicada: base, grafia, três emendas); vocabulário
  `edicoes/vocabulario/ode-maritima.json` (63 entradas; termos náuticos só os de sentido seguro; `conferir` ok).
- Não era avulso: a ode não está em `poesia.js` nem em `OBRAS_PROPRIAS`; não há redirecionamento.

## Não conferido (falta o fac-símile)
- Nenhum fac-símile livre achado (Commons só tem a capa; o Internet Archive só tem a Ática 1978, protegida; a BNP
  restringe o *Orpheu*; o modernismo.pt só tem recortes). **Todo o texto vem de transcrição**, sem ver as páginas.
  Pontos para olhar na revista: «fumo» × «fundo» (chaminés das fábricas), «sentidos parados», «derramam»,
  «para onde fôr», «um corpo cheio de sanguessugas» (copo?), «estranguladoras», «numa capa», «há só um vácuo», e as
  três emendas («uma gata», «opostas», «à força»). Também as estrofes, o itálico e as maiúsculas da canção do
  pirata, e se o *Orpheu* punha mesmo travessão onde a transcrição tem `--`.
- Se aparecer o fac-símile: conferir esses pontos, mexer em `texto/orpheu-1915.txt` ou no `modernizar.py`, rodar
  `modernizar.py` e `montar.py` e atualizar o `edicao.json` (listas) e a «Sobre».

## Dúvidas de método
- Recuo da canção do pirata: o site não tem; as linhas ficam à margem (dito na «Sobre»).
- Contrações «pró», «prá», «prós», «plas», «plos», «pla», «pr'» ficam (voz de Campos); nada as troca no
  `modernizar.py`.
- «passastes», «enchestes», «vendestes»… (2ª pessoa do plural em -stes, que Pessoa escreve) ficam.

## Ao publicar (o principal)
- Sem regra de `_redirects`. Catálogo `obras.sql` (entra a obra); tirar o pedido da fila (Catálogo `sugestoes`);
  `traducoes_revisao.py --revisao` para as 3 decisões.
- Rascunhos (Wikisource, comparações) em `~/.cache/claude-pedidos-2611/ode-maritima/`, só neste PC.
