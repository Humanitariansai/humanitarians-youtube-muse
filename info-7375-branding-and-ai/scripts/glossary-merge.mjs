#!/usr/bin/env node
// glossary-merge.mjs — merge _parts/*.md entries into key-terms/Glossary.md.
// Deterministic: dedupe by normalized term, union chapter tags, keep a citation
// if any part had one, sort A–Z, append a "foundational concepts not yet named"
// section computed from facts/<topic>/graph.json. NO AI / no network.
//   node SCRIPTS/glossary-merge.mjs --topic branding

import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : d; };
const TOPIC = arg('--topic', 'branding');
const BOOK = process.cwd();
const PARTS = join(BOOK, 'key-terms', '_parts');
const FACTS_DIR = join(BOOK, '..', '..', 'facts', TOPIC);

const norm = (s) => s.toLowerCase().replace(/\([^)]*\)/g, ' ').replace(/[‘’']/g, '')
  .replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim().replace(/s$/, '');

// --- parse all batch parts ---
const HEADER = /^-\s+\*\*(.+?)\*\*\s*::\s*ch\s*(.+?)\s*::\s*src\s*(.+?)\s*$/;
const entries = new Map(); // key -> {display, chapters:Set, src, def}
for (const f of readdirSync(PARTS).filter(f => f.endsWith('.md')).sort()) {
  const lines = readFileSync(join(PARTS, f), 'utf8').split('\n');
  let cur = null;
  const flush = () => { if (cur) addEntry(cur); cur = null; };
  for (const ln of lines) {
    const m = ln.match(HEADER);
    if (m) {
      flush();
      cur = { display: m[1].trim(), chapters: m[2].split(/[,\s]+/).filter(Boolean), src: m[3].trim(), defLines: [] };
    } else if (cur) {
      if (ln.trim() === '' && cur.defLines.length) flush();
      else if (ln.trim() !== '') cur.defLines.push(ln.trim());
    }
  }
  flush();
}
function addEntry(c) {
  const key = norm(c.display);
  if (!key) return;
  const def = c.defLines.join(' ').trim();
  if (!entries.has(key)) entries.set(key, { display: c.display, chapters: new Set(), src: '-', def });
  const e = entries.get(key);
  c.chapters.forEach(ch => e.chapters.add(ch));
  if ((e.src === '-' || !e.src) && c.src && c.src !== '-') e.src = c.src;
  if (def.length > e.def.length) e.def = def; // keep the fuller definition
}

// --- assemble A–Z ---
const all = [...entries.values()].sort((a, b) => a.display.toLowerCase().localeCompare(b.display.toLowerCase()));
const bucket = (d) => { const c = d.replace(/^[^a-z0-9]+/i, '')[0]; return c && /[a-z]/i.test(c) ? c.toUpperCase() : '#'; };
const groups = new Map();
for (const e of all) { const b = bucket(e.display); if (!groups.has(b)) groups.set(b, []); groups.get(b).push(e); }
const order = [...groups.keys()].sort((a, b) => a === '#' ? -1 : b === '#' ? 1 : a.localeCompare(b));

const chTag = (set) => [...set].sort().map(c => c.replace(/^0/, '') || c).join(', ');
let md = `# Branding and AI — Glossary\n\n`;
md += `> ${all.length} terms, A–Z. Definitions are in the book's voice; citations link a sourced reference where one exists in the project's facts slice. Chapter tags show where each term is used.\n`;
md += `> Generated from chapters' \`## Key Terms\` sections plus proposed terms for chapters without one. Regenerate via \`SCRIPTS/glossary-extract.mjs\` → batch authoring → \`SCRIPTS/glossary-merge.mjs\`.\n\n`;
md += `---\n\n`;
for (const g of order) {
  md += `## ${g}\n\n`;
  for (const e of groups.get(g)) {
    const cite = e.src && e.src !== '-' ? `  \n  *Source: [${hostName(e.src)}](${e.src})*` : '';
    md += `**${e.display}** *(ch ${chTag(e.chapters)})*  \n${e.def}${cite}\n\n`;
  }
}
function hostName(u) { try { return new URL(u).hostname.replace(/^www\./, ''); } catch { return 'source'; } }

// --- foundational-gaps appendix from facts graph ---
let gaps = [];
if (existsSync(join(FACTS_DIR, 'graph.json'))) {
  const g = JSON.parse(readFileSync(join(FACTS_DIR, 'graph.json'), 'utf8'));
  const covered = new Set([...entries.keys()]);
  const nodes = (g.nodes || []).filter(n => (n.in_degree || 0) >= 2)
    .sort((a, b) => (b.in_degree || 0) - (a.in_degree || 0));
  for (const n of nodes) {
    const k = norm(n.term);
    const hit = covered.has(k) || [...covered].some(c => c.includes(k) || k.includes(c));
    if (!hit) gaps.push(n);
  }
}
if (gaps.length) {
  md += `---\n\n## Appendix — Foundational concepts not yet named in the book\n\n`;
  md += `> Concepts the branding knowledge graph treats as foundational (linked by ≥2 other branding pages) that the book's glossary does not currently define. Candidates for future coverage — not gaps in the existing text.\n\n`;
  for (const n of gaps.slice(0, 25)) md += `- **${n.term}** — linked by ${n.in_degree} pages · ${n.url}\n`;
  md += `\n`;
}

const dest = join(BOOK, 'key-terms', 'Glossary.md');
writeFileSync(dest, md);
console.log(`merged entries: ${all.length}`);
console.log(`with citations: ${all.filter(e => e.src && e.src !== '-').length}`);
console.log(`foundational-gap candidates: ${gaps.length}`);
console.log(`-> ${dest}`);
