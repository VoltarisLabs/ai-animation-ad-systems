# Ad 16: JMSN house walkthrough ("The Catch"): where everything is

Every Ad 16 file starts with `Ad16_`. Files that are no longer used are in `old/` folders and start with `OLD_`.

## 1. Script
| File | What it is |
|---|---|
| `03_Ad_Scripts_and_Briefs/Ad16_JMSN_Walkthrough/Ad16_SCRIPT_3clips_shot_list.json` | **The current script.** 3 clips of 8 s, with a time, camera, picture and on-screen text for every shot |
| `11_Psychological_Hooks/Ad16_JMSN_hook_bank.md` | All hook ideas, plus the longer 107-word version (3 loops) |

## 2. Character (JMSN)
| File | What it is |
|---|---|
| `13_Generated/images/Ad16_JMSN_character_sheet_B_CHOSEN.png` | **The chosen character** (6 views) |
| `13_Generated/images/Ad16_JMSN_character_sheet_A.png` | The other sheet, not chosen |
| `13_Generated/images/Ad16_JMSN_car_selfie_new_outfit_A.png` | Car selfie in the new outfit, take A |
| `13_Generated/images/Ad16_JMSN_car_selfie_new_outfit_B.png` | Car selfie in the new outfit, take B (used for real skin in the scene images) |
| `12_AI_Characters/JMSN/Ad16_prompt_character_sheet.txt` | The prompt that made the sheets |
| `12_AI_Characters/JMSN/Ad16_prompt_car_selfie_new_outfit.txt` | The prompt that made the car selfies |
| `12_AI_Characters/JMSN/Ad16_compare_*.jpg` | Side-by-side checks (faces, earbud, chain) |
| `12_AI_Characters/JMSN/outfit_1.jpg` | Your outfit reference (unchanged) |
| `12_AI_Characters/JMSN/JMSN_car_v1.png` | The original navy car selfie (unchanged) |

## 3. Scene images (generated 2026-09-27)
| File | What it is |
|---|---|
| `12_AI_Characters/JMSN/Ad16_prompt_scene_images.md` | All 3 scene prompts, with settings and the upload order |
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_image_prompt_scene1_front_walk.txt` | Scene 1 prompt: front walk |
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_image_prompt_scene2_kitchen.txt` | Scene 2 prompt: kitchen |
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_image_prompt_scene3_broken_floor.txt` | Scene 3 prompt: broken floor |

Images:
- `13_Generated/images/Ad16_JMSN_scene1_front_walk_v2.png`: **used for clip 1.** Clean, but has earbuds in both ears.
- `Ad16_JMSN_scene1_front_walk.png` (v1): car visor at the top, not used.
- `Ad16_JMSN_scene2_kitchen.png`: clean, for clip 2.
- `Ad16_JMSN_scene3_broken_floor.png`: car visor at the top, not used.
- `Ad16_JMSN_scene3_broken_floor_v2.png`: **for clip 3.** Clean, one earbud. Prompt: `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_image_prompt_scene3_broken_floor_v2.txt`.
- Scene 1 v2 prompt: `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_image_prompt_scene1_front_walk_v2.txt`.

## 4. Talking clips
| File | What it is |
|---|---|
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_video_prompt_clip1_front_walk.txt` | Clip 1 prompt (8 s) |
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_video_prompt_clip2_kitchen.txt` | Clip 2 prompt (8 s) |
| `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_video_prompt_clip3_broken_floor.txt` | Clip 3 prompt (10 s, 23 words: starts with "You fix NOTHING.", no company name) |

- **Clip 1 done:** `13_Generated/videos/Ad16_clip1_front_walk.mp4` (8.000 s, 1080 × 1920, all 21 words). Frames: `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_clip1_front_walk_frames_2fps.jpg`.
- **Clip 2 done:** `13_Generated/videos/Ad16_clip2_kitchen.mp4` (8.000 s). Omni dropped "You fix NOTHING." (19 of 22 words), so that line moved to clip 3.
- **Clip 3 done:** `13_Generated/videos/Ad16_clip3_broken_floor.mp4` (10.000 s). Omni said "That's why I'd buy it" twice; the edit cuts the first one out. Frames: `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_clip3_broken_floor_frames_2fps.jpg`.

## 4b. Final ad
- **`13_Generated/videos/Ad16_final_v1.mp4`**: 23.042 s, 1080 × 1920, -14.5 LUFS, all 63 words once. Frames: `10_Video_Builds/Ad16_JMSN_Walkthrough/Ad16_final_v1_frames_2fps.jpg`.
- Build script: `10_Video_Builds/Ad16_JMSN_Walkthrough/build_final_v1.py` (`--captions` redoes only the captions). B-roll sources: `Ad16_SOURCES_broll.md` in the same folder.
- Airtable holds a 720p review copy (`Ad16_final_v1_review_720p.mp4`, under the 5 MB upload limit).

## 5. Records
- `10_Video_Builds/Ad16_JMSN_Walkthrough/logs/`: one log per paid run. The 3 `STOPPED_` logs are the scene run you stopped (54 credits charged, no images saved).
- Airtable: base UGC_Ads, table Content, row "Ad16 - JMSN House Walkthrough - The Catch" (`recEIzDwdmSyFZ18i`). The images there are JPEG copies that still have their old names.
- Session log: `session-chat/2026-09-26_jmsn-walkthrough-prompts.session.md`.

## Old versions (not used)
- `03_Ad_Scripts_and_Briefs/Ad16_JMSN_Walkthrough/old/`: the first 4-clip plan, the "repair quotes" script, the 5-clip plan and the 5-clip shot list.
- `10_Video_Builds/Ad16_JMSN_Walkthrough/old/`: the 5-clip video prompts.
