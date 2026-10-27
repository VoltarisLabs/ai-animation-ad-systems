# Ad 16 clip plan v2: "The Catch" (2026-09-27)

**Character:** JMSN, from character sheet B (`13_Generated/images/Ad16_JMSN_character_sheet_B_CHOSEN.png`). The user picked it on 2026-09-27.
**Script:** The Catch v3.1 (`11_Psychological_Hooks/Ad16_JMSN_hook_bank.md`), 107 words.
**Model:** Kie `gemini-omni-video`, 9:16, 1080p. The prompt is locked: only the place, the action and the line change. Prompts: `10_Video_Builds/Ad16_JMSN_Walkthrough/old/OLD_5clip_plan_OLD_5clip_plan_clip1_prompt.txt` to `OLD_5clip_plan_clip5_prompt.txt`.
**Start images:** from the 3 scene prompts in `12_AI_Characters/JMSN/Ad16_prompt_scene_images.md`. Image 1 = sheet B. Image 2 = `Ad16_JMSN_car_selfie_new_outfit_B.png`, used for real skin and grain only.

```text
CLIP 1 (L1 front walk, 8 s)
[OPEN A]   I'd buy this house exactly like this.
             SHOW → AI UGC front walk: slow walk, glances back at the sagging roof. Text: I'D BUY IT LIKE THIS
[payload]  Holes and all.
             SHOW → B-roll: collapsed roof (roof_11629980)
[OPEN B]   And yes, there's a catch.
             SHOW → AI UGC front walk: face close, small smile. Text: THERE'S A CATCH
[payload]  Broken furniture. Old beds. Full closets.
             SHOW → B-roll, 3 quick cuts: broken furniture (NEEDS CLIP) → old bed (NEEDS CLIP) → full closet (closet_8844337)
CLIP 2 (L2 kitchen, 8 s)
[OPEN C]   But first, some cash buyers never actually buy your house.
             SHOW → AI UGC kitchen: leans in on "But first". Text: SOME NEVER BUY IT
[payload]  They lock it under contract. Then sell that contract to someone else.
             SHOW → B-roll: contract and pens, no people (contract_7841865)
CLIP 3 (L2 kitchen, 10 s)
[CLOSE C]  That's why I'll say it plain. We're the buyer. No fees. No commission.
             SHOW → AI UGC kitchen: steady eye contact. Text: WE'RE THE BUYER
[payload]  As-is means you fix NOTHING. Every repair in here becomes OURS.
             SHOW → B-roll: gutted ceiling (ceiling_4882745 from 8.5 s) → water into a bucket (leak_4159571)
CLIP 4 (L3 broken floor, 10 s)
[CLOSE B]  That's why there IS a catch. Our offer is LOWER than a fixed-up sale.
             SHOW → AI UGC broken floor: face only, NO cutaway (trust line)
[payload]  You pick the closing date. And you can still say no.
             SHOW → B-roll: quiet house and lawn (house_32116905)
CLIP 5 (L1 front walk, 6 s)
[CLOSE A]  That's why I'd buy it exactly like this. Property Abundance.
             SHOW → AI UGC front walk: smile, small nod. Text: PROPERTY ABUNDANCE
[CTA]      Tap below to learn more.
             SHOW → End card: logo + arrow down to the Learn More button
```

| Clip | Start image | Words | Speech at 176 wpm | Speech at 166 wpm | Omni | Credits (list) |
|---|---|---|---|---|---|---|
| 1 | L1 front walk | 21 | 7.16 s | 7.59 s | 8 s | 105 |
| 2 | L2 kitchen | 22 | 7.50 s | 7.95 s | 8 s | 105 |
| 3 | L2 kitchen | 24 | 8.18 s | 8.67 s | 10 s | 126 |
| 4 | L3 broken floor | 25 | 8.52 s | 9.04 s | 10 s | 126 |
| 5 | L1 front walk | 15 | 5.11 s | 5.42 s | 6 s | 84 |
| | | **107** | | | | **546 ($2.73)** |

**Where the two speeds come from:** 176 wpm is Emily's clip 1 raw (23 words in 7.83 s, measured with the "fast pace" rule). 166 wpm is her edited v4 cut.

**Risk:** clip 2 is tight in 8 s if he speaks at 166 wpm (7.95 s). The prompt says "say every word before the clip ends". If it gets cut off, redo it at 10 s (+21 credits).

**Order:** make clip 1 first, judge it harshly, add rules to the prompt, and only then make clips 2–5.
