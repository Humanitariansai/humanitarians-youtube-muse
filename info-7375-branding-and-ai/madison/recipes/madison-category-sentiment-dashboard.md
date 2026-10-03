---
status: DRAFT
todos_open: 15
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison Category Sentiment Dashboard

## Purpose

Aggregates public and owned-channel sentiment across a product category so marketers can see whether the category climate supports promotion, education, repositioning, or caution.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-category-sentiment-dashboard.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Category query config | JSON | [TODO: DATA SOURCE] Approved category terms, exclusions, competitors, and channels. | Yes |
| Sentiment records | JSON/CSV/RSS | [TODO: DATA SOURCE] News, review, survey, social archive, or support-theme records. | Yes |
| Dashboard schema | JSON | [TODO: DEV] Define chart fields, grouping keys, and date buckets. | Yes |
| Mycroft adaptation source | Markdown | `/Users/bear/Documents/CoWork/bear-textbooks/books/mycroft/recipes/market-sentiment-analysis-part-1.md` | No |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-category-sentiment-dashboard.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-category-sentiment-dashboard.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-category-sentiment-dashboard/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-category-sentiment-dashboard data/verified/madison-category-sentiment-dashboard -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-category-sentiment-dashboard-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-category-sentiment-dashboard.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-category-sentiment-dashboard-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-category-sentiment-dashboard.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-category-sentiment-dashboard-[DATE].json && test -f reports/generated/madison-category-sentiment-dashboard-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-category-sentiment-dashboard-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-category-sentiment-dashboard-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-category-sentiment-dashboard/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-category-sentiment-dashboard-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-category-sentiment-dashboard/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-category-sentiment-dashboard-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-category-sentiment-dashboard/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-category-sentiment-dashboard-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-category-sentiment-dashboard-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-category-sentiment-dashboard`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-category-sentiment-dashboard-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-category-sentiment-dashboard-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison Category Sentiment Dashboard` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if category query config is missing because trends would be unscoped.
- Stop if dashboard schema is undefined because charts would be arbitrary.
- Stop if sentiment trends are reported without date buckets or source coverage.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-category-sentiment-dashboard --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-category-sentiment-dashboard --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-category-sentiment-dashboard --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-category-sentiment-dashboard --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-category-sentiment-dashboard --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-category-sentiment-dashboard --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-category-sentiment-dashboard --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-category-sentiment-dashboard --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-category-sentiment-dashboard --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-category-sentiment-dashboard-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-category-sentiment-dashboard-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-category-sentiment-dashboard-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-category-sentiment-dashboard-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-category-sentiment-dashboard-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-category-sentiment-dashboard-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-category-sentiment-dashboard/` | JSON |
| Verified data | `data/verified/madison-category-sentiment-dashboard/` | JSON |
| Agent log | `logs/madison-category-sentiment-dashboard-[DATE].json` | JSON |
| Human report | `reports/generated/madison-category-sentiment-dashboard-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `recipes/madison-category-sentiment-dashboard.md` | `test -f "recipes/madison-category-sentiment-dashboard.md"` | Current recipe file used as spec-first provenance. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Aggregates public and owned-channel sentiment across a product category so marketers can see whether the category climate supports promotion, education, repositioning, or caution.

1. Category gate: query config is approved. Test: `python3 -m json.tool data/raw/madison-category-sentiment-dashboard/category-query-config.json`. Human capacity: [PF].
2. Dashboard gate: chart fields and date buckets are defined. Test: `rg -n "TODO:" recipes/madison-category-sentiment-dashboard.md`. Human capacity: [PA].
3. Sample gate: sample mode creates local dashboard data only. Test: `snickerdoodle run madison-category-sentiment-dashboard --mode dialogic --sample`. Human capacity: [TO].

1. Step name: Ingest category sentiment records. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/ingest/madison-category-sentiment-dashboard-ingest-category-sentiment-records.py`
   Input: category query config and approved sentiment sources.
   Output: raw JSON fields: source, channel, text, url_or_record_id, published_at, category_term, brand_term.
   Where output goes: `data/raw/madison-category-sentiment-dashboard/`.
2. Step name: Aggregate category sentiment. Labor: AI with Human gate.
   Script called: `[TODO: DEV] Create scripts/gigo/madison-category-sentiment-dashboard-aggregate-category-sentiment.py`
   Input: raw sentiment records and dashboard schema.
   Output: verified JSON fields: date_bucket, channel, category, sentiment_counts, volume, confidence_notes, flags.
   Where output goes: `data/verified/madison-category-sentiment-dashboard/`.
3. Step name: Produce category dashboard report. Labor: AI with Human review.
   Script called: `[TODO: DEV] Create scripts/tools/madison-category-sentiment-dashboard-produce-category-dashboard-report.py`
   Input: verified dashboard data.
   Output: markdown sections: category mood, channel breakdown, sentiment trends, evidence samples, campaign timing recommendation.
   Where output goes: `reports/generated/`.
