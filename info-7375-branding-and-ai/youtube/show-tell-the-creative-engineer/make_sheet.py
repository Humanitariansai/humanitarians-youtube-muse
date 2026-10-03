#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-the-creative-engineer.

SHOW-TELL, a COURSE film for INFO 7375 Branding and AI (credit spoken in BIDEA, on screen in the
BDEFS title and the BHTF composer topic). Bear, 2026-09-27: "Create a show, tell video on the
creative engine[er] here" + his framing (SOURCE.md): designers need to learn the tools because
Claude Code / agentic AI make building easy; engineers need to learn design because routine code
is what AI takes; judgment and creative sense are what stay valuable, more so because it is so
cheap to build, try, and retry. Chapter 1's own spine (the Copilot experiment, the costly-signal
collapse, the four verbs) supplies the evidence.

Card test (SKILL.md): no beat passes, so there are no cards. B00 is numbers, but the chart card's
motion (bars melt into a line) is not the claim; the claim is one bar shrinking, drawn in Manim.

Cast: the SKETCH (a white page, design), the CODE (a dark block, engineering), the BOX (the built
thing, kraft), terracotta tape = the one somebody judged worth making.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "The Creative Engineer"
COURSE = "INFO 7375 Branding and AI · Nik Bear Brown · Northeastern University"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Start with one experiment. In 2022, researchers from GitHub, Microsoft and MIT asked professional programmers to build the same small web server. "
             "The ones working alone took about a hundred and sixty minutes. The ones with GitHub Copilot, an AI coding assistant, took about seventy. Building got cheap.",
      "B00_Cheap", "Two grey bars grow side by side to the same height ('161 min'); then the right bar, 'with Copilot', shrinks to less than half ('71 min').",
      [{"at": 0.3, "event": "both bars grow"}, {"at": 0.75, "event": "the Copilot bar shrinks to 71"}]),
 beat("B01", "When building is cheap, the expensive part moves. Anyone can make the box now. "
             "The hard part is deciding what should go in it, who it's for, and whether it's any good. That's judgment, and no tool decides it for you.",
      "B01_Judgment", "Five kraft boxes drop in fast along a row ('anyone can build'); four fade back; the middle one rises and gets the terracotta tape ('judgment').",
      [{"at": 0.2, "event": "five boxes drop in"}, {"at": 0.6, "event": "one rises, taped"}, {"at": 0.85, "event": "judgment"}]),
 beat("B02", "So designers need the tools. With Claude Code and agentic AI, a designer can turn a sketch into a working thing in an afternoon. "
             "Try it, throw it out, and try again. Producing at that speed used to be the engineer's job. Now it's everyone's.",
      "B02_DesignerBuilds", "A white sketch page on the left ('sketch'); a line draws to the right and a box drops in; the box falls away; a second box drops in, taped ('built').",
      [{"at": 0.15, "event": "sketch"}, {"at": 0.35, "event": "line draws, box drops"}, {"at": 0.55, "event": "thrown out"}, {"at": 0.7, "event": "tried again"}]),
 beat("B03", "And engineers need design. For routine code, the tools already do in minutes what used to take hours, and they keep improving. "
             "A good coder who never decides what to build is competing with the machine, on the machine's ground.",
      "B03_CoderCompetes", "A dark code block on the left ('coder'); on the right, copies of the same block pop in one after another until there are four ('AI').",
      [{"at": 0.15, "event": "coder's block"}, {"at": 0.4, "event": "copies pop in"}, {"at": 0.8, "event": "four of them"}]),
 beat("B04", "Cheap building changes the loop. You can have an idea, build it, try it, and go again, ten times in a day. "
             "The tool will happily make every version. It can't tell you which one is worth keeping. That choice is yours.",
      "B04_Loop", "A grey loop; a terracotta dot runs round it, and each lap drops a small box onto a pile at the right; at the end one box on the left gets the tape ('keep').",
      [{"at": 0.2, "event": "the loop runs"}, {"at": 0.5, "event": "versions pile up"}, {"at": 0.85, "event": "one is kept"}]),
 beat("B05", "The course names four kinds of work. Ideate: deciding what's worth making. Build: making it. "
             "Brand: making sure the people it's for can find it, and know it's for them. Ship: putting it in front of real users. "
             "Build is the one that got cheap. The other three are where the value moved.",
      "B05_FourVerbs", "Four kraft slabs appear one by one, labelled Ideate, Build, Brand, Ship, as a small box hops across them; the Build slab fades to ghost; terracotta dots land under the other three.",
      [{"at": 0.1, "event": "Ideate"}, {"at": 0.2, "event": "Build"}, {"at": 0.35, "event": "Brand"}, {"at": 0.6, "event": "Ship"}, {"at": 0.75, "event": "Build fades"}, {"at": 0.9, "event": "dots on the other three"}]),
 beat("B06", "It changes how people get noticed, too. A working app on GitHub used to take weeks, so having one said something about you. "
             "Now an AI can help anyone make one in an afternoon, and they all start to look the same. What still sets you apart is what the tools can't supply: what you chose to make, and why.",
      "B06_Signal", "A row of five boxes of different heights ('GitHub app'); they all turn into the same box; then one gets the terracotta tape ('why').",
      [{"at": 0.2, "event": "different boxes"}, {"at": 0.55, "event": "they all look the same"}, {"at": 0.85, "event": "one stands out"}]),
 beat("B07", "That's the creative engineer: a designer who can build, or an engineer who can design. "
             "Either way, what you really bring is your creative sense and your judgment. When building is this cheap, those are worth more, not less.",
      "B07_Both", "The sketch page from the left and the code block from the right slide into one open box in the middle; the tape seals it ('creative engineer').",
      [{"at": 0.2, "event": "page and block slide in"}, {"at": 0.6, "event": "sealed"}, {"at": 0.8, "event": "creative engineer"}]),
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
    "Sawasdee. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Branding and AI. "
    "People ask who wins now that AI can code: the designer, or the engineer. The answer is the one who is both.",
    "BrutalistHesitantWriter",
    {"text": "Who wins now,\nthe designer or the engineer?", "triggerWords": "the designer or the engineer", "replacementWords": "the one who is both",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Who wins now, the designer or the engineer?'"}, {"at": 0.6, "event": "'the designer or the engineer' → 'the one who is both'"}],
    lead_silence_s=0.8, motion_claim="The writer types the either-or question and corrects it: the one who is both.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Agentic AI: AI that carries out multi-step work for you, like Claude Code building an app. "
    "Judgment: deciding what to make, for whom, and whether it's good. "
    "And a creative engineer: someone who can both build a thing and decide it's worth building.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "agentic AI", "meaning": "AI that carries out multi-step work, like Claude Code building an app"},
               {"term": "judgment", "meaning": "deciding what to make, for whom, and whether it's good"},
               {"term": "creative engineer", "meaning": "someone who can build a thing and decide it's worth building"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'agentic AI'"}, {"at": 0.4, "event": "'judgment'"}, {"at": 0.7, "event": "'creative engineer'"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here's something I'm planning to build: [one line]. Before I build anything, act as a skeptical design lead. "
             "Ask me five questions about who it's for, what problem it solves for them, and how I'll know it worked. "
             "Then tell me which of my answers are guesses I should test with a real person first.")
SPOKEN_PROMPT = YT_PROMPT.replace("[one line]", "one line")
CHECKS = ["Check: can you name one real person it's for?",
          "Check: which answer did you have to guess?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Pick something you want to build, and paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Can you name one real person it's for? And which of your answers did you have to guess? Test that one before you build.",
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
    "caption_policy": "none", "greeting_language": "Thai (Sawasdee) — confirmed unused 2026-09-27",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 Branding and AI students (Fall 2026): designers and engineers deciding what to learn next",
    "bookloop_policy": "Course film: carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-branding-and-ai/chapters/01-the-creative-engineer.md (opening + Spence + Four Verbs) and Bear's framing, 2026-09-27 (SOURCE.md); Peng et al., arXiv 2302.06590, read 2026-09-27",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["creative engineer", "design and engineering", "agentic AI", "Claude Code", "judgment", "GitHub Copilot", "branding", "INFO 7375", "Northeastern", "Claude", "Nik Bear Brown"]},
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
