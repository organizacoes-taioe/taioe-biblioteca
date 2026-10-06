# PS 7 — notas da tradução

**Metro do original:** octossílabo francês, contado até a última tônica, com o *e* mudo final como +1; sem cesura fixa, apoio interno quase sempre na 5.ª (desenho 2-5-8), às vezes na 3.ª ou na 4.ª.

**Metro da tradução:** octossílabo português com a 4.ª obrigatória (`8: 4`), pela tabela do manual, já que o 2-5-8 do original não tem tradição em português.

**Rimas:** duas quadras ABAB, como no original: grave nos ímpares (*mansa / herança*; *imoladas / inebriadas*), aguda nos pares (*luz / Jesus*; *véu / Céu*). Oito versos, duas estrofes, como no original. Não há refrão nem acróstico.

**Escolhas e perdas.** Na 1.ª quadra, *doux langage* virou *fala mansa* (cede a palavra literal: «doce» não cabia com a rima); *partage* virou *herança*; *de tous les élus* perdeu o *todos* (ornamento), e *lá na luz* situa os eleitos no Céu sem acrescentar ideia nova. O paralelo *Des anges... / Des âmes...* ficou em *De anjos... / De almas...*. Na 2.ª quadra, *Carmel* (grave em português, *Carmelo*) não cabe na rima aguda que responde a *Céu*: o lugar ficou em *no claustro, sob o véu*, que mantém o contraste entre a vida no Carmelo e o Céu; é a única perda de nome do poema. *Au sein des sacrifices* virou *imoladas* (as carmelitas é que se oferecem em sacrifício; a restrição *ce n'est que* ficou em *Só nos podemos... amar*). *Enivrées de délices* virou *em gozo, inebriadas*, com o feminino plural de Teresa. O jogo *s'aimer / nous nous aimerons* ficou em *amar / nos amaremos*.

**Cabeçalho.** O título do arquivo-fonte é o primeiro verso; a tradução usa o primeiro verso traduzido. A epígrafe (Jo 15,12, que Teresa remete a «XVI-12») foi traduzida com a remissão como ela escreveu e posta numa linha `# epigrafe:`, chave que o § 6 não lista: proposta de acrescentá-la ao guia. O site antigo e o novo trazem o mesmo texto (o antigo, «nous» minúsculo no v. 8).

**Conferência:** `molde.mjs` — 8 versos: 8 exatos (✓), 0 aceitáveis (~), 0 falhos (✗), 0 fora da medida (≠); nenhuma «leitura natural tem N». Esqueletos: 1-4-6-8, 1-4-6-8, 2-4-6-8, 1-4-8 / 1-4-8, 2-4-8, 2-4-8, 4-6-8. Grep de mesóclise: nada.

**Revisão após a crítica** (substitui o que se diz acima sobre a 2.ª quadra):
- Vv. 5-6: «Só nos podemos, imoladas, / Amar no claustro, sob o véu» → «Só nos amamos, imoladas, / Cá no Carmelo, sob o véu»: o *Carmel* volta nomeado dentro do verso (a rima continua em *véu*), o *só* prende-se a *imoladas* (o sacrifício como condição), e *cá* responde ao *lá no Céu* do v. 8; cede o *peut* (*podemos* → *amamos*). `molde.mjs`: 8 ✓, 0 ~, 0 ✗, 0 ≠.
