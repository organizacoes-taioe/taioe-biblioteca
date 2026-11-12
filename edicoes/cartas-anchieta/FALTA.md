# Cartas de Anchieta (seleção): estado

Branch `pedido-cartas-anchieta`. Não-ficção, «outras» (`/admin/sugestoes/`, pedido `cartas-anchieta`). Autor novo
`jose-de-anchieta` (área `nao-ficcao`, «São José de Anchieta»). Obra `cartas-anchieta`, título «Cartas, informações e
sermão», 13 peças (numeração de 1933: I, II, III, X, XI, XIV, XV, XVI, XX, XXVII, XXIX, XXXIII, XXXVIII), ~73 mil
palavras. **Pronta para juntar e publicar** (12/11).

## Fonte
- Base: *Cartas, informações, fragmentos historicos e sermões do Padre Joseph de Anchieta* (Academia Brasileira /
  Civilização Brasileira, 1933). Fac-símile: Internet Archive `r-19794-v_0000_grav-569_t24-C-R0150` (BNP). Folha do
  arquivo = página − 3 (no fim do volume, − 7).
- Traduções (latim: I, X; castelhano: III, XI, XIV, XV, XXVII): as de 1933, atribuídas na nota preliminar a Antônio
  de Alcântara Machado (†1935), sobre versões anteriores de Teixeira de Melo (†1907), Cunha Barbosa (†1846) e
  Silva Lisboa (†1840). A VII e a XXXI ficaram de fora: tradução de João Vieira de Almeida (1900, data de morte
  desconhecida); a X de 1933 **não** é a dele (conferido com BBM 4683).
- Segundo testemunho da XXIX: Capistrano de Abreu, 1886 (BBM 8015): corrigiu uma linha trocada na composição de 1933.

## Como refazer (na raiz do repo)
1. Baixar o `_jp2.zip` (descompactar em `dl/jp2/`) e o `_djvu.xml` (`dl/ia_djvu.xml`) do item do IA para
   `~/.cache/claude-pedidos-0511/cartas-anchieta/` (os PNGs e as pranchas foram apagados; o OCR, o voto e o rascunho ficaram).
2. `python3 edicoes/cartas-anchieta/ocr.py` (páginas endireitadas, duas leituras do Tesseract + a do IA).
3. `python3 edicoes/cartas-anchieta/rascunho.py` (voto → rascunho; tira cabeço, sumário e notas de 1933).
4. Conferência nas imagens (subagentes Sonnet; brief em `~/.cache/claude-pedidos-0511/cartas-anchieta/BRIEF-CONFERENCIA.md`):
   `conferir.py` (pranchas das linhas duvidosas), `conferir.py --segunda`/`--terceira`, `faltas.py` (linhas que a
   leitura-base pulou, pelo OCR do IA). Tudo vai para `conferencia.tsv` («folha⇥linha⇥texto»; «folha⇥k+⇥texto»
   insere depois da linha k; «-» apaga; «# título» = subtítulo da XXIX).
5. `python3 edicoes/cartas-anchieta/rascunho.py --aplicar` → `1933/<folha>.txt` (a transcrição de 1933).
6. `python3 edicoes/cartas-anchieta/montar.py --publicar` (grafia de hoje, decisões em `decisoes.py`, «Sobre» em
   `sobre.py`) → `atual/` e `conteudo/jose-de-anchieta/cartas-anchieta.js`.
- Vocabulário: `edicoes/vocabulario/cartas-anchieta.json` (488 verbetes, `conferir` ok).
- `revisao.json`: 8 decisões (o texto segue a recomendação de todas).

## Para o principal
- Gerar, Catálogo `obras` (obra nova) e `traducoes_revisao.py --revisao` (8 escolhas novas). Sem `_redirects`.
- Notas gerais: não feitas (vão por lotes).
- Amostra de páginas inteiras depois da conferência: ~0,5% de erro, quase tudo acento grave × circunflexo que a
  grafia de hoje apaga; as rodadas seguintes trataram crase, pontos e linhas puladas. Uma leitura corrida do
  sermão (XXXVIII) e da XV contra as imagens ainda acharia miudezas.
