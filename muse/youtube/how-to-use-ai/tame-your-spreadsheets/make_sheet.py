#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for tame-your-spreadsheets.

SHOW-TELL film, skill show-tell (assigned; kept: one drawing per beat, the voice
explains — exactly what a formula/cleanup/insight demo needs).

REFACTOR of nikbearbrown/humanitarians-youtube-muse
claude/claude-for-education/claude-liam-how-to-make-perfect-spreadsheets.
The source's argument: let the AI do the spreadsheet mechanics while you stay
in control (its "list assumptions before you build" handshake). Rewritten for a
general, non-expert audience as a three-move coach film: (1) describe the
formula you want in plain English, (2) paste messy data and ask it to clean it,
(3) ask "what's interesting in this data?" — plus the standing warning to
sanity-check formulas on a small sample, because the AI can be confidently
wrong about cell references. All example data is fictional (Lena's Bake Shop).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "tame-your-spreadsheets"
TITLE = "Tame Your Spreadsheets"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00",
      "Start with the thing itself. Picture a small bake shop's sales list: a month of days, one row per day. The fear is normal. A grid of cells looks like maths you forgot, and one wrong keystroke feels like breaking it. But look again: it is just a table. Days down the side, numbers across. You already know how to read a table. And you are about to get a very patient coach — one who never judges you for asking the same question twice.",
      "B00_MessySheet",
      "A flat spreadsheet grid lands on the stage; messy cells pop in (mixed dates, mixed spellings); a rectangle frames one chaotic cell; a terracotta dot marks it. Label: 'a messy spreadsheet'.",
      [{"at": 0.05, "event": "grid draws cell by cell"}, {"at": 0.3, "event": "messy values pop in"}, {"at": 0.6, "event": "chaotic cell framed, dotted"}]),
 beat("B01",
      "Here is the move that changes everything. Instead of memorizing formula syntax, you describe what you want in plain words. You type, or say: write me the formula that adds up my March sales. The AI writes it, explains what each part does, and tells you exactly where to paste it. You are not learning spreadsheet-ese. You are giving instructions the way you would give them to a person sitting next to you. Plain English in, formula out. That is the whole trick.",
      "B01_Coach",
      "The same sheet tidies slightly; a Claude chat page slides in beside it; a bubble holds the hero phrase 'write me the formula that...'; a cable draws from the page to the sheet. Labels: 'plain words', 'the formula'.",
      [{"at": 0.1, "event": "sheet on stage, chat page slides in"}, {"at": 0.45, "event": "prompt bubble appears"}, {"at": 0.7, "event": "cable draws page to sheet"}]),
 beat("B02",
      "Let us watch one land. Lena's sales sit in column B, one row per day. You paste the AI's formula into the empty cell at the bottom: equals, sum, open bracket, B 2 colon B 31, close bracket. Read it left to right. Sum means add up. B 2 is the first sales number. The colon means through. B 31 is the last one. So the whole thing says: add up everything from B 2 to B 31. That B 2 colon B 31 is a cell reference — the address of the stretch you want. Once that pattern clicks, half of spreadsheet fear evaporates.",
      "B02_Formula",
      "The sheet again; an ink bracket grows around column B rows 2 to 31; the formula '=SUM(B2:B31)' lands in the total cell; an ink check ticks beside it. Label: 'the formula'.",
      [{"at": 0.1, "event": "sheet and chat page"}, {"at": 0.4, "event": "bracket grows around B2:B31"}, {"at": 0.65, "event": "formula lands in the total cell, check"}]),
 beat("B03",
      "Now the warning, and it matters. The AI can be confidently wrong about cell references. It can point at the price column instead of the quantity column and call the answer correct. The total looks plausible. It is nonsense. So the rule is simple: sanity-check every formula on a small sample. Add up five rows yourself and compare. If those five match, you can trust the other twenty-six. The AI is your coach, not your accountant. The checking is your job, and it takes about a minute.",
      "B03_Check",
      "The formula highlights the wrong column with an ink cross; a magnifier circles five rows of the right column; the highlight moves; an ink check lands. Label: 'check 5 rows'.",
      [{"at": 0.1, "event": "sheet with formula"}, {"at": 0.35, "event": "wrong column crossed out"}, {"at": 0.6, "event": "magnifier checks five rows, check lands"}]),
 beat("B04",
      "Next superpower: cleanup. Real data arrives messy. Lena copies her market-stall receipts into the sheet and the dates are chaos: the fourth of March, three slash four, oh-four dash oh-three. New York shows up as N Y C, n.y.c. with dots, and plain new york. You paste it all in and ask: clean this up, and make everything consistent. The AI rewrites the dates one way, settles on one spelling per city, and leaves every number untouched. An afternoon of find-and-replace, done in seconds.",
      "B04_Cleanup",
      "A grid of messy rows (mixed dates, mixed city spellings); a terracotta scan line sweeps down; the messy labels are replaced by tidy ones. Labels: 'messy', then 'clean'.",
      [{"at": 0.1, "event": "messy grid"}, {"at": 0.3, "event": "scan line sweeps"}, {"at": 0.55, "event": "tidy values replace messy ones"}]),
 beat("B05",
      "Then the fun one. Ask: what is interesting in this data? You do not need to know what a pivot table is. The AI counts, compares, and answers in plain words: your Saturday sales are nearly double your weekday average. One tall bar. That is the whole point of a spreadsheet — noticing something you could not see in a pile of receipts. And the same rule applies as before: glance back at the sheet and confirm the tall bar is real. The AI proposes. You decide.",
      "B05_Insight",
      "Six grey bars grow for the days of the week; Saturday's bar towers; a terracotta dot tops it; a label reads 'Saturday'. The chat page asks the question.",
      [{"at": 0.1, "event": "day bars grow"}, {"at": 0.55, "event": "Saturday's bar towers, dotted"}, {"at": 0.75, "event": "label lands"}]),
 beat("B06",
      "Look at the sheet now. Same bake shop, same month. The data is clean, the formula adds up the column, and the chart tells the story. You never learned Excel. You described what you wanted, checked the answers, and stayed in charge. A tamed spreadsheet: it works for you, and you understand every cell that matters.",
      "B06_Payoff",
      "The same sheet returns tidy: formula in its cell, clean rows, three small bars beside it; a large ink check grows over the corner. Label: 'you are in charge'.",
      [{"at": 0.1, "event": "tidy sheet with formula"}, {"at": 0.4, "event": "mini chart grows beside it"}, {"at": 0.65, "event": "big check lands"}]),
]

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. Most people open a spreadsheet the way they would open a dentist's bill: reluctantly. So the real question is not how you learn Excel. It is how you tame this spreadsheet.",
    "BrutalistHesitantWriter",
    {"text": "How do I learn Excel,\nto track my sales?", "triggerWords": "learn Excel", "replacementWords": "tame this spreadsheet",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I learn Excel,'"}, {"at": 0.6, "event": "backspaces 'learn Excel' → 'tame this spreadsheet' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive learn-Excel question and corrects it to the real one: taming the spreadsheet.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms, one breath each. A formula: a recipe you type into a cell, and the sheet calculates for you. A cell reference: a cell's address on the grid, like B 2 or C 4. And clean data: the same information written the same way everywhere, so the computer can trust it.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "formula", "meaning": "a recipe typed into a cell — the sheet calculates for you"},
               {"term": "cell reference", "meaning": "a cell's address on the grid, like B2 or C4"},
               {"term": "clean data", "meaning": "the same information written the same way everywhere"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'formula' lands"}, {"at": 0.5, "event": "'cell reference' lands"}, {"at": 0.78, "event": "'clean data' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is my monthly sales list. Write me the formula that adds up column B, and explain what each part does. "
             "Then tell me: what is interesting in this data?")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Two checks you run yourself. Add up five rows by hand and make sure "
    "the formula agrees. And read the AI's answer back against your own sheet before you believe a word of it.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Tame Your First Spreadsheet", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: add up five rows by hand — the formula must agree.", "Check: read the answer back against your own sheet."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "Normal"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · HOW TO AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hallo (German/Dutch)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not AI experts — every term explained, show rather than tell",
    "source_doc": "REFACTOR of nikbearbrown/humanitarians-youtube-muse claude/claude-for-education/claude-liam-how-to-make-perfect-spreadsheets (beat_sheet.json + README.md, read 2026-10-03). All example data fictional (Lena's Bake Shop).",
    "playlist": "How to AI", "chapter_number": 15,
    "watermark": "@NikBearBrown",
    "tags": ["spreadsheets", "formulas", "Excel", "Google Sheets", "Claude", "How to AI", "Nik Bear Brown"]},
    "beats": B}

# ── asserts: beat counts + total duration ──
body = [b for b in B if b["lane"] == "manim"]
assert len(B) == 11, f"expected 11 beats, got {len(B)}"
assert len(body) == 7, f"expected 7 manim body beats, got {len(body)}"
total = sum(b["estimated_duration_s"] for b in B)
assert 180 <= total <= 390, f"total {total}s outside 3-6 min target band"
assert [b["beat_id"] for b in B] == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "B06", "BHTF", "BOUT"]
for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']} missing narration"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats (", len(body), "manim ); est", round(total), "s")
