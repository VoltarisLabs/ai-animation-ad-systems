# Ad 20 clip map (LOCKED)

J's clip-by-clip copy, word for word, as the user pasted it on 2026-09-30 and 2026-10-01. This file is the only source for what each clip says and shows. Every clip prompt is built from it, and the quoted line is checked against it by script before any cost summary. Don't re-split lines, add stress capitals, or move a sentence between clips. Change this file only with the user's typed confirmation.

Model and settings for the clips (user, 2026-10-01): Seedance 2.0, 4 s per generation, 9:16, 720p, about 2 shots and 1 jump cut per 4 s, the same reference images and voice description in every clip, no auto-retry. A clip longer than 4 s of speech is made as two 4 s generations, split at J's own labels.

```text
━━ CLIP 1 · inside, at the dresser ━━
[OPEN A]   Don't sort it. Don't pack it. Just go.
           SHOW → First frame: AVA (Look D) pushes the overstuffed dresser drawer shut with her hip. It jams; a grey sweater sleeve hangs out. On "Just go" she lets it be, turns to the lens, small smile. TEXT: DON'T SORT IT

[payload]  Wanting it gone. Feeling guilty for wanting it.
           SHOW → AVA to the lens, softer. No cutaway.
           (2026-10-01, J on WhatsApp, relayed by the user: "Wanting it gone feeling guilty part should be b roll". This replaces "No cutaway". Done in v12, see below.)
           (2026-10-01: the user tried option B, "You want it gone. And you feel bad about it.", then went back to J's words: "I told you about this hook." J's words stand. The user also asked for jump cuts that change the picture: 3 shots of her in different spots, only a little sexy.)

━━ CLIP 2 · inside, selfie ━━
[payload]  And every month a house sits, it costs: upkeep, insurance, another drive back.
           SHOW → AVA, slower and softer, one small nod on "costs". "drive back": street_37314233. TEXT: EVERY MONTH IT SITS

━━ CLIP 3 · inside, selfie ━━
[OPEN B]   The fear underneath: am I getting less because I'm tired?
           SHOW → AVA brings the phone closer (tighter), quiet. TEXT: AM I GETTING LESS?

[payload]  Straight answer?
           SHOW → AVA, eyebrows lift, a little firmer.
```

To confirm with the user: clip 3 was pasted twice. The first paste (2026-09-30) includes the `[payload] Straight answer?` block; the second paste shows only `[OPEN B]`.

Clips 4 onward: not received yet. Ask the user for J's copy; don't write a split.

## Generation split (4 s each)

| Gen | J's clip | Words | Status |
|---|---|---|---|
| 1A | CLIP 1, OPEN A | Don't sort it. Don't pack it. Just go. (8) | made, accepted by the user: `13_Generated/videos/Ad20_selected_01_clip1A_dont_sort_it.mp4` (164 credits). She holds a second phone in her free hand; from 1B on, that phone lives in her front jeans pocket |
| 1B | CLIP 1, payload | Wanting it gone. Feeling guilty for wanting it. (8) | made: `13_Generated/videos/Ad20_selected_02_clip1B_wanting_it_gone.mp4` (164 credits). Starts on 1A's last frame; 3 shots (cuts at 1.33 and 2.875 s); 8/8 words; voice 0.537 against 1A with 1A's voice as the audio reference |
| 2 | CLIP 2 | And every month a house sits, it costs: upkeep, insurance, another drive back. (13) | made: `13_Generated/videos/Ad20_selected_03_clip2_every_month.mp4` (164 credits). 6 shots (too many); Whisper hears "the house", to check |
| 3 | CLIP 3, OPEN B only ("Straight answer?" moves to row 4, per J's table) | The fear underneath: am I getting less because I'm tired? (10) | made: `13_Generated/videos/Ad20_Ava_clip3_openB_seedance_4s_v1.mp4` (164 credits). Starts on 1B's last frame; 3 shots (cuts at 1.5 and 2.96 s: face, then a ceiling water stain with a crack, then a worried face); 10/10 words; voice 0.605 against 1A |

## Gen 1A: approved shot plan (user, 2026-10-01: "okay I think it's okay. Just remember we generated this, not something else.")

A selfie with one jump cut. No drawer close-up; her face is on screen the whole time. Prompt: `10_Video_Builds/Ad20_Ava_Heir/Ad20_Ava_seedance_4s_clip1A_selfie_v2.txt`. References: v3's last frame and the Look D face crop, the same as clip 2.

| Time (est.) | What you see | Her words |
|---|---|---|
| 0.0 s | High selfie, phone in her right hand (arm off the right edge), angled down: her face, red top and hips. The dresser is on the left of the frame, the stuck drawer at her hip with the grey sleeve hanging out. She is glancing back at it. | |
| 0.0–1.2 s | One quick bump with the hip nearest the drawer. It knocks back and jams, the sleeve still out, and the phone jolts. Free hand across her waist; her hands never touch the drawer. | Don't sort it. |
| 1.2–2.5 s | She looks from the drawer back to the lens, one eyebrow up, weight onto one leg. | Don't pack it. |
| 2.5 s | Jump cut: punch-in to head and shoulders at eye level. | |
| 2.5–3.3 s | Eyes into the lens, small smile, slight head tilt. Her last words. | Just go. |
| 3.3–4.0 s | Holds the smile, mouth closed. | |

## Selected by the user (2026-10-01)

"I selected and made them perfectly… the voice should be Seedance's original voice." The three clips were renamed in play order and joined, each clip's own Seedance voice kept (not the `_v3voice` copy):
- `13_Generated/videos/Ad20_selected_01_clip1A_dont_sort_it.mp4`
- `13_Generated/videos/Ad20_selected_02_clip1B_wanting_it_gone.mp4`
- `13_Generated/videos/Ad20_selected_03_clip2_every_month.mp4`
- Joined: `13_Generated/videos/Ad20_selected_01-03_joined_v1.mp4`. 12.300 s, 720x1280, 24 fps, each clip's loudness evened to -14 LUFS, whole file -13.4 LUFS with a -1.4 dBFS peak. Whisper hears all 29 words, with "the house" for "a house" in clip 2.
- Voice fix for clip 3, free (user, 2026-10-01: "the third clip doesn't match with the voice. Fix that." then "use that process"): clip 3's Seedance voice was converted with Chatterbox to 1A+1B's voice. A 0.4 s lead-in keeps "And", and "upkeep" is converted on its own and spliced in with 25 ms crossfades, because the whole-clip conversion slurred it to "of keep". Voice similarity to 1A went from 0.375 to 0.574 (1B scores 0.537). File: `13_Generated/videos/Ad20_selected_03_clip2_every_month_voice1A1B_v2.mp4`. **Joined: `13_Generated/videos/Ad20_selected_01-03_joined_v3.mp4`** (12.300 s, -14.4 LUFS, -1.4 dBFS peak; Whisper hears all 29 words, with "the house").
- Clip 3 voice raised, free (user, 2026-10-01: "the voice is too much. Less. Raise it. So that it matches..."): Praat "Change gender" with the formants unchanged, a new pitch median of 250, pitch range factor 0.85 and the same duration, so the lip sync holds. Measured pitch went from 210 to 262 Hz (1A is 262), pitch range from 117 to 92 Hz, and 10/10 words stayed. File: `13_Generated/videos/Ad20_Ava_clip3_openB_seedance_4s_v1_pitchup.mp4`. **Joined, 4 clips: `13_Generated/videos/Ad20_selected_01-04_joined_v4.mp4`** (16.400 s, -14.7 LUFS, -1.4 dBFS peak). Clip 2 (fixed) is still at 209 Hz.

## J's row 4, split into 4A and 4B (user approved the script on 2026-10-01)

J's row 4, word for word: `[payload] Straight answer? Being tired shouldn't cost you. You fix nothing. You pay no commission.` SHOW → AVA, steady, NO cutaway, music down. TEXT: TIRED SHOULDN'T COST YOU / FIX NOTHING / NO COMMISSION.

It is 14 words, too many for one steady 4 s clip, so it is split at J's sentences. The stress goes in her delivery, not in the words. The user's rules: different pictures in every clip (don't reuse the ceiling), questions sound like questions, one stressed word per line, and the same voice sound, pitch, tone and level as 1A and 1B.

```text
━━ CLIP 4A · inside, the doorway ━━
[payload]  Straight answer? Being tired shouldn't cost you.
           SHOW → AVA. "Straight answer?" is a real question (rises, eyebrows up). Jump cut to OUTSIDE: she has just walked out of the front door of the same house (the clip 2 house, no house number), standing naturally with no leaning pose (user, 2026-10-01); steady, stress on "shouldn't". TEXT: TIRED SHOULDN'T COST YOU

━━ CLIP 4B · inside, the kitchen ━━
[payload]  You fix nothing. You pay no commission.
           SHOW → Kitchen damage (cabinet door hanging off one hinge, chipped counter) on "You fix nothing" (stress "nothing"), then AVA leaning on the counter on "You pay no commission" (stress "no"). TEXT: FIX NOTHING / NO COMMISSION
```
- Gen 4A made 2026-10-01: `13_Generated/videos/Ad20_Ava_clip4A_seedance_4s_v1.mp4` (164 credits, task ee0c9354). 2 shots (cut at 1.375 s), 7/7 words. Voice 0.666 against 1A and 0.61 against 1B (the best match yet); pitch 288 Hz (1A 262, 1B 291). "Answer" rises from 273 to 337 Hz, so it sounds like a real question. Seedance gave her **blue jeans** outside, so they were darkened to black for free (a mask on blue pixels in the lower 40 % of the frame, 64 frames of shot 2): `13_Generated/videos/Ad20_Ava_clip4A_seedance_4s_v1_blackjeans.mp4`.
- Gen 4A v2 made 2026-10-01 (the user rejected v1: "you made her face look worse… match her face… consistent"): `13_Generated/videos/Ad20_Ava_clip4A_seedance_4s_v2.mp4` (164 credits). Face refs are the clean 1A/1B frames, and the skin is written as smooth. 2 shots (cut at 1.417 s), 7/7 words, voice 0.548 against 1A and 0.74 against 1B, pitch 271 Hz, black jeans. Shot 2 is a hands-free standing shot (phone propped), not a selfie.

## Voice = Ad 19's voice (user, 2026-10-01: "remember the same voice as Ad19_final_v2… first make the full video and match the whole voice")

Every clip's original Seedance audio was converted to Ad 19's voice (Chatterbox VC, target `10_Video_Builds/Ad20_Ava_Heir/voice/ad19voice/Ad19_voice_ref_0-12.wav`, 0.4 s lead-in). Pitch was then shifted per clip by its measured semitones to about 225 Hz (Ad 19 sits at 225 Hz), except clip 2: any shift slurred "upkeep", so clip 2 stays at 203 Hz. The audio is in `voice/ad19voice/final_*.wav`.
- **Full video: `13_Generated/videos/Ad20_selected_01-05_joined_v5_ad19voice.mp4`**: 1A, 1B, 2, 3, 4A v2. 20.209 s, -15.1 LUFS, -1.3 dBFS peak. The whole track scores 0.818 against Ad 19's own voice (a stretch not used as the target). Pitch per clip: 227 / 210 / 203 / 214 / 219 Hz. Whisper hears every word, with "the house" in clip 2 (from Seedance's take).
- From 4B on: generate on Seedance, then run the same Ad 19 conversion and pitch step, with a Whisper check.
- **CORRECTION 2026-10-01:** the Ad 19 voice conversion (joined v5) was WRONG. The user: "I wanted to keep the original [Seedance] voice. And match the rest of the things to the last video's voice." Don't use v5 or `voice/ad19voice/`.
  - v6 `Ad20_selected_01-05_joined_v6.mp4` has the original voices restored (1A, 1B, clip 2 voice1A1B_v2, clip 3 pitchup, 4A v2).
  - v7 `Ad20_selected_01-05_joined_v7.mp4` keeps 1A, 1B and 4A's original Seedance voices, and converts clips 2 and 3 from their original audio to 4A's voice (4A is the last video). Clip 2 goes 0.436 to 0.615 against 4A and clip 3 goes 0.372 to 0.582, with no pitch shift: raising the pitch dropped the match to 0.31–0.37. Clip 2 has a clean "upkeep" (word splice).
- Clip 3 face tone fixed, free (user, 2026-10-01): shot 3 (2.958 s to the end) was darker (face L 128–132 against 141–150 elsewhere). It was brightened x1.12, and a 60 % bilateral skin smoothing was applied to the face only. Afterwards: L 140–151, roughness 258 → 136. Files: `..._clip3_openB_seedance_4s_v1_pitchup_facefix.mp4` and `..._voice4A_facefix.mp4`. Joined v6 and v7 were rebuilt with it.
- Clip 3, "because I'm tired?" (user, 2026-10-01: "the face doesn't look good there… replace the face with some other visuals"): shot 3 (2.958 s to the end) is replaced by stock `07_Assets/Stock_Video/bed_17041569.mp4` from 2.0 s (Pexels 17041569, free commercial use, no people; logged in `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_SOURCES_broll.md`). Her voice is unchanged. Clip: `13_Generated/videos/Ad20_Ava_clip3_openB_v7_bedcut.mp4`. **Full video: `13_Generated/videos/Ad20_selected_01-05_joined_v8.mp4`** (v7 plus this swap; 20.5 s, -14.8 LUFS, -1.4 dBFS peak, every word heard).
- Gen 4B made 2026-10-01: `13_Generated/videos/Ad20_Ava_clip4B_seedance_4s_v1.mp4` (164 credits). 7/7 words; voice 0.673 against 4A. Seedance showed the filming phone in her raised hand (mirror-selfie look) and a big hole in the counter. Free fix (the user: "there is the phone in her hand… we do this for free"): shot 1 kept only to 0.85 s (the cabinet, before the hole) and slowed with motion interpolation to 1.40 s; the 1 s pause removed; shot 2 cropped to x 0–440 (no phone, no raised hand) and scaled to 720x1280; the audio cut keeps the lip sync (audio leads by 40 ms). File: `..._clip4B_seedance_4s_v1_nophone.mp4`, 2.875 s. **Full video: `13_Generated/videos/Ad20_selected_01-06_joined_v9.mp4`** (v8 plus 4B).
- 4B checklist, free (user, 2026-10-01: "blur all of these and show an animation of no commission and ... other things ... crossing off from the list"): the 4B nophone clip is blurred (gblur 22). A white card lists REPAIRS / COMMISSION / FEES / CLOSING COSTS, all confirmed terms, and each gets a red X and strike: REPAIRS at 0.90 s on "nothing", COMMISSION at 2.15 s on "commission", then FEES at 2.42 s and CLOSING COSTS at 2.62 s. The card sits in the caption-safe band. Built by `10_Video_Builds/Ad20_Ava_Heir/build_clip4B_checklist.py`, output `13_Generated/videos/Ad20_Ava_clip4B_checklist_v1.mp4`. **Full video: `13_Generated/videos/Ad20_selected_01-06_joined_v10.mp4`.**
- 4B icon version, free (user, 2026-10-01: "do that animation like the PNG photos ... cross with less blur ... the cropped version"): the base is the cropped nophone 4B with light blur (gblur 6, brightness -0.04). Four white tiles (Tabler Icons, MIT: hammer = REPAIRS, user-dollar = COMMISSION, receipt = FEES, file-dollar = CLOSING COSTS; licence in `10_Video_Builds/Ad20_Ava_Heir/icons/LICENSE_tabler.txt`) pop in, and each gets a red X at 0.90, 2.15, 2.42 and 2.62 s. Built by `build_clip4B_icons.py`, output `13_Generated/videos/Ad20_Ava_clip4B_icons_v1.mp4`. **Full video: `13_Generated/videos/Ad20_selected_01-06_joined_v11.mp4`.**
- Captions (user, 2026-10-01: "the whole video should have the /dynamic_captions_3click"): the skill's yellow-pop style (Impact, #F6ED04, black outline, 78 -> 106 -> 100 % pop), run through `10_Video_Builds/Ad20_Ava_Heir/captions/run_dyncap_ad20.py` without editing the skill. Words come from a corrected SRT (`captions/v11_words_corrected.srt`: faster-whisper small.en, "and other" -> "another", 46 words) with J's punctuation. 18 hand-set phrases; each caption is held through short pauses (max +0.6 s). Captions sit at y 662–747 of 1280, on her chest, clear of her face and inside the safe band. None during the 4B checklist (20.50 s to the end), where the tile labels carry the words. **Output: `13_Generated/videos/Ad20_selected_01-06_joined_v11_captions.mp4`** (23.375 s, -15.0 LUFS, -1.4 dBFS peak).
- B-roll on 1B, free (J, 2026-10-01: "Wanting it gone feeling guilty part should be b roll"): all of clip 1B's picture (4.042–8.167 s) is replaced by 3 Pexels shots with no people. The cuts sit inside the measured silences, on the caption breaks. "Wanting it gone." gets an armchair under plastic in an empty room (`armchair_7347890`). "Feeling guilty" gets a lived-in corner with a lamp, an old clock and an old TV (`lamp_5708383`). "for wanting it." is a 1.6x punch-in on the lamp and clock. Stock is colour-pulled toward Ava's interior shots (Ad 17's method). Her voice is untouched: the audio md5 is the same as v11's. JUST GO now ends at the cut instead of holding onto the b-roll (`CUTS` in `run_dyncap_ad20.py`). Built by `10_Video_Builds/Ad20_Ava_Heir/build_v12_broll_1B.py`; sources in `10_Video_Builds/Ad20_Ava_Heir/SOURCES_broll.md`. **Output: `13_Generated/videos/Ad20_selected_01-06_joined_v12_broll_captions.mp4`** (23.375 s, 561 frames, -15.0 LUFS, -1.4 dBFS peak).

## Section C (user, 2026-10-01, final: "make those shorter but keep the meaning the same ... generate it within the 4-second, show jump cuts of the visuals when payloads and show her face when you say the hooks ... the same character consistency")

All three parts are shortened with the same meaning, at the user's request. Hooks = her face; payload = jump cuts to visuals with Ava in each; every clip is a selfie with main Look D as @Image1. The prompts are written by `10_Video_Builds/Ad20_Ava_Heir/build_sectionC_prompts.py`.

J's originals: OPEN C "Five ways out of that house. Four are projects." / payload "List it: you paint, patch, and let strangers in. Fix it first: contractors you chase long-distance. Rent it: midnight calls. Wait: you heat a house nobody sleeps in." / CLOSE C "That's why the fifth way isn't a project. It's an exit. You hand it over exactly as it stands."

```text
━━ CLIP 5A · outside, selfie ━━
[OPEN C]   Five ways out. Four are projects.
           SHOW → White flash. AVA on the front path: five fingers up, folds to one. TEXT: 5 WAYS OUT. 4 ARE PROJECTS
━━ CLIP 5B · inside, selfie ━━
[payload]  List it: paint, patch, let strangers in. Fix it: chase contractors.
           SHOW → roller on the patched wall | holding the front door open | among the ladder and toolbox, eye-roll. TEXT: LIST IT / FIX IT
━━ CLIP 5C · inside, selfie ━━
[payload]  Rent it: midnight calls. Wait: heat an empty house.
           SHOW → night, sitting up in bed, groggy | day, hand on the old radiator, empty made bed behind. TEXT: RENT IT / WAIT
━━ CLIP 5D · outside, selfie ━━
[CLOSE C]  That's why way five isn't a project. It's an exit, as it stands.
           SHOW → one finger up on "way five" | holds the house keys up to the lens. TEXT: WAY 5: AN EXIT / AS IT STANDS
```
- Section C made 2026-10-01 (4 Seedance clips sent at once by mistake, 656 credits, 8,985.29 → 8,329.29): `13_Generated/videos/Ad20_Ava_clip5A_openC_seedance_4s_v1.mp4`, `…5B_payload…`, `…5C_payload…`, `…5D_closeC…`. Checks: 5B, 5C and 5D are selfies, match Look D, black jeans, no phone in hand; voice against the full video 0.602 / 0.790 / 0.728 / 0.716. 5A has two issues: it is shot third-person, not as a selfie, and the house number "43" is readable on the porch post (not yet fixed; the user was offered a free blur or a redo).
- **Full video v13 (user, 2026-10-01: "attach those in serial to ... v12_broll_captions"):** `13_Generated/videos/Ad20_selected_01-10_joined_v13_captions.mp4` = v12_broll_captions (23.375 s) + section C (5A with a 0.17 s white flash in, 5B, 5C, 5D; each at -14 LUFS; captioned by `captions/run_dyncap_sectionC.py` in the same yellow-pop style, from the script's words on Whisper timings, `captions/sectionC_words.srt`). 39.792 s, 720x1280, 24 fps, -14.5 LUFS, -1.4 dBFS peak. Whisper hears every line in order.
- **Clip 6A · CLOSE B (user's words, 2026-10-01):** "That's why tired isn't a discount. Less work, more of your life back. No fees. No closing costs. That's the deal." (21 words, 4 s, the user's choice after the 13-words-per-4-s limit was flagged). Prompt `10_Video_Builds/Ad20_Ava_Heir/Ad20_Ava_seedance_4s_clip6A_closeB_v1.txt` (built by `build_sectionD_prompts.py`, section C blocks unchanged; Look D + face crop + `voice/Ad20_fullvideo_v11_voice_ref_0-14.5.mp3`). Made: `13_Generated/videos/Ad20_Ava_clip6A_closeB_seedance_4s_v1.mp4`, task `2276a15e…`, 164 credits (8,329.29 → 8,165.29), 720x1280, 4.063 s. Checks: Whisper hears 14/21 words; "Less work, more of your life back." was dropped (the couch shot has a quiet exhale, -30 to -43 dB, at 1.3-1.9 s). 3 shots as written (standing, couch, standing), but shots 2 and 3 are not selfies (both hands visible). Look D face, black jeans, no phone. Voice vs the full video 0.768 (section C 0.602-0.790). Hand out to the lens on "That's the deal" happens.
- Clip 6B · CLOSE A + CTA prompt ready, not run: `Ad20_Ava_seedance_4s_clip6B_closeA_cta_v1.txt` (20 words; @Image3 = `12_AI_Characters/Ava/Ad20_Ava_scene_I1_dresser_hip_v1.png` for the room only).
- **6A free fix (user, 2026-10-01: "fix the 6A for free"):** `13_Generated/videos/Ad20_Ava_clip6A_closeB_seedance_4s_v1_fixed_captions.mp4` (4.083 s, 0 credits). Yellow-pop captions like the rest (`captions/run_dyncap_sectionD.py`, `captions/sectionD_6A_words.srt`); the dropped line shows on screen as LESS WORK / MORE LIFE BACK in the silent couch shot (1.44-2.14 s). 7 captions: THAT'S WHY TIRED / ISN'T A DISCOUNT / LESS WORK / MORE LIFE BACK / NO FEES / NO CLOSING COSTS / THAT'S THE DEAL. 6B sent the same day (task `a37058bc…`, 164 credits).
- **Clip 6B · CLOSE A + CTA (2026-10-01):** `13_Generated/videos/Ad20_Ava_clip6B_closeA_cta_seedance_4s_v1.mp4`, task `a37058bc…`, 164 credits (8,165.29 → 8,001.29), 720x1280. Whisper: 20/20 words in order ("That's why you don't sort a thing: everything stays. Tap Learn More and tell us where it is. No obligation."), last word ends 3.82 s. 2 shots (cut at 2.042 s): selfie at the clip 1 dresser, drawer pushed shut with the grey sleeve still out; then chest-up selfie pointing down. Voice vs the full video 0.798.
- **Full video v14 (user: "This should be the last part of the video"):** `13_Generated/videos/Ad20_selected_01-12_joined_v14_captions.mp4` = v13_captions + section D (6A with a 0.17 s white flash in, 6B; each at -14 LUFS; captions `captions/run_dyncap_sectionD.py` 6AB, `captions/sectionD_words.srt`, 39 caption words incl. LESS WORK / MORE LIFE BACK). 48.000 s, 720x1280, 24 fps, -14.4 LUFS, -1.3 dBFS peak. Whisper hears section D in order (minus the dropped 6A line, which is on screen). No end card yet (no logo file).
- **Full video v16 = the complete video (user, 2026-10-01: "add the rest ... If some parts are too fast, then you can slow it down but ... keep the voice the same"; "The lip sync should also match. Not too slow that it looks fake"):** `13_Generated/videos/Ad20_selected_01-12_joined_v16_captions.mp4`, built by `10_Video_Builds/Ad20_Ava_Heir/build_v16_sectionD_natural.py`. v13 untouched + 6A and 6B slowed: talking x1.2-1.45, silent frames between sentences x2-3 (rubberband R3, pitch kept), one time map per clip for picture and sound (motion interpolation, last source frame held so picture = sound: 6A 5.291667 s both). 51.333 s, -14.3 LUFS, -1.3 dBFS peak, 0 credits. Talking speed in the last part 6.58/4.49 -> 3.94 words/s (v13 2.93, its fastest sentences 3.4-5.9). Pitch 243.6 -> 244.2 Hz (6A), 238.3 -> 237.5 Hz (6B). Voice vs the full video 0.705 / 0.728 (section C 0.602-0.790). Lip check: the closed-lip "m" of "More" lands on the same frames of the time map (6.34-6.40 s original, 8.81-8.90 s slowed). Whisper hears "No obligations" (an extra s) at the end. v15 (`…v15_captions.mp4`, whole shots up to x1.75) looked slowed and made "Tap" read as "App": superseded.
- **Full video v18 = the complete video (user, 2026-10-01: "the logo should be 'Learn More'"; "keep the normal speed for the last two because it looks worse if you slow down"):** `13_Generated/videos/Ad20_selected_01-12_joined_v18_learnmore.mp4`, built by `10_Video_Builds/Ad20_Ava_Heir/build_v18_learnmore.py` on v14 (6A and 6B at normal speed). A white LEARN MORE button (4B tile style, Montserrat Black, chevron) pops in on "Tap" at 45.954 s under the TAP LEARN MORE caption, inside the safe band (y 753-831), and pulses to 48.000 s; then a 1.5 s end card (caption-free last frame blurred, the button, NO OBLIGATION), silent. 49.500 s, -14.4 LUFS, -1.3 dBFS peak, 0 credits. The slowed v16 and v17 (button on v16) are superseded.
- **v19-v25 (2026-10-01), current = `13_Generated/videos/Ad20_selected_01-12_joined_v25.mp4`** (29.583 s, -14.0 LUFS, LRA 2.4 LU, -1.5 dBFS, 0 credits). Built from `10_Video_Builds/Ad20_Ava_Heir/build_v23_voice_sync.py` work files (`v23_work/v23_fast.mp4`, `v23_button.mp4`) with two cuts: 4B ends -> "It's an exit, as it stands." (user: cut "Five ways out" through "That's why way five isn't a project."), and 6A/6B back at 1x (user: "slow down a little bit on the last parts"). Contents: J's new second phase "Feeling guilty for wanting it gone." (Chatterbox clone, free, b-roll only); b-roll for 4B (leak, for-sale sign under the tiles), "No fees, no closing costs" (contract), "everything stays" (shed), "and tell us where it is" (house), house end card with LEARN MORE / NO OBLIGATION (sources in `10_Video_Builds/Ad20_Ava_Heir/SOURCES_broll.md`); R5 transitions (light leak, pastel flash, flash + leak); voice evened (LRA 2.4 LU); body 1.2x up to section C's "It's an exit", 1x after; captions at 61.5% height; Mixkit "Classical 3" bed (-27 LUFS before ducking, 8 dB extra dip under the CTA). Voice: clips 2, 3, 4B, 5A, 5B, 6A and the second-phase line converted to the first hook's voice where it scored closer AND Whisper read the same words (`voice/vc_first_hook/pick_per_clip.py`): all parts 0.502-0.654 to the first hook (was 0.454-0.653). Sync fix: the parts' sound has timestamp gaps; v19-v22 dropped them (section C voice 205 ms, D 352 ms early); v23+ gap-fill every input (sections 0 / 0 / +3 ms). Open: with the music, Whisper reads "Tap Learn More" as "Stop/App learn more" (voice alone reads "Tap").
- **v26 (2026-10-01), current = `13_Generated/videos/Ad20_selected_01-12_joined_v26.mp4`** (28.042 s, -14.0 LUFS, LRA 2.1 LU, -1.5 dBFS, 0 credits), built by `10_Video_Builds/Ad20_Ava_Heir/build_v26_j_notes.py` from J's WhatsApp notes on v25: no music ("music sucks"; voice only like R1-R3); the second phase now her face and real voice from clip 1B ("Feeling guilty" shot 2 | "for wanting it" shot 3 | "gone" from shot 1 over the armchair b-roll, with R5's light leak); clip 2 at 1x ("insurance upkeep another drive back its too fast"); 8 pauses over 0.30 s cut to 0.25 s, 1.54 s of silence out ("no dead space or long pauses"; longest left 0.39 s); end card 0.8 s. Whisper reads every line, incl. "Tap Learn More", but punctuates the splice as "for wanting it. Gone." (her "it" falls like a sentence end in the source take).
- v26 rebuilt (user: "first you have to do it for free"): the second phase is now one smooth phrase from clip 1B: shot 2 "Feeling guilty" | jump cut | shot 1 "for" (from shot 3, 2.95-3.08 s) + her own "wanting it gone" (shot 1, said as one phrase), both on her face. Whisper: "Feeling guilty for wanting it gone." 27.792 s, -14.0 LUFS, LRA 2.1 LU, -1.4 dBFS. Whisper flips between runs on two unchanged lines ("The fear underneath" / "So if you're underneath"; "Tap" / "Stop").

- **v27 (2026-10-01):** `13_Generated/videos/Ad20_selected_01-12_joined_v27.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v27_pauses_broll.py`). User: "There should be a long pause as he suggested. And while the pause happens you can show some B-roll there." v26's pause trimming is undone. Pauses added after "upkeep," (+0.75 s), "insurance," (+0.75 s) and "another drive back." (+0.25 s); her gaps there had been 30-40 ms. Measured pauses: 0.76 / 0.76 / about 0.85 s. B-roll over every pause, including the natural ones after "Straight answer?" (0.74 s) and "...shouldn't cost you." (0.56 s). Words and clips unchanged. 30.917 s, -14.0 LUFS, LRA 3.6 LU, peak -1.1 dBFS, 89 caption words, 0 credits.
- **v28 (2026-10-01):** `13_Generated/videos/Ad20_selected_01-12_joined_v28.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v28_research_edit.py`). User: "you made it worse ... get the recent research data first. And fix it like that." The edit follows `PERSUASIVE_SCRIPTING_PLAYBOOK.md` section 9 and `COURSE_REPORT.md` B.6:
  - every part at 1x (no speed-ups): 177.3 wpm;
  - natural pauses, 0.30-0.49 s (the references' longest gaps were 0.50 and 0.68 s);
  - a 0.33 s beat with room tone after "upkeep," and "insurance,";
  - no transitions (R5's flashes and leaks removed; 6A's baked white flash undone);
  - shake on the static face shots;
  - small white lowercase Anton captions;
  - clip 2 (the cost of keeping the house) in black and white; saturation +7.
  Measured: 31.917 s, -14.0 LUFS, LRA 2.6 LU, peak -1.5 dBFS, 31 cuts. Words and clips unchanged, 0 credits.
- **v29 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v29.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v29_think_pause.py`). User: "there should be a small pause" after "Feeling guilty for wanting it gone", "to give people some time to think but not much time".
  - The pause stays on her face: clip 1B shot A runs on into its own silent frames after "gone" (+15 frames).
  - Measured silence after "gone.": 0.62 s. The other gaps are 0.34-0.50 s; the references' longest were 0.50 and 0.68 s.
  - Run 1 (+12 frames) measured 0.50 s, no longer than the other gaps, so it was lengthened.
  - Otherwise v28. 32.542 s, -14.0 LUFS, peak -1.1 dBFS, 171.9 wpm, 0 credits.
- **v30 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v30.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v30_natural_pause.py`). User: "the pause should feel natural ... before She said 'every month the house sits' ... No extra sound so that it looks like different clips."
  - What v29 got wrong, measured:
    - "Every" came in with a hard edge (-67 to -14 dB in 2.5 ms), because clip 2's audio starts mid-attack in every version;
    - the filled beats were a looped word tail (-52 dB, flatness 0.10) instead of her near-silent floor (-78 to -85 dB);
    - the face hold played frames back and forth;
    - the caption said "and", which isn't spoken.
  - v30:
    - her own silent frames after "gone" (forward only);
    - the black-and-white house leads her voice by 0.25 s;
    - a 15 ms attack on "Every";
    - every filled gap is her floor (SRC 16.30-16.75 s);
    - the caption reads "every month".
  - Pause after "gone.": 0.54 s at -75 dB, the same floor as her other pauses (0.33-0.49 s).
  - 32.458 s, -14.0 LUFS, peak -1.5 dBFS, 0 credits.
- **v31 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v31.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v31_music.py`). User: "the music should be the background music ... trusted and energetic".
  - v30 plus Mixkit "Follow My Voice" (112 BPM, confident, motivating) as a background bed, ducked under her voice.
  - Measured bed: 11.9 LU under her voice while the whole ad plays (-26.0 vs -14.1 LUFS, 0-27.9 s), -28.3 dBFS in her pauses, -41.9 dBFS under the CTA.
  - Run 1 (v23's duck) was 36.4 dB under her while she talked, so it was inaudible.
  - Whisper reads "Tap learn more" correctly with the bed in.
  - 32.458 s, -14.0 LUFS, peak -1.5 dBFS, 0 credits.
- **v32 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v32.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v32_score.py` + `v32_plan.json`). User: "the music doesn't go well with how she says the hooks ... agency video ... feel real ... The music should cover [the voice]".
  - Researched by two agents: scoring practice and voice masking, with sources; track matching against her measured delivery.
  - **The score:**
    - "Home" (soft dream pop, no beat) under 0-15.28 s, 13 LU under her voice, low-passed to 1 kHz in the black-and-white problem;
    - silence in her own pause before "Straight answer?";
    - "Uplifting Bass" (134 BPM) lands on its downbeat at "Straight" (15.71 s), 9 LU under her voice, ducked 6 dB plus 4 dB in 1.5-4 kHz while she talks;
    - it stops on its beat at 29.14 s so the CTA is clean, then hits again on the 31.84 s downbeat for the end card.
  - **Voice:** high-pass 110 Hz, de-ess, -1.5 dB above 8 kHz, 2.5:1 glue, soft clip, a diffuse room (RT60 0.35 s, wet 0.10), room tone at -60 dBFS. The clip's "Tap" had no "t" release, so a 22 ms release was added in her closure.
  - **Measured:**
    - 32.5 s, -14.0 LUFS, LRA 1.4 LU, peak -1.5 dBFS;
    - music -93 dBFS in the stop, about +7.5 dB at the turn;
    - Whisper reads every word correctly; "Tap" reads 6 of 8 on the CTA alone (0 of 8 before the fix);
    - 0 credits.
- **v33 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v33.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v33_open.py` + `v33_plan.json`). User: "the starting music should be interesting too ... use the psychological data".
  - v32 with an opening: Mixkit "Pop Track 01" (Lily J, the same artist as the turn track) under 0-3.96 s, 9 LU under her voice.
  - Its hit lands at frame 0 (-21 dBFS within 5 ms; v32 faded in and took about 50 ms to reach -40 dBFS).
  - Chord stabs on "don't" and "go"; silent before the 4.04 s cut; then "Home" as in v32.
  - Measured: -14.0 LUFS, LRA 1.5 LU, peak -1.5 dBFS. The hook reads 3 of 3 in Whisper; "Tap" reads 5 of 8 (v32 7 of 8, the same CTA mix); 0 credits.
- **v34 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v34.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v34_one_track.py`). User: "The music starts energetic but it is just a few seconds ... shouldn't stop suddenly ... another version of that music, not something different."
  - One track all the way through: Mixkit "Pop Track 01" (Lily J), split into drums, bass and other with demucs 4.1 (`v34_work/stems/`).
  - **Its versions:**
    - full band for the opening hook (the hit at frame 0, stabs on her words);
    - a quiet version from 3.8-4.3 s: the same song 8 beats ahead, where the chords run (the track's own 4-7.5 s is drums only), drums 9 dB down, a 3 kHz low-pass, 13 LU under her voice; muffled to 1 kHz in the black-and-white problem;
    - the drums back on the beat at 15.406 s, in her pause before "Straight answer?";
    - full through the offer and the closing hooks (the bass enters at 23.5 s);
    - 7 dB down under the CTA, back up for the end card, a 0.7 s fade at the end.
  - Every change is a crossfade on a beat, with no stops: the music's quietest 400 ms window is -52.7 dBFS, inside the hook, against v32's -93.5.
  - Measured: -14.0 LUFS, LRA 1.6 LU, peak -1.5 dBFS. Whisper reads all words; "Tap" 8 of 8 on the CTA. 0 credits.
  - Trending music: Instagram's library is "intended for personal, non-commercial use", and Sound Collection "can be used for commercial purposes like ads" (help.instagram.com/402084904469945, read 2026-10-02). Downloading from Sound Collection needs the user's Facebook login.
- **v35 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v35.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v35_voice.py`; voice `voice/unify/voice_v35.wav`; scripts `voice/unify/`). User: "Keep the original voice. Just match the whole voice so that he/she sounds like a human", then "You can install the new one".
  - Seed-VC was installed in `~/tools/seed-vc` (local, 4.4 GB with models; code GPL-3.0).
  - **Used, measured better:**
    - the four parts v23's Chatterbox conversion had cut at 11.4 kHz (clips 2, 3, 4B, 6A) get their top end back from Seed-VC's 44.1 kHz conversion: 14.9-15.3 kHz, UTMOS and ECAPA unchanged;
    - "It's an exit" takes Seed-VC's speech-mode body: similarity 0.449 -> 0.522, pitch movement 9.8 -> 13.2 st, UTMOS 3.73 -> 3.69.
  - **Rejected, measured worse:**
    - Chatterbox re-conversion of 1B/4A/5D/6B (similarity down; "Tap" -> "App");
    - Praat pitch widening (UTMOS -0.45/-0.6);
    - whole-part Seed-VC (UTMOS down in most parts).
  - **Calibration:** ECAPA on 2-s halves of the same take scores 0.49-0.69, so 0.53-0.68 between parts is within "same person".
  - **Final mix:** energy above 10.5 kHz +5 to +10 dB on clips 2, 3, 4B and 6A vs v34; -14.0 LUFS, peak -1.5 dBFS; all words read; "Tap" 8 of 8; 0 credits.
  - **Still open:** the rushed close and CTA (4.7-5.1 words/s) and the flat middle (9-10 st) need regeneration.
- **v36 (2026-10-02):** `13_Generated/videos/Ad20_selected_01-12_joined_v36.mp4` (`10_Video_Builds/Ad20_Ava_Heir/build_v36_slow_end.py` -> `build_v36_mix.py`). User: "from 26 seconds to 32 seconds ... too fast. Slow only that part a little bit ... It should feel natural."
  - 26.04 s to the end card: 5.625 -> 6.542 s, so 4.62 -> 3.97 words/s. New pauses: 0.20 s after "no closing costs" (contract b-roll), 0.40 s at "a thing: | everything stays" (shed b-roll), 0.21 s after "where it is" (house b-roll), 0.17 s before the end card.
  - Her face shots are slowed 6-10% with picture and voice together (minterpolate + rubberband R3, formants kept). The "Tap Learn More" shot plays at 1x.
  - Music not stretched: the CTA dim and the end-card return sit on the track's beats (29.779 / 32.751 s). The music stays ducked through the CTA.
  - **Bugs, and the measurement that caught each:**
    - "end of last sound" put the shed pause inside "Tap" (Whisper "Tap" 0 of 8). The pause now goes at the colon before "everything".
    - The "t" release stayed at 29.50 s. It now moves with the vowel.
    - Stretching "Tap Learn More" or "everything stays" smeared the "t". Both are now 1x.
    - The evenly stretched shed shot showed "everything stays" 180 ms early. Now 7 ms.
  - The "Tap" audio is identical to v35 (0.0 dB difference, 0 ms offset). Whisper's lower read (1-3 of 8 vs 4-8) comes from the new timing around it.
  - 33.375 s (801 frames), -14.0 LUFS, peak -1.5 dBFS, 0 credits.
