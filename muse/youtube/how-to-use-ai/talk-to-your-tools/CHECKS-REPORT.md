# CHECKS-REPORT.md — Talk to your tools

QC gate run 2026-10-04, package `muse/youtube/how-to-use-ai/talk-to-your-tools/`.

## Gate 1 — py_compile

| file | result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — static_scene_check (Gate A simulation)

Run from `/tmp/gatea-ttt/` holding **only** `scenes.py` — exactly what `art run`'s
Gate A sees. Command per class:
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| class | warnings | errors |
|---|---|---|
| B00_TheGap | 0 | 0 |
| B01_ThePlug | 0 | 0 |
| B02_Permissions | 0 | 0 |
| B03_MorningBrief | 0 | 0 |
| B04_InboxTriage | 0 | 0 |
| B05_MeetingPrep | 0 | 0 |
| B06_YouSend | 0 | 0 |
| B07_PullThePlug | 0 | 0 |
| B08_StrangerInvite | 0 | 0 |

Also ran all 9 with `beat_sheet.json` beside `scenes.py` to confirm the
`until()`/`finish()` pacing path executes: 0 warnings, 0 errors.

Additionally verified by script: every `until()` phrase (19) appears verbatim
in its beat's `narration_text` (all present).

## Gate 3 — make_sheet.py asserts

All asserts passed at generation time: 13 beats in the show-tell spine order;
total 243.6 s inside the 200–300 s band; every manim beat carries a
`shot.manim.class` named for its beat id; BIDEA `triggerWords`
("give Claude my passwords") verbatim in `text`, trigger/replacement free of
trailing punctuation; all BDEFS terms ≤ 17 chars; BHTF topic contains
"YOUR TURN", greeting exactly "Your turn.", two output checks, prompt read in
full; BOUT `kind: outro_voice` with 1.0 s tail ending "At Nik Bear Brown.".

## Skill switch (for the record)

Assigned skill was `cc-explainer`; built with `show-tell` (reasoning in
BUILD-LOG.md). cc-explainer's TERMINAL-FIRST and REAL-SESSION laws require a
reconstructed Claude Code terminal session, which this film does not have.
The sheet declares `metadata.skill: "show-tell"` honestly.

## Known gaps (not failures — deferred to the Mac render pass)

1. `manim_layout_audit.py --curve-strict` not run — no Manim/pangocairo in
   this VM. Mitigation: hand-placed labels (≥ 0.3 leader gaps, no curve/label
   crossings), all coords inside ±6.2 × ±3.3, type ≥ 32; cables edged in
   deep kraft (`#9C8462`) to avoid GATE T fusion with the dark socket.
   **Run before the 4K render.**
2. Midpoint render-guard not verifiable without measured Kokoro audio.
   Mitigation: event phrases timed off the 45–55% window (see SHOTLIST.md;
   B04 uses `lead=0.5`). **Re-verify after audio measurement.**
3. Whisper transcript check of BIDEA ("Hallo") — **at render time**.
