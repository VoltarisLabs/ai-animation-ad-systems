# Ad 23: "The Letter" (Zack D 3D story ad): script and shot plan v1

Picked by the user on 2026-10-06 (option 1 of 3).

**Format:** Zack D 3D story, 9:16. A narrator speaks the whole ad; nobody on screen speaks.

**Rules followed:**
- `11_Psychological_Hooks/claims-registry.md`, `sell-the-destination.md` and `DRAMA_HOOK_RETENTION_RULES.md`.
- `01_Skills_and_SOPs/Zack_D_3D/STEP_LOOP_PROMPT_TEMPLATES.md`.

**Local only:** this is not a UGC format, so it doesn't go on Airtable.

## Script

134 words, 47.3 s at 170 wpm.

| # | Time | Line | Tag |
|---|---|---|---|
| L01 | 0.0-3.9 | Someone taped a letter to her door. Every neighbor signed it. | PAIN, OPEN A |
| L02 | 3.9-7.1 | It called her house the eyesore of the street. | PAIN |
| L03 | 7.1-11.3 | But her realtor said: fix everything first, or it will never sell. | PAIN, OPEN B |
| L04 | 11.3-13.8 | So she stopped waving at the neighbors. | PAIN |
| L05 | 13.8-16.6 | Then she asked: what if it sells untouched? | PATH, OPEN C |
| L06 | 16.6-20.5 | Truth? Cash offers usually come in lower than listing. Ours too. | PAIN (registry admission) |
| L07 | 20.5-24.0 | That's why nothing got touched. The house sells as-is. | PLANE, CLOSE C |
| L08 | 24.0-27.5 | That's why lower isn't everything. No commission. No closing costs. | DEST |
| L09 | 27.5-31.1 | That's why the fix-it list went in the recycling. | DEST, CLOSE B |
| L10 | 31.1-34.6 | She kept her reading chair and chose her closing day. | PATH |
| L11 | 34.6-38.1 | That's why the next letter on her door said welcome. | DEST, CLOSE A |
| L12 | 38.1-43.1 | New street, fresh cookies from next door, and she waves first, every single morning. | DEST |
| L13 | 43.1-47.3 | House the neighbors complain about? Ask for a cash offer. No obligation. | CTA |

- **Brand:** not spoken until the owner confirms the name. The repo rule is to say it once, in Close A.
- **Words added in the edit, never generated:** the letter's signatures, "Welcome" on the card, the hook text, the term pops, captions and the end card.

## Cast and references

| Asset | File | Status |
|---|---|---|
| Maya | `13_Generated/images/ZackD_3D/ZackD_Maya_master_sheet_v3_pixar_1k.jpeg` (course Pixar style, 2026-10-06) | done |
| Maya's old house | `13_Generated/images/ZackD_3D/ZackD_House_sheet1_exterior_v3_pixar_worn.jpeg` (course style, 1K). Checked 2026-10-06: the two front views mirror the front (door in the west bay in one, the east bay in the other; the porch overhangs a different side); back-left has the chimney on the wrong wall; back-right has the garage and driveway on the wrong side; no sagging gutter. **Rules:** every house shot uses one front: the street sheet's (window, door + steps in the middle bay, window; porch flush with the house; 4 columns on brick bases). Front-on shots attach `ATTACH_street_wide.jpg`; only S09's angle attaches `ATTACH_house_front_right.jpg`, with the door position written in words. Never attach `ATTACH_house_front_left.jpg` or the back crops. Write the wear and the sagging gutter into every house prompt. | done, with rules |
| Old house interior | `13_Generated/images/ZackD_3D/ZackD_House_sheet2_cutaway_v2.jpeg` (kitchen, living room) | done |
| Supporting cast: the realtor, 2 old-street neighbors, the new neighbor | `13_Generated/images/ZackD_3D/Ad23_cast_sheet_v2_pixar.png` (course Pixar style, 9:16 2K, prompt `prompts/step0_A_cast_sheet_v2_course_style.txt`). v1 failed on style (semi-realistic). Extras to repeat in scene prompts: white pocket square (realtor), pearl studs + ring (neighbor 2), small gold studs (new neighbor). | made, waiting on the user's OK |
| The street (her house + 4 tidy neighbor houses) | `13_Generated/images/ZackD_3D/Ad23_street_sheet_v4_pixar.png` (course style, 9:16 2K, prompt `prompts/step0_B_street_sheet_v4_9x16.txt`); crops `ATTACH_street_wide.jpg`, `ATTACH_street_from_porch.jpg`. The blue house here has no garage or driveway: any shot that shows the house's right side (S09's arc) takes the house master, not this sheet. | made, waiting on the user's OK |
| The new home (exterior, door, living room) | `prompts/step0_C_new_home_sheet.txt` (upload the house exterior sheet, as a style reference only) | Step 0 |
| Props: the letter on the door, teal reading chair, clipboard, recycling bin, calendar, cookies + card | `prompts/step0_D_props_sheet.txt` (upload the house exterior sheet) | Step 0 |

Prompt files are in `10_Video_Builds/Ad23_ZackD_TheLetter/prompts/`.

## Shot plan

**Settings for every image (user, 2026-10-06):** Nano Banana Pro, **9:16, 2K**. A first-time generation attaches only the master that sets the style or character; everything else is described in words.

**Settings for every clip (user, 2026-10-06):** Kling 3.0 (`kling-3.0/video`, std mode), **9:16, 720p, 5 s**, start image only (no end image), sound off. Where the camera continues into the next shot, that clip starts from the previous approved clip's last frame (free). Each new location starts from a fresh Nano Banana Pro image. Prompts: `prompts/S<nn>_start_image_v<n>.txt` and `prompts/S<nn>_clip_kling_v<n>.txt`. Every clip is saved next to the images in `13_Generated/images/ZackD_3D/` (user, 2026-10-06).

17 shots, average 2.8 s. Each clip is generated at 5 s; only the clean seconds are kept.

| Shot | Time | Line | Shot + action | Frames | Attach |
|---|---|---|---|---|---|
| S01 | 0.0-3.9 | L01 | **Hook (2026-10-06):** over the grey-haired neighbor's shoulder she slaps the blank paper onto the red panelled door, turns away with a disapproving squint and leaves; slow push-in on the letter. Edit: EYESORE in red marker from frame 1, 8-10 signatures write on (tracked to the paper), headline THE WHOLE STREET SIGNED IT. DONE: start `Ad23_S01_start_v2_zackd.png`, clip `13_Generated/images/ZackD_3D/Ad23_S01_clip_omni_v1.mp4` (Gemini Omni 4 s 720p, 63 credits), last frame `Ad23_S01_clip_omni_v1_lastframe.png` | start (Omni) | neighbor 2, door |
| S02 | 3.9-7.1 | L02 | **Reveal:** the camera pulls back fast from the letter, out over the porch and across the street: Maya on her porch reading it, hand over her mouth; the two neighbors in the foreground, arms crossed. Edit: red marker circle round her house + EYESORE. Kling 3.0 first frame = S01 clip's last frame, last frame = new reveal image | first + last (Kling) | street, Maya, neighbors 2 + 3 |
| S03 | (merged) | | Merged into S02 (the reveal). The old S02 (Maya opening the door inside) is dropped from the hook. | | |
| S04 | 7.1-9.4 | L03 | Medium on the front walk: the realtor points up at the roof and shakes his head; Maya beside him, arms folded | start | Maya, realtor, house |
| S05 | 9.4-11.3 | L03 | Insert: his pen taps the peeling trim under the sagging gutter | start | house |
| S06 | 11.3-13.8 | L04 | Medium-wide at her mailbox: neighbor 2 lifts a hand to wave; Maya looks down and turns away | start | Maya, cast 2, street |
| S07 | 13.8-16.6 | L05 | Night, inside: Maya in the teal chair under lamplight, phone at her ear (screen away), looking up at a water-stained ceiling. Text: WHAT IF IT SELLS UNTOUCHED? | start | Maya, chair, living room |
| S08 | 16.6-20.5 | L06 | Close-up push-in on Maya's face; she lowers the phone and thinks. No cutaway during the admission. | start | Maya portrait |
| S09 | 20.5-24.0 | L07 | Day, wide, slow arc: the house exactly as it was; Maya calm on the porch steps | start | house, Maya |
| S10 | 24.0-27.5 | L08 | Medium: Maya at a clear kitchen table sets down a pen beside a closed folder, breathes out, smiles. Term pops added in the edit. | start | Maya, kitchen |
| S11 | 27.5-31.1 | L09 | Insert at the curb: her hand drops the clipboard's blank list into the blue recycling bin; the lid flips shut | start + end | Maya forearm, clipboard, bin |
| S12 | 31.1-33.1 | L10 | Medium-wide: Maya carries the teal chair down the porch steps, smiling | start + end | Maya, chair, house |
| S13 | 33.1-34.6 | L10 | Insert: a red marker circles one empty square on a blank wall calendar | start + end | calendar |
| S14 | 34.6-38.1 | L11 | New sage-green door: a cream card tucked in the frame; Maya opens it and smiles. "Welcome" added in the edit. | start + end | Maya, new door, card |
| S15 | 38.1-40.6 | L12 | New porch: the new neighbor leans over the low fence with the cookie plate; Maya takes it, laughing | start | Maya, cast 4, new home |
| S16 | 40.6-43.1 | L12 | Golden morning: Maya steps out with coffee and waves first; the neighbor waves back | start | Maya, cast 4, new home |
| S17 | 43.1-47.3 | L13 | Hold S16's last frame with a slow push; end card "Ask for a cash offer · No obligation" | none (edit) | none |

That's 16 clips: 16 start frames and 6 end frames (S01, S02, S11, S12, S13, S14).

## Rules for every frame and clip (to avoid the AI-slop look)

1. **Same style line, same references.** Every frame uses the STYLE line from the Step 0 prompts and attaches Maya plus the matching location crop.
2. **Check every frame against Maya's sheet:** her one beauty mark, gold hoops, watch on the left wrist, camel blazer.
3. **Clips:**
   - one action and one camera move each;
   - first and last frame where the state changes;
   - "single continuous shot";
   - mouths closed, nobody speaks;
   - no extra people.
4. **No text, signs or numbers inside AI frames.** All of it goes on in the edit.
5. **Light stays continuous:**
   - day scenes: late morning;
   - S07-S08: lamplit night;
   - S14-S16: golden morning.
6. **Close-up inserts on the key nouns** (tape, gutter, list, calendar), Zack D style. A new shot every 2-3 s.
7. **Hands do one simple action each.** Check the fingers on every hand frame.
8. **Sound:**
   - effects: tape rip, door creak, birds, paper, bin lid thunk, plate clink;
   - one licensed music bed, swelling on the peak (S14) and fading out;
   - voice on top.
9. **Keep only the clean seconds of each clip.** Regenerate any clip with a morph or a face change.

## Cost (Kie list prices; images measured at 18 credits)

| Item | Count | Credits |
|---|---|---|
| Step 0 reference sheets (Nano Banana Pro 2K) | 4 | 72 |
| Scene frames (Nano Banana Pro 9:16 2K) | 22 | 396 |
| Clips, Kling 3.0, 5 s, 720p, no audio (chosen 2026-10-06) | 16 | 1,120 (70 each: 14 credits per second, Kie list price 2026-10-06, not measured) |
| Narrator (ElevenLabs via Kie, about 700 characters) | 1 | about 10 |
| **Total** | | **about 1,918 credits ($9.59) at 1080p, or 1,598 ($7.99) at 720p**, plus redos |

Kie balance on 2026-10-06: 7,547.29.
