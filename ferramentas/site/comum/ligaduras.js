/* ────────────────────────────────────────────────────────────────
   ligaduras.js — o latim na tela com æ e œ (pedido do Gere, 29/10/2026:
   «sim, em tudo», nos Cards e na Biblioteca), como nas edições da Igreja
   (a Vulgata Clementina escreve cælum, cœpit, Israël). Os arquivos de
   origem continuam com «ae» e «oe»: a troca é só no que vai ao ar.

   Cópia idêntica em taioe-cards (fonte/latim/ligaduras.js) e em
   taioe-biblioteca (ferramentas/site/comum/ligaduras.js): mudou uma,
   mudar a outra.

   O «ae» e o «oe» viram æ e œ, menos no hiato, em que o «e» é outra sílaba
   e leva trema: Israël, poëta, aër, coëgit. Os hiatos são os da lista
   abaixo, tirada das 2.240 palavras com ae ou oe do latim dos dois sites
   (29/10/2026). Palavra nova em hiato entra nela.
   ──────────────────────────────────────────────────────────────── */
'use strict';

/* Cada regra casa com o começo da palavra (em minúsculas, sem acento) até o
   «e» do hiato, inclusive. */
const HIATOS = [
  /^(?:isra|isma|micha|rapha|nathana|misa|asa)e(?=l)/,   // os nomes hebraicos em -ael: Israël, Michaël
  /^[ij]oe(?=l)/,                                       // Ioël
  /^(?:noe|aloe)$/,                                     // Noë, aloë
  /^poe(?=t|m|s)/,                                      // poëta, poëma, poësis (pœna é ditongo)
  /^(?:in)?coe(?=g|rc|mpt|x|d|pisc|[aeiou])/,           // coëgit, coërceo, coëmptus, coëo (cœpit, cœlum e cœtus são ditongo)
  /^ae(?=r(?:is|e|em|a)?$|re(?:a|ae|am|as|i|is|o|orum|um|us)$|ri(?:a|ae|am|i|is|o|um|us)$)/  // aër, aëris, aërius (ærumna e ærugo são ditongo)
];

function ligarPalavra(w) {
  const m = w.toLowerCase();
  if (!/ae|oe/.test(m)) return w;
  const hiato = new Set();
  for (const re of HIATOS) {
    const r = re.exec(m);
    if (r) hiato.add(r.index + r[0].length - 1);
  }
  let saida = '';
  for (let i = 0; i < w.length; i++) {
    if ((m[i] === 'a' || m[i] === 'o') && m[i + 1] === 'e') {
      if (hiato.has(i + 1)) saida += w[i] + (w[i + 1] === 'E' ? 'Ë' : 'ë');
      else {
        const maiuscula = w[i] !== m[i];
        saida += m[i] === 'a' ? (maiuscula ? 'Æ' : 'æ') : (maiuscula ? 'Œ' : 'œ');
      }
      i++;
    } else saida += w[i];
  }
  return saida;
}

const PALAVRA = /[A-Za-z]+/g;

/* O texto todo em latim. Com «so», um Set de palavras em minúsculas: só elas
   mudam (para texto em que o latim vem no meio do português, como as notas). */
function ligar(texto, so) {
  return String(texto).replace(PALAVRA, w => (so && !so.has(w.toLowerCase()) ? w : ligarPalavra(w)));
}

/* As palavras de um texto latino que mudam (para montar o «so»). */
function palavrasQueMudam(texto) {
  return (String(texto).match(PALAVRA) || []).filter(w => ligarPalavra(w) !== w).map(w => w.toLowerCase());
}

module.exports = { ligar, ligarPalavra, palavrasQueMudam, HIATOS };
