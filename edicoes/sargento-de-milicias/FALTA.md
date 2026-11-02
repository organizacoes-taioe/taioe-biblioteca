# Memórias de um Sargento de Milícias: o que falta (2026-11-02, fim da rodada das 15:45)

Estado: **fontes e confronto montados e rodando; texto ainda não conferido nem publicado.**

## Feito
- Edição-base: a 1ª em livro (Typographia Brasiliense de Maximiano Gomes Ribeiro, tomo I 1854,
  tomo II 1855), fac-símile da Brasiliana USP, BBM 4846 (`config.PDF`). O DjVu do Commons/Wikisource é
  a mesma digitalização, com a mesma numeração de páginas, mas traz um OCR diferente.
- `config.py`: os 48 capítulos (23 + 25) com as páginas e os títulos de 1854–55 na grafia de hoje
  (lidos na camada do PDF; o Wikisource troca alguns: «batismo», «Despedidas»). Quatro leitores:
  - `camada()` (pdf): OCR da Brasiliana, pdftotext;
  - `djvu()` (dj): camada de texto do DjVu do Commons (`commons.txt`, feito com `djvutxt --page=N`
    página a página, sem os `\f` internos; djvulibre extraído sem sudo em `~/.cache/djvu-local/raiz`,
    `LD_LIBRARY_PATH=~/.cache/djvu-local/raiz/usr/lib/x86_64-linux-gnu`);
  - `tesseract()` (bt): OCR novo, já rodado (`tess-bbm4846/`, 301 páginas; Tesseract em
    `~/.cache/tesseract-local/raiz`);
  - `wikisource_moderno()` (ws): texto moderno (Formulário de 1943) posto sobre as páginas do DjVu;
    dá parágrafos e grafia, e desempata. `python3 edicoes/sargento-de-milicias/config.py` mostra as
    palavras por capítulo (ws 59.530, pdf 59.565, bt 60.033).
  Não há outro exemplar acessível: HathiTrust pede verificação da Cloudflare (CAPTCHA, não usado),
  a cota da API do Google Livros acabou, e no Internet Archive só há edições modernas.
- Voto: pdf e dj são `CORRELACIONADOS` (erram juntos: «linha», «ler», «eslava»), com `UM_VOTO = False`:
  a maioria deles perde para o Tesseract quando a moderna o apoia. Com `UM_VOTO = True` quase tudo
  empatava. Resultado: 3.890 divergências, 2.883 por maioria, 298 por minoria com apoio moderno, 709 sem
  maioria (relatório `sitios.tsv`: 1.848 pontos fracos).
- `config.modernizar` (antes da grafia pela moderna, sempre só onde a moderna, alinhada no mesmo ponto,
  confirma): parte as palavras coladas pelos OCRs (76: «Tinhãoesses», «emquantoella»); passa a 3ª do
  plural em -ão a -am (814, também com pronomes: «formão», «enfurecião-se»; o futuro fica); troca as letras que os três OCRs
  confundem igual (131: l/t, c/e, ó/é, b/h, n/u…; lista em `relatorios/letras.tsv`, conferir uma amostra).
- `_capitulo_ocr` corrige antes do voto dois vícios constantes dos OCRs: o til de -ão lido como acento
  («podiáo», «fizerào», «chamavãó») e «lhe» lido «Ihe», «Ibe», «Jhe».
- `decisoes.EMENDAS`: 11 leituras conferidas nas imagens (pranchas dos pontos 1–80 de `ver/pontos.json`) e 7
  palavras que só os OCRs têm, de correção evidente (as primeiras ~60 linhas de `modernas.tsv`); `MANUAL`
  com 5 formas em -ão que não alinham. Em `modernas.tsv` há também lições de 1854 que as edições modernas
  mudaram e que ficam («espanava», não «esganava»; «engodar», não «engordar»; «achava cheio de
  espírito»; «viu-se presa»): só emendar o que for erro de OCR, de preferência visto na imagem.
- `edicoes/sargento-de-milicias/conferir.py` (pranchas, cópia do de Policarpo) funciona:
  `python3 edicoes/sargento-de-milicias/conferir.py ferramentas/cache/sargento-de-milicias/ver/p3.tsv`.
  `ver/pontos.json` tem os 650 pontos de palavra sem apoio moderno, na ordem do texto; as pranchas dos
  pontos 1–80 já foram lidas (`ver/p10-*`, `p2-*`, `p3-*`); seguir do 81.
- `texto.py` roda: 48 partes, 1.456 parágrafos; relatórios: 592 em `modernas.tsv`, 1.695 em
  `pontuacao.tsv`, 522 em `sem_par.tsv`, 384 em `vocabulario.tsv` (resíduo de OCR quase todo:
  «Leopardo», «máosrolhados», «quatrooreIhas»; resolver com EMENDAS, olhando a imagem quando houver dúvida).
- `decisoes.py` e `notas.py` com a estrutura e um rascunho da «Sobre». O bloco do autor está no item 7 abaixo.

## Falta (na ordem)
1. **Conferência**: ler as pranchas dos 650 pontos de palavra (`ver/pontos.json`, a partir do 81) e
   registrar em `EMENDAS` só o que o texto final ainda erra (muitos pontos já saem certos pelos passos de
   `config.modernizar`: conferir em `relatorios/texto.txt` antes de anotar). Depois, `modernas.tsv` e
   `vocabulario.tsv` (palavras que só os OCRs têm) e a pontuação (`pontuacao.tsv`: «meirinho!.;.»).
   Para muitas decisões, passar a `conferencia.json` + `rever()` como em Policarpo.
2. **Formas de 1854**: `transcricoes()` dá ao `ocr.limpar` o léxico das palavras que os dois OCRs leram
   iguais (um dos ABBYY e o Tesseract), senão a guia moderna «corrigia» as formas da época. Com o passo
   -ão → -am de `config.modernizar` sobram poucas formas em -ão onde o alinhamento não é 1:1: ver
   `sem_par.tsv` e `modernas.tsv` e resolver em `MANUAL`/`AJUSTES` (cuidado com o futuro).
3. **Ruído no começo**: «chamava-se nesse tempo-O — O. canto dos meirinhos —» (o Wikisource tem
   «tempo-O canto dos meirinhos-», com hífens no lugar de travessões; 1854: «— O canto dos meirinhos —»).
   Os travessões de citação e as aspas do Wikisource não são de fiar.
4. **Itálico**: nenhum dos OCRs marca; ver se *Angústia* (`italico.py`, inclinação das letras) serve.
5. **Versos** (modinhas, p. 10 e outras) em `decisoes.VERSOS` ou pelo `<poem>` do Wikisource.
6. Grafia final (`MANUAL`), `notas.py` completa (erros corrigidos, lista, descrição das fontes) e
   `texto.py --publicar`.
7. Autor em `conteudo/autores.js`, **só junto com a obra** (sem obra, o `conferir.mjs` acusa link quebrado
   em `literatura/index.html`; por isso saiu do commit), depois do de Lima Barreto:
   `BIBLIOTECA.autor({ id: 'manuel-antonio-de-almeida', nome: 'Manuel Antônio de Almeida', nomeCompleto:
   'Manuel Antônio de Almeida', vida: '1831–1861', ordem: 'Almeida, Manuel Antônio de', nota: 'Romancista e
   jornalista carioca; autor de um romance só, publicado sem o seu nome.' });`
   O `--publicar` grava `conteudo/manuel-antonio-de-almeida/sargento-de-milicias.js`.
8. `edicoes/vocabulario/sargento-de-milicias.json` (`edicoes/vocabulario/LEIA.md`;
   `node ferramentas/vocabulario.mjs … conferir` dá `ok`): o livro tem muito léxico de época (meirinho,
   chicana, rótula, mantilha, granadeiro, ucharia, malsinar…).
9. Gerar e conferir (`gerar.mjs`, `conferir.mjs`) sem commitar o gerado; commit e push na branch.

Publicação, depois do merge (com o principal): Catálogo `obras.sql` no teste e na produção e tirar o
pedido de `sugestoes.json` (Catálogo `sugestoes`).
