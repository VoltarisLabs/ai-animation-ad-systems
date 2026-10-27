# Ad 27 v7: "Let Me Go", 60-second version

Status: 2026-10-13, the user's ask: "make it a little bit smaller, 1 minute or less; the music should sound similar, and the visuals too". Replaces v6 (about 1:50). Nothing generated yet.

## How it got under a minute

- 12 sung lines instead of 20: the minimum the required loop order allows (3 nested loops, a payload after every open and close).
- The song shape is now verse / chorus / verse / chorus / outro, and the second chorus mirrors the first with the same melody (couch -> her bed, Christmas at her sister's -> Christmas at her new place). It sounds like a real song with fewer words.
- Same style, same voice and instruments; the tempo goes from 96 to 108 BPM. At 96 BPM, 12 lines of 2 bars each take 60.0 s before the CTA, so the cut can't fit at 96.
- Cut from v6: the ladder, the rowboat, "took what she loved / left me with the rest", the thunder verse, "the happiest I've seen", the "As is. Her date." tag. The end card and stamps still carry the terms.
- CLOSE C now starts with its open's words ("No more roofers..."), per the loop rule.

## Lyrics with loop labels and tags

```
[Verse 1]
[OPEN A]   PAIN   Forty-two years old, and I wet her bed again,
[payload]  PAIN   Since that hailstorm hit, I can't hold it in,

[Chorus]
[OPEN B]   PAIN   She sleeps on the couch, a bucket by her chair,
[payload]  PAIN   Christmas at her sister's, ashamed to have it there.

[Verse 2]
[OPEN C]   PAIN   Three roofers, two tarps, and a whole lotta talk,
[payload]  PAIN   Every patch sent the leak out for a walk,
[CLOSE C]  PLANE  No more roofers, I sell just as I am,
[payload]  PATH   So she picked her own closing date and got out of that jam.

[Chorus, mirrored]
[CLOSE B]  DEST   She sleeps in her bed, no bucket by her chair,
[payload]  DEST   Christmas at her new place, the whole family's there.

[Outro]
[CLOSE A]  DEST   And me? I'm forty-three, happy for her, understand,
[payload]  DEST   Her bucket's at the beach, buildin' castles in the sand.

[CTA, voice-over in the edit]
[CTA]      PATH   What year was your house built? Ask for a cash offer. No obligation.
```

**Measured (script, 2026-10-13):** 127 words (114 sung + 13 CTA). Tag split PAIN 55 (43.3%) · PLANE 9 (7.1%) · PATH 26 (20.5%) · DESTINATION 37 (29.1%), inside the cold budget of `sell-fear.md`. Lines 10-14 syllables. Every couplet rhymes (again/in is slant). 0 shared four-word phrases with 13 reference transcripts.

**Length (estimate):** 12 lines x 2 bars at 108 BPM = 53.3 s of singing; the 13-word CTA voice-over is 5.2 s at 2.5 words/s; total about 58.5 s. Suno decides the real length; the edit cuts the intro and any instrumental gaps on whole bars, and the final cut is measured.

## Suno

- Lyrics box: `10_Video_Builds/Ad27_Song_Ruthie/suno_lyrics_v7_60s.txt`
- **Tone changed 2026-10-13 (user): sea shanty, like Nathan Evans' "Wellerman" (feel only; no melody, recording, soundalike or names).**
- Style: `Sea shanty, stomping folk, 108 BPM, warm male baritone lead, rowdy male crew on the chorus, foot stomps, hand claps, fiddle, accordion, playful, clear diction`
- Exclude: `EDM, electronic drums, autotune, pop production, rap, lo-fi`
- Old country-soul style (superseded): `Midtempo country-soul confession, 108 BPM, warm male baritone, sheepish and playful, pedal steel, brushed drums, acoustic guitar, clear diction, sparse arrangement`
- Suno free plan = audition only (no downloads, no rights; recording is banned by Suno's terms). Free route with downloads: ElevenLabs Music free plan (5 lossless downloads a day; commercial use with an ElevenMusic credit, ElevenLabs blog 2026-09-11). Paid route: Suno Pro.
- Video: 3 faceless Gemini-website prompts, 30 s each: `10_Video_Builds/Ad27_Song_Ruthie/gemini_web/Ad27_PART1-3_gemini_30s_v1.txt`.

## Video script

`10_Video_Builds/Ad27_Song_Ruthie/video_script_v7_60s.txt` (12 lines, ~60 shots of 1-2 beats, Chorus 2 copies Chorus 1's camera angles).
