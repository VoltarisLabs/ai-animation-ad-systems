# Ad 4 - The Honest Cash Buyer (Brief v1)

**Made:** 2026-09-23. **Brand:** Property Abundance. **Status:** script locked, claims NOT filled.
**Concept:** #1 from `Cash_Home_Buying_Winning_Concepts.md`: call out the category, then show the offer math on screen.
**Persona:** Inherited Irene (heir far away).
**Format:** AI talking head, founder selfie, 9:16.
**Hook source:** Dream Catchers row 15, family `contrarian`, score 70 (`pick_hook.py`, 2026-09-23).

> **Nothing in this file ships until every `[NEEDS YOUR TERM]` is replaced with a real Property Abundance fact.**
> FTC Act s.5. An ad may not promise what the business does not deliver.

---

## Step 5 - The five boxes

| Box | Answer |
|---|---|
| Who | Inherited Irene. Inherited a parent's house hours away. Grieving, paying taxes and upkeep on a house she never asked for, tired of the drive. |
| Why she'd buy | She wants a fair price she can *see the reasoning for*, so the family can't blame her for selling too cheap. |
| What it looks like | AI talking head, founder selfie, plus on-screen math. |
| How much she knows | Solution-aware. She has seen the "we buy houses" ads and assumes they are a scam. |
| What we're testing | Does showing the offer formula on screen beat the category's feature list (no repairs, no fees, no showings)? |

---

## Step 6 - The script

**Hook, chosen structure (verbatim shape kept):**
> Everyone tells you to (insert action) but nobody actually tells you how to do it. Here is a # second step by step tutorial that you can save.

**Filled:**

| # | Line | Notes |
|---|---|---|
| 1 | "Everyone tells you to get a cash offer on the house you inherited." | Hook part 1. Names persona in line one. |
| 2 | "Nobody shows you how that number gets made." | Hook part 2. This is the whole ad. |
| 3 | "Watch ten of these ads. Count how many show you the math." | Verifiable by the viewer. Not a claim about a named competitor. |
| 4 | "So here's ours." | The turn. |
| 5 | "Start with what the house is worth fixed up." | Math line 1. On-screen text builds here. |
| 6 | "Subtract what the repairs actually cost." | Math line 2. |
| 7 | "Subtract what it costs us to hold it and resell it." | Math line 3. |
| 8 | "What's left is your offer. That's the whole formula." | Math payoff. |
| 9 | "Sometimes that number beats listing it. Sometimes it doesn't." | The trust line. |
| 10 | "We'll tell you which one you're looking at." | **COMMITMENT: only keep if you will actually do this.** |
| 11 | "If you're hours away and tired of driving back for stupid stuff, that's worth knowing." | Irene's own words, from the research quote. |
| 12 | "[NEEDS YOUR TERM: form URL]. Tell us about the house, and we'll walk you through the worksheet." | CTA. Form must return HTTP 200 before spend. |

### Three alternate hooks to test against line 1+2

- **B (warning):** "Before you take a cash offer on that inherited house, ask one question: how did you get that number?"
- **C (diagnosis):** "If a cash buyer won't show you how the offer was worked out, that's not a price problem. That's a disclosure problem."
- **D (pov):** "Every cash-buyer ad: no repairs, no fees, no showings. Not one of them tells you how they got the number."

**Measured pace:** 115 spoken words over 36 s = 191.7 wpm.
Sits inside the measured band of the references: ref 6 = 182, ref 2 = 185, ref 3 = 205, ref 1 = 228 (judged rushed).
This deviates from `reel_script_2` Step 4, which budgets 150 wpm minus 10% (= 72 words). That budget is for organic reels.
Every measured ad in this category runs 182 wpm or faster, so 72 words over 36 s would read as slow against the feed it competes in.

---

## Step 7 - Shot brief

Target **36 s**, 12 shots, matching ref 3's shot count (12 shots, 32.37 s, 2.70 s average).

| Shot | Time | Line | On screen | What we see |
|---|---|---|---|---|
| 1 | 0.0-8.9 | 1, 2, 3 | Caption only | **NO CUT.** Founder holds frame, selfie, talking straight to camera. Mirrors the reference reel's 8.93 s static open. |
| 2 | 8.9-11.6 | 4 | "OUR FORMULA" | Cut in tighter on the same face. |
| 3 | 11.6-14.3 | 5 | `VALUE FIXED UP` | Text builds, line 1 of 4. |
| 4 | 14.3-17.0 | 6 | `− REPAIR COST` | Text builds, line 2. |
| 5 | 17.0-19.7 | 7 | `− HOLD + RESELL` | Text builds, line 3. |
| 6 | 19.7-24.0 | 8 | `= YOUR OFFER` | **Hold 4.3 s.** The payoff sits here. All four lines on screen at once. |
| 7 | 24.0-26.7 | 9 | "SOMETIMES LISTING WINS" | Back to face. |
| 8 | 26.7-29.4 | 10 | - | Face. |
| 9 | 29.4-32.1 | 11 | - | B-roll: a porch, a locked front door, a long drive. No cash, no money fanning. |
| 10 | 32.1-34.0 | 12a | Form URL | Back to face. |
| 11 | 34.0-35.2 | 12b | Form URL | Form on screen. |
| 12 | 35.2-36.0 | - | Logo + URL | End card. |

---

## Step 8 - Generation (free route)

1. `character_anchor_gemini`: lock the founder's face first. One anchor image, reused for every shot. Without this the face drifts between clips and the ad reads as AI.
2. Gemini/Veo for the clips. Three `gemini_generated_video_*.mp4` already render in this folder, so the route works.
3. Shots 3-6 are text-on-screen, built in the edit. Do not generate them.

## Step 9 - Edit spec (measured, not guessed)

| Setting | Value | Where it came from |
|---|---|---|
| Delivery | 1080x1920, 30 fps | `measure_reference.py`, and the skill's fixed delivery rule |
| Length | 36 s | Between ref 3 (32.37 s) and ref 1 (51.03 s, judged too long) |
| First cut | 8.93 s | Measured off the hook's own reel |
| Body cut rate | 2.70 s per shot | Measured off ref 3, the 2,342,271-view ad |
| Longest hold | 4.3 s on `= YOUR OFFER` | Skill rule: the payoff sits in the static stretch |
| Loudness | −14 LUFS integrated | Reference reel measured −14.34; refs 1, 2, 6 measured −14.2 |
| Captions | `dynamic_captions_3click` | Ref 2 failed on thin white-on-cream text. Ours must read with sound off. |

## What must be true before this ships

| Slot | Needed |
|---|---|
| Line 5-8 | Your real offer formula. If it is not value − repairs − carry/resell, rewrite those four lines to match what you actually do. |
| Line 10 | You will genuinely tell a seller when listing beats your offer. If not, cut lines 9 and 10. |
| Line 12 | A form URL that loads. `propertyabundanceusa.com` returned HTTP 403 on 2026-09-22. |
| All | Meta Housing Special Ad Category status, not yet checked. |

## Deliberately not in this ad

- No dollar figures. Ref 2 put "$450,000" on a run-down clay house and invited the lowball doubt it was trying to calm.
- No countdown, no cap, no "now or never". Ref 1 does this; the research says hype reads as a scam signal.
- No claim about what other buyers pay. Refs 3 and 5 do this and cannot prove it.
- No actor playing a past customer. 16 CFR 465.2 and 255.1.
- No cash-fanning shots.
