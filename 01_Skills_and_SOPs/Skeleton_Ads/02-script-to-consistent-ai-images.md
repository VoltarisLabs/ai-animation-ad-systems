# How to Turn a Script Into Consistent AI Images for an Ad

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-28
**Covers:** Skill Stage 2 (Visual Concept Board) → Stage 3 (Image Prompts)
**Skill:** `skeleton-ads-SKILL.md`

---

## The 8 steps

### 1. Start with a script and generate recommended styles (0:00)
After inserting/choosing a script in the skill, it first suggests **recommended styles**.
- Click the style image/link to open the menu and pick a different visual style
- The tool then creates a **line-by-line breakdown** of the script covering: situations · emotions · settings · props · product mentions

> **Quality lever:** the breakdown gets better the more context you add and the more you talk back and forth with the tool about what you want. Don't accept draft 1.

### 2. Generate prompts for each scene (0:58)
Use a command like:
```
generate images for 1, 2, 3
```
Output:
- a **prompt for each shot**
- a **character bible** for the main character

The character bible keeps the character visually consistent across all images.
**The prompt is model-agnostic** — even though the skill names a specific model, it works with any image generator.

### 3. Create the FIRST character image to lock in consistency (1:37)
- Copy the character bible → paste into your image generator
- **Generate image 1 BEFORE any scene images**
- This first image becomes the visual reference for the whole ad

> Demo uses MaxFusion with **Seedream 4.5** as a cheap test model. → **Our substitute: Nano Banana Pro on KIE (~$0.09)**.

### 4. Review the character, then use it as a reference (2:11)
- Check the generated character actually matches what you want
- Adjust before moving on — do NOT proceed on a "close enough" hero

For every next scene, copy **three things**:
1. the character bible
2. the scene-specific prompt section
3. **the reference image**

> **Why:** prompt-only generation causes small character differences between shots. Reference-based is the preferred workflow.

### 5. Generate the remaining scene images with the same character (2:55)
- Same character reference for every new shot
- You can test different image models to see how the style shifts

Models shown in the demo:
- Seedream
- GPT-Image2
- NanoBanana2

Goal: **character stays visually consistent** while each shot still matches its own scene and style.

### 6. Build out the full sequence and add missing shots (3:20)
Once the first few images look right, generate the rest.

After reviewing the set, **identify missing coverage**. Examples the creator found:
- a community shot
- a POV screen shot

Add extra prompts for those missing moments so the ad feels complete.

> This is a real step, not optional polish. The script's VO lines are not always the full shot list.

### 7. Automate if you have the tools, else prompt manually (4:23)
- With **Higgs Field, MaxFusion MCP, or APIs** → automate; send instructions straight through Claude Code / Claude
- Without them → do it manually: write prompts directly, use the layout shown in the demo

Either works. **The key is keeping the workflow organized and consistent.**

> **Our setup:** we have the KIE API + Claude Code, so we're on the automated path. Python fire-scripts, same pattern as `output/broll_v2.py`.

### 8. Move from images into video (4:46)
Once the image set is complete, image generation is finished and the process transitions into ad video production (Stage 4).

---

## Our tool mapping (KIE, not MaxFusion)

| Lesson says | We use | Cost |
|---|---|---|
| MaxFusion + Seedream 4.5 (cheap test) | **Nano Banana Pro** on KIE | ~$0.09/image |
| GPT-Image2 | Nano Banana Pro | ~$0.09 |
| NanoBanana2 | **Nano Banana Pro** (same family) | ~$0.09 |
| Higgs Field / MaxFusion MCP | **KIE API + Python fire-scripts** | — |
| Image → video | **Seedance 2.0** | $0.205/sec |

**Nano Banana Pro reference mechanic on KIE:**
```json
{
  "model": "nano-banana-pro",
  "input": {
    "prompt": "<CHARACTER BIBLE verbatim> + <scene action/framing/setting/lighting>. Reference image 1 for the character. no text, no captions, no words, no letters, no watermark, no UI",
    "image_input": ["<HERO IMAGE URL>"],
    "aspect_ratio": "9:16",
    "resolution": "2k",
    "output_format": "png"
  }
}
```
Host the hero on catbox.moe, then pass that URL in `image_input` for **every** later shot.

---

## Hard rules (repeated from the skill, do not break)

1. **Hero image first.** Never generate scene images before the hero is approved.
2. **Reference the HERO, never the previous image.** Referencing the previous shot compounds drift.
3. **Character Bible pasted verbatim** in every prompt — not paraphrased, not shortened.
4. **NO text in prompts.** Every image prompt ends with `no text, no captions, no words, no letters, no watermark, no UI`. Captions go in Premiere later.
5. **Product photo as a second reference** in any shot where the product appears.

---

## Cost planning for an Altura skeleton ad

Assume a 7-line VO script → 1 hero + 7 scenes + 2 gap-fill shots = **10 images**.

| Item | Qty | Unit | Total |
|---|---|---|---|
| Nano Banana Pro images | 10 | $0.09 | **$0.90** |
| Seedance image-to-video (avg 4s/clip × 9 clips) | 36s | $0.205/s | **$7.38** |
| ElevenLabs VO | 1 | ~$0 | ~$0 |
| **Total** | | | **~$8.28** |

⚠️ Retries not included. Budget ~30% headroom → **~$11**.
🚨 **No API call without Rafiul's explicit typed approval.**
