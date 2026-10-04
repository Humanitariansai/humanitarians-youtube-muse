#!/usr/bin/env python3
"""make_sheet.py — Don't get fooled. (Humanitarians AI YouTube film)

Builds beat_sheet.json: 13 beats, ai-explainer spine (composer cold open ->
hesitant-writer BLUF -> three acts -> verdict recap -> your-turn handoff ->
title-restate outro). Skill: ai-explainer. Persona: Liam, in for Bear.
TTS: Kokoro am_onyx. Register: Teardown. Channel: claude-liam.
Watermark: @NikBearBrown.

Source argument (mirror repo nikbearbrown/humanitarians-youtube-muse,
claude/claude-for-education/): the beat_sheet.json in the base folder
`prompt-avoiding-hallucinations` was a mislabeled copy of lesson 07
(few-shot); the true source is its PEDAGOGY.md verdict plus the
claude-liam Lesson-08 sheet (`claude-liam-prompt-tutorial-lesson-08-
avoiding-hallucinations`): hallucination is a structural property of an
ungrounded next-token predictor (confidence and correctness uncorrelated);
the three-part grounding pattern (source in prompt, answer only from it,
"I don't know" permitted); citations as the verifiable audit trail.
Rewritten for a smart, pragmatic general audience: every term explained
in plain language, in the same breath it is first used.

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~150 wpm narration => words/2.5 + small pause, rounded.
"""
import json

BEATS = [
    {
        "id": "B00", "scene": "M01", "dur_s": 21, "act": "hook",
        "voice": "Muse", "greeting": "Olá",
        "line": ("Olá. This is Liam, in for Bear. Quick question: why does "
                 "the AI sound so sure when it's wrong? It's not badly trained. "
                 "It's built that way. For the next few minutes, watch what it's "
                 "actually doing when it answers you — and the three habits "
                 "that keep you safe."),
        "screen": ("Claude-style composer window: spark + 'Olá, Liam' "
                   "serif header; the ask types in on two lines; running "
                   "line; two output lines answer it."),
        "shot": {"type": "MANIM", "manim": {"class": "M01_ColdOpen"},
                 "show": [{"at": "0.05", "event": "composer card fades in; spark + 'Olá, Liam' header"},
                          {"at": "0.25", "event": "the ask types in on two lines"},
                          {"at": "0.55", "event": "running line 'thinking…'"},
                          {"at": "0.75", "event": "two output lines answer the ask"}]}},
    {
        "id": "B01", "scene": "M02", "dur_s": 15, "act": "hook",
        "voice": "Muse", "lead_silence_s": 0.8,
        "line": ("AI lies to you because it's badly trained. No — AI can "
                 "sound completely sure and still be wrong, because it guesses "
                 "the most likely words, not the truth. Three small habits keep "
                 "you safe."),
        "screen": ("Hesitant writer: a hand writes 'AI lies because it's "
                   "badly trained.', strikes through 'badly trained', and "
                   "corrects it to a two-line claim: 'AI guesses the most "
                   "likely words, / not the truth.'"),
        "shot": {"type": "MANIM", "manim": {"class": "M02_Bluf"},
                 "show": [{"at": "0.05", "event": "paper card fades in; hand cursor writes the naive line"},
                          {"at": "0.40", "event": "terracotta strike-through crosses 'badly trained'"},
                          {"at": "0.65", "event": "the corrected two-line claim writes in"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer bookend beat: one card, one correction"}}},
    {
        "id": "B02", "scene": "M03", "dur_s": 27, "act": "1",
        "voice": "Muse",
        "line": ("Here's what's actually happening. An AI like Claude doesn't "
                 "look up the answer. It predicts the most likely next word, "
                 "then the next, then the next — building a sentence out "
                 "of probability. Most of the time the most likely word is also "
                 "the right word. But not always. And when it isn't, the "
                 "sentence still sounds perfect — because perfect-sounding "
                 "was the whole target."),
        "screen": ("The two-line sentence stem 'The capital of France / is "
                   "_______.' waits; three candidate next-words with "
                   "probability bars: Paris (tall, terracotta), Lyon, Nice "
                   "(short, ghost). Paris drops into the blank."),
        "shot": {"type": "MANIM", "manim": {"class": "M03_Mechanism"},
                 "show": [{"at": "0.05", "event": "two-line sentence stem card pins; the blank pulses"},
                          {"at": "0.25", "event": "three candidate words land with probability bars"},
                          {"at": "0.60", "event": "tallest bar rings; 'Paris' drops into the blank"},
                          {"at": "0.85", "event": "caption lands: 'most likely ≠ always right'"}]}},
    {
        "id": "B03", "scene": "M04", "dur_s": 27, "act": "1",
        "voice": "Muse",
        "line": ("So here's habit zero — the one that underlies all three: "
                 "the confident tone tells you nothing. Listen. 'The treaty was "
                 "signed in 1847.' Sure, firm, no hesitation. It could be a "
                 "fact. It could be invented — and you would never hear "
                 "the difference. A confident wrong answer looks and sounds "
                 "exactly like a confident right one. Treat confidence as "
                 "decoration, never as proof."),
        "screen": ("Two identical answer cards, same confident header "
                   "'Definitely.', same short quote '“Signed in 1847.”'. One "
                   "gets a terracotta X stamped: 'made up'. The other gets an "
                   "ink check: 'true'. A rule lands: 'confident ≠ proof'."),
        "shot": {"type": "MANIM", "manim": {"class": "M04_ConfidentTone"},
                 "show": [{"at": "0.05", "event": "two identical answer cards land side by side"},
                          {"at": "0.45", "event": "terracotta X stamps the left card: 'made up'"},
                          {"at": "0.65", "event": "ink check lands on the right card: 'true'"},
                          {"at": "0.85", "event": "rule plate drops: 'confident ≠ proof'"}]}},
    {
        "id": "B04", "scene": "M05", "dur_s": 28, "act": "1",
        "voice": "Muse",
        "line": ("This is not a thought experiment. In 2023, a lawyer in New "
                 "York asked an AI chatbot to find court cases for his filing. "
                 "It gave him six cases — names, judges, quotes, all "
                 "beautifully formatted. He filed them. None of them existed. "
                 "The cases were invented, word by perfectly confident word. "
                 "The judge fined him and his firm five thousand dollars. "
                 "Nobody checked, because nobody doubted."),
        "screen": ("A legal brief card with three citation rows (the real "
                   "'Varghese v. China Southern Airlines, 925 F.3d 1339 (11th "
                   "Cir. 2019)' plus two rows labeled 'invented'); each gets a "
                   "terracotta stamp 'NOT A REAL CASE'. A fine plate drops: "
                   "'$5,000 fine'."),
        "shot": {"type": "MANIM", "manim": {"class": "M05_LawyerStory"},
                 "show": [{"at": "0.05", "event": "legal brief card fades in with three citation rows"},
                          {"at": "0.35", "event": "terracotta stamps land on each citation: 'NOT A REAL CASE'"},
                          {"at": "0.65", "event": "a '$5,000 fine' plate drops in"},
                          {"at": "0.85", "event": "caption: 'nobody checked, because nobody doubted'"}]}},
    {
        "id": "B05", "scene": "M06", "dur_s": 27, "act": "2",
        "voice": "Muse",
        "line": ("Now the fix. The strongest thing you can do is called "
                 "grounding, and it's three short sentences. First: paste the "
                 "source into the chat — the article, the document, the "
                 "contract. Second: tell the AI to answer only from that text. "
                 "That's it: you stop asking it to reach into its memory, and "
                 "start asking it to read. A reader can be checked. A memory "
                 "cannot."),
        "screen": ("A source document slides into a chat window; the two-line "
                   "instruction 'Answer only / from this text.' types in; the "
                   "answer card emerges pinned to the document by a terracotta "
                   "tether."),
        "shot": {"type": "MANIM", "manim": {"class": "M06_Grounding"},
                 "show": [{"at": "0.05", "event": "source document card slides into the chat frame"},
                          {"at": "0.35", "event": "'Answer only / from this text.' types in"},
                          {"at": "0.65", "event": "answer card emerges, tethered to the document"},
                          {"at": "0.85", "event": "'a reader can be checked' tag lands"}]}},
    {
        "id": "B06", "scene": "M07", "dur_s": 27, "act": "2",
        "voice": "Muse",
        "line": ("Third sentence — the one people skip: if the answer "
                 "isn't in the text, say you don't know. This matters because "
                 "the AI fills gaps rather than admitting them. Without that "
                 "permission, it fills the silence with its best guess, "
                 "delivered in full confidence. With it, you've given it a way "
                 "out — and the guessing mostly stops."),
        "screen": ("A question card asks what the document can't answer; a gap "
                   "opens between question and document; the AI card answers on "
                   "two lines: 'I don't know — / it's not in the text.' A "
                   "terracotta ellipse rings 'I don't know'."),
        "shot": {"type": "MANIM", "manim": {"class": "M07_IDontKnow"},
                 "show": [{"at": "0.05", "event": "question card lands; document can't cover it"},
                          {"at": "0.35", "event": "a gap opens between the question and the document"},
                          {"at": "0.60", "event": "'I don't know — / it's not in the text.' writes in"},
                          {"at": "0.85", "event": "terracotta ellipse rings 'I don't know'"}]}},
    {
        "id": "B07", "scene": "M08", "dur_s": 27, "act": "3",
        "voice": "Muse",
        "line": ("Habit two: ask where it got that from. Tell the AI to quote "
                 "the exact sentence it's drawing on — then search that "
                 "sentence in your document. If you find it word for word, the "
                 "answer is anchored. If you can't find it, congratulations: "
                 "you just caught a hallucinated citation. A fake quote is "
                 "still a fake — but now it's one you can see."),
        "screen": ("An answer card quotes 'The meeting is on Tuesday.'; a "
                   "magnifier carries the quote to the sample document; the "
                   "word-for-word match ticks. A second quote, 'The meeting is "
                   "on Friday.', fails the search — terracotta X: 'hallucinated "
                   "citation'."),
        "shot": {"type": "MANIM", "manim": {"class": "M08_CitationAudit"},
                 "show": [{"at": "0.05", "event": "answer card with quoted passage lands"},
                          {"at": "0.30", "event": "magnifier carries the quote to the source doc"},
                          {"at": "0.55", "event": "word-for-word match ticks; ink check lands"},
                          {"at": "0.80", "event": "a second quote fails; terracotta X: 'hallucinated citation'"}]}},
    {
        "id": "B08", "scene": "M09", "dur_s": 26, "act": "3",
        "voice": "Muse",
        "line": ("Habit three: cross-check anything that matters. Money, "
                 "health, anything you'd put your name on — verify it "
                 "somewhere the AI can't reach. A second source, the original "
                 "document, a real person who knows. The AI is a brilliant "
                 "first draft. It is not a witness. And remember habit zero: "
                 "if it sounds sure, that's the machine being fluent — "
                 "not being right."),
        "screen": ("One claim card in the center; two independent source cards "
                   "land on either side; checks land on each; a badge drops: "
                   "'confident tone ≠ proof'."),
        "shot": {"type": "MANIM", "manim": {"class": "M09_CrossCheck"},
                 "show": [{"at": "0.05", "event": "the claim card pins center"},
                          {"at": "0.30", "event": "two source cards land left and right"},
                          {"at": "0.60", "event": "checks land on each source"},
                          {"at": "0.85", "event": "'confident tone ≠ proof' badge drops"}]}},
    {
        "id": "B09", "scene": "M10", "dur_s": 25, "act": "3",
        "voice": "Muse",
        "line": ("So here's the card to keep. One: paste the source; answer "
                 "only from this text. Two: if the answer isn't in the text, "
                 "say you don't know. Three: quote the exact sentence, and "
                 "check it. Three sentences in your prompt, three habits in "
                 "your head — and the machine goes from a confident "
                 "storyteller to something you can actually trust."),
        "screen": ("Three numbered two-line sentence cards stack: the "
                   "grounding instruction, the 'I don't know' permission, the "
                   "quote-and-check rule — the third with a terracotta edge. "
                   "Checks land on each."),
        "shot": {"type": "MANIM", "manim": {"class": "M10_ThreeSentences"},
                 "show": [{"at": "0.10", "event": "sentence card 1 lands: paste the source"},
                          {"at": "0.40", "event": "sentence card 2 lands: say you don't know"},
                          {"at": "0.70", "event": "sentence card 3 lands with terracotta edge: quote and check"}]}},
    {
        "id": "BVDT", "scene": "M11", "dur_s": 23, "act": "recap",
        "voice": "Muse",
        "line": ("Don't get fooled — the recap. The AI predicts the most "
                 "likely words, so a confident answer can be pure invention. "
                 "The fix is grounding: paste the source, answer only from it, "
                 "and let it say 'I don't know.' Then audit: make it quote the "
                 "passage, check the quote, and cross-check anything that "
                 "matters."),
        "screen": ("Three recap lines reveal with dot bullets: 'It guesses "
                   "words, not truth.' / 'Ground it: give it the source; "
                   "answer only from that.' / 'Audit it: quote the passage; "
                   "check it; cross-check it.'"),
        "shot": {"type": "MANIM", "manim": {"class": "M11_Recap"},
                 "show": [{"at": "0.10", "event": "recap line 1 reveals: the mechanism"},
                          {"at": "0.40", "event": "recap line 2 reveals: the fix (two lines)"},
                          {"at": "0.70", "event": "recap line 3 reveals: the audit (two lines)"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer verdict beat: three lines on cream"}}},
    {
        "id": "BHTF", "scene": "M12", "dur_s": 29, "act": "do_today",
        "voice": "Muse",
        "line": ("Your turn. Open Claude and paste in any article — a "
                 "Wikipedia page works. Then paste this in: 'Answer only from "
                 "the text above. If the answer isn't in the text, say you "
                 "don't know. Quote the exact sentence you draw from.' Ask it "
                 "something the article covers. Then ask it something the "
                 "article doesn't. The second answer is the whole lesson — "
                 "enjoy hearing an AI say it doesn't know."),
        "screen": ("Composer card: 'Your turn.' header; the three-sentence "
                   "prompt types in (sentence two wraps to two lines), each "
                   "with a terracotta underline; a 'paste into Claude' tag "
                   "lands."),
        "shot": {"type": "MANIM", "manim": {"class": "M12_YourTurn"},
                 "show": [{"at": "0.10", "event": "composer card fades in; 'Your turn.' header"},
                          {"at": "0.30", "event": "prompt sentence 1 types in with underline"},
                          {"at": "0.55", "event": "prompt sentence 2 types in, wrapping to two lines"},
                          {"at": "0.75", "event": "prompt sentence 3 types in; 'paste into Claude' tag lands"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer handoff beat: prompt card on cream"}}},
    {
        "id": "BOUT", "scene": "M13", "dur_s": 9, "act": "outro",
        "voice": "Muse",
        "line": ("Don't get fooled. Liam, in for Bear. At Nik Bear Brown. "
                 "Thanks for watching."),
        "screen": ("Title card: 'Don't get fooled' writes in serif; a "
                   "terracotta rule draws under it; terracotta period; "
                   "@NikBearBrown handle fades in."),
        "shot": {"type": "MANIM", "manim": {"class": "M13_Outro"},
                 "show": [{"at": "0.10", "event": "title writes in, serif"},
                          {"at": "0.55", "event": "terracotta rule draws under the title"},
                          {"at": "0.80", "event": "terracotta period drops; handle fades in"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer outro beat: title card"}}},
]

METADATA = {
    "title": "Don't get fooled.",
    "slug": "dont-get-fooled",
    "series": "Humanitarians AI — how to use AI",
    "skill": "ai-explainer",
    "style_preset": "ai-explainer",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": "Olá",
    "palette": {"stage": "#F2F0E9", "ink": "#3D3929", "accent": "#D97757",
                "dim": "#8B8F96", "ghost": "#D9D4C7", "card": "#FAF9F5"},
    "playlist": "how-to-use-ai",
    "tags": ["ai-explainer", "hallucinations", "grounding", "citations",
             "prompting", "general-audience"],
    "derived_from": ("nikbearbrown/humanitarians-youtube-muse:"
                     "claude/claude-for-education/ [base folder "
                     "prompt-avoiding-hallucinations beat_sheet.json is a "
                     "mislabeled copy of lesson 07; true source: PEDAGOGY.md "
                     "verdict + claude-liam-prompt-tutorial-lesson-08-"
                     "avoiding-hallucinations/beat_sheet.json]"),
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
}

if __name__ == "__main__":
    ids = [b["id"] for b in BEATS]
    assert len(BEATS) == 13, len(BEATS)
    assert 13 <= len(BEATS) <= 22, "beat count outside 13-22 band"
    assert ids[0] == "B00" and ids[1] == "B01", ids[:2]
    assert ids[-3:] == ["BVDT", "BHTF", "BOUT"], ids[-3:]
    body = [b for b in BEATS if b["act"] in ("1", "2", "3")]
    assert len(body) == 8, len(body)
    for b in body:
        n = len(b["line"].split())
        assert 45 <= n <= 70, f"{b['id']} body beat {n} words outside 45-70"
    idea = BEATS[0]["line"]
    assert "Liam, in for Bear" in idea, "IN-FOR-BEAR LAW: name the voice"
    bluf = BEATS[1]["line"].split()
    assert 20 <= len(bluf) <= 35, f"B01 BLUF {len(bluf)} words outside 20-35"
    assert BEATS[1].get("lead_silence_s") == 0.8, "B01 needs lead_silence_s 0.8"
    htf = next(b for b in BEATS if b["id"] == "BHTF")["line"]
    assert "Your turn" in htf, "handoff greeting"
    assert "Answer only from" in htf, "handoff must read the prompt aloud"
    recap = next(b for b in BEATS if b["id"] == "BVDT")["line"].lower()
    for kw in ["predicts", "confident", "grounding", "i don't know", "quote",
               "cross-check"]:
        assert kw in recap, f"recap missing {kw!r}"
    total = sum(b["dur_s"] for b in BEATS)
    assert 180 <= total <= 360, f"total {total}s outside 3-6 min band"
    BS = {"metadata": METADATA, "beats": BEATS}
    print(f"beats={len(BEATS)} body={len(body)} "
          f"total={total//60}m{total%60:02d}s")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
