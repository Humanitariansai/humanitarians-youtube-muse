# Storyboard — One Number, Many Names

_Fellow: Asavari (Ash) Shejwal · Mycroft — SEC Filings Financial Metrics Agent · 2026-08-14 · 16:9 + 9:16_

Brutalist explainer, framework-first (PROOF standard). One visual per beat; automated narration.

## Beat 1 — TRUSTWORTHY DATA · SEC FILINGS

**On screen:** One Number, Many Names

**Narration:** Here's a problem that sounds trivial and isn't. Two companies report the same thing, their revenue, and they label it completely differently. One calls it Net Sales. Another calls it Revenue from Contracts with Customers. Some invent their own custom tag. A human sees they mean the same thing in a second. Software cannot assume that. Deciding when two differently-named numbers are actually the same, and proving it, is the real work.

## Beat 2 — THE PROBLEM

**On screen:** The same concept, three different labels.

**Narration:** In practice it looks like this. Three filings, three different labels, all pointing at the same idea. If your tool treats them as different, your comparison across companies is broken before it starts. If it treats them as the same without checking, it might merge two things that only look alike. Either mistake is silent.

## Beat 3 — THE MECHANISM

**On screen:** Try known tags in order — and record which one matched.

**Narration:** The fix is deliberate, not clever. For each metric, the tool keeps an ordered list of the tags a company might use, most preferred first, the modern standard tag before the older ones. It takes the first one the company actually reports, and it records which tag it matched, on every single value. So the mapping decision is visible. Anyone can see this company's revenue came from that tag, and disagree if they want to. And when nothing matches, it does not guess. It flags the metric as missing, so a human can map it.

## Beat 4 — THE LIMIT

**On screen:** A custom tag isn't a wrong tag.

**Narration:** One honest nuance. When a company uses its own custom tag, that is not an error. It is often the most accurate label for something unusual in their business. So missing does not mean the data is bad. It means the tool needs a human to confirm the mapping before it trusts it. That distinction, between I can't map this yet and this is wrong, is what keeps the dataset honest.

## Beat 5 — THE TAKEAWAY

**On screen:** Comparability is a decision you have to prove.

**Narration:** So the takeaway, whether or not you ever touch a filing. Any time you merge data from different sources, comparability is not given. It is a decision, and you should be able to prove it. Do the labels truly mean the same thing? Which exact source did each value come from? Could someone audit that mapping months later? And what did you deliberately refuse to merge, because you weren't sure? Numbers are never just numbers. The names matter.
