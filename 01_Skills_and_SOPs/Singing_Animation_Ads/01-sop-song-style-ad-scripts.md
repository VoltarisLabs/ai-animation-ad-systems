# SOP — Generate Song-Style Ad Scripts

**Source:** Ad Creators Lab lesson (team SOP)
**Saved:** 2026-08-29
**Prompt:** `song-style-ad-generator-PROMPT.txt` → `/singing`
**Loom:** https://loom.com/share/d64b8a79b1df4534ac0673c7f4979a2c

---

## Objective

Create song-style ad scripts tailored to a specific **avatar, product, and awareness stage**. Produces usable lyrics, style guidance, and visual ideas without writing from scratch.

---

## The 10 steps

### 1. Gather source material (0:20)
Collect the input document or webpage. Whatever is available:
- research document
- website copy
- notes with pain points, objections, solutions

Must clearly describe the product and its benefits. **A simple document is fine** — it doesn't need to be highly formatted.

### 2. Run the prompt (0:37)
Paste the source material → Run.
Wait for it to analyze the product and identify **core selling points**.
**Confirm the output reflects the main product themes before moving on.**

### 3. Choose song style and length (0:53)
- Select the genre when prompted
- Unsure → ask the tool to **recommend** a genre
- Choose ad length: **30s** or **45s**
- Unsure → ask it to recommend based on the **campaign goal**

### 4. Confirm or enter the target audience (1:23)
- Check whether the research doc already identifies the target market
- Missing or unclear → **enter it manually**
- **Be specific about the avatar:** *"Moms age 50+"* · *"Dads age 40+"* · *"Social-media-native users ages 15-34"*
- The audience details drive the genre and tone recommendation

### 5. Review the genre recommendation (1:41)
Compare the suggested genres against audience and offer. Example output: Pop · R&B · Hyperpop.
Pick the one that best supports the ad's **energy and platform fit**.

### 6. Select awareness stage and angle (2:24)
Review the recommended angle + awareness stage. Example from the transcript:
- **Angle:** *"Whiter teeth in 7 days without the zaps"*
- **Awareness stage:** Solution aware

Ask for other angles or stages to compare before deciding.

### 7. Use alternative angles if needed (2:58)
Suggested angle doesn't fit → **request more options**. Review alternatives, choose what aligns with the campaign objective.
Use this step when testing different messaging directions before finalizing.

### 8. Generate and extract the final script (3:44)
Once genre, length, audience, and angle are locked, let it generate.
- **Copy the lyrics directly**
- Save them for **Suno** or the next production step
- Treat this as the **working draft**, not final

### 9. Review style guidance and visual ideas (4:08)
Style notes include:
- music style (e.g. *upbeat pop*)
- vocal (e.g. *bright female lead*)
- **BPM guidance**

Visual ideas cover formats like: **animated character · pixel object · claymation-style visuals**

### 10. Refine to include unique product mechanisms (4:39)
🚨 **This is the step that turns a song into a marketing asset.**

Review for accuracy and relevance. **Make sure the unique mechanism / differentiator is included.** Adjust the output so it highlights the product's special features.

Examples from the transcript: *peroxide powder* · *coconut comfort*

> *"Use this step to ensure the ad is not just a song, but also a persuasive marketing asset."*

---

## ⚠️ Cautionary notes (verbatim)

- **Do not skip the audience step** — genre and angle depend on who you're targeting
- **Make sure the awareness stage matches** the customer's familiarity with the problem and solution
- **Review the generated lyrics for accuracy** before production
- **Confirm the unique mechanism is represented clearly** so the ad doesn't feel generic
- If the source document is vague, the prompt may require you to **re-enter target market details**

---

## 💡 Efficiency tips (verbatim)

- Use the **recommendation features** when unsure about genre, length, or angle
- Keep a **reusable research document template** with pain points, objections, and product benefits
- **Start with the recommended angle**, explore alternatives only if the first isn't strong
- **Save approved outputs as examples** for future campaigns
- Use the **visual ideas section** to speed up creative planning for production teams

---

## Notes for our setup

**We already have the "reusable research document" the tips ask for** — `Research protocole/RESEARCH-DOCUMENT-Altura-2026-08-24-v2.md` has pain points, objections, misconceptions, awareness/sophistication level, and ICP language. It is exactly the Step 1 input this prompt wants, and it already answers Step 4 (target audience) and Step 6 (awareness stage), so those steps should go fast.

**Duration mismatch to watch:** the SOP says 30s or 45s; the underlying prompt offers **15s / 30s / 60s**. Follow the prompt's options — it's the actual tool.

**Step 10 is the one to not rush.** Our v6 rejection came from output that was on-format but wrong on substance. For Altura the unique mechanism is **pre-qualification with no hard inquiry** plus **0% intro-APR card options** — if those aren't in the lyrics, the song is generic and the whole thing fails the same way.

**Suno is not set up.** The lyrics are free to generate, but turning them into a track needs a Suno account. Not a KIE model — separate tool, separate cost. Flag before planning a song ad into a delivery timeline.
