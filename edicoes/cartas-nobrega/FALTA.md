# Cartas do Brasil (Nóbrega): estado

Branch `pedido-cartas-nobrega`. Não-ficção, «outras» (`/admin/sugestoes/`, pedido `cartas-nobrega`). Autor novo `manuel-da-nobrega`
(área `nao-ficcao`), gênero «Cartas». **Pronta para juntar e publicar** (12/11): 19 cartas, ~39,8 mil palavras.

## Fonte
- Base: *Cartas do Brasil do padre Manoel da Nobrega (1549–1560)* (Cartas Jesuíticas I), org. Alfredo do Valle Cabral (†1894), Rio de
  Janeiro, Imprensa Nacional, 1886. Fac-símile da Brasiliana USP, https://digital.bbm.usp.br/handle/bbm/8016 (PDF
  `45000009662_Output.o.pdf`; página impressa = página do PDF − 16); mesmo volume no Internet Archive (`cartaaaapdrmnelnobrg`,
  resolução menor, borda esquerda inteira). A edição da ABL de 1931 e a de Serafim Leite (protegida) não foram usadas.
- O volume traz 21 cartas; IV e VI são traduções do italiano feitas pelo editor e ficam de fora (19 cartas). O *Diálogo sobre a
  conversão do gentio* (Rev. do Inst. Hist., t. XLIII, 1880) e as cartas de 1561–1570 não estão no volume: ficam para depois (decisão
  `dialogo` do `revisao.json`).
- Downloads em `~/.cache/claude-pedidos-0511/cartas-nobrega/` (dl, pag, tess, voto, ver, conf; fora do git).

## Como refazer (na raiz do repo)
1. `ocr.py`: máscara JBIG2 de 900 dpi → leituras A (450 dpi, psm 4), B (600 dpi, psm 6) e C (camada de texto do PDF).
2. `voto.py` (voto por palavra; tira cabeçalho e notas de rodapé pela altura da letra) e `transcricao.py` (`1886/<p>.txt`; `<p>.cab` =
   primeira linha do corpo que a máscara tomou por cabeçalho).
3. Conferência nas imagens por subagentes Sonnet: `conferir_lista.py` + `preparar_lotes.py` (lotes 01–08, 1.269 linhas →
   `conferencia.json`), trechos suspeitos (lotes 09–10 → `correcoes.json`) e começo das linhas das 11 páginas cortadas na borda
   (lote 11). Um defeito sistemático: palavra hifenizada que o voto juntou fica duplicada no começo da linha seguinte
   (`montar.desduplicar`).
4. `montar.py --publicar` (grafia de hoje: `decisoes.py`; limites das cartas: `cartas.py`; latim: `decisoes.LATIM`), depois
   `vocabulario.py` (93 verbetes, `conferir` ok).

## Para o principal
- Gerar, Catálogo `obras` (obra nova) e `traducoes_revisao.py --revisao` (8 escolhas novas em `revisao.json`). Sem `_redirects`.
- Notas gerais: não feitas (vão por lotes). Limite do trabalho: nem todas as linhas foram vistas na imagem, só as suspeitas e as das
  páginas cortadas; erros de palavra que existe ainda podem restar (ver Armadilhas no guia).
