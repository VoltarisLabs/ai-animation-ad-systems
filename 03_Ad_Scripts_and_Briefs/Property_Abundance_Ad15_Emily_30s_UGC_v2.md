# Property Abundance: Ad 15, 30 s UGC (v2)

*Written 2026-09-25. The user approved this script the same day. Untested. It replaces `Property_Abundance_Ad15_Emily_OnlyThing_30s_v1.md`, which had Emily speaking as a seller behind an AI label.*

- **Speaker:** Emily (the AI avatar in `12_AI_Characters/Emily/`) talks to her phone as the voice of Property Abundance ("we"). She never says she sold a house, so the ad needs no "dramatization / not a real customer" label.
- **Audience:** the heir.
- **Structure:** nested loops. Open A → payload → Open B → payload → Open C → payload → Close C → payload → Close B → payload → Close A.
- **Length:** 94 words. The edge-tts draft voice (`en-US-AvaNeural`, rate +42%) runs at 199.1 wpm, and its last word ends at 28.42 s. That leaves 1.58 s for the end card.

## What the references do (all 9 vertical ads in `07_Assets/Reference_Ads/`, watched 2026-09-25)

Each ad was checked with a 1 fps contact sheet and a faster-whisper `small` transcript.

| Ad | Who talks | Where | Words / wpm |
|---|---|---|---|
| hall_of_fame_23s | The buyer ("I'll make you an all cash offer") | At a desk, dark room | 72 / 207.9 |
| quick_close_62s | The buyer ("I'm an actual buyer, not a wholesaler") | At a desk | 196 / 190.6 |
| bright_future_16s | The buyer ("we still want to make you an offer") | Standing at a run-down house | 51 / 212.8 |
| zion_fast_15s | The buyer ("we buy houses cash as is") | Standing on the street | 58 / 246.1 |
| cava_buys_34s | Owner, then a real customer | Green screen, then a webcam | 87 / 164.9 |
| housecashin_16s | Company presenter | Selfie indoors, with b-roll | 49 / 182.4 |
| clever_offers_16s | Company presenter ("the we buy houses guys aren't all the same") | Selfie in a car | 50 / 197.1 |
| sell_for_cash_27s | Posed as a seller ("the biggest mistake I made before selling my house") | Green screen, with b-roll | 105 / 233.0 |
| ref6_betterpath | Posed as a seller ("Fire your realtor! I did") | B-roll with an actor | 72 / 182.4 |

- **The shared pattern:** one person talking straight to a phone, with bold keyword captions, b-roll cutaways (the house, the rooms, the form on a phone), a spoken "click below", and a logo end card. The median pace is 197.1 wpm.
- **What this ad takes:** the buyer's-voice format of the first 7. Emily's car selfie matches clever_offers. hall_of_fame lists the same terms Property Abundance confirmed, and quick_close uses the "not a wholesaler" line.
- **What it doesn't take:** the posed-seller format of sell_for_cash and ref6. An undisclosed AI speaking as a real seller is a fake testimonial under the FTC rule (16 CFR 465.2).

## Script

| # | Beat | Spoken line | Time (draft) |
|---|---|---|---|
| 01 | **OPEN A** | "Inherited a house? Don't clean it out yet." | 0.10–2.13 |
| 02 | Payload | "Closet's still full. Hours away." | 2.13–4.19 |
| 03 | **OPEN B** | "Scared a cash buyer will lowball you?" | 4.19–5.74 |
| 04 | Payload | "Family can't agree." | 5.74–6.79 |
| 05 | **OPEN C** | "Truth? Cash offers usually come in lower than listing. Ours too." | 6.79–10.38 |
| 06 | Payload | "Listing usually means repairs, cleanout, commission, closing costs." | 10.38–13.58 |
| 07 | **CLOSE C** | "That's why lower isn't everything: we buy as-is, no commission, no closing costs." | 13.58–17.41 |
| 08 | Payload | "No wholesaling. We're the buyer." | 17.41–19.21 |
| 09 | **CLOSE B** | "That's why no lowball can trap you. No obligation. Show your family." | 19.21–22.66 |
| 10 | Payload | "You pick the closing date." | 22.66–23.84 |
| 11 | **CLOSE A** | "That's why you don't clean it out. Take what matters. Leave the rest. This is Property Abundance." | 23.84–28.42 |
| End card | | Logo, "TAP BELOW", the form | 28.42–30.00 |

## Loops

| Loop | Opens | Closes | Repeated words |
|---|---|---|---|
| A | 01 "Don't clean it out yet" | 11, last | "clean it out" |
| B | 03 "lowball you" | 09 | "lowball" |
| C | 05 "come in lower" | 07 | "lower" |

**Order check:** A(01) → B(03) → C(05) → close C(07) → close B(09) → close A(11). There is a payload between every step, and no loop opens and closes back to back.

## Truth check

| Line | Claim | Status |
|---|---|---|
| 01, 11 | You don't have to clean it out; leave the rest | Confirmed (belongings can stay) |
| 05 | "Cash offers usually come in lower than listing. Ours too." | Approved by the user on 2026-09-25 ("I agree with the script"). |
| 06 | What listing usually means | A general description of a listed sale |
| 07 | As-is, no commission, no closing costs | Confirmed |
| 08 | No wholesaling, we're the buyer | Confirmed |
| 09 | No obligation | Confirmed |
| 10 | You pick the closing date | Confirmed |

The ad makes no speed claim, no price claim and no claim that any customer came out ahead.

## Talking clips (Omni lengths 4, 6, 8 or 10 s)

| Clip | Lines | Speech (draft) | Omni length |
|---|---|---|---|
| 1 | 01–04 | 6.69 s | 8 s |
| 2 | 05–06 | 6.79 s | 8 s |
| 3 | 07–08 | 5.63 s | 6 s (0.37 s to spare) |
| 4 | 09–10 | 4.63 s | 6 s |
| 5 | 11 | 4.58 s | 6 s |

At Kie's list price that is 462 credits for one take of each clip. This is the list price, not a measured cost.

**Pace:** Emily has to talk at about 199 wpm, as fast as the references. If Omni delivers the lines slower, the ad runs past 30 s, so trim the gaps in the edit.

## Open items

- Meta and TikTok rules on labelling AI-generated people in ads were not checked this session.
- `12_AI_Characters/Emily/character.yaml` still describes Emily as "an heir who sold". Her role here is Property Abundance's presenter.
- `propertyabundanceusa.com` returns HTTP 403, so the "TAP BELOW" form won't work until it's fixed.

## Talking-clip dialogue with word stress (Kristian's method, 2026-09-25)

A word in capitals gets stressed. Three rules decided which words:
1. **Echo each loop.** The same word is stressed in a loop's open and in its close, so the viewer links the answer to the question.
2. **Only where natural stress would miss.** A word that normal speech already stresses stays lowercase. Too many capitals and she starts shouting.
3. **Never capitalise the brand or "as-is".** In capitals, the model may spell them out letter by letter.

| Clip | Dialogue | Why |
|---|---|---|
| 1 (lines 01–04, 8 s) | "INHERITED a house? DON'T clean it out yet. Closet's STILL full. Hours away. Scared a cash buyer will LOWBALL you? Family can't agree." | INHERITED = the callout, so the right person recognises themselves. DON'T = the warning that opens loop A and comes back in its close. STILL = the stuck feeling. LOWBALL opens loop B. "Agree" is stressed naturally. |
| 2 (05–06, 8 s) | "Truth? Cash offers usually come in LOWER than listing. OURS too. Listing usually means repairs, cleanout, commission, closing costs." | LOWER opens loop C. OURS lands the honest admission. The list stays flat and quick. |
| 3 (07–08, 6 s) | "That's why lower isn't EVERYTHING: we buy as-is, NO commission, NO closing costs. No wholesaling. WE'RE the buyer." | EVERYTHING is the twist that closes loop C. The two NOs subtract costs. WE'RE = the direct buyer. |
| 4 (09–10, 6 s) | "That's why no lowball can TRAP you. NO obligation. Show your family. YOU pick the closing date." | TRAP answers the fear from loop B. NO obligation is the reason. YOU hands control back to the seller. |
| 5 (line 11, 6 s) | "That's why you DON'T clean it out. Take what MATTERS. Leave the rest. This is Property Abundance." | DON'T mirrors the opening hook. MATTERS carries the emotion. The brand stays lowercase. |

15 capitalised words out of 94 (counted). No sentence has more than 3; the close of loop C (clip 3) has the most. While generating: if a word comes out shouted, lowercase it and generate again. If a word comes out flat, capitalise it and generate again. Lock clip 1 before generating clips 2 to 5.

These capitals are for the video prompt only. The on-screen captions use normal case.
