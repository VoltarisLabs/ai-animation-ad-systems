# JMSN-3D — stylized 3D animated character

Built 2026-09-23. Schema: `JMSN-3D_character.json`.

Face derived from a separate photoreal base character,
rebuilt as a CG-animated character: very short 360 waves flat to the skull, thin
mustache and chin goatee, warm medium-brown skin, dark brown eyes.

> **Separate asset. Never mix references.** The base character's lockfile carries
> `negative: no cartoon styling`. Feeding the base character's photoreal refs into JMSN-3D,
> or JMSN-3D's renders back into the base character, contaminates both.

---

## Read this before you expect consistency

**The same prompt does not give the same image.** Text-to-image models are not
deterministic. The Gemini app exposes no seed field, so two runs of an identical
prompt give two different faces. Anyone who tells you a prompt alone locks a
character is wrong.

What the JSON actually buys you:

| It does | It does not |
|---|---|
| Removes the drift caused by vague words — "strong jaw" is a different jaw every time, `gonial_angle_degrees: 122` is not | Make the model deterministic |
| Gives named handles so you change one field and nothing else moves | Survive without reference images |
| Pins the profile and three-quarter views, which is where faces usually re-invent themselves | Guarantee the first render is right |

**The lock is: render the turnaround once → save it → attach it to every
future prompt.** The JSON gets you a good first face and keeps the language
stable. The attached image is what holds it.

---

## Engine (free)

gemini.google.com → **Nano Banana 2**. Free tier, compute-based limits refreshing
roughly every 5 hours, no published per-day number
(`~/.claude/skills/brain/engines.md`, Images, checked 2026-09-10).

Nano Banana **Pro** needs a Google AI Plan. Paid. Not used here.

Nano Banana is a *renderer*, not a vibe machine — it rewards a dense schema.
Midjourney would ignore most of this (`~/.claude/skills/json_render_workflow/`).

---

## Run order

### 1. First render — the turnaround sheet

New Gemini chat. Nothing attached. Paste the whole
`JMSN-3D_character.json`, then this line under it:

```
Render this character as a model turnaround sheet: one row, four views of the
SAME character, left to right — front view, three-quarter left view, left
profile view, back view. Head and shoulders only. Identical face, hair, facial
hair, skin tone and lighting in all four views. Flat neutral mid-grey backdrop,
no props, no text, no labels. 16:9.
```

Head-and-shoulders, not full body — you are buying facial resolution, and a
four-up full body wastes it on shoes.

### 2. The second pass — this is the one you keep

First renders tilt and drift. Paste the **exact same JSON** into the same chat
with one line appended:

```
Faithfully follow this JSON. Correct any view that deviates from the stated
ratios. Keep all four views identical in face, hair and lighting.
```

The `json_render_workflow` skill calls this the regenerate trick. Do not stop
at v1.

### 3. Save it

```
09_Characters/JMSN-3D/turnaround_v1.png
09_Characters/JMSN-3D/front_v1.png
09_Characters/JMSN-3D/threequarter_v1.png
09_Characters/JMSN-3D/profile_v1.png
```

Crop the individual views out of the turnaround. Four separate files beat one
sheet as attachments.

### 4. Every scene from then on

New chat. Attach all four. Paste:

```
Use the attached reference images. This is the same character — identical face,
identical head proportions, identical hair, identical facial hair, identical
skin tone.

[paste the full JSON]

SCENE: <your scene, including the shot type>
```

**Bake the shot type into the scene.** Never ask for a close-up as a follow-up
in a chat that already rendered — the model reinterprets and the face breaks.
Start a fresh chat instead. That is the single most common way people lose a
character.

---

## Which fields to move, which to freeze

**Freeze** — these are identity. Changing one gives you a different person:
`skull`, `eyes`, `brows`, `nose`, `mouth`, `cheeks_and_jaw`, `ears`,
`profile_view_lock`, `three_quarter_view_lock`, `hair`, `facial_hair`, `skin`.

**Move freely** — these are style, not identity:
`wardrobe_default`, `lighting_default`, `camera_default`, and the scene text.

Change **one field per render**. That is the whole point of a schema — you can
see what caused the change. Change three and you have learned nothing.

---

## Check every render against the sheet

- [ ] Eye line still sits below the vertical midpoint of the head
- [ ] Cranium still reads larger than the jaw
- [ ] Hair still flat to the skull, no lift, silhouette follows the cranium
- [ ] Goatee is a chin patch only, not connected to the mustache or jawline
- [ ] Hands and neck match the face albedo
- [ ] Sclera is off-white, not pure white
- [ ] No earrings, no logos, no readable text
- [ ] Still reads as CG-animated, not photoreal and not anime

If two of these fail, the face has drifted. Re-attach the turnaround and rerun
rather than editing the image.

---

## Status

Nothing has been generated. Every value in the JSON is a specification, not a
measured output. The proportions are a coherent stylization, but which of them
Nano Banana 2 actually honours is unknown until step 1 runs.
