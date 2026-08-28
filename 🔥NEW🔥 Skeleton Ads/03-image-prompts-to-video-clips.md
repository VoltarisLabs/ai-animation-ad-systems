# Generating Video Clips from Image Prompts

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-28
**Covers:** Skill Stage 4 (Video Prompts) + automation
**Skill:** `skeleton-ads-SKILL.md`

---

## The 7 steps

### 1. Generate video prompts for each image (0:00)
Move into the stage where image prompts become video prompts.
Ask the tool: **generate video prompts for all images**.

Output = a **motion description** per image.

> **Keep it simple.** For this style of content you only need basic motion directions, **not complex cinematic instructions.**

### 2. Paste prompt + attach image in your video generator (0:43)
The whole workflow:
```
image + prompt + model = generated clip
```
- Open the video generator
- Paste the video prompt
- Upload / drag the corresponding image
- Pick the model

### 3. Start with the cheapest model first (0:50)
**Recommendation: begin with the lowest-cost model.** Move up only if needed.

| Model | When |
|---|---|
| **Seedance 1.5 Pro** ⭐ | Start here — speaker's personal pick for testing results fast |
| Kling 2.6 | Save credits |
| Kling 3.0 Pro | Best quality |

### 4. Match video duration to the prompt timing (1:09)
The prompt carries a duration. **Set the clip length to match it.**
- Prompt says 4 seconds → generate a 4-second clip
- Keeps motion aligned with the intended shot

Then generate and review.

### 5. Review the clip and adjust (1:38)
- Motion should reflect the prompt (slow push-in, simple movement)
- ⚠️ **Seedance 1.5 may add music automatically.** If you don't want music, prompt for no music or switch to Kling.

### 6. Use simple motion styles (2:29)
**These videos do not need elaborate animation.** Most examples use only:
- a push-in
- slight camera movement around the character

> **Don't overcomplicate the animation style.** The default format works well with simple motion. Change the shot only if you actually want something different.

### 7. Automate with Claude Code + API or MCP (3:03)
Advanced setup: connect Claude Code to an API or MCP.
- Example given: Claude Code → MaxFusion API — automates image generation in the correct order
- Higgs Field MCP works the same way: connect it to Claude and generate assets inside the workflow

Powerful, but more complex if you're new to Claude Code.

> **We're already on this path** — KIE API + Python fire-scripts driven from Claude Code.

---

## Our model mapping (KIE, not MaxFusion)

| Lesson says | Our status on KIE | Cost |
|---|---|---|
| **Seedance 1.5 Pro** (start cheap) | ⚠️ **Not yet verified on KIE** — check before planning around it | TBD |
| **Kling 2.6** (save credits) | 🔴 **DOWN** — 500 Internal Error (tested 2026-08-27) | — |
| **Kling 3.0 Pro** (best quality) | 🔴 **DOWN** — 500 Internal Error (tested 2026-08-27) | — |
| Seedance 2.0 | ✅ **Working** — our current workhorse | $0.205/sec |
| Veo 3 Fast | ✅ Working, but 🚫 **course-banned** for talking/B-roll | ~$0.30 flat |

**Practical read:** the lesson's whole cost strategy is "start cheap, escalate." Right now both Kling tiers are dead on KIE, so our cheap tier is missing. **Action item: verify whether `seedance-1.5-pro` exists on KIE** — if it does, it becomes our test tier and Seedance 2.0 becomes the finish tier. That would cut test-round cost significantly.

---

## Cost math, why step 3 matters

Seedance 2.0 is **per-second** ($0.205/s), so a 4s clip = **$0.82**. Ten clips = **$8.20 per round**.

If a round needs retries — and it usually does — cost doubles. That's exactly why the lesson says test on the cheapest model first and only regenerate the finals on the good one.

| Approach | 10 clips × 4s |
|---|---|
| Everything on Seedance 2.0, 1 retry round | ~$16.40 |
| Test tier first, finals on 2.0 | test cost + $8.20 |

---

## Hard rules for Stage 4

1. **Simple motion only.** One camera move + one subject action per clip. No stacked moves.
2. **Clip length = VO line length.** The prompt's stated duration is the setting, not a suggestion.
3. **No dialogue in video prompts** — VO is recorded separately in ElevenLabs.
4. **No text/captions/words** in video prompts. Captions go in Premiere.
5. **Watch for auto-music** on Seedance and strip or prompt it out — it will fight the VO.
6. 🚨 **No API call without Rafiul's explicit typed approval.**

---

## Assembly (from the skill)

1. VO from the line list in ElevenLabs — one calm dramatic narrator
2. Generate each clip from its still, clip ≈ its VO line length
3. Timeline in order, trim each to land with its line
4. *(Optional)* captions in the editor — bold white sans, centered lower-third, thin dark outline, 2-3 words karaoke
5. Background music — tense under the build, lift at the payoff, duck under VO
6. Export **9:16, 1080×1920**
