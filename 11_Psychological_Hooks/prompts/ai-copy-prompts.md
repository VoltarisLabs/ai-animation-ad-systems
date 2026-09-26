# AI Copywriting Prompts

Use these with Claude, ChatGPT or any LLM. For best results, **attach or paste these files first**: `AD_COPY_CHECKLIST.md`, `hook-formulas.md`, `ad-scorecard.md`, your filled `templates/ad-brief.md`, and `templates/brand-voice.md`.

Run the prompts in order. Never skip the brief.

---

## 0. System / setup prompt (paste once per chat)
```
You are a direct-response copywriter. You follow the attached AD_COPY_CHECKLIST,
hook formulas and ad scorecard exactly. Rules:
- Write for ONE reader in the brief, at their awareness level.
- Use the customer's exact words from the brief wherever possible.
- Specific beats vague: numbers, times, places, names. No adjectives without proof.
- Never invent statistics, testimonials, results or scarcity. If proof is missing,
  write [PROOF NEEDED: ...] instead.
- Grade 5-7 reading level. Short sentences. Sound like a person, not a brand.
- Follow the brand voice file. Respect platform character limits in platform-specs.md.
- No em dashes. No emojis unless the brand voice allows them.
```

## 1. Research synthesis
```
Here are [N] raw customer quotes (reviews, comments, calls): [paste].
Sort them into Pains, Wants, Worries, Tried-and-failed, and Exact phrases.
Then give me: top 5 pains, top 3 worries, top 3 failed alternatives,
10 exact phrases to reuse, and your read on the awareness level and market
sophistication stage (1-5) with one sentence of reasoning each.
```

## 2. Offer check
```
Score this offer on the value equation in offer-builder.md (dream outcome,
likelihood, time, effort; 1-5 each): [offer].
Name the weakest lever and give 3 specific ways to improve it.
Then write the one-line offer: "We help [who] get [outcome] in [time] without [effort], guaranteed by [x]."
```

## 3. Hooks
```
Using the brief and hook-formulas.md, write 15 hooks across at least 6 hook types
suited to [awareness level]. Score each on the 7-point check (Useful, Urgent,
Unique, Ultra-specific, New, Easy, Safe; 1-4 each). Show a table sorted by score.
Recommend the top 3 and say why.
```

## 4. Script / ad copy
```
SHORT-FORM VIDEO:
Write a [length]s [Reels/TikTok/Shorts] ad using [framework] and hook #[n].
Use templates/video-scripts.md. Output the 4-column script sheet
(time | visual/b-roll | spoken line | on-screen text). The three-layer hook
lands in 0-2s, there is a visual change every 1-3s, and it ends on a CTA card.
Then write 3 alternate 0-3s hooks, keeping the body identical.

STATIC:
Write a [Feed 4:5 / Stories 9:16] static ad using layout #[n] from
templates/static-ads.md and hook #[n]. Output: image concept (what's shown),
image text (8 words max), primary text (first line = hook), headline (~27 chars).
Then give 3 variants that change ONE element each (hook, image or layout).
```

## 5. Score and fix
```
Score this ad with ad-scorecard.md. Show points per category with one line of
reasoning each, run the format checks (video or static) and the compliance gate, and total it.
If it scores under 75, rewrite it to fix the 2 weakest categories and re-score.
Ad: [paste]
```

## 6. Ad Grid variations
```
Build an Ad Grid: rows = these audience segments [list], columns = Problem,
Opportunity, Prediction angles. Write one hook + one-line body + CTA per cell.
Keep the offer identical across cells so the test isolates the angle.
```

## 7. Rewrite for another awareness level or platform
```
Rewrite this winning ad for [new awareness level / new platform]. Keep the
core promise and proof. Change the opening strategy per the checklist table and
fit [platform] limits. Ad: [paste]
```

## 8. Learn from results
```
Here is our test log: [paste rows]. What patterns separate winners from losers
(hook type, angle, awareness, format, proof type)? Give 3 hypotheses to test next,
each as a single-variable test.
```
