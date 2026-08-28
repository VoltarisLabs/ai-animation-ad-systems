# SOP — Script → Character-Consistent Storyboard → Video

**Source:** Ad Creators Lab lesson (team SOP)
**Saved:** 2026-08-29
**Skill:** `crochet-ad-visuals-SKILL.md` → `/crochet`

> **Note:** this SOP describes the **same skill already installed** as `/crochet`. The workflow matches exactly — character question → phrase breakdown with multiple visual ideas → storyboard with start/end frames. No separate skill file needed.

---

## Objective

Use the custom skill workflow to turn a script into **character-consistent storyboard frames**, then generate matching video prompts and test outputs. Produce consistent visuals and short clips efficiently while preserving the intended character, scene, and product details.

---

## The 14 steps

### 1. Install the skill (0:00)
Claude → **Customize → Skills** → **+** → **Create skill** → **Upload skill** → upload the `.zip`. Confirm installed before moving on.

> ✅ **Already done for us** — installed as a project skill, run it with `/crochet`.

### 2. Understand what the skill generates (0:12)
- First checks whether the project uses a **consistent character**
- If yes, generates a character prompt/description for reference
- Then breaks the script into phrases and suggests **multiple visual ideas per phrase**
- Use the suggestions to pick visuals that match the script and improve attention/engagement

### 3. Launch the skill and upload the script (1:30)
- Three dots → **Try in chat**, or run the **slash command** directly
- Upload or paste the script
- **Verify the skill is actually running** — confirm it says it's reading the skill

### 4. Define the character for consistency (1:53)
- Choose the option indicating **yes, there is a character**
- Provide a clear description **based on your target audience / avatar**
- 🚨 **Include only research-based details. Do not invent traits that don't match the avatar.**
- **Save the generated character reference** for later use

### 5. Review phrase-by-phrase visual suggestions (2:25)
- Read the breakdown — each phrase paired with several visual ideas
- Pick the one that best fits **message, tone, and pacing**
- Treat the suggestions as a **starting point, not a final answer**
- You can revisit and change a selection later

### 6. Select a visual and generate the storyboard prompt (3:02)
Submit the chosen phrase/visual combination back to the skill. Output should include:
- a **scene explanation**
- **prompt text** for image generation
- guidance on whether to use a **start frame, end frame, or both**

### 7. Generate the character reference image FIRST (3:13)
- Copy the character reference prompt into the image tool
- **Start with Seedream** for the lower-cost option
- Use this character image as the reference for **all later frames**

### 8. Create the start frame (3:44)
- Copy the start-frame instructions into the image generator
- **Upload the character reference alongside the prompt**
- Generate multiple versions
- Pick the frame that best matches the intended action and composition

### 9. Refine and preserve continuity (5:05)
- Compare the generated frame to the intended scene
- Edit the prompt to improve **emotion, pose, or clarity** if needed
- **Keep the same background and character reference** when regenerating
- 🚨 **Make small changes rather than rebuilding the scene from scratch** — this is what preserves continuity

### 10. Generate the video prompt and set motion endpoints (6:06)
- Move to Videos
- **Start with Seedance 1.5 Pro** — the cheapest model
- Paste the video prompt
- Set the **start frame** and, if available, the **end frame**
- Use a **short duration such as 5 seconds** for a simple test render

### 11. Test higher-quality models if needed (6:39)
- First result not strong enough → test other models
- **Seedance 2.0 with references** — better control over multiple images
- **Kling** — compare output quality
- Pick the model balancing quality, motion, and consistency for that scene

### 12. Work ahead while renders process (7:19)
- While images/videos generate, go back to the skill output
- Move to the next phrase, choose the next visual idea
- Decide whether to show the product **early, later, or as a held reveal**
- Repeat per phrase until the script is covered

### 13. Include product details, keep the character reference (8:48)
- **Product must be in the prompt** when the scene requires it
- **Always reuse the same character reference** to avoid unwanted changes
- Scene looks off → revise and regenerate, don't accept a weak result
- Keep visual style, character, and environment aligned across all scenes

### 14. Review and iterate to completion (10:12)
- Generate for every phrase
- Compare outputs across models to find the best performer
- **Talk to the skill conversationally:**
  - *"Go back to phrase two, visual one."*
  - *"Make him look more sad."*
- Iterate until the storyboard and video set is complete

---

## ⚠️ Cautionary notes (verbatim)

- **Do not use the generated character description as a prompt** unless the workflow specifically instructs it
- **Do not invent character traits** — base the description on real audience/avatar research
- **Always reattach the character reference** when generating new frames, or the character will change
- **Make sure the product is explicitly included** in prompts when the scene depends on it
- Some models add **unwanted elements such as music or inconsistent backgrounds** — compare outputs before finalizing
- **Verify the skill is actually running** by confirming it's reading the skill

---

## 💡 Efficiency tips (verbatim)

- **Seedream first** for quick low-cost image tests before moving to expensive options
- **Generate multiple image variations at once** so you can pick the strongest frame quickly
- **Keep the same background and character reference** when refining, to reduce rework
- **Work ahead** — storyboard the next phrase while a render processes
- **Short test durations (5s)** to validate motion before committing to longer renders
- **Ask for revisions in plain language** instead of restarting the workflow

---

## Our stack translation (Max Fusion → KIE)

| SOP says | We use | Cost |
|---|---|---|
| Max Fusion → Images → **Seedream** (cheap test) | ⚠️ Seedream unverified on KIE → fallback **Nano Banana Pro** | ~$0.09/image |
| Max Fusion → Videos → **Seedance 1.5 Pro** (cheapest) | ⚠️ unverified on KIE | TBD |
| **Seedance 2.0 with references** | ✅ working — our workhorse | $0.205/sec |
| **Kling** (compare quality) | 🔴 DOWN — 500 error (2026-08-27) | — |

**The 5-second test-render rule matters a lot for us.** On Seedance 2.0 at $0.205/sec, a 5s test = **$1.03**. Ten phrases × 1 test each = **$10.30** before a single final render. That is our entire remaining balance.

This is exactly why the SOP says start with the cheapest model. **Without a cheap test tier we cannot follow this SOP as written.** Verifying `seedream-4.5` and `seedance-1.5-pro` on KIE is the blocking action item.

### Rough cost, 10-phrase crochet ad on our current stack

| Item | Qty | Unit | Total |
|---|---|---|---|
| Character reference (2-3 tries) | 3 | $0.09 | $0.27 |
| Start frames (10 scenes, 2 tries each) | 20 | $0.09 | $1.80 |
| End frames (assume 4 Type B, 2 tries) | 8 | $0.09 | $0.72 |
| Video, Seedance 2.0, 10 clips × 5s | 50s | $0.205/s | **$10.25** |
| **Total, no retries on video** | | | **~$13.04** |

Video retries are the risk — one full retry round adds another $10.25. Balance is **$20.68**.

🚨 **No API call without Rafiul's explicit typed approval.**
