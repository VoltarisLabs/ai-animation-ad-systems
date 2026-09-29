# AI Character Sheet: Master Prompt Template

Written 2026-09-23. Experimental. Expect the team to change fields: every
changeable thing lives in the FIELD BLOCK below, so a rejection is a field edit, not a rewrite.

Use: "make the character, use the template" → fill the FIELD BLOCK → paste PROMPT A into a new
Gemini chat (free tier, Nano Banana) → generate 3-4, keep the best → run PROMPT B set for the
reference angles → run PROMPT C to lock the face.

No image is generated from this file by itself.

---

## 1. FIELD BLOCK (the only part that changes)

Copy this, fill it, keep it with the character's folder.

```yaml
character_name:      # e.g. Marcus Hale
role:                # host / spokesperson / narrator. NEVER "satisfied customer" (FTC 16 CFR 255.1, 465.2)
gender:
age:                 # exact number, not a range. "41 years old"
ethnicity:
build:               # e.g. solid, slight softness at the middle, broad shoulders
skin:                # tone + real texture markers: pores, sun damage, a mole, forehead shine
hair:                # cut, length, color, greys, cowlick
facial_hair:         # or "clean shaven"
eyes:                # color, lid shape, crow's feet, under-eye
nose:
mouth_expression:    # default resting face. Closed-mouth half smile beats a grin
distinguishing_mark: # one small scar / mole / tan line. This is what makes the face re-findable
top:                 # no logo, no readable text
bottom:
shoes:
accessory:           # one max, or "none"
location:            # where he lives in frame
light:               # e.g. overcast mid-morning, flat
camera_feel:         # e.g. phone front camera, handheld, slight tilt
shot:                # half body waist up / chest up / full body
aspect_ratio:        # 4:5 Meta feed · 9:16 Stories+Reels · 1:1 fallback. Master = 4:5
```

Rules for filling it:
- One exact number for age. Ranges make the model average two faces.
- Every clothing item gets "no logo, no text". Brand marks and readable text break the ad and
  the render.
- Always one `distinguishing_mark`. Without it the face drifts and you cannot prove drift.
- Wear and imperfection are required: scuffs, dust, chapped lips, a bleach spot. Clean = plastic.

---

## 2. PROMPT A: create the character

New Gemini chat. Nothing attached. Generate 3-4 times, keep the best.

```
Create a UGC influencer image.

gender: {{gender}}
age: {{age}}
ethnicity: {{ethnicity}}
background: {{location}}, soft and out of focus behind him, {{light}}
style: natural, realistic, phone camera, no studio lighting, no retouching,
  slight sensor noise, the flat look of a modern phone front camera
camera placement: {{camera_feel}}, held at eye level
coverage: {{shot}}, head not cropped, some room above the hair
aspect ratio: {{aspect_ratio}}
additional details: {{skin}}; {{hair}}; {{facial_hair}}; {{eyes}}; {{nose}};
  {{mouth_expression}}; {{build}}; {{distinguishing_mark}}; wearing {{top}},
  {{bottom}}, {{shoes}}, {{accessory}}; no jewellery beyond that, no sunglasses,
  no hat, no branding anywhere in frame, no readable text, no signage
```

**Reject and regenerate if:** wide toothy grin · poreless plastic skin · suit, branded polo,
headset or lanyard · any readable text, logo or sign · studio rim light · face reads more than
8 years off `{{age}}` · symmetrical "AI model" face with no markers.

---

## 3. PROMPT B: the reference set (4 images, this is what makes him reusable)

From the winning image, run each as a separate follow-up **in the same chat**, attaching the
winner each time. One angle per message.

```
1. Same person, same face, same hair, same {{facial_hair}}, same clothes.
   Three-quarter left view, {{shot}}, same background, same light, {{aspect_ratio}}.
2. Same person, same face, same hair, same {{facial_hair}}, same clothes.
   Straight-on tight close-up, chest up, same background soft behind, {{aspect_ratio}}.
3. Same person, same face, same hair, same {{facial_hair}}, same clothes.
   Full body, standing, hands relaxed at the sides, same background, {{aspect_ratio}}.
```

Save as (07_Assets/ is gitignored: binaries stay local, this .md stays in the repo):

```
07_Assets/Characters/{{character_name}}/ref_01_master.png
07_Assets/Characters/{{character_name}}/ref_02_threequarter.png
07_Assets/Characters/{{character_name}}/ref_03_closeup.png
07_Assets/Characters/{{character_name}}/ref_04_fullbody.png
```

---

## 4. PROMPT C: lock the face (run once per character)

Per `~/.claude/skills/character_anchor_gemini/SKILL.md` (Vivek Kathait, 3-chat workflow).

1. New chat. Attach all four reference images.
2. Paste `~/.claude/skills/character_anchor_gemini/prompts/prompt-1-character-anchor.md`.
3. Gemini returns a ~100-word facial blueprint. That is the **Character Anchor**. Paste it into
   section 6 of this character's own copy of the file.

The skill was written for Nano Banana **Pro** in Gemini Pro mode, which is paid. On the free
tier run the same three chats in whatever mode the free account gives you; the anchor text still
works, the face lock is weaker. Say so out loud if a render drifts.

**Every later image after this:** new chat + attach the 4 refs + paste the Anchor + paste one
scene. Never ask for a different shot type as a follow-up inside a chat that already rendered.
That single mistake is what breaks the face.

---

## 5. Scene prompt shape (paste after the Anchor)

One scene per message, complete, shot type stated inside it.

```
{{shot}}, {{aspect_ratio}}. {{where he is and what is behind him}}. {{light}}.
{{camera_feel}}. {{expression and where he is looking}}. Natural realistic
phone-camera look, visible skin texture, no studio lighting, no retouching.
```

Never put a readable number, dollar figure, timeline or guarantee on anything in frame unless
that term is confirmed by the business in writing.

---

## 6. QC: check every render before use

- [ ] Face matches `ref_03_closeup.png`: eye shape, nose width, hairline, beard line
- [ ] `{{distinguishing_mark}}` is present and in the same place
- [ ] Skin has pores and texture, not plastic
- [ ] No logo, no readable text, no sign, no number in frame
- [ ] No suit, branded polo, headset, lanyard
- [ ] Not grinning; matches `{{mouth_expression}}`
- [ ] Aspect ratio matches the placement
- [ ] He is not implied to be a customer or a seller

---

## 7. Character Anchor

Paste the ~100-word blueprint from section 4 here. Until it is filled, the character is not
locked and faces will drift between ads.

```
(empty, run section 4)
```
