# Claymation Ads — Script to Storyboard Images

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-29
**Resource for other LLM models:** https://canva.link/m7ozanry62r6k31

> ✅ The Canva resource has been transcribed → **`00-README-claymation-SOP.md`** (the full Claymation SOP: ChatGPT → NanoBanana 2 → Kling 3.0).
> ⏳ Still missing: the **"THIS document"** linked inside that SOP — the actual claymation system prompt that gets pasted into the ChatGPT project as its source.

---

## What you need

| Item | Lesson says | Our stack |
|---|---|---|
| Script (or idea) | — | Client's 15 approved scripts, or `/singing` lyrics |
| LLM | custom GPT / ChatGPT / Claude | Claude Code |
| Image generator | **Nano Banana 2** | ✅ Nano Banana Pro on KIE, ~$0.09 |
| Image editor | for fixing + consistency | Nano Banana Pro edit mode |
| Reference images | for same character | hero image, hosted on catbox.moe |

---

## The 7 steps

### Step 1 — Add your script
- Drop the script into the LLM
- Command: **"turn into claymation storyboard"**
- No script → **ask for ideas instead**

### Step 2 — Get scenes + prompts
The model will:
- break the script into **scenes**
- create **claymation image prompts** for each scene

### Step 3 — Generate images
- Copy prompts
- Paste into the image tool (Nano Banana 2)
- **One image per scene**

### Step 4 — Repeat fast
- Duplicate the prompt
- Run multiple scenes quickly
- Build all images

> Speed is the point of this step. Our KIE fire-scripts already do this — parallel task creation, IDs written to disk immediately.

### Step 5 — Fix images *(optional)*
- Remove elements if needed (e.g. effects)
- Edit images to prepare for animation

### Step 6 — Keep the same character
🚨 **If the character changes:**
1. **Save the image**
2. **Use it as a reference**
3. **Switch to image EDITING, not generation**
4. Generate new scenes with the same person

> This is a different fix than the other frameworks use. Skeleton and crochet both prevent drift up front (locked Character Bible + hero reference). Claymation's method is corrective — when drift happens, you switch modes from generate to edit.

### Step 7 — Prepare for animation
- Download images
- **Separate elements if needed** (for transitions)

---

## Comparison to our other formats

| | Skeleton | Crochet | **Claymation** |
|---|---|---|---|
| Consistency method | Character Bible verbatim + hero ref | Character ref + diorama framing | **Save image → switch to edit mode** |
| Frames per scene | 1 | 1 or 2 (Type A/B/C) | 1 |
| Style enforcement | Locked style block | 3 universal excerpts | ⏳ unknown — prompt not received |
| Structure | Curiosity hook + escalating spine | Phrase → 5 visual ideas | Script → scenes |

---

## ⚠️ Conflict to watch: crochet's negative prompt bans claymation

The crochet Universal Negative explicitly lists:
```
... CGI render, claymation, clay texture, Pixar style, ...
```

That negative exists to stop knitted textures drifting into clay. **The two formats must be kept separate** — never reuse crochet's universal excerpts on a claymation job, and vice versa. When the claymation prompt arrives it will have its own style rules; document them separately rather than adapting crochet's.

---

## Gaps in this lesson

The lesson covers **images only** and stops at "prepare for animation." Not covered:
- the actual claymation style prompt wording (the differentiator)
- image-to-video step — which model, what motion rules
- audio / VO
- assembly

Those either come in a later lesson, or are in the Canva resource.

---

## ⏳ Still needed

1. **The claymation prompt / custom GPT instructions** — the Canva link resource
2. **The video generation lesson**, if there is one

🚨 **No API call without Rafiul's explicit typed approval.**
