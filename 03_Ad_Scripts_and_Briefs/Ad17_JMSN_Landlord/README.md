# Ad 17: JMSN in the trashed rental ("Now You Can Too")

Property Abundance AI UGC ad for Persona 3, the Burned-Out Landlord. The tenant is gone, the rental is trashed and the mortgage still comes out every month. JMSN speaks as Property Abundance's buyer (company voice). He is never a landlord or customer, so no AI label is needed. The brand name is never spoken; it appears as the logo on the end card.

**Status (2026-09-27):** script and storyboard v4, synced to the Seedance plan.
- **The takes:** 3 takes of 8 s with Seedance 2.0 at 720p, filmed by a camera operator. No video take has been generated.
- **Take 3 is cut to 19 words** to fit 8 s. Status: proposed; user reply "yeah", explicit confirmation requested before take 3.

**Credits already spent: 36.** 2 × 18 went on the v3 selfie scene images `13_Generated/images/Ad17_JMSN_L1_front_door_v1.png` and `..._L2_wall_hole_v1.png` (the logs `10_Video_Builds/Ad17_JMSN_Landlord/logs/Ad17_L1_v1.log` and `Ad17_L2_v1.log` record `creditsConsumed` 18.0 each). They are **superseded and not used**: the Seedance takes use 2 reference crops and no first frame.

## Files

| File | What it is |
|---|---|
| `Ad17_BREAKDOWN_v4.md` | **Current.** It covers:<br>• Step 1 Research, Step 2 Offer and Step 3 Write (20 scored hooks, template #5 Us vs. Them).<br>• The four-part breakdown, with Part C for a camera operator and the Seedance clip plan.<br>• The test plan.<br>• The AI-pass appendix. |
| `Ad17_SCRIPT_3clips_shot_list.json` | **Current (v4 Seedance sync).** 8 shots, 7 cuts at sentence starts, 3 takes of 8 s. It also holds the per-take dialogue, the model and settings, the 2 reference images, the Seedance prompt paths, the superseded files, text pops, hook variants, costs and flags. |
| `Ad17_GEMINI_VEO_PLAN_v1.txt` | Remake plan for Gemini web (Veo), 2026-09-27: 3 talking clips (T1-T3) and 3 house-only clips (B1-B3), same script with "as it is", a human-voice brief, a per-clip reject checklist and the edit steps. |
| `old/OLD_Ad17_BREAKDOWN_v3.md` | v3: the full playbook run, selfie framing |
| `old/OLD_Ad17_BREAKDOWN_v2.md` | v2: review fixes 1-4, template only |
| `old/OLD_Ad17_BREAKDOWN_v1.md` | v1, which failed review |

Related files in `10_Video_Builds/Ad17_JMSN_Landlord/`:
- **Current take prompts (Seedance 2.0):** `Ad17_seedance_prompt_take1_porch.txt`, `..._take2_wall_hole.txt`, `..._take3_bedroom.txt`. Their dialogue matches this script (checked by script). ugc-video-director owns them.
- **Reference images:** `13_Generated/images/Ad17_JMSN_ref_face_crop.png` (428 × 886) and `..._ref_body_crop.png` (430 × 946).
- **Superseded, not used:** the Omni prompts `Ad17_video_prompt_clip1/2/3_*.txt` and the image prompts `Ad17_image_prompt_L1/L2/L3_*.txt`.
- **Reviews:** `REVIEW_script_v1.md`, `REVIEW_pregen_v1.md`, `REVIEW_seedance_v1.md`.

## Script at a glance (H1)

| Take | Location | Words | Dialogue |
|---|---|---|---|
| 1 (8 s) | L1 porch and open front door (he stays in the doorway) | 19 | The tenant left. Now YOU can too. House is sitting empty. Same mortgage, every month. So what's the move? |
| 2 (8 s) | L2 living room, hole in the wall (no orbit) | 18 | Patch THAT and bet on the NEXT tenant? Fix it, list it, pay commission? Or sell it AS-IS. |
| 3 (8 s) | L3 bedroom, ceiling leak | 19 | Our offer's LOWER than a fixed-up sale. No commission, no fees. They left. That's how YOU leave. Tap below. |

- 56 words in total.
- Loops run OPEN A → OPEN B → CLOSE B → CLOSE A, nested.
- 7 cuts in about 21.9 s (3.19 per 10 s, estimate), each at a sentence start.
- Light: low late-afternoon sun with hard shadows.
- The end card reads "Ask for my offer" / "No obligation".
- Alternate hooks: H2 "What the tenant broke? Not YOURS to fix.", H3 "Before the contractor, get the AS-IS number." and H4 "Walking away from THIS isn't giving up."
- **Planned cost at list price, not yet run:** 3 × 328 = 984 credits ($4.92), at 41 credits/s × 8 s. An audio surcharge is not confirmed. Each extra hook variant costs 656 credits (takes 1 and 3).

## Open
- **Before take 3:** the user's explicit yes on the 19-word cut and on "Our offer's LOWER than a fixed-up sale". That line is not on the CLAUDE.md confirmed list; it was used in the Ad 16 final and the approved Ad 15 v2 script.
- **Before spend:**
  - The second click fails (measured 2026-09-27): propertyabundanceusa.com returns 403 over http and a certificate error over https, and a search shows only the UK training company.
  - Set Meta's Housing Special Ad Category when the campaign is created.
  - There is no proof yet (the template's [Proof] slot is empty).
  - Reconfirm "we buy it ourselves" for the page.

## Current video (2026-09-27)
- **`13_Generated/videos/Ad17_final_v11_refs.mp4`**, picked by the user on 2026-09-27. JMSN on "Same mortgage", signing papers on "pay commission?", a $100 bundle on "No commission, no fees", stock colour-matched, "Or sell it as it is." in a clone of JMSN's voice under the ceiling-leak cutaway. Build: `10_Video_Builds/Ad17_JMSN_Landlord/build_final_v11_refs.py` (it runs on `build_final_v9_newvoice.py` and `build_final_v8_recut.py`). Log: `session-chat/2026-09-27_ad17-v8-recut.session.md`.
- The older cuts (v1-v10) were moved to the Finder Trash on 2026-09-27 at the user's request. Their build scripts are kept.
