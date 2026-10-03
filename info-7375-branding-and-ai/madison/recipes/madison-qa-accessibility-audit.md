---
status: DRAFT
todos_open: 10
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Madison QA And Accessibility Audit

## Purpose

Audits generated campaign templates before launch handoff. The Email QA Agent checks links, variables, scheduling logic, HTML validity, copy, and launch readiness. The Email Accessibility Agent checks WCAG, ADA, AODA, Section 508, and EN 301 549.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/madison-qa-accessibility-audit.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Copy variants | JSON | `data/verified/madison-branding-marketing-pipeline/copy-variants-verified.json` | Yes |
| Email templates | ZML/HTML files | `data/verified/madison-branding-marketing-pipeline/email-templates/` | Yes |
| Campaign structure | JSON | `data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json` | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/madison-qa-accessibility-audit.md" && rg -n "\[TODO: DEFINE]" "recipes/madison-qa-accessibility-audit.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/madison-qa-accessibility-audit/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/madison-qa-accessibility-audit data/verified/madison-qa-accessibility-audit -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/madison-qa-accessibility-audit-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/madison-qa-accessibility-audit.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/madison-qa-accessibility-audit-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/madison-qa-accessibility-audit.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/madison-qa-accessibility-audit-[DATE].json && test -f reports/generated/madison-qa-accessibility-audit-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-qa-accessibility-audit-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/madison-qa-accessibility-audit-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/madison-qa-accessibility-audit/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-qa-accessibility-audit-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/madison-qa-accessibility-audit/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-qa-accessibility-audit-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/madison-qa-accessibility-audit/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-qa-accessibility-audit-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/madison-qa-accessibility-audit-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `madison-qa-accessibility-audit`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/madison-qa-accessibility-audit-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/madison-qa-accessibility-audit-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `Madison QA And Accessibility Audit` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if templates are missing.
- Stop if QA results are summary-only and do not identify failing fields.
- Stop if any FAIL item is open.
- Stop if Gate G4 is not approved.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run madison-qa-accessibility-audit --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run madison-qa-accessibility-audit --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run madison-qa-accessibility-audit --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run madison-qa-accessibility-audit --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run madison-qa-accessibility-audit --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run madison-qa-accessibility-audit --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run madison-qa-accessibility-audit --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run madison-qa-accessibility-audit --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate madison-qa-accessibility-audit --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/madison-qa-accessibility-audit-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/madison-qa-accessibility-audit-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/madison-qa-accessibility-audit-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/madison-qa-accessibility-audit-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/madison-qa-accessibility-audit-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/madison-qa-accessibility-audit-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/madison-qa-accessibility-audit/` | JSON |
| Verified data | `data/verified/madison-qa-accessibility-audit/` | JSON |
| Agent log | `logs/madison-qa-accessibility-audit-[DATE].json` | JSON |
| Human report | `reports/generated/madison-qa-accessibility-audit-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json` | `test -f "data/verified/madison-branding-marketing-pipeline/campaign-structure-verified.json"` | Referenced source/evidence path from prior recipe text. |
| `data/verified/madison-branding-marketing-pipeline/copy-variants-verified.json` | `test -f "data/verified/madison-branding-marketing-pipeline/copy-variants-verified.json"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Extracted Notes

Audits generated campaign templates before launch handoff. The Email QA Agent checks links, variables, scheduling logic, HTML validity, copy, and launch readiness. The Email Accessibility Agent checks WCAG, ADA, AODA, Section 508, and EN 301 549.

1. Input readiness gate: Every required input in this recipe exists or is marked with a typed TODO. Test: `rg -n "TODO:" recipes/madison-qa-accessibility-audit.md`.
   Human capacity: [PA].
2. Sample run gate: Ingest and tool steps run without live side effects before live mode. Test: `snickerdoodle run madison-qa-accessibility-audit --mode dialogic --sample`.
   Human capacity: [TO].
3. Data-shape gate: Raw and verified outputs parse as JSON where applicable. Test: `find data/raw/madison-qa-accessibility-audit data/verified/madison-qa-accessibility-audit -name "*.json" -print -exec python3 -m json.tool {} \;`.
   Human capacity: [IJ].
4. Report contract gate: Human report defines reader, decision enabled, and sections. Test: `rg -n "Reader:|Decision enabled:|Sections:" recipes/madison-qa-accessibility-audit.md`.
   Human capacity: [EI].

1. Step name: Run QA and accessibility audit. Labor: AI with Human gate.
   Script called: `scripts/gigo/madison-gigo-qa-audit.py`
   Input: copy-variants-verified.json, email templates, and campaign-structure-verified.json.
   Output: qa-audit-report JSON fields: template_id, check_id, standard, status, severity, remediation, blocker_flag plus markdown QA report.
   Where output goes: data/verified/madison-branding-marketing-pipeline/.
2. Step name: Gate G4 review. Labor: Human.
   Human action: Record approval, rejection, or requested changes with supervisory capacity label [TODO: DEFINE].
   Input: qa-audit-report.json and generated QA markdown.
   Output: gate decision with blocker count, remediation notes, and approval status.
   Where output goes: logs/gate-G4-qa.json.
