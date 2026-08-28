# Claymation — Video Stage

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-29
**Covers:** claymation images → animated clips

---

## The 5 steps

### Step 1 — Upload your images
Take the claymation images and put them into your video tool (e.g. Max Fusion).

### Step 2 — Pick a video model
- **Kling 3.0** — best quality
- **Seedance** — cheaper option

### Step 3 — Set start + end frames
```
Start frame = current scene
End frame   = next scene
```
👉 **This creates the transition between them.**

> Each scene image serves twice — as one clip's end frame and the next clip's start frame. That chaining is what makes the ad flow continuously instead of hard-cutting.

### Step 4 — Set duration
- Keep it **short: 3-4 seconds**
- **Don't waste credits on long clips**

### Step 5 — Add animation prompts

**Structure — follow this exactly:**
```
[Visual direction] + [camera directions] + Ensure handmade stop-motion clay animation
throughout the video. Non CGI. Non cinematic. Animation must start at the first frame.
Non-disney. Non cartoon.
```

**If a character is involved, include verbatim:**
> *"Keep character facial consistency. No character redesign. No facial feature changes."*

**Camera directions (pick one):**
1. **Static** — stays still
2. **Slight push-in** — camera moves towards subject (often confused with zoom in)
3. **Slow pan left** — stationary camera that horizontally rotates to the left
4. **Arc right**

**Must include animation directions — verbatim:**
> *"Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon."*

---

## What's new vs the Canva SOP

This lesson confirms the same prompt structure and camera list, with **two changes worth noting:**

**1. Seedance is now named as an acceptable model.** The Canva SOP specified Kling 3.0 only. This lesson says *"Use something like Kling 3.0 (best quality), or cheaper option like Seedance."*

**That partially unblocks us.** Kling is down on KIE, but Seedance 2.0 works. The open question stays: does Seedance 2.0 support an **end frame**? Step 3's start+end chaining is the core mechanic, and without an end-frame parameter only single-frame clips are possible.

**2. Duration guidance is tighter — 3-4 seconds.** The Canva SOP derived clip length from audio section length (3-5s → 1 clip, 6-9s → 2 clips). This lesson just says keep clips short and don't waste credits. The two agree in practice: short clips, chained.

---

## Cost on our stack

Seedance 2.0 is **per-second at $0.205/sec**:

| Clip length | Cost per clip |
|---|---|
| 3s | $0.62 |
| 4s | $0.82 |

A 10-scene claymation ad at 4s per clip = **$8.20** of video, plus ~$1-2 of Nano Banana Pro images. Roughly **$10** per full ad, no retries.

Balance is **$20.68** — enough for one ad plus a partial retry round. The lesson's "don't waste credits on long clips" advice is doubly true for us, since Seedance charges by the second while Kling charges flat per clip.

---

## Claymation section status

| File | Covers |
|---|---|
| `00-README-claymation-SOP.md` | Full Canva SOP: ChatGPT → NanoBanana 2 → Kling 3.0 |
| `01-claymation-storyboard-workflow.md` | Script → storyboard images (7 steps) |
| `02-claymation-gpt-link.md` | The ready-made Claymation GPT + what we can't extract |
| `03-poppy-board-workflow.md` | Poppy Board route (subscription, not held) |
| `04-claymation-video-stage.md` | This file — images → clips |

**Pipeline now documented end to end.** Script → scenes → image prompts → images → clips.

### Remaining blockers
1. **Does Seedance 2.0 support an end frame?** If yes, the chaining mechanic transfers and claymation is fully producible on our stack. If no, we get single-frame clips only and lose the continuous-flow look. **This is the one question that decides whether this format is viable for us.**
2. **Kling 3.0 on KIE** — 500 error as of 2026-08-27, worth a recheck.
3. **The "THIS document"** — still needed for a local `/claymation` skill. Route A (Claymation GPT in browser) works without it.

🚨 **No API call without Rafiul's explicit typed approval.**
