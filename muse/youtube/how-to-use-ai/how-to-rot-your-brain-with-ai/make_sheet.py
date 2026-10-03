#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "How to outsource everything to AI & get dumb".

SHOW-TELL (Bear, 2026-09-26): one simple isometric Manim drawing per body beat,
minimal labels, Liam's narration (Kokoro am_onyx) explaining the action. The
viewer is a smart general audience, not AI experts: every term is explained in
plain words, ideally by showing.

Source argument (from nikbearbrown/humanitarians-youtube-muse,
claude-for-artificial-intelligence/how-to-rot-your-brain-with-ai):
most people paste a problem into AI and hope it understands; the rule is
"outsource work, not understanding"; the five-step method (constraints, rough
draft, paste draft+constraints, three versions, pick/edit); the trap feels
like getting fast, not getting dumb.

New evidence beats (fact-checked 2026-10-03, see FACTCHECK.md):
- B07: UCL 2017 satnav study (Javadi et al., Nature Communications) — following
  turn-by-turn directions, the hippocampus/prefrontal cortex didn't respond.
- B08: MIT Media Lab 2025 preprint (Kosmyna et al., arXiv:2506.08872) — the
  ChatGPT essay group showed the weakest neural engagement; 83% couldn't quote
  their own essay minutes later (vs 11% without AI). Attributed aloud + captioned.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "how-to-rot-your-brain-with-ai"
TITLE = "How to outsource everything to AI & get dumb"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
    beat("B00",
         "Meet your brain. It runs on use \u2014 the more you think things through, the stronger it gets. "
         "And meet your AI. It never sleeps, never gets tired, and it will do any work you hand it. "
         "The only question: which work should you never hand over?",
         "B00_Hero",
         "A worker with a glowing brain in the head stands left; a dark AI box with a terracotta spark drops in right; labels 'you' and 'your AI'.",
         [{"at": 0.05, "event": "worker fades in with glowing brain"},
          {"at": 0.45, "event": "the dark AI box drops in; its spark lights"},
          {"at": 0.7, "event": "labels 'you' / 'your AI' land"}]),
    beat("B01",
         "Here's how most people use AI. Problem. Open the app. Paste it in. Hope it understands. "
         "Like GPS: it gets you there. But you stop learning the terrain. "
         "And the first time you navigate without it, you're lost in your own city.",
         "B01_PasteHope",
         "A phone draws a turn-by-turn route while a 'terrain knowledge' gauge beside it drains from full to one bar.",
         [{"at": 0.1, "event": "worker and phone arrive"},
          {"at": 0.35, "event": "the route draws on the phone"},
          {"at": 0.6, "event": "the terrain-knowledge gauge fills, then drains"}]),
    beat("B02",
         "So here's the one line you can't cross. Outsource work to AI \u2014 that's fine. "
         "But you cannot outsource understanding. The thinking that happens before you open the app stays yours. "
         "Clear intent in, useful output out. Vague hope in, garbage out.",
         "B02_OneLine",
         "Pages and a gear fly into the AI box and earn an ink check ('work'); a terracotta ring locks around the worker's brain ('understanding').",
         [{"at": 0.05, "event": "worker and AI box on stage"},
          {"at": 0.3, "event": "pages and gear arc into the box; check lands"},
          {"at": 0.65, "event": "the ring grows around the brain; label swaps to 'understanding'"}]),
    beat("B03",
         "The fix is five steps, and the first two are yours \u2014 before you touch the AI. "
         "One: write your constraints. What should this look like, who's reading it, what's not allowed. "
         "Two: write a rough draft. A bad one. That draft is your thinking, on paper.",
         "B03_ThinkFirst",
         "A 'constraints' card lands with its three lines (format, audience, not allowed); a pencil scribbles a messy rough draft on a page.",
         [{"at": 0.05, "event": "the constraints card drops in with its three lines"},
          {"at": 0.5, "event": "page and pencil arrive"},
          {"at": 0.7, "event": "the pencil scribbles the rough draft"}]),
    beat("B04",
         "Three: paste your draft and your constraints into the AI. Four: ask for three versions. "
         "Now the AI is working inside your thinking \u2014 not instead of it.",
         "B04_HandOver",
         "The draft page and constraints card slide into the AI box; three finished pages spring out, labelled '3 versions'.",
         [{"at": 0.05, "event": "draft, constraints card and AI box on stage"},
          {"at": 0.35, "event": "draft and card arc into the box"},
          {"at": 0.65, "event": "three pages spring out; '3 versions' lands"}]),
    beat("B05",
         "Five: pick one version, edit it, call it yours. Two extra minutes of thinking at the start \u2014 "
         "and what comes out is genuinely yours.",
         "B05_YouDecide",
         "Three pages in a row; the middle one lifts, a pencil edit line draws on it, an ink check lands, label 'yours'.",
         [{"at": 0.05, "event": "three pages land in a row"},
          {"at": 0.4, "event": "the middle page lifts"},
          {"at": 0.65, "event": "edit line draws; check and 'yours' land"}]),
    beat("B06",
         "Same method, everywhere you work. A strategy document \u2014 say, a ninety-day rollout plan: you write the goals first. "
         "An email: you write the one point that must land. A spreadsheet: you list your assumptions. Intent first, always.",
         "B06_ThreeDomains",
         "Three stations \u2014 strategy page, email envelope, spreadsheet grid \u2014 each with a small AI box: the pencil writes first, then the work slides into the box.",
         [{"at": 0.05, "event": "three stations land: strategy, email, spreadsheet"},
          {"at": 0.35, "event": "station one: pencil writes, work slides into its AI box"},
          {"at": 0.6, "event": "station two: same motion"},
          {"at": 0.8, "event": "station three: same motion"}]),
    beat("B07",
         "In London, researchers scanned twenty-four volunteers navigating the city. "
         "When they navigated themselves, the brain's navigation areas lit up with every junction. "
         "When they followed turn-by-turn directions, those areas simply didn't respond. "
         "The brain switched off its interest in the streets around it. Published in Nature Communications, 2017.",
         "B07_GPSBrain",
         "A head with a glowing brain region; turn-by-turn arrows arrive and the glow dies to ghost grey; caption 'UCL, 2017'.",
         [{"at": 0.05, "event": "head fades in, brain region glowing"},
          {"at": 0.5, "event": "turn-by-turn arrows draw in from the right"},
          {"at": 0.65, "event": "the glow dies; label swaps to 'GPS navigates'; caption lands"}]),
    beat("B08",
         "And it's not just maps. In 2025, MIT put brain sensors on fifty-four people writing essays. "
         "The ChatGPT group showed the weakest brain engagement \u2014 and afterward, eighty-three percent of them "
         "couldn't quote a single sentence of the essay they'd just written, against eleven percent in the group "
         "that wrote without AI. Per MIT Media Lab \u2014 a preprint, so suggestive, not settled.",
         "B08_EightyThree",
         "Two meters: 'wrote with AI' fills to a hero 83%, 'wrote without AI' to 11%; caption 'per MIT Media Lab, 2025 \u00b7 preprint'.",
         [{"at": 0.1, "event": "'wrote with AI' meter fills; hero 83% lands"},
          {"at": 0.55, "event": "'wrote without AI' meter fills to 11%"},
          {"at": 0.8, "event": "attribution caption lands"}]),
    beat("B09",
         "The trap is subtle. Brain rot doesn't feel like getting dumb. It feels like getting fast. "
         "You're shipping more, faster. But when someone asks why you did it that way, you can't explain. "
         "You used AI to think, so you wouldn't have to.",
         "B09_FastTrap",
         "The AI box streams out pages while a speedometer needle swings up; a 'why?' bubble pops over the worker as his brain gauge drains.",
         [{"at": 0.05, "event": "AI box and worker on stage"},
          {"at": 0.3, "event": "pages stream out; the needle swings up"},
          {"at": 0.65, "event": "'why?' bubble pops; the brain gauge drains"}]),
]

OPEN = [
    remotion("BIDEA", "the question",
             "Hallo. This is Liam, in for Bear. You asked: how do I outsource everything to AI, and stay sharp? "
             "Wrong question. Everything includes the thinking. The real question is: how do I outsource the work, and keep the thinking?",
             "BrutalistHesitantWriter",
             {"text": "How do I outsource everything\nto AI and stay sharp?",
              "triggerWords": "outsource everything", "replacementWords": "outsource the work",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
              "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'How do I outsource everything to AI and stay sharp?'"},
              {"at": 0.6, "event": "backspaces 'outsource everything' \u2192 'outsource the work' on the spoken correction"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive outsource-everything question and corrects it to the real one: outsource the work, keep the thinking.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms you'll hear. Brain rot: your judgment fading, because you stopped doing the thinking. "
             "Outsource: handing work off \u2014 to someone, or to something. And constraints: the rules you set before you start. "
             "The format, who's reading it, and what's not allowed in.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "brain rot",
                         "meaning": "your judgment fading, because you stopped doing the thinking"},
                        {"term": "outsource",
                         "meaning": "handing work off \u2014 to someone, or to something"},
                        {"term": "constraints",
                         "meaning": "the rules you set first: format, audience, what's not allowed"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'brain rot' lands"},
              {"at": 0.5, "event": "'outsource' lands"},
              {"at": 0.78, "event": "'constraints' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True,
                 "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is my rough draft and my constraints: [paste your draft here] "
             "[paste your constraints: audience, format, and what can't be in it]. "
             "Give me 3 improved versions. Keep my core point. Don't change my voice.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Pick one thing you're working on this week. Write your constraints and a rough draft before you open the AI. "
    "Then paste this in: Here is my rough draft and my constraints \u2014 paste your draft, then your constraints: audience, format, "
    "and what can't be in it. Give me three improved versions. Keep my core point. Don't change my voice. "
    "Run it, and notice: the AI is working inside your thinking now, not instead of it.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "AI \u00b7 YOUR TURN", "segment": "Outsource Work, Not Understanding",
     "command": YT_PROMPT, "runningText": "paste this into your AI\u2026",
     "output": ["Check: the AI worked inside your thinking, not instead of it.",
                "Check: you can explain every choice in the version you picked."],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
DENSE_BEATS = {"B06", "B08"}  # three stations / twin meters fill the frame on their own
for b in B:
    if b["lane"] == "manim" and b["beat_id"] not in DENSE_BEATS:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.",
          "estimated_duration_s": round(len(f"{TITLE}. At Nik Bear Brown.".split()) / 2.5, 1),
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown",
                                          "subline": "Outsource work, not understanding."}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

# ═══════════════════════ assertions: beat counts and total duration ═══════════════════════
EXPECTED_IDS = (["BIDEA", "BDEFS"] + [f"B{i:02d}" for i in range(10)] + ["BHTF", "BOUT"])
assert [b["beat_id"] for b in B] == EXPECTED_IDS, "beat ids out of order"
assert len(B) == 14, f"expected 14 beats, got {len(B)}"
assert sum(1 for b in B if b["lane"] == "manim") == 10, "expected 10 manim body beats"
assert sum(1 for b in B if b["lane"] == "bookend") == 4, "expected 4 bookends"
total = sum(b["estimated_duration_s"] for b in B)
assert 200 <= total <= 320, f"total duration {total}s outside 200-320s band"
for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", f"{b['beat_id']}: voice/engine"
    assert b["shot"]["show"], f"{b['beat_id']}: no show block"
    if b["lane"] == "manim":
        cls = b["shot"]["manim"]["class"]
        assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls} must start with beat id"
# BIDEA trigger contract: trigger appears verbatim in text; neither ends in punctuation
_idea = next(b for b in B if b["beat_id"] == "BIDEA")
_tp = _idea["shot"]["remotion"]["props"]
assert _tp["triggerWords"] in _tp["text"].replace("\n", " "), "triggerWords not verbatim in text"
assert not _tp["triggerWords"][-1] in ".?!" and not _tp["replacementWords"][-1] in ".?!", "trigger/replacement must not end in punctuation"
# BDEFS term-length contract (ClaudeDefinitions truncates past ~17 chars)
_defs = next(b for b in B if b["beat_id"] == "BDEFS")
for t in _defs["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"BDEFS term too long: {t['term']!r}"
# BOUT outro contract
_out = next(b for b in B if b["beat_id"] == "BOUT")
assert _out["kind"] == "outro_voice" and _out["tail_silence_s"] == 1.0, "BOUT must be outro_voice with 1.0s tail"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "AI \u00b7 BRAIN ROT", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "engine": "kokoro", "watermark": "@NikBearBrown",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24,
    "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses "
                              "as the second'), no verdict card; Your Turn is the composer; spoken outro stays."),
    "audience": "smart general audience \u2014 pragmatic, not necessarily AI experts; every term explained",
    "source_doc": ("nikbearbrown/humanitarians-youtube-muse, "
                   "claude-for-artificial-intelligence/how-to-rot-your-brain-with-ai/beat_sheet.json (read 2026-10-03); "
                   "evidence beats B07/B08 fact-checked 2026-10-03, see FACTCHECK.md"),
    "playlist": "How to use AI", "chapter_number": 0,
    "tags": ["AI brain rot", "cognitive offloading", "ChatGPT", "how to use AI", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total), "s")
