#!/usr/bin/env node
// glossary-extract.mjs — deterministic glossary skeleton builder.
// Reads chapters' "## Key Terms" sections + a facts/<topic> knowledge slice,
// matches declared terms to sourced definitions, emits a candidate JSON.
// NO AI / no network. Run from the book root:
//   node SCRIPTS/glossary-extract.mjs --topic branding
//
// Output: key-terms/_glossary-candidates.json  (term, display, chapters[], source{def,url} | null)

import { readFileSync, writeFileSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : d; };
const TOPIC = arg('--topic', 'branding');
const BOOK = process.cwd();
const FACTS_DIR = join(BOOK, '..', '..', 'facts', TOPIC);

// --- normalize a term for matching (not for display) ---
const norm = (s) => s.toLowerCase()
  .replace(/\([^)]*\)/g, ' ')        // drop parentheticals
  .replace(/[‘’']/g, '')   // apostrophes
  .replace(/[^a-z0-9 ]/g, ' ')       // punctuation -> space
  .replace(/\s+/g, ' ').trim()
  .replace(/s$/, '');                // crude singularize

// --- 1. extract declared Key Terms from each chapter ---
const chDir = join(BOOK, 'chapters');
const files = readdirSync(chDir).filter(f => /^\d+.*\.md$/.test(f)).sort();
const terms = new Map(); // normKey -> {display, chapters:Set}

for (const f of files) {
  const txt = readFileSync(join(chDir, f), 'utf8');
  const m = txt.match(/##\s+Key Terms\s*\n([\s\S]*?)(?:\n##\s|\n---\s*\n|$)/);
  if (!m) continue;
  const body = m[1].replace(/\n+/g, ' ').trim();
  // split on middot, allow with/without surrounding spaces
  const parts = body.split(/\s*[·•]\s*/).map(s => s.trim()).filter(Boolean);
  for (const p of parts) {
    const key = norm(p);
    if (!key) continue;
    if (!terms.has(key)) terms.set(key, { display: p, chapters: new Set() });
    terms.get(key).chapters.add(f.replace(/\.md$/, ''));
  }
}

// --- 2. load facts/<topic> definitions, build a lookup ---
const factDefs = new Map(); // normKey -> {def, url, verbatim}
if (existsSync(FACTS_DIR)) {
  const termsJson = existsSync(join(FACTS_DIR, 'terms.json'))
    ? JSON.parse(readFileSync(join(FACTS_DIR, 'terms.json'), 'utf8')) : [];
  for (const t of termsJson) {
    if (!t.term) continue;
    const def = t.definition && String(t.definition).trim();
    if (def) factDefs.set(norm(t.term), { def, url: t.url || null, verbatim: def });
  }
  const factsJson = existsSync(join(FACTS_DIR, 'facts.json'))
    ? JSON.parse(readFileSync(join(FACTS_DIR, 'facts.json'), 'utf8')) : [];
  for (const fct of factsJson) {
    const ev = (fct.evidence || [])[0];
    const label = ev && ev.module;
    if (label && fct.canonical && !factDefs.has(norm(label))) {
      factDefs.set(norm(label), { def: fct.canonical, url: ev.url || null, verbatim: ev.verbatim || fct.canonical });
    }
  }
} else {
  console.error(`! facts dir not found: ${FACTS_DIR} (continuing with no sourcing)`);
}

// --- 3. match declared terms to sourced defs ---
const out = [];
let matched = 0;
for (const [key, v] of [...terms.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
  let src = factDefs.get(key) || null;
  if (!src) { // loose contains match
    for (const [fk, fv] of factDefs) {
      if (fk === key) { src = fv; break; }
      if ((fk.includes(key) && key.length > 4) || (key.includes(fk) && fk.length > 4)) { src = fv; break; }
    }
  }
  if (src) matched++;
  out.push({ term: v.display, key, chapters: [...v.chapters].sort(), source: src });
}

const dest = join(BOOK, 'key-terms', '_glossary-candidates.json');
writeFileSync(dest, JSON.stringify(out, null, 2));
console.log(`topic: ${TOPIC}`);
console.log(`chapters with Key Terms: ${new Set(out.flatMap(o => o.chapters)).size}`);
console.log(`declared terms (deduped): ${out.length}`);
console.log(`facts-sourced matches: ${matched}  (${Math.round(100 * matched / (out.length || 1))}%)`);
console.log(`facts definitions available: ${factDefs.size}`);
console.log(`-> ${dest}`);
