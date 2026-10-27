# Ad 17 v2: JMSN in the trashed rental, script and scene breakdown

Built with [11_Psychological_Hooks/templates/script-and-scene-breakdown.md](../../11_Psychological_Hooks/templates/script-and-scene-breakdown.md). The worked example it matches is `03_Ad_Scripts_and_Briefs/Property_Abundance_Ad16_JMSN_Breakdown_v3.md`.

**Speaker:** JMSN, Property Abundance's buyer, in the company voice ("we", "our"). He never plays a landlord, seller or customer, so no AI label is needed.
**Audience:** Persona 3, the Burned-Out Landlord. The tenant is finally out and left the rental trashed, and the mortgage keeps coming.
**Format:** AI UGC handheld selfie, 9:16. Three spots inside one vacant rental. 3 Omni clips of 8 / 8 / 10 s.
**Status:** script and storyboard only. Nothing has been generated and no credits have been spent.

## What changed from v1 (review `10_Video_Builds/Ad17_JMSN_Landlord/REVIEW_script_v1.md`, FAIL)

| Fix | v1 | v2 |
|---|---|---|
| 1. Cut plan | 10 cuts in 23.4 s (4.27 per 10 s), 2 of them mid-sentence ("Fix it, / list it", "But you pay / no commission"), and an unsourced "3-4.5" target | **7 cuts in 23.4 s = 2.99 per 10 s, every cut at a sentence start.** Text pops cover "change something every 1-3 s". The target is the user's rule (`ugc-edit-merge-then-scenes`): about 3 cuts per 10 s, cut at sentence boundaries, never mid-sentence. |
| 2. Trust line | "We buy it ourselves, for LESS than a fixed-up sale." (two claims fused, no admission frame, and it failed the read-aloud check) | **"Our offer's LOWER than a fixed-up sale."** This is the Ad 16 final's wording, as its own sentence (claim status: used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm). "We buy it ourselves." is **cut**; the reason is below. |
| 2b. Close A | "They left. Now YOU can." (a callback only) | **"They left. That's how YOU leave too."** "That's how" ties the payoff to the mechanism, as Ad 16's "That's why" did. |
| 2c. Read-aloud | "House sits empty." (reads like a caption) | **"House is sitting empty."** Clip 1 goes from 18 to 19 words, under the 20 limit. |
| 3. Part D | "Pass on all 7" kill checks, no Step 6 row, brand departure not recorded | The copyable check is marked **borderline**. A **Step 6 CTA row** is added, and the end card now says what the tap does: ASK FOR MY OFFER · NO OBLIGATION. The **no-brand-name** departure is recorded with its source. |
| 4. Paths | Prompt and image names didn't match the files on disk | Synced in the JSON: `Ad17_video_prompt_clip1_front_door.txt` / `clip2_wall_hole.txt` / `clip3_ceiling_leak.txt`, and `Ad17_JMSN_L1_front_door_v1.png` / `L2_wall_hole_v1.png` / `L3_ceiling_leak_v1.png` |
| Review fix 5 (for the avatar director) | L2 said "punched" | Part C now says "a hole in the drywall", with nothing that hints at who the tenant was: no toys, no religious items |

**Why "We buy it ourselves." was cut rather than kept as its own sentence:**
1. It answers the wholesaler fear, and the ad never voices that fear. Voicing it would cost 6-8 words that clip 3 doesn't have (25 max). It would also rebuild Ad 16's centre beat, which the brief says not to repeat.
2. Without it, Close B ("Or sell it AS-IS.") leads straight into "Our offer's LOWER...". The word "our" already tells the viewer who the buyer is.
3. It removes the one claim whose status the files disagree on (Part A). What's lost is the anti-wholesaler credential that the Hook Map calls "the one credential he cares about". It stays available for a later ad that sets the fear up.

## How this differs from Ad 16 ("The Catch")

| | Ad 16 | Ad 17 |
|---|---|---|
| Hook | "I'd buy this house EXACTLY like this." (the buyer's claim) | "The tenant left. Now YOU can too." (the viewer's exit) |
| Open B | "And yes, there's a CATCH." | "So what's the move?" (his decision) |
| Body | An object list, then the wholesaler exposé | His two alternatives, each with its cost (re-rent, fix and list) |
| Admission | Close B: "That's the CATCH: our offer's LOWER than a fixed-up sale." | Payload, opening clip 3: "Our offer's LOWER than a fixed-up sale." This is the Ad 16 final's claim sentence without the "catch" frame, which is the form review 1 asked for (claim status: used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm). The "honest part" line is not reused. |
| Close A | Repeats "EXACTLY like this" | "They left. That's how YOU leave too." |
| Locations | Front walk outside, kitchen, broken floor | Open front door looking in, living room with a hole, bedroom with a ceiling leak |

---

## Part A. Research card (internal only, never on screen)

| Field | Content | Source |
|---|---|---|
| Audience + moment | A side investor with a day job. The tenant is finally gone. He walks in and finds holes in the walls, bags and broken furniture left behind, and a leak stain on the ceiling. The house is empty and the mortgage still comes out every month. | Research doc, persona 3 (pain: "No rent coming in, legal fees, damage to the property"; lifestyle: "using savings to cover the mortgage"). Hook Map trigger moment [R]: "He walks the property and sees new damage." |
| Awareness | **Solution-aware.** See the justification below. | Hook Map, Avatar 3: "Solution-aware, most-aware on a good day" [I] |
| Sophistication | Stage 4. Assume he has already seen every "we buy houses" ad, so sell against his alternatives and show the mechanism. | `03-modern-creators/jeremy-haynes.md`, rule 2 |
| Bullseye desire | "Get out, tenant and all." In this moment the tenant is gone, so the desire is simply to get out. | Research doc, persona 3 desire. Representative voice (Buyer_Avatar README, not a quote): "I just want out." |
| Hidden desire | For the loss to stop being his. "A clean transfer of the problem is worth more to him than a higher number." | Hook Map [I] |
| Top pain (their words) | "Bleeding money for months on an attorney is gutting me." · "This house has drained my energy, finances, health, and happiness." | Research doc Golden Nuggets (r/Landlord, r/simpleliving) |
| Top fear / objection | "Are you going to renegotiate later?" · "Are you a wholesaler?" · "How much below market?" · "What's the catch?" | Buyer_Avatar README, primary objections; research doc objections table |
| What he's weighing | 1. **Re-rent it** → another tenant: "managing tenants... could just turn into another thing on my plate." 2. **Fix it, then list it** → "No money, time or energy to manage contractors. Big renovations rarely pay back." Plus the commission. 3. **List it as-is** → "Buyers still inspect, bring a repair list and renegotiate." | Research doc, failed solutions and misconceptions tables. Jeremy Haynes: name the alternatives. |
| Unspoken sentence | "I told people this was a good investment, and now I just want it to stop being mine." | Hook Map core wound and hidden desire [I]. Research [R]: "I honestly feel like I'm a victim and the tenant is a bully here." |
| Scenes (dimensionalized) | 1. The fist-size hole in the living room drywall at head height. 2. The brown ring on the bedroom ceiling, with a bucket under it (research scene, **not in frame**: the L3 shot is a low-angle, chest-up selfie that can't show the floor). 3. The mortgage payment that still clears every month on a house with nobody in it. 4. Trash bags and a broken chair left in the front room (picture only; no line promises anything about them). | Dimensionalized from the pains above |
| Confirmed claims we may use | Buys as-is · belongings can stay · no commission · no fees or closing costs · seller picks the closing date · no obligation · Property Abundance buys the house itself (not a wholesaler) | Project CLAUDE.md, confirmed by the user 2026-09-25 |
| **Claim to confirm** | "Our offer's lower than a fixed-up sale": **used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm.** Ad 15 v2 said "Cash offers usually come in lower than listing. Ours too." | Ad 16 final clip 3 (run on the user's typed go, session checkpoints 29-30; Ad 16 is still unreviewed); Ad 15 v2 script; CLAUDE.md open items |
| **Used in v2** | As-is · our offer is lower than a fixed-up sale (user to confirm) · no commission · no fees · no obligation (end card) | |
| Banned in this ad | Any number, price, timeline or speed ("fast", "in days") · scarcity · showing the offer math · buying with a tenant inside · eviction help · legal advice · any promise about the tenant's abandoned property · competitor names · "any condition" · "top dollar" · personal-attribute lines ("you're behind on your mortgage") | Brief; CLAUDE.md open items; Hook Map banned language; checklist Step 8 |

**Discrepancy to know about ("we buy it ourselves").** v2 no longer uses the line, but the conflict remains for later ads. CLAUDE.md lists "Property Abundance buys the house itself (no wholesaling)" as confirmed on 2026-09-25, and the Ad 16 final used "WE'RE the buyer". But the Ad 16 v3 breakdown banned it as an open question, the research doc marks the offer terms PLACEHOLDER, and the Hook Map's truth gate lists "direct purchase" as unconfirmed. Please reconfirm it once, and then update the research doc.

**Why Solution-aware.**
1. He knows his problem. He is standing in it.
2. He already knows the ways out: re-rent, fix and list, list as-is, or sell to a cash buyer. The research lists every one of them as something landlords try.
3. The Hook Map places him at solution-aware and says he "has already considered cash buyers".
4. He is not most-aware. He doesn't know Property Abundance, and a search for the name finds the UK training company first (research doc, "Name conflict").

So the ad opens on the result he wants (to be out), sells against his alternatives (Stage 4) and shows the mechanism with confirmed terms only: as-is, our offer, no commission, no fees. Checklist Step 1 table for this level: open with the result or the mechanism.

---

## Part B. Script breakdown (H1, the main hook)

| # | Beat | Spoken line | Job of this line | Source (research quote or rule) | Trigger |
|---|---|---|---|---|---|
| 1 | **Open A** (hook) | "The tenant left. Now YOU can too." | Qualify him in the first second (the word "tenant") and promise the one thing he buys: an exit. It opens a loop: how? | Hook Map, Jason lever 3: "Finality. The promise is not money, it's 'it stops being yours.'" Research desire: "Get out." Sabri: benefit-led. | Curiosity + benefit, permission to stop |
| 2 | Payload | "House is sitting empty. Same mortgage, every month." | Turn the bleed into a picture, in monthly terms with no number | Hook Map lever 2: "Arithmetic of the bleed. He thinks in monthly loss. Speak in it." Research outcome: "Stop the money leak." | Loss aversion (accurate) |
| 3 | **Open B** | "So what's the move?" | Say out loud the decision he's stuck on | Hook Map: "He does not need convincing that selling is right." Jeremy Haynes: he's comparing options | Curiosity gap |
| 4 | Payload | "Patch THAT and bet on the NEXT tenant?" | Alternative 1 and its real cost: another tenant | Research: "managing tenants... could just turn into another thing on my plate." README voice: "I don't want to deal with another tenant." | Contrast |
| 5 | Payload | "Fix it, list it, pay commission?" | Alternative 2 and its real cost: repairs, then a commission | Research: "Fixing it up first: No money, time or energy to manage contractors"; misconception table (commission) | Contrast |
| 6 | **Close B** | "Or sell it AS-IS." | Answer "what's the move" with the third road | Confirmed: buys as-is. `offer-and-mechanism.md`: "A buyer who buys it as it stands" | Mechanism |
| 7 | Payload | "Our offer's LOWER than a fixed-up sale." | Say the catch first, in the Ad 16 final's words, on its own | Claim used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm. Hook Map: "Self-incrimination... the one move that outperforms on all three." | Damaging admission |
| 8 | Payload | "But you pay no commission, no fees." | Offset the admission with the costs he named in line 5 | Confirmed: no commission, no fees or closing costs | Risk reversal, contrast |
| 9 | **Close A** | "They left. That's how YOU leave too." | Pay off the hook and tie it to the mechanism: the as-is sale on these terms is how he gets out | Loop rule: A closes last with the biggest payoff. Review: link Close A to the mechanism, as Ad 16's "That's why" did. | Consistency, reason why |
| 10 | CTA | "Tap below." End card: ASK FOR MY OFFER · NO OBLIGATION | The smallest honest step, and it says what the tap does | `copy-banks.md` CTA rules: first person, say what happens next. Confirmed: no obligation. | Zero-price first step |

**Loop sequence:** OPEN A (1) → payload (2) → OPEN B (3) → payload (4, 5) → CLOSE B (6) → payload (7, 8) → CLOSE A (9) → CTA (10). They are nested and close in reverse order. No loop opens and closes back to back. When B closes, A is still open. The hook's promise closes last.

**Why only 2 loops:** the ad runs about 23 s. The psychology report says under 30 s gets 1 loop and 30-60 s gets A + B, and Howie (00:25:08) says a 30 s ad has no time for A, B and C. Two loops follow the brief and Ad 16's precedent.

### Labelled script (H1)

```text
CLIP 1 (8 s, L1 open front door, 19 words)
[OPEN A]   The tenant left. Now YOU can too.
           SHOW → AI UGC, L1: JMSN just inside the open front door, thumb over his shoulder at the messy front room on "left". Text top third: TENANT LEFT. YOU CAN TOO.
[payload]  House is sitting empty. Same mortgage, every month.
           SHOW → b-roll house_32116905 (from 3 s in, after the passing SUV), cut on "House", held through both sentences. Text: HOUSE SITTING EMPTY, then SAME MORTGAGE. EVERY MONTH.
[OPEN B]   So what's the move?
           SHOW → AI UGC, L1 punch-in 131%, small shrug, eyebrows up. Text: WHAT'S THE MOVE?

CLIP 2 (8 s, L2 living room with the hole, 18 words)
[payload]  Patch THAT and bet on the NEXT tenant?
           SHOW → AI UGC, L2 (new setup): half-turned, free hand points at the hole in the drywall on "THAT". Text: PATCH IT?, then NEXT TENANT?
[payload]  Fix it, list it, pay commission?
           SHOW → cut on "Fix" to b-roll forsale_7578271 (FOR SALE sign on a lawn, no people, no broker name), held through the question. Under it, his hand drops on "Fix it". Text: FIX IT? LIST IT? COMMISSION?
[CLOSE B]  Or sell it AS-IS.
           SHOW → AI UGC, L2, hand already down (it dropped under the insert), still, eyes on the lens. Text: OR SELL IT AS-IS

CLIP 3 (10 s, L3 bedroom with the ceiling leak, 23 words)
[payload]  Our offer's LOWER than a fixed-up sale.
           SHOW → AI UGC, L3 (new setup): standing still under the ceiling stain. NO cutaway (trust line). Text: OUR OFFER'S LOWER
[payload]  But you pay no commission, no fees.
           SHOW → same L3 shot, no cut. Text pop: NO COMMISSION. NO FEES.
[CLOSE A]  They left. That's how YOU leave too.
           SHOW → same L3 shot, small nod on "YOU leave". Text pops: THEY LEFT. (on "They"), then THAT'S HOW YOU LEAVE (on "That's")
[CTA]      Tap below.
           SHOW → cut on "Tap" to the end card: logo, arrow down to the button, ASK FOR MY OFFER · NO OBLIGATION.
```

Plain lines for Omni's dialogue field (one per clip):

```text
Clip 1: The tenant left. Now YOU can too. House is sitting empty. Same mortgage, every month. So what's the move?
Clip 2: Patch THAT and bet on the NEXT tenant? Fix it, list it, pay commission? Or sell it AS-IS.
Clip 3: Our offer's LOWER than a fixed-up sale. But you pay no commission, no fees. They left. That's how YOU leave too. Tap below.
```

**Prompt files:** all 3 Omni prompts were synced to these dialogue lines on 2026-09-27 (clip 3 nod on "YOU leave").

### Word count and length (counted by script)

| Clip | Duration | Words | Stress words (CAPS) | Speech at Omni pace (0.351-0.380 s/word, measured on Ad 16) | Limit |
|---|---|---|---|---|---|
| 1 | 8 s | 19 | YOU | 6.67-7.22 s | ≤ 20 |
| 2 | 8 s | 18 | THAT, NEXT, AS-IS | 6.32-6.84 s | ≤ 20 |
| 3 | 10 s | 23 | LOWER, YOU | 8.07-8.74 s | ≤ 25 |
| **Total** | | **60** | | **21.06-22.80 s** | |

- **At the reference pace (197.1 wpm), 60 words take 18.26 s.** Omni speaks slower: 162.4 and 170.7 wpm on Ad 16 clips 2 and 1. So the edit length estimate is about 23.4 s (21.90 s of speech at 0.365 s/word, plus a 1.5 s end-card hold). Retime to the real clips.
- **Fit against the Omni lengths:**
  - Clip 1 needs 6.7-7.2 s and clip 2 needs 6.3-6.8 s, both over the 6 s option. So 8 s is right.
  - Clip 2 stays at 18 words because its last line is Close B, and Ad 16's clip 2 dropped its last sentence at 22 words.
  - Clip 3 needs 8.1-8.7 s, which is over the 8 s option. So 10 s is right, with a 1.3-1.9 s margin.
- **You vs. we:** 3 "you" words, 1 "we" word (our) = 75 / 25, close to the 80 / 20 target. v1 was 60 / 40.

### Hook variants (test the hook only; the body stays the same)

Each swap re-makes clip 1 (the hook) and clip 3 (Close A).

| # | Family | Lead | Hook (line 1) | On-screen text | Close A (line 9) | Clip 1 / clip 3 words |
|---|---|---|---|---|---|---|
| **H1 (main)** | Two-beat, finality | Benefit-led | "The tenant left. Now YOU can too." | TENANT LEFT. YOU CAN TOO. | "They left. That's how YOU leave too." | 19 / 23 |
| H2 | Pain → relief question | Pain-led | "What the tenant broke? Not YOURS to fix." | NOT YOURS TO FIX | "So what they broke? Not YOURS." | **20** / 22 |
| H3 | Reframe (reel_direction_2 archetype 4) | Pain-reframe | "Not a repair problem. An EXIT problem." | NOT A REPAIR PROBLEM | "So take the EXIT." | 19 / 20 |

- **H1 against H2 is the benefit-vs-pain test.**
- **H2's clip 1 sits at the 20-word limit.** Word-diff it first. If Omni drops "So what's the move?", that clip has lost Open B.
- **H2 descends from the unused Ad 16 hook bank #11.**
- **H3** is the diagnostic line the reel_direction_2 format would have put in ILLUSTRATE. It has only 1 "you" word, and the picture has to do the qualifying.

### The 10 hooks scored (checklist Step 4)

These are written as 5 pairs, each pain-led hook with its benefit-led twin. The kill checks come from `testing-and-iteration.md`. The 7-point score uses Useful, Urgent, Unique, Ultra-specific, New, Easy and Safe, each 1-4. Keep a hook at **20/28 or more**. All scores are my judgment, not measured.

**Change in v2:** the copyable check is now applied at the same bar to every hook. Every hook here is tied to the landlord's moment, but none names anything only Property Abundance could say. So hooks 1, 2, 3, 5 and 9 are now marked **borderline** on it. Hooks 4, 6 and 8 stay as fails, because they don't even carry the moment. The scores are unchanged: the Unique column already priced this in.

| # | Pair | Lead | Hook | Kill checks | U | Ur | Un | Sp | N | E | S | Total | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | Pain | "The tenant left. The mortgage didn't." | Borderline (copyable) | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 18 | Cut: no benefit. Its idea lives on as payload line 2. |
| 2 | A | Benefit | "The tenant left. Now YOU can too." | Borderline (copyable) | 3 | 2 | 3 | 3 | 4 | 3 | 3 | **21** | **Keep: H1** |
| 3 | B | Pain | "What the tenant broke? Not YOURS to fix." | Borderline (copyable) | 4 | 2 | 3 | 3 | 2 | 4 | 3 | **21** | **Keep: H2** |
| 4 | B | Benefit | "Sell the rental. Leave the damage to US." | Fail: copyable, and no moment in it | 4 | 1 | 1 | 2 | 2 | 4 | 3 | 17 | Cut |
| 5 | C | Pain-reframe | "Not a repair problem. An EXIT problem." | Borderline (copyable) | 3 | 2 | 3 | 2 | 4 | 3 | 3 | **20** | **Keep: H3** |
| 6 | C | Benefit | "Skip the repairs. Take the EXIT." | Fail: copyable, generic | 3 | 1 | 2 | 2 | 2 | 4 | 3 | 17 | Cut (kept as H3's Close A idea) |
| 7 | D | Pain | "Still paying the mortgage on a rental that looks like THIS?" | Fail: "you" plus a money situation reads as a personal-attribute call-out (Meta) | 2 | 3 | 3 | 3 | 2 | 2 | 1 | 16 | Cut |
| 8 | D | Benefit | "Sell a rental that looks like THIS, as-is." | Fail: copyable. The bright_future ref says "If your house looks like this", and Ad 16 used "EXACTLY like this". | 4 | 1 | 1 | 3 | 1 | 4 | 3 | 17 | Cut |
| 9 | E | Pain (pattern interrupt) | "Don't patch this wall for the NEXT tenant." | Borderline (copyable) | 3 | 2 | 3 | 4 | 3 | 2 | 2 | 19 | Cut: under 20, and it clashes with body line 4 |
| 10 | E | Benefit | "Put the paint roller DOWN." | Borderline: the benefit isn't stated | 2 | 2 | 3 | 3 | 4 | 3 | 2 | 19 | Cut: under 20, and it needs a prop in the L1 image |

### Departures from the template and the preloaded skill (with sources)
- **The brand name is never spoken.** The template's Part B row 7 says Close A should "reveal the brand". The user made this call on Ad 16 on 2026-09-27 ("no company name in clip 3"; session log `2026-09-26_jmsn-walkthrough-prompts`, checkpoint 29; Ad 16 shot list, shot 10 note). The brand appears only as the logo on the end card.
- **Hook 2 (Close A) echoes Hook 1 instead of being a different type** (reel_direction_2). The template's Close A pays off the hook for consistency, and Ad 16 v3 did the same.
- **There is no ILLUSTRATE diagnostic line or redefined term** (reel_direction_2). Neither fits in 60 words. H3 carries the diagnostic line as a testable hook.
- **Language gate:** zero em dashes, zero banned phrases (grep run on this file). Tension lands in the first 5 words ("The tenant left. Now YOU").

---

## Part C. Scene breakdown

### The three JMSN locations (for the avatar director, Nano Banana Pro 9:16)

Character input: `13_Generated/images/Ad16_JMSN_character_sheet_B_CHOSEN.png` **only**. He wears the buffalo-check overshirt, grey tee, olive cargos and white sneakers, with the earbud and chain as on the sheet. **Do not upload any car selfie.** In Ad 16 the car's sun visor leaked into scenes 1 and 3.

Every image: an amateur phone look, no words anywhere (no signs, papers, labels or screens), daylight only, and no other people. **Nothing may hint at who the tenant was:** no children's toys, no religious items, no personal photos (review fix 5, Fair Housing guard). Output names: `13_Generated/images/Ad17_JMSN_L1_front_door_v1.png`, `..._L2_wall_hole_v1.png`, `..._L3_ceiling_leak_v1.png`.

| Loc | Where | Damage in frame | JMSN pose / action | Framing and camera |
|---|---|---|---|---|
| **L1** | Standing just inside the open front door of a vacant single-family rental, looking into the front room | Behind him: two black trash bags, a broken dining chair on its side, a stained beige carpet, crooked blinds, scuffed walls. The door frame edge is at one side of the frame. | Relaxed. His free thumb points back over his shoulder at the room. A small wry half-smile. | Close, off-centre (face in the left third, the mess in the right two thirds), arm's-length selfie, phone slightly below eye level |
| **L2** | Living room of the same rental | A fist-size **hole in the drywall** at head height, clearly visible, with scuffs around it. A bent blind. A bag and a broken lamp on bare subfloor. | Half-turned toward the wall. His free hand points at the hole. | Close, off-centre (face in the right third, hole in the left third at head height), arm's-length selfie at eye level |
| **L3** | Back bedroom of the same rental | A brown water-stain ring on the ceiling with a sagging patch, and peeling paint on the upper wall. No bucket: the low-angle, chest-up frame can't show the floor. | Standing still, calm, eyes on the lens (trust line), free hand relaxed at his side | Close, off-centre (face in the lower-left third), arm's-length selfie from a **low angle, phone just below the chin, tilted up**, so the stain is in the upper third above his head |

### Shot table (H1)

Times are estimates at 0.365 s/word, the midpoint of Ad 16's measured Omni pace; retime to the real clips.
- **Every cut sits at a sentence start** (user rule `ugc-edit-merge-then-scenes`). In the edit, cut inside the measured silence before that sentence.
- **Between cuts, a text pop changes every 1-3 s.**

| Scene | Time (s) | Spoken over it | Shot / framing | On screen (subject + action) | B-roll insert (lands on) | On-screen text (3-5 words), pop times | Sound | Source image / note |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.000-2.555 | "The tenant left. Now YOU can too." | L1 selfie, close, off-centre, slightly low | JMSN in the doorway, thumb over his shoulder on "left" | none: the three-layer hook is on his face | TENANT LEFT. YOU CAN TOO. (0.0) | Door creak, room tone, music in low | Clip 1 / L1 |
| 2 | 2.555-5.475 | "House is sitting empty. Same mortgage, every month." | Insert, slow drift | | `house_32116905`, cut on "House" (sentence start), held through both sentences | HOUSE SITTING EMPTY (2.555) → SAME MORTGAGE. EVERY MONTH. (4.015) | Room tone | Stock, no people. Take it from 3 s in or later: a black SUV passes at 1.0-2.5 s (reviewer's 2 fps sheet). |
| 3 | 5.475-6.935 | "So what's the move?" | L1 punch-in 131% | Small shrug, eyebrows up | none (loop line) | WHAT'S THE MOVE? (5.475) | Music dips | Clip 1 |
| 4 | 6.935-9.855 | "Patch THAT and bet on the NEXT tenant?" | L2 selfie, eye level (new setup, clip boundary) | Half-turned, points at the hole on "THAT" | none: the hole is in his own shot. No stock drywall-hole clip exists. | PATCH IT? (6.935) → NEXT TENANT? (8.76) | Knock on drywall SFX on "THAT" | Clip 2 / L2 |
| 5 | 9.855-12.045 | "Fix it, list it, pay commission?" | Insert, push-in | | `forsale_7578271`, cut on "Fix" (sentence start), held through the question | FIX IT? LIST IT? COMMISSION? (9.855) | Wind | Stock. The sign reads only FOR SALE: no broker name or phone, no people. It is 720 × 1280, so upscale 1.5×. His hand drops on "Fix it" in clip 2 under this insert. |
| 6 | 12.045-13.505 | "Or sell it AS-IS." | L2 selfie | Hand already down (dropped under shot 5), still, eyes to the lens | none (loop line) | OR SELL IT AS-IS (12.045) | Music lifts slightly | Clip 2 |
| 7 | 13.505-21.170 | "Our offer's LOWER than a fixed-up sale. But you pay no commission, no fees. They left. That's how YOU leave too." | L3 selfie, low angle (new setup, clip boundary) | Still, direct, steady. Small nod on "YOU leave". | **none: trust line and close, stay on the face** | OUR OFFER'S LOWER (13.505) → NO COMMISSION. NO FEES. (16.06) → THEY LEFT. (18.615) → THAT'S HOW YOU LEAVE (19.345) | Music drops out, faint drip SFX, music back in on "They left" | Clip 3 / L3 |
| 8 | 21.170-23.400 | "Tap below." | End card, cut on "Tap" (sentence start) | Logo, arrow down to the button | none | ASK FOR MY OFFER · NO OBLIGATION | Music out | Editor end card. The landing page must work first. |

**Cut rate (user rule: about 3 per 10 s, at sentence boundaries):**
- **7 cuts in about 23.4 s = 2.99 per 10 s.** The cuts are at 2.555, 5.475, 6.935, 9.855, 12.045, 13.505 and 21.170 s, and each is the first word of a sentence.
- The first cut is at 2.555 s. The competitor median first cut is 2.92 s (analysis of 44 Meta ads, 2026-09-26).
- The longest shot is scene 7 (7.665 s). It covers the trust line and Close A on one face shot, and four text pops change the screen inside it, at most 2.555 s apart.
- **Spare, not planned:** `contract_7841865` on "But you pay no commission, no fees." It would add 2 cuts (9 = 3.85 per 10 s), which is above the user's figure, and it would break the trust shot.

**Sound-off test:** read alone, the text pops go TENANT LEFT. YOU CAN TOO. → HOUSE SITTING EMPTY → SAME MORTGAGE. EVERY MONTH. → WHAT'S THE MOVE? → PATCH IT? NEXT TENANT? → FIX IT? LIST IT? COMMISSION? → OR SELL IT AS-IS → OUR OFFER'S LOWER → NO COMMISSION. NO FEES. → THEY LEFT. → THAT'S HOW YOU LEAVE → ASK FOR MY OFFER · NO OBLIGATION. That tells the whole story.

### Stock clips checked (3 frames each, at 1/6, 1/2 and 5/6; 2 larger frames for the ones used)

| Clip | What it shows | Verdict |
|---|---|---|
| `house_32116905` | House under a red-leaf tree, street | **Used** (scene 2), from 3 s in |
| `forsale_7578271` | FOR SALE sign on a lawn, garage behind | **Used** (scene 5). Plain sign, 720 × 1280. |
| `contract_7841865` | "CONTRACT" page and 2 pens on a desk | Spare. The body text needs a blur if used. |
| `leak_4159571`, `leak_6108991`, `ceiling_4882745` | Ceiling water into a bucket, peeling paint, collapsed ceiling | Spare. No line names a leak. |
| `junk_35421432`, `hole_32583498` | Barn storeroom, institutional corridor | Spare. They don't look like a rental. |
| `hole_26976625`, `hole_30213746` | Building demolition, excavator | Not a hole in a wall. Don't use. |
| `hole_4903222`, `leak_6813965`, `keys_7768205`, `keys_7817154`, `keys_7817160`, `keys_8293116`, `garage_*`, `table_*`, `yard_13126902` | People or hands in frame | **Don't use.** |

v2 needs no extra b-roll. The calendar clip v1 asked for is dropped, and the mortgage line runs over the house insert.

### Clip plan (Kie `gemini-omni-video`, 9:16, 1080p)

| Clip | Scenes | Words | Image | Prompt file | Duration | Credits (list) |
|---|---|---|---|---|---|---|
| 1 | 1-3 | 19 | `Ad17_JMSN_L1_front_door_v1.png` | `10_Video_Builds/Ad17_JMSN_Landlord/Ad17_video_prompt_clip1_front_door.txt` | 8 s | 105 |
| 2 | 4-6 | 18 | `Ad17_JMSN_L2_wall_hole_v1.png` | `..._clip2_wall_hole.txt` | 8 s | 105 |
| 3 | 7-8 | 23 | `Ad17_JMSN_L3_ceiling_leak_v1.png` | `..._clip3_ceiling_leak.txt` | 10 s | 126 |
| | | **60** | | | | **336** |

- **Scene images:** 3 × 18 credits (nano-banana-pro, measured on Ad 16) = 54.
- **Total at list price: 390 credits = $1.95** (336 for the clips = $1.68). **Nothing has been run.**
- **Each extra hook variant** re-makes clip 1 and clip 3: 105 + 126 = 231 credits = $1.155.
- **Omni lessons from Ad 16:** word-diff every clip against the script (Omni dropped a sentence at 22 words and repeated a phrase in the 10 s clip). Keep the prompt locked and change only the dialogue.

---

## Part D. Checks

| Check | Result |
|---|---|
| Kill checks (H1) | **6 pass, 1 borderline.** It doesn't announce itself. The curiosity has a benefit (you can leave too). The mechanism is held back until clip 3. It doesn't accuse him. The body pays off the hook. It asks only for a tap. **Copyable: borderline.** It names one moment (tenant gone), but any cash buyer could say it word for word; nothing in it is specific to Property Abundance. Hooks #4 and #6 were cut for being copyable with no moment at all. H1 stays because it carries the moment and scores 21, but a competitor could run it. |
| 7-point score | H1 21/28 · H2 21/28 · H3 20/28. All three keep. My judgment, not measured. |
| Loop order | OPEN A → payload → OPEN B → payload → CLOSE B → payload → CLOSE A → CTA. Nested, closing in reverse. No open-close back to back. The biggest payoff is on the last close. |
| Beat-by-beat claims | 1. You can leave too. 2. The house is empty and the mortgage keeps coming. 3. What's the move? 4. Re-renting bets on another tenant. 5. Fixing and listing means a commission. 6. Or sell it as-is. 7. Our offer is lower than a fixed-up sale. 8. You pay no commission and no fees. 9. That's how you leave too. No contradiction and no wander. |
| Claims vs. the confirmed list | As-is ✓ · offer lower than a fixed-up sale ⚠ (used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm) · no commission ✓ · no fees ✓ · no obligation ✓ (end card). "We buy it ourselves" is no longer used. No number, price, timeline, speed, scarcity, offer math, occupied purchase, eviction or legal line. |
| Quotes on screen | None. The Part A quotes shaped the lines but are never shown or voiced. |
| Step 5 body rules | First line is 7 words ✓. It opens on his situation ✓. It is dimensionalized: the empty house, the monthly mortgage, the hole he points at ✓. The alternatives are named ✓. The top worry (lowball) is raised by the admission ✓. There is an honest admission, as its own sentence in the Ad 16 final's wording ✓ (claim to confirm, see Part A). You vs. we is 75/25 (target 80/20, close). No proof sits next to the claims ✗: none exists yet, so the landing page must carry it. |
| **Step 6 CTA** | **Partial.** One action: spoken "Tap below.", then the end card ASK FOR MY OFFER · NO OBLIGATION. It is first person, says what the tap does (asks for an offer) and is free with no obligation, all without a new claim. The platform button should match: Learn More, or Get Quote if the page is a quote form (`copy-banks.md` CTA table; Meta's button list was not checked live). **Gaps:** no proof comes before the CTA (none exists yet), and the destination page returns HTTP 403, so "what happens next" can't be stated more precisely than "ask for my offer" until the page and its form are live. |
| Step 8 compliance | It names the situation (tenant gone, house empty), never a trait of the person. No AI or dramatization label is needed, because JMSN speaks only as the company. No words in any AI image or video prompt. The images carry no hints about who the tenant was (Part C). **Meta's Housing Special Ad Category must be set when the campaign is created, and it limits targeting.** The project rule says to expect targeting to be stripped, which is why this ad speaks to one situation (`03_Ad_Scripts_and_Briefs/Property_Abundance_UGC_Set_ReelDirection_v1.md`, "Before any of this runs", item 5). Meta's own policy page was not loaded this session. |
| Temperature | Blunt, calm and competent, with no sympathy (Hook Map: "He wants competence, not comfort"). The landing page and the first text must match. |
| Read-aloud | Done on all 13 sentences. The v1 fail ("We buy it ourselves, for LESS...") is gone, and "House sits empty" became "House is sitting empty". The humanizer skill was not loaded. |
| Language gate | Zero em dashes, zero banned phrases (grep run). |

### Claims flagged for review
1. **"Same mortgage, every month."** Keep it. The review found it states the house's carrying cost, with no "you" and no distress word. The fallback "The bills don't stop." is only for a Meta rejection. The caption must never become "YOUR MORTGAGE".
2. **"Our offer's LOWER than a fixed-up sale."** Status: used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm. It is the Ad 16 final's wording. It compares the price, not the seller's net. "But you pay no commission, no fees" invites a net comparison, the same shape as the Ad 15 v2 script. Don't make it stronger.
3. **"pay commission"** is a general statement about listing, with no rate or number. Low risk.
4. **The tenant's leftovers.** The trash bags and broken chair in L1 and L2 are picture only. No line or text says the owner can leave the tenant's things behind, because abandoned-property rules vary by state.
5. **"ASK FOR MY OFFER"** promises only a request, not an offer on every house and not a timeline.

### Blockers
- **propertyabundanceusa.com still returns HTTP 403** (last recorded in CLAUDE.md). The CTA has nowhere to go. Fix it before any spend.
- **Second click:** a name search finds the UK "Property Abundance" training company first (research doc). Plan the proof page and the brand check before scaling.
- Prompt files for all 3 clips carry the v2 dialogue (synced 2026-09-27).
