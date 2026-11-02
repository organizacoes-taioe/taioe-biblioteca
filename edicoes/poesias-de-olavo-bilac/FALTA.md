# Poesias de Olavo Bilac (1902): o que está feito e o que falta

## Feito (2026-11-02)
- Obra `poesias-de-olavo-bilac` (Literatura, autor `olavo-bilac`), montada por `montar.py` a partir de `texto/`
  (cópia dos arquivos do corpus do Versificador, transcritos das imagens do fac-símile de 1902, Brasiliana
  Mindlin no Wikimedia Commons, `File:Poesias_(1902).pdf`).
- No ar (depois do gerar): **Panóplias** (12 poemas; *Para a Rainha Dona Amélia*, que não está em 1902, fica de
  fora), **Via Láctea** (35 sonetos, com as dedicatórias de 1902) **Sarças de Fogo** (30 poemas) e **Alma Inquieta** (38 poemas): 115 poemas, 23.828 palavras.
- Confronto palavra por palavra: (1) transcrição do corpus × Wikisource (poemas avulsos, grafia atual, edição
  não indicada): 72 divergências nas duas primeiras partes, 43 nas Sarças e 69 na Alma Inquieta (*Abyssus*, *É nestas noites
  sossegadas*, *Noite de inverno*, *Wilfredo* e *Baladas românticas* não estão no Wikisource: corpus × OCR, e as
  *Baladas* nem isso, porque o OCR não achou o título: conferir nas imagens); (2) cada divergência conferida na camada de OCR do próprio PDF de 1902.
  Em todas, 1902 dá a lição do corpus; as do Wikisource são de outras edições (Bilac reescreveu versos d'*A morte
  de Tapir* e da *Via Láctea*: mangueira/ramada, Tornas/Volves, tornando/volvendo…) ou erros de leitura
  (Neto, dava, precipitar, asserena, tio, batei). Mantidas como em 1902: «Heliostes» (2 vezes, por
  «heliastas»), «hetere», «fermosura», «No liminar da morte». Erro de 1902 corrigido: «tal..» → «tal...» (*Profissão de fé*).
- Grafia: AO1990 já feita no corpus, menos o «porque» das perguntas, «a fora», «para traz», «vasios»,
  «cor de rosa» e «Campo Santo» da Alma Inquieta, corrigidos em `GRAFIA` no `montar.py` (nas próximas partes, procurar
  esses casos: o Wikisource, em grafia atual, os mostra no confronto); o `montar.py` passa d'essa/n'um/outr'ora a dessa/num/outrora e mantém as
  elisões do verso (minh'alma, d'alma, d'água); E' → É; Gœthe → Goethe; Luiz → Luís.
- Vocabulário: `edicoes/vocabulario/poesias-de-olavo-bilac.json` (144 palavras, tiradas do
  `olavo-bilac-poesia.json` já revisado; `conferir` dá ok).

## Falta
- **As Viagens, O Caçador de Esmeraldas**: os textos de 1902 já estão no corpus
  (`Solar/producao/versificador/corpus/bilac/{as-viagens,cacador-de-esmeraldas}--*.txt`).
  Para cada parte: copiar para `texto/`, pôr a parte em `PARTES` do `montar.py`, rodar o confronto com o Wikisource
  (scripts `parte.py <slug>` (acha o poema na `Categoria:Olavo_Bilac`) e `diff.py`, que ficaram em `~/.cache/claude-pedidos-0211/scr-bilac/`, só neste PC; o
  Wikisource tem os poemas um a um na `Categoria:Olavo_Bilac`) e conferir cada divergência no PDF
  (`pdftotext -layout` do PDF do Commons), estender o vocabulário (`so_capitulos` = número do poema na obra),
  e atualizar `descricao` (montar.py) e `apresentacao` (edicao.json).
- Ver a nota de abertura e o índice de 1902 (ordem dos poemas dentro de cada parte já é a do corpus, que segue o
  índice de 1902).
- **Duplicação**: os mesmos poemas estão em `conteudo/olavo-bilac/poesia.js` (poemas soltos, do
  `ferramentas/poesia.py`, livros panoplias…cacador-de-esmeraldas). Decidir com o Gere, quando a obra estiver
  completa, se saem de lá (sugestão: sair, mantendo Avulsos e Tarde; os endereços antigos perdem a posição de leitura).
