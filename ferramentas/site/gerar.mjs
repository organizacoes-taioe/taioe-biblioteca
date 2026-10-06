// Gera a Biblioteca Taioé estática em public/biblioteca/ (PLANO, etapa 4):
// uma página HTML pronta para cada área, autor, gênero, pasta de poemas, obra, parte e
// «Sobre esta edição», com endereço fixo, título e descrição próprios, sitemap e dados
// estruturados. Funciona sem JavaScript; o js/leitor.js só acrescenta as preferências,
// original e tradução, as setas do teclado e a posição de leitura.
//
//   node ferramentas/site/gerar.mjs
//
// Lê o mesmo conteudo/ do site antigo, na ordem do index.html antigo. A marcação do texto
// sai das mesmas funções do js/app.js antigo, só com os endereços trocados. Os endereços das
// partes ficam congelados em ferramentas/site/enderecos.json: uma parte nunca muda de endereço.
// Também grava ferramentas/sql/obras.sql (o catálogo, aplicado pelo workflow do taioe-infra).
// Sem dependências: Node 20+.

import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const SAIDA = path.join(RAIZ, 'public', 'biblioteca');
const BASE = '/biblioteca/';
const SITE = 'https://taioe.com.br';
const ARQ_ENDERECOS = path.join(RAIZ, 'ferramentas', 'site', 'enderecos.json');
const ARQ_SQL = path.join(RAIZ, 'ferramentas', 'sql', 'obras.sql');

// ------------------------------------------------------------------ carregar o conteúdo
const dados = { autores: [], obras: [], porId: {} };
function registrar(o) {
  if (dados.porId[o.id]) throw new Error('obra repetida: ' + o.id);
  dados.obras.push(o);
  dados.porId[o.id] = o;
}
const BIBLIOTECA = {
  autor(a) { dados.autores.push(a); },
  obra: registrar,
  poemas(pac) {
    pac.poemas.forEach((p, k) => {
      const l = p.livro >= 0 ? pac.livros[p.livro] : null;
      registrar({
        id: p.id, autor: pac.autor, titulo: p.titulo, genero: 'Poesia', poema: true,
        forma: p.forma, n: p.n || '', secao: p.secao || '', subtitulo: p.subtitulo || '',
        ano: p.ano || (l && l.ano) || null, versos: p.versos, lingua: p.lingua || '',
        traducao: p.traducao || null,
        coletanea: l ? { id: pac.autor + '/' + l.id, titulo: l.titulo, ano: l.ano || '', ordem: k, seq: p.livro } : null,
        ordem: k,
        divisao: { singular: 'parte', plural: 'partes' },
        partes: (p.partes || [{}]).map((x) => ({ n: '', titulo: x.titulo || '' })),
        arquivo: pac.arquivo
      });
    });
  },
  textos(mapa) {
    Object.keys(mapa).forEach((id) => {
      const o = dados.porId[id], e = mapa[id];
      if (!o) return;
      e.t.forEach((t, i) => {
        if (!o.partes[i]) o.partes[i] = { n: '', titulo: '' };
        o.partes[i].texto = t;
        if (e.o) o.partes[i].original = e.o[i];
      });
      if (e.e) o.edicao = e.e;
      o.carregada = true;
    });
  }
};
const ctx = vm.createContext({ BIBLIOTECA });
// Sempre com LF: no Windows o Git entrega CRLF, e o resultado tem de ser igual ao do GitHub.
const lerLf = (arq) => fs.readFileSync(arq, 'utf8').replace(/\r\n/g, '\n');
function rodar(rel) { vm.runInContext(lerLf(path.join(RAIZ, rel)), ctx, { filename: rel }); }

const indiceAntigo = lerLf(path.join(RAIZ, 'index.html'));
const scripts = [...indiceAntigo.matchAll(/<script[^>]*src="(conteudo\/[^"]+)"/g)].map((m) => m[1]);
scripts.forEach(rodar);
[...new Set(dados.obras.filter((o) => o.arquivo && !o.carregada).map((o) => o.arquivo))].forEach(rodar);
dados.obras.forEach((o) => {
  o.partes.forEach((p, i) => { if (p.texto === undefined) throw new Error(`sem texto: ${o.id} parte ${i + 1}`); });
});

// ------------------------------------------------------------------ marcação (do app.js antigo)
function esc(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function inline(s) {
  return esc(s)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/_([^_]+)_/g, '<em>$1</em>')
    .replace(/\s*\{§ ([^}]+)\}\s*/g, (m, x) => ' <span class="folha-ms" title="capítulo e seção">' + x + '</span> ')
    .replace(/\s*\{Ms ([A-C]) (\d+)([rv]?)\}\s*/g, (m, ms, f, l) =>
      ' <span class="folha-ms" title="Manuscrito ' + ms + ', folha ' + f + (l === 'r' ? ' recto' : l === 'v' ? ' verso' : '') + '">' + ms + ' ' + f + l + '</span> ')
    .replace(/^ | $/g, '');
}
function textoPuro(s) { return String(s || '').replace(/\{[^}]*\}/g, '').replace(/[_*]/g, '').replace(/\s+/g, ' ').trim(); }

function blocos(texto) {
  const todos = String(texto).trim().split(/\n\s*\n/);
  const notas = todos.filter((b) => /^¤ /.test(b));
  let html = paragrafos(todos.filter((b) => !/^¤ /.test(b)));
  if (notas.length) {
    html += '\n<aside class="nota-do-autor"><p class="rotulo">' + (notas.length > 1 ? 'Notas do autor' : 'Nota do autor') + '</p>' +
      paragrafos(notas.map((b) => b.replace(/^¤ /, ''))) + '</aside>';
  }
  return html;
}
function paragrafos(lista) {
  return lista.map((b) => {
    if (/^## /.test(b)) return '<p class="cena">' + inline(b.slice(3).trim()) + '</p>';
    if (/^@ /.test(b)) return '<p class="fala">' + inline(b.slice(2).trim()) + '</p>';
    const linhas = b.split('\n');
    if (linhas.every((l) => /^\|\s?/.test(l))) {
      return '<p class="verso">' + linhas.map((l) => inline(l.replace(/^\|\s?/, ''))).join('<br>') + '</p>';
    }
    const p = b.replace(/\s*\n\s*/g, ' ').trim();
    const cls = /^[a-zà-ÿ]/.test(p) ? ' class="continua"' : '';
    return '<p' + cls + '>' + inline(p) + '</p>';
  }).join('\n');
}
function blocosPoema(texto) {
  const bl = []; let estrofe = null, branco = true;
  String(texto || '').split('\n').forEach((l) => {
    if (!l.trim()) { estrofe = null; branco = true; return; }
    const m = /^::(\w+)\s?(.*)$/.exec(l);
    if (m) { bl.push({ marca: m[1], valor: m[2].trim(), sep: branco }); estrofe = null; branco = false; return; }
    if (!estrofe) { estrofe = { versos: [], sep: branco }; bl.push(estrofe); }
    estrofe.versos.push(l);
    branco = false;
  });
  return bl;
}
const SEPARADORES = { 'filete': '<span class="fio"></span>', 'fio horizontal': '<span class="fio"></span>',
  'linha de pontos': '. . . . . . . . . . .' };
function htmlMarca(b) {
  const v = b.valor;
  switch (b.marca) {
    case 'epigrafe': return v.split(/\s+\/\s+/).map(inline).join('<br>');
    case 'separador': return SEPARADORES[v] || esc(v || '*');
    case 'lacuna': return '. . . . . . . . . . .';
    case 'pagina': return '';
    default: return inline(v);
  }
}
function linhasPoema(texto) {
  return blocosPoema(texto).map((b) => {
    if (b.marca) return { sep: b.sep, linhas: [{ cls: 'm m-' + b.marca, html: htmlMarca(b) }] };
    return { sep: b.sep, linhas: b.versos.map((v) => ({ cls: 'v', html: inline(v) })) };
  });
}
function linhasProsa(texto) {
  const todos = String(texto || '').trim().split(/\n\s*\n/).filter(Boolean);
  const corpo = todos.filter((b) => !/^¤ /.test(b));
  const notas = todos.filter((b) => /^¤ /.test(b));
  const linhas = corpo.map((b) => ({ sep: false, linhas: [{ cls: 'p', html: paragrafos([b]) }] }));
  if (notas.length) {
    linhas.push({ sep: false, linhas: [{ cls: 'p nota-do-autor', html: '<p class="rotulo">' + (notas.length > 1 ? 'Notas do autor' : 'Nota do autor') + '</p>' +
      paragrafos(notas.map((b) => b.replace(/^¤ /, ''))) }] });
  }
  return linhas;
}
function grade(ladoTrad, ladoOrig, lingua) {
  const n = Math.max(ladoTrad.length, ladoOrig ? ladoOrig.length : 0); let html = '', i = 0;
  for (let b = 0; b < n; b++) {
    const bt = ladoTrad[b] || { linhas: [] }, bo = ladoOrig ? ladoOrig[b] || { linhas: [] } : { linhas: [] };
    const m = Math.max(bt.linhas.length, bo.linhas.length);
    const sep = b > 0 && (bt.sep || bo.sep) ? ' ini' : '';
    for (let j = 0; j < m; j++, i++) {
      const ini = j === 0 ? sep : '';
      if (ladoOrig) html += celula('orig', bo.linhas[j], ini, i, lingua);
      html += celula('trad', bt.linhas[j], ini, i, '');
    }
  }
  return html;
}
function celula(lado, l, ini, i, lingua) {
  if (!l) return '<div class="' + lado + ' vazio' + ini + '" data-i="' + i + '"></div>';
  return '<div class="' + lado + ' ' + l.cls + ini + '" data-i="' + i + '"' + (lingua ? ' lang="' + lingua + '"' : '') + '>' + l.html + '</div>';
}
function textoParte(o, p) {
  const poema = !!o.poema;
  const linhas = poema ? linhasPoema : linhasProsa;
  const orig = p.original !== undefined && p.original !== null;
  const lingua = orig && o.traducao ? o.traducao.codigo || '' : '';
  const cls = 'paralelo ' + (poema ? 'poema' : 'prosa');
  const attr = o.lingua && !orig ? ' lang="' + esc(o.lingua) + '"' : '';
  if (!orig && !poema) return '<div class="texto">' + blocos(p.texto) + '</div>';
  return '<div class="texto"><div class="' + cls + '"' + attr + '>' +
    grade(linhas(p.texto), orig ? linhas(p.original) : null, lingua) + '</div></div>';
}
function incipit(texto, limite) {
  const t = String(texto).replace(/\{[^}]*\}/g, '').replace(/^\|\s?/gm, '').replace(/[_*]/g, '').replace(/\s+/g, ' ').trim();
  if (t.length <= limite) return esc(t);
  let corte = t.slice(0, limite);
  corte = corte.slice(0, corte.lastIndexOf(' '));
  return esc(corte) + '…';
}
const plural = (n, s, p) => n + ' ' + (n === 1 ? s : p);
const numeradas = (o) => o.partes.filter((p) => p.n).length || o.partes.length;
const rotuloPasso = (p) => [esc(p.n), p.titulo ? inline(p.titulo) : ''].filter(Boolean).join(' · ');

const GENEROS = ['Romance', 'Novela', 'Contos', 'Autobiografia', 'Hagiografia', 'Ensaio', 'Poesia', 'Teatro',
  'Cartas', 'Orações', 'Crônica', 'Crítica', 'Tradução'];
const PLURAIS = { 'Romance': 'Romances', 'Novela': 'Novelas', 'Contos': 'Contos', 'Poesia': 'Poesia',
  'Teatro': 'Teatro', 'Crônica': 'Crônicas', 'Crítica': 'Crítica', 'Tradução': 'Traduções',
  'Autobiografia': 'Autobiografia', 'Cartas': 'Cartas', 'Orações': 'Orações',
  'Hagiografia': 'Hagiografia', 'Ensaio': 'Ensaios' };
const AREAS = [{ id: 'literatura', nome: 'Literatura' }, { id: 'catolicismo', nome: 'Catolicismo' }];
const areaDe = (a) => a.area || 'literatura';
const acharArea = (id) => AREAS.find((x) => x.id === id) || null;
const nomeGenero = (g) => PLURAIS[g] || g;
const slug = (s) => String(s).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
const slugGenero = (g) => slug(nomeGenero(g));

const PALAVRA = /[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu;
function palavras(o) {
  if (o._palavras === undefined) {
    o._palavras = o.partes.reduce((n, p) => n + (String(p.texto).replace(/[_*|]/g, ' ').match(PALAVRA) || []).length, 0);
  }
  return o._palavras;
}
const milhar = (n) => n.toLocaleString('pt-BR');
function fichaObra(o) {
  const d = o.divisao || { singular: 'parte', plural: 'partes' };
  if (o.poema) {
    return [o.partes.length > 1 ? plural(o.partes.length, d.singular, d.plural) : '',
      o.versos === 1 ? '1 verso' : milhar(o.versos) + ' versos'].filter(Boolean).join(' · ');
  }
  if (o.coletanea) {
    return [o.partes.length > 1 ? plural(numeradas(o), d.singular, d.plural) : '', milhar(palavras(o)) + ' palavras'].filter(Boolean).join(' · ');
  }
  return [o.datas || (o.ano ? String(o.ano) : ''), plural(numeradas(o), d.singular, d.plural), milhar(palavras(o)) + ' palavras'].filter(Boolean).join(' · ');
}
const textoPublicacao = (o) => (o.publicacao ? 'Primeira publicação: ' + o.publicacao : '');
const daColetanea = (o) => dados.obras.filter((x) => x.coletanea && x.coletanea.id === o.coletanea.id)
  .sort((a, b) => a.coletanea.ordem - b.coletanea.ordem);
function livros(obras) {
  const vistos = {};
  obras.forEach((o) => { vistos[o.coletanea ? 'c:' + o.coletanea.id : o.id] = 1; });
  return Object.keys(vistos).length;
}
const TEXTOS = { 'Contos': ['conto', 'contos'], 'Poesia': ['poema', 'poemas'] };
function porColetanea(obras) {
  const grupos = [], idx = {};
  obras.forEach((o) => {
    const k = o.coletanea ? o.coletanea.id : '';
    if (!(k in idx)) {
      idx[k] = grupos.length;
      grupos.push({ titulo: o.coletanea ? o.coletanea.titulo : '', ano: o.coletanea ? o.coletanea.ano : o.ano,
        seq: o.poema ? (o.coletanea ? o.coletanea.seq : 1e6) : null, obras: [] });
    }
    grupos[idx[k]].obras.push(o);
  });
  grupos.forEach((g) => g.obras.sort((a, b) => {
    if (a.poema && b.poema) return a.ordem - b.ordem;
    return a.coletanea && b.coletanea ? a.coletanea.ordem - b.coletanea.ordem : 0;
  }));
  return grupos.sort((a, b) => (a.seq !== null && b.seq !== null ? a.seq - b.seq : (a.ano || 0) - (b.ano || 0)));
}
const FORMAS = [{ id: 'sonetos', nome: 'Sonetos' }, { id: 'apologos', nome: 'Apólogos' }, { id: 'liras', nome: 'Liras' },
  { id: 'odes', nome: 'Odes' }, { id: 'verso-livre', nome: 'Verso livre' }, { id: 'outras', nome: 'Outras formas' }];
const acharForma = (id) => FORMAS.find((f) => f.id === id) || null;
const pastasDe = (obras) => FORMAS.map((f) => ({ forma: f, obras: obras.filter((o) => (o.forma || 'outras') === f.id) })).filter((x) => x.obras.length);
const poesiaDe = (autorId) => dados.obras.filter((o) => o.autor === autorId && o.genero === 'Poesia');
const acharAutor = (id) => dados.autores.find((a) => a.id === id) || null;
const obrasDe = (autorId) => dados.obras.filter((o) => o.autor === autorId)
  .sort((a, b) => (a.ano || 0) - (b.ano || 0) || a.titulo.localeCompare(b.titulo, 'pt'));
function generosDe(autorId) {
  const grupos = {};
  obrasDe(autorId).forEach((o) => { const g = o.genero || 'Outros'; (grupos[g] = grupos[g] || []).push(o); });
  return GENEROS.filter((g) => grupos[g])
    .concat(Object.keys(grupos).filter((g) => GENEROS.indexOf(g) < 0).sort())
    .map((g) => ({ genero: g, obras: grupos[g] }));
}
function soPoesia(autorId) { const g = generosDe(autorId); return g.length === 1 && g[0].genero === 'Poesia'; }
const autoresOrdenados = () => dados.autores.slice().sort((a, b) => (a.ordem || a.nome).localeCompare(b.ordem || b.nome, 'pt'));
const autoresDaArea = (id) => autoresOrdenados().filter((a) => areaDe(a) === id);
function vizinhosPoema(o) {
  let lista = [];
  porColetanea(poesiaDe(o.autor).filter((x) => (x.forma || 'outras') === (o.forma || 'outras'))).forEach((g) => { lista = lista.concat(g.obras); });
  return lista;
}
function rotuloParte(obra, parte) {
  if (!parte.n && !parte.titulo) return obra.titulo;
  if (!parte.n) return textoPuro(parte.titulo);
  if (obra.divisao && obra.divisao.rotulo === 'n') return parte.n;
  if (obra.divisao && obra.divisao.rotulo === 'nome') return textoPuro(parte.titulo || parte.n);
  if (obra.divisao && obra.divisao.rotulo === 'titulo') return textoPuro(parte.titulo) + ', ' + parte.n;
  const d = obra.divisao ? obra.divisao.singular : 'parte';
  return d.charAt(0).toUpperCase() + d.slice(1) + ' ' + parte.n;
}
const tituloSobre = (o) => (o.edicao && o.edicao.titulo) || 'Sobre esta edição';
const umaParte = (o) => (o.coletanea || o.poema) && o.partes.length === 1;

// ------------------------------------------------------------------ endereços (congelados)
const RESERVADOS = new Set(['css', 'js', 'vendor', 'sitemap.xml', '404.html', 'obras.json', 'favicon.svg', ...AREAS.map((a) => a.id)]);
const congelados = fs.existsSync(ARQ_ENDERECOS) ? JSON.parse(lerLf(ARQ_ENDERECOS)) : {};
const enderecos = {};
function slugParte(o, p, i) {
  const ag = o.divisao && (o.divisao.agrupar || o.divisao.rotulo === 'titulo');
  let s = slug(ag ? `${p.n} ${textoPuro(p.titulo)}` : p.n ? p.n : textoPuro(p.titulo));
  if (s.length > 50) s = s.slice(0, 50).replace(/-[^-]*$/, '');
  return s || 'parte-' + (i + 1);
}
dados.obras.forEach((o) => {
  if (umaParte(o)) return;
  const antes = congelados[o.id] || {}, agora = {}, usados = new Set(Object.values(antes));
  const vistos = {};
  o.partes.forEach((p, i) => {
    let marca = `${p.n}|${textoPuro(p.titulo)}`;
    vistos[marca] = (vistos[marca] || 0) + 1;
    if (vistos[marca] > 1) marca += '#' + vistos[marca];
    let s = antes[marca];
    if (!s) {
      const base = slugParte(o, p, i);
      s = base;
      for (let k = 2; usados.has(s) || s === 'sobre'; k++) s = base + '-' + k;
      usados.add(s);
    }
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(s) || s.length > 60) throw new Error(`endereço inválido: ${o.id}/${s}`);
    agora[marca] = s;
    p.slug = s;
  });
  enderecos[o.id] = agora;
});

// O endereço da obra é o id sem o nome do autor repetido no começo
// ("machado-de-assis-americanas-lua-nova" → "americanas-lua-nova"), único dentro do autor.
dados.obras.forEach((o) => {
  const pref = o.autor + '-';
  o.url = o.id.startsWith(pref) && o.id.length > pref.length ? o.id.slice(pref.length) : o.id;
});
dados.autores.forEach((a) => {
  const vistos = {};
  dados.obras.filter((o) => o.autor === a.id).forEach((o) => {
    if (vistos[o.url]) o.url = o.id;                    // colisão: fica o id inteiro
    vistos[o.url] = true;
  });
});

const U = {
  capa: () => BASE,
  area: (id) => BASE + id + '/',
  autor: (a) => BASE + a.id + '/',
  genero: (a, g) => BASE + a.id + '/' + slugGenero(g) + '/',
  pasta: (a, f) => BASE + a.id + '/poesia/' + f + '/',
  obra: (o) => BASE + o.autor + '/' + o.url + '/',
  parte: (o, i) => (umaParte(o) ? U.obra(o) : U.obra(o) + o.partes[i - 1].slug + '/'),
  sobre: (o) => U.obra(o) + 'sobre/'
};
U.poesia = (a) => (soPoesia(a.id) ? U.autor(a) : U.genero(a, 'Poesia'));
U.indicePoema = (a, o) => (pastasDe(poesiaDe(a.id)).length > 1 ? U.pasta(a, o.forma || 'outras') : U.poesia(a));
const chaveObra = (o) => o.autor + '/' + o.url;

// colisões: dentro de cada autor, obras × gêneros × "poesia"; autores × reservados
dados.autores.forEach((a) => {
  if (RESERVADOS.has(a.id)) throw new Error('autor com nome reservado: ' + a.id);
  const nomes = new Set(generosDe(a.id).map((x) => slugGenero(x.genero)));
  obrasDe(a.id).forEach((o) => { if (nomes.has(o.url)) throw new Error(`obra com o nome de um gênero: ${a.id}/${o.url}`); });
});

// ------------------------------------------------------------------ moldura das páginas
const hash = (s) => crypto.createHash('sha256').update(s).digest('hex').slice(0, 8);
const CSS = lerLf(path.join(RAIZ, 'ferramentas', 'site', 'estilo.css'));
const LEITOR = lerLf(path.join(RAIZ, 'ferramentas', 'site', 'leitor.js'));
const V_CSS = hash(CSS), V_JS = hash(LEITOR);

function trilhaHtml(itens) {
  return itens.map((it) => (it.href ? '<a href="' + it.href + '">' + esc(it.txt) + '</a>' : '<span aria-current="page">' + esc(it.txt) + '</span>'))
    .join('<span class="sep">›</span>');
}
function comArea(a, itens) {
  const ar = a && acharArea(areaDe(a));
  return ar ? [{ txt: ar.nome, href: U.area(ar.id) }].concat(itens) : itens;
}
function descricaoDe(t) { const s = textoPuro(t); return s.length > 155 ? s.slice(0, 154).replace(/\s+\S*$/, '') + '…' : s; }

const sitemap = [];
let paginas = 0;
function gravar(url, html) {
  const dir = path.join(SAIDA, url.slice(BASE.length));
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), html);
  paginas++;
}
function pagina(o) {
  const titulo = o.titulo ? o.titulo + ' · Biblioteca Taioé' : 'Biblioteca Taioé';
  const ds = o.dados ? Object.entries(o.dados).map(([k, v]) => ` data-${k}="${esc(v)}"`).join('') : '';
  const html = `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(titulo)}</title>
<meta name="description" content="${esc(o.descricao || 'Biblioteca Taioé: clássicos em português, abertos a todos.')}">
<link rel="canonical" href="${SITE}${o.url}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="${BASE}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="${BASE}css/estilo.css?v=${V_CSS}">
${o.prev ? `<link rel="prev" href="${o.prev}">\n` : ''}${o.next ? `<link rel="next" href="${o.next}">\n` : ''}<script defer src="${BASE}js/leitor.js?v=${V_JS}"></script>
${o.jsonld ? `<script type="application/ld+json">${JSON.stringify(o.jsonld).replace(/</g, '\\u003c')}</script>\n` : ''}</head>
<body${ds}>
<a class="pular" href="#app">Ir para o texto</a>

<header class="topo">
  <div class="topo-int">
    <a class="marca" href="${BASE}">Biblioteca</a>
    <nav class="topo-nav" id="trilha" aria-label="Trilha de navegação">${trilhaHtml(o.trilha || [])}</nav>
    <div class="ferramentas">
      <button type="button" id="fonte-menos" class="btn" aria-label="Diminuir a letra" title="Diminuir a letra" hidden>A−</button>
      <button type="button" id="fonte-mais" class="btn" aria-label="Aumentar a letra" title="Aumentar a letra" hidden>A+</button>
      <button type="button" id="tema" class="btn" aria-label="Alternar tema claro e escuro" title="Alternar tema" hidden>◐</button>
    </div>
  </div>
${o.bilingue ? `  <div class="idiomas" id="idiomas" hidden>
    <div class="idiomas-int" role="group" aria-label="Textos visíveis: original e tradução">
      <button type="button" class="idioma" data-lado="orig" aria-pressed="false" title="Mostrar ou esconder o original">${esc(o.bilingue)}</button>
      <button type="button" class="idioma" data-lado="trad" aria-pressed="true" title="Mostrar ou esconder a tradução">Português</button>
    </div>
  </div>
` : ''}${o.progresso !== undefined ? `  <div class="barra-progresso" id="progresso" data-frac="${o.progresso.toFixed(4)}" hidden><span></span></div>\n` : ''}</header>

<main id="app" tabindex="-1">
${o.corpo}
</main>

<footer class="rodape">
  <p>Textos em domínio público. <a href="/">Taioé</a> · <a href="/privacidade/">Privacidade</a> · <a href="/termos/">Termos de uso</a></p>
</footer>
</body>
</html>
`;
  gravar(o.url, html);
  if (!o.semSitemap) sitemap.push(o.url);
}

// ------------------------------------------------------------------ páginas
function paginaCapa() {
  let html = '<div class="folha capa"><h1>Biblioteca</h1><p class="subtitulo">Textos em domínio público</p></div><div class="folha">' +
    '<div id="retomar"></div>' +
    '<p class="aviso-conta" id="aviso-conta">Sua posição de leitura fica salva só neste navegador. ' +
    '<a href="/entrar/?voltar=%2Fbiblioteca%2F">Entre com seu email</a> para guardá-la em qualquer aparelho.</p>' +
    '<p class="secao-titulo">Acervo</p>';
  AREAS.forEach((ar) => {
    const autores = autoresDaArea(ar.id), generos = [];
    autores.forEach((a) => generosDe(a.id).forEach((x) => { if (generos.indexOf(x.genero) < 0) generos.push(x.genero); }));
    generos.sort((x, y) => GENEROS.indexOf(x) - GENEROS.indexOf(y));
    html += '<a class="cartao pasta area" href="' + U.area(ar.id) + '">' +
      '<span class="cartao-titulo">' + esc(ar.nome) + '</span>' +
      '<span class="cartao-meta">' + (autores.length ? plural(autores.length, 'autor', 'autores') : 'em preparação') + '</span>' +
      (generos.length ? '<span class="cartao-texto">' + generos.map((g) => esc(nomeGenero(g))).join(' · ') + '</span>' : '') + '</a>';
  });
  html += '</div>';
  pagina({ url: U.capa(), titulo: '', corpo: html, trilha: [], dados: { pagina: 'capa' },
    descricao: 'Biblioteca Taioé: romances, contos, poesia e obras católicas em português, abertos a todos, para ler capítulo por capítulo.',
    jsonld: { '@context': 'https://schema.org', '@type': 'WebSite', name: 'Biblioteca Taioé', url: SITE + BASE, inLanguage: 'pt-BR' } });
}

function paginaArea(ar) {
  let html = '<div class="folha"><header class="cabeca"><h1>' + esc(ar.nome) + '</h1></header><p class="secao-titulo">Autores</p>';
  autoresDaArea(ar.id).forEach((a) => {
    const obras = obrasDe(a.id), prosa = obras.filter((o) => !o.poema), versos = obras.length - prosa.length;
    const conta = [prosa.length ? plural(livros(prosa), 'obra', 'obras') : '', versos ? plural(versos, 'poema', 'poemas') : ''].filter(Boolean).join(' · ') || '0 obras';
    html += '<a class="cartao" href="' + U.autor(a) + '"><span class="cartao-titulo">' + esc(a.nome) + '</span>' +
      '<span class="cartao-meta">' + esc(a.vida || '') + (a.vida ? ' · ' : '') + conta + '</span>' +
      (obras.length ? '<span class="cartao-texto">' + generosDe(a.id).map((x) => esc(nomeGenero(x.genero))).join(' · ') + '</span>' : '') + '</a>';
  });
  html += '</div>';
  pagina({ url: U.area(ar.id), titulo: ar.nome, corpo: html, trilha: [{ txt: ar.nome }],
    descricao: `${ar.nome} na Biblioteca Taioé: ${autoresDaArea(ar.id).map((a) => a.nome).join(', ')}.` });
}

function cabecaAutor(a) {
  return '<header class="cabeca"><h1>' + esc(a.nome) + '</h1>' +
    '<p class="meta">' + esc([a.nomeCompleto, a.vida].filter(Boolean).join(' · ')) + '</p>' +
    (a.nota ? '<p class="nota-autor">' + inline(a.nota) + '</p>' : '') + '</header>';
}
function htmlPastas(a, obras) {
  const pastas = pastasDe(obras);
  if (pastas.length === 1) return htmlListaPoemas(pastas[0].obras);
  let html = '<p class="secao-titulo">Formas</p>';
  pastas.forEach((x) => {
    const titulos = [];
    porColetanea(x.obras).forEach((g) => { if (g.titulo && titulos.indexOf(g.titulo) < 0) titulos.push(g.titulo); });
    html += '<a class="cartao pasta" href="' + U.pasta(a, x.forma.id) + '"><span class="cartao-titulo">' + esc(x.forma.nome) + '</span>' +
      '<span class="cartao-meta">' + plural(x.obras.length, 'poema', 'poemas') + '</span>' +
      (titulos.length ? '<span class="cartao-texto">' + titulos.map((t) => '<em>' + esc(t) + '</em>').join(', ') + '</span>' : '') + '</a>';
  });
  return html;
}
function htmlListaPoemas(obras) {
  const grupos = porColetanea(obras); let html = '';
  grupos.forEach((g) => {
    const titulo = g.titulo || (grupos.length > 1 ? 'Avulsos' : '');
    if (titulo) html += '<p class="secao-titulo">' + (g.titulo ? '<em>' + esc(titulo) + '</em>' : esc(titulo)) + (g.ano ? ' · ' + g.ano : '') + '</p>';
    const comNum = g.obras.some((o) => o.n);
    html += '<ol class="indice poemas' + (comNum ? '' : ' sem-num') + '">';
    g.obras.forEach((o) => {
      const extra = o.traducao ? '<span class="orig-tit" lang="' + esc(o.traducao.codigo || '') + '">' + esc(o.traducao.titulo) + '</span>'
        : o.partes.length > 1 ? '<span class="orig-tit">' + esc(fichaObra(o)) + '</span>' : '';
      html += '<li><a href="' + U.obra(o) + '">' + (comNum ? '<span class="num">' + esc(o.n) + '</span>' : '') +
        '<span class="tit"' + (o.lingua ? ' lang="' + esc(o.lingua) + '"' : '') + '>' + esc(o.titulo) + extra + '</span></a></li>';
    });
    html += '</ol>';
  });
  return html;
}
function trilhaPasta(a, o) {
  const f = acharForma(o.forma || 'outras'), itens = [{ txt: a.nome, href: U.autor(a) }];
  if (!soPoesia(a.id)) itens.push({ txt: 'Poesia', href: U.genero(a, 'Poesia') });
  if (pastasDe(poesiaDe(a.id)).length > 1) itens.push({ txt: f.nome, href: U.pasta(a, f.id) });
  return comArea(a, itens);
}
const trilhaGenero = (a, g) => ({ txt: nomeGenero(g), href: U.genero(a, g) });

function paginaPasta(a, f) {
  const obras = poesiaDe(a.id).filter((o) => (o.forma || 'outras') === f.id);
  const itens = [{ txt: a.nome, href: U.autor(a) }];
  if (!soPoesia(a.id)) itens.push({ txt: 'Poesia', href: U.genero(a, 'Poesia') });
  const html = '<div class="folha"><header class="cabeca"><h1>' + esc(f.nome) + '</h1><p class="meta">' + esc(a.nome) + ' · ' +
    plural(obras.length, 'poema', 'poemas') + '</p></header>' + htmlListaPoemas(obras) + '</div>';
  pagina({ url: U.pasta(a, f.id), titulo: f.nome + ' — ' + a.nome, corpo: html, trilha: comArea(a, itens.concat({ txt: f.nome })),
    descricao: `${f.nome} de ${a.nome}: ${plural(obras.length, 'poema', 'poemas')} na Biblioteca Taioé.` });
}

function paginaAutor(a) {
  const desc = `${a.nome}${a.vida ? ' (' + a.vida + ')' : ''} na Biblioteca Taioé.${a.nota ? ' ' + textoPuro(a.nota) : ''}`;
  if (soPoesia(a.id)) {
    pagina({ url: U.autor(a), titulo: a.nome, corpo: '<div class="folha">' + cabecaAutor(a) + htmlPastas(a, poesiaDe(a.id)) + '</div>',
      trilha: comArea(a, [{ txt: a.nome }]), descricao: descricaoDe(desc) });
    return;
  }
  let html = '<div class="folha">' + cabecaAutor(a) + '<p class="secao-titulo">Gêneros</p>';
  generosDe(a.id).forEach((x) => {
    const grupos = porColetanea(x.obras), titulos = [];
    grupos.forEach((g) => { if (g.titulo) titulos.push(g.titulo); else g.obras.forEach((o) => titulos.push(o.titulo)); });
    let meta = plural(livros(x.obras), 'obra', 'obras');
    if (grupos.some((g) => g.titulo)) {
      const t = TEXTOS[x.genero] || ['texto', 'textos'];
      meta += ' · ' + plural(x.obras.filter((o) => !o.paratexto).length, t[0], t[1]);
    }
    html += '<a class="cartao" href="' + U.genero(a, x.genero) + '"><span class="cartao-titulo">' + esc(nomeGenero(x.genero)) + '</span>' +
      '<span class="cartao-meta">' + meta + '</span><span class="cartao-texto">' + titulos.map((t) => '<em>' + esc(t) + '</em>').join(', ') + '</span></a>';
  });
  html += '</div>';
  pagina({ url: U.autor(a), titulo: a.nome, corpo: html, trilha: comArea(a, [{ txt: a.nome }]), descricao: descricaoDe(desc) });
}

function paginaGenero(a, x) {
  let html = '<div class="folha"><header class="cabeca"><h1>' + esc(nomeGenero(x.genero)) + '</h1><p class="meta">' + esc(a.nome) + '</p></header>';
  const trilha = comArea(a, [{ txt: a.nome, href: U.autor(a) }, { txt: nomeGenero(x.genero) }]);
  if (x.genero === 'Poesia') {
    pagina({ url: U.genero(a, x.genero), titulo: 'Poesia — ' + a.nome, corpo: html + htmlPastas(a, x.obras) + '</div>', trilha,
      descricao: `Poesia de ${a.nome} na Biblioteca Taioé.` });
    return;
  }
  porColetanea(x.obras).forEach((g) => {
    if (g.titulo) html += '<p class="secao-titulo"><em>' + esc(g.titulo) + '</em>' + (g.ano ? ' · ' + g.ano : '') + '</p>';
    g.obras.forEach((o) => {
      const pub = textoPublicacao(o);
      html += '<a class="cartao' + (o.paratexto ? ' paratexto' : '') + '" href="' + U.obra(o) + '">' +
        '<span class="cartao-titulo">' + (o.coletanea ? esc(o.titulo) : '<em>' + esc(o.titulo) + '</em>') + '</span>' +
        '<span class="cartao-meta">' + esc(fichaObra(o)) + '</span>' + (pub ? '<span class="cartao-texto">' + inline(pub) + '</span>' : '') + '</a>';
    });
  });
  html += '</div>';
  pagina({ url: U.genero(a, x.genero), titulo: nomeGenero(x.genero) + ' — ' + a.nome, corpo: html, trilha,
    descricao: descricaoDe(`${nomeGenero(x.genero)} de ${a.nome} na Biblioteca Taioé: ${x.obras.map((o) => o.titulo).join(', ')}.`) });
}

function trilhaObra(a, o) {
  return o.poema ? trilhaPasta(a, o) : comArea(a, [{ txt: a.nome, href: U.autor(a) }, trilhaGenero(a, o.genero || 'Outros')]);
}
function jsonObra(a, o) {
  return { '@context': 'https://schema.org', '@type': o.poema ? 'CreativeWork' : 'Book', name: o.titulo, inLanguage: 'pt-BR',
    author: { '@type': 'Person', name: a.nomeCompleto || a.nome }, url: SITE + U.obra(o),
    ...(o.ano ? { datePublished: String(o.ano) } : {}), isAccessibleForFree: true,
    ...(o.traducao ? { translationOfWork: { '@type': 'CreativeWork', name: o.traducao.titulo || o.titulo, inLanguage: o.traducao.codigo || undefined } } : {}),
    publisher: { '@type': 'Organization', name: 'Taioé', url: SITE + '/' } };
}

function paginaObra(a, o) {
  const d = o.divisao || { singular: 'parte', plural: 'partes' };
  let html = '<div class="folha"><header class="rosto"><p class="rosto-autor">' + esc(a.nome) + '</p><h1>' + esc(o.titulo) + '</h1>' +
    (o.subtitulo ? '<p class="subtitulo-obra">' + inline(o.subtitulo) + '</p>' : '') +
    '<p class="meta">' + (o.coletanea && o.coletanea.titulo !== o.titulo ? '<em>' + esc(o.coletanea.titulo) + '</em>' + (o.coletanea.ano ? ', ' + esc(o.coletanea.ano) : '') + ' · '
      : o.poema && o.ano ? esc(o.ano) + ' · ' : '') + esc(fichaObra(o)) + '</p>' +
    (o.publicacao ? '<p class="publicacao">' + inline(textoPublicacao(o)) + '</p>' : '') +
    (o.traducao && !o.poema ? '<p class="publicacao">Tradução do ' + esc(o.traducao.lingua) +
      (o.traducao.titulo ? ' (<em lang="' + esc(o.traducao.codigo || '') + '">' + esc(o.traducao.titulo) + '</em>)' : '') + '</p>' : '') +
    (o.descricao ? '<p class="descricao">' + inline(o.descricao) + '</p>' : '') +
    '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
    '<p class="acoes"><a class="botao" id="comecar" href="' + U.parte(o, 1) + '">Começar a ler</a>' +
    (o.edicao ? ' <a class="botao secundario" href="' + U.sobre(o) + '">' + esc(tituloSobre(o)) + '</a>' : '') + '</p></header>' +
    '<p class="secao-titulo">' + esc(d.plural.charAt(0).toUpperCase() + d.plural.slice(1)) + '</p><ol class="indice">';
  const agrupa = o.divisao && (o.divisao.rotulo === 'titulo' || o.divisao.agrupar);
  o.partes.forEach((p, i) => {
    const num = agrupa && i && o.partes[i - 1].n === p.n ? '' : p.n;
    html += '<li data-parte="' + p.slug + '"><a href="' + U.parte(o, i + 1) + '"><span class="num">' + esc(num) + '</span>' +
      '<span class="tit">' + (p.titulo ? inline(p.titulo) : '<span class="inc">' + incipit(p.texto, 60) + '</span>') +
      (p.folhas ? '<span class="folhas">' + esc(p.folhas) + '</span>' : '') + '</span></a></li>';
  });
  html += '</ol></div>';
  pagina({ url: U.obra(o), titulo: o.titulo + ' — ' + a.nome, corpo: html, trilha: trilhaObra(a, o).concat({ txt: o.titulo }),
    descricao: descricaoDe(o.descricao || `${o.titulo}, de ${a.nome}${o.ano ? ' (' + (o.datas || o.ano) + ')' : ''}: ${fichaObra(o)}. Leia na Biblioteca Taioé.`),
    dados: { pagina: 'obra', obra: chaveObra(o), 'titulo-obra': o.titulo, total: o.partes.length }, jsonld: jsonObra(a, o) });
}

function paginaParte(a, o, i) {
  const p = o.partes[i - 1], total = o.partes.length, poema = !!o.poema, conto = !!o.coletanea || poema;
  const bilingue = p.original !== undefined && p.original !== null;
  let passos;
  if (poema) {
    passos = trilhaPasta(a, o).concat(total > 1 ? [{ txt: o.titulo, href: U.obra(o) }, { txt: rotuloParte(o, p) }] : [{ txt: o.titulo }]);
  } else {
    passos = [{ txt: a.nome, href: U.autor(a) }, { txt: o.titulo, href: U.obra(o) }, { txt: rotuloParte(o, p) }];
    if (conto) {
      passos.splice(1, 0, trilhaGenero(a, o.genero || 'Outros'));
      if (total === 1) passos = passos.slice(0, 2).concat({ txt: o.titulo });
    }
    passos = comArea(a, passos);
  }
  const passo = (cls, rel, dir, href, alvo) => '<a class="passo ' + cls + '" href="' + href + '" rel="' + rel + '"><span class="dir">' + dir + '</span><span class="alvo">' + alvo + '</span></a>';
  const indice = (href, alvo) => '<a class="passo seg" href="' + href + '"><span class="dir">Índice</span><span class="alvo">' + esc(alvo) + '</span></a>';
  let navAnt = '<span class="passo vazio"></span>', navSeg, prev = null, next = null;
  const irmaos = poema ? vizinhosPoema(o) : conto ? daColetanea(o) : [], k = irmaos.indexOf(o);
  if (i > 1) { prev = U.parte(o, i - 1); navAnt = passo('ant', 'prev', '← Anterior', prev, rotuloPasso(o.partes[i - 2])); }
  else if (k > 0) { const x = irmaos[k - 1]; prev = U.parte(x, x.partes.length); navAnt = passo('ant', 'prev', '← Anterior', prev, esc(x.titulo)); }
  if (i < total) { next = U.parte(o, i + 1); navSeg = passo('seg', 'next', 'Seguinte →', next, rotuloPasso(o.partes[i])); }
  else if (k >= 0 && k < irmaos.length - 1) { const x = irmaos[k + 1]; next = U.parte(x, 1); navSeg = passo('seg', 'next', 'Seguinte →', next, esc(x.titulo)); }
  else if (poema) navSeg = indice(U.indicePoema(a, o), pastasDe(poesiaDe(a.id)).length > 1 ? acharForma(o.forma || 'outras').nome : 'Poesia');
  else if (conto) navSeg = indice(U.genero(a, o.genero), nomeGenero(o.genero));
  else navSeg = indice(U.obra(o), o.titulo);

  function titulo(tag, cls, trad, orig) {
    const h = '<' + tag + (cls ? ' class="' + cls + '"' : '') + '>';
    if (!bilingue || !orig) return h + inline(trad) + '</' + tag + '>';
    const lingua = o.traducao ? o.traducao.codigo || '' : '';
    return '<div class="paralelo titulos"><div class="orig" data-i="t"' + (lingua ? ' lang="' + esc(lingua) + '"' : '') + '>' + h + inline(orig) + '</' + tag + '></div>' +
      '<div class="trad" data-i="t">' + h + inline(trad) + '</' + tag + '></div></div>';
  }
  let cabeca;
  if (conto) {
    const livro = [o.coletanea ? '<em>' + esc(o.coletanea.titulo) + '</em>' : '', o.secao ? esc(o.secao) : ''].filter(Boolean).join(' · ');
    cabeca = (i === 1 ? (livro ? '<p class="coletanea-parte">' + livro + '</p>' : '') +
      (poema && o.n ? '<p class="num-parte">' + esc(o.n) + '</p>' : '') +
      titulo('h1', 'titulo-conto', o.titulo, o.traducao && o.traducao.titulo) +
      (o.subtitulo ? '<p class="subtitulo-obra">' + inline(o.subtitulo) + '</p>' : '') +
      (o.traducao ? '<p class="publicacao">Tradução do ' + esc(o.traducao.lingua) + '</p>' : '') +
      (o.publicacao ? '<p class="publicacao">' + inline(textoPublicacao(o)) + '</p>' : '') : '') +
      (total > 1 ? (p.n ? '<p class="num-parte">' + esc(p.n) + '</p>' : '') + (p.titulo ? titulo('h2', '', p.titulo, p.tituloOriginal) : '') : '');
  } else {
    cabeca = (p.n ? '<p class="num-parte">' + esc(p.n) + '</p>' : '') + (p.titulo ? titulo('h1', '', p.titulo, p.tituloOriginal) : '');
  }
  if (!/<h1/.test(cabeca)) cabeca = '<h1 class="visualmente-oculto">' + esc(rotuloParte(o, p) === o.titulo ? o.titulo : o.titulo + ' — ' + rotuloParte(o, p)) + '</h1>' + cabeca;
  const lingua = bilingue && o.traducao ? o.traducao.codigo || '' : '';
  const html = '<p class="aviso-outro" id="aviso-outro" hidden></p>' +
    '<article class="folha leitura' + (poema ? ' de-poema' : '') + (bilingue ? ' bilingue ver-trad' : '') + '"' + (lingua ? ' data-lingua="' + esc(lingua) + '"' : '') + '>' +
    '<header class="cabeca-parte' + (conto && i === 1 ? ' conto' : '') + '">' + cabeca + '</header>' + textoParte(o, p) +
    (i < total || poema ? '' : '<p class="fim">Fim</p>') +
    '<nav class="passos" aria-label="Navegação entre ' + esc(poema && total === 1 ? 'poemas' : o.divisao ? o.divisao.plural : 'partes') + '">' + navAnt + navSeg + '</nav>' +
    (total > 1 ? '<p class="posicao">' + i + ' de ' + total + ' · <a href="' + U.obra(o) + '">índice</a></p>' : '') +
    (conto && o.edicao && i === total ? '<p class="posicao"><a href="' + U.sobre(o) + '">' + esc(tituloSobre(o)) + '</a></p>' : '') + '</article>';
  const rot = rotuloParte(o, p);
  const tituloPagina = (rot && rot !== o.titulo ? rot + (p.titulo && rot.indexOf(textoPuro(p.titulo)) < 0 ? ': ' + textoPuro(p.titulo) : '') + ' — ' : '') + o.titulo + ' — ' + a.nome;
  pagina({ url: U.parte(o, i), titulo: tituloPagina, corpo: html, trilha: passos, prev, next,
    bilingue: bilingue ? (o.traducao && o.traducao.lingua ? o.traducao.lingua.charAt(0).toUpperCase() + o.traducao.lingua.slice(1) : 'Original') : null,
    progresso: total > 1 ? i / total : undefined,
    descricao: descricaoDe(p.texto),
    dados: { pagina: 'parte', obra: chaveObra(o), parte: umaParte(o) ? 'texto' : p.slug, indice: i, total,
      rotulo: rot === o.titulo ? '' : rot, 'titulo-obra': o.titulo, 'url-obra': U.obra(o) },
    jsonld: umaParte(o) ? jsonObra(a, o) : { '@context': 'https://schema.org', '@type': 'Chapter', name: tituloPagina.replace(/ — [^—]+$/, ''),
      position: i, isPartOf: { '@type': 'Book', name: o.titulo, url: SITE + U.obra(o) }, author: { '@type': 'Person', name: a.nomeCompleto || a.nome }, inLanguage: 'pt-BR' } });
}

function colunaLugar(itens, rotParte) {
  const tem = itens.some((v) => v.cap);
  return { th: tem ? '<th>' + esc(rotParte) + '</th>' : '', td: (v) => (tem ? '<td class="cap">' + esc(v.cap || 'Texto') + '</td>' : '') };
}
function listaVariantes(itens, rotDe, rotPara, rotParte) {
  const c = colunaLugar(itens, rotParte);
  return '<table class="variantes"><thead><tr>' + c.th + '<th>' + esc(rotDe) + '</th><th>' + esc(rotPara) + '</th></tr></thead><tbody>' +
    itens.map((v) => '<tr>' + c.td(v) + '<td>' + esc(v.de) + '</td><td>' + esc(v.para) + '</td></tr>').join('') + '</tbody></table>';
}
function paginaSobre(a, o) {
  const e = o.edicao, d = o.divisao || { singular: 'parte' };
  const rotParte = o.coletanea && o.partes.length === 1 ? 'Onde' : d.singular.charAt(0).toUpperCase() + d.singular.slice(1);
  const rotBase = e.base || '1ª edição', tit = tituloSobre(o);
  let html = '<article class="folha sobre"><header class="cabeca"><h1>' + esc(tit) + '</h1><p class="meta">' +
    (o.coletanea ? esc(o.titulo) + ' · <em>' + esc(o.coletanea.titulo) + '</em>' : '<em>' + esc(o.titulo) + '</em>') + ' · ' + esc(a.nome) + '</p></header>' +
    '<div class="texto">' + blocos(e.apresentacao || '') + '</div>';
  const S = e.secoes || {};
  const secao = (nome, padrao) => { const s = S[nome] || {}; return { titulo: s.titulo || padrao.titulo, explica: s.explica || padrao.explica, de: s.de || padrao.de || rotBase, para: s.para || padrao.para }; };
  let s;
  if (e.erros && e.erros.length) {
    s = secao('erros', { titulo: 'Erros tipográficos da 1ª edição corrigidos', explica: 'Grafia da 1ª edição nas duas colunas.', para: 'Corrigido' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + ' ' + e.erros.length + ' correções.</p>' + listaVariantes(e.erros, s.de, s.para, rotParte);
  }
  if (e.tradicao && e.tradicao.length) {
    s = secao('tradicao', { titulo: 'Lições da 2ª edição adotadas', explica: 'Leituras em que todas as edições posteriores concordam contra a 1ª. Grafia da 1ª edição.', para: 'Adotado' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p>' + listaVariantes(e.tradicao, s.de, s.para, rotParte);
  }
  if (e.pontuacao && e.pontuacao.length) {
    s = secao('pontuacao', { titulo: 'Pontuação da 2ª edição adotada', explica: 'Mesmo critério: só onde toda a tradição posterior concorda. Grafia atualizada.', para: 'Adotado' });
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p>' + listaVariantes(e.pontuacao, s.de, s.para, rotParte);
  }
  if (e.mantidas && e.mantidas.length) {
    s = secao('mantidas', { titulo: 'Leituras da 1ª edição mantidas', explica: 'Pontos em que parte das edições modernas lê diferente.' });
    const cm = colunaLugar(e.mantidas, rotParte);
    html += '<h2>' + esc(s.titulo) + '</h2><p class="explica">' + esc(s.explica) + '</p><table class="variantes"><thead><tr>' + cm.th +
      '<th>Este texto</th><th>Outras edições</th></tr></thead><tbody>' +
      e.mantidas.map((v) => '<tr>' + cm.td(v) + '<td>' + esc(v.texto) + '</td><td>' + esc(v.variante) + (v.obs ? '<span class="obs">' + esc(v.obs) + '</span>' : '') + '</td></tr>').join('') + '</tbody></table>';
  }
  if (e.fontes && e.fontes.length) {
    html += '<h2>Fontes consultadas</h2><ul class="fontes">' + e.fontes.map((f) => {
      const nome = f.url ? '<a href="' + esc(f.url) + '" target="_blank" rel="noopener">' + esc(f.nome) + '</a>' : esc(f.nome);
      return '<li>' + nome + (f.nota ? ' — <span class="obs-inline">' + esc(f.nota) + '</span>' : '') + '</li>';
    }).join('') + '</ul>';
  }
  html += '<p class="posicao"><a href="' + U.obra(o) + '">' + (umaParte(o) ? 'Voltar ao texto' : 'Voltar ao índice') + '</a></p></article>';
  pagina({ url: U.sobre(o), titulo: tit + ' — ' + o.titulo, corpo: html, trilha: trilhaObra(a, o).concat({ txt: o.titulo, href: U.obra(o) }, { txt: tit }),
    descricao: descricaoDe(`${tit}: ${o.titulo}, de ${a.nome}. ${e.apresentacao || ''}`) });
}

// ------------------------------------------------------------------ gerar
fs.rmSync(SAIDA, { recursive: true, force: true });
fs.mkdirSync(SAIDA, { recursive: true });

paginaCapa();
AREAS.forEach(paginaArea);
dados.autores.forEach((a) => {
  if (!obrasDe(a.id).length) return;
  paginaAutor(a);
  generosDe(a.id).forEach((x) => { if (!(x.genero === 'Poesia' && soPoesia(a.id))) paginaGenero(a, x); });
  pastasDe(poesiaDe(a.id)).forEach((x) => { if (pastasDe(poesiaDe(a.id)).length > 1) paginaPasta(a, x.forma); });
});
dados.obras.forEach((o) => {
  const a = acharAutor(o.autor) || { nome: o.autor, id: o.autor };
  if (!umaParte(o)) paginaObra(a, o);
  o.partes.forEach((p, i) => paginaParte(a, o, i + 1));
  if (o.edicao) paginaSobre(a, o);
});

// 404, estilo, leitor, ícone, cópias do login
const html404 = `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Página não encontrada · Biblioteca Taioé</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="${BASE}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="${BASE}css/estilo.css?v=${V_CSS}">
<script defer src="${BASE}js/leitor.js?v=${V_JS}"></script>
</head>
<body data-pagina="404">
<header class="topo"><div class="topo-int"><a class="marca" href="${BASE}">Biblioteca</a><nav class="topo-nav" id="trilha"></nav></div></header>
<main id="app" tabindex="-1"><div class="folha cabeca"><h1>Página não encontrada</h1><p><a href="${BASE}">Voltar à capa da Biblioteca</a></p></div></main>
<footer class="rodape"><p>Textos em domínio público. <a href="/">Taioé</a></p></footer>
</body>
</html>
`;
fs.writeFileSync(path.join(SAIDA, '404.html'), html404);
fs.mkdirSync(path.join(SAIDA, 'css'), { recursive: true });
fs.mkdirSync(path.join(SAIDA, 'js'), { recursive: true });
fs.writeFileSync(path.join(SAIDA, 'css', 'estilo.css'), CSS);
fs.writeFileSync(path.join(SAIDA, 'js', 'leitor.js'), LEITOR);
fs.copyFileSync(path.join(RAIZ, 'favicon.svg'), path.join(SAIDA, 'favicon.svg'));
// cópias idênticas do taioe-hub (o workflow Cópias confere o sha256)
fs.mkdirSync(path.join(SAIDA, 'vendor'), { recursive: true });
fs.writeFileSync(path.join(SAIDA, 'vendor', 'supabase-js-2.117.2.js'), lerLf(path.join(RAIZ, 'ferramentas', 'site', 'comum', 'supabase-js-2.117.2.js')));
fs.writeFileSync(path.join(SAIDA, 'js', 'taioe-sessao.js'), lerLf(path.join(RAIZ, 'ferramentas', 'site', 'comum', 'taioe-sessao.js')));

// índice compacto das obras: títulos e partes, para «Continuar a leitura» de outro aparelho
// e para converter os endereços antigos (#/o/<id>/<n>)
const indiceObras = {};
dados.obras.forEach((o) => {
  indiceObras[chaveObra(o)] = { i: o.id, t: o.titulo, u: U.obra(o), p: umaParte(o) ? [['texto', '']] : o.partes.map((p) => [p.slug, rotuloParte(o, p)]) };
});
fs.writeFileSync(path.join(SAIDA, 'obras.json'), JSON.stringify(indiceObras));

fs.writeFileSync(path.join(SAIDA, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  sitemap.map((u) => `<url><loc>${SITE}${u}</loc></url>`).join('\n') + '\n</urlset>\n');  // sem data: gerar de novo dá o mesmo arquivo

// endereços congelados (só acrescenta; nunca muda um que já existe)
const juntos = { ...congelados };
Object.entries(enderecos).forEach(([id, mapa]) => { juntos[id] = { ...(congelados[id] || {}), ...mapa }; });
fs.writeFileSync(ARQ_ENDERECOS, '{\n' + Object.keys(juntos).sort().map((k) => JSON.stringify(k) + ': ' + JSON.stringify(juntos[k])).join(',\n') + '\n}\n');

// catálogo para o banco (biblioteca.obras), idempotente
const linhas = dados.obras.slice().sort((a, b) => chaveObra(a).localeCompare(chaveObra(b)))
  .map((o) => `  (${sql(chaveObra(o))}, ${sql(o.titulo.length > 200 ? o.titulo.slice(0, 199).replace(/\s+\S*$/, '') + '…' : o.titulo)})`);  // o banco aceita até 200
function sql(s) { return "'" + String(s).replace(/'/g, "''") + "'"; }
fs.mkdirSync(path.dirname(ARQ_SQL), { recursive: true });
fs.writeFileSync(ARQ_SQL, `-- Catálogo da Biblioteca Taioé (biblioteca.obras). Gerado por ferramentas/site/gerar.mjs; não edite à mão.
-- Aplicado pelo workflow Catálogo do taioe-infra, primeiro no teste e depois na produção.
-- Obra que sai do site continua no catálogo: as posições de leitura guardadas dependem dela.
insert into biblioteca.obras (obra, titulo) values
${linhas.join(',\n')}
on conflict (obra) do update set titulo = excluded.titulo, atualizado_em = now()
  where biblioteca.obras.titulo is distinct from excluded.titulo;
`);

console.log(`${paginas} páginas, ${sitemap.length} no sitemap, ${dados.obras.length} obras, ${dados.autores.length} autores.`);
