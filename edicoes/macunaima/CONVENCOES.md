# Macunaíma: convenções do texto (2026-11-05)

Edição-base: a 1ª (São Paulo, 1928, edição do autor), fac-símile da Biblioteca Nacional (Internet
Archive `or182096`; o mesmo exemplar do índice do Wikisource «Macunaíma (1928).pdf»). Inteira: 18
capítulos e o epílogo, com «As três Normalistas» (cap. XI), que Mário cortou em 1937. As decisões que
são do Gere estão em `revisao.json`, com a recomendação aplicada.

## O princípio
A grafia de Mário é parte da obra (ele escrevia «à brasileira» de propósito). Moderniza-se só a
ortografia de época sem valor de estilo, isto é, o que qualquer texto de 1928 grafava assim e que não
marca a fala.

## Fica como Mário escreveu
- `si`, `sinão`, `siquer`; `mãi`, `mamãi`, `mãis`; `milhor`, `guspir`, `enguliu`, `guela`, `frexa` e
  `flexa` (as duas estão no impresso), `mostro`, `bolir`, `escapoliu`, `alumear`, `desembuxar`.
- `pra`, `prá`, `pro`, `pros`, `prás`, `nagua`, `dagua`, `inda`, `riba`, `adonde`, `desinfeliz`, `té-logo`,
  `Vam’bora`, `’tá’í`, `sinh’Helena`; a colocação dos pronomes e as regências da fala.
- Compostos e aglutinações do livro (`arranhacéu`, `boca-da-noite`, `mãi-de-santo`, `pai-de-terreiro`,
  `talqualmente`, `senvergonhice`, `simsinhô`), sem as regras de hífen de hoje.
- Na «Carta pras Icamiabas» (pastiche lusitano): `dextro`, `assás`, `hemos`, `abstémio`, `Polónia`,
  `nipónicos`, `colónia`, `imperescível`, `tesoiros`.
- Palavras indígenas e africanas cuja grafia de 1928 ainda é variante registrada (`cachiri`, `curumi`,
  `embiroçu` com ç mas a forma de Mário).
- Pontuação do livro (sem vírgulas acrescentadas) e as falhas que podem ser intencionais («Vinham
  médicos veio Assistência», `estorcegado de cócegas`, «Principiou» depois de «porta» sem ponto).

## Modernizado (`config.modernizar`, `decisoes.MANUAL` e `decisoes.FINAL`)
- Acentos pela norma de hoje: heroi → herói, tambem → também, porêm/porem → porém, êle → ele,
  fôrça → força, agua → água, cunhas → cunhãs, puito → puíto, individuo → indivíduo; oxítonas em
  -i/-u sem o acento que a norma não pede (jejú → jeju, Exú → Exu, Gurupí → Gurupi; `_oxitona`),
  mantido o do hiato (Pauí, tuiuiú); acento grave das derivadas (sabiàcica → sabiacica, pèsão →
  pezão); `E’` → É, `A’s` → Às, `D’aí` → Daí.
- Ortografia de época: quasi → quase, tribu → tribo, poude → pôde, geito → jeito, tezouro → tesouro,
  gôso/gosar → gozo/gozar, dansa → dança, cincoenta → cinquenta, milreis → mil-réis, sciencia →
  ciência, -isar → -izar, idea → ideia, sopetão → supetão, alvíçaras → alvíssaras.
- Palavras indígenas e africanas cuja grafia de 1928 caiu: Ochum → Oxum, Ochosse → Oxóssi,
  macacheira → macaxeira, girau → jirau, sussuarana → suçuarana, massaroca → maçaroca, pagé → pajé,
  pegí → peji, guassú → guaçu (e os outros -assú/-ussú), assai → açaí, çairê → sairê, gêge → jeje.
- Aspas “ ” → « ».

## Como o texto foi feito
`python3 ferramentas/texto.py macunaima [--publicar]`. Base `b28`: Wikisource revisado nos caps. I,
XII–XVIII e epílogo; OCR ABBYY do IA nos caps. de `DO_OCR` (I–XI). `t28`: Tesseract das 253 páginas.
`ws`: o Wikisource inteiro (nos caps. II–XI é de edição posterior: só aponta dúvidas). `rever()` +
`conferencia.json` (351 pontos conferidos nas imagens); `decisoes.CORRECOES` (por `corrigir()`) os erros
de OCR achados depois, pela comparação com uma edição moderna (só para achar diferenças de palavra) e
conferidos no fac-símile; `notas.ERROS_ANTERIORES` os 5 erros de 1928.
