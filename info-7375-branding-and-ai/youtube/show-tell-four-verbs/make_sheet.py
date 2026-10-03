#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-four-verbs.

SHOW-TELL, a COURSE film for INFO 7375 Branding and AI. Bear, 2026-09-27: "Make sure you're using the
updates to the show tell skill to use everything you can do now. A film on this aspect of the Four
Verbs" + chapter 1's "The Four Verbs" section (SOURCE.md). So: no length cap (as long as it needs),
and cards ONLY where they pass the card test:

  B05 `search`  — the idea IS an interface (a stranger searching); results arriving IS "can they find
                  you"; a drawing can't show search better.
  B07 `focus`   — the idea IS a table (the scoring rubric); the lens stepping row by row IS scoring
                  yourself verb by verb.
  B08 `tabs`    — the idea IS compare-A-then-B (two firms, similar tech, two positions); the tab switch
                  IS the comparison. Rows are verified wording only.

Everything else is drawn. Cast: four kraft SLABS (the verbs), the BOX (a project), the dark BLOCK (tech /
an API), the white PAGE (a spec, documentation), a SHELF with a gap; terracotta = the move that matters.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Ideate, Build, Brand, Ship"
COURSE = "INFO 7375 Branding and AI · Nik Bear Brown · Northeastern University"

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image},
            "qc": {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", lane="bookend", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.8, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


def card(bid, narration, props, claim, why):
    return remotion(bid, "show-tell", narration, "ShowTellCard", props,
                    [{"at": 0.0, "event": f"{props['kind']} card, shot on twos"}], lane="card", motion_claim=claim, why_card=why)


B = [
 beat("B00", "A creative engineer is an engineer who noticed the costly signals shifted, and invested accordingly. The work comes down to four verbs. Ideate. Build. Brand. Ship.",
      "B00_FourVerbs", "Four kraft slabs land one by one as each verb is spoken, labelled Ideate, Build, Brand, Ship; a small box lands on the first.",
      [{"at": 0.5, "event": "Ideate"}, {"at": 0.65, "event": "Build"}, {"at": 0.8, "event": "Brand"}, {"at": 0.92, "event": "Ship"}]),
 beat("B01", "Ideate is the hardest move, and the one AI can't do for you yet. Hand the tools a specification and they'll build it. "
             "They can't tell you whether it's worth building. That takes talking to real people, and finding a real gap.",
      "B01_Gap", "A white spec page slides into a dark block and a box pops straight out ('spec'); then a shelf of boxes, a dot scans along it and stops at the one empty slot, where a dashed outline appears ('the gap').",
      [{"at": 0.2, "event": "spec in, box out"}, {"at": 0.6, "event": "the shelf"}, {"at": 0.85, "event": "the gap"}]),
 beat("B02", "The mistake I see most: pick a technology you want to learn, build a project around it, then try to glue a user need on afterward. "
             "You get a competent thing nobody wanted. It shows Build. It doesn't show Ideate.",
      "B02_TechFirst", "A dark block ('tech first') drops; a box builds on top of it; a white tag is stuck on crooked and slides off.",
      [{"at": 0.15, "event": "tech first"}, {"at": 0.4, "event": "build around it"}, {"at": 0.65, "event": "tag glued on, falls off"}]),
 beat("B03", "Build is the verb AI cheapened. Real production systems still need deep technical judgment. "
             "But a repo on GitHub no longer sets you apart. Build is necessary. It isn't sufficient.",
      "B03_Necessary", "A box on a plinth ('necessary'); identical boxes appear on plinths either side until it no longer stands out ('not sufficient').",
      [{"at": 0.2, "event": "the box"}, {"at": 0.55, "event": "copies appear"}, {"at": 0.85, "event": "not sufficient"}]),
 beat("B04", "Brand is where engineers push back hardest. So think of an API with no documentation. It computes. It returns the right values. "
             "But the developer who needs it can't tell what it's for, so it's useless. Documentation isn't decoration. "
             "It's what connects the API to the people who need it. Brand is documentation for your career.",
      "B04_Docs", "A dark API block on the right; a cable from a second block on the left reaches toward it and stops short; a white doc page attaches to the API, the cable connects, and lights come on ('API', 'docs').",
      [{"at": 0.15, "event": "API"}, {"at": 0.4, "event": "cable stops short"}, {"at": 0.7, "event": "docs attach, cable connects"}]),
 card("B05", "In practice, Brand is a handful of choices: who it's for, how it's positioned, the voice, the look. Together they decide whether a stranger who needs your work can find it, and see it's for them. "
             "Your work can't speak for itself if the person it's for never finds it.",
      {"kind": "search", "heading": "accessible charts for nonprofits",
       "items": [{"label": "Accessible Charts for Nonprofits", "sub": "who it's for, a demo, a clear README"},
                 {"label": "chart-utils-v2", "sub": "no description"},
                 {"label": "dataviz-final", "sub": "no description"}], "focus": 0},
      "A stranger types what they need; three results drop in; only the one that says who it's for gets picked.",
      "Search IS the idea (a stranger finding your work); results arriving IS the claim; a drawing can't show search better."),
 beat("B06", "Ship means a public link, people who found it, and feedback from real use. Not a commit. Not a class demo. "
             "Shipping teaches you the most, because every guess you made gets tested the moment real users touch it.",
      "B06_Ship", "The box rides out through an open gate ('public'); three curved feedback lines draw back from the right with dots travelling along them; the box's tape turns on ('feedback').",
      [{"at": 0.2, "event": "out the gate"}, {"at": 0.6, "event": "feedback comes back"}, {"at": 0.85, "event": "the box changes"}]),
 card("B07", "So score yourself honestly on each verb, one to five, where five means public evidence a stranger could see. "
             "For Ideate, that's user research. For Build, a deployed project. For Brand, a clear audience. For Ship, real users.",
      {"kind": "focus", "heading": "What a 5 looks like", "focus": 3,
       "items": [{"label": "Ideate", "value": "user research"}, {"label": "Build", "value": "deployed"},
                 {"label": "Brand", "value": "clear audience"}, {"label": "Ship", "value": "real users"}]},
      "A lens steps down the rubric verb by verb as each is spoken.",
      "The rubric IS a table; the lens stepping row by row IS scoring yourself verb by verb."),
 card("B08", "It works at company scale too. Anthropic was founded in 2021 by former OpenAI researchers, and put a published safety method, Constitutional AI, at its front door. "
             "OpenAI does similar technical work, but leads with capability, and a mission of AGI that benefits all of humanity. Similar tech. Two brands. Two audiences.",
      {"kind": "tabs", "labels": ["Anthropic", "OpenAI"],
       "items": [{"label": "Constitutional AI", "value": "2022"}, {"label": "Helpful, honest, harmless", "value": ""},
                 {"label": "Safety at the front door", "value": ""}],
       "items2": [{"label": "Capability launches", "value": ""}, {"label": "AGI for all of humanity", "value": ""},
                  {"label": "Frontier first", "value": ""}]},
      "Two tabs: Anthropic's panel, then the pill slides and OpenAI's panel replaces it.",
      "The idea IS compare A then B; the tab switch IS the comparison. Rows are verified wording only."),
 beat("B09", "And it works for one person. A clear audience, a clear position, and the work to prove it decide who can find you, want you, and hire you. Not a company. A career.",
      "B09_Career", "The four slabs again, Build ghosted; the box hops across all four and gets the terracotta tape on Ship ('a career').",
      [{"at": 0.2, "event": "the slabs"}, {"at": 0.5, "event": "the box hops across"}, {"at": 0.85, "event": "a career"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Dumela. This is Liam, in for Bear, with a short film for INFO seventy-three seventy-five, Branding and AI. "
    "Engineers tend to ask how to build it better. Now that building is cheap, the question is what else you have to show.",
    "BrutalistHesitantWriter",
    {"text": "How do I get better\nat building?", "triggerWords": "better at building", "replacementWords": "seen for what I build",
     "fontSize": 72, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get better at building?'"}, {"at": 0.6, "event": "'better at building' → 'seen for what I build'"}],
    lead_silence_s=0.8, motion_claim="The writer types the build-only question and corrects it: be seen for what you build.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. A costly signal: something that's hard to fake cheaply, so it tells people apart. "
    "Brand: the choices that decide whether the right stranger can find your work and see it's for them. "
    "And ship: put it in front of real users, at a public link.",
    "ClaudeDefinitions",
    {"title": "INFO 7375 · Terms In This Film",
     "terms": [{"term": "costly signal", "meaning": "hard to fake cheaply, so it tells people apart"},
               {"term": "brand", "meaning": "choices that let the right stranger find your work"},
               {"term": "ship", "meaning": "real users, at a public link"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'costly signal'"}, {"at": 0.4, "event": "'brand'"}, {"at": 0.75, "event": "'ship'"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here are my three best projects: [list them, with links]. Score me from one to five on each of four verbs: "
             "Ideate, Build, Brand, Ship. A five means a public artifact a stranger could see. For each score, name the evidence you used, "
             "then tell me the one change that would raise my lowest verb.")
SPOKEN_PROMPT = YT_PROMPT.replace("[list them, with links]", "list them, with links")
CHECKS = ["Check: is every score backed by something public?",
          "Check: is your lowest verb the one you avoid?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. Is every score backed by something a stranger "
    "could actually find? And is your lowest verb the one you've been avoiding?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "INFO 7375 BRANDING AND AI · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])



def cue(narr, phrase, lead=0.03):
    """Fraction of the beat where `phrase` is spoken (the same share rule as until()), kept out of GATE T's 45-55% window."""
    f = max(0.02, narr.index(phrase) / len(narr) - lead)
    if 0.45 <= f <= 0.55:
        f = 0.44 if f < 0.5 else 0.56
    return round(f, 3)


for b in B:
    n = b["narration_text"]
    if b["beat_id"] == "B07":
        b["shot"]["remotion"]["props"]["cues"] = [cue(n, "For Build"), cue(n, "For Brand"), cue(n, "For Ship")]
    if b["beat_id"] == "B08":
        # the tab switch + panel swap lasts ~0.3 of the beat, so it must START after GATE T's 50% frame
        b["shot"]["remotion"]["props"]["cues"] = [max(0.56, cue(n, "OpenAI does"))]

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
    "caption_policy": "none", "greeting_language": "Setswana (Dumela) — confirmed unused 2026-09-27",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "course": COURSE,
    "audience": "INFO 7375 Branding and AI students (Fall 2026), mostly engineers",
    "bookloop_policy": "Course film: carries the INFO 7375 credit, spoken in BIDEA and on screen in the BDEFS title and the BHTF composer topic; not a numbered lecture. Outro stays OUTRO-LOCK.",
    "source_doc": "info-7375-branding-and-ai/chapters/01-the-creative-engineer.md, 'The Four Verbs' (pasted by Bear 2026-09-27); arXiv 2212.08073; arXiv 2112.00861; Wikipedia (Anthropic, OpenAI)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["creative engineer", "four verbs", "ideate", "brand", "ship", "portfolio", "careers", "Anthropic", "Constitutional AI", "INFO 7375", "Claude", "Nik Bear Brown"]},
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
    if rem and b.get("actual_duration_s") and rem["pattern"] in ("ClaudeDefinitions", "BrutalistHesitantWriter", "ShowTellCard"):
        rem["props"]["durationSeconds"] = round(float(b["actual_duration_s"]), 3)
old.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b["estimated_duration_s"] for b in B)), "s")
