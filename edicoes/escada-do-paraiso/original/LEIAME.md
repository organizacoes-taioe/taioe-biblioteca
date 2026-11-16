# Escada do Paraíso: texto grego

Base: _Patrologia Graeca_ de Migne, vol. 88 (Paris, 1860), col. 631–1164, _S. Joannis Climaci Scala Paradisi_, que
reproduz a edição de Mateus Rader, S.J. (Paris, 1633), com a tradução latina dele na coluna ao lado e os escólios de
Elias de Creta depois de cada degrau. Domínio público. A edição de Sofrônio Eremita (Constantinopla, 1883) é também
livre, mas não há fac-símile acessível; edições críticas modernas não existem completas.

## De onde vem
- Fac-símile principal: Internet Archive `bim_early-english-books-1641-1700_1860_88` (folhas 315–581 = col. 631–1164;
  folha f tem as colunas 633 + 2·(f − 316) e a seguinte). O grego ora está na coluna esquerda, ora na direita.
- Segunda leitura: Documenta Catholica Omnia, PDF de imagens `0525-0606,_Joannes_Climacus,_Scala_Paradisi_(MPG_088_0631_1163),_GM.pdf`
  (outra digitalização, de 912 px de largura, ampliada 3×).
- Não há transcrição livre do texto de Rader: o grego é um OCR nosso (Tesseract 5, modelo `grc`).

## Como foi feito (scripts em `../ferramentas/`)
1. OCR das duas colunas de cada folha (`ocr.py`), releitura das linhas que o Tesseract pulou (`lacunas.py`).
2. Coluna grega, sem latim, cabeçalho, notas de pé e números de escólio (`linhas.py`); hifenização desfeita e letras
   que o OCR confunde (κ/χ, β/δ, ν/υ…) corrigidas por um léxico de formas tirado do First1KGreek e do Perseus
   (`lex.py`, `montar.py`); a segunda leitura decide as palavras fora do léxico.
3. Estrutura (`estrutura-frases.json`, `resolver.py`), títulos lidos nas imagens (`titulos.json`), divisão em blocos
   nos fins de frase (`dividir.py`, `cortes.json`): só o texto dos degraus, sem os escólios.
4. Conferência nas imagens: as ~2.300 palavras fora do léxico em pranchas (`suspeitas.py`, `pranchas.py`,
   `aplicar.py`), os erros que os tradutores apontaram nas notas (`../traducao/notas-degrau-NN.md`, «Grego a
   corrigir») e as linhas que faltavam, inseridas pela imagem. Desde então o `original/` é editado à mão (não
   rodar de novo o `dividir.py` sobre ele).

## Apresentação
- `[n.k]`: degrau e bloco, numeração desta edição (os parágrafos de Rader, divididos nos fins de frase).
- `{PG 88.nnn}`: começo da coluna da PG.
- `## …`: título de seção dentro do degrau (23, 26, 27), como na PG.
- Colchetes: as lições alternativas que Rader e Migne imprimem no texto («[al. …]», «[cod. A. …]»), como estão.
- Saíram: os números dos escólios, os escólios, as notas de pé (referências bíblicas) e o latim.

## O que ainda pode ter erro
A conferência dos degraus 26–30 foi menos completa (só as palavras fora do léxico e os pontos das notas foram
vistos nas imagens); acentos e espíritos que formam palavra existente só foram corrigidos onde alguém os apontou.
