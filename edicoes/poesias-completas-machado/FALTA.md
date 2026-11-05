# Poesias Completas (Machado de Assis, 1901): o que está feito e o que falta

Pedido do Gere (rodada de 05/11/2026). Branch `pedido-poesias-completas-machado`. Obra `poesias-completas` do autor
`machado-de-assis` (Literatura), endereço `/biblioteca/machado-de-assis/poesias-completas/`: advertência + 70 poemas
(Crisálidas 12, Falenas 19, Americanas 12, Ocidentais 27), 6.806 linhas de verso, ~44.800 palavras, 28 notas do autor
no fim dos poemas, 88 erros de 1901 corrigidos (lista na «Sobre»).

## Fontes (fora do git: `~/.cache/claude-pedidos-0511/poesias-completas-machado/`, só neste PC)
- Base: o volume da Garnier (folha de rosto 1902, advertência 22/07/1900, colofão 08/1901), exemplar Google
  (I7oQAAAAIAAJ) no Commons (`commons/pc1901.pdf`); páginas `pag/p-NNN.png` (300 dpi), OCR Tesseract `tess/`.
  Página do PDF = página do livro + 16.
- Confronto: Wikisource, as primeiras edições revistas (1864, 1870, 1875) e o próprio volume nas Ocidentais (`ws*/`);
  Un vieux pays pelo Wikisource francês. O corpus do Versificador NÃO foi tocado.
- A advertência diz que o prefácio de Caetano Filgueiras foi suprimido: não entra (pergunta no revisao.json).

## Fluxo (na raiz do repositório)
1. `rascunho.py` (rascunhos) · `conferir.py pontos` (1.561 pontos, ~690 por regra, o resto decidido nas pranchas;
   decisões em `conferencia.json`: ws, ocr, ws! = erro de 1901, !texto = erro corrigido, texto livre) ·
   `conferir.py aplicar` → `base/` · `linhas.py base|1901` (confere as linhas com o OCR).
2. `ajustes.py` → `1901/` (cabeçalhos, epígrafes, partes, teatro, consertos); `1901/lira-chinesa.txt`,
   `1901/advertencia.txt` e `1901/notas.txt` foram passados a limpo à mão (MANUAL).
3. `modernizar.py` → `texto/` e `relatorios/grafia.tsv` (MANUAL, regras, léxico do sistema, dicionário do Wikisource).
4. `montar.py` → `conteudo/machado-de-assis/poesias-completas.js` (erros em `erros.json`, apresentação em `edicao.json`).
5. Avulsos: `OBRAS_PROPRIAS['machado-de-assis']` em `ferramentas/poesia.py` (saem 25; fica «A Carolina», das
   Relíquias); `conteudo/poesia.js` e `conteudo/machado-de-assis/poesia.js` regerados.
6. Vocabulário: `edicoes/vocabulario/poesias-completas.json` (378 verbetes; 73 vieram do arquivo do autor, que ficou
   vazio, só com «A Carolina»; conferir ok).

## Ao publicar (o principal)
- `public/_redirects`: as 50 linhas de `redirects.txt` (regras exatas, antes da primeira com `/*`); Catálogo `obras`
  (saem 25 avulsos, entra a obra); `traducoes_revisao.py --revisao` (8 escolhas em `revisao.json`).
- Cards: nenhum texto aponta para os poemas avulsos de Machado (conferir antes).

## Dúvidas que ficaram (leituras mantidas ou decididas com pouca certeza)
- «depois de tempo» (Versos a Corina, III) e «àquela» (Clódia; 1901 «áquilea»): no revisao.json.
- Grafia de palavras raras que o léxico não tem (SEM_PAR em `relatorios/grafia.tsv`, ~700 formas, quase todas
  palavras de hoje sem acento a pôr ou nomes): revistas por amostra; podem sobrar acentos faltando em palavras raras.
- Números romanos da Pálida Elvira e da Cristã nova seguem o Wikisource onde o OCR leu outro (não conferidos um a um).
- Vocabulário menos seguro (do subagente): destoucar, banhos (proclamas), al, pear, franças, ardido, empecer, queimor,
  transmontando, familiar (Inquisição), houveste, vingar, vênia, peregrino, arranco, fezes, cria, vero, vergôntea,
  magano, tasquinar, bocaiuva e as definições tupis.
