# Copy Prompts

Our own prompts, built on the methods in [stefan-georgi.md](../03-modern-creators/stefan-georgi.md) and [sabri-suby.md](../03-modern-creators/sabri-suby.md). They work with Claude or ChatGPT. Run them in the order of [testing-and-iteration.md](../testing-and-iteration.md), Section 5.

Rules for every prompt: fill in every `[bracket]`, open a new chat when output gets stuck in a style rut, and fact-check every number the model writes.

---

## 1. Research miner
```
Below are raw comments, reviews and messages from [audience] about [problem].
1. List the 7 most repeated pains, 5 wants, 5 fears and 5 "already tried, didn't work" items.
2. For each, quote the customer's EXACT words (2-3 quotes each). Do not paraphrase or clean up grammar.
3. Write the one sentence this audience thinks but would never say out loud.
4. Tell me which single want appears most often (the bullseye desire).
5. Estimate their awareness level (unaware / problem / solution / product / most aware) and why.
[paste raw text]
```

## 2. Brief check (paste before any generation prompt)
```
Here is the brief for an ad. Summarise it back in 5 bullets and list anything missing or vague before we write.
Market / audience + moment: [...]
Awareness level: [...]
Bullseye desire (their words): [...]
Top pains (their words): [...]
What they already tried and why it failed: [...]
Mechanism (problem + solution), named: [...]
Offer + risk reversal (true terms only): [...]
Proof we can show: [...]
Claims we must NOT make: [invented numbers, speed claims, fake scarcity, anything unconfirmed]
```

## 3. Hook generator (20 at a time)
```
Using the brief above, write 20 opening hooks for a [15-30]s vertical video ad on [platform].
Spread them across these types (2 each): curiosity + specific benefit; contrarian; common mistake;
testable self-check; story already in motion; mocking the "obvious" solution; binding statement
(a truth they nod at); gross or surprising reveal; burning question; the drawback admitted first.
Rules:
- Max 12 words. Conversational, the way a person talks.
- Lead with a benefit in at least half of them.
- Name the situation, never "you are / you have" + a sensitive trait.
- Never announce the ad or the speaker. Never reveal the whole mechanism.
- Only use claims in the brief. No invented numbers.
For each hook give: the line, on-screen text (3-5 words), the first-frame visual, and the type.
```

## 4. Register variants
```
Rewrite this hook and first 3 lines in 4 registers: (a) news exposé, (b) calm empathetic expert,
(c) mid-scene story, (d) blunt friend who's seen it all. Keep the claims identical.
[paste]
```

## 5. Copy chief (dimensionalization pass)
```
Act as a direct-response copy chief. Edit the copy below for:
1. Dimensionalization: replace every generic word with the specific scene the reader lives
   (a place, an object, a moment). Use the pains in the brief.
2. Specificity: swap adjectives for concrete details that are true.
3. Flow: every line must earn the next. Flag any line that contradicts or wanders from the last.
4. Emotional temperature: does it stay at the hook's heat all the way down?
Do not shorten it just to finish. Show each change as: original -> rewrite -> why.
[paste]
```

## 6. Headline iteration (weekly, on the current winner)
```
Here is our best-performing headline: "[headline]".
Give me 10 variations. Make them visceral, ultra-specific and direct. Each must carry a real benefit
and burning intrigue. Max 45 characters. Only use claims from the brief.
```

## 7. Kill-check review
```
Review these hooks against the kill checks. For each, answer yes/no:
announces itself? / curiosity with no benefit? / solvable without clicking? / accuses the reader? /
a competitor could run it word for word? / the body doesn't pay it off? / tries to close in the ad?
Then rank the survivors and give the top 2 fixes for each loser.
[paste hooks + the body they lead into]
```

## 8. Teardown (our ad or a competitor's)
```
Tear down this ad and its landing page in this order:
1) hook: benefit + intrigue, or about the company? 2) scent from ad to page 3) CTA clarity
4) proof density vs. the ask 5) offer strength 6) only then layout.
Score the ad out of 10 and give the 3 highest-leverage fixes, most important first.
[paste ad script / text + page copy]
```

## 9a. Pre-mortem and skeptic (Sabri, `gFaR8BQhqsE`)
LLMs tend to agree with whatever you show them. Force the opposite:
```
Assume this campaign failed badly after 90 days. List the 5 most likely reasons, most likely first.
Then argue against this ad and page as the most skeptical person in [audience] would, objection by objection.
Then grade the copy 1-10 as a top direct-response copywriter and describe exactly what a 10/10 version would contain.
[paste ad + page + brief]
```

## 9. Beat-by-beat check
```
List every claim in this script in order, one per line, as plain statements.
Flag any line that contradicts, repeats or wanders from the one before it, and any claim not in the brief.
[paste script]
```
