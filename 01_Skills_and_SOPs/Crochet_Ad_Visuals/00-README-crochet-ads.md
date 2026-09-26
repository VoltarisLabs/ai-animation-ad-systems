# AI Animation — Crochet Style Ads

**Skill:** `crochet-ad-visuals-SKILL.md` (Ad Creators Lab, saved 2026-08-28)
**Slash command:** `/crochet` (installed at `.claude/skills/crochet/`)

**Lessons:**
- `01-sop-script-to-storyboard-to-video.md` — the 14-step team SOP for running this skill end to end
- `02-hall-of-fame-ad-review-loop.md` — course close, post to Ad Reviews before spending budget

> ⚠️ **Note from the lesson:** the reference ad is a **combination of the crochet framework + the singing framework.** The singing framework is a separate resource — **not yet received.** Drop it in this folder when it arrives.

---

## What this format is

A fully handmade **crocheted and knitted miniature diorama** world. Every surface, character, object, and skin is visible yarn stitches and fabric loops. No realistic skin. No smooth surfaces. No photorealistic textures anywhere.

You give it an ad script, it gives you a complete production storyboard: image prompts + image-to-video prompts.

---

## 🚨 The single most important rule

**Frame the world as a "stop-motion diorama" — NEVER as "crocheted characters."**

And **never describe "knitted skin" directly.** It produces inconsistent results. The diorama framing carries the yarn texture across the character automatically.

This is counterintuitive and it's the rule that separates working output from failed generations.

---

## The 3-step flow

| Step | What happens |
|---|---|
| **Step 0** | Character question — A (user describes) / B (skill suggests) / C (no consistent character). **Wait for the reply.** |
| **Step 1** | Phrase-by-phrase breakdown. 5 visual ideas per phrase, bulleted, never paragraph-mashed. User replies `Phrase 1: 2, Phrase 2: 4...` |
| **Step 2** | Full storyboard per chosen visual — character prompt (once), director's note, start frame, end frame (Type B only), I2V prompt |

---

## The 3 scene types (director's decision)

| Type | When | Output |
|---|---|---|
| **A** | Motion is self-contained — starts and ends in the SAME visual state (vapor erupts then dissipates, flame ignites then burns out) | 1 start frame + I2V with full motion arc |
| **B** | State changes — begins one stable state, lands in a different stable state (bottle on counter → bottle in hand, neutral face → grimace) | Start frame + **end frame** + I2V transition |
| **C** | Held or near-still shot — hero shot, product sitting, confident pose | 1 start frame + I2V with subtle motion (yarn fiber sway, slow push, breath) |

**Critical rule for Type B:** the end frame is the **FINAL LANDED state, never mid-motion.** If the end frame says "vapor mid-dissipation" or "hand reaching" — that's wrong. Push to the resolved state, or reclassify as Type A.

**Default to Type A when unsure** — fewer images, and modern I2V handles full motion arcs from one keyframe.

---

## The 3 universal excerpts (bake into EVERY prompt)

### Universal Positive — every image prompt
> The entire scene is fully crocheted and knitted — every surface, character, object, and skin is made of visible yarn stitches and fabric loops. No realistic skin, no smooth surfaces, no photorealistic textures anywhere in the frame. Every element, including hands, arms, faces, and backgrounds, must have visible knit and crochet stitch texture throughout. Stop-motion animation diorama scene, handmade knitted and crocheted miniature world.

### Universal Negative — every image prompt (models that support it)
> realistic skin, smooth skin, photorealistic hands, photorealistic faces, realistic textures, smooth surfaces, CGI render, claymation, clay texture, Pixar style, Disney style, 3D animation, plastic texture, flat cartoon, airbrushed, anime, illustrated, 2D, studio lighting, ring light, HDR, symmetrical lighting, harsh shadows, perfectly exposed.

### Universal I2V Closing Line — end every video prompt
> Ensure the entire scene remains fully crocheted and knitted throughout every frame — all characters, objects, and surfaces must retain visible yarn stitch texture with no realistic or smooth surfaces at any point. Non-CGI. Non-cinematic. Animations must start at the first frame. Non-disney.

---

## Prompt structures

**Image prompt — 5 parts, in this order:**
1. Scene-specific description (what, who, where, props)
2. Universal Positive (verbatim)
3. Lighting (one template from below)
4. Universal Negative (verbatim)
5. Product reference tag `@image1` when the real product is in scene

**I2V prompt — 4 parts, in this order:**
1. Primary motion — what moves, how, at what pace
2. Secondary elements — what stays still, what reacts subtly
3. Camera — locked, slow push, or slow pull. Keep minimal.
4. Universal I2V Closing Line (verbatim)

---

## Lighting templates (use exactly ONE per scene)

Always a **single motivated light source**:

| Scene | Template |
|---|---|
| Daytime indoor | soft natural light from a small diorama window to the left |
| Bar / evening interior | warm motivated light from tiny knitted overhead pendant lamps |
| Night street | warm soft glow from tiny crocheted streetlamps |
| Bathroom / clean indoor | soft cool flat natural light from a window to the left |
| Outdoor day | soft diffused daylight from above-left |
| Cozy living room | warm lamplight from a tiny knitted floor lamp in the corner |

**NEVER:** studio lighting, ring light, HDR, symmetrical lighting, harsh shadows, perfectly exposed.

---

## Battle-tested model limitations (Section 4 — apply to every prompt)

1. **Diorama framing, not "a crocheted man."**
2. **Never describe knitted skin directly.**
3. **Avoid complex arm/hand poses.** The model can't render fingers in yarn texture. Allowed: standing, sitting, single-arm gestures, leaning, walking. Banned: pointing with multiple fingers, intricate hand actions, two-handed manipulation of small objects.
4. **Particle clouds and explosions fail** — the model defaults to CGI smoke/burst. Replace with **individual yarn ball orbs**, "floating" or "hovering."
5. **Scent/evaporation effects do not work.** Use **character-based storytelling** instead — character sniffs wrist and grimaces (before), lifts collar and smiles (after). Far more reliable than rendering particles.
6. **No dense molecule clouds.** A small handful of yarn ball orbs in product-matching colors.

### Yarn ball orb rules
- Small, round, yarn-textured, slightly varied size
- Color matches product: amber = fragrance · blue = hydration/cooling · green = freshness · gold = luxury/energy · white = purity
- Quantity: a small handful. Never fill the frame.
- Motion: drift lazily, bob gently, hover. Never violent bursts.
- "Before" scenes: orbs evaporate / fade. "After" scenes: orbs persist and drift.
- Never call them: glass particles, CGI sparkles, realistic mist, smoke, vapor cloud. Say **yarn cloud** or **yarn ball orbs**.

---

## Models

| Purpose | Skill recommends | Our KIE status |
|---|---|---|
| Image | **Seedream 4.5** (best, supports negative prompts) | ⚠️ not verified on KIE |
| Image (alt) | Nano Banana Pro | ✅ working, ~$0.09 |
| Image (alt) | ChatGPT / DALL-E | n/a |
| Image-to-video | **Seedance 1.5 Pro** (cheapest reliable) | ⚠️ not verified on KIE |
| I2V (alt) | Kling | 🔴 **DOWN** — 500 error (2026-08-27) |
| I2V (alt) | Veo | ✅ working, 🚫 course-banned elsewhere |
| I2V (our workhorse) | Seedance 2.0 | ✅ working, $0.205/sec |

**Negative-prompt problem:** the skill leans on Seedream 4.5 specifically because it **supports negative prompts**, and the Universal Negative is doing heavy lifting here (it's what blocks CGI/claymation/Pixar drift). Nano Banana Pro has no negative-prompt field. Workaround: fold the negatives into the positive prompt as explicit exclusions ("no realistic skin, no smooth surfaces, no CGI render, no claymation…"). Weaker, but it's what we have unless Seedream 4.5 turns out to be on KIE.

**Action item:** verify `seedream-4.5` and `seedance-1.5-pro` on KIE. Both would materially improve this workflow — one for negative prompts, one for cheap I2V.

---

## Production tips (from the skill)

- **Always upload the character reference alongside every frame prompt** (or `@image1` in Seedream)
- Upload the real product photo as `@image1` for product shots
- **Generate each frame 2-3 times, pick the best** — budget for this
- If a result looks too realistic or CGI → **emphasize "stop-motion diorama" framing harder**
- Stitch in CapCut / Premiere / ffmpeg

---

## How this compares to our other two formats

| | Seedance UGC | Skeleton Ads | **Crochet** |
|---|---|---|---|
| Look | Real human, iPhone UGC | 3D cartoon skeleton | Knitted stop-motion diorama |
| Voice | Native Seedance in-shot | ElevenLabs narrator VO | (script-driven; singing framework pending) |
| Consistency device | Pinterest ref → @Image1 | Character Bible + hero image | Character ref image + diorama framing |
| Frames per scene | 1 (continuous take) | 1 | **1 or 2** (Type B needs an end frame) |
| Scroll-stop power | Low-medium (credibility play) | High | **High** (pattern interrupt) |
| Best for | Advisor trust | Viral reach | Viral reach, novelty |

Crochet is the only one of the three with a **two-frame** option, and that's the main new production cost to plan around — Type B scenes need double the image generations.

---

## ⏳ Still missing

- **Singing framework** — the reference ad combines crochet + singing. Not yet received.
