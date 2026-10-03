# Storyboard — Same Number, Two Ways

_Fellow: Asavari (Ash) Shejwal · Mycroft — SEC Filings Financial Metrics Agent · 2026-08-14 · 16:9 + 9:16_

Brutalist explainer, framework-first (PROOF standard). One visual per beat; automated narration.

## Beat 1 — TRUSTWORTHY DATA · AI ACCOUNTABILITY

**On screen:** SEC Filings Financial Metrics Agent

**Narration:** Can you trust a number an AI hands you? It's a simple question, and the honest answer is more uncomfortable than most people expect. Because a number can look completely normal — correctly formatted, in a believable range, the kind of figure you would paste into a report without a second thought — and still be wrong. The checks we usually rely on will not catch it, because they only test whether the number is well formed, not whether it is true. In the next few minutes, I want to show you the one kind of check that does catch it, using a real bug from my own tool.

## Beat 2 — THE PROBLEM

**On screen:** A plausible number is the dangerous kind.

**Narration:** Let me show you exactly what I mean. This is a real revenue figure my tool first produced for Microsoft: fiscal year twenty twenty-five revenue, two hundred eleven point nine billion dollars. It passed every structural check I had. It is correctly formatted. It sits in a completely believable range for a company like Microsoft. If you saw it in a spreadsheet, nothing about it would make you pause. And yet it is wrong — off by two full years. The reason nothing flagged it is subtle but important. None of my checks had anything to compare it against. They could confirm the number was well formed. They could not confirm it was the right number.

## Beat 3 — THE MECHANISM

**On screen:** Rules catch the impossible. A cross-check catches the plausible.

**Narration:** So how do you catch a wrong number that looks right? The tool I built trusts nothing by default, and it checks in two different ways, because there are two different kinds of wrong. The first kind is the impossible: a profit margin over one hundred percent, a balance sheet where assets do not equal liabilities plus equity. Deterministic rules catch those instantly, every single time, because they violate arithmetic. But the second kind is the plausible but wrong: a number that breaks no rule and still is not true. Rules cannot catch that, because it is internally consistent. The only thing that catches it is a comparison against a figure you did not derive from the same data. And underneath both, every value keeps a link back to the exact filing it came from, so any claim can be traced and checked by hand.

## Beat 4 — WE TESTED IT

**On screen:** Same number, two ways.

**Narration:** Here is the moment it actually mattered, side by side. On the left, the first approach: group the data by the filing's own fiscal-year field. That gives two hundred eleven point nine billion for twenty twenty-five, and it passes. It is self-consistent, so it looks fine. On the right, the second approach: cross-check that same number against Microsoft's actually reported revenue, two hundred eighty-one point seven billion. Now the mismatch is obvious. The self-consistent version sailed through, because it was only ever compared against itself. Only the independent check, the one that used a source I did not derive from the same data, caught the error. And notice the receipt along the bottom. The correct figure carries its exact tag, its filing accession number, and a link to the document. That is what makes it verifiable, rather than just asserted.

## Beat 5 — THE LIMIT

**On screen:** No rule replaces a known-good reference.

**Narration:** Now, the honest limit, because a method you cannot break is just a slogan. A number can be correctly tagged, perfectly well formed, and still land on the wrong period. No amount of rules will fix that case. And here is the key reason why. The rules are computed from the same data, so they share the data's blind spot. They cannot see the error, because the error is baked into the very thing they are checking. The cross-check is the one test that does not share that blind spot, because it comes from outside the data. That is exactly why it is not optional.

## Beat 6 — THE TAKEAWAY

**On screen:** Trust the check you didn't derive from the data.

**Narration:** So here is what to take with you. The next time an AI hands you a number, any number, in any tool, run four quick checks. One: can you trace it back to its source? Two: is there a rule that would catch an impossible value? Three: can the system say, I don't know, when it is not sure, instead of guessing? And four, the one that matters most: did you check it against a source you did not derive from the same data? The first three are good hygiene. The fourth is the one that catches the dangerous errors. Fail it, and you are not verifying anything. You are just trusting a number because it happens to look clean. Thanks for watching.
