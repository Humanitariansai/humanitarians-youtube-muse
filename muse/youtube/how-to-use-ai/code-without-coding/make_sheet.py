#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for code-without-coding (How to AI).

SHOW-TELL (Bear, 2026-09-26): one simple isometric drawing per body beat,
minimal labels, Liam's narration carries every idea. No composer cold open,
no verdict card (bookend_exempt); the spoken @NikBearBrown outro stays.

Topic: what a non-programmer can safely build with AI coding tools — and the
three mistakes that bite beginners (start too big; paste secrets; trust
without testing). General audience; every term explained on first use.
The one number (25%, Y Combinator W25) is attributed aloud and captioned.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "code-without-coding"
TITLE = "Code without coding"

YT_PROMPT = ("Build me one small page I can check: a page that picks a random name "
             "from a short list I give you. Show me what each button does. "
             "Do not add anything I did not ask for.")

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b

B = [
 beat("B00",
      "Imagine asking for a page that does exactly what you want — and getting it. "
      "Without writing a line of code. No installs, no jargon, no classes. "
      "Just words in, a page out. That's the whole promise.",
      "B00_YourPage",
      "The hero object: a finished page drops onto the stage, labeled 'your page', with a terracotta check.",
      [{"at": 0.05, "event": "page drops in"}, {"at": 0.35, "event": "label lands; terracotta check"}]),
 beat("B01",
      "Here's how it works. Your words go into the tool, it writes the code, and your page comes back. "
      "Code is just the written instructions the computer follows — think of it as a recipe the computer reads: "
      "do this, then that. The tool writes the recipe. You taste the dish.",
      "B01_HowItWorks",
      "The pipeline: a 'your words' card slides into the Claude window, code lines appear, a finished page lands.",
      [{"at": 0.05, "event": "words card slides into the tool"}, {"at": 0.3, "event": "code lines appear"},
       {"at": 0.6, "event": "finished page lands"}]),
 beat("B02",
      "First, what's safe to build: things you can check by looking. "
      "A page for your hobby. A quiz for your class. A tracker for your walks. "
      "If you can see what's wrong, you can judge it — a typo in a recipe you can see. "
      "That's your first safety rule.",
      "B02_Checkable",
      "Three cards spring up one by one — 'a page', 'a quiz', 'a tracker' — then the banner 'you can check it'.",
      [{"at": 0.1, "event": "'a page' card"}, {"at": 0.35, "event": "'a quiz' card"},
       {"at": 0.6, "event": "'a tracker' card"}, {"at": 0.85, "event": "'you can check it' banner"}]),
 beat("B03",
      "Second safety rule: keep it personal — things that only touch you and your stuff. "
      "Passwords, payments, or other people's data are not a first project. "
      "A tracker for your own workouts is fine. Your data, your mess — "
      "if it breaks, you're the only one who notices.",
      "B03_OnlyYou",
      "Your page sits inside a ring labeled 'only you'; a 'password' card drops toward it, bounces off, and 'not passwords' lands.",
      [{"at": 0.05, "event": "page in the ring, 'only you'"}, {"at": 0.3, "event": "check lands"},
       {"at": 0.55, "event": "'password' card bounces off; 'not passwords'"}]),
 beat("B04",
      "Now the three mistakes that bite beginners. Mistake one: starting too big. "
      "'Build me a whole shop' — and the tool writes thousands of lines you can't check, "
      "then it breaks in ways you can't fix. Start small. Get one thing working, then add the next. "
      "One working button beats ten broken ones.",
      "B04_TooBig",
      "Pages stack too high and topple under a cross ('too big'); then one clean page lands with a check ('one small thing').",
      [{"at": 0.05, "event": "pages stack too high"}, {"at": 0.4, "event": "stack topples, cross, 'too big'"},
       {"at": 0.7, "event": "one page lands, check, 'one small thing'"}]),
 beat("B05",
      "Mistake two: pasting secrets. Your passwords, your keys, anything private — "
      "once it's in the AI, you can't take it back. Never paste anything into an AI that you wouldn't "
      "pin to a noticeboard. Treat the chat like a postcard: anyone along the way could read it.",
      "B05_NoSecrets",
      "A 'password' card drops toward the Claude window; a cross blocks it; the card is rejected; 'never paste' lands.",
      [{"at": 0.05, "event": "'password' card drops toward the tool"}, {"at": 0.4, "event": "cross blocks it"},
       {"at": 0.7, "event": "card rejected; 'never paste'"}]),
 beat("B06",
      "Mistake three: trusting it without testing. The tool says done, the page looks finished — "
      "but there's a bug hiding in a button you never clicked. Always click every button yourself. "
      "If you can't check it, don't ship it. Ten minutes of clicking now saves a week of wondering why it broke.",
      "B06_TestIt",
      "A page with three buttons; a cursor clicks each — two get checks, the third gets a cross and a bug dot.",
      [{"at": 0.05, "event": "page + three buttons"}, {"at": 0.35, "event": "cursor clicks two, checks land"},
       {"at": 0.65, "event": "third button: cross + bug dot"}]),
 beat("B07",
      "And when something breaks — not if, when — don't panic and don't start over. "
      "Describe the problem back to the tool, in the same plain words: 'the button doesn't work; "
      "it should open my list.' It fixes the code. You check it again. "
      "Describe, check, repeat. That's the whole loop.",
      "B07_DescribeItBack",
      "A page with a bug dot; an arrow draws back to the tool; a fixed page lands with a check ('describe it back').",
      [{"at": 0.05, "event": "page with a bug dot, 'a bug'"}, {"at": 0.35, "event": "arrow draws back to the tool"},
       {"at": 0.6, "event": "fixed page, check, 'describe it back'"}]),
 beat("B08",
      "A quarter of Y Combinator's Winter twenty twenty-five batch — the startup school behind Airbnb and Stripe — "
      "shipped products on codebases that were ninety-five percent AI-written. "
      "That's why this is suddenly possible: the tools got that good. "
      "If startups ship on AI-written code, your one page is well within reach.",
      "B08_WhyNow",
      "The number beat: hero '25%' in ink, an ink curve sweeps up with a terracotta end dot, caption 'per Y Combinator'.",
      [{"at": 0.05, "event": "'25%' lands"}, {"at": 0.15, "event": "ink curve sweeps up, terracotta end dot"},
       {"at": 0.3, "event": "'per Y Combinator' caption"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. I don't write code, and I bet some of you don't either. "
    "So the question isn't only what an AI coding tool can build. "
    "It's what you can safely have it build for you.",
    "BrutalistHesitantWriter",
    {"text": "Write me an app that does everything", "triggerWords": "does everything",
     "replacementWords": "does one small thing",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Write me an app that does everything'"},
     {"at": 0.6, "event": "backspaces 'does everything' → 'does one small thing' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive build-everything request and corrects it to one small thing: mistake one's lesson.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Code: the written instructions a computer follows. "
    "An AI coding tool: an AI you describe what you want to, and it writes the code for you. "
    "And a bug: a mistake in the code that makes it do the wrong thing — or nothing at all.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "code", "meaning": "the written instructions a computer follows"},
               {"term": "AI coding tool", "meaning": "an AI you describe what you want to, and it writes the code for you"},
               {"term": "bug", "meaning": "a mistake in the code that makes it do the wrong thing"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'code' lands"}, {"at": 0.5, "event": "'AI coding tool' lands"}, {"at": 0.78, "event": "'bug' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into your AI coding tool: " + YT_PROMPT + " "
    "Then check two things yourself. Does every button do what you asked — click each one? "
    "And did anything private go into it? If it did, take it out before you go on.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Build One Small Thing", "command": YT_PROMPT,
     "runningText": "paste this into your AI coding tool…",
     "output": ["Check: every button does what you asked — click each one yourself.",
                "Check: nothing private went in — no passwords, no keys."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Claude", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.5, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

# ---- assertions: beat count + total duration + structural sanity ----
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
total = sum(b["estimated_duration_s"] for b in B)
assert 180 <= total <= 300, f"total estimated duration {total}s outside 180-300s band"
manim_beats = [b for b in B if b["lane"] == "manim"]
assert len(manim_beats) == 9, f"expected 9 manim body beats, got {len(manim_beats)}"
for b in manim_beats:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
    assert b["shot"]["type"] == "GRAPHIC" and "manim" in b["shot"], b["beat_id"]
    assert b.get("estimated_duration_s") or b.get("actual_duration_s"), b["beat_id"]
idea = next(b for b in B if b["beat_id"] == "BIDEA")
tw = idea["shot"]["remotion"]["props"]["triggerWords"]
assert tw in idea["shot"]["remotion"]["props"]["text"], "triggerWords must appear verbatim in text"
assert not tw.rstrip().endswith(("?", "!", ".")), "triggerWords must not end in punctuation"
rw = idea["shot"]["remotion"]["props"]["replacementWords"]
assert not rw.rstrip().endswith(("?", "!", ".")), "replacementWords must not end in punctuation"
defs = next(b for b in B if b["beat_id"] == "BDEFS")
assert all(len(t["term"]) <= 17 for t in defs["shot"]["remotion"]["props"]["terms"]), "BDEFS term too long"
for bid in ("BIDEA", "BDEFS", "BHTF", "BOUT"):
    bb = next(b for b in B if b["beat_id"] == bid)
    assert bb["lane"] == "bookend" and "remotion" in bb["shot"], bid
assert "YOUR TURN" in YOURTURN["shot"]["remotion"]["props"]["topic"], "BHTF topic must contain YOUR TURN"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · AI CODING FOR NON-PROGRAMMERS",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hallo (German/Dutch)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + "
                             "terms card, no verdict card; Your Turn is the Claude.ai composer; "
                             "spoken outro stays.",
    "audience": "smart general audience — curious non-experts; every term explained on first use",
    "source_doc": "NEW film (no mirror-repo source). The one number (25% / 95% AI-written, Y Combinator W25) "
                  "verified 2026-10-04 via web search: TechCrunch (Mar 2025) reporting YC managing partner "
                  "Jared Friedman and CEO Garry Tan in the YC YouTube video 'Vibe Coding is the Future'. "
                  "Attribution is spoken aloud and captioned on screen.",
    "playlist": "How to AI", "chapter_number": 0,
    "tags": ["AI coding tools", "vibe coding", "no-code", "beginners", "Claude", "AI basics", "how to AI",
             "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total, 1), "s")
