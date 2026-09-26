# Claymation GPT — the ready-made custom GPT

**Saved:** 2026-08-29

## Link

https://chatgpt.com/g/g-69ce6ba6e9688191951e560fb94f9128-claymation-gpt

**Name:** Claymation GPT

---

## What this is

The ChatGPT-hosted version of the claymation prompt system. Instead of following the SOP's Step-1 setup (create a project → add the source document → paste its contents), this GPT already has that system loaded.

**Two paths to the same thing:**

| Path | How |
|---|---|
| **A — Use this GPT** | Open the link in ChatGPT, describe the frame, get the image prompt |
| **B — Build it yourself** | SOP Step 1: new project → sources → add → text input → paste the source document |

Path A is faster. Path B is what the SOP documents, and needs the source document we still don't have.

---

## ⚠️ Its instructions are not extractable

Custom GPT system instructions are private by design — not served on the public page, not visible via fetch. I confirmed this: the page returns only the name.

**What that means for us:**

- ✅ **You can use the GPT directly** in ChatGPT right now — it works, it just runs on OpenAI's side
- ❌ **We cannot turn it into a `/claymation` slash command** without the underlying instructions
- ❌ **I should not reconstruct its style rules from guesswork** — that is the exact Rule Zero violation that got v6 rejected

**To get a local `/claymation` skill**, we need the source document the SOP calls "THIS document" — the one meant to be pasted into a ChatGPT project as its source. That link lives on the Canva board.

---

## Workable interim process

Until the source document arrives, claymation can still be produced — just with a manual hop:

```
1. Open Claymation GPT in ChatGPT
2. Describe the frame using the SOP's structure:
      [shot angle] [character] [action] [background]
3. Copy the output prompt
4. Paste into Nano Banana Pro on KIE (1k, 9:16)
5. Frames → Kling 3.0 for video
```

Steps 1-3 happen in the browser; steps 4-5 run through our KIE fire-scripts.

**Step 5 is still blocked** — Kling 3.0 returns 500 on KIE (tested 2026-08-27), and the SOP's continuous-flow mechanic depends on Kling's start/end frame feature. See `00-README-claymation-SOP.md`.

---

## The 5 framing questions (usable with either path)

When you don't know what to show for a script section:

1. What is this part of the script actually saying in one sentence?
2. What does the viewer need to understand here?
3. Is this moment explaining, proving, transitioning, or creating emotion?
4. If I could only show one thing here, what would it be?
5. What would be confusing if I showed nothing here?

These are model-agnostic — they work whether the prompt is written by the GPT, by me, or by hand.
