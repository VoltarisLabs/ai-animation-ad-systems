# Claymation SOP

**Source:** Ad Creators Lab — Canva "Claymation SOP" board
**Saved:** 2026-08-29 (transcribed from screenshots; Canva pages are JS-rendered and not fetchable)
**Canva:** https://www.canva.com/design/DAHFo1UG8aA/_zSEiFDatzhKEz8l2D7FCA/view

---

## What is claymation

> A stop-motion animation technique where characters and objects made from clay are moved slightly between each frame to create the illusion of movement.

---

## The 3-tool automation process

```
1. ChatGPT (project w/ prompt doc)  →  image prompts
2. NanoBanana 2                     →  frames (1k, 9:16)
3. Kling 3.0                        →  video (780p, audio off)
```

---

# 1. ChatGPT

## Setup
1. Go to ChatGPT
2. Left column → **"New Project"**
3. Name the project
4. Once created, click **"sources"**
5. Click **"add"** → select **text input** → copy and paste all the contents of **THIS document** into the "text" section. **Title is not needed.**
6. **Save**

> 🚨 **"THIS document" is a linked resource we have NOT received.** It is the actual claymation system prompt. Without it the ChatGPT project has no style rules and this step cannot be reproduced. **This is the missing piece for this format.**

## How to use
Once the project is set up, click the text bar below the project name to start a new conversation.

**Literally describe what you want to see in the frame.** Example given:

> *"A close up shot of an anthropomorphized tomato taking a walk in a garden. The sun is beaming on the top right of the corner. It's holding a Gucci bag. Wearing Prada sunglasses. The tomato character must be in the center of the frame."*

Then send and watch it cook.

## Don't know what to say/show? Ask these 5 questions
1. What is this part of the script actually saying in one sentence?
2. What does the viewer need to understand here?
3. Is this moment **explaining, proving, transitioning, or creating emotion**?
4. If I could only show one thing here, what would it be?
5. What would be confusing if I showed nothing here?

---

## Tips on prompting

### Referring to an existing clay character
Include at the beginning of the script:

- **If the image was generated with the previous prompt:**
  > *"With the image generated above as reference image."*

- **If the character image is from a separate conversation:**
  1. Upload the image to GPT
  2. > *"The attached image will also be given to nanobanana as a reference image."*

### Simple background
> *"Make the background simple"*

### Shot angles
- ¾ shot
- Over the shoulder shot
- Straight on shot
- Close-up shot
- Macro shot

### Basic prompt structure
```
[shot angle] [character] [action] [background]
```

> **No need to give lighting directions or camera quality**, unless you have special requests.

---

# 2. NanoBanana 2

Once you get the output from ChatGPT, **copy and paste everything into Nanobanana 2.**

**Settings: 1k quality, 9:16 frame size.**

---

# 3. Kling 3.0

## Setup
1. Select **Kling 3.0** as the video generation model
2. Select **780p**
3. **Turn off audio**

---

## Branch A — Want continuous flow?

For a video that looks like it's constantly transitioning, you **must use the start/end frame in Kling 3.0.** That means generating start AND end frames.

### "How do I know when I need a start frame and end frame?"

**First, generate the audio for the script** so you can gauge how long a section takes to say. Then decide how many clips fill that section.

**The rule:**

| Audio section length | Clips |
|---|---|
| **3-5 seconds** | **1 clip** |
| **6-9 seconds** | **2 clips** |

### Worked example
Script: *"But our body can only make so much IGF-1, that's why you can't break through your plateau even with more food."*

- *"But our body can only make so much IGF-1"* = 3 seconds
- *"that's why you can't break through your plateau even with more food"* = 5 seconds

→ Two clips, one 3s and one 5s.

**Clip 1:** generate **X** as start frame, **Y** as end frame. Kling set to 3 seconds. Input prompt, generate.
**Clip 2:** use **Y** as start frame, generate **Z** as end frame. Kling set to 5 seconds. Input prompt, generate.

> **The chaining is the mechanic** — each clip's end frame becomes the next clip's start frame. That's what produces continuous flow.

---

## Branch B — Want just a clip?

Normal claymation clip → **all you need is a start frame.** Give it to Kling, input directions, generate.

---

## Prompting process

### If a character is involved, include this verbatim:
> **"Keep character facial consistency. No character redesign. No facial feature changes."**

### Camera directions (pick one)
1. **Static** — stays still
2. **Slight push-in** — camera moves towards subject (often confused with zoom in)
3. **Slow pan left** — stationary camera that horizontally rotates to the left
4. **Arc right**

### Must include animation directions — verbatim
> **"Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon."**

### Prompt structure
```
[Visual direction] [camera directions] Ensure handmade stop-motion clay animation
throughout the video. Non CGI. Non cinematic. Animation must start at the first frame.
Non-disney. Non cartoon.
```

### Settings
**No sounds & 780p.**

### Example prompt
> *"Vines around the frame pull back and out of the frame. Hovenial Dulcis falls from the vine it's attached to into the mug of beer. The camera is static. Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon."*

### "What if I don't know what to say?"
Replace the `[Visual direction] [camera directions]` sections with:
> *"Create a handmade stop-motion clay animation transition between start and end frame."*

---

# 🚨 Two blockers for our stack

## 1. Kling 3.0 is DOWN on KIE
This SOP is **built around Kling 3.0** — specifically its **start/end frame** feature, which is the entire mechanic behind continuous flow. Tested 2026-08-27: Kling 2.6 and 3.0 both return **500 Internal Error**, 0 credits charged.

**Options:**
- Recheck whether Kling has come back on KIE
- Check whether **Seedance 2.0 supports an end/last frame parameter** — if it does, the chaining mechanic transfers. If not, only Branch B (single clip, start frame only) is reproducible for us.
- Use Kling through a non-KIE provider

**This needs resolving before any claymation production is planned.** Branch A is the good half of the format.

## 2. The ChatGPT prompt document is missing
The Step-1 setup pastes a linked document into a ChatGPT project as its source. That document holds the actual claymation style system. Without it we'd be inventing our own style rules, which is exactly the Rule Zero violation that got v6 rejected.

**Get the "THIS" link from the Canva board** and drop it in this folder.

---

# How claymation differs from our other formats

| | Skeleton | Crochet | Singing | **Claymation** |
|---|---|---|---|---|
| Consistency method | Character Bible verbatim | Character ref + diorama framing | n/a | **"Keep character facial consistency. No character redesign. No facial feature changes."** + reference image |
| Frames per clip | 1 | 1 or 2 (Type A/B/C) | n/a | **1 (clip) or 2 (continuous flow)** |
| Clip length driver | VO line length | phrase | music beat | **audio section: 3-5s → 1 clip, 6-9s → 2 clips** |
| Video model | Seedance/Kling/Veo | Seedance 1.5 Pro / Kling / Veo | — | **Kling 3.0 specifically** |
| Resolution | 1080×1920 | — | — | **780p, audio off** |
| Style enforcement | Style Library block | 3 universal excerpts | — | **animation directions line, verbatim** |

**Note the audio-first ordering.** Claymation and singing both generate audio *before* video, because audio determines clip count and length. Skeleton is the same. Only the Seedance UGC talking-head format generates speech inside the video itself.

## ⚠️ Do not mix claymation and crochet prompts
Crochet's Universal Negative explicitly bans `claymation, clay texture` to stop knitted textures drifting into clay. The two formats' style blocks are mutually exclusive — never reuse one's excerpts on the other.

---

🚨 **No API call without Rafiul's explicit typed approval.**
