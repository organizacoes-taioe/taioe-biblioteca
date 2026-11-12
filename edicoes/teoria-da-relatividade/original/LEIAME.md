# Über die spezielle und die allgemeine Relativitätstheorie: texto alemão

Base: A. Einstein, *Über die spezielle und die allgemeine Relativitätstheorie (Gemeinverständlich)*,
**5. Auflage** (10.–14. Tausend), Braunschweig, Friedr. Vieweg & Sohn, 1920 (Sammlung Vieweg, Heft 38).
Einstein †1955: domínio público no Brasil desde 2026; publicada em 1920, livre também nos EUA. Os
apêndices de edições muito posteriores (1952 etc.) ficaram de fora.

## Testemunhos (baixados em 2026-11-12, em `~/.cache/claude-pedidos-0511/teoria-da-relatividade/dl/`)
- **G**: Projeto Gutenberg 77850 (2026), a **1ª edição** (1917), revisada pelo Distributed Proofreaders
  («offensichtliche Druckfehler wurden stillschweigend korrigiert»). Base das partes I e II.
- **A** e **B**: duas digitalizações do mesmo exemplar de 1920 (Univ. de Wisconsin, Google) no Internet
  Archive, `berdiespezielle00unkngoog` e `bub_gb_kTdWAAAAMAAJ`, com duas leituras OCR independentes.
  B tem páginas faltando no apêndice; A é completa. As imagens de A serviram para conferir.

## Como foi montado (scripts em `../montagem/`, `construir.sh` refaz tudo)
1. `montar_g.py` divide G em prefácio e partes I–II (`gesperrt` de nomes → texto normal; o resto → itálico).
2. `diff1920.py` compara G com A e B palavra por palavra e lista as diferenças em que A e B concordam
   (mudança de 1920, não erro de OCR). Todas as de palavra foram conferidas nas imagens. Mudanças de 1920
   aplicadas por `aplicar1920.py` (lista em `fix-g.tsv` e no próprio script):
   - § 2 «Die Erdoberfläche» → «Der Erdboden»; § 5 «20 km» → «30 km», «Umlaufbewegung» → «Umlaufsbewegung»;
     § 9 «alle Betrachtungen» → «unsere Betrachtung»; § 11 «erfüllt sein kann» → «erfüllt ist»,
     «Lichterregung» → «Lichtausbreitung» (2ª ocorrência) e a fórmula de _t′_ na forma de 1920;
     § 12 «… der Lorentz-Transformation für die Zeit _t_ = 0»; § 13 «ausgleichenden» → «ausgezeichneten»;
     § 15 «für eine kinetische Energie» → «für die Energie»; § 17 «liegt darin» → «liegt daran»;
     § 19 «(z. B. die Erde)»; § 20 «relativ zu dem» → «relativ zu welchem» e a frase final
     «Dies Schwerefeld ist es auch, welches den Ruck des Beobachters bewirkt»; § 21 «Diesen Mangel
     fühlte» → «Diesen Einwand sah»; § 23 «der mit der Scheibe bewegte Beobachter»; § 27 a frase
     «Solche Koordinaten … unterscheiden kann» substituída por «Diese Zuordnung braucht nicht einmal …»;
     § 29 «zwei wesensverschiedene Beobachtungsergebnisse … Merkur», «die Gleichungen der allgemeinen
     Relativitätstheorie» e o último parágrafo reescrito (a curvatura da luz já confirmada).
   - Notas novas de 1920: § 11 (Anhang), § 16 (elétron e gravitação), § 17 (Anhang), § 22 (eclipse de
     1919), § 23 (sistema galileano _K_), § 26 (Anhang). As outras 15 notas já estavam em 1917.
3. Parte III, apêndice e «Nachtrag zur dritten Auflage»: OCR de B (parte III) e de A (apêndice) com as
   correções de `fix-p3.tsv`, `fix-anh.tsv`, `fix-nach.tsv`, todas conferidas nas imagens (as margens
   esquerdas das p. 71, 73, 75 e 77 estão cortadas no fac-símile; as letras perdidas foram repostas pelo
   sentido). As fórmulas do apêndice foram transcritas das imagens.
4. `pos.py`: cabeçalhos, marcas `[I.n]`, fórmulas em linha (Unicode: √, ², ₁, ′), figuras `{fig …}`;
   `renumerar.py` leva as notas ao fim de cada § e as numera 1, 2…

## Apresentação (não texto)
- Ortografia e pontuação de 1920 (daß, Entwickelung, numerieren). «Zeemann» como impresso.
- § 15 «die kinetische Theorie» (por «Energie») e § 29 «die … zugänglich sind» (por «ist») ficam como
  impressos; a tradução lê o sentido.
- Notas numeradas por parágrafo, em vez de por página. «Gesperrt» de ênfase → itálico; de nomes → normal.
- Fórmulas: em linha, com √( ) e frações com barra; os números das equações como «. . . (1)».
- As 4 figuras (Fig. 1, 2, 3 e a do tubo de Fizeau, sem número) foram redesenhadas em SVG
  (`conteudo/img/teoria-da-relatividade/`); a Fig. 1 tem rótulos em alemão no original e em português na tradução.
