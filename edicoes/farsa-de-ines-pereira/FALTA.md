# Farsa de Inês Pereira: o que falta

Branch `pedido-farsa-de-ines-pereira` (worktree `~/.cache/claude-wt27-farsa-de-ines-pereira`).
Trabalho de apoio (fac-símile, páginas, scripts) em `~/.cache/claude-pedidos-2711/farsa-de-ines-pereira/`.

## Fontes
- **Base: Copilação de 1562**, fac-símile da BNP (purl.pt/11494, PDF `res-175-a`, 534 pp.):
  a Farsa está nas pp. 440–454 do PDF (fól. CCXIIII v.º–CCXX v.º, «Auto de Ines Pereyra» … «Laus Deo»).
- Leitura auxiliar: reimpressão de Hamburgo (1834), tomo III, pp. 121–159 (IA `obrasvic03viceuoft`, OCR
  bom; 2ª cópia `obrasdegilvicen02vicegoog`, OCR ruim, só para desempate). OCR limpo de cabeçalhos em
  `colacao/ocr-1834-toronto.txt`.

## Etapas
1. [em andamento] Texto de 1834 passado a limpo e colacionado com 1562, coluna por coluna (dois
   Sonnet): `colacao/v1834-A.txt` + `colacao/colacao-A.tsv` (pp. 440–447) e `-B` (pp. 448–454).
2. Aplicar as lições de 1562 e passar à grafia de hoje (regras das Barcas) → `texto.txt`.
3. `publicar.py`, `CONVENCOES.md`, «Sobre esta edição», `revisao.json` (se houver decisão).
4. Vocabulário `edicoes/vocabulario/farsa-de-ines-pereira.json` (`conferir` ok).
5. Gerar e conferir o site na worktree (sem commitar `public/`).
