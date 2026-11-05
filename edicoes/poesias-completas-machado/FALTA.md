# Poesias Completas (Machado de Assis, 1901): o que está feito e o que falta

Pedido do Gere (rodada de 05/11/2026). Branch `pedido-poesias-completas-machado`, worktree
`~/.cache/claude-wt5-poesias-machado`. Obra `poesias-completas` do autor `machado-de-assis` (Literatura).

## Fontes (fora do git: `~/.cache/claude-pedidos-0511/poesias-completas-machado/`, só neste PC)
- Base: *Poesias Completas* (Rio de Janeiro/Paris, H. Garnier; folha de rosto 1902, advertência de 22/07/1900,
  colofão «353.8.1901»), fac-símile do Google (I7oQAAAAIAAJ) no Commons (`commons/pc1901.pdf`, sem camada de
  texto; também `archive.org/details/poesiascompleta00assigoog`). Páginas em `pag/p-NNN.png` (300 dpi) e OCR
  Tesseract em `tess/NNN.txt` (`scr/ocr.py`). Página do PDF = página do livro + 16.
- Confronto: Wikisource, as páginas do mesmo PDF (`ws/`; só as *Ocidentais* e o índice estão transcritos, nível
  3–4) e as primeiras edições revistas (`ws-Chrysalidas` 1864, `ws-Phalenas` 1870, `ws-Americanas` 1875);
  *Un vieux pays* pelo Wikisource francês (mesmo PDF). O corpus do Versificador (25 poemas) só como testemunho
  a mais; **não se grava nada nele**.
- A advertência de 1901 diz que o prefácio de Caetano Filgueiras foi suprimido: ele não entra.

## Método
1. `poemas.json`: os 72 itens do volume (advertência, 70 poemas, notas), com as páginas de 1901 e do Wikisource.
2. `rascunho.py` → `rascunho/<id>.txt`: o texto do Wikisource com as divergências do OCR de 1901 marcadas.
3. Conferência nas imagens (subagentes, `INSTRUCOES.md`) → `1901/<id>.txt` (o texto de 1901, formato do corpus,
   grafia antiga) e `1901/notas.txt`.
4. `modernizar.py` → `texto/<id>.txt` (grafia de hoje), com relatório das trocas; `montar.py` →
   `conteudo/machado-de-assis/poesias-completas.js`.
5. Avulsos: `OBRAS_PROPRIAS['machado-de-assis']` em `ferramentas/poesia.py`; `redirects.txt`; vocabulário.

## Estado
- [x] fontes baixadas, OCR, rascunhos (1.566 marcas)
- [ ] conferência nas imagens (1901/)
- [ ] notas do autor
- [ ] grafia, montagem, avulsos, vocabulário, revisao.json
