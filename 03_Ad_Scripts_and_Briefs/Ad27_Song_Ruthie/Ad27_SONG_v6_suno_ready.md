# Ad 27 v6: "Let Me Go", Suno-ready lyrics + video script

Status: 2026-10-13, replaces v5 after a lyric check (the user's ask: "properly check if the lyrics are okay"). Checked by script and by a songwriter review agent. Nothing generated yet.

## What changed from v5 and why

| v5 | v6 | Why |
|---|---|---|
| "...and a tub of caulk" | "...and a whole lotta big talk" | sung, "caulk" can sound like a vulgar word next to "wet her bed" (ad rejection risk) |
| "made one call, and bam!" | "and got out of that jam" | "one call... bam" reads as a speed/ease claim; the registry bans speed |
| "Left the boxes, left the buckets" | "Left the boxes and the clutter" | contradicted her bucket at the beach |
| "her house is full of noise" | "her new place full of noise" | "her house" sounds like the singer |
| "The only mess she's got now is..." | "Only mess she's got is..." | 14 -> 11 syllables, matches its pair (10) |
| bucket line alone at the end of Verse 3 | moved into the Outro with its rhyme partner | Suno restarts the melody at each section tag |
| "...and I'm happy for her, understand" | "...happy for her, understand" | 15 -> 13 syllables |
| (none) | "Just as I am, she's the happiest I've seen," | the hook comes back once, and "clean" finally rhymes (seen/clean) |
| CTA under [Spoken Word] in Suno | CTA recorded as voice-over in the edit | Suno often sings or garbles spoken parts; the CTA must be word-exact |
| "As-is." | "As is." in the Suno box | hyphen may get clipped (untested); captions keep "As-is" |

## Lyrics with loop labels and tags

```
[Verse 1]
[OPEN A]   PAIN   Forty-two years old, and I wet her bed again,
[payload]  PAIN   That hailstorm cracked my roof, and now I just can't hold it in,
[OPEN B]   PAIN   She sleeps on the couch now, with a bucket by her chair,
[payload]  PAIN   Moved Christmas to her sister's, too ashamed to have it there.

[Verse 2]
[OPEN C]   PAIN   Three roofers, two tarps, and a whole lotta big talk,
[payload]  PAIN   Every patch just sent the leak out for a walk,
[payload]  PAIN   She kept on fixin' me when she should've let me go,
[payload]  PAIN   Patchin' me was bailin' out a boat that's got a hole.

[Chorus]
[CLOSE C]  PLANE  Then she found out I sell just as I am,
[payload]  PATH   So she picked her closing date and got out of that jam,
[payload]  PATH   No fixin', no cleanin', she just took what she loved best,
[payload]  PATH   Left the boxes and the clutter, left me with the rest.

[Verse 3]
[CLOSE B]  DEST   Thunder rolled last night, and she slept right through,
[payload]  DEST   Rain on her window, but her pillow's dry and new,
[payload]  DEST   Christmas is back, her new place full of noise,
[payload]  DEST   Only mess she's got is grandkids and their toys.

[Outro]
[payload]  DEST   Her bucket's at the beach, buildin' castles in the sand,
[CLOSE A]  DEST   And me? I'm forty-three, happy for her, understand.
[payload]  DEST   Just as I am, she's the happiest I've seen,
[payload]  PLANE  As is. Her date. Nothin' left to clean.

[CTA, voice-over in the edit]
[CTA]      PATH   What year was your house built? Ask for a cash offer. No obligation.
```

**Measured (script, 2026-10-13):** 216 words (203 sung + 13 CTA). Tag split PAIN 87 (40.3%) · PLANE 18 (8.3%) · PATH 47 (21.8%) · DESTINATION 64 (29.6%), inside the cold budget of `sell-fear.md`. Lines 9-14 syllables (v5: 9-15). Every couplet rhymes (again/in and go/hole are slant). 0 shared four-word phrases with 13 reference transcripts. Sung length about 104.0 s at 117.1 wpm (estimate; Suno sets the real length).

**Loops:** A, B, C, close C, close B, close A, CTA, with a payload between each.

**Claims:** as v5 (as-is, no fixing, no cleaning out, she picks the closing date, take what you love and leave the rest, no obligation, ask for a cash offer). Not in the script: "we buy", speed, "any condition".

## Suno

- Paste files: `10_Video_Builds/Ad27_Song_Ruthie/suno_lyrics_v6.txt`; style and exclude as in v5.
- **Free plan (checked live 2026-10-13, suno.com/pricing + help.suno.com/en/articles/2425729):** 50 credits a day, model v6-mini only, no downloads, no stems, no commercial rights, and upgrading later does not license songs made on the free plan. So free = audition by ear only.
- **Final:** regenerate on Pro or Premier (v6), download there into `Singing_ads/`, then the 3 hooks (Remix > Use as Inspiration 85%) and stems.

## Video script

`10_Video_Builds/Ad27_Song_Ruthie/video_script_v6.txt` (20 lyric lines + end card, cast refs `Singing_ads/Ad27_Cast_12panel_v2_edited.png` + the Gemini Linda master). Shot timing follows `shot_plan_v5.md` until the real song exists.
