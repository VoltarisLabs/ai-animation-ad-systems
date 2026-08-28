# Generating the Voiceover in ElevenLabs

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-28
**Covers:** Assembly step 1 — VO line list → finished voiceover file
**Skill:** `skeleton-ads-SKILL.md`

---

## The 7 steps

### 1. Prepare the script and open ElevenLabs (0:10)
- Copy the **finalized** script (the numbered VO line list from Stage 1)
- Open ElevenLabs → voice generation area
- **Confirm the script is complete before moving forward** — don't generate against a draft

### 2. Choose a voice that matches the audience (0:19)
- Review the available voices
- Pick one that fits the **target demographic and the message**
- Experiment with different styles to find the match

> For story-based content, pick a voice that feels **natural and engaging rather than overly polished.**

### 3. Customize the voice style if needed (0:30)
If no default voice fits, use **voice design / style adjustments**. Define:
- gender and age range
- tone and energy level
- delivery style — assertive, strong, casual, conversational

Test a few variations if the first result sounds too artificial or too formal.

### 4. Generate a sample (0:55)
- Paste the script → **Generate Speech**
- Listen and compare against the intended tone
- **Too professional / too AI-like → adjust the style and regenerate**

### 5. Refine the tone for realism (1:09)
- Shift toward **casual and conversational**
- Target: sounds like a real person speaking naturally
- Match the content — e.g. someone casually sharing something interesting
- Regenerate until it's believable

### 6. Enhance and finalize (1:26)
- Use the **Enhance** option if available
- A/B the enhanced version against the original
- Generate the final once tone and pacing feel right
- Download the file

### 7. Review the final audio (1:48)
Listen start to finish and confirm:
- ✅ every word pronounced correctly, **especially brand names**
- ✅ pacing, tone, and clarity match expectations

Anything off → back to the generator before handing off.

---

## ⚠️ Cautionary notes (verbatim from the lesson)

- **Do not assume the first generated voice will be the best fit** — AI voice output may require several iterations
- **Always verify pronunciation of brand names, product names, and specialized terms**
- **Avoid a voice that sounds too polished** if the content needs a casual or authentic feel
- Make sure the voice matches the intended audience and content type

---

## Altura-specific application

### Brand-name pronunciation risk 🚨
**"Altura"** is the exact kind of word this lesson warns about. Check it renders as **al-TOO-rah**, not "al-TYUR-ah" or "AL-chur-ah". If it drifts, fix with SSML-style phonetic spelling in the input text (e.g. `Al-too-rah`) and regenerate.

Also verify: **"APR"**, **"0%"**, **"pre-qualification"**, **"hard inquiry"**.

### Voice direction for a skeleton ad
The skill says: *"one calm, dramatic narrator voice."*

That is **not** the same brief as our talking-head ads. Skeleton ads are narrated over cartoon footage, so:

| | Seedance UGC advisor (what we built) | Skeleton ad narrator |
|---|---|---|
| Source | Native Seedance in-shot dialogue | Separate ElevenLabs VO |
| Feel | Credible advisor, trustworthy | Calm, dramatic, storyteller |
| Energy | Warm professional | Building tension → payoff lift |
| Reference | Female advisor, whiteboard | Documentary/creepypasta narrator |

The lesson's "don't be too polished" note matters here. A corporate-finance-announcer read will kill a skeleton ad. The swipe file (creatine, braces, never-cleaned-room) is all **casual guy telling you something wild**, not a brand voice.

### Candidate voices (finance/narration, already noted in memory)
- **Brian** `nPczCjzI2devNBz1zQrb` — used on our Altura work
- Adam · Eric · Roger

For skeleton the pick may differ — leaning casual-conversational over authoritative.

---

## Our API path

KIE's ElevenLabs wrapper is **broken** (repeated 500s, tested 2026-08-25). Use the **direct ElevenLabs API**:

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
header: xi-api-key: <key>
```

Key location: memory `elevenlabs-api-key.md`.

**Line-by-line, not one blob.** Generate **one file per VO line** — the skill's line list exists so each line becomes one clip. Separate files make trimming to picture trivial in Premiere; a single blob forces manual splitting.

🚨 **No API call without Rafiul's explicit typed approval.**

---

## Where this sits in the pipeline

```
Stage 1  script + VO line list
Stage 2  visual concept board
Stage 3  hero image + scene images        (Nano Banana Pro)
Stage 4  video prompts → clips            (Seedance 2.0)
   ↓
► THIS LESSON: VO from the line list      (ElevenLabs direct API)
   ↓
Assembly: timeline, trim to VO, captions in Premiere, music, export 9:16 1080×1920
```

The VO can be generated **in parallel with Stage 3/4** — it only depends on the Stage 1 line list, not on the images. Doing it early also catches pronunciation problems before any video credits are spent.
