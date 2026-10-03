---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Brand Consistency Contradiction Checker

## Purpose

Compares brand claims across websites, ads, press releases, decks, social posts, and investor-facing materials so a brand owner can find contradictions before customers, regulators, or partners do.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-brand-consistency-contradiction-checker.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Brand claim corpus | JSON/Markdown | [TODO: DATA SOURCE] Approved website, ad, press, deck, and social claim files. | Yes |
| Claim taxonomy | JSON | [TODO: DEFINE] Define product, price, availability, ESG, privacy, safety, and performance claim types. | Yes |
| Contradiction rubric | JSON | [TODO: DEFINE] Define direct conflict, stale claim, scope mismatch, and unsupported claim. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/contradiction-detection-agent.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-brand-consistency-contradiction-checker.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-brand-consistency-contradiction-checker.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-brand-consistency-contradiction-checker/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-brand-consistency-contradiction-checker data/verified/madison-brand-consistency-contradiction-checker -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-brand-consistency-contradiction-checker-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-brand-consistency-contradiction-checker.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-brand-consistency-contradiction-checker-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-brand-consistency-contradiction-checker.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-brand-consistency-contradiction-checker-[DATE].json && test -f reports/generated/madison-brand-consistency-contradiction-checker-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-consistency-contradiction-checker-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-brand-consistency-contradiction-checker-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-brand-consistency-contradiction-checker/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-consistency-contradiction-checker-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-brand-consistency-contradiction-checker/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-brand-consistency-contradiction-checker-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-brand-consistency-contradiction-checker/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-consistency-contradiction-checker-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-brand-consistency-contradiction-checker-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-brand-consistency-contradiction-checker`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-brand-consistency-contradiction-checker-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-brand-consistency-contradiction-checker-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Brand Consistency Contradiction Checker` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if claim sources are not approved because the checker could audit drafts as live claims.
- Stop if contradiction rubric is undefined because severity would be subjective.
- Stop if legal or public correction actions are requested without human approval.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-brand-consistency-contradiction-checker --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-brand-consistency-contradiction-checker --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-brand-consistency-contradiction-checker --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-brand-consistency-contradiction-checker --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-brand-consistency-contradiction-checker --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-brand-consistency-contradiction-checker --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-brand-consistency-contradiction-checker --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-brand-consistency-contradiction-checker --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-brand-consistency-contradiction-checker --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-brand-consistency-contradiction-checker-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-brand-consistency-contradiction-checker-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-brand-consistency-contradiction-checker-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-brand-consistency-contradiction-checker-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-brand-consistency-contradiction-checker-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-brand-consistency-contradiction-checker-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-brand-consistency-contradiction-checker/` | JSON |
| Verified data | `data/verified/madison-brand-consistency-contradiction-checker/` | JSON |
| Agent log | `logs/madison-brand-consistency-contradiction-checker-[DATE].json` | JSON |
| Human report | `reports/generated/madison-brand-consistency-contradiction-checker-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-brand-consistency-contradiction-checker.md` | `test -f "recipes/madison-brand-consistency-contradiction-checker.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Compares brand claims across websites, ads, press releases, decks, social posts, and investor-facing materials so a brand owner can find contradictions before customers, regulators, or partners do.

1. Corpus gate: all claim sources are approved and current. Test: `rg -n "TODO:" recipes/madison-brand-consistency-contradiction-checker.md`. Human capacity: [PF].
2. Taxonomy gate: claim types are defined before extraction. Test: `python3 -m json.tool data/raw/madison-brand-consistency-contradiction-checker/claim-taxonomy.json`. Human capacity: [IJ].
3. Sample gate: sample mode produces local contradiction records only. Test: `snickerdoodle run madison-brand-consistency-contradiction-checker --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest brand claims. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-brand-consistency-contradiction-checker-ingest-brand-claims.py`
   Input: approved claim corpus.
   Output: raw JSON fields: source_id, source_type, title, url_or_path, claim_text, collected_at.
   Where output goes: `data/raw/madison-brand-consistency-contradiction-checker/`.
2. Step name: Detect contradictions. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-brand-consistency-contradiction-checker-detect-contradictions.py`
   Input: raw claim records, claim taxonomy, contradiction rubric.
   Output: verified JSON fields: contradiction_id, claim_a, claim_b, conflict_type, severity, evidence_refs, recommended_owner.
   Where output goes: `data/verified/madison-brand-consistency-contradiction-checker/`.
3. Step name: Produce contradiction report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-brand-consistency-contradiction-checker-produce-contradiction-report.py`
   Input: verified contradiction records.
   Output: markdown sections: high-risk contradictions, stale claims, unsupported claims, source links, remediation owner.
   Where output goes: `reports/generated/`.
