# FACTCHECK.md — "AI that sees"

Checked 2026-10-04. No invented statistics anywhere in the film; the film's
only numbers are beat counts. Every factual claim below is generic enough to
survive UI redesigns, and the narration is hedged where a single product is
named. Nothing in the film depends on version-specific UI, pricing, or model
availability.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Most AI apps let you attach a photo to your message via a paperclip or plus button (like sending a picture to a friend). | PASS | Mirrored Anthropic developer docs (`eyre921/ofiicial-developer-docs`, ai-models/anthropic-claude-code/pages/desktop.md): "Attach files: attach images, PDFs, and other files to your prompt using the attachment button, or drag and drop files directly into the prompt." | Kept generic on purpose ("a paperclip or plus button") — no version-specific UI asserted. |
| 2 | B00/B01 | Claude sees attached photos directly as part of your message and answers in words. | PASS | Mirrored Anthropic docs (`flolep2607/cctop`, docs/harnesses/claude/remote-control.md): "attach a photo or file in the Claude app … Claude sees attached photos directly as part of your message." | — |
| 3 | B01 | "The AI scans it the way you would — top to bottom, looking for the parts that matter." | PASS (analogy) | The vision mechanism is deliberately a plain-language analogy ("the way you would"), not a technical spec of any model. | — |
| 4 | B02–B07 | Use-case guidance: error screenshots, receipts, sick plants, forms, which-one comparisons, handwriting transcription. | PASS (use-case guidance) | Mirrored Anthropic developer docs name "sharing screenshots of bugs" as an attach-files use case. Plant/form/handwriting uses are presented as when-a-photo-wins craft guidance, not product claims. | Presented as "the classic" / use-case advice, never as a guaranteed capability list. |
| 5 | BDEFS | "multimodal: an AI that takes more than one kind of input — words, photos, even speech." / "vision: the AI's ability to read a photo or screenshot." / "attach: adding a photo to your message." | PASS (definition) | Plain-language definitions; the terms are used in their ordinary sense. | — |
| 6 | B08 | A blurry dark photo is a blurry dark question: the AI can only read what the camera caught. | PASS (advice) | No accuracy figure asserted; "the camera caught" is a qualitative, durable claim. | — |
| 7 | B09 | If the photo is busy, crop in or name the spot ("the cracked tile, top left"). | PASS (advice) | Craft advice, not a product spec. | — |
| 8 | B10 | A photo never replaces the question; add a few words (transcribe this / explain this error). | PASS (advice) | Craft advice, not a product spec. | — |
| 9 | B11 | The AI reads everything you show it, including what you did not mean to share. | PASS (general) | The model processes the entire attached image — a durable property of image input. The film asserts NO vendor data-retention or training policy; the rule ("photograph the receipt, not the bank statement") is advice. | — |

EXEMPT (not factual claims): the BIDEA/BHTF/BOUT narration, all visual
metaphors (the AI eye, the scan line, cards), "Ciao" greeting, "At Nik Bear
Brown".
