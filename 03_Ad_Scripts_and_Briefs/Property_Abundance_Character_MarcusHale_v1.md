# Property Abundance, AI Character: "Marcus Hale"

Built 2026-09-23. Framework from https://www.youtube.com/watch?v=pRtkjKD38SM
(100x Engineers, "How To Create AI UGC Ads", 9:55), Step 1 only, adapted for
**image ads** and locked with the Character Anchor workflow.

---

## Who he is and why

**Role: the buyer-side host.** He is the face of Property Abundance: the person
who explains the offer. He is **not** a satisfied seller.

> **Do not build a fake happy seller.** A generated person presented as a real
> customer giving a testimonial is a deceptive endorsement (FTC 16 CFR 255.1,
> and the 2024 rule at 16 CFR 465.2 on fake reviews and testimonials). A host
> who explains what the company does is a spokesperson, not a testimonial.
> If he ever appears to be a customer, the ad is non-compliant.

**Brief he has to hit:** "A calm, straight-talking neighbor. Not a hype
marketer." (`04_Audience_Research/Research_Document_Cash_Home_Buying.md`,
Brand Information, "How we want to be seen").

**Why this look:**

| Choice | Reason |
|---|---|
| Male, 41 | Old enough to be trusted with a house transaction, young enough not to read as retired. The ICP skews 45-70 (inherited houses, tired landlords, pre-foreclosure); a host slightly younger than the seller reads as helpful, not as a peer competing for status. |
| Black American, medium-brown skin | Distinct from the two characters already written in `Property_Abundance_Character_Sheets.json` (38M fair-skin, 45F) and from the photoreal base character (mid-20s). Nothing in the research file ties the offer to one ethnicity. |
| Short beard, few grays | Reads experienced without reading corporate. |
| No suit, no logo polo | Suits and branded polos test as "salesman". The brief says neighbor. |

**Swapping him is one field.** Change `ethnicity` or `gender` in the prompt
below and regenerate. Nothing else in this file has to change.

---

## Engine (free route)

The video uses **GPT Image 2** inside a paid ChatGPT account. That is not the
route here.

**Free route: gemini.google.com → Nano Banana 2.** Free tier, compute-based
limits that refresh roughly every 5 hours, no published per-day number
(`~/.claude/skills/brain/engines.md`, Images, checked 2026-09-10). This is a
**hand-off**: the prompts below are copy-paste ready, you click generate, then
bring the file back and it gets reviewed against this sheet.

Nano Banana **Pro** is a paid Google AI Plan feature. Do not switch to it
unless you turn billing on.

---

## Aspect ratio: one deliberate change from the video

The video hardcodes `9:16` because it is making TikTok/Reels video. You asked
for **image ads**. Meta's image placements want:

| Placement | Ratio | Use |
|---|---|---|
| Feed (primary) | `4:5` | Main ad image |
| Stories / Reels image | `9:16` | Same character, regenerate |
| Square fallback | `1:1` | Right column, some partner slots |

Generate the character at **4:5** first. That is the master.

---

## STEP 1: Create the character

Paste into a **new** Gemini chat. Nothing attached. Generate 3-4 times and
keep the best.

```
Create a UGC influencer image.

gender: male
age: 41 years old
ethnicity: Black American
background: standing on a residential street in an ordinary American
  suburb, single-storey houses and a parked pickup soft and out of focus
  behind him, overcast mid-morning light
style: natural, realistic, phone camera, no studio lighting, no retouching,
  slight sensor noise, the flat look of a modern phone front camera
camera placement: held at arm's length at eye level, as if he is holding
  the phone himself, very slight handheld tilt
coverage: half body, waist up, head not cropped, some room above the hair
aspect ratio: 4:5
additional details: medium-brown skin with real texture, visible pores,
  faint sun sheen on the forehead and nose; close-cropped natural hair with
  a clean low fade; a short full beard, neatly lined, with a few grey hairs
  at the chin; warm dark brown eyes, light crow's feet, relaxed heavy-lidded
  look; broad nose; calm closed-mouth half smile, not a grin, not a sales
  face; solid build, slight softness at the middle, shoulders relaxed;
  wearing a plain heather-grey crewneck t-shirt with no logo and no text
  under an open dark navy canvas work jacket, sleeves pushed back once;
  a plain steel watch on the left wrist; no jewellery, no earrings, no
  sunglasses, no hat, no branding anywhere in frame; no house-for-sale sign
  in this image
```

**Reject and regenerate if:** teeth showing in a wide grin, poreless plastic
skin, a suit or branded polo, a headset, any readable text or logo, a
for-sale sign, studio-perfect rim light, or a face that looks under 30 or
over 55.

---

## STEP 1b: Build the reference set (this is what makes him reusable)

Nano Banana holds a face far better with several angles to work from.
From the winning image, run these three as **separate follow-up prompts in
the same chat**, attaching the winning image each time:

1. `Same man, same face, same hair, same beard, same clothes. Three-quarter
   left view, waist up, same street, same overcast light, 4:5.`
2. `Same man, same face, same hair, same beard, same clothes. Straight-on
   tight close-up, chest up, same street background soft behind him, 4:5.`
3. `Same man, same face, same hair, same beard, same clothes. Full body,
   standing, hands relaxed at his sides, same street, 4:5.`

Save all four as:

```
07_Assets/Characters/MarcusHale/ref_01_halfbody.png
07_Assets/Characters/MarcusHale/ref_02_threequarter.png
07_Assets/Characters/MarcusHale/ref_03_closeup.png
07_Assets/Characters/MarcusHale/ref_04_fullbody.png
```

> `07_Assets/` is gitignored, so these stay local. That is fine: they are
> big binaries. Keep this .md in the repo as the source of truth.

---

## STEP 2: Lock the face (Character Anchor)

Do this **once**. The output is the asset you reuse forever.

Per `~/.claude/skills/character_anchor_gemini/SKILL.md`, which is Vivek
Kathait's 3-chat workflow. That skill was written for Nano Banana **Pro** in
Gemini Pro mode. On the free tier you run the same three chats in whatever
mode the free account gives you; the anchor text still works, face lock is
just slightly weaker. Say so if a render drifts.

1. New Gemini chat. Attach all four reference images.
2. Paste the Step-1 prompt from
   `~/.claude/skills/character_anchor_gemini/prompts/prompt-1-character-anchor.md`.
3. Gemini returns a ~100-word facial blueprint. **That is the Character
   Anchor.** Paste it into the box at the bottom of this file.

From then on, every new ad image = new chat + attach the 4 refs + paste the
Anchor + paste the scene. Never ask for a different shot type as a follow-up
inside a chat that already rendered: start fresh. That is the single
mistake that breaks the face.

---

## STEP 3: The "product" placement, adapted

The video's Step 2 is "influencer holds the product". Property Abundance has
no physical product. The equivalent objects, in order of how well they test:

| Object | Prompt fragment |
|---|---|
| The house itself | `standing in front of a tired single-family house with peeling paint and an overgrown lawn` |
| A printed offer sheet | `holding a single sheet of white paper at chest height, held so the camera cannot read it` |
| Keys | `holding a small ring of house keys in one open palm` |
| Nothing | Strongest for the "calm neighbor" brief. Use this as the control. |

> Never put readable numbers, a dollar figure, a timeline or a guarantee on
> anything in frame. Every offer term in the research file is still marked
> `PLACEHOLDER` or `TBD`: none is confirmed for Property Abundance. An image
> that shows a promise the business has not confirmed is an FTC Act s.5
> problem, and it is also just wrong.

---

## Scene prompts (paste after the Anchor)

Each is a complete scene. Attach the 4 refs, paste the Anchor, then one of
these.

**A: The street, control shot**
```
Half body shot, waist up, 4:5. He stands on a quiet residential street in an
ordinary American suburb, overcast mid-morning, houses soft and out of focus
behind him. Held at arm's length at eye level like a phone selfie, slight
handheld tilt. Calm closed-mouth half smile, looking straight into the lens.
Natural realistic phone-camera look, no studio lighting, no retouching.
```

**B: In front of the tired house**
```
Three-quarter shot, waist up, 4:5. He stands on the front walk of a tired
single-family house, peeling paint, overgrown lawn, one shutter hanging
loose, soft and out of focus behind him. Flat overcast light. Phone held at
arm's length at eye level. Relaxed, unbothered expression, not smiling.
Natural realistic phone-camera look, no retouching.
```

**C: At the kitchen table**
```
Medium shot, chest up, 4:5. He sits at a plain kitchen table in a modest
older American home, a mug and a single sheet of white paper on the table in
front of him, the paper angled so the camera cannot read it. Soft daylight
from a window to his left. Camera stationary on the table opposite him at
eye level, as if propped against something. Calm, listening expression.
Natural realistic phone-camera look, no retouching.
```

**D: Tight close-up (for the hook frame)**
```
Tight close-up, chest up, 85mm equivalent, 4:5. Plain residential street
heavily blurred behind him. Flat overcast light. Looking straight into the
lens, mouth relaxed and slightly open as if mid-sentence, eyebrows neutral.
Natural realistic phone-camera look, visible skin texture, no retouching.
```

---

## Check every render against this before you use it

- [ ] Face matches `ref_03_closeup.png`: eyes, nose width, beard line, hairline
- [ ] Skin has pores and texture, is not plastic
- [ ] No logo, no readable text, no sign, no number anywhere in frame
- [ ] Not wearing a suit, branded polo, headset or lanyard
- [ ] Not grinning; reads calm, not salesy
- [ ] Correct aspect ratio for the placement
- [ ] He is not implied to be a customer or a seller

---

## Character Anchor

_Paste the ~100-word blueprint from Step 2 here once you have it. Until then
this character is not locked and faces will drift between ads._

```
(empty, run Step 2)
```
