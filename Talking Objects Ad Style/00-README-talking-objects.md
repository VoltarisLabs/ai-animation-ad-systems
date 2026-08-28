# Talking Objects Ad Style

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-29
**Custom GPT:** https://chatgpt.com/g/g-69667f7a5fb081918fcc4499670788f3-object-talk ("Object Talk")

Talking Pixar-character videos where **the product itself speaks.** Performing exceptionally well for brands.

---

## 🚨 The whole format in one line

> **"I'm the failed solution explaining why I suck."**

The talking object is **not your product**. It's the thing the customer already tried and that let them down. It confesses its own flaws, and your product becomes the obvious upgrade by contrast.

---

## 1. Start with the real strategy (most people skip this)

Before generating anything, answer:

> **What failed solutions did customers try before your product?**

That answer becomes the character. Example script from the lesson:

> *"I'm your drugstore moisturizer.
> I'm packed with cheap seed oils to keep my price low…
> but those oils clog pores and irritate your skin."*

**Structure of the confession:**
1. *"I'm [the failed solution]"* — identify
2. *"I [do this cheap thing] to [serve my interest]"* — admit the motive
3. *"but that [causes this harm to you]"* — the cost, in the customer's body/wallet

---

## 2. Turn the product into a character

Generate an image where the product becomes a character.

| Model | Trade-off |
|---|---|
| **Seedance** | cheap, **but not good with text** |
| **Nano Banana** | pricier, **elite at text** |

**Tip: generate 4-6 variations, pick the most expressive one.**

> We learned the Seedance text weakness the hard way — B-roll v1 rendered "ARP" instead of "APR." Same limitation, confirmed independently. For any character with legible packaging text, Nano Banana.

---

## 3. Turn the image into a talking video

Generate a talking avatar video from the image. The image will:
- move slightly
- **lip sync** (a little off is fine)
- speak the script

**Google Veo is the best but pricier.**

**Test different models — results vary.**

### Typical testing workflow
```
1️⃣ Cheap model  → test timing
2️⃣ Better model → final version
```

---

## Why these ads work — 3 psychological triggers

| # | Trigger | Mechanism |
|---|---|---|
| 1️⃣ | **Pattern interrupt** | Objects talking = scroll stopping |
| 2️⃣ | **Educational** | Explains *why* the old solution sucks |
| 3️⃣ | **Product positioning** | Your product becomes the obvious upgrade |

---

## Quick ecom examples from the lesson

| Vertical | The talking failed solution |
|---|---|
| Skincare | Drugstore moisturizer talking about seed oils |
| Coffee | Supermarket coffee explaining why it's stale |
| Mattress | Cheap Amazon mattress explaining why it sinks |

---

## Altura application

Our research doc already did step 1 — the **"failed solutions"** section is one of its 15 parts. The talking objects write themselves:

| Talking object | Its confession |
|---|---|
| **An MCA contract** | *"I'm the merchant cash advance you took in 2024. I gave you money in 48 hours because I knew you were desperate. I take $758 every single day before you've served a customer. And I'm not a loan, so those rate caps don't apply to me."* |
| **A maxed-out business credit card** | *"I'm your 24.99% APR. Every month you pay me, and every month you owe about the same."* |
| **A bank loan application** | *"I'm the SBA application you started 9 months ago. I'm still pending."* |
| **A hard-inquiry credit pull** | *"I'm the hard inquiry from the last five lenders you applied to. I dropped your score every time you tried."* |

**The MCA one is the strongest.** It's the single most emotionally charged failed solution in our raw customer voice file, and the 2026 SBA rule change (SBA loans can no longer be used to pay off MCAs) means people are more trapped than ever. That's a real, current, verifiable pain — not a manufactured one.

**Why this format fits Altura better than skeleton/crochet/singing:** those three are pattern interrupts that risk undercutting a funding brokerage's credibility. Talking objects is a pattern interrupt that is **also an education play** — and financial services buyers at Level 4-5 sophistication respond to being taught the mechanism, not to being sold. It's the closest of the four animated formats to our actual positioning.

**Compliance note:** the object's confession is a claim about a competitor category. Keep every number to what our research file substantiates ($758/day, 24.99% APR are from real customer quotes), and never name a specific competitor company.

---

## Production path on our stack

```
1. Pick the failed solution        (research doc, "failed solutions" section)
2. Write the confession script     (Object Talk GPT, or the 3-part structure above)
3. Character image                 → Nano Banana Pro, KIE, ~$0.09 × 4-6 variations
4. Talking video                   → ??? see below
```

### ⚠️ The open question: which model for talking video

The lesson says Veo is best but pricey, and to test cheap-then-good. Our situation:

| Model | Status | Note |
|---|---|---|
| **Veo 3 Fast** | ✅ works on KIE, ~$0.30 flat | 🚫 **course-banned elsewhere** for talking segments |
| **Seedance 2.0** | ✅ works, $0.205/sec | native audio + lipsync in one pass — this is what we used for the Altura advisor |
| Kling | 🔴 down on KIE | — |

**The Veo ban needs checking against this lesson.** The G.E.M framework bans Veo 3 for talking segments (*"weird sounds, wacky animations, bad background music"*). This lesson recommends Veo for talking objects. Those may not conflict — the G.E.M ban was about human characters, and a talking object has no human face to fall into uncanny valley. But I am not going to assume it. **Ask Camilo / the Ad Reviews channel before spending on Veo here.**

**Safe default:** Seedance 2.0, which already produced acceptable lipsync on our Altura advisor and needs no separate lipsync pass.

### Cost estimate, one 20s talking-object ad
| Item | Qty | Unit | Total |
|---|---|---|---|
| Character images | 6 | $0.09 | $0.54 |
| Seedance 2.0 talking video | 20s | $0.205/s | $4.10 |
| **Total** | | | **~$4.64** |

Cheapest of all four animated formats — one character, one continuous take, no storyboard, no frame chaining.

🚨 **No API call without Rafiul's explicit typed approval.**

---

## ⏳ Still needed

The **Object Talk GPT** instructions are private (same as Claymation GPT — OpenAI does not serve custom GPT system prompts). Two paths:
- **Use it directly** in the browser, paste the output here
- Write scripts from the 3-part confession structure above, which the lesson states in full

Unlike claymation, this lesson gives us enough to work without the GPT — the strategy, the structure, and a worked example are all in the lesson text.
