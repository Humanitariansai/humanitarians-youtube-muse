# FACTCHECK.md — AI is a slot machine.

Every claim in the script was checked before writing. Unverifiable claims
were cut; hedges ("never quite", "often", "seems") are kept where the
source is a metaphor or one person's observation.

## Verified (record)

1. The Kübler-Ross five stages of grief are denial, anger, bargaining,
   depression, and acceptance (the DABDA model), introduced by
   psychiatrist Elisabeth Kübler-Ross in her 1969 book *On Death and
   Dying*, based on interviews with terminally ill patients. → [record]
   (psychologytoday.com "Stages of Grief: The Harmful Myth That Refuses
   to Die"; mcgill.ca Office for Science and Society; healthcentral.com)
2. The stages are NOT a fixed sequence and not everyone experiences all
   of them — Kübler-Ross herself did not present them as a strict order.
   → [record] (thecityceleb.com; liquisearch.com Kübler-Ross model)
3. The film frames the stages as a *borrowed pattern* ("the way we react
   to AI follows a pattern — borrowed from the five stages of grief"),
   not as a clinical model of AI users. This is the correction for the
   source's stronger "everyone goes through five stages" phrasing. → [record]
4. LLMs predict a probability distribution over the next token and sample
   from it; the same prompt run twice can give two different answers.
   → [record] (sitation.com "Are LLMs deterministic? Non-determinism
   explained"; github.com/linda-mhmd/ai-solutions-wiki LLM mental model)
5. Not fully deterministic even at temperature 0 — Anthropic's API docs
   state results will not be fully deterministic at temperature 0.0;
   floating-point arithmetic on parallel GPU hardware is non-associative
   and request batching varies. → [record] (sitation.com, citing Anthropic
   docs and Thinking Machines Lab research, Sept 2025)
6. "The engine inside — called a model — is guessing the most likely next
   word, every word, every time" matches the documented next-token
   sampling mechanism. → [record]
7. The narration hedges the demo ("the machine never *quite* answers the
   same way twice"; "you *often* get three different answers") because
   near-deterministic outputs are possible; the absolute claim was cut.
   → [record]

## Judgments (judgment)

- "This is where most people get stuck" (stage three) is the source's
  observation, kept as the film's judgment; no empirical study of AI
  users' stage distribution was found. [judgment]
- "Beats ninety percent of magic prompts" is rhetorical, not a measured
  figure — the source's flourish, kept as rhetoric. [judgment]
- "A hundred times, keep the five best" and "six hours at the keyboard"
  are illustrative examples from the source, not data. [judgment]
- "You'll never go back to one-shot prompting" is a rhetorical flourish,
  not a prediction. [judgment]
- "The ratio is the whole game" / "volume beats precision" is the film's
  thesis, argued from the probabilistic mechanism, not an empirical
  claim. [judgment]

## Definitions (exempt — not factual claims)

- prompt, probabilistic/deterministic, hallucination ("a confident wrong
  answer"), model ("the engine inside"), the AI gambler — plain-language
  definitions authored for the film's general audience.

## Cut or disclosed

- No specific AI product is shown or recommended; the machine is a drawn
  slot machine, never a screenshot of a real interface.
- No model version numbers, no dates that drift — the film names no
  model at all.
- The film does not claim the five stages describe grief itself
  correctly; it borrows the pattern and names the borrowing.
- "Six hours," "a hundred pulls," "five best" are illustrative numbers,
  presented as the gambler's example, not as research findings.
