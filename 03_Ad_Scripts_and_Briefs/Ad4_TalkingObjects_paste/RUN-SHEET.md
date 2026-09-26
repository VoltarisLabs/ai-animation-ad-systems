# Ad 4 · talking objects · run sheet

Written for whoever is at the machine, generating.

Five files in this folder. Each one is a complete request. You never merge anything by hand.

| Order | File | What you do | Costs |
|---|---|---|---|
| 1 | `01_hero_image.json` | Paste into the Gemini app. Ask for 6 variations. Save the best as `refs/ad4_object_hero.png`. | free |
| 2 | `02_clip1.json` | Paste. **Attach `refs/ad4_object_hero.png`.** Check it against the verify list at the bottom of the file. | free |
| 3 | `03_clip2.json` | Same. Attach the hero again. | free |
| 4 | `04_clip3.json` | Same. Attach the hero again. | free |
| 5 | `05_clip4.json` | Same. Attach the hero again. | free |

## Three rules that stop the drift

1. **Attach the hero image to every single clip request.** Never attach the previous clip. Referencing the previous shot is what compounds drift across a sequence.
2. **One clip per request.** Two clips in one request is how you get an invented cut.
3. **Do not reword anything.** `object_bible` and `room_bible` are pasted byte-identical in all four files on purpose. Identical wording is what makes the model re-render the same character. Paraphrasing breaks it.

## Stop after clip 1

Generate clip 1 alone. Open it and check the five lines in `_verify_after_render`. If the face is turned away from the lens, or the camera ended up behind the phone, **do not** generate clips 2 to 4. Fix clip 1 first, because the same wording produces the same error three more times.

A fail means a more specific prompt, not a bigger model.

## What fixes the camera problem you hit

Three separate statements of the same constraint appear in every clip file:

- `world.camera_side` — "The camera always lives in +Z space, in front of the phone. Never in -Z space."
- `camera.azimuth_deg` — degrees measured **off the phone's own face**, not off the room. 0 is dead in front. The whole ad stays inside -20 to +20.
- `facing_contract` — a full paragraph saying the face points at the lens every frame, and that if the camera moves, the phone turns with it.

Clip 3 is the only one where the camera moves off-axis, and it says explicitly that the phone rotates 12 degrees to follow, so the face still points at the lens at the end.

## After all four render

Order: clip 1, clip 2, clip 3, clip 4. Cuts land at 10.0, 20.0 and 30.0 seconds. Clip 4 is trimmed at 8.5 seconds, so the ad delivers at 38.5 seconds.

The offer math is typed into the empty right third that clip 3's drift opens up. It is never generated. Full timings in `../Property_Abundance_Ad4_TalkingObjects_PROMPTS_v1.json` under `edit`.

## Before it ships

Nothing goes live until the real offer formula is in lines 7 and 8, and until the form URL returns HTTP 200. `propertyabundanceusa.com` returned HTTP 403 on 2026-09-22. Meta's Housing Special Ad Category status is still unchecked.
