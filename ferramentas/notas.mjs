// As notas gerais da Biblioteca Taioé (notas de contexto nos livros em português; edicoes/notas/LEIA.md).
// Rodar na raiz do repositório (lê conteudo/ como o gerar.mjs):
//   node ferramentas/notas.mjs texto <id…>              grava ~/.cache/taioe-notas/textos/<id>.txt (o texto cru de cada parte)
//   node ferramentas/notas.mjs conferir [arquivo…]      confere os arquivos (sem nome, todos os de edicoes/notas/)
//   node ferramentas/notas.mjs revisao <pasta>          grava <pasta>/notas.json, a página de revisão (só as notas sem «revista»)
//   node ferramentas/notas.mjs aplicar <respostas.json> aplica as respostas do Gere (aprovar, alterar, excluir) e
//                                                       grava ao lado <respostas>.aplicadas.json, para o «marcar»
// Só o lado em português conta: nas obras bilíngues, o campo «original» fica de fora.
import fs from 'node:fs'; import path from 'node:path'; import os from 'node:os';
const CASA = path.join(os.homedir(), '.cache', 'taioe-notas');
const DIR = path.join('edicoes', 'notas');
const porId = {}, ordem = [], autores = {};
const reg = (o) => { if (porId[o.id]) return; porId[o.id] = o; ordem.push(o); };
const B = new Proxy({}, { get: (t, k) => ({
  obra: reg,
  autor: (a) => { autores[a.id] = a; },
  poemas: (pac) => pac.poemas.forEach((p) => reg({ ...p, autor: pac.autor, poema: true, partes: (p.partes || [{}]).map((x) => ({ titulo: x.titulo || '' })) })),
  textos: (mapa) => Object.keys(mapa).forEach((id) => { const o = porId[id]; if (!o) return; mapa[id].t.forEach((t, i) => { o.partes[i] = o.partes[i] || {}; o.partes[i].texto = t; }); }),
}[k] || (() => {})) });
const andar = (d) => fs.readdirSync(d).sort().flatMap((f) => { const p = path.join(d, f); return fs.statSync(p).isDirectory() ? andar(p) : p.endsWith('.js') ? [p] : []; });
const todos = andar('conteudo'), raiz = todos.filter((f) => path.dirname(f) === 'conteudo');
const rodar = (f) => { try { new Function('BIBLIOTECA', 'window', fs.readFileSync(f, 'utf8'))(B, {}); } catch (e) { /* arquivo que não é de obra */ } };
const lista = raiz.concat(todos.filter((f) => !raiz.includes(f)));
lista.forEach(rodar);
lista.filter((f) => fs.readFileSync(f, 'utf8').includes('BIBLIOTECA.textos(')).forEach(rodar);
const MESOCLISE = /[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)/;
const [, , cmd, ...args] = process.argv;

const arquivos = () => (fs.existsSync(DIR) ? fs.readdirSync(DIR).filter((x) => x.endsWith('.json')).sort().map((x) => path.join(DIR, x)) : []);
const ler = (f) => JSON.parse(fs.readFileSync(f, 'utf8'));
const gravar = (f, d) => fs.writeFileSync(f, JSON.stringify(d, null, 1) + '\n');
const obraDe = (arq, n) => n.obra || arq.obra;

/* posição da nota no texto cru da parte: logo depois do «apos», na ocorrência pedida (-1 se não achou) */
function posicao(texto, n) {
  let k = -1;
  for (let v = 0; v < (n.ocorrencia || 1); v++) { k = texto.indexOf(n.apos, k + 1); if (k < 0) return -1; }
  return k + n.apos.length;
}
/* a frase (ou o verso) em volta da nota, para a página de revisão, sem as marcas do texto */
function trecho(texto, pos) {
  const limpa = (s) => s.replace(/\{[^}]*\}/g, '').replace(/^[|@#¤]\s?/gm, '').replace(/[_*]/g, '').replace(/\s+/g, ' ').trim();
  let ini = Math.max(texto.lastIndexOf('\n', pos - 1), 0), fim = texto.indexOf('\n', pos);
  if (fim < 0) fim = texto.length;
  let s = texto.slice(ini, fim);
  const rel = pos - ini;
  if (s.length > 420) {   // parágrafo longo: só a frase
    const antes = s.slice(0, rel), depois = s.slice(rel);
    const a = Math.max(antes.search(/[.!?;][^.!?;]*$/) + 1, 0), d = depois.search(/[.!?;]/);
    s = antes.slice(a) + (d < 0 ? depois : depois.slice(0, d + 1));
  }
  return limpa(s);
}

function conferir(fs_) {
  const erros = [], ids = new Set();
  let total = 0;
  for (const f of fs_) {
    const arq = ler(f);
    if (!arq.obra && !arq.obras) erros.push(f + ': falta «obra» ou «obras»');
    for (const n of arq.notas || []) {
      total++;
      const id = obraDe(arq, n), o = porId[id], onde = f + ', ' + (n.id || '?');
      if (!n.id || !/^[a-z0-9-]+$/.test(n.id)) erros.push(onde + ': id vazio ou com caractere fora de a-z, 0-9 e -');
      if (ids.has(id + ':' + n.id)) erros.push(onde + ': id repetido');
      ids.add(id + ':' + n.id);
      if (!o) { erros.push(onde + ': obra que não existe: ' + id); continue; }
      if (arq.obras && !arq.obras.includes(id)) erros.push(onde + ': obra fora da lista «obras»');
      const p = o.partes[(n.parte || 0) - 1];
      if (!p) { erros.push(onde + ': parte que não existe: ' + n.parte); continue; }
      if (!n.apos || /[{}]/.test(n.apos)) { erros.push(onde + ': «apos» vazio ou com chaves'); continue; }
      const pos = posicao(String(p.texto), n);
      if (pos < 0) erros.push(onde + ': «' + n.apos + '» não está na parte ' + n.parte + (n.ocorrencia ? ' (ocorrência ' + n.ocorrencia + ')' : ''));
      else if (!n.ocorrencia && String(p.texto).indexOf(n.apos, pos) >= 0) erros.push(onde + ': «' + n.apos + '» aparece mais de uma vez na parte: pôr «ocorrencia» ou alongar o trecho');
      else if (/\p{L}/u.test(String(p.texto)[pos] || '')) erros.push(onde + ': «apos» termina no meio de uma palavra');
      const t = String(n.texto || '');
      if (!t.trim()) erros.push(onde + ': nota sem texto');
      if (t.length > 600) erros.push(onde + ': nota longa demais (' + t.length + ' caracteres; até ~3 frases curtas)');
      if (MESOCLISE.test(t)) erros.push(onde + ': mesóclise na nota');
      if (/[“”"]/.test(t)) erros.push(onde + ': aspas: usar « »');
    }
  }
  return { erros, total };
}

if (cmd === 'texto') {
  fs.mkdirSync(path.join(CASA, 'textos'), { recursive: true });
  for (const id of args) {
    const o = porId[id]; if (!o) { console.error('obra que não existe:', id); continue; }
    const f = path.join(CASA, 'textos', id + '.txt');
    fs.writeFileSync(f, o.partes.map((p, i) => '=== parte ' + (i + 1) + (p.titulo ? ': ' + p.titulo : '') + '\n\n' + String(p.texto || '')).join('\n\n'));
    console.log(f, o.partes.length + ' partes');
  }
} else if (cmd === 'conferir') {
  const { erros, total } = conferir(args.length ? args : arquivos());
  erros.forEach((e) => console.log(e));
  console.log(erros.length ? erros.length + ' erro(s) em ' + total + ' notas' : 'ok, ' + total + ' notas');
  process.exit(erros.length ? 1 : 0);
} else if (cmd === 'revisao') {
  const { erros } = conferir(arquivos());
  if (erros.length) { erros.forEach((e) => console.log(e)); process.exit(1); }
  /* um «capítulo» da página por obra; dentro, uma seção por parte; só as notas sem «revista» */
  const caps = [];
  for (const f of arquivos()) {
    const arq = ler(f), porObra = new Map();
    for (const n of arq.notas || []) {
      if (n.revista) continue;
      const id = obraDe(arq, n);
      if (!porObra.has(id)) porObra.set(id, []);
      porObra.get(id).push(n);
    }
    for (const [id, notas] of porObra) {
      const o = porId[id], autor = o.autor;
      const secoes = new Map();
      notas.map((n) => ({ n, pos: posicao(String(o.partes[n.parte - 1].texto), n) }))
        .sort((a, b) => a.n.parte - b.n.parte || a.pos - b.pos)
        .forEach(({ n, pos }) => {
          const p = o.partes[n.parte - 1];
          if (!secoes.has(n.parte)) secoes.set(n.parte, { id: 'parte-' + n.parte,
            titulo: o.partes.length > 1 ? (p.titulo ? String(p.titulo).replace(/[_*]/g, '') : 'Parte ' + n.parte) : 'Notas', itens: [] });
          secoes.get(n.parte).itens.push({ id: id + ':nota:' + n.id, tipo: 'nota',
            ref: (o.partes.length > 1 ? 'Parte ' + n.parte + ' · ' : '') + 'depois de «' + n.apos + '»',
            versiculo: trecho(String(p.texto), pos), texto: n.texto });
        });
      const pasta = path.join('public', 'biblioteca', autor, id);
      caps.push({ id, rotulo: o.titulo + ', ' + (autores[autor] ? autores[autor].nome : autor),
        estado: 'lote ' + Math.max(...notas.map((n) => n.lote || 0)),
        url: fs.existsSync(pasta) ? '/biblioteca/' + autor + '/' + id + '/' : '/biblioteca/', rotuloUrl: 'Abrir a obra', secoes: [...secoes.values()],
        lote: Math.max(...notas.map((n) => n.lote || 0)) });
    }
  }
  caps.sort((a, b) => a.lote - b.lote);
  caps.forEach((c) => { delete c.lote; });
  const saida = path.join(args[0] || '.', 'notas.json');
  gravar(saida, { slug: 'notas', titulo: 'Biblioteca: notas', capitulos: caps });
  console.log(saida, caps.reduce((s, c) => s + c.secoes.reduce((t, x) => t + x.itens.length, 0), 0) + ' notas em ' + caps.length + ' obras');
} else if (cmd === 'aplicar') {
  /* respostas: [{item: '<obra>:nota:<id>', decisao: 'aprovar'|'alterar'|'excluir', texto?, explicacao?}] (ou {respostas: [...]}) */
  const r = ler(args[0]), resp = Array.isArray(r) ? r : r.respostas || Object.values(r);
  const porItem = new Map(resp.filter((x) => x && x.item && x.lida !== true).map((x) => [x.item, x]));
  const aplicadas = [];
  for (const f of arquivos()) {
    const arq = ler(f);
    let mudou = false;
    arq.notas = (arq.notas || []).filter((n) => {
      const x = porItem.get(obraDe(arq, n) + ':nota:' + n.id);
      if (!x) return true;
      mudou = true; aplicadas.push({ item: x.item, atualizado_em: x.atualizado_em });
      if (x.decisao === 'excluir') return false;
      if (x.decisao === 'alterar' && x.texto) n.texto = x.texto.trim();
      if (x.decisao === 'aprovar' || x.decisao === 'alterar') n.revista = true;
      if (x.explicacao) n.explicacao_gere = x.explicacao;
      return true;
    });
    if (mudou) gravar(f, arq);
  }
  gravar(args[0].replace(/\.json$/, '') + '.aplicadas.json', { lidas: aplicadas });   // o formato do «respostas.sh notas marcar»
  console.log(aplicadas.length + ' respostas aplicadas de ' + porItem.size);
} else {
  console.log('uso: node ferramentas/notas.mjs texto|conferir|revisao|aplicar …');
  process.exit(1);
}
