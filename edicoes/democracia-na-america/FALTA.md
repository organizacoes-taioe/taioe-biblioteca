# A democracia na América (seleção): o que falta

Branch `pedido-democracia-na-america`. **Pronta para publicar** (2026-11-12): texto francês conferido
(`original/LEIAME.md`, 91 pontos no fac-símile), tradução dos 14 arquivos (`traducao/`, conferida por
`checar.sh`: mesmos blocos, notas e sem mesóclise), `CONVENCOES.md`, `obra.py`, `revisao.json`
(8 decisões), vocabulário (`edicoes/vocabulario/democracia-na-america.json`, 31 verbetes), `conteudo/`
gravado por `traducoes.py democracia-na-america`; o site gera e o `conferir.mjs` dá «tudo certo».

Para o principal:
- autor novo `alexis-de-tocqueville` no fim de `conteudo/autores.js`: na junção, conferir o «});» entre
  autores novos (`autores-fix.py`);
- gerar, PR, Catálogo `obras`, merge; `traducoes_revisao.py --revisao` para as 8 decisões; tirar dos pedidos;
- notas gerais: ficam para os lotes.

Scripts fora do git, só neste PC: `~/.cache/claude-pedidos-0511/democracia-na-america/scripts/`
(`gut.sh` remonta `original/`; `checar.sh` confere as traduções).
