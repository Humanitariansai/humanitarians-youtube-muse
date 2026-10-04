#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for write-with-ai-sound-like-you.

SHOW-TELL (new style, Bear 2026-09-26): "very simple direct explanations … every beat
needs an image … minimal text … the voice over explains." Every body beat is ONE drawn
illustration (Manim, Claude palette, isometric objects) with at most a few words of
label; Liam's narration carries the explanation. No composer cold open, no verdict or
your-turn cards (bookend_exempt); the spoken @NikBearBrown outro stays (never exempt).

Source: ORIGINAL — built from scratch, no mirror source. Skill: show-tell (assigned).
Card test ran per body beat: every idea is a thing/part/flow (a page, a tray, a box, a
speech bubble, a pencil), so zero cards, all drawings.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "write-with-ai-sound-like-you"
TITLE = "Write with AI, Still Sound Like You"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00",
      "Here is the problem. Most people type a prompt, take the first draft, and ship it. "
      "And every first draft comes out in the same voice — the AI's default voice. Polite, padded, "
      "a little bit robotic. It sounds like everyone. Which means it sounds like no one.",
      "B00_RobotDraft",
      "A dark AI block prints pages; three identical pages drop out in a row, all in the same grey voice; the words 'default voice' sit beside them.",
      [{"at": 0.05, "event": "AI block on stage"}, {"at": 0.3, "event": "first identical page drops"},
       {"at": 0.6, "event": "two more identical pages"}, {"at": 0.85, "event": "'default voice' label"}]),
 beat("B01",
      "Why does that happen? Because the AI has nothing to copy. A draft is a guess, and with no sample "
      "of how you write, the AI falls back on its safest habit — the voice it learned from reading everything. "
      "And 'everything' is exactly what makes it sound like everyone.",
      "B01_NoSample",
      "The same AI block with an empty input tray labelled 'no sample'; identical pages still roll out of it.",
      [{"at": 0.1, "event": "empty tray drops onto the block"}, {"at": 0.45, "event": "'no sample' label"},
       {"at": 0.65, "event": "identical pages roll out anyway"}]),
 beat("B02",
      "Fix one. Give it something to copy. Take one email or paragraph you actually wrote — one that sounds "
      "like you — paste it into your prompt, and add the words: match this voice. Now the AI has your words, "
      "your rhythm, your sentence length. It is copying you now, not the internet.",
      "B02_MatchMyVoice",
      "A white page labelled 'your email' slides into the AI block; a fresh page comes out carrying a terracotta check and the words 'sounds like you'.",
      [{"at": 0.1, "event": "'your email' page on stage"}, {"at": 0.45, "event": "page slides into the block"},
       {"at": 0.7, "event": "new page comes out"}, {"at": 0.9, "event": "check + 'sounds like you'"}]),
 beat("B03",
      "Fix two. Ban the giveaways. AI drafts lean on the same telltale phrases — delve, in today's fast-paced "
      "world, and a forest of em-dashes. None of them are wrong. They are just the uniform. Add one line to "
      "your prompt: never use these words. The draft comes back plainer. Which is to say, more like a person.",
      "B03_BanTheGiveaways",
      "A page lists 'delve', \"in today's fast-paced world\" and a row of em-dashes; each is crossed out in turn; 'the giveaways' beside.",
      [{"at": 0.1, "event": "page with the three phrases"}, {"at": 0.4, "event": "'delve' crossed out"},
       {"at": 0.6, "event": "'fast-paced world' crossed out"}, {"at": 0.8, "event": "em-dashes crossed out"}]),
 beat("B04",
      "Fix three. Stop starting from nothing. Instead of asking the AI to invent your thoughts, dictate your "
      "rough ones — talk it out, typos and all — and ask it to clean them up. It is easier to keep your ideas "
      "and borrow its sentences than to inject your ideas into its sentences.",
      "B04_DictateThenClean",
      "A speech bubble labelled 'rough thoughts' holds messy scribbled lines; a clean page drops beside it labelled 'cleaned up'.",
      [{"at": 0.1, "event": "speech bubble"}, {"at": 0.35, "event": "messy scribbles"}, {"at": 0.7, "event": "clean page drops"}]),
 beat("B05",
      "Fix four. Do the last pass yourself. Read the draft out loud, and anywhere it does not sound like "
      "something you would say, change it in your own words. The AI did the typing. But the voice at the "
      "end — that has to be yours.",
      "B05_YourFinalPass",
      "A page with three lines; a pencil ellipse circles the middle line, which is swapped for a plainer one; a terracotta check lands; 'your pass' beside.",
      [{"at": 0.1, "event": "draft page"}, {"at": 0.45, "event": "line circled"}, {"at": 0.65, "event": "line swapped"},
       {"at": 0.85, "event": "check + 'your pass'"}]),
 beat("B06",
      "Now watch all four fixes on a real email. The default draft says: I hope this email finds you well. "
      "Delving into our proposal dash dash. Nobody talks like that. The fixed version says: Hi Maya, here is "
      "the proposal. Page three has the price. Shout if anything looks off. Same facts. One of them sounds like a person.",
      "B06_TheEmail",
      "Two pages side by side: the left labelled 'default' in grey, the right labelled 'your voice' with a terracotta check.",
      [{"at": 0.1, "event": "'default' page"}, {"at": 0.45, "event": "'your voice' page slides in"},
       {"at": 0.8, "event": "check lands"}]),
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
    "Hallo. This is Liam, in for Bear. AI writing tools will draft anything you ask for. But if you have ever "
    "read what comes back and thought, that does not sound like me, you are not alone. The real question is "
    "not how you make the AI write better. It is how you make it sound like you.",
    "BrutalistHesitantWriter",
    {"text": "How do I get AI to\nwrite better for me?", "triggerWords": "write better", "replacementWords": "sound like me",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get AI to'"}, {"at": 0.5, "event": "backspaces 'write better' → 'sound like me' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive writing question and corrects it to the real one: sounding like you.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms you will need. Voice: the way you sound on the page — your words, your rhythm. A prompt: "
    "the instruction you type before the AI writes anything. And a draft: a rough version that nobody is supposed to see.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "voice", "meaning": "the way you sound on the page — your words, your rhythm"},
               {"term": "prompt", "meaning": "the instruction you type before the AI writes anything"},
               {"term": "draft", "meaning": "a rough version that nobody is supposed to see"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'voice' lands"}, {"at": 0.5, "event": "'prompt' lands"}, {"at": 0.78, "event": "'draft' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is a paragraph I wrote: [paste it]. Match this voice — my words, my rhythm, my sentence length. "
             "Never use these words: delve, leverage, game-changer, in today's fast-paced world. No em-dashes. "
             "Below are my rough thoughts, dictated. Clean them up without adding new ideas: [paste your thoughts].")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. Read it out loud — does "
    "it sound like something you would actually say? And did you do your own final pass, in your own words?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Make AI Write Like You", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: read it out loud — would you actually say that?", "Check: do your own final pass, in your own words."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · WRITING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not AI experts; every term explained, show-don't-tell",
    "source_doc": "Original script — no external source (2026-10-03)",
    "playlist": "How to AI", "chapter_number": 14,
    "tags": ["AI writing", "prompting", "voice", "writing style", "Claude", "Nik Bear Brown"]},
    "beats": B}

# ── assertions: the sheet is what the film needs ──────────────────────────
BODY = [b for b in sheet["beats"] if b["lane"] == "manim"]
BOOKENDS = [b for b in sheet["beats"] if b["lane"] == "bookend"]
assert len(sheet["beats"]) == 11, f"want 11 beats, got {len(sheet['beats'])}"
assert len(BODY) == 7, f"want 7 body beats, got {len(BODY)}"
assert len(BOOKENDS) == 4, f"want 4 bookends, got {len(BOOKENDS)}"
assert [b["beat_id"] for b in sheet["beats"]] == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "B06", "BHTF", "BOUT"]
assert all(b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_") for b in BODY), "class names must start with the beat id"
assert all(b.get("qc", {}).get("sparse_by_design") for b in BODY), "every body beat carries the sparse waiver"
assert all(b["voice"] == "am_onyx" and b["engine"] == "kokoro" for b in sheet["beats"]), "voice lock"
total = sum(b["estimated_duration_s"] for b in sheet["beats"])
assert 180 <= total <= 360, f"total {total}s outside the 3–6 min brief"
idea = sheet["beats"][0]
assert idea["shot"]["remotion"]["props"]["triggerWords"] in idea["shot"]["remotion"]["props"]["text"], "trigger must appear verbatim in text"
assert idea["shot"]["remotion"]["props"]["triggerWords"][-1].isalnum(), "trigger must not end in punctuation"
assert idea["shot"]["remotion"]["props"]["replacementWords"][-1].isalnum(), "replacement must not end in punctuation"
defs = sheet["beats"][1]
assert all(len(t["term"]) <= 17 for t in defs["shot"]["remotion"]["props"]["terms"]), "ClaudeDefinitions truncates terms over ~17 chars"
assert sheet["beats"][-1]["tail_silence_s"] == 1.0, "BOUT needs the 1.0 s tail"
assert sheet["metadata"]["bookend_exempt"] == ["cold-open", "bvdt"]
for b in sheet["beats"]:
    assert b["narration_text"].strip(), f"{b['beat_id']} has empty narration"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(sheet["beats"]), "beats;", len(BODY), "body;", "est", round(total), "s")
