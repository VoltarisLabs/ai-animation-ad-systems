# Skeleton Ad Director — Install Skill & Generate Script

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-28
**Skill file:** ✅ `skeleton-ads-SKILL.md` (in this folder)
**Digest:** `00-README-skeleton-ads.md`

---

## What this skill does

Turns a **product website, research document, script, or objection list** into:
1. A **skeleton-style ad script** (with an angle)
2. A **visual concept board** (scene-by-scene visual + on-screen text plan)

---

## Key Steps

### 1. Install the Skeleton Ad Director skill in Claude (0:00)
- Open Claude
- Click the plus (+) icon
- Select **Create skill**
- Choose **Upload skill**
- Upload the Skeleton Ad Director skill file from the provided link
- Confirm the skill is installed before moving on

### 2. Open the skill and start a chat session (0:12)
- After uploading, optionally review the skill instructions
- Click the three dots menu
- Select **Try in chat**
- In chat, type **`/skeleton`** to activate the skill
- Verify the skill is active when the skeleton ad interface appears

### 3. Provide source material (0:22)
Start with one of:
- A script
- A product website
- A research document
- A list of objections

If using a website, copy the page content and paste it into Claude.
Use the best available source material so the skill has enough context.

### 4. Review the generated skeleton-style script (0:57)
Check for the "examine skill" indicator to confirm it's running.

Review the output for:
- An **angle**
- A **skeleton-style script**
- A structure following the expected pattern (e.g. **day 1, day 2, day 3**)

Read the draft carefully — does it fit the product and campaign goal?

### 5. Request a different script style if needed (1:24)
If the first draft isn't a good fit, ask for another version:
> *"Give me a different script"*
> *"Do a script in a different style"*

Keep iterating until tone, structure, and messaging match.

### 6. Generate the visual concept board (1:47)
Once a script is selected, proceed with generation.
The skill creates a **visual concept board** showing what visuals go with each line of voiceover.
Treat it as a **first-draft planning tool**.

### 7. Review scene-by-scene visual + text suggestions (2:01)
Each voiceover line is broken into:
- **Situation**
- **Setting**
- **Product placement**
- **On-screen text suggestions**

Use it to plan shots and creative direction. Not every suggestion must be followed verbatim — it's a strong starting point.

---

## ⚠️ Cautionary Notes

- **Never treat the first generated script as final** — always review for fit and quality
- **Weak or incomplete source material → generic output**
- The visual concept board is a **planning aid, not a mandatory blueprint**
- Confirm the script aligns with **product, audience, and campaign objective** before use

---

## Resources

| Item | Status |
|---|---|
| Claude Skill File | ✅ `skeleton-ads-SKILL.md` (saved 2026-08-28) |
| Style guide image (4 skeleton styles) | [Gdrive](https://drive.google.com/file/d/1cB8Od47Wc3ssdaZQylnyLBoFX_MD0gwF/view) |

**Note:** the lesson video only covers Steps 1-2 of the skill. The actual skill runs **4 stages**: Script → Visual Concept Board → Image Prompts → Video Prompts. See `00-README-skeleton-ads.md`.

---

## How this fits our stack

| Stage | Tool |
|---|---|
| Research → customer language | `Research protocole/` (RESEARCH-DOCUMENT-Altura-v2) |
| Script structure | `frameworks/` (12 scripting frameworks) + client's 15 approved scripts |
| **Skeleton script + visual concept board** | **← this skill** |
| Talking-head UGC production | `ai ugc/` Seedance 2.0 UGC Ad Director skill |
| B-roll | Seedance 2.0 (Kling currently down on KIE) |
| Assembly | Local ffmpeg / Premiere |

**Input we can feed it:** the Altura research doc (100+ verbatim customer quotes) or the client's objection list — both already in `Research protocole/`.
