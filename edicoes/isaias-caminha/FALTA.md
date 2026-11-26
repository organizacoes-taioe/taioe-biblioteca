# Isaías Caminha — estado e o que falta (branch `pedido-isaias-caminha`)

**Pronto para o principal juntar e publicar** (26/11): `conteudo/lima-barreto/isaias-caminha.js` (Breve notícia +
14 capítulos, ~62 mil palavras), a linha no `index.html`, `edicoes/vocabulario/isaias-caminha.json` (124 verbetes,
`conferir` ok) e `revisao.json` (2 decisões, recomendação aplicada). Autor já existia. Sem `_redirects`. Não rodei
Catálogo nem mexi no infra.

## Fontes (em `ferramentas/cache/isaias-caminha/`, fora do git; baixar de novo se sumirem)
- `bbm4808-1917.pdf`: 2ª ed., 1917 (edição-base), https://digital.bbm.usp.br/handle/bbm/4808 (001228_COMPLETO.pdf);
  «Breve notícia» nas p. 11–17 do PDF, romance 19–238, errata na 239. Página do livro = PDF − 4.
- `bbm4799-1909.pdf`: 1ª ed., 1909, https://digital.bbm.usp.br/handle/bbm/4799 (001179_COMPLETO.pdf); texto 11–319,
  errata 321–322.
- `c17.txt`, `c09.txt`: `pdftotext` dos dois PDFs (a camada de OCR da Brasiliana).
- `ws_moderno.json`: Wikisource pt (API, as 15 páginas): Breve notícia de 1917, mas o romance pelo texto de **1909**.
- `bveb.pdf`/`bveb.txt` (`pdftotext -layout`): Ática 1995, texto de **1917** sem a Breve notícia; perdeu muitos acentos.
- `tess-bbm4808-1917/`, `tess-bbm4799-1909/`: Tesseract psm 6 (`tesseract.py`, cabeçalho). `tess4-…`: psm 4 (não usado).

## Fluxo
```
python3 ferramentas/texto.py isaias-caminha            # 1917; relatórios em ferramentas/cache/isaias-caminha/relatorios/
python3 edicoes/isaias-caminha/pontos.py               # diferenças ainda não decididas contra a Ática -> pontos.tsv
python3 edicoes/isaias-caminha/conferir.py ferramentas/cache/isaias-caminha/relatorios/pontos-busca.tsv   # pranchas
python3 edicoes/isaias-caminha/edicao1909.py           # texto de 1909 (texto1909.pkl)
python3 edicoes/isaias-caminha/mudancas.py             # mudancas.json (lista 1909 -> 1917 da «Sobre»)
python3 ferramentas/texto.py isaias-caminha --publicar
```
Decisões: `conferencia.json` (364; chaves `c|antes¦atual¦depois` sobre o texto do confronto, ver `config.corrigir_lidos`),
`decisoes.py` (EMENDAS 'erro' de 1917, errata, linhas perdidas completadas por 1909; acentos; Loberant; versos;
itálicos), `notas.py` («Sobre»). Gravador de chaves: `~/.cache/claude-pedidos-2611/isaias-caminha/scripts/decidir.py`
(só neste PC).

## O que não ficou conferido (pode ter erro)
- Pontuação: só se conferiu nas imagens onde as palavras divergiam; vírgula × ponto e aspas soltas foram tratadas
  por regra (`config.varrer_pontuacao`, `decisoes.corrigir`). Restam umas 70 «palavra, Maiúscula», quase todas
  legítimas (vocativos, nomes), e alguns «palavra. minúscula».
- Paragrafação: vem da edição da Ática (bv) projetada sobre os OCRs; não foi conferida linha a linha com 1917.
- Itálicos: achados pela inclinação das letras (`italico.py`) e escolhidos por plausibilidade (estrangeirismos,
  títulos, falas citadas); não conferidos um a um nas imagens.
- Onde os dois OCRs de 1917 e a Ática concordam, não houve conferência (um erro comum aos três passaria).
- A lista das mudanças 1909 → 1917 só traz o que as duas leituras de cada edição e as duas modernas confirmam
  (198 itens + 26 trechos longos); muitas mudanças pequenas ficaram de fora.
- Vocabulário (Sonnet): definições inferidas do contexto, a rever se ele apontar: songamonga, quinau, compoteira,
  cavação, pedrês, mãos-abertas, pistolão, solitário, arroba («de arrobas»).
