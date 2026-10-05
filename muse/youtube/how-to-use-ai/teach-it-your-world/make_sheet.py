#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Teach it your world" (How-to-AI series).

SKILL: ai-explainer (switched from the assigned cc-explainer; reasoning in
BUILD-LOG.md). Liam, "in for Bear"; Kokoro am_onyx; Teardown register;
channel claude-liam; watermark @NikBearBrown.

Premise: the AI knows the world's knowledge, not YOUR world. Upload your own
documents (attachments, a project's knowledge shelf) and it answers from your
material. Non-technical: RAG ("the AI searches your documents, then answers
from what it finds"), embeddings ("similar meanings sit near each other"), and
grounding ("answer only from what I handed you") are all explained in plain
words by showing. Facts verified 2026-10-04 (see FACTCHECK.md); the anchor
source is Anthropic's own help article "Retrieval augmented generation (RAG)
for projects" (support.anthropic.com, opened live 2026-10-04).

Spine: B00 composer cold open (ask without docs -> generic answer) ->
B01 hesitant-writer BLUF -> BDEFS terms card -> B02-B08 Manim body ->
BVDT verdict artifact -> BHTF your-turn composer -> BOUT title outro.

No pricing tiers anywhere (standing rule). No model version numbers.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "teach-it-your-world"
TITLE = "Teach it your world"

WPM = 2.5  # Kokoro words-per-second estimate, same as sibling sheets


def dur(narration):
    return round(len(narration.split()) / WPM, 1)


def graphic(bid, act, narration, cls, visual_intent, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": dur(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own",
                  "visual_intent": visual_intent, "show": show,
                  "manim": {"class": cls},
                  "motion_claim": visual_intent}}
    b.update(extra)
    return b


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": dur(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
# ---------------------------------------------------------------- cold open
remotion(
    "B00", "the question",
    "Konnichiwa \u2014 this is Liam, in for Bear. Watch: I ask the AI about MY "
    "trek, and it hands me EVERYONE's trek. It knows the world. It does not know "
    "my world. That is the gap this film closes: how to teach it YOUR world, so "
    "it answers from your material, not the internet's.",
    "ClaudeComposerAsk",
    {"greeting": "Konnichiwa, Liam",
     "topic": "HOW TO AI \u00b7 Teach it your world",
     "segment": "Humanitarians AI",
     "command": "What should I pack for my trek next month?",
     "running_text": "thinking\u2026",
     "output": ["A trek packing list: layered clothing,",
                "waterproof shell, first-aid kit,",
                "headlamp, and trail snacks."],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer types the command: 'What should I pack for my trek next month?'"},
     {"at": 0.35, "event": "Running indicator; the generic packing list types in, line by line"},
     {"at": 0.8, "event": "The generic list holds \u2014 correct for everyone, right for no one"}],
    motion_claim="The composer asks a personal question and gets the internet's generic answer: the gap, in one exchange.",
    qc={"sparse_by_design": True, "sparse_reason": "Cold-open composer beat: the ask lands answered (ASK\u2192RESULT)."}),

# ---------------------------------------------------------------- BLUF
remotion(
    "B01", "the idea",
    "The AI is smart when you give it your material. Upload your own documents "
    "\u2014 your notes, your team's manuals, your policies \u2014 and it stops "
    "answering from the internet and starts answering from your world. This film "
    "shows you what to hand it, the three habits that make it stick, and where "
    "the trick bites back.",
    "BrutalistHesitantWriter",
    {"text": "AI is smart because it knows everything.\nHand it your documents, and it answers from your world.",
     "triggerWords": "because it knows everything",
     "replacementWords": "when you give it your material",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
     "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "Writer types the naive overview"},
     {"at": 0.45, "event": "'because it knows everything' is struck through and corrected"},
     {"at": 0.75, "event": "Final corrected overview holds; narration states the stakes"}],
    lead_silence_s=0.8,
    motion_claim="The writer corrects the misconception: the AI is not smart because it knows everything \u2014 it is useful when you hand it your material.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),

# ---------------------------------------------------------------- definitions
remotion(
    "BDEFS", "terms",
    "Four terms. A knowledge base: your own documents, gathered in one place for "
    "the AI. An upload: copying a file into the chat so the AI can read it. "
    "Grounding: answering only from the material you handed it. And RAG: the AI "
    "searches your documents, then answers from what it finds. Plain words from "
    "here on.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [
        {"term": "knowledge base",
         "meaning": "your own documents, gathered in one place for the AI"},
        {"term": "upload",
         "meaning": "copying a file into the chat so the AI can read it"},
        {"term": "grounding",
         "meaning": "answering only from the material you handed it"},
        {"term": "RAG",
         "meaning": "the AI searches your documents, then answers from what it finds"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'knowledge base' lands"},
     {"at": 0.38, "event": "'upload' lands"},
     {"at": 0.62, "event": "'grounding' lands"},
     {"at": 0.84, "event": "'RAG' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one plain line each."}),

# ---------------------------------------------------------------- B02 the gap
graphic(
    "B02", "the gap",
    "Here is the problem. The AI trained on the internet \u2014 it knows "
    "everyone's everything, and nobody's specifics. Ask it who is on call "
    "Friday, and it has no rota to read, so it does what a confident stranger "
    "does: it guesses. A fluent, plausible, completely invented answer. The "
    "knowledge it needs exists \u2014 it just is not in its world. It is in "
    "yours \u2014 your docs: your files, your folders, your head.",
    "B02_TheGap",
    "Left: a big dim circle, 'the internet'. Right: a small kraft box with terracotta tape, 'your docs'. "
    "A question card, 'who's on call Friday?', fires an arrow into the big circle; wobbly squiggle lines "
    "grow as the answer, with an ink '?' beside them.",
    [{"at": 0.1, "event": "big dim circle lands, label 'the internet'"},
     {"at": 0.25, "event": "small taped box lands, label 'your docs'"},
     {"at": 0.45, "event": "question card slides in; arrow fires into the big circle"},
     {"at": 0.65, "event": "wobbly squiggle answer grows; ink '?' lands beside it"}],
    motion_claim="The gap, drawn: a question about YOUR world goes to the internet's knowledge and comes back a guess."),

# ---------------------------------------------------------------- B03 the fix
graphic(
    "B03", "the fix",
    "The fix is embarrassingly simple: give it the source. Attach the rota, "
    "the manual, the notes \u2014 the file goes into the chat, and suddenly "
    "the answer has somewhere to come from. Most AI apps let you attach files "
    "to a conversation, including Claude's. And some give the project a "
    "permanent shelf: Claude's projects keep your documents on hand, so every "
    "chat in that project starts already knowing them.",
    "B03_TheFix",
    "An open kraft box centre-stage. Pages drop into it one by one. Beside it, an answer card whose "
    "squiggles straighten into solid ink lines as a terracotta check lands. Label: 'give it the source'.",
    [{"at": 0.1, "event": "open box lands"},
     {"at": 0.25, "event": "pages drop into the box, one by one"},
     {"at": 0.55, "event": "answer card lands with wobbly lines"},
     {"at": 0.75, "event": "lines straighten into solid ink; terracotta check lands; 'give it the source' label"}],
    motion_claim="The fix, shown: documents go in, the guess becomes an answer with a check."),

# ---------------------------------------------------------------- B04 the librarian
graphic(
    "B04", "the librarian",
    "What happens next is the clever part, and it has a name you will meet: "
    "RAG. The AI does not read all your documents \u2014 that would take "
    "forever. It searches them like a librarian, pulls only the matching "
    "pages \u2014 the rota, not the handbook \u2014 and reads those before it "
    "answers. Anthropic's own help pages "
    "describe exactly this: a search tool that retrieves only the most "
    "relevant information from your uploaded documents. Librarian, not scanner.",
    "B04_TheLibrarian",
    "A shelf of five dim pages. A question card, 'rota?', slides in; two pages glow with terracotta "
    "edges, lift off the shelf, and fly to an answer card whose solid lines draw in. Label: 'librarian'.",
    [{"at": 0.1, "event": "shelf of five dim pages lands"},
     {"at": 0.3, "event": "question card 'rota?' slides in"},
     {"at": 0.5, "event": "two matching pages light with terracotta edges"},
     {"at": 0.65, "event": "the two pages fly to the answer card; its lines draw in; 'librarian' label lands"}],
    motion_claim="RAG in plain words, performed: the librarian pulls only the matching pages, then reads."),

# ---------------------------------------------------------------- B05 meaning map
graphic(
    "B05", "meaning map",
    "How does the librarian know which pages match? Every word becomes a point "
    "on a map \u2014 this is the 'embeddings' idea, in plain words. Points for "
    "similar meanings sit near each other: invoice, receipt, bill cluster "
    "together; elephant lands across the map. So when you ask about billing, "
    "the search pulls the invoice cluster, not the elephant. Meaning becomes "
    "distance. That is the whole trick.",
    "B05_MeaningMap",
    "A dim scatter of dots. Three dots sit close together, labelled 'invoice', 'receipt', 'bill', inside a "
    "terracotta ring; one far dot labelled 'elephant'. Dim grid lines with gaps. Label: 'near = similar meaning'.",
    [{"at": 0.1, "event": "dim dot scatter lands"},
     {"at": 0.3, "event": "the 'invoice / receipt / bill' cluster lights; terracotta ring draws around it"},
     {"at": 0.55, "event": "'elephant' dot lands far away, labelled"},
     {"at": 0.75, "event": "'near = similar meaning' label lands beneath"}],
    motion_claim="Embeddings as a map: similar meanings cluster, so the search finds the right shelf by distance."),

# ---------------------------------------------------------------- B06 what to upload
graphic(
    "B06", "what to upload",
    "So what belongs in the box? Three kinds of material. Your notes \u2014 the "
    "stuff in your head that the internet never saw. Your work documents \u2014 "
    "the handbook, the rota, the meeting notes your team actually lives by: your work docs. And "
    "the only-you-know pile \u2014 your data, your drafts, your sources. "
    "Rule of thumb: if you would attach it to an email to brief a new "
    "colleague, it belongs in the AI's world too.",
    "B06_WhatToUpload",
    "Three open kraft boxes in a row, labels beneath: 'your notes', 'work docs', 'only-you-know'. "
    "A page drops into each box in turn.",
    [{"at": 0.1, "event": "three open boxes land with their labels"},
     {"at": 0.35, "event": "a page drops into 'your notes'"},
     {"at": 0.55, "event": "a page drops into 'work docs'"},
     {"at": 0.75, "event": "a page drops into 'only-you-know'"}],
    motion_claim="Three boxes fill: the three kinds of material that belong in the AI's world."),

# ---------------------------------------------------------------- B07 three habits
graphic(
    "B07", "three habits",
    "Three habits make it stick. One: give it the source \u2014 attach the "
    "file, or keep it on the project's shelf. Two: pin it down \u2014 say "
    "'answer only from these files,' and name the document, so it searches the "
    "rota instead of the handbook. Three: make it quote \u2014 ask for the "
    "exact line it used, and check the quote against your file. A citation you "
    "can verify beats a confident paragraph every time.",
    "B07_ThreeHabits",
    "Three cards in a row, numbered 1-2-3 with one short line each: 'give it the source', "
    "'pin it: only from this', 'make it quote'. A terracotta check lands on each card in turn.",
    [{"at": 0.1, "event": "three numbered cards land"},
     {"at": 0.35, "event": "check lands on card 1"},
     {"at": 0.55, "event": "check lands on card 2"},
     {"at": 0.75, "event": "check lands on card 3"}],
    motion_claim="The working practice, as three stamped cards: source, pin, quote."),

# ---------------------------------------------------------------- B08 where it bites
graphic(
    "B08", "where it bites",
    "Now the teardown \u2014 where this bites. First, the AI never warns you "
    "about what is missing \u2014 your blind spots. It answers from what it "
    "has; silence is not disagreement. Second, stale documents give stale answers \u2014 the box "
    "needs weeding, or last year's policy becomes this year's confidently wrong "
    "reply. Third, it trusts your uploads completely. A wrong document does "
    "not get flagged; it gets quoted. Garbage in, confident garbage out.",
    "B08_WhereItBites",
    "Three mini-panels: a half-empty box ('blind spots'), a cobwebbed page beside a fresh page "
    "('stale in, stale out'), a page with an ink X and a quoted line ('wrong doc = confident quote').",
    [{"at": 0.1, "event": "half-empty box lands, label 'blind spots'"},
     {"at": 0.35, "event": "cobwebbed page vs fresh page land, label 'stale in, stale out'"},
     {"at": 0.6, "event": "wrong page with ink X lands; a quoted line appears beneath it"}],
    motion_claim="The honest teardown in three panels: blind spots, staleness, and misplaced trust."),

# ---------------------------------------------------------------- verdict
remotion(
    "BVDT", "verdict",
    "The verdict. The AI answers from the world's knowledge \u2014 not yours. "
    "Hand it your documents and it searches them, reads the matching parts, "
    "and answers from your material. Pin it to the source, and make it quote. "
    "And the falsifiable test: ask about something only your files know. A "
    "generic answer means the upload never happened.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "Verdict",
     "artifactHeading": "Teach it your world",
     "brandLabel": "@NikBearBrown",
     "artifactLines": [
        "The AI knows the world \u2014 it doesn't know your world.",
        "Upload your documents; it searches them and answers from what it finds.",
        "Pin it: 'answer only from these files' \u2014 and make it quote the line.",
        "Falsifiable: ask about something only your docs know. A generic answer means it never read them."]},
    [{"at": 0.0, "event": "verdict card lands, heading 'Teach it your world'"},
     {"at": 0.25, "event": "lines 1-2 stagger in"},
     {"at": 0.6, "event": "lines 3-4 stagger in; the falsifiable line holds"}],
    motion_claim="The recap as an artifact card: mechanism, practice, and the falsifiable test.",
    qc={"sparse_by_design": True, "sparse_reason": "Verdict artifact page: four recap lines, read in full."}),

# ---------------------------------------------------------------- your turn
remotion(
    "BHTF", "your turn",
    "\"Here is our on-call rota for this month: [paste it]. From now on, answer "
    "my scheduling questions only from this rota, and quote the line you used. "
    "First question: who is on call this Friday?\" Pick any document only you "
    "have \u2014 a rota, a menu, a reading list. Paste it in, pin the AI to it, "
    "and ask a question whose answer you can check. Then check two things "
    "yourself: does the quote match your document, word for word? And what does "
    "it say when the answer is not in there? Take this prompt, run it on your "
    "own material \u2014 and see what it quotes.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.",
     "topic": "CLAUDE \u00b7 YOUR TURN",
     "segment": "Teach It Once",
     "command": "Here is our on-call rota for this month: [paste it]. From now on, answer my scheduling questions only from this rota, and quote the line you used. First question: who is on call this Friday?",
     "running_text": "paste this into Claude\u2026",
     "output": ["Check: does the quoted line match your document?",
                "Check: what does it say when the answer isn't in the rota?"],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}],
    motion_claim="The handoff: a paste-ready prompt read aloud in full, with two self-checks."),

# ---------------------------------------------------------------- outro
remotion(
    "BOUT", "outro",
    "Teach it your world. At Nik Bear Brown. Liam, in for Bear.",
    "ClaudeTitleOutro",
    {"title": "Teach it your world", "slug": SLUG,
     "handle": "@NikBearBrown", "subline": ""},
    [{"at": 0.0, "event": "title restates; handle; mascot"}],
    kind="outro_voice", tail_silence_s=1.0),
]

# ---------------------------------------------------------------- assertions
BEAT_IDS = [b["beat_id"] for b in B]
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
assert BEAT_IDS == ["B00", "B01", "BDEFS", "B02", "B03", "B04", "B05",
                    "B06", "B07", "B08", "BVDT", "BHTF", "BOUT"], BEAT_IDS
MANIM_IDS = [b["beat_id"] for b in B if b["shot"]["type"] == "GRAPHIC"]
assert MANIM_IDS == ["B02", "B03", "B04", "B05", "B06", "B07", "B08"], MANIM_IDS
for b in B:
    assert b["beat_id"] and b["narration_text"] and b["shot"]["type"], b
    assert b.get("estimated_duration_s", 0) > 0, b["beat_id"]
    if b["shot"]["type"] == "GRAPHIC":
        assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
    else:
        assert b["shot"]["remotion"]["pattern"], b["beat_id"]
total = round(sum(b["estimated_duration_s"] for b in B), 1)
assert 180 <= total <= 360, f"total {total}s outside the 3-6 minute window"
# B01 BLUF needs >= 9 s of audio so the typing + correction land
b01 = next(b for b in B if b["beat_id"] == "B01")
assert b01["estimated_duration_s"] >= 9, b01["estimated_duration_s"]
# every until() phrase in scenes.py must be findable in its narration (checked in BUILD-LOG)
UNTIL_PHRASES = {
    "B02": "it guesses", "B03": "the file goes into the chat",
    "B04": "Librarian, not scanner.", "B05": "not the elephant",
    "B06": "belongs in the AI's world too",
    "B07": "beats a confident paragraph", "B08": "confident garbage out",
}
for bid, phrase in UNTIL_PHRASES.items():
    n = next(b for b in B if b["beat_id"] == bid)["narration_text"]
    assert phrase in n, f"{bid}: until() phrase {phrase!r} not in narration"

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "series": "How to AI",
        "audience": "claude-liam", "engine": "kokoro", "voice_kokoro": "am_onyx",
        "persona": "Liam (in for Bear)", "palette": "claude",
        "register": "Teardown", "channel": "claude-liam",
        "folder_label": "@NikBearBrown", "watermark": "@NikBearBrown",
        "skill": "ai-explainer",
        "derived_from": "built from scratch (NEW); research notes in FACTCHECK.md",
        "total_duration_s": total, "beat_count": len(B),
    },
    "beats": B,
}

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote beat_sheet.json: {len(B)} beats, {total}s estimated")
