# Ad 16: JMSN house walkthrough, 30 s (v1)

**Speaker:** JMSN speaks as Property Abundance's buyer, in the company voice ("we"). He never plays a seller or a customer, so the ad needs no AI label.
**Format:** a walk-and-talk tour of a run-down house. Each clip is shot in a new spot and has one simple action. B-roll close-ups of the damage cut in over his voice.
**Method:** `kristian_jennings_ai_ugc_workflow`. Avatar prompts: `12_AI_Characters/JMSN/prompt_v2_house_walkthrough.md`.
**Claims used:** only the offer terms the user confirmed on 2026-09-25. Those are as-is, belongings can stay, no commission, no fees or closing costs, the seller picks the closing date, no obligation, and a direct buyer. The ad has no prices, no speed claims and no numbers.

---

## What the 9 vertical refs actually do (watched 2026-09-26)

Sources: 1 fps contact sheets (0.5 fps for the 62 s ad) and faster-whisper `small` transcripts of the 9 files in `07_Assets/Reference_Ads/`.

| Ref | Length | Where the presenter is | Moves? | Damage shown? |
|---|---|---|---|---|
| bright_future | 16.917 s | Standing on the step of a run-down house: debris, a broken step, a rusty rail. Full body, wide lens. | No. He spreads his arms on "if your house looks like this". | Yes, behind him |
| zion_fast | 14.633 s | Standing on a dry dirt lot with houses behind him. Full body. | No, only hand gestures | No |
| hall_of_fame | 23.593 s | Seated at a desk against a black background | No | No |
| quick_close | 62.133 s | Seated at an office desk, one camera the whole time | No | No |
| clever_offers | 15.720 s | Car selfie | No | No |
| housecashin | 16.600 s | Indoor selfie, then cut out over a suburban street, then indoors again | Only the background changes | No |
| cava_buys | 34.773 s (16:9) | Cut out over an aerial shot of houses, then a customer testimonial | No | No |
| sell_for_cash | 27.424 s | Same pose on the same background for the whole ad | No | Yes, as b-roll: a dated bathroom, a stained ceiling, a gutted basement |
| ref6_betterpath | 24.383 s | Nobody talks to camera. A montage (it includes cash, which our rules ban). | n/a | No |

**What this shows:**
- 0 of 9 have a presenter walking room to room. Each one talks from a single spot.
- The ads get their variety from cuts. They use b-roll cutaways (sell_for_cash, ref6) or a background swap (housecashin moves its presenter to 3 places).
- Damage appears in 2 of 9: behind the buyer in bright_future, and as b-roll in sell_for_cash.
- The refs don't show which presenters are AI. The sell_for_cash woman holds the same pose on the same background for 27 s, which fits a green screen or an avatar. That is not proof.

**So the walkthrough is new, not copied.** It takes three things from the refs:
- bright_future's "the buyer standing at a rough house";
- sell_for_cash's damage cutaways;
- housecashin's changes of location.

Kristian's "scene change" tip covers the rest: the same avatar in a new spot for each clip.

---

## Storyboard

Nested loops: A (the roof), B (the floor) and C (who would buy this) all open in clip 1. They close in reverse order: C in clip 2, B in clip 3, A in clip 4.

| # | JMSN says | On screen | Start image | Omni |
|---|---|---|---|---|
| 1 | "Look at this roof. SHOT. And the floor inside? WORSE. So who would EVER buy this house? Come look." | AI UGC: he walks slowly along the front walk and glances up at the roof. Cutaway on "roof": a roof close-up. | L1 front | 8 s |
| 2 | "WE would. As-is. We're the actual buyer, no middleman. Broken cabinets, old furniture, the junk? Leave ALL of it." | AI UGC in the kitchen. He points back at the hanging cabinet door. Cutaway on "cabinets" / "furniture". | L2 kitchen | 8 s |
| 3 | "Now this floor. You'd fix it BEFORE listing. With us you DON'T. No repairs, no commission, no closing costs." | AI UGC above the broken floor. He points down. Cutaway on "floor": broken boards. | L3 floor | 8 s |
| 4 | "And that roof? Not your problem. YOU pick the closing date. No obligation. Tap below. Tell us about it." | AI UGC back outside. He glances up at the roof and smiles. End card. | L1 front | 8 s |

Each line is 19 words, 76 words in total. At the 166.0 wpm measured on Emily's Omni clips 1-2, one line takes about 6.9 s, and the whole script takes about 27.5 s of speech. This is an estimate. JMSN's real pace is not measured yet. Each 8 s clip leaves a smile tail to trim.

**Edit** (per the merge-then-scenes rule):
1. Merge the 4 clips.
2. Cut at sentence ends.
3. Put object-only b-roll video under his voice, about 3 cuts per 10 s.

The stock in `07_Assets/Stock_Video/` has no close-ups of an American house roof, floorboards or kitchen cabinets. The `hole_` clips show an abandoned corridor and demolition. That b-roll still has to be found.

**Open:** the "Tap below" CTA needs `propertyabundanceusa.com` fixed first. It returned HTTP 403 on 2026-09-25.

---

## Omni settings (all 4 clips)

| Setting | Value |
|---|---|
| Model | `gemini-omni-video` (full Omni, not Flash) |
| Duration | `8` |
| Aspect | `9:16` |
| Resolution | `1080p` |
| Upload | 1 image: that clip's start image from the table above |
| Cost | 105 credits per clip at Kie's list price for 8 s at 1080p. Not measured. |

**The prompt is locked.** Only 3 slots change between clips: the place and action sentence, the light and room tone, and the dialogue. Lock clip 1 first. Generate it and judge it harshly. Add a rule for each problem. Only then run clips 2-4.

---

## Clip 1: front walk (image L1)

```
Handheld UGC iPhone front-camera selfie video. The man films himself at arm's length outside an old house that needs a lot of work. Use the uploaded image as the first frame: the same man, same face, same very short hair, thin mustache and light goatee, the same navy quarter-zip over a white t-shirt, the single white earbud and the small black clip-on mic, and the same house with the sagging roof, missing shingles and blue tarp. Natural hand shake only; the camera never cuts, never zooms and never flips to the back camera. He takes slow steps along the cracked front walk while he talks. The phone moves with him, so his face stays in the same place in the frame and the house slides slowly past behind him. On "Look at this roof" he glances up over his shoulder at the roof for one second, then looks back into the lens. Apart from that one glance he keeps eye contact with the lens. His mouth moves naturally with every word, his head moves a little, natural blinks and small eyebrow raises. Energy: high, warm and confident, fast-talking like a local house buyer on TikTok giving a straight answer. Expressive, but never shouting. Flat overcast daylight. Audio: only his voice, close and clear from the clip-on mic, with light outdoor wind and distant birds.

He says: "Look at this roof. SHOT. And the floor inside? WORSE. So who would EVER buy this house? Come look."

Rules:
- One continuous take, no jump cuts.
- Fast pace: the whole line takes about 7 seconds, with no long pauses between sentences.
- After the last word he holds a small, relaxed smile until the clip ends.
- A natural Black American man in his late twenties.
- Say only the dialogue above. Do not add, repeat or skip any word.
- Words in capitals get extra stress, spoken at normal volume, never shouted.
- His face, hair, clothes and accessories stay exactly as in the image for the whole clip.
- The house stays exactly as it is: no damage appears, grows, moves or disappears.
- The phone is never seen. His hands stay out of frame.
- No other people.
- No text, captions, subtitles, signs, logos or watermark on screen.
- No music, no sound effects.
```

## Clip 2: kitchen (image L2)

```
Handheld UGC iPhone front-camera selfie video. The man films himself at arm's length inside an old house that needs a lot of work. Use the uploaded image as the first frame: the same man, same face, same very short hair, thin mustache and light goatee, the same navy quarter-zip over a white t-shirt, the single white earbud and the small black clip-on mic, and the same kitchen with the cabinet door hanging off its hinge. Natural hand shake only; the camera never cuts, never zooms and never flips to the back camera. He stands still in the kitchen. On "Broken cabinets" he raises his free hand, points back over his shoulder at the cabinet door hanging off its hinge, then lowers his hand. Apart from that one point he keeps eye contact with the lens. His mouth moves naturally with every word, his head moves a little, natural blinks and small eyebrow raises. Energy: high, warm and confident, fast-talking like a local house buyer on TikTok giving a straight answer. Expressive, but never shouting. Grey window daylight mixed with one bare warm ceiling bulb. Audio: only his voice, close and clear from the clip-on mic, with the slight hollow echo of an empty room.

He says: "WE would. As-is. We're the actual buyer, no middleman. Broken cabinets, old furniture, the junk? Leave ALL of it."

Rules:
- One continuous take, no jump cuts.
- Fast pace: the whole line takes about 7 seconds, with no long pauses between sentences.
- After the last word he holds a small, relaxed smile until the clip ends.
- A natural Black American man in his late twenties.
- Say only the dialogue above. Do not add, repeat or skip any word.
- Words in capitals get extra stress, spoken at normal volume, never shouted.
- His face, hair, clothes and accessories stay exactly as in the image for the whole clip.
- Every object stays exactly where it is: the cabinet door does not swing, fall or fix itself, and nothing appears or disappears.
- The phone is never seen. His free hand enters the frame only for the one point, then leaves.
- No other people.
- No text, captions, subtitles, signs, logos or watermark on screen.
- No music, no sound effects.
```

## Clip 3: broken floor (image L3)

```
Handheld UGC iPhone front-camera selfie video. The man films himself inside an old house that needs a lot of work. Use the uploaded image as the first frame: the same man, same face, same very short hair, thin mustache and light goatee, the same navy quarter-zip over a white t-shirt, the single white earbud and the small black clip-on mic, and the same living room with the broken floorboards. Natural hand shake only; the camera never cuts, never zooms and never flips to the back camera. He holds the phone a little above his head, tilted down, so the broken floorboards in front of his feet stay in the lower part of the frame. He stands still on solid floor. On "Now this floor" he points down at the broken boards with his free hand, then lowers his hand and looks back into the lens. Apart from that one point he keeps eye contact with the lens. His mouth moves naturally with every word, his head moves a little, natural blinks and small eyebrow raises. Energy: high, warm and confident, fast-talking like a local house buyer on TikTok giving a straight answer. Expressive, but never shouting. Grey window daylight. Audio: only his voice, close and clear from the clip-on mic, with the slight hollow echo of an empty room.

He says: "Now this floor. You'd fix it BEFORE listing. With us you DON'T. No repairs, no commission, no closing costs."

Rules:
- One continuous take, no jump cuts.
- Fast pace: the whole line takes about 7 seconds, with no long pauses between sentences.
- After the last word he holds a small, relaxed smile until the clip ends.
- A natural Black American man in his late twenties.
- Say only the dialogue above. Do not add, repeat or skip any word.
- Words in capitals get extra stress, spoken at normal volume, never shouted.
- His face, hair, clothes and accessories stay exactly as in the image for the whole clip.
- Every board stays exactly as it is: nothing breaks further, moves, fixes itself, appears or disappears. He never steps onto the broken boards.
- The phone is never seen. His free hand enters the frame only for the one point, then leaves.
- No other people.
- No text, captions, subtitles, signs, logos or watermark on screen.
- No music, no sound effects.
```

## Clip 4: back outside (image L1)

```
Handheld UGC iPhone front-camera selfie video. The man films himself at arm's length outside an old house that needs a lot of work. Use the uploaded image as the first frame: the same man, same face, same very short hair, thin mustache and light goatee, the same navy quarter-zip over a white t-shirt, the single white earbud and the small black clip-on mic, and the same house with the sagging roof, missing shingles and blue tarp. Natural hand shake only; the camera never cuts, never zooms and never flips to the back camera. He stands still on the cracked front walk. On "And that roof?" he glances up over his shoulder at the roof for one second, then looks back into the lens. Apart from that one glance he keeps eye contact with the lens. His mouth moves naturally with every word, his head moves a little, natural blinks and small eyebrow raises. Energy: high, warm and confident, fast-talking like a local house buyer on TikTok giving a straight answer. Expressive, but never shouting. Flat overcast daylight. Audio: only his voice, close and clear from the clip-on mic, with light outdoor wind and distant birds.

He says: "And that roof? Not your problem. YOU pick the closing date. No obligation. Tap below. Tell us about it."

Rules:
- One continuous take, no jump cuts.
- Fast pace: the whole line takes about 7 seconds, with no long pauses between sentences.
- After the last word he holds a small, relaxed smile until the clip ends.
- A natural Black American man in his late twenties.
- Say only the dialogue above. Do not add, repeat or skip any word.
- Words in capitals get extra stress, spoken at normal volume, never shouted.
- His face, hair, clothes and accessories stay exactly as in the image for the whole clip.
- The house stays exactly as it is: no damage appears, grows, moves or disappears.
- The phone is never seen. His hands stay out of frame.
- No other people.
- No text, captions, subtitles, signs, logos or watermark on screen.
- No music, no sound effects.
```

---

## Cost (Kie list prices, nothing run yet)

| Item | Count | Credits each | Credits | $ (1 credit = $0.005) |
|---|---|---|---|---|
| Nano Banana Pro avatar images, 2K 9:16 | 3 | 18 (measured at 3:4) | 54 | 0.27 |
| Gemini Omni clips, 8 s 1080p | 4 | 105 (list price) | 420 | 2.10 |
| **Total, one take each** | | | **474** | **2.37** |

The last measured balance was 3,981 credits (2026-09-26, Ad 15 session). Retakes cost extra.
