# "Thinking They're Real": AI street interview, measured

Analysed 2026-10-02. This is a reference for the street-interview format: what makes these AI people pass as real, measured against our own raw Gemini Omni and Seedance clips.
- The downloaded video, its full transcript and the measurement files stay local (`07_Assets/` is not in the repo).
- The clone kit built from this analysis, `STREET_INTERVIEW_CLONE_KIT.md`, belongs in this folder and is local only so far.

## Source

| | |
|---|---|
| Post | https://x.com/mightyking/status/2105617595403489651 (@mightyking, 2026-10-01) |
| Post text | "Thinking They're real. FLUX 3 bends reality. Kudos to u/love1008 (reddit)" |
| Maker | u/love1008 on Reddit. The Reddit post did not come up in a web search, so the prompts are unknown. |
| Model (per the post) | FLUX 3 by Black Forest Labs: released 2026-07-23, video up to 20 s with native audio, early access only. **Not on Kie:** `flux-3`, `flux-3-video`, `flux3-video` and `black-forest-labs/flux-3-video` all returned 422 "not supported" on 2026-10-02, and kie.ai/flux-3 says "upcoming". |
| Stats at download | 18,866 views, 276 likes, 12 reposts, 13 comments |
| File | 42.167 s, 1906 × 1080, 30 fps, H.264 + AAC 48 kHz stereo |

## Shot list

Cuts come from ffmpeg scene scores, words from faster-whisper large-v3. Answers are given as their opening words plus a paraphrase; the full lines are the creator's script.

| # | Time (s) | Who | Framing | What is heard |
|---|---|---|---|---|
| 1 | 0.00–1.57 | Woman, ~25, green work jacket, tote strap, hoops | Tight close-up, no mic in frame | Off-camera interviewer: "How would you know if you were talking to an AI?" She listens, eyes up and to the side, closed-mouth half smile. |
| 2 | 1.57–5.27 | Same woman | Wider, mic hand enters bottom-left | "It would be too polished…": AI wouldn't have small odd pauses. |
| 3 | 5.27–10.00 | Man, ~50s, grey hair, glasses, navy rain jacket, backpack strap | Mid-chest up, café and chalkboard behind | "I'd ask something personal…": he'd test whether it gets the feeling behind it. |
| 4 | 10.00–14.43 | Young man, ~20, black tee, backpack | Low angle, crosswalk and traffic lights behind | First ~0.7 s: a different young man in a grey hoodie fills the frame and moves out left with motion blur while a hand points. Then "If every answer…": right answers that feel rehearsed. |
| 5 | 14.43–21.60 | Man, ~30, curly hair, olive overshirt | Mid-chest up, crowded sidewalk behind | The question again, then "It would sound confident…": sure of everything, with no real memory behind it. |
| 6 | 21.60–25.90 | Woman, ~45, black bob, round glasses, trench coat, bag strap | Café terrace railing behind | "I would ask it something messy…": real people hesitate when it matters. |
| 7 | 25.90–31.93 | Woman, ~25, curly bun, denim jacket over yellow tee, hoops | Bikes and storefront behind | The question a third time, then "It would be too perfect…": no awkward pauses, no odd details. |
| 8 | 31.93–35.23 | Young man, ~22, navy overshirt, white tee | Café terrace, diners behind | "Maybe it would answer fast…": quick answers that don't mean anything. |
| 9 | 35.23–42.17 | Man, ~25, messy hair, hoodie under olive jacket, backpack | Closest shot of all, warmer late light | The twist, "Actually…": he wonders whether he is an AI himself, pauses, and says he doesn't know why he is standing there. It ends there: no end card. |

9 shots in 42.17 s, one cut every 4.69 s on average. 8 people, 4 women and 4 men, ages about 20 to 55, mixed ethnicities. No captions, no logo, no end card, no music. The spectrogram shows no steady tones under the 15.8–17.4 s gap, only low traffic rumble.

The structure: one question asked 3 times (0.0 s, 14.4 s, 26.0 s) splits the video into blocks of 3, 2 and 3 answers. The last answer turns the question back on the speaker.

## How the characters talk

- **Every answer is short:** 10–19 words, one idea, 1–2 sentences. Per answer: 10, 14, 10, 14, 12, 13, 11, 19 words.
- **7 of 8 answers open with a hedge or a condition:** "It would…" ×3, "I'd ask…", "I would ask…", "If every answer…", "Maybe it would…". The 8th opens with "Actually," which is the turn word for the twist.
- **Small fillers, never "um":** "like" ×2, "somehow" ×2, "actually" ×2, "maybe" ×1.
- **Fragments are allowed:** two answers are not full sentences.
- **Plain, concrete words**, no abstract ones.
- **Pace:** 192.4 wpm across the whole video. Per answer 133.9–223.0 wpm.

## How they think on camera

- **Thinking is shown before the words.** Shot 1 is pure listening: eyes up and to the side, mouth closed, half smile, while the question plays.
- **They talk to the interviewer, not to the lens.** Most look just beside the lens. Only the twist guy stares straight into it, so the one look into the lens lands as unsettling.
- **Faces move mid-thought:** lips part, one brow lifts, eyes narrow into the light. Nobody holds a smile.
- **They're mid-errand:** a bag or backpack strap on 6 of 8, everyday jackets, nobody styled.
- **The twist guy is quieter:** street floor −45.4 dBFS against −32 to −39 for the others, and a 1.18 s pause mid-line. Flatter pitch too: 2.68 semitones SD, the lowest of the 8.

## What they say AI sounds like (their own checklist)

The dialogue lists the tells, and the video passes because it does the opposite of each. Each one next to what we measured in our own clips:

| They say AI is… | Our raw clips, measured |
|---|---|
| too polished, no odd little pauses | Voice 33.9–47.9 dB above a near-silent background. Reference: 8.7–16.6 dB above street noise. |
| rehearsed | Omni Ava's pitch moves 6.87 semitones SD (more than any reference answer, so it reads acted). Omni JMSN 2.31, flatter than any reference answer. Reference 2.68–4.27. |
| confident about everything | Held smile, eyes locked on the lens. |
| never hesitating | Our lines are ad copy delivered to the lens, with no glance away. |
| too perfect | Faces 3.0–13.7× sharper than the reference (below). |

## Picture, measured

Face crops are taken with YuNet and resized to 256 × 256, so different resolutions compare fairly.

| | Face sharpness (Laplacian var.) | Face height / frame | Saturation | Clipped highlights | Crushed blacks | fps |
|---|---|---|---|---|---|---|
| Reference, all shots | 50.43 | 0.45 | 53.3 | 2.58 % | 0.04 % | 30 |
| Reference, shots without glasses | 38.18–66.41 (median 39.88) | 0.34–0.58 | | | | |
| Omni, Ad20 Ava | 134.6 | 0.19 | 87.44 | 0.0 % | 0.78 % | 24 |
| Omni, Ad16 JMSN | 544.98 | 0.21 | 40.83 | 0.24 % | 0.63 % | 24 |
| Seedance, Ad18 Ava | 230.39 | 0.31 | 97.17 | 0.5 % | 2.91 % | 24 |
| Seedance, Ad17 JMSN | 121.51 | 0.40 | 55.17 | 0.26 % | 0.63 % | 24 |

- **Our faces are 3.0× to 13.7× sharper** than the reference's no-glasses median (121.51 / 39.88 to 544.98 / 39.88). Glasses frames add edges, which is why shots 3 and 6 read 290.48 and 248.3.
- **The reference lets the sky clip** (2.58 % of pixels at 250+) and keeps its blacks up (0.04 % at 5 or below). Ours do the opposite: no clipped sky, more crushed blacks.
- **Ava's saturation** (87.44, 97.17) comes mostly from her red top. JMSN is in the reference's range.
- **Camera shake** doesn't separate the two groups: reference median 0.063 % of the frame width per frame, ours 0.029–0.132.
- **Frame rate:** the reference runs at 30 fps like a phone. All four of our raw clips are 24 fps.

**Softening test (2026-10-02):** `gblur=sigma=1.0,eq=contrast=0.94:brightness=0.02` gave face sharpness 36.6 (Omni Ava) and 55.5 (Seedance Ava), with crushed blacks at 0.00 %. That is inside the reference's range, except Omni at 36.6, just under its 38.18 low end. Sigma 1.6 overshot (19.6 and 26.9).

Side by side, the blur fixes the number but not the look. These three differences remain:
1. **Posed smile into the lens** vs a stranger mid-thought looking beside it.
2. **Plain wall** vs a deep, busy street with people at several distances.
3. **Even, frontal "beauty" light and sleek hair** vs flat overcast daylight from above and messy hair.

## Sound, measured

| | Pitch SD (semitones) | Pitch range p5–p95 | Street floor | Voice above floor | wpm | LUFS | LRA |
|---|---|---|---|---|---|---|---|
| Reference, whole | 5.13 | 16.2 | −41.1 dBFS | 17.8 dB | 192.4 | −23.8 | 13.2 |
| Reference, per answer | 2.68–4.27 | 9.82–17.4 | −32.2 to −45.4 | 8.7–16.6 | 133.9–223.0 | | |
| Omni, Ad20 Ava | 6.87 | 21.99 | −63.7 | 39.4 | 127.7 | −25.4 | 4.7 |
| Omni, Ad16 JMSN | 2.31 | 7.6 | −55.2 | 33.9 | 168.0 | −22.6 | 2.4 |
| Seedance, Ad18 Ava | 3.42 | 11.2 | −53.9 | 38.8 | 212.7 | −17.4 | 1.9 |
| Seedance, Ad17 JMSN | 3.23 | 11.06 | −60.2 | 47.9 | 158.7 | −14.2 | 2.9 |

- **The biggest sound gap is the background.** Every reference line sits on street noise at −32 to −45 dBFS. Ours sit on near silence (−53.9 to −63.7). That near silence is the "studio clean" tell.
- **Pitch movement:** Seedance is already in the reference's range. Omni went both ways: Ava over-acted, JMSN flat.
- **The interviewer is not one consistent voice.** The 3 question reads have median pitch 129.3, 173.5 and 140.5 Hz, and ECAPA voice match between them of 0.359–0.538 (different people in this video match each other at 0.161). From 1.3 s snippets this can't be settled. It looks like the voice was generated again in each clip.
- LRA isn't a fair comparison: the reference is 9 shots with different mic distances, ours are single takes.

## Why it reads as real, in order of measured gap

1. **Performance:** a stranger thinking out loud to an interviewer beside the lens, not a presenter talking to the lens.
2. **Sound:** a lav mic on a loud street, with the voice only 8.7–16.6 dB above the traffic.
3. **Picture:** soft phone video, the sky allowed to clip, blacks lifted, 30 fps.
4. **Casting:** ordinary commuters with bag straps, ages 20–55, glasses, nobody styled.
5. **Messy moments:** a hand pointing, someone crossing the frame, the listener's face during the question.
6. **The twist:** the last person turns the question on himself, closer and quieter, and the video ends without an end card.
