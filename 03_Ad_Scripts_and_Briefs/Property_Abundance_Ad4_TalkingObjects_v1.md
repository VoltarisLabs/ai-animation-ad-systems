# Ad 4 – The Honest Cash Buyer, talking-objects cut (v1)

**Made:** 2026-09-23. **Brand:** Property Abundance. **Status:** script written, claims NOT filled, nothing generated.
**Prompts:** `Property_Abundance_Ad4_TalkingObjects_PROMPTS_v1.json` and `Ad4_TalkingObjects_paste/` (five paste-ready files + run sheet).
**Converts:** `Property_Abundance_Ad4_Honest_Cash_Buyer_Brief_v1.md` (AI talking head) into the animated
talking-objects format.
**Format skill:** `talking-objects-ads`. Lesson source: `01_Skills_and_SOPs/Talking_Objects/00-README-talking-objects.md`.
**Concept:** #1 from `Cash_Home_Buying_Winning_Concepts.md` — call out the category, then show the offer math.
**Persona:** Inherited Irene (heir living hours away).

> Nothing here ships until every `[NEEDS YOUR TERM]` is replaced with a real Property Abundance fact.
> FTC Act s.5. An ad may not promise what the business does not deliver.

---

## 1. Why this format, and why this object

The format is one line: **"I'm the failed solution explaining why I suck."** The object is never your product.

| Question | Answer |
|---|---|
| What did Irene already try? | She called a number off an ad or a yard sign and got a cash offer read to her over the phone. |
| Why did it fail her? | The number arrived with no paper and no reasoning. She could not check it, so she could not trust it. |
| So the character is | **The cash offer itself**, played by a 1990s corded kitchen wall phone with a face. |

Three reasons this object and not another:

1. **It is the argument.** Ad 4's whole spine is "nobody shows you how that number gets made." A phone is the thing that delivered the number without paper. The object and the objection are the same object.
2. **It needs no legible text.** A yard sign or an offer letter is a text character, and every rule in this repo says keep text out of generated footage. A phone has nothing to read. Keypad digits get explicitly banned in the prompt.
3. **It confesses only what the viewer can verify.** It admits its own silence — which is literally true of any phone call — instead of claiming what a named competitor pays. No unprovable competitor claim, per `Cash_Home_Buying_Winning_Concepts.md` §3 "Concepts to avoid".

---

## 2. Confession structure, mapped

| Step | Format rule | This ad |
|---|---|---|
| 1 | "I'm [the failed solution]" | "I'm the cash offer you got on your mom's house." |
| 2 | "I [do this cheap thing] to [serve my interest]" | "One number, no paper. Sounding sure is cheaper than showing my work." |
| 3 | "but that [costs you this]" | "Nobody showed you how that number got made" — so she cannot tell a fair offer from a bad one. |
| Turn | Your product is the upgrade | "Property Abundance does the boring thing. They write it down." |

---

## 3. The script

Four clips, one per Gemini generation. The object speaks natively in-shot — no separate voiceover track.

### Clip 1 — 0.0 to 10.0 s · identify and admit the motive

| # | Line | Words |
|---|---|---|
| 1 | "I'm the cash offer you got on your mom's house." | 10 |
| 2 | "I came over the phone. One number, no paper, and then quiet." | 12 |
| 3 | "Sounding sure is cheaper than showing my work." | 8 |

### Clip 2 — 10.0 to 20.0 s · the cost to her

| # | Line | Words |
|---|---|---|
| 4 | "Nobody showed you how that number got made. Not me. Not the sign in your yard." | 16 |
| 5 | "Watch ten of these ads. Count how many show the math." | 11 |
| 6 | "I'll wait." | 2 |

Line 6 lands after a real 0.60 s stop. That silence is scripted, not slack.

### Clip 3 — 20.0 to 30.0 s · the turn

| # | Line | Words |
|---|---|---|
| 7 | "Property Abundance does the boring thing. They write it down." | 10 |
| 8 | "What the house is worth fixed up. Minus the repairs. Minus what it costs to hold it and sell it again." | 21 |

The on-screen math builds under line 8. It is typed in the edit, never generated.

### Clip 4 — 30.0 to 38.5 s · the close and the button

| # | Line | Words |
|---|---|---|
| 9 | "What's left is your offer. That's the whole formula." | 9 |
| 10 | "Ask them for that sheet." | 5 |
| 11 | "Then ask me for mine." | 5 |
| 12 | "I don't have one." | 4 |

The cord turns over empty on line 11, a 0.55 s beat, then line 12. The failed solution cannot produce the
one thing it just told you to ask for. That is the whole ad in four words.

**Measured word count:** 113 spoken words (`wc -w`, 2026-09-23).
**Planned runtime:** 38.5 s. **Overall pace: 176.1 wpm.**

That is below ref 6's 182, the slowest of the five references. The gap is 4.60 s of deliberate silence — the
beat before "I'll wait" and the beat before "I don't have one". Those two silences are the format's joke.
The talking-head cut of this same ad measured 191.7 wpm and contains no silence at all.

If you would rather sit inside the reference band, cut both pauses: the ad lands at about 35.2 s and
192.6 wpm, and loses the button. That is a real trade, not a rounding error. Pick one.

**One number here is a plan, not a measurement.** Every line timing assumes the model speaks at 0.30 s per
word, which is 200 wpm while actually talking. Check that against the first render. If it reads slower,
lines get trimmed, not stretched.

### Optional swap for the commitment lines

Only if you will genuinely tell a seller when listing beats your offer. Replaces line 9:

> "Sometimes that number beats listing. Sometimes it doesn't. They'll tell you which one you're looking at."

That is 18 words instead of 9, so clip 4 runs about 2.9 s longer and the ad delivers at about 39 s.

---

## 4. Character bible — paste this block verbatim into every prompt

Repo rule 4: paraphrasing breaks consistency. Identical wording is what makes the model re-render the same character.

```
THE OBJECT (identical in every shot): a cream-white 1990s corded kitchen wall telephone,
about 24 cm tall, yellowed with age, one hairline crack across the lower right corner of the
body. It is a living Pixar-style 3D cartoon character. Its two round dial buttons are its
eyes, glossy and expressive, set slightly too far apart. The handset rests in its cradle and
the cradle slot is its mouth, which opens and closes as it speaks. The coiled beige cord is
its one limp arm, hanging down and curling on the counter. Soft rounded cartoon shapes,
matte plastic with fine dust in the seams, warm subsurface light in the plastic. All keypad
buttons are completely blank. No digits, no letters, no labels, no logos, no brand marks
anywhere on the object.
```

```
THE ROOM (identical in every shot): a dated suburban kitchen in an empty inherited house.
Oak cabinets, a laminate counter with a chipped edge, a bare fridge with four faded tape
marks where photos used to be, one window over the sink. Cool grey daylight from the window
plus one warm ceiling bulb. Dust in the air. Nobody in the room at any point.
```

---

## 5. Production path — free route

The three existing renders in this folder measure **720x1280, 24 fps, 10.005 s** (`ffprobe`, 2026-09-23),
so the free Gemini route gives ten-second clips. Four of them cover this ad.

| Step | Do | Cost |
|---|---|---|
| 1 | **Hero image first.** Generate the object in the Gemini app from §6. Pick the most expressive of 4–6 variations. Save as `refs/ad4_object_hero.png`. | free in the app |
| 2 | Generate clips 1–4 from §7, one request each, **attaching the hero image every time**. Never reference the previous clip — that is what makes the character drift. | free in the app |
| 3 | Join, add the math text, captions, end card, master. §8. | free, local |

Paid alternative, only with your explicit go-ahead: Nano Banana Pro (~$0.09/image) for the hero and
Seedance 2.0 ($0.205/s ≈ $7.38 for 36 s) for native lipsync. Not run. Not needed to start.

---

## 6. The prompts live in JSON now

The prose prompts that were in this section have been replaced. They said the same thing in a form the
model was free to reinterpret, and reinterpretation is what put the camera behind the character.

| File | What it is |
|---|---|
| `Property_Abundance_Ad4_TalkingObjects_PROMPTS_v1.json` | The whole build as one structured document: world geometry, camera convention, object and room bibles, style, hard rules, negative prompt, failure guards, hero image, four clips with per-line timings, edit spec, ship gates. |
| `Ad4_TalkingObjects_paste/01_hero_image.json` | Paste-ready. Run first. |
| `Ad4_TalkingObjects_paste/02_clip1.json` … `05_clip4.json` | Paste-ready, one request each, globals already merged in. |
| `Ad4_TalkingObjects_paste/RUN-SHEET.md` | The order, the three anti-drift rules, and the stop-after-clip-1 gate. |

### What the JSON adds that prose could not

- **`world`** — an origin, three axes, and where the window, the wall and the camera sit in that space.
- **`camera_convention.azimuth_deg`** — camera angle measured off *the phone's own face*, not off the room.
  0 is dead in front. The whole ad stays between -20 and +20.
- **`facing_contract`** — repeated in all four clips: the face points at the lens every frame, and if the
  camera moves, the phone turns with it.
- **`failure_guards`** — each failure seen in the earlier renders, paired with the field that now prevents it.
- **`dialogue_timeline`** — start and end second for every line, so a render can be checked against a number
  instead of a feeling.
- **`verify_after_render`** — per clip, what to look at before generating the next one.

## 7. Edit spec

| Setting | Value | Where it came from |
|---|---|---|
| Source clips | 720x1280, 24 fps, 10.005 s each | `ffprobe` on the three existing Gemini renders, 2026-09-23 |
| Delivery | 1080x1920, 30 fps | Ad 4 brief, and the skill's fixed delivery rule. Conform with `scale=1080:1920:flags=lanczos` and `-r 30` |
| Length | 38.5 s | Between ref 3 (32.37 s) and ref 1 (51.03 s, judged too long) |
| Cuts | 3, one per clip join, at 10.0 / 20.0 / 30.0 | The format is one continuous character take. It does not get the 2.70 s cut rate of the talking-head cut |
| Math build | Typed over clip 3's empty left third, one line per spoken phrase: `VALUE FIXED UP` / `− REPAIRS` / `− HOLD + RESELL`, then `= YOUR OFFER` on line 9 | Ad 4 brief shots 3–6 |
| Longest hold | `= YOUR OFFER` stays on screen from 30.0 s to the end card | Skill rule: the payoff sits in the static stretch |
| Loudness | −14 LUFS integrated | Reference reel measured −14.34; refs 1, 2, 6 measured −14.2 |
| Captions | `dynamic_captions_3click` | Ref 2 failed on thin white-on-cream text. Ours must read with sound off |
| End card | Over clip 4's silent tail: logo + form URL | — |

**Known tooling constraint, measured 2026-09-23:** `ffmpeg` on this machine is built without `libfreetype`
and without `libass`, so `drawtext` and `subtitles` do not exist. The last session rendered captions as
transparent PNGs with Pillow and composited them with `overlay` + `enable='between(t,a,b)'`. Same route here
for both the captions and the math build.

**No dollar figures anywhere**, on screen or spoken. Ref 2 put "$450,000" on a run-down clay house and invited
the lowball doubt it was trying to calm.

---

## 8. What must be true before this ships

| Slot | Needed |
|---|---|
| Lines 7–9 | Your real offer formula. If it is not value − repairs − carry/resell, rewrite those lines to match what you actually do. |
| Optional swap | You will genuinely tell a seller when listing beats your offer. If not, leave it out. |
| End card | A form URL that loads. `propertyabundanceusa.com` returned HTTP 403 on 2026-09-22. |
| All | Meta Housing Special Ad Category status — not yet checked. |
| Format | The confession is a claim about a category. Lines 2 and 4 are true of any phone call and of any yard sign, which is why they are safe. Do not add a line about what other buyers pay. |

## 9. Deliberately not in this ad

- No named competitor. No claim about what another buyer pays.
- No dollar figures, no days-to-close, no "offer in 24 hours" — no number that is not Property Abundance's real measured fact.
- No countdown, no cap, no "now or never". The research says hype reads as a scam signal.
- No actor or character presented as a real past customer. 16 CFR 465.2 and 255.1.
- No cash fanning, no money counting.
- No second talking character. The format is one object, one take.
