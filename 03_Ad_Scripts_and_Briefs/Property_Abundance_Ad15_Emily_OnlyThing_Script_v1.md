# Property Abundance: Ad 15 "The Only Thing I Took" (script v1)

*Written 2026-09-25. Untested.*

- **Pipeline:** script (this file) → storyboard → reference frame → avatar image → talking clips → edit.
- **Audience:** Emily "The Heir" (buyer avatar 1): an inherited house hours away, grief, a sibling who disagrees.
- **Speaker:** Emily, the AI character (`12_AI_Characters/Emily/`), talking to camera. She plays an heir who sold her mom's house, as a dramatization.
- **Structure:** nested loops. Open A → payload → Open B → payload → Open C → payload → Close C → payload → Close B → payload → Close A → CTA.
- **Length:** 240 words. The draft voice runs 95.65 s (edge-tts `en-US-AvaNeural`, rate -6%, 0.35 s gaps, 158.1 wpm). Re-time after the real talking clips.

## Required on screen for the whole ad

> AI-generated character. Dramatization. Not a real customer.

Emily speaks as a seller, so the FTC rules apply. Under 16 CFR 255.2(c), an actor shown as a customer needs a clear disclosure. Under 255.2(b), what she describes is read as the typical result. So she only mentions terms the business gives every seller.

## Facts this script is allowed to use

The owner confirmed these on 2026-09-25:

| Term | Used in |
|---|---|
| Buys as-is (no repairs) | 07 |
| Belongings can stay (no clean-out) | 01, 07, 11a |
| No commission | 07 |
| No fees or closing costs | 07 |
| Seller picks the closing date | 10 |
| No obligation | 09, 12 |
| Property Abundance buys the house itself (no wholesaling) | 08 |

**Not confirmed, so not used:** showing the seller how the offer is built, any offer or closing speed, any price or net-proceeds comparison.

## The script

| # | Beat | Spoken line | Draft time | Omni clip |
|---|---|---|---|---|
| 01 | **OPEN A** | "This is the only thing I took out of my mom's house. I didn't even empty her closet." *(holds up a chipped coffee mug)* | 0.00–5.54 | 6 s |
| 02 | Payload | "She lived three hours away. Every weekend I drove down, opened that closet, and shut it again." | 5.89–13.09 | 8 s |
| 03 | **OPEN B** | "My real fear? I was so tired, I'd take whatever anyone offered." | 13.44–18.82 | 6 s |
| 04 | Payload | "My brother wouldn't pay for repairs. And he said a cash buyer meant giving it away." | 19.17–24.55 | 6 s |
| 05 | **OPEN C** | "He wasn't wrong about one thing. As-is cash offers usually come in lower than a fixed-up listing." | 24.90–31.38 | 8 s |
| 06a | Payload | "But selling it fixed up meant repairs first. Emptying every room." | 31.73–36.33 | 6 s |
| 06b | Payload | "Commission. Closing costs. Then waiting on a buyer, three hours from home." | 36.68–42.71 | 8 s |
| 07 | **CLOSE C** | "That's why the lower offer wasn't the whole story. No repairs. No emptying the house. No commission. No closing costs." | 43.06–52.49 | 10 s |
| 08 | Payload | "And they bought it themselves. Nobody handed Mom's house off to another investor." | 52.84–58.26 | 6 s |
| 09 | **CLOSE B** | "That's why being tired didn't make me take whatever was offered. No obligation. My brother saw the number first." | 58.61–66.05 | 8 s |
| 10 | Payload | "We picked the closing date. After my brother flew in, so we could walk through her house together one last time." | 66.40–73.41 | 8 s |
| 11a | **CLOSE A** | "That's why this is the only thing I took out of my mom's house. Her things could stay, closet and all. I didn't have to be the one who emptied it." | 73.76–83.05 | 10 s |
| 11b | **CLOSE A** | "She had her coffee in this every morning. This, I kept. The house, I sold to Property Abundance." | 83.40–90.50 | 8 s |
| 12 | CTA | "If you're where I was, ask them for a number. You can still say no." | 90.85–95.65 | 6 s |

Omni clip length is the shortest of 4, 6, 8 or 10 s that fits the line with 0.4 s to spare. Where a line falls between two lengths, use Kristian's padding trick: add a few throwaway words at the end, generate the longer clip, and cut the extra words in the edit.

**Word stress for the talking clips** (Kristian's method puts the stressed word in capitals in the video prompt): 01 ONLY, 03 WHATEVER, 05 LOWER, 07 WHOLE, 09 TIRED, 11a ONLY, 11b KEPT.

## What each loop does

| Loop | Opens (line) | The viewer wonders | Closes (line) | The answer |
|---|---|---|---|---|
| A | 01, the mug and the full closet | Why only that? How do you sell a house full of her things? | 11a–11b, last | Her things could stay, so she wasn't the one who emptied the house. She kept the mug and sold the house. The brand comes last. |
| B | 03, "I'd take whatever anyone offered" | Did someone take advantage of her being tired? | 09 | No obligation. Her brother saw the number first. |
| C | 05, "cash offers usually come in lower" | Then why take it? | 07 | What a listing costs you (repairs, clean-out, commission, closing costs) doesn't come out of this offer. |

**Order check:** A(01) → B(03) → C(05) → close C(07) → close B(09) → close A(11). There is a payload between every step. No loop opens and closes back to back, and another loop is still open at every close. Each close starts with "That's why" and repeats the words of its own open ("lower offer", "tired / take whatever", "the only thing I took out of my mom's house").

## Truth check

| Line | Claim | Status |
|---|---|---|
| 01, 07, 11a | Her things could stay, no emptying the house | Confirmed (belongings can stay) |
| 05 | As-is cash offers *usually* come in lower than a fixed-up listing | General industry statement, not a company term. It works against the company's own interest, so it cannot overstate. Cut it if you don't want to say it. |
| 06a–06b | Selling fixed up means repairs, emptying the house, commission, closing costs and waiting for a buyer | A description of a normal listed sale |
| 07 | No repairs, no commission, no closing costs | Confirmed |
| 08 | They bought it themselves | Confirmed (no wholesaling) |
| 09, 12 | No obligation, you can say no | Confirmed |
| 10 | We picked the closing date | Confirmed |
| 02, 04, 10, 11b | Three hours away, the brother, the mug | Story details inside a labelled dramatization. No price, speed or result claim. |

Emily never says the offer was fair, high or quick, and never says she came out ahead. Those would be result claims that nothing confirms.

## Hook score (the Hook Map rubric, my scoring)

Open A: self-recognition 2 (the closet trigger), emotional precision 2 (the unspoken wish not to empty it), trust posture 1, specificity 2, truth 2. **Total 9/10.** The first draft ("This is the only thing I took out of my mom's house.") scored 6 and was rewritten.

**Language gate (`reel_direction_2` rules):** 0 em dashes, 0 banned phrases, 6.91 words per sentence. Flesch-Kincaid grade 2.7, under the grade 7 limit. The grade is an estimate: the syllables were counted by a regex, not a dictionary. The skill's QUESTION/HOOK/EXPLAIN format was not used, because this ad follows the nested-loop order you asked for.

## What this is built from

**The 4 picked reference ads** (`07_Assets/Reference_Ads/Reference_Videos_for_House_Buying.md`):
- **One idea per ad.** Here the idea is: keep the one thing that matters, let the house go.
- **Show the pain, don't list it.** The pain comes as moments (the drive, the closet shut again). The only list is in line 07, where it pays off loop C.
- **Calm, trusted ending.** No urgency, and the last spoken words are "You can still say no."
- **The real-seller format (r05) is on hold** until real sellers exist. This ad is the labelled dramatization version of it.

**Where this script departs from them:** they are 15–30 s TV spots with 23–75 words. A full A-B-C nest needs time (Howie: 30 s is too short). The mug in the first frame carries the hook visually instead.

**Your Ad10–Ad14:**
- **Kept:** the closet and drive trigger moments, the "That's why" closes, and the self-incriminating "a cash offer is lower" line (Ad12, line 10). The mug is the Ad14 jar idea turned into a prop Emily can hold on camera. Swap the jar back in if you prefer; the lines work with any object.
- **Removed:**
  - "We show you the math first" (Ad12 clip 17, Ad13 block 5, Ad14 line 8). You said this isn't done today, so those lines can't run as written.
  - "The lower number can still leave you with more" (Ad12, Ad13). This is a result claim that can't be shown.
  - "No more months of taxes" (Ad12, Ad13). It implies a closing speed nobody has confirmed.
- **Changed:** the voice. It was a narrator over b-roll; now it is a first-person avatar who has already solved the problem. This is Kristian's authority rule.

## Open items

1. **The website is still down.** On 2026-09-25, `propertyabundanceusa.com` returned HTTP 403 "No application found", and curl failed TLS verification ("unable to get local issuer certificate"). The CTA needs a working form first.
2. **Length.** The draft runs 95.65 s. A 60 s cut is possible if you drop payloads 04 and 08 and shorten 06, but loop B loses the brother.
3. **Line 05.** Confirm you're happy saying that as-is cash offers usually come in lower.
4. **Next step:** the storyboard. It sets the frame per line: "AI UGC" (Emily) or b-roll, captions of 2–3 keywords, and the mug prop.
