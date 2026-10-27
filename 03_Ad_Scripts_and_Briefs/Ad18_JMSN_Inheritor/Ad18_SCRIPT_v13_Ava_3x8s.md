# Ad 18 v13: Ava, three 8-second clips

Written 2026-09-29. The user, on the 7-clip plan (v12): "I told you to generate three clips of 8 seconds." v12 overrode that instruction without asking; this version follows it.

- **Why the lines are shorter than v11:** an 8 s Omni clip holds about 19-21 words (measured on Ad 16; it dropped the last sentence at 22). Three clips hold about 60 words; v11 has 162. All 13 beats of the required structure stay, shortened.
- **Presenter:** Ava v2_a. **Visuals:** R5's.
  - Clip 1 is inside (the hook).
  - Clip 2 is outside with the house behind her (the second hook).
  - Clip 3 is inside again (the last hook).
  - Stock b-roll and an icons graphic go over the voice in the edit.

```text
[OPEN A]   Hold up. Cash for your house, plus a bonus nobody told you about.
           SHOW → CLIP 1, Ava INSIDE, face and body fill the frame. Palm to the lens on "Hold up", big smile.
[payload]  Any condition, closed within 30 days.
           SHOW → same shot, small nod.
[OPEN B]   Legit? You'll see.
           SHOW → white flash → CLIP 2, Ava OUTSIDE walking the front walk, the house behind her. Eyebrow up.
[payload]  No repairs.
           SHOW → B-ROLL: drone over a suburban street (Pexels 29052852).
[OPEN C]   Three costs disappear.
           SHOW → back to Ava outside.
[payload]  Take what you love, leave the rest.
           SHOW → B-ROLL: family carrying moving boxes (Pexels 7347874).
[CLOSE C]  Commission, fees, closing costs. Gone.
           SHOW → GRAPHIC: blurred paper, 3 icons pop in and get crossed off on each word.
[payload]  Cash in hand.
           SHOW → flash → B-ROLL: hands counting $100 bills (stock cash100_6266251). CLIP 3 audio starts.
[CLOSE B]  Legit? I'm the buyer.
           SHOW → CLIP 3, Ava INSIDE, hand on chest.
[payload]  No pressure.
           SHOW → same shot, easy shrug.
[CLOSE A]  Your bonus? The middleman's fee.
           SHOW → B-ROLL: couple among moving boxes (Pexels 4277371).
[payload]  All yours.
           SHOW → Ava INSIDE, big smile.
[CTA]      Tap the link below.
           SHOW → she points down; red LINK BELOW pill. End card.
```
- **On every frame:** the red top banner CASH FOR YOUR HOUSE + A BONUS, red chest captions, white flashes between shots (R5 style).
- **Words:** 19 / 20 / 20 = 59. At 176 wpm the speech lasts 6.48 / 6.82 / 6.82 s (estimates). The video is up to 24 s.
- **Checks:** the loop order matches the required structure, and each prompt matches its lines word for word (checked by script).

## Generate
| # | What | Upload | Settings | Credits |
|---|---|---|---|---|
| A | Ava outside, house behind (2, pick 1) | `12_AI_Characters/Ava/Ad18_Ava_avatar_v2_a.png` | nano-banana-pro, 9:16, 2K | 36 |
| 1 | `10_Video_Builds/Ad18_JMSN_Inheritor/ava/Ad18_Ava_omni_8s_clip1.txt` | Ava v2_a | gemini-omni-video, 8 s, 9:16, 1080p | 105 |
| 2 | `…/Ad18_Ava_omni_8s_clip2.txt` | image A | same | 105 |
| 3 | `…/Ad18_Ava_omni_8s_clip3.txt` | Ava v2_a | same | 105 |
| | **Total** | | | **351 credits = $1.755** (Omni at list price; NBP measured) |
