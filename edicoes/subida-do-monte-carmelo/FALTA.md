# Subida do Monte Carmelo (e Noite Escura): o que falta

Branch `pedido-subida-noite-escura` (uniformização em `pedido-subida-noite-escura-e2`). Situação em 2026-11-16.

## Feito

- Texto espanhol completo das duas obras (Silverio, 1929): `original/` aqui e em `../noite-escura/original/`; método,
  fontes e dúvidas em `original/LEIAME.md`.
- `obra.py` das duas; `CONVENCOES.md` (vale para as duas, com os termos da uniformização); `VERSOS.md` (aqui e na
  Noite, com a lista completa dos lugares).
- **Tradução completa** das duas obras (7 arquivos aqui, 4 na Noite; ≈ 144 mil palavras), em 5 lotes, com as
  escolhas de cada lote em `traducao/notas-*.md`; parágrafos iguais ao original, arquivo por arquivo.
- Uniformização (2026-11-16): termos, citações repetidas da Escritura, versos repetidos (idênticos às canções,
  conferidos por script), aspas, registro. Grep de mesóclise vazio; sem aspas retas; sem «lho/lha/no-lo».
- `revisao.json` aqui (9 decisões) e na Noite (5); `python3 ferramentas/traducoes_revisao.py` dá ok.

## Falta

- Vocabulário: palavras raras com nota (regra do guia da Biblioteca, «Vocabulário»).
- Notas gerais (por lotes, `edicoes/notas/`).
- Versos: esperam a decisão `cancoes` do `revisao.json` (literal, Teófilo Braga ou Versificador).
- Publicar: juntar com a branch das emendas do original (estrutura de parágrafos), gerar o site, Catálogo.

## Por conferir

- Emendas de OCR anotadas nas `traducao/notas-*.md` (seções «OCR»): o outro agente as passa ao `original/`.
  Parágrafos partidos ou juntados por engano (Subida II,31,2; III,26,7–8; Noite II,1,2–3; Noite I,9, cabeço): ao
  juntar ou separar no original, fazer o mesmo na tradução.
- Canção 3: os dois originais trazem «Sin otra luz y guía»; a tradução ficou «Sem outra luz e guia» nas duas (a
  Subida tinha «nem guia»). Se a emenda do original da Subida trouxer «ni guía», voltar a «nem guia» só lá.
- Texto espanhol dos livros II e III da Subida e da Noite não conferido palavra a palavra na imagem.
- Silverio pula números de parágrafo em Subida III,15 (1→3) e III,19 (10→12): conferido na imagem, ficou assim.
- Autor: `sao-joao-da-cruz` em `conteudo/autores.js` não tem `area: 'catolicismo'` nem `ordem`: o principal decide.
