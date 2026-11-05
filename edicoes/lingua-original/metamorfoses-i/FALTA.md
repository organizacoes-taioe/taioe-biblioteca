# Metamorphoses I, 1–88: o que falta

- [x] texto latino (Magnus 1914, conferido nas imagens, pp. 5–11) e tradução de Castilho (1841, pp. 11–16, conferida)
- [x] obras.json e autor novo (`ovidio`) em conteudo/autores.js
- [x] glossario.json juntado (455 verbetes; `conferir` ok); falta a revisão das notas difíceis pelo principal
- [ ] revisao.json (Castilho ao lado; «fulgora» × «fulgura» no v. 56)
- [ ] `lingua_original.py conferir metamorfoses-i`, `publicar`, gerar e conferir o site; commitar só `conteudo/lingua-original.js`
      e `conteudo/ovidio/lingua-original.js` (não `public/`)

Como seguir: `python3 ferramentas/lingua_original.py palavras metamorfoses-i` dá as chaves; cada bloco de versos tem as chaves
que aparecem pela primeira vez nele.
