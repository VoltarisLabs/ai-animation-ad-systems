# Property Abundance — Ad 5: "Three Questions" (Vidu, animated)

**Built:** 2026-09-24
**Model:** Vidu Q3-pro (fallback: Vidu Q2 Reference Pro)
**Format:** 9:16, 1080p, stylized 3D animation, ~35 s total, 5 clips
**Concept:** Winning Concept #4 — "How to spot a bad cash buyer" (`Cash_Home_Buying_Winning_Concepts.md`, §3)
**Subject:** unchanged — selling a house for cash to Property Abundance.
**What is new vs Ad 1 and Ad 2:** new hook type (Curiosity Gap, not Contrarian or Labeling), new visual device (a three-box checklist that fills in on screen), animated instead of live-action, and a host who asks questions instead of a voiceover that explains.

---

## 1. Verified model facts this script is built on

Source: `https://platform.vidu.com/docs/text-to-video`, fetched 2026-09-24.

| Setting | Value used | Model limit |
|---|---|---|
| Model | `viduq3-pro` | also `viduq3-turbo`, `viduq2`, `viduq1` |
| Duration | 8 s, 7 s, 7 s, 7 s, 6 s | q3: 1–16 s (default 5) · q2: 1–10 s · q1: 5 s only |
| Resolution | 1080p | 540p / 720p / 1080p (q1: 1080p only) |
| Aspect ratio | 9:16 | 16:9, 9:16, 3:4, 4:3, 1:1 (3:4 and 4:3 are q2/q3 only) |
| Prompt length | ~160 words per shot | max 5000 characters |
| Background music param | not used | Q3 does not support it — put music in the Sound line, or add the bed in your edit |

Prompt structure below follows Vidu's five-part order: **Scene → Character → Action (time-ordered) → Camera → Sound.**

---

## 2. Character lock (do this before generating)

Vidu holds a character across clips through **Reference to Video** — upload reference stills of the same character, up to 7 images on Vidu Q2 Reference Pro.

**Host: Marcus Hale, animated variant.** Same person as `Property_Abundance_Character_MarcusHale_v1.md`, redrawn as animation.

> He is the **buyer-side host**, not a past customer. A generated person presented as a real customer giving a testimonial is a deceptive endorsement (FTC 16 CFR 255.1 and 16 CFR 465.2). He explains and asks — he never says he sold a house.

Generate 3 stills free in Gemini / Nano Banana at 9:16, then upload all 3 as Vidu references:

```
Stylized 3D animated character, single character sheet image, 9:16.
Black American man, 41, medium-brown skin, short trimmed beard with a few
grays, close-cropped hair. Calm, friendly, direct — a neighbor, not a
salesman. Navy henley shirt, sleeves pushed up, no logo, no suit, no tie.
Soft matte shading, rounded forms, warm daylight, gentle rim light.
Muted warm palette: cream, warm grey, soft navy, one amber accent.
Neutral light background. Full body, standing, arms relaxed.
Rendered like a modern animated feature, not photoreal, not cartoon-goofy.
```
Regenerate the same prompt with `three-quarter view, chest up` and `wide shot, standing on an ordinary American residential sidewalk` for stills 2 and 3.

**Style line to repeat in every shot prompt:** *stylized 3D animation, soft matte shading, rounded forms, muted warm palette of cream, warm grey and soft navy with one amber accent, warm daylight, shallow depth of field.*

---

## 3. Hard rules (carried from Ad 1 and Ad 2)

- No cash piles, no money fanning, no money counters.
- No dollar amounts, no days-to-close, no "X houses bought" — no number on screen that Property Abundance has not measured.
- No fake urgency: no "limited spots", no "before it's too late".
- No claims about named competitors.
- The host is a spokesperson, never a customer.
- Captions: 1–4 words per card, one keyword in the amber accent.

---

## 4. The script

Total 35 s. Caption cards are burned in your edit, not asked of Vidu.

---

### CLIP 1 — HOOK (0:00–0:08, 8 s)

**ON SCREEN:** THREE QUESTIONS
**VO / on-camera:** "A bad cash buyer can answer two of these. Not three."

**Vidu prompt:**
```
Scene: an ordinary American residential street in late morning, single-story
houses, a mailbox and a bare young tree, soft warm daylight, stylized 3D
animation with soft matte shading and rounded forms, muted warm palette of
cream, warm grey and soft navy with one amber accent, shallow depth of field.

Character: one man, Black American, 41, medium-brown skin, short trimmed beard
with a few grays, navy henley with sleeves pushed up, calm and direct, standing
centered facing camera, holding a plain clipboard with three empty checkboxes.

Action: first he lowers the clipboard and looks straight into the lens; then he
raises three fingers, one at a time, unhurried; finally he turns the clipboard
toward camera so the three empty boxes fill the lower frame.

Camera: medium shot, eye level, slow push in, subject centered, shallow depth of
field, background softly blurred, steady, 24 fps.

Sound: the man says, "A bad cash buyer can answer two of these. Not three."
Quiet suburban ambience, distant birds, a faint breeze. No music.
```

---

### CLIP 2 — QUESTION ONE (0:08–0:15, 7 s)

**ON SCREEN:** WHOSE MONEY?
**VO:** "One. Show me proof of funds, in your company's name."

**Vidu prompt:**
```
Scene: same residential street, same stylized 3D animation look, soft matte
shading, muted warm palette with one amber accent, warm daylight, shallow depth
of field.

Character: the same Black American man, 41, short beard, navy henley, now
holding a single sheet of paper at chest height, expression steady and patient.

Action: first he holds the sheet up so the camera can read that it is a bank
letter with the company name at the top; then the first checkbox on his
clipboard fills with an amber check; finally he tilts his head slightly, a
small questioning look, waiting for an answer.

Camera: medium close-up, eye level, static frame, slight rack focus from the
paper to his face, shallow depth of field, 24 fps.

Sound: the man says, "One. Show me proof of funds, in your company's name."
A soft paper rustle. Quiet street ambience underneath. No music.
```

---

### CLIP 3 — QUESTION TWO (0:15–0:22, 7 s)

**ON SCREEN:** WHO ACTUALLY BUYS IT?
**VO:** "Two. Are you buying it, or selling my contract to someone else?"

**Vidu prompt:**
```
Scene: same street, the house now shown in a clean wide frame, stylized 3D
animation, soft matte shading, muted warm palette with one amber accent, warm
daylight, shallow depth of field.

Character: the same Black American man, 41, short beard, navy henley, standing
to the left of frame; in the background three faceless stylized silhouettes
stand in a line, neutral grey, not threatening.

Action: first a single sheet of paper passes from the first silhouette to the
second, then to the third, hand to hand; then the man watches it travel and
turns back to camera; finally the second checkbox on his clipboard fills with
an amber check.

Camera: wide shot settling into a slow dolly left, eye level, the paper handoff
staying in focus, shallow depth of field, 24 fps.

Sound: the man says, "Two. Are you buying it, or selling my contract to someone
else?" Light paper handling sounds. Quiet street ambience. No music.
```

---

### CLIP 4 — QUESTION THREE (0:22–0:29, 7 s)

**ON SCREEN:** WHERE'S THE MATH?
**VO:** "Three. Show me how you got the number. Worth fixed up, minus repairs, minus your costs."

**Vidu prompt:**
```
Scene: a plain kitchen table indoors, warm window light from the left, a mug and
a pen on the table, stylized 3D animation, soft matte shading, muted warm
palette of cream, warm grey and soft navy with one amber accent, shallow depth
of field.

Character: the same Black American man, 41, short beard, navy henley, seated at
the table, leaning in slightly, calm and unhurried, a plain worksheet in front
of him.

Action: first his hand writes one short line on the worksheet; then a second
line under it; finally a third line, and he turns the worksheet to face camera
so the three handwritten lines are readable as words only, with no numbers
anywhere on the page.

Camera: high three-quarter angle over the table, slow tilt down to top-down on
the worksheet, shallow depth of field, steady, 24 fps.

Sound: the man says, "Three. Show me how you got the number. Worth fixed up,
minus repairs, minus your costs." Pen on paper, a mug set down, quiet room tone.
No music.
```

---

### CLIP 5 — TURN + CTA (0:29–0:35, 6 s)

**ON SCREEN:** ASK US FIRST
**VO:** "Ask us first. If we can't answer all three, don't sell to us."

**Vidu prompt:**
```
Scene: back on the residential sidewalk in front of the house, warm late-morning
daylight, stylized 3D animation, soft matte shading, muted warm palette with one
amber accent, shallow depth of field.

Character: the same Black American man, 41, short beard, navy henley, standing
centered, holding the clipboard with all three boxes now checked in amber,
relaxed and open, a small honest smile at the end.

Action: first he turns the completed clipboard toward camera; then he lowers it
and gives a small shrug, palms open; finally he holds still, looking into the
lens, and the frame settles.

Camera: medium shot, eye level, slow push in to a tighter medium close-up,
subject centered with headroom for an end card, shallow depth of field, 24 fps.

Sound: the man says, "Ask us first. If we can't answer all three, don't sell to
us." Quiet suburban ambience, a soft breeze. No music.
```

**End card (built in your edit, not in Vidu):** phone showing the Property Abundance form, logo, caption `SEE THE MATH ON YOUR HOUSE`.

---

## 5. How to run it

1. Generate the 3 character stills free in Gemini / Nano Banana at 9:16.
2. In Vidu, use **Reference to Video**, upload all 3 stills, model `viduq3-pro`, 1080p, 9:16, and paste Clip 1's prompt. Set duration per the table.
3. Keep the same 3 references for all 5 clips. That is what holds the face.
4. Generate 3–4 takes per clip. Keep the one where the mouth matches the line.
5. If a face drifts, add that clip's best frame as a 4th reference and regenerate.
6. If Q3 is unavailable, use `viduq2` — same prompts, but cap every clip at 10 s and expect weaker lip-sync; in that case mute the clip and lay your own voiceover.
7. Assemble in your editor, burn the caption cards, add the end card and one quiet music bed.

## 6. Open items
- The three lines Marcus writes in Clip 4 must match Property Abundance's real offer worksheet. Confirm the wording before shooting.
- "Don't sell to us" in Clip 5 is a real promise. Confirm the company will stand behind it.
- Proof of funds in the company's name (Clip 2) must be true and producible on request.
