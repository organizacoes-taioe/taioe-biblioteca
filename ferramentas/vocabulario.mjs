// O vocabulário da Biblioteca Taioé (palavras raras em português com nota; edicoes/vocabulario/LEIA.md).
// Rodar na raiz do repositório (lê conteudo/ como o gerar.mjs):
//   node ferramentas/vocabulario.mjs texto <id…>            grava ~/.cache/taioe-raras/textos/<id>.txt
//   node ferramentas/vocabulario.mjs candidatos <id…>       palavras fora do português de hoje, com a contagem
//   node ferramentas/vocabulario.mjs conferir <vocab.json>  confere o arquivo (formas no texto, repetidas…)
//   node ferramentas/vocabulario.mjs ocorrencias <vocab.json> <lema…>   cada ocorrência que será marcada
// Só o lado em português conta: nas obras bilíngues, o campo «original» fica de fora.
import fs from 'node:fs'; import path from 'node:path'; import os from 'node:os';
const CASA = path.join(os.homedir(), '.cache', 'taioe-raras');
const porId = {}, ordem = [];
const reg = (o) => { if (porId[o.id]) return; porId[o.id] = o; ordem.push(o); };
const B = new Proxy({}, { get: (t, k) => ({
  obra: reg,
  poemas: (pac) => pac.poemas.forEach((p) => reg({ ...p, autor: pac.autor, poema: true, partes: (p.partes || [{}]).map((x) => ({ titulo: x.titulo || '' })) })),
  textos: (mapa) => Object.keys(mapa).forEach((id) => { const o = porId[id]; if (!o) return; mapa[id].t.forEach((t, i) => { o.partes[i] = o.partes[i] || {}; o.partes[i].texto = t; }); }),
}[k] || (() => {})) });
const andar = (d) => fs.readdirSync(d).sort().flatMap((f) => { const p = path.join(d, f); return fs.statSync(p).isDirectory() ? andar(p) : p.endsWith('.js') ? [p] : []; });
const todos = andar('conteudo'), raiz = todos.filter((f) => path.dirname(f) === 'conteudo');
const rodar = (f) => { try { new Function('BIBLIOTECA', 'window', fs.readFileSync(f, 'utf8'))(B, {}); } catch (e) { /* arquivo que não é de obra */ } };
const lista = raiz.concat(todos.filter((f) => !raiz.includes(f)));
lista.forEach(rodar);
// de novo os textos: alguns arquivos vêm antes do índice que registra a obra
lista.filter((f) => fs.readFileSync(f, 'utf8').includes('BIBLIOTECA.textos(')).forEach(rodar);
const limpo = (t) => String(t || '').replace(/::\S+/g, ' ').replace(/\{[^}]*\}/g, ' ').replace(/[_*|¤@#]/g, ' ');
const PAL = /\p{L}+(?:-\p{L}+)*/gu;
const MESOCLISE = /[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)([^A-Za-zÀ-ÿ]|$)/;
const [, , cmd, ...args] = process.argv;

if (cmd === 'texto') {
  fs.mkdirSync(path.join(CASA, 'textos'), { recursive: true });
  for (const id of args) {
    const o = porId[id]; if (!o) { console.error('obra que não existe:', id); continue; }
    const f = path.join(CASA, 'textos', id + '.txt');
    fs.writeFileSync(f, o.partes.map((p, i) => '=== ' + (i + 1) + '. ' + (p.titulo || '') + '\n\n' + limpo(p.texto)).join('\n\n'));
    console.log(f);
  }
} else if (cmd === 'candidatos') {
  // o português de hoje: as nossas traduções (escritas agora) e a lista de frequência dos Cards
  const hoje = new Set();
  for (const o of ordem) if (o.traducao) for (const p of o.partes) for (const w of limpo(p.texto).toLowerCase().match(PAL) || []) hoje.add(w);
  const freq = path.resolve('..', 'cards', 'fonte', 'frequencia', 'pt.tsv');
  if (fs.existsSync(freq)) for (const l of fs.readFileSync(freq, 'utf8').split('\n')) for (const w of l.toLowerCase().match(PAL) || []) hoje.add(w);
  const conta = new Map();
  for (const id of args) { const o = porId[id]; if (!o) { console.error('obra que não existe:', id); continue; }
    o.partes.forEach((p, i) => { for (const w of limpo(p.texto).match(PAL) || []) { const k = w.toLowerCase(); if (hoje.has(k) || /^\p{Lu}/u.test(w)) continue; const c = conta.get(k) || { n: 0, onde: id + ':' + (i + 1) }; c.n++; conta.set(k, c); } }); }
  for (const [w, c] of [...conta].sort((a, b) => b[1].n - a[1].n)) console.log(c.n + '\t' + w + '\t' + c.onde);
} else if (cmd === 'conferir' || cmd === 'ocorrencias') {
  const v = JSON.parse(fs.readFileSync(args[0], 'utf8'));
  const obras = v.obras || [v.obra];
  const erros = [], vistas = new Map();
  for (const id of obras) if (!porId[id]) erros.push('obra que não existe: ' + id);
  const achar = (w, f, cada) => {
    const re = new RegExp('(?<![\\p{L}])' + f.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![\\p{L}])', 'giu');
    let n = 0;
    for (const id of obras) { if (w.so_obras && !w.so_obras.includes(id)) continue; const o = porId[id]; if (!o) continue;
      o.partes.forEach((p, i) => { if (w.so_capitulos && !w.so_capitulos.includes(i + 1)) return; const t = limpo(p.texto);
        for (const m of t.matchAll(re)) { n++; if (cada) cada(id, i + 1, t.slice(Math.max(0, m.index - 50), m.index + f.length + 30).replace(/\s+/g, ' ')); } }); }
    return n;
  };
  if (cmd === 'ocorrencias') {
    for (const w of v.palavras.filter((x) => args.slice(1).includes(x.lema))) {
      console.log('##', w.lema, '→', w.def);
      for (const f of w.formas) achar(w, f, (id, c, t) => console.log('  ', id, c, '…' + t));
    }
  } else {
    for (const w of v.palavras) {
      if (!w.lema || !w.def || !Array.isArray(w.formas) || !w.formas.length) { erros.push('sem lema, def ou formas: ' + JSON.stringify(w).slice(0, 80)); continue; }
      if (w.def.split(/\s+/).length > 22) erros.push('definição longa: ' + w.lema);
      if (MESOCLISE.test(w.def)) erros.push('mesóclise na definição: ' + w.lema);
      for (const f of w.formas) {
        const k = f.toLowerCase();
        if (vistas.has(k)) erros.push('forma em duas palavras: ' + f + ' (' + vistas.get(k) + ', ' + w.lema + ')');
        vistas.set(k, w.lema);
        if (!achar(w, f)) erros.push('forma que não está no texto: ' + f + ' (' + w.lema + ')');
      }
    }
    console.log(erros.length ? erros.join('\n') : 'ok: ' + v.palavras.length + ' palavras em ' + obras.length + ' obra(s)');
    process.exitCode = erros.length ? 1 : 0;
  }
} else {
  console.log('uso: texto | candidatos | conferir | ocorrencias (ver o topo do arquivo)');
}
