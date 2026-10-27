# Ad 18 v5: v4 with a positive hook

Written 2026-09-28, after the user's note on v4: "start the hook with something positive."

- **Base:** `Ad18_SCRIPT_v4_R1_remake.md`, the line-by-line remake of R1. It is unchanged; this file is a new version.
- **What changed:** only the hook (line 1), and line 2, which the new hook forced (§3). Every other line is word for word v4.
- **Status:** nothing generated, no Airtable row. All times are estimates (word count × 60 / 176) until the voice exists.

**The evidence for a gain frame** (`04_Audience_Research/Ref_Ads_Research.md` §2, §11):
- A loss frame ("Don't…") is not proven better. The meta-analysis has gain-framed appeals slightly *more* persuasive (r = .03).
- Meta names Value Promise as a Reel hook type. R1's own hook is a value promise ("bonus cash"), even though it opens with "Don't".
- Two references open with a positive line:
  - R4: "This house sold for cash in eight days."
  - R5: "Wait, I can buy your house."

**Rule conflict:** `reel_direction_2` says "pain-first". The user's instruction overrides it here.

---

## 1. Positive hook options

Every option has 8 words, so it ends at 2.73 s at 176 wpm and the first cut falls at 2.73 s. Each word lasts 0.3409 s. None starts with a negation or a question.

| # | Hook | Words | Ends | First money word | Money at stake | Reference hook type | Interesting + profitable (1-10) |
|---|---|---|---|---|---|---|---|
| **H1** | **Cash for your house. Pay nothing to sell.** | 8 | 2.73 s | "Cash" 0.00 s | Cash, and no commission, fees or closing costs | Value Promise (Meta). R1's first picture is the payoff (a bed of cash), and R4 says "cash" early. This version is gain-framed. | **8** |
| H2 | I'll pay cash for your house. Mess included. | 8 | 2.73 s | "pay" 0.34 s | Cash, as it is, with the belongings left in | Statement of Intent (R5 "I can buy your house.") plus a twist | 7 |
| H3 | You pick the day your house becomes cash. | 8 | 2.73 s | "cash" 2.39 s | Cash, on a closing date the seller picks | Value Promise plus control. No reference uses it, because they all claim speed instead. | 7 |
| H4 | Your house for my cash. You pay nothing. | 8 | 2.73 s | "cash" 1.36 s | Cash, plus paying nothing | Direct offer (R3's "Send me your address…" is a direct ask) | 6 |
| H5 | Leave everything in your house. I'll pay cash. | 8 | 2.73 s | "pay" 2.05 s | Cash, and belongings can stay | Permission plus value (R5: "You can even leave things behind") | 6 |
| H6 | Get paid cash for your house. Pay nothing. | 8 | 2.73 s | "paid" 0.34 s | Cash, plus paying nothing | Value Promise, with "paid / pay nothing" as the contrast | 7 |

**Weak points:**
- **H2:** "Not one dime." no longer pays off the hook. Line 5 answers "Mess included" at 10.57 s, which is an early close. And "mess" may sting an heir whose parents' belongings are in the house.
- **H3:**
  - It is the most original option, but line 9 ("you pick the closing date") becomes its payoff. The loop labels would have to be rebuilt, which goes beyond the changes the brief allows.
  - The claims grep flags the word "day". Here it means the seller's chosen date, not a speed claim.
  - "Cash" arrives late (2.39 s).
- **H4 and H6:** "Pay nothing" without "to sell" is broader than the confirmed terms. It can be read as covering the mortgage payoff too.
- **H5:** the money arrives late, and it opens on the clean-out angle that v1 was rejected for.

## 2. The pick: H1

"Cash for your house. Pay nothing to sell."
- **The money comes first.** The first word is the money itself, spoken at 0.00 s over R1's cash shot. "Pay nothing to sell" is the confirmed-safe form of the offer (no commission, no fees, no closing costs).
- **v4's structure still works.** "Not one dime." at 36.82 s still closes the hook's loop ("how can selling cost nothing?") on the cash picture, so no later line had to change.

---

## 3. Lines changed vs v4

| # | v4 | v5 | Why |
|---|---|---|---|
| 1 | Don't pay a dime to sell your house. (8 words) | Cash for your house. Pay nothing to sell. (8 words) | The user asked for a positive start. The first word is now a gain. |
| 2 | I can pay cash for your house myself. No realtor. No middleman. (12 words) | You deal straight with me. No realtor. No middleman. (9 words) | **Forced.** v4's line 2 would repeat "cash for your house" word for word, 2.73 s after the hook said it. "Deal straight with me" plus "No middleman" keeps the confirmed term that Property Abundance buys the house itself. Cash is already said at 0.00 s. |
| 3-12 | unchanged | unchanged | |

The CLOSE A callback "Not one dime." is **not** changed: it still pays off "Pay nothing to sell". What is lost is the exact word echo, "dime" in both the hook and the close.

The totals drop by 3 words and 1.02 s: from 136 words and 46.36 s to 133 words and 45.34 s.

---

## 4. The script

133 words. At JMSN's 176 wpm: 45.34 s. At R1's own 214.9 wpm: 37.13 s.

```text
[OPEN A]   Cash for your house. Pay nothing to sell.
           SHOW → R1 shot 1: a pile of $100 bundles, handheld, looking down (stock cash100_6266433). JMSN's voice over it.
[payload]  You deal straight with me. No realtor. No middleman.
           SHOW → R1 shot 2: a cluttered, run-down room, slow handheld drift (stock junk_35421432). Cut at 2.73 s.
[payload]  I buy houses exactly the way they sit.
           SHOW → R1 shot 3: JMSN, arm's-length front-camera selfie, walking a leafy residential sidewalk, overcast, background always moving.
[payload]  Any condition, any mess, any age.
           SHOW → one quick insert per word: collapsed ceiling (ceiling_4882745) → old unmade bed (bed_17041569) → old house behind a broken fence (yard_18854299).
[payload]  You don't have to fix it, scrub it, or even clear it out if you'd rather not.
           SHOW → back to JMSN walking, counts three on his fingers. On "clear it out", cut to a packed clothes rail (closet_8844337).
[OPEN B]   If that's what you need, let me make you a cash offer. No obligation.
           SHOW → JMSN walking, open palms on "No obligation".
[CTA 1]    Just tap the button under this video to start.
           SHOW → R1 shot 4: a fingertip tapping a phone, dark background, screen turned away from the lens (NEEDS CLIP).
[CLOSE B]  All you do is answer a few quick questions about the house, and I'll work up your offer.
           SHOW → R1 shot 5: JMSN walking, points down on "questions".
[payload]  And you pick the closing date. Your calendar, not mine.
           SHOW → R1 shot 6: a hand signing a paper with a pen, top-down (table_7735907).
[CLOSE A]  No realtor. No commission. No fees. No closing costs. Not one dime.
           SHOW → the pen shot holds through "closing costs". On "Not one dime." cut back to cash (cash100_6266251, hands counting bills): the hook's first word and picture close its loop.
[payload]  So don't sit on it.
           SHOW → R1 shot 7: JMSN walking, then stops, eyes on the lens.
[CTA 2]    Hit that button down below. Tell me about the house and see what I'd pay for it.
           SHOW → same shot, points down on "button" → logo end card.
```

Every SHOW line is v4's. The only change is the note on the CLOSE A cash shot, which now calls back the hook's first word.

**Captions:** R1's style, as in v4. The hook reads CASH / FOR YOUR HOUSE, then PAY NOTHING / TO SELL, with "CASH" and "NOTHING" in green. No top banner.

**Loops, nested A-B-B-A:**

| Time | Beat | Line |
|---|---|---|
| 0.00 s | OPEN A | the hook |
| 16.36 s | OPEN B | "let me make you a cash offer" |
| 24.20 s | CLOSE B | "All you do is answer a few quick questions" |
| 33.75 s | CLOSE A | the cost list; "Not one dime." lands at 36.82 s on the cash shot |

- **A:** the hook opens "how can selling cost nothing?". The script answers it in steps:
  - no realtor or middleman at 2.73 s;
  - as it is from 5.80 s;
  - no clean-out at 13.98 s;
  - the full list at 33.75 s.
- **B:** opens and closes with CTA 1 between, while A is still open.
- **CTA 2:** "see what I'd pay for it" also calls back the hook's "Cash for your house".

---

## 5. Shots and Omni clips (at 176 wpm, estimates)

| Time | Shot (R1's shot) | First word of the shot | Omni clip |
|---|---|---|---|
| 0.00-2.73 | cash pile (1) | Cash | C1 |
| 2.73-5.80 | run-down room (2) | You | C1 |
| 5.80-8.52 | JMSN walking (3) | I | C2 |
| 8.52-10.57 | ceiling → bed → old house, 0.68 s each | Any | C2 |
| 10.57-13.98 | JMSN walking (3) | You | C3 |
| 13.98-16.36 | closet | clear | C3 |
| 16.36-21.14 | JMSN walking (3) | If | C4 |
| 21.14-24.20 | finger tap (4) | Just | C4 |
| 24.20-30.34 | JMSN walking (5) | All | C5 |
| 30.34-36.82 | pen signing (6) | And | C6 |
| 36.82-37.84 | cash, callback | Not | C6 |
| 37.84-45.34 | JMSN walking (7) → end card | So | C7 |

- **Cuts:** 14 shots and 13 cuts, 2.87 per 10 s (v4: 2.80; R1: 1.40). Every cut falls on a sentence start except the closet cut at "clear". That one is v4's mid-sentence insert, on the word it shows.
- **Clip joins:** all 6 land on a cut to or from b-roll, the same as v4.
- **JMSN's face on screen:** 72 words = 24.55 s of 45.34 s = 54.1% (v4: 52.9%; R1: 63.5%).

| Clip | Length | Words | Lines | Credits (list) |
|---|---|---|---|---|
| C1 | 8 s | **17** | 1-2 (audio only, under b-roll) | 105 |
| C2 | 8 s | 14 | 3-4 | 105 |
| C3 | 8 s | 17 | 5 | 105 |
| C4 | 10 s | 23 | 6-7 | 126 |
| C5 | 8 s | 18 | 8 | 105 |
| C6 | 10 s | 22 | 9-10 | 126 |
| C7 | 10 s | 22 | 11-12 | 126 |

- **Talking clips:** 7 clips, 798 credits = $3.99 at Kie's Omni list price (1080p, 9:16). Not measured, not run. This is unchanged from v4: C1 got shorter but still needs 8 s, because 17 words at 176 wpm take 5.80 s.
- **Start frame:** 1 Nano Banana Pro still, 18 credits = $0.09. Unchanged from v4.
- **B-roll:** the same files as v4. They were frame-checked there on 2026-09-28 and were not re-checked for v5. The finger tap is still NEEDS CLIP.
- **Word-diff every clip** against this script after generation.

---

## 6. Checks

| Check | Result |
|---|---|
| First word is positive, not a negation or a pain question | PASS: "Cash" |
| First word at 0.00 s, hook 3 s or less | PASS: 8 words, 2.73 s |
| Money in the first line | PASS: "Cash" at 0.00 s, "Pay nothing" at 1.36 s |
| "You" plus the house, in one breath | PASS: "your house", word 3-4 (0.68 s) |
| Offer word by 4.5 s | PASS: "cash" at 0.00 s (v4: 3.75 s) |
| First cut at 2.5-2.8 s | PASS: 2.73 s, at the start of "You deal…" (R1: 2.60 s) |
| C1 at 21 words or fewer | PASS: 17 |
| Line 2 doesn't repeat the hook | PASS: "cash" is said once in lines 1-2 |
| CTA 1 at 30-60%, CTA 2 at the end, both naming steps | PASS: CTA 1 at 46.6% (R1: 48.1%); CTA 2 is the last line |
| Confirmed terms, each on its own line | 7 of 7:<ul><li>cash buyer (lines 1, 6);</li><li>no commission, fees or closing costs (summed up in line 1, listed in line 10);</li><li>buys it itself / no middleman (line 2);</li><li>as it is (lines 3-4);</li><li>belongings can stay (line 5);</li><li>no obligation (line 6);</li><li>the seller picks the closing date (line 9).</li></ul> |
| No speed, bonus, scarcity or result claim | **1 flag.** The claims grep hit "quick" in line 8 ("a few quick questions"), which is unchanged from v4. It describes the questions, not the sale, but "quick" is on the never-claim list. |
| "ugly" / WE BUY UGLY HOUSES | PASS: 0 hits |
| Language gate (em dashes, banned filler) | PASS: 0 hits on the 12 spoken lines |
| Loop order | PASS: nested A-B-B-A; the biggest payoff ("Not one dime.") is on the last close |
| No person shown as our seller | PASS: JMSN only; the b-roll is objects and places |
| Could a competitor run the hook word for word? | Yes (borderline). The same is true of every reference hook, because plain offer hooks are copyable by design. |
| Deal stated by about 13 s | PASS: cash and "pay nothing to sell" by 2.73 s; no realtor or middleman by 5.80 s; as it is by 10.57 s. The itemised costs come at 33.75 s, where R1 puts them. |

## 7. Watch-outs

- **"Pay nothing to sell"** carries v4's risk. It rests on the confirmed no commission, no fees and no closing costs. If any cost can land on the seller at closing (for example, a transfer tax that a state puts on the seller by law), the hook must change.
- **"quick" (line 8)** can become "a few simple questions" (R1's own word), if a zero-hit grep matters more than keeping line 8 word for word. It was not changed, because the brief keeps lines 3-12 as they are.
- **"Cash for your house"** is a common descriptive phrase. No trademark search was run on it. HomeVestors' "WE BUY UGLY HOUSES" is not used.
- **The landing page** (propertyabundanceusa.com) still fails, as v4 notes: 403 over http, a certificate error over https (measured 2026-09-27).
- **Pace:** 45.34 s at 176 wpm is 2.46 s longer than R1 (42.88 s). Ask Omni for a brisk delivery.
