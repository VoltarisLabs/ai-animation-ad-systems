# AI Animation — Skeleton Ads

**Skill:** `skeleton-ads-SKILL.md` (Ad Creators Lab, saved 2026-08-28)

**Lessons:**
- `01-skeleton-ad-director-lesson.md` — install skill, generate script (Stage 1)
- `02-script-to-consistent-ai-images.md` — script → consistent images (Stage 2 → 3)
- `03-image-prompts-to-video-clips.md` — images → video clips + automation (Stage 4)
- `04-elevenlabs-voiceover.md` — VO line list → finished voiceover (assembly step 1)

**Slash command:** `/skeleton` (installed at `.claude/skills/skeleton/`)

---

## What this format is

A **30–60s vertical (9:16) video** where a recurring **literal 3D cartoon skeleton** lives out an escalating second-person journey, narrated by one voiceover:

> *"What happens if you ___? Day 1… Day 30… Day 365…"*

Borrowed from viral "What happens if you ___?" YouTube Shorts. Completely different from our talking-head advisor format.

---

## 4 stages, one chat

| Stage | Input | Output |
|---|---|---|
| **1 — Script** | Product website / research doc / objection list | Angle + skeleton script + numbered VO line list |
| **2 — Visual Concept Board** | Approved script pasted back | Style + theme + per-line shot grid |
| **3 — Image Prompts** | Chosen concepts | Character Bible + hero image + one prompt per shot |
| **4 — Video Prompts** | "Images are done" | One image-to-video prompt per VO line + assembly checklist |

**Never skip stages.** Each ends with a hand-off telling you exactly what to bring back.

---

## The 4 mechanics every script must hit

| | Mechanic | What it means |
|---|---|---|
| **A** | **Curiosity-gap hook** | *"What would happen if you ___?"* — a question the brain needs closed |
| **B** | **Escalating progression spine** | Time (Day 1 → 30 → 365) · Quantity (1 → 15 → 42) · Stage (1 → 5) |
| **C** | **Visceral concrete specifics** | One physical sensory image per beat, never an abstract claim |
| **D** | **A payoff** | Triumph (transformed, crowned) OR catastrophe (system failure) |

---

## Angle selection — diagnose the product first

| If the product… | Angle | Spine | Payoff |
|---|---|---|---|
| Benefit compounds over time | **Transformation** | Time | Triumph |
| Painful worsening status quo | **Cost-of-inaction** | Time | Catastrophe |
| People overdo a broken old way | **Limit / overload** | Quantity | Catastrophe |
| Vivid in an unexpected world/era | **Origin / scenario** | Time/Stage | Triumph |

**Never default to one arc.** Often fuse two.

---

## The craft: B2B benefit → visceral image

| Abstract benefit | Skeleton-ad image |
|---|---|
| Saves time | *"You blink and the work's already done. You stare at an empty to-do list, twitching."* |
| Reduces churn | *"Customers used to vanish like smoke. Now they're chained to you, grinning."* |
| More qualified leads | *"Day 30: the leads stop trickling. They kick down the door."* |
| Cuts costs | *"Your burn rate was a bonfire. Now it's a birthday candle."* |
| Hard to set up | *"Day 90: still duct-taping spreadsheets. The cracks are spreading up the walls."* |

**Banned words:** revolutionary, seamless, leverage, solution, game-changer.

---

## The "turn" — most important move

Don't bolt the product on at the end. Build tension first, then pivot on a hinge line:
> *"Then you find [product]."* / *"Everything changes the day you [use product]."*

The product must feel like **the answer to the loop you opened**, not an ad break.

---

## 4 skeleton styles (locked Character Bibles in the skill file)

| Style | Best for |
|---|---|
| **1. Bare-Bones Cinematic** ⭐ default | Origin/scenario + transformation ads |
| 2. Dressed Skeleton | Wearable, fashion, lifestyle, identity products |
| 3. X-Ray with Organs | Health, body, biology, supplement, medical |
| 4. Cute Cartoon Mascot | Playful/fun brands only — never silently default here |

**Style guide image:** [drive.google.com/file/d/1cB8Od47Wc3ssdaZQylnyLBoFX_MD0gwF/view](https://drive.google.com/file/d/1cB8Od47Wc3ssdaZQylnyLBoFX_MD0gwF/view)

---

## Character consistency — the whole game

1. **Locked text** — paste the Character Bible block into every prompt word-for-word
2. **Hero reference image** — generate image 1 first, it's the source of truth
3. **Reference the HERO, never the previous image** (stops drift)

| Tool | Mechanic |
|---|---|
| Nano Banana 2 | Attach hero as reference: *"Using the attached skeleton character, keep its exact face, eyes, and bone style. Now show it [action]."* |
| GPT image | Same chat, point to hero, repeat the Bible text each time |
| Seedance (image) | Hero in reference-image slot + Bible as prompt |
| Midjourney | `--cref [hero URL] --cw 100 --sref [URL] --seed [n] --ar 9:16 --v 7` |

---

## 🚫 NO TEXT IN PROMPTS

Never put captions, words, titles, labels, subtitles, watermarks, or UI into image **or** video prompts.

End every image prompt with:
```
no text, no captions, no words, no letters, no watermark, no UI
```

Caption ideas from the Stage 2 board are **editor notes** — added later in Premiere, never baked into generated footage.

---

## Video tools (Stage 4)

| Tool | Use |
|---|---|
| **Kling** | Image-to-video, 5s/10s, subject motion + ONE camera move |
| **Seedance** | Image-to-video, native audio, up to ~15s |
| **Veo** | Strong prompt adherence, ~8s, best for hero/payoff shots |

⚠️ **Our KIE status (2026-08-27):** Kling 2.6 **and** 3.0 both returning 500 Internal Error. Seedance 2.0 works at **$0.205/sec**. Veo 3 Fast works at **~$0.30 flat per generation**.

---

## Assembly checklist

1. Voiceover from the VO line list in **ElevenLabs** (one calm dramatic narrator)
2. Generate each clip from its still; clip ≈ length of its VO line
3. Timeline in order, trim each to land with its VO line
4. *(Optional)* captions added **in the editor** — bold white sans, centered lower-third, thin dark outline, 2–3 words karaoke style
5. Background music — tense/curious under the build, lift at payoff, duck under VO
6. Export **9:16, 1080×1920**

---

## How this differs from our Altura work

| | Seedance UGC (what we built) | Skeleton Ads (this) |
|---|---|---|
| Format | Real human advisor, talking head | 3D cartoon skeleton, narrated |
| Voice | Native Seedance in-shot dialogue | Separate ElevenLabs VO over clips |
| Structure | Client's approved script, C.U.R.E. | Curiosity hook + escalating spine + payoff |
| Character | Pinterest ref → @Image1 | Locked Character Bible + hero image |
| Best for | Credibility, advisor trust | Scroll-stopping, viral reach |

**Possible Altura angle:** *Cost-of-inaction / Time* — *"What happens if you never fix your business credit?"* Day 1 → Day 90 → Day 365, catastrophe payoff, turn on the pre-qualification. Our research doc already has the visceral raw material (*"$0 by 10 AM"*, *"$758 daily drain"*, *"14 months to clear"*).
