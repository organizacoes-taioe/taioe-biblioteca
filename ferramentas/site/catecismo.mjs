// O Catecismo da Igreja Católica na Biblioteca Taioé (área Catolicismo).
//
// Os dados vêm de edicoes/catecismo/dados/, cópia fiel da pasta dados/ do site próprio do
// Catecismo (ver edicoes/catecismo/sincronizar.py): o manifesto (blocos, aberturas, subtítulos)
// e os pontos (trilha, corpo em HTML com as chamadas de nota, notas). O leitor é o mesmo do
// site antigo, em páginas estáticas:
//
//   .../catecismo-da-igreja-catolica/          rosto, índice (a partir das aberturas) e «Ir ao ponto»
//   .../catecismo-da-igreja-catolica/27/       o ponto 27: trilha, numeral, subtítulo, corpo, referências
//   .../catecismo-da-igreja-catolica/a27/      a abertura do tópico que começa no ponto 27
//   .../catecismo-da-igreja-catolica/sobre/    a origem do texto
//
// A navegação passa pelas aberturas, como no leitor antigo: … 26 → a27 → 27 → 28 …
// Os endereços são o próprio número do ponto e não mudam: não entram em enderecos.json.
// Para a busca, as partes da obra são os pontos; as aberturas são páginas de passagem. O estado de
// leitura guarda só a posição («Continuar: Ponto N») e a escolha manual da obra (lendo, lida), sem
// marca por ponto: milhares de marcas estourariam o limite de leituras.partes no banco (64 KB).
// No obras.json, a obra vai com q = [primeiro, último, 'Ponto'] em vez da lista dos pontos.

import fs from 'node:fs';
import path from 'node:path';

export const ID = 'catecismo-da-igreja-catolica';
export const TOTAL = 2865;                         // pontos do Catecismo inteiro
const NIVEIS = ['parte', 'secao', 'capitulo', 'artigo', 'paragrafo', 'topico'];
const RODAPE = 'Catecismo da Igreja Católica © Libreria Editrice Vaticana.';
const VATICANO = 'https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html';

const semTags = (s) => String(s || '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<')
  .replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
const PALAVRA = /[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu;

export function carregarCatecismo(raiz) {
  const dir = path.join(raiz, 'edicoes', 'catecismo', 'dados');
  const ler = (arq) => JSON.parse(fs.readFileSync(path.join(dir, arq), 'utf8'));
  if (!fs.existsSync(path.join(dir, 'manifesto.json'))) return null;
  const man = ler('manifesto.json');
  man.aberturas = man.aberturas || {};
  man.subtitulos = man.subtitulos || {};
  const pontos = {};
  man.blocos.forEach((b) => {
    const d = ler(b.file);
    for (let n = b.de; n <= b.ate; n++) {
      if (!d[n]) throw new Error(`catecismo: ponto ${n} anunciado em ${b.file}, mas ausente`);
      pontos[n] = d[n];
    }
  });
  const partes = [];
  let palavras = 0;
  for (let n = man.min; n <= man.max; n++) {
    const p = pontos[n];
    if (!p) throw new Error(`catecismo: falta o ponto ${n}`);
    const sub = man.subtitulos[n] || '';
    palavras += (semTags(sub + ' ' + p.body).match(PALAVRA) || []).length;
    // o texto da busca: subtítulo, corpo e notas (fonte e citação)
    const busca = [sub, p.body].concat(p.notes.map((x) => x.fonte + ' ' + (x.txt || ''))).map(semTags).join('\n\n');
    partes.push({ n: String(n), titulo: '', slug: String(n), texto: busca, ponto: p, num: n });
  }
  return {
    id: ID, autor: 'igreja-catolica', titulo: 'Catecismo da Igreja Católica', tituloCurto: 'Catecismo',
    ano: 1992, genero: 'Catecismo', divisao: { singular: 'ponto', plural: 'pontos' },
    descricao: 'A exposição da fé e da moral da Igreja, promulgada por São João Paulo II em 1992: ' +
      'a profissão da fé, os sacramentos, a vida em Cristo e a oração cristã.',
    rodape: RODAPE, _palavras: palavras, partes, catecismo: man,
    edicao: {
      apresentacao: `O _Catecismo da Igreja Católica_ foi promulgado por São João Paulo II em 11 de outubro de 1992, com a constituição apostólica _Fidei depositum_. A edição típica latina, com as correções definitivas, saiu em 1997.

O texto desta edição é a tradução portuguesa publicada pela Santa Sé no sítio vatican.va, com ajustes de português de Portugal para o Brasil.

Os direitos do texto são da Libreria Editrice Vaticana (© Libreria Editrice Vaticana). Ao contrário das outras obras desta biblioteca, o _Catecismo_ não está em domínio público.

Cada um dos ${TOTAL} pontos (os parágrafos numerados do _Catecismo_) tem página própria, com as referências embaixo. Quando a nota traz um texto que não aparece no corpo do ponto, esse texto vem junto da fonte; quando a citação já foi transcrita no corpo, a nota mostra só a fonte e uma etiqueta que o diz. Tocar no número de uma nota abre a referência ali mesmo. Entre um tópico e outro, uma página de abertura anuncia o que começa ali: parte, seção, capítulo, artigo, parágrafo ou tópico.

Por enquanto estão publicados os pontos ${man.min} a ${man.max}; os outros entram aos poucos.`,
      fontes: [{ nome: 'Catecismo da Igreja Católica, em vatican.va', url: VATICANO, nota: 'tradução portuguesa publicada pela Santa Sé' }]
    }
  };
}

/* As páginas da obra. h: as funções do gerar.mjs (pagina, esc, U, trilhaObra, jsonObra…). */
export function paginasCatecismo(a, o, h) {
  const { esc, U, SITE } = h;
  const man = o.catecismo, ab = man.aberturas, min = man.min, max = man.max;
  const chave = h.chaveObra(o), raiz = U.obra(o);
  const P = (n) => raiz + n + '/', A = (n) => raiz + 'a' + n + '/';
  const temAb = (n) => !!ab[n];
  const textoNivel = (x) => (x.rotulo ? x.rotulo + ': ' : '') + x.titulo;
  const tituloAb = (n) => textoNivel(ab[n].novos[0]);
  const autor = { '@type': 'Organization', name: a.nomeCompleto || a.nome };

  const trilha = (ultimo) => h.trilhaObra(a, o).concat({ txt: o.tituloCurto, href: raiz }, { txt: ultimo });
  const passo = (cls, rel, dir, alvo) => (alvo
    ? '<a class="passo ' + cls + '" href="' + alvo.url + '" rel="' + rel + '"><span class="dir">' + dir + '</span><span class="alvo">' + esc(alvo.txt) + '</span></a>'
    : '<span class="passo vazio"></span>');
  const indice = () => '<a class="passo seg" href="' + raiz + '"><span class="dir">Índice</span><span class="alvo">' + esc(o.tituloCurto) + '</span></a>';
  const irAoPonto = (sufixo) => '<form class="ir-ponto" id="ir-ponto" data-url="' + raiz + '" data-min="' + min + '" data-max="' + max + '"' +
    (sufixo === 'obra' ? ' data-aberturas="' + Object.keys(ab).join(' ') + '"' : '') + ' hidden>' +
    '<label for="ir-ponto-n">Ir ao ponto</label><input id="ir-ponto-n" type="number" inputmode="numeric" min="1" max="' + TOTAL + '" placeholder="' + min + '">' +
    '<button type="submit">Ir</button><span class="ir-aviso" id="ir-aviso" role="status"></span></form>';
  // a sequência do leitor: o que vem antes e depois de cada ponto e de cada abertura
  const pontoOuAbertura = (n) => (temAb(n) ? { url: A(n), txt: tituloAb(n) } : { url: P(n), txt: 'Ponto ' + n });

  // ---------------------------------------------------------------- rosto e índice
  {
    const entradas = [];
    Object.keys(ab).map(Number).sort((x, y) => x - y).forEach((n) => {
      ab[n].novos.forEach((x) => entradas.push({ k: NIVEIS.indexOf(x.nivel), x, de: n, filhos: [] }));
    });
    entradas.forEach((e, i) => {
      const prox = entradas.slice(i + 1).find((f) => f.k <= e.k && f.de > e.de);
      e.ate = prox ? prox.de - 1 : max < TOTAL ? null : max;     // null: continua nos pontos ainda não publicados
    });
    const topo = [], pilha = [];
    entradas.forEach((e) => {
      while (pilha.length && pilha[pilha.length - 1].k >= e.k) pilha.pop();
      (pilha.length ? pilha[pilha.length - 1].filhos : topo).push(e);
      pilha.push(e);
    });
    const faixa = (e) => '<span class="pontos">' + (e.ate === null ? e.de + '–…' : e.ate > e.de ? e.de + '–' + e.ate : e.de) + '</span>';
    const rotulo = (e) => (e.x.rotulo ? '<span class="rot">' + esc(e.x.rotulo) + '</span> ' : '') + '<span class="tit">' + esc(e.x.titulo) + '</span>';
    const lista = (es) => (es.length ? '<ol>' + es.map((e) => '<li class="nivel-' + e.x.nivel + '"><a href="' + A(e.de) + '">' + rotulo(e) + faixa(e) + '</a>' +
      lista(e.filhos) + '</li>').join('') + '</ol>' : '');
    const arvore = topo.map((e) => (e.x.nivel === 'parte'
      ? '<details class="parte-cat"><summary>' + rotulo(e) + faixa(e) + '</summary>' + lista(e.filhos) + '</details>'
      : '<ol>' + '<li class="nivel-' + e.x.nivel + '"><a href="' + A(e.de) + '">' + rotulo(e) + faixa(e) + '</a>' + lista(e.filhos) + '</li></ol>')).join('');
    const publicados = min === 1 && max === TOTAL ? '' : 'Publicados até agora: pontos ' + min + ' a ' + max + ', de ' + TOTAL + '.';
    const html = '<div class="folha catecismo"><header class="rosto"><p class="rosto-autor">' + esc(a.nome) + '</p><h1>' + esc(o.titulo) + '</h1>' +
      '<p class="meta">' + esc(h.fichaObra(o)) + '</p>' +
      (publicados ? '<p class="publicacao">' + esc(publicados) + '</p>' : '') +
      '<p class="descricao">' + esc(o.descricao) + '</p>' +
      '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
      '<p class="acoes"><a class="botao" id="comecar" href="' + pontoOuAbertura(min).url + '">Começar a ler</a> ' +
      '<a class="botao secundario" href="' + U.sobre(o) + '">' + esc(h.tituloSobre(o)) + '</a></p>' + irAoPonto('obra') +
      '<div class="estado-leitura" id="estado-leitura" data-alvo="obra" hidden></div></header>' +
      '<p class="secao-titulo">Índice</p><nav class="indice-cat" aria-label="Índice do Catecismo">' + arvore + '</nav></div>';
    h.pagina({ url: raiz, titulo: o.titulo, corpo: html, trilha: h.trilhaObra(a, o).concat({ txt: o.tituloCurto }), rodape: o.rodape,
      descricao: h.descricaoDe(o.descricao),
      dados: { pagina: 'obra', obra: chave, 'titulo-obra': o.titulo, total: o.partes.length, 'so-posicao': 1, primeira: String(min) },
      jsonld: { ...h.jsonObra(a, o), author: autor, copyrightHolder: { '@type': 'Organization', name: 'Libreria Editrice Vaticana' } } });
  }

  // ---------------------------------------------------------------- aberturas
  Object.keys(ab).map(Number).forEach((n) => {
    const x = ab[n];
    const contexto = x.contexto.length ? '<div class="contexto">' + x.contexto.map((t) => '<span>' + esc(t) + '</span>').join('') + '</div>' : '';
    const niveis = x.novos.map((v, k) => {
      const tag = k === 0 ? 'h1' : 'h2';
      return '<div class="nivel ' + v.nivel + '">' + (v.rotulo ? '<p class="rotulo">' + esc(v.rotulo) + '</p>' : '') +
        '<' + tag + ' class="titulo">' + esc(v.titulo) + '</' + tag + '></div>';
    }).join('<div class="elo"></div>');
    const prev = n > min ? { url: P(n - 1), txt: 'Ponto ' + (n - 1) } : null, next = { url: P(n), txt: 'Ponto ' + n };
    const html = '<article class="folha catecismo abertura-cat">' + contexto + '<div class="ornato"></div>' + niveis +
      '<p class="adiante">Ponto ' + n + ' em diante</p>' +
      '<nav class="passos" aria-label="Navegação entre os pontos">' + passo('ant', 'prev', '← Anterior', prev) + passo('seg', 'next', 'Seguinte →', next) + '</nav>' +
      '<p class="posicao"><a href="' + raiz + '">índice</a></p>' + irAoPonto() + '</article>';
    h.pagina({ url: A(n), titulo: tituloAb(n) + ' — ' + o.titulo, corpo: html, trilha: trilha('Abertura ' + n), rodape: o.rodape,
      prev: prev && prev.url, next: next.url, semSitemap: true,
      descricao: h.descricaoDe(`${o.titulo}, a partir do ponto ${n}: ` + x.contexto.concat(x.novos.map(textoNivel)).join(' · ') + '.'),
      dados: { pagina: 'abertura', obra: chave, 'url-obra': raiz } });
  });

  // ---------------------------------------------------------------- pontos
  o.partes.forEach((p) => {
    const n = p.num, d = p.ponto, sub = man.subtitulos[n];
    const trilhaPonto = d.trail.length ? '<p class="trilha-ponto">' + d.trail.map((t, k) =>
      '<span' + (k === d.trail.length - 1 ? ' class="aqui"' : '') + '>' + esc(t) + '</span>').join('') + '</p>' : '';
    const notas = d.notes.length ? '<section class="notas-ponto" aria-labelledby="ref-' + n + '"><h2 id="ref-' + n + '">Referências</h2>' +
      d.notes.map((x) => '<div class="nota-ponto" id="nota-' + x.n + '"><span class="n">' + x.n + '</span><div class="nota-corpo">' +
        '<p class="src">' + x.fonte + '</p>' + (x.txt ? '<div class="quoted">' + x.txt + '</div>' : '') +
        (x.tag ? '<span class="etiqueta">' + esc(x.tag) + '</span>' : '') + '</div></div>').join('') + '</section>' : '';
    const prev = temAb(n) ? { url: A(n), txt: tituloAb(n) } : n > min ? { url: P(n - 1), txt: 'Ponto ' + (n - 1) } : null;
    const next = n < max ? pontoOuAbertura(n + 1) : null;
    const html = '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
      '<article class="folha leitura catecismo ponto">' +
      '<header class="cabeca-ponto">' + trilhaPonto + '<h1 class="numeral"><span class="visualmente-oculto">Ponto </span>' + n + '</h1>' +
      '<div class="regua"></div>' + (sub ? '<h2 class="subtitulo-ponto">' + esc(sub) + '</h2>' : '') + '</header>' +
      '<div class="texto corpo-ponto">' + d.body + '</div>' + notas +
      '<div id="fim-parte" aria-hidden="true"></div>' +
      (n === TOTAL ? '<p class="fim">Fim</p>' : '') +
      '<nav class="passos" aria-label="Navegação entre os pontos">' + passo('ant', 'prev', '← Anterior', prev) +
      (next ? passo('seg', 'next', 'Seguinte →', next) : indice()) + '</nav>' +
      '<p class="posicao">Ponto ' + n + ' de ' + TOTAL + ' · <a href="' + raiz + '">índice</a></p>' + irAoPonto() + '</article>';
    h.pagina({ url: P(n), titulo: 'Ponto ' + n + ' — ' + o.titulo, corpo: html, trilha: trilha('Ponto ' + n), rodape: o.rodape,
      prev: prev && prev.url, next: next ? next.url : null, progresso: n / TOTAL,
      descricao: h.descricaoDe(`Catecismo, ${n}. ` + semTags(d.body)),
      dados: { pagina: 'parte', obra: chave, parte: p.slug, indice: n, total: TOTAL, ponto: n, 'so-posicao': 1,
        rotulo: 'Ponto ' + n, 'titulo-obra': o.titulo, 'url-obra': raiz },
      jsonld: { '@context': 'https://schema.org', '@type': 'Chapter', name: 'Ponto ' + n, position: n,
        isPartOf: { '@type': 'Book', name: o.titulo, url: SITE + raiz }, author: autor, inLanguage: 'pt-BR' } });
  });
}
