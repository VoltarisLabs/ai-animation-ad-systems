# Ad 16 script v2: JMSN walkthrough, "Stop getting repair quotes"

**Replaces** the dialogue in `Property_Abundance_Ad16_JMSN_Walkthrough_30s_v1.md`. The v1 locked Omni prompt structure and the avatar images stay the same. Only the dialogue, the clip-to-image mapping and the durations change.

**Speaker:** JMSN as Property Abundance's buyer, company voice. He never plays a customer.
**Avatar targeted:** "The House Needs Everything" (Fixer-Upper Fran) from `04_Audience_Research/Research_Document_Cash_Home_Buying.md`. What the research says about her:
- She spends her time getting repair quotes.
- She is afraid of repair bills and of being taken advantage of.
- Her own words: "No Money.. How can I repair My Home before Selling".

**Built with:**
- `kristian_jennings_ai_ugc_workflow`: storyboard layout, hooks first, the avatar who has solved the problem, capitalised stress words, 4/6/8/10 s durations.
- `reel_direction_2`: the format, the language gate and one redefined term.
- `05_Tutorials/Hook_Psychology_Research_Report.md`: two loops for a 30–60 s ad, payload between every step, every close starts with "That's why", brand on the last close.
- `loop-order-rule`: nested A-B, closed B-A.
- The Hook Map rubric and its three gates (situation, predator, truth).

---

## What the references say about the talking hook

Measured from all 44 refs: 35 in `07_Assets/Reference_Ads/v2/` (transcripts) and 9 vertical (contact sheets and transcripts, 2026-09-26).
- 17 of the 35 start talking at 0.00 s. In all 9 vertical refs, faster-whisper word timings put the first word at 0.00 s.
- 3 of the 9 vertical refs open with an "If" callout: bright_future ("If your house looks like this"), hall_of_fame and quick_close. That is the Labeling type (hook H2 below).
- 6 of the 35 open on a name or brand ("Hi, I'm…", "My name is…"). That wastes the first second. This script saves the brand for the last close.
- 7 of the 35 open on a question. 6 of those 7 are the HomeVestors "What could go wrong?" line, which belongs to their campaign. The research file says question-only hooks slightly lower engagement. This script opens on a command instead.
- Damage shows up in 2 of the 9 vertical refs. No presenter walks through a house in any of them. The walkthrough is original.

---

## Hooks (Open A), pick one per cut

Scores use the Hook Map rubric (5 axes, 0–2 each, under 7 = rewrite). They are my judgement, not measured.

| # | Type | Hook | Score | Close A line to match |
|---|---|---|---|---|
| **H1 (main)** | Pattern Interrupt | "Stop getting repair quotes." | 7 | "That's why you stop getting repair quotes." |
| H2 | Labeling | "If you're pricing out a new roof, stop." | 7 | "That's why you stop pricing out that roof." |
| H3 | Contrarian | "You don't have to fix this house to sell it." | 7 | "That's why you don't fix it to sell it." |

A hook test re-makes clip 1 and clip 4: 84 + 105 = 189 credits per extra hook, at list price.

---

## Script (script left, picture right)

| Clip | Loop | Line | On screen |
|---|---|---|---|
| 1 | **Open A** | "Stop getting repair quotes." | AI UGC, front walk (L1). He walks slowly. |
| 1 | payload | "Look at this ROOF. And the floor inside? WORSE." | B-roll: roof close-up on "ROOF" (first cut before 2.5 s), then floorboards on "floor". |
| 2 | **Open B** | "You're scared we'll lowball you for it." | AI UGC, broken floor (L3). |
| 2 | payload | "You got the roof quote. Read it twice. Put it in a drawer." | B-roll: an old kitchen drawer, objects only, no paper text showing. |
| 3 | payload | "That's not a house problem. That's a BUYER problem." | AI UGC, kitchen (L2). He points at the hanging cabinet door. |
| 3 | **Close B** | "That's why I won't dodge the lowball question. Our offer is LOWER than a fixed-up sale." | AI UGC, kitchen. Stay on his face for this trust line. |
| 4 | payload | "As-is means you fix NOTHING. Not the roof. Not the floor." | B-roll: roof on "roof", floorboards on "floor". |
| 4 | **Close A** | "That's why you stop getting repair quotes. Property Abundance." | AI UGC, front walk (L1). |
| 5 | Hook 2 | "Your house doesn't need fixing. It needs a different buyer." | AI UGC, front walk (L1). Smile. |
| 5 | CTA | "Tap below. No fees, no obligation." | End card: logo and the form on a phone. |

**reel_direction_2 map:**
- **QUESTION** (the viewer's silent question): "Do I have to fix this house before anyone will buy it?"
- **HOOK 1** (Pattern Interrupt): stops the thing she is doing right now.
- **EXPLAIN:** the roof and floor lines, which give the specific detail.
- **ILLUSTRATE:** quote → drawer → "That's not a house problem. That's a BUYER problem."
- **Redefined term:** "as-is", which comes to mean "you fix nothing".
- **LESSON:** stop getting quotes. It is something she can do today.
- **HOOK 2** (Reframe): echoes the diagnosis.

**Loops:** Open A → payload → Open B → payload → Close B → payload → Close A → Hook 2 → CTA. There are 2 loops, the count the report gives for 30–60 s. A payload follows every loop line, and no loop opens and closes back to back.

**Claims:** the only claims are ones the user confirmed on 2026-09-25: as-is, no fees, no obligation. The line "our offer is lower than a fixed-up sale" is the same self-incrimination line the user approved for Ad 15 ("Cash offers usually come in LOWER than listing. OURS too."). The script has no numbers, no speed claims and no competitor names.

---

## Checks (run 2026-09-26)

| Check | Result |
|---|---|
| Words | 94 (the 8 Ads rule allows 65–95) |
| Length | 33.98 s at 166.0 wpm (Emily's measured Omni pace); 28.61 s at 197.1 wpm (the 9 vertical refs' median). Estimates. |
| Em dashes / banned phrases | 0 / 0 |
| Reading grade | 1.7 (Flesch-Kincaid, regex syllable estimate). 21 sentences, 4.6 words each on average. |
| First 5 words | "Stop getting repair quotes. Look" |
| Back-to-back open/close | none |
| topic_gate.py | 50 / 100, pass mark 55. It is calibrated on 12 @billy.coder tech posts. Its two missing points, a named angry party (30) and a named price (8), are both banned in this ad (no competitor claims, no numbers). |

## Omni clips

The locked v1 prompt stays. Swap in the dialogue, the image and the duration below.

| Clip | Image | Words | At 166 wpm | Duration | Credits (list) |
|---|---|---|---|---|---|
| 1 | L1 front | 13 | 4.70 s | 6 s | 84 |
| 2 | L3 floor | 20 | 7.23 s | 8 s | 105 |
| 3 | L2 kitchen | 25 | 9.04 s | 10 s | 126 |
| 4 | L1 front | 20 | 7.23 s | 8 s | 105 |
| 5 | L1 front | 16 | 5.78 s | 8 s | 105 |
| | | **94** | | | **525** |

Add the 3 avatar images (54 credits) for a total of 579 credits, $2.895, for one take each. Nothing has been run.

**Open:** the "Tap below" line needs `propertyabundanceusa.com` fixed first. It returned HTTP 403 on 2026-09-25.
