# Ad 18 v12: Ava, full video plan (v11 script + R5's visuals)

Written 2026-09-29. The user: "you have to do the complete video. With all the payload and visuals… similar visuals to [ref_1.mp4]… the house in her background… a drone shot… boxes with multiple [people] packing or moving… for the first hook and the last hook… inside the house… logos [for] the commission… not stuck to her face all the time… make it look real, not like an AI." A faster delivery is fine (the user will slow it down).

- **Script:** v11, word for word (162 words). The user pasted the v10 wording of two lines; v11 replaced them at the user's request, so v11 is used.
- **Presenter:** Ava v2_a (`12_AI_Characters/Ava/Ad18_Ava_avatar_v2_a.png`), picked 2026-09-29.
- **Why 7 talking clips, not 3:** an Omni clip holds about 19-21 words in 8 s and 25 in 10 s (measured on Ad 16). Three clips hold about 60 words; this script has 162.
- **People in b-roll:** the user asked for people packing and moving boxes, so the objects-only b-roll rule is lifted for this ad.

## R5's shot order (ad time, from `04_Audience_Research/Ref_Ads_Research.md` §11) and ours
| R5 | Ours |
|---|---|
| 0.00-4.91 selfie inside a bright living room (the hook) | Ava inside, hook |
| 4.91 spin → porch with a stone wall | flash → Ava outside, the house behind her (the second hook) |
| 7.58-10.39 drone over the neighbourhood | packing b-roll, then drone |
| 12.92-15.65 couple packing boxes | (packing moved to "boxes", and again on the bonus) |
| 15.65 / 20.84 street selfie | Ava walking the front walk |
| 17.63-20.84 NO FEE / agent / cleaning icons over a blurred paper | icons for commission, fees, closing costs, crossed off |
| 22.89-end inside again + LINK BELOW pill | Ava inside again + LINK BELOW pill |

## Script with visuals (times at 176 wpm, estimates)
```text
[OPEN A]   Hold up. Cash for your house, plus a bonus nobody told you about.
           SHOW → 0.00 Ava INSIDE (clip 1): close selfie, face and body fill the frame. Palm to the lens on "Hold up", then a big smile.
[payload]  Any condition. Closed within 30 days, or whenever you're ready.
           SHOW → same shot, a small nod on "thirty".
[OPEN B]   And how do you know this is legit? I'll show you.
           SHOW → 7.84 white flash → Ava OUTSIDE (clip 2), the house partly behind her. One eyebrow up on "legit".
[payload]  Take what you love, and leave the rest. Furniture, boxes, all of it.
           SHOW → 11.59 B-ROLL: a family carrying moving boxes (Pexels 7347874, filmed vertical). Her voice continues.
[OPEN C]   Plus, there are three costs you get to cross off your list.
           SHOW → 16.02 B-ROLL: drone over a quiet suburban street (Pexels 29052852).
[payload]  You won't fix a thing, patch a thing, or paint a thing.
           SHOW → 20.11 Ava OUTSIDE walking the front walk (clip 3), a small head shake on each "thing".
[CLOSE C]  Agent commission. Fees. Closing costs. All crossed off.
           SHOW → 24.20 GRAPHIC (made in the edit): a blurred paper, three icons pop in (agent, fee tag, closing papers), each gets a red strike on its word.
[payload]  Cash in your hand, and the house off your plate.
           SHOW → 26.93 B-ROLL: hands counting $100 bills (stock cash100_6266251, frame-checked 2026-09-28).
[CLOSE B]  Here's how you know it's legit. I'm the one buying it. I'm paying cash. And nothing happens until you say yes.
           SHOW → 30.34 Ava OUTSIDE (end of clip 4): stops, serious half-smile. 32.39 white flash → clip 5: hand on chest on "I'm the one buying it".
[payload]  No pressure. Just a straight cash offer.
           SHOW → same shot, an easy shrug.
[CLOSE A]  And that bonus nobody told you about? There's no middleman in my deals, so the middleman's fee stays with you.
           SHOW → 39.89 flash → Ava INSIDE (clip 6), leans in on "bonus". 42.28 B-ROLL on "There's no middleman…": a couple among moving boxes (Pexels 4277371).
[payload]  Cash, a bonus, and your closing date. All yours.
           SHOW → 46.70 Ava INSIDE (clip 7), big smile on "All yours".
[CTA]      Tap the link below, tell me about the house, and I'll send you a cash offer.
           SHOW → she points down on "link below"; red LINK BELOW pill pops in at the bottom. Logo end card.
```
- **On every frame:** a permanent top banner in R5's style (white bold text on a red box): CASH FOR YOUR HOUSE + A BONUS. Short red captions with a dark outline sit on her chest, 2-3 words at a time.
- **Transitions:** R5 uses white flashes and light leaks, not hard cuts; the same here.
- **Ava on screen:** about 36.15 s of 55.23 s = 65.5 % (R5: 70.9 %). 12 shots, 11 cuts = 1.99 per 10 s (R5: 2.67).
- **Every clip join lands on a cut:**
  - clip 1/2 is the location change;
  - 2/3 is packing → drone;
  - 3/4 is face → graphic;
  - 4/5 has a white flash;
  - 5/6 is outside → inside;
  - 6/7 is b-roll → face.

## What to generate (Kie web app)
| # | What | Model | Upload | Settings | Words | Credits (list) |
|---|---|---|---|---|---|---|
| A | Ava outside, house behind (make 2, pick 1) | nano-banana-pro | `Ad18_Ava_avatar_v2_a.png` | 9:16, 2K, png | — | 2 × 18 = 36 |
| 1 | Hook, inside | gemini-omni-video | `Ad18_Ava_avatar_v2_a.png` | 10 s, 9:16, 1080p | 23 | 126 |
| 2 | Second hook, outside | gemini-omni-video | image A | 10 s | 24 | 126 |
| 3 | Walking, outside | gemini-omni-video | image A | 10 s | 24 | 126 |
| 4 | Costs + cash, outside | gemini-omni-video | image A | 10 s | 24 | 126 |
| 5 | Legit answer, outside | gemini-omni-video | image A | 10 s | 22 | 126 |
| 6 | Bonus reveal, inside | gemini-omni-video | `Ad18_Ava_avatar_v2_a.png` | 8 s | 20 | 105 |
| 7 | Close + CTA, inside | gemini-omni-video | `Ad18_Ava_avatar_v2_a.png` | 10 s | 25 | 126 |
| | **Total** | | | | 162 | **897 credits = $4.485** (Omni at list price, not measured; NBP measured) |

- **Prompts:** `10_Video_Builds/Ad18_JMSN_Inheritor/ava/` (`Ad18_Ava_image_prompt_outside.txt`, `Ad18_Ava_omni_clip1.txt` … `clip7.txt`). Every clip repeats Ava's full description and the same voice description.
- **Order:** image A first, then clip 1 alone as the voice test. Lock the voice, then run clips 2-7.
- **Checks:** word-diff every clip against its line. Omni has dropped the last sentence at 22 words in 8 s and repeated a phrase in a 10 s clip. Clip 7 holds 25 words, the most Omni has handled in 10 s.
- **B-roll** (free; real Pexels video, commercial use allowed): 29052852 (drone), 7347874 (family with boxes), 4277371 (couple among boxes). So far only preview frames have been checked; frame-check each clip for faces in close-up, text, signs and brand names before the cut. Cash: `07_Assets/Stock_Video/cash100_6266251`.
- **Length:** 55.23 s at 176 wpm, or 64.80 s at 150 wpm (both estimates). Omni's delivery sets the real length.
