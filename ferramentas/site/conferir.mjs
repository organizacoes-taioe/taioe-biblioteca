// Confere o site gerado em public/biblioteca/: todo link interno leva a uma página que existe,
// toda página tem título, descrição, canonical e um <h1>, nenhuma tem script ou estilo inline
// (a CSP bloquearia), e os endereços das partes valem no banco.
//
//   node ferramentas/site/conferir.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const PUB = path.join(RAIZ, 'public');
const problemas = [];
let paginas = 0, links = 0, bytes = 0;

function andar(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) andar(p);
    else if (e.name.endsWith('.html')) conferir(p);
  }
}
function existe(url) {
  const limpo = url.split('#')[0].split('?')[0];
  if (!limpo.startsWith('/biblioteca/')) return true;           // fora da Biblioteca: outro Worker
  const alvo = path.join(PUB, decodeURIComponent(limpo));
  return limpo.endsWith('/') ? fs.existsSync(path.join(alvo, 'index.html')) : fs.existsSync(alvo);
}
function conferir(arq) {
  const html = fs.readFileSync(arq, 'utf8'), rel = path.relative(PUB, arq);
  paginas++; bytes += html.length;
  if (!/<title>[^<]+<\/title>/.test(html)) problemas.push(rel + ': sem título');
  if (!rel.endsWith('404.html')) {
    if (!/<meta name="description" content="[^"]+">/.test(html)) problemas.push(rel + ': sem descrição');
    if (!/<link rel="canonical" href="https:\/\/taioe\.com\.br\/biblioteca\//.test(html)) problemas.push(rel + ': sem canonical');
  }
  if (!/<h1[\s>]/.test(html)) problemas.push(rel + ': sem h1');
  if (/\sstyle="/.test(html)) problemas.push(rel + ': estilo inline');
  if (/<script(?![^>]*\ssrc=)(?![^>]*type="application\/ld\+json")[^>]*>/.test(html)) problemas.push(rel + ': script inline');
  if (/\son[a-z]+="/.test(html)) problemas.push(rel + ': handler inline');
  for (const m of html.matchAll(/\shref="([^"]+)"/g)) {
    const u = m[1];
    if (u.startsWith('http') || u.startsWith('mailto:') || u.startsWith('#')) continue;
    links++;
    if (!existe(u)) problemas.push(rel + ': link quebrado ' + u);
  }
  for (const m of html.matchAll(/\ssrc="([^"]+)"/g)) if (!existe(m[1])) problemas.push(rel + ': arquivo ausente ' + m[1]);
}
andar(path.join(PUB, 'biblioteca'));

const enderecos = JSON.parse(fs.readFileSync(path.join(RAIZ, 'ferramentas', 'site', 'enderecos.json'), 'utf8'));
for (const [obra, mapa] of Object.entries(enderecos)) {
  for (const s of Object.values(mapa)) {
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(s) || s.length > 60) problemas.push(`endereço inválido para o banco: ${obra}/${s}`);
  }
}
const sql = fs.readFileSync(path.join(RAIZ, 'ferramentas', 'sql', 'obras.sql'), 'utf8');
for (const m of sql.matchAll(/^\s+\('([^']+)'/gm)) {
  if (!/^[a-z0-9]+(-[a-z0-9]+)*\/[a-z0-9]+(-[a-z0-9]+)*$/.test(m[1]) || m[1].length > 120) problemas.push('obra inválida para o banco: ' + m[1]);
}

console.log(`${paginas} páginas, ${links} links internos, ${(bytes / 1048576).toFixed(1)} MB de HTML`);
if (problemas.length) {
  console.log(`${problemas.length} problema(s):`);
  problemas.slice(0, 40).forEach((p) => console.log('  ' + p));
  process.exit(1);
}
console.log('tudo certo');
