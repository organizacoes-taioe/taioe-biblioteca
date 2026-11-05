# Broquéis (Cruz e Sousa, 1893): o que está feito e o que falta

## Feito (2026-11-02)
- Obra `broqueis` (Literatura, autor `cruz-e-sousa`), montada por `montar.py` a partir de `texto/` (cópia dos 54
  poemas do corpus do Versificador, que é a transcrição validada do Wikisource, `Livro:Broqueis.pdf`, posta na
  grafia de hoje). 54 poemas na ordem da 1ª edição, 914 versos, 5.322 palavras; a epígrafe de Baudelaire vai no
  alto da «Antífona» (como a da *Mensagem* no primeiro poema). «Sobre esta edição» em `edicao.json`.
- Confronto: (1) corpus × Wikisource (páginas validadas, grafia de 1893), palavra por palavra pelo esqueleto
  (sem acento, th/ph/y/dobradas…): 99 divergências, todas modernização ou erro de digitação do Wikisource
  (brancnras, levauta, aneias, brauda, quebrautos, voos por vaes…), que o corpus já tinha corrigido pelo impresso;
  (2) Wikisource × OCR próprio do fac-símile (Tesseract, 300 dpi): 55 divergências, todas ruído do OCR ou as mesmas
  do Wikisource; (3) pontuação corpus × Wikisource × OCR: 14 pontos; nas imagens, o corpus erra em dois, corrigidos
  em `texto/` («em trenos;» → «em trenos,» na *Lua*; «violinos.» → «violinos...» nas *Sinfonias do ocaso*).
  Conferidos nas imagens: *Desfila* (não «Destila», *Carnal e místico*), a epígrafe, os dois pontos acima e
  *eletrismos.*; no OCR (palavras que faltam no Wikisource): *Luzes claras e augustas* (*Primeira comunhão*) e os
  quatro da *Tulipa real* (aos, a, e, e), que o corpus já tinha.
- Erros de 1893 corrigidos (na «Sobre»): «ao sóes» → «aos sóis» (*Satã*); na epígrafe, acordez, grace, inferieur,
  Beaudelaire. Mantidos: «eletrismos.» com ponto (*Sonata* III: o ponto está no impresso, embora estranho),
  «Murmuríos», «Subtis», «c'roado».
- Grafia: `montar.py` junta só as contrações com forma de hoje (dentre, num, numa, nela, daquele, outrora) e
  mantém as elisões do verso (minh'alma, tu'alma, d'ouro, d'aço, d'Ela, d'estranhos, d'incensos, c'roado). Os
  títulos latinos saem sem ligadura (Regina Coeli, Foederis Arca: o `slug` do gerador não trata «œ»); nos versos,
  «Cœli» como no impresso.
- Avulsos: `OBRAS_PROPRIAS['cruz-e-sousa'] = ('broqueis--',)` em `ferramentas/poesia.py` e `poesia.py --fonte
  …/versificador`: saíram os 54 de `conteudo/cruz-e-sousa/poesia.js` (ficam *Faróis* e *Últimos Sonetos*).
  `redirects.txt`: os 54 endereços antigos `/biblioteca/cruz-e-sousa/broqueis-<poema>/` → o poema na obra (301).
- Vocabulário: `edicoes/vocabulario/broqueis.json` (85 palavras, tiradas do `cruz-e-sousa-poesia.json` já revisado;
  `conferir` ok); o do autor ficou com as 119 obras que restam e 75 palavras (`conferir` ok).

## Ao publicar (o principal)
- `public/_redirects`: as 54 linhas de `redirects.txt`; Catálogo `obras.sql` (saem 54 avulsos, entra `broqueis`).
- Cards: nenhum texto aponta para esses endereços (`taioe-cards`, `origin/main`).
- Tirar *Broquéis* dos pedidos (Catálogo `sugestoes`).

## Falta
- Nada do texto. Scripts do confronto em `~/.cache/claude-pedidos-0211b/poesia-0211/scr/` (só neste PC).
