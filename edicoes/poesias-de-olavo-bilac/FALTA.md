# Poesias de Olavo Bilac (1902): o que está feito e o que falta

## Feito (2026-11-02)
- Obra `poesias-de-olavo-bilac` (Literatura, autor `olavo-bilac`), montada por `montar.py` a partir de `texto/`
  (cópia dos arquivos do corpus do Versificador, transcritos das imagens do fac-símile de 1902, Brasiliana
  Mindlin no Wikimedia Commons, `File:Poesias_(1902).pdf`).
- As seis partes: **Panóplias** (12; *Para a Rainha Dona Amélia*, que não está em 1902, fica de fora),
  **Via Láctea** (35 sonetos, com as dedicatórias de 1902), **Sarças de Fogo** (30), **Alma Inquieta** (38),
  **As Viagens** (14) e **O Caçador de Esmeraldas**: 130 poemas, 29.367 palavras.
- Confronto palavra por palavra: (1) transcrição do corpus × Wikisource (poemas avulsos da
  `Categoria:Olavo_Bilac`, grafia atual, edição não indicada): 72 divergências nas duas primeiras partes, 43 nas
  Sarças, 69 na Alma Inquieta, 59 nas Viagens, 18 no Caçador; (2) as divergências conferidas na camada de OCR do
  próprio PDF de 1902 (`pdftotext -layout`). Em todas as conferidas, 1902 dá a lição do corpus; as do Wikisource
  são de outras edições (Bilac reescreveu versos d'*A morte de Tapir*, da *Via Láctea* etc.) ou erros de leitura
  (Neto, dava, precipitar, asserena, tio, batei, dano por clarão). Sem Wikisource: *Abyssus*, *É nestas noites
  sossegadas*, *Noite de inverno*, *Wilfredo* (corpus × OCR, sem divergência real) e *Baladas românticas*.
- Erro de 1902 corrigido: «tal..» → «tal...» (*Profissão de fé*). Mantidas como em 1902: «Heliostes» (2 vezes,
  por «heliastas»), «hetere», «fermosura», «No liminar da morte», «Jacob», «cœli», «vêm» (= veem, monossílabo).
- Grafia: AO1990 já feita no corpus; o `montar.py` passa d'essa/n'um/outr'ora a dessa/num/outrora e mantém as
  elisões do verso (minh'alma, d'alma, d'água); E' → É; Gœthe → Goethe; Luiz → Luís; títulos Fenícios, Índias,
  Brasil. O que o corpus deixou na grafia antiga vai em `GRAFIA` (montar.py): «por que» nas perguntas (Alma
  Inquieta, Viagens), afora, trás, vazios, cor-de-rosa, Campo-Santo, Caos, Cristãs, juçaras, antemanhã, Guaicuí,
  dar-lhe-ás (mesóclise do autor, fica).
- Vocabulário: `edicoes/vocabulario/poesias-de-olavo-bilac.json` (195 palavras, tiradas do
  `olavo-bilac-poesia.json` já revisado, com `so_capitulos` = número do poema na obra; `conferir` dá ok).
- `ferramentas/site/gerar.mjs`: o livro inteiro aparece em «Livros», em cima das formas, na página do autor.

## Falta
- *Baladas românticas*: conferida só com o OCR de 1902 (não está no Wikisource), sem divergência real.
- Ver se 1902 numera os poemas d'*As Viagens* (o Wikisource põe I–XIV) e se há nota ou prefácio a incluir.
- **Duplicação**: os mesmos poemas estão em `conteudo/olavo-bilac/poesia.js` (poemas soltos, do
  `ferramentas/poesia.py`, livros panoplias…cacador-de-esmeraldas). Decidir com o Gere se saem de lá (sugestão:
  sair, mantendo Avulsos e Tarde; os endereços antigos perdem a posição de leitura).
- Scripts do confronto (`parte.py <slug>`, `diff.py`, `ocr.py`, `ocr1.py`) em `~/.cache/claude-pedidos-0211/scr-bilac/`,
  só neste PC.
