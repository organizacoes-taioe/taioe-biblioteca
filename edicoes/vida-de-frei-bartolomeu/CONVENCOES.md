# Vida de D. Frei Bertolameu dos Mártires — convenções desta edição

Frei Luís de Sousa, Viana, Nicolau Carvalho, 1619 (sobre os materiais de Frei Luís de Cácegas). Não-ficção,
gênero «Hagiografia», autor `frei-luis-de-sousa`. Endereço: `/frei-luis-de-sousa/vida-de-frei-bartolomeu/`.

## Edição-base e testemunhos
- **Base: 1619**, a única edição do autor, lida no exemplar da BNP (res-33-a, https://purl.pt/33227, PDF
  livre) e conferida no do Internet Archive (`bub_gb_ejJfgR_PmtQC`, Biblioteca Nacional Central de Roma).
- **Transcrição de trabalho**: as reimpressões da Tipografia Rolandiana (Lisboa): 1818, tomo I (Oxford,
  `vidadedfrbertol00sousgoog`) e 1850–1853, tomos I e II (Michigan, `vidadedfrbertol00luisgoog`,
  `vidadedfrbertol01luisgoog`). Servem para ler sem ſ e sem abreviaturas; onde diferem de 1619, vale 1619.
- Sete leituras por OCR (`ocr.py`, `testemunhos.py`): Tesseract nosso das cinco digitalizações e o OCR do
  Internet Archive de três delas. Referência da colação: o Tesseract do exemplar da BNP (ordem e completude de
  1619, e as coordenadas para a conferência).

## Texto
- Corpo: fólios 1–282 (páginas 19–582 do PDF da BNP); dedicatória «À Câmara e governo da notável vila de
  Viana» (pp. 15–17). Ficam de fora as aprovações e licenças dos censores (pp. 11–14) e a Taboada (pp.
  583–592), que só serviu para os títulos e a ordem dos capítulos (`taboada/taboada-1619.tsv`).
- Divisão de 1619: seis livros, 177 capítulos (27, 34, 30, 30, 30, 26). Uma página por capítulo.
- **Parágrafos**: 1619 corre cada capítulo num bloco só, sem parágrafos; assim fica (decisão nas pendências).
- Títulos dos capítulos: os do corpo; a Taboada desempata.
- Citações latinas (itálico em 1619): em itálico, sem mudança de grafia (`latim.py`).
- Citações à margem (lugares da Escritura e dos autores): notas do autor no fim do capítulo.

## Grafia (decisoes.py, grafia.py)
- Grafia de hoje, forma brasileira, sem trocar palavra: he → é, hum/hũa → um/uma, Deos → Deus, foy → foi,
  muyto → muito, polo/polla → pelo/pela, pera → para, assi → assim, despois → depois, cousa → coisa,
  dous → dois, oje → hoje, avia → havia, -ão átono → -am (erão → eram), -eo → -eu (respondeo → respondeu),
  sintir → sentir, minino → menino, fogir → fugir (forma arcaica de palavra atual).
- Pronome pegado ao verbo em 1619 ganha hífen (fezlhes → fez-lhes; dirseha → dir-se-á: a mesóclise do autor fica).
- Palavras que não se usam mais ficam e ganham verbete no vocabulário.
- Nomes de pessoas e lugares na forma de hoje (Bertolameu → Bartolomeu, Hespanha → Espanha); «el-rei».
