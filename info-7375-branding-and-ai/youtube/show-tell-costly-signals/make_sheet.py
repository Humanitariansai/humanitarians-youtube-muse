#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-costly-signals.

SHOW-TELL, a COURSE film for INFO 7375 Branding and AI. Bear, 2026-09-27, after pasting chapter 1's
Spence section: "when things are cheap to make they hold less value as a signal of what you can do as a
human being so you want to show the things that are irreducibly human the judgment the creativity the
effort ... mention what Spence signaling is ... in the age of AI what used to be very expensive is now
very cheap in some cases mention a few examples but what's even more important now is judgment uh
ideation creativity" (SOURCE.md).

Card test: no beat passes (no interface, no dataset whose motion is the claim), so there are no cards.
Cast: CANDIDATES (sealed kraft boxes: what's inside can't be seen), SIGNALS (white page tags), a SORTER
(two grey lanes), AI (a dark server stack that prints tags), and terracotta tape = the costly, human part.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Cheap to Make, Cheap to Signal"
COURSE = "INFO 7375 Branding and AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "In 1973, the economist Michael Spence asked a simple question. An employer wants productive people, but you can't see productivity until after the hire. So how does anyone choose?",
      "B00_CantSee", "Five sealed kraft boxes drop onto the stage in a row; a grey bracket draws over them ('can't see inside').",
      [{"at": 0.3, "event": "sealed boxes drop in"}, {"at": 0.8, "event": "can't see inside"}]),
 beat("B01", "They look at signals: things you can show that stand in for what they can't see. Spence's example was a degree.",
      "B01_Signal", "White page tags drop onto two of the five boxes ('signal').",
      [{"at": 0.3, "event": "tags land"}, {"at": 0.8, "event": "signal"}]),
 beat("B02", "A degree works as a signal because it's costly, and costlier for some people than for others. It's hard to fake cheaply, so it tells people apart.",
      "B02_Costly", "A staircase of kraft steps builds; two small boxes climb it; one reaches the top and gets a page tag, the other stops halfway ('costly').",
      [{"at": 0.2, "event": "steps build"}, {"at": 0.5, "event": "two climb"}, {"at": 0.8, "event": "one reaches the tag"}]),
 beat("B03", "When the cost holds, the signal separates people. Spence called that a separating equilibrium. The work later shared a Nobel prize, for markets where one side knows more than the other.",
      "B03_Separating", "A grey sorter splits into two lanes; boxes with tags slide into the right lane, boxes without into the left ('separating').",
      [{"at": 0.2, "event": "the sorter draws"}, {"at": 0.5, "event": "boxes split into two lanes"}]),
 beat("B04", "Now AI has made some of those signals nearly free. A working demo app. A clean cover letter. A polished essay, a logo, a slide deck. "
             "In one experiment, programmers with an AI assistant built a small web server in less than half the time.",
      "B04_AIPrints", "A dark server stack lights up and prints page tags, one after another, onto every box in the row ('AI').",
      [{"at": 0.2, "event": "the server lights"}, {"at": 0.4, "event": "tags print onto every box"}]),
 beat("B05", "When everyone can produce the signal, it stops sorting. Spence called that pooling. Everyone looks the same on paper, and the employer is back to guessing.",
      "B05_Pooling", "The two lanes merge into one; every tagged box slides into the same pile ('pooling').",
      [{"at": 0.3, "event": "lanes merge"}, {"at": 0.6, "event": "one pile"}]),
 beat("B06", "So what didn't get cheap? Judgment: choosing what's worth making. Ideation: finding a problem real people actually have. "
             "Creative taste. And the effort of putting something in front of real users and changing it because of what they said. Those still cost you something, so they still signal.",
      "B06_StillCostly", "In the pooled pile, one box lifts out and gets the terracotta tape; three dots light beside it one by one ('judgment').",
      [{"at": 0.2, "event": "one box lifts"}, {"at": 0.4, "event": "judgment"}, {"at": 0.6, "event": "ideation"}, {"at": 0.8, "event": "effort"}]),
 beat("B07", "So show the expensive part. The problem you chose, and why. The versions you threw away. What real users told you, and what you changed. "
             "The artifact is cheap now. The reasons behind it aren't.",
      "B07_ShowIt", "The taped box opens; three white pages rise out of it and fan to the right ('why', 'versions', 'users').",
      [{"at": 0.2, "event": "the box opens"}, {"at": 0.4, "event": "why"}, {"at": 0.6, "event": "versions"}, {"at": 0.8, "event": "users"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Mingalaba. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Branding and AI. "
    "You might think a polished portfolio proves what you can do. It only proves something if it cost you something to make.",
    "BrutalistHesitantWriter",
    {"text": "Does a polished portfolio\nprove what I can do?", "triggerWords": "prove what I can do", "replacementWords": "cost me anything to make",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Does a polished portfolio prove what I can do?'"}, {"at": 0.6, "event": "'prove what I can do' → 'cost me anything to make'"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question and corrects it: does it cost anything to make.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. A signal: something you show that stands in for what others can't see. "
    "A costly signal: one that's hard to fake cheaply, so it tells people apart. "
    "And pooling: when everyone can produce the signal, so it stops telling anyone apart.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "signal", "meaning": "something you show that stands in for what others can't see"},
               {"term": "costly signal", "meaning": "hard to fake cheaply, so it tells people apart"},
               {"term": "pooling", "meaning": "everyone can produce the signal, so it stops sorting"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'signal'"}, {"at": 0.4, "event": "'costly signal'"}, {"at": 0.7, "event": "'pooling'"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here's a project in my portfolio: [describe it]. Act as a skeptical hiring manager who knows AI can produce code and text cheaply. "
             "Tell me which parts of this project an AI could have made in an afternoon, and which parts show judgment an AI couldn't supply. "
             "Then suggest three things I could add so the costly part is visible to a stranger.")
SPOKEN_PROMPT = YT_PROMPT.replace("[describe it]", "describe it")
CHECKS = ["Check: is each 'costly' part something you actually did?",
          "Check: could a stranger see it without asking you?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Pick one project you'd show an employer, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Is each costly part something you actually did? And could a stranger see it without asking you?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 BRANDING AND AI · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · BRANDING AND AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Burmese (Mingalaba) — confirmed unused 2026-09-27",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 Branding and AI students (Fall 2026) building portfolios in the age of AI",
    "bookloop_policy": "Course film: carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-branding-and-ai/chapters/01-the-creative-engineer.md, 'The Machinery: Spence Signaling Mechanism' + Bear's framing, 2026-09-27 (SOURCE.md); Spence 1973 QJE 87(3):355-374; Peng et al., arXiv 2302.06590",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["signaling", "Michael Spence", "costly signals", "portfolio", "judgment", "AI", "hiring", "branding", "INFO 7375", "Northeastern", "Claude", "Nik Bear Brown"]},
    "beats": B}

old = HERE / "beat_sheet.json"
if old.exists():
    prev = {b["beat_id"]: b for b in json.load(open(old))["beats"]}
    for b in B:
        p = prev.get(b["beat_id"])
        if p and p.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file"):
                if p.get(k):
                    b[k] = p[k]
for b in B:
    if not b.get("audio_file") and (HERE / f"mp3/beat-{b['beat_id']}.mp3").exists():
        b["audio_file"] = f"mp3/beat-{b['beat_id']}.mp3"
    rem = b["shot"].get("remotion")
    if rem and b.get("actual_duration_s") and rem["pattern"] in ("ClaudeDefinitions", "BrutalistHesitantWriter"):
        rem["props"]["durationSeconds"] = round(float(b["actual_duration_s"]), 3)
old.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b["estimated_duration_s"] for b in B)), "s")
