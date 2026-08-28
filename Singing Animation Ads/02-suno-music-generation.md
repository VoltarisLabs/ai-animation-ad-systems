# Generating the Track in Suno

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-29
**Covers:** lyrics → finished song track (the step between `/singing` and `/crochet`)

---

## Setup

1. Go to **suno.com**
2. Sign up
3. **Use the Pro plan.** The course recommendation, with two reasons:
   - **Better results** — paid gives access to their best model
   - **2,500 credits instead of ~50** — you can test a lot more songs

> *"It's cheap, and it gives you much better results than the free plan."*

---

## The workflow

1. Go to the **Advanced tab**
2. **Lyrics box** → paste the copy from the brief (the `/singing` output)
3. **Styles box** → tell the model what kind of style you want
4. *(Optional)* add a **negative style** below that, or play with the settings — not strictly necessary
5. **Generate.** Change prompts and settings as needed.

---

## 💡 The styles-box tip

> *"I like using Claude to write this based on the inspiration I have, since I personally often lack the musical vocab that the model understands well."*

**This is already handled for us.** `/singing` outputs a **SUNO STYLE PROMPT** field per option, built to the formula:

```
[genre], [vocal style], [tempo/BPM], [mood], [production style]
```
Under 25 words — Suno does better with concise style prompts.

So the `/singing` output drops straight into both boxes: LYRICS → lyrics box, SUNO STYLE PROMPT → styles box.

---

## ⚠️ Three pitfalls (verbatim)

### 1. Never name real popular tracks as inspiration
**Suno will reject them for copyright.** Describe the style you want in the styles box instead.

> This is exactly why the styles-box vocabulary matters — you have to say *"upbeat electro-pop, bright female lead, 128 BPM, confident, modern polished"* rather than *"sounds like [artist]."*

### 2. Don't use the free version
The paid plan gives access to their best model, which produces the best results.

### 3. Check pronunciation across the whole song
**Go through the entire song and verify every word is pronounced correctly.**
The course's example of a word the model struggles with: **"ashwagandha."**

---

## 🚨 Pronunciation risk for Altura

This is the **same warning the ElevenLabs lesson gave**, and it bites harder here — you can't re-read a single line in a sung track, you have to regenerate.

Words to check in any Altura song ad:

| Word | Risk |
|---|---|
| **Altura** | The brand name. Must land as *al-TOO-rah*. |
| **APR** | 3-letter acronym — may be sung as a word instead of letters |
| **0%** | May render as "zero percent" or "oh percent" |
| **pre-qualification** | Long, easy to slur when sung |
| **hard inquiry** | Core mechanism — must be intelligible |

**Fix method:** respell phonetically in the lyrics box (e.g. `Al-too-rah`) and regenerate. Same technique as ElevenLabs.

**Why this matters more than usual:** our unique mechanism *is* "pre-qualification with no hard inquiry." If that phrase is unintelligible when sung, the ad has no differentiator left — it becomes exactly the generic song the SOP's Step 10 warns about.

---

## Where this sits in the combined pipeline

```
/singing   → lyrics + Suno style prompt + visual idea
    ↓
► SUNO     → generate track, check pronunciation, pick the best take
    ↓
/crochet   → lyrics become the phrase list → storyboard frames + I2V prompts
    ↓
Images (Nano Banana Pro) → Video (Seedance 2.0)
    ↓
Assembly: cut clips to the track's beat, export 9:16 1080×1920
```

🚨 **Lock the Suno track BEFORE generating any video.** In a song ad the music sets the cut points, so clip lengths come from the finished track. Generating video first means paying twice.

---

## Cost note

Suno Pro is a **separate subscription, not KIE credits.** Not yet set up.

The 2,500-credit argument is the real one for us: song generation is iterative — wrong genre feel, bad pronunciation, weak hook delivery all mean regenerating. On ~50 free credits there is no room to iterate, and a bad take would get shipped.

🚨 **No subscription purchase or paid API call without Rafiul's explicit typed approval.**
