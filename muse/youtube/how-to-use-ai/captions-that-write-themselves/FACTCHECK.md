# FACTCHECK.md — Captions That Write Themselves

Every factual claim in the script was checked on 2026-10-05 before
writing. The film quotes exactly two numbers; both are attributed aloud
and captioned on screen (thin-numbers law). No pricing tiers appear
anywhere.

| # | Beat | Claim | Verdict | Source | Fix |
|---|------|-------|---------|--------|-----|
| 1 | BDEFS | Captions = the words being said, written on screen, timed to the sound; subtitles = the same idea, translated into another language | PASS | Standard definitions (captions same-language timed text; subtitles translated) — e.g. techtippr.com captioning guide, CapCut docs | Plain-language paraphrase, no jargon beyond the terms being defined |
| 2 | BDEFS | Auto-captioning = an AI listens to your video and writes the captions for you, line by line | PASS | CapCut auto captions: "uses advanced speech recognition to instantly transcribe your video's spoken content into accurate captions" (capcut.com official); YouTube auto-captions every upload (techtippr.com) | "line by line" is the film's plain phrasing for timed caption clips |
| 3 | B02 | The AI listens to the speech and writes down what it hears, each line timed to when it is said | PASS | Same as row 2: speech recognition transcribes audio into timed captions (capcut.com; typito.com 2026 guide) | Framed as "the AI does the boring part in one pass" — the mechanism, not a product benchmark |
| 4 | B02 | The draft is ready in about the time it takes to watch the video once; by hand would take far longer | PASS (qualitative) | Auto-captions "generate captions in seconds" (capcut.com); manual entry "slower" (typito.com). No time claim is quantified in the film | Deliberately kept comparative, not numeric — the film says "far longer", never a ratio |
| 5 | B03 | Almost everything that edits video on your phone has a captions button built in now | PASS | CapCut (free, phone + desktop) auto captions; Microsoft Clipchamp auto captions; Canva auto captions in free tier; YouTube auto captions (techtippr.com) | Said as "almost everything", with "look for it where the text tools live" as the locating instruction |
| 6 | B04 / B05 | The timing will be close; the words will be nearly right; the AI fumbles names, places, and unusual words | PASS | "Auto Captions commonly misses proper nouns, technical terms, and fast speech" (typito.com); "they mishear names, technical terms, and accented words" (techtippr.com); background music/noise hurts accuracy (caption-x.com) | "Nearly right" is a deliberate hedge; the check step exists because of exactly these sources |
| 7 | B06 | Burned in = part of the video, everyone sees them; a caption file = sits beside the video, viewer can turn them on or off | PASS | "Export burns captions into the video — there is no sidecar SRT" vs "export a separate .srt file" (typito.com) | Plain-language paraphrase; "For short feeds, burn them in. For YouTube, keep the file" is editorial judgment (see below) |
| 8 | B07 | "Nine in ten viewers watch phone video with the sound off" | PASS | 92% of US consumers view videos with the sound off on mobile — Verizon Media / Publicis Media survey (2019), via Next TV | Spoken aloud as "a Verizon survey of mobile viewers" and captioned on screen as "per Verizon survey, 2019". "Nine in ten" is the plain-English rounding of 92% |
| 9 | B07 | "Four hundred thirty million people worldwide with disabling hearing loss", per WHO | PASS | WHO: 430 million have disabling hearing loss; 1.5 billion live with some hearing loss (who.int) | Spoken aloud as "says the World Health Organization" and captioned on screen as "per WHO" |
| 10 | B05 / BHTF | The workflow (generate the draft, read along, fix names, ask the AI to flag unclear lines) | EXEMPT | Prescribed user actions, not factual claims — the viewer runs the steps and judges the result themselves | The film never says "the AI will correctly fix…" |
| 11 | — | Film identity: channel claude-liam; persona "Liam, in for Bear"; Kokoro am_onyx; Teardown register; watermark @NikBearBrown | PASS | Film-builder brief | — |

## Judgments (judgment)

- The four-step walkthrough (open a tool / press the button / check the
  names / choose burned-in or a file) is my structure for the brief's
  "practical walkthrough for a normal person with phone-shot video".
  No named app is recommended — the steps are tool-agnostic on purpose,
  so the film cannot date. [judgment]
- "For short feeds, burn them in. For YouTube, keep the file" is my
  editorial guidance, not a sourced claim: feed platforms reward
  always-on text, while YouTube's player supports toggleable caption
  tracks. It is framed as guidance ("For short feeds…"), not as a
  fact. [judgment]
- "For viewers who cannot hear the audio, captions aren't a convenience
  — they're the only way in" is the film's framing line, not a measured
  claim — the WHO figure grounds the scale, the line states the
  stakes. [judgment]
- The 2019 Verizon figures are the best-attributed recent survey on
  sound-off mobile viewing; they are spoken with attribution and dated
  on screen ("2019") so the viewer knows their age. [judgment]

## Cut or disclosed

- No pricing tiers, no product recommendations, no accuracy percentages
  (the film says "nearly right", never a number).
- No other statistics from the survey are quoted (the 80%/83%/37% side
  figures stay in SOURCES.md as background).
- The BHTF prompt is presented as a starting point the viewer runs and
  judges themselves, not as a certified workflow.
- The demo "Maine street" → "Main street" mishearing is the film's own
  invented example (clearly a demonstration, not a reported event).
