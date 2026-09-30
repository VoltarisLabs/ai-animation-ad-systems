# QA and launch

## 1. Automated checks after every render

`bash scripts/qa_checks.sh out/ad.mp4 work/script.txt` (script.txt = the final voice script as plain text; quoted text also works):

- Frame count equals duration x 24 (catches drift from unsnapped cuts).
- `blackdetect` and `freezedetect` find nothing unexpected (a still with a push-in is not frozen; a static freeze-frame shot is expected).
- `ebur128`: integrated about -14 LUFS, peak under about -1.5.
- faster-whisper transcript of the final audio matches the script word for word. If the first line comes out wrong ("The ceilings leak"), an effect is masking it: lower it or move it.

Manual checks (the script does not do these):

- Key word times: compare the pop / list / strike times the builder prints with the word times in `work/vo_words.json` mapped through the pause map; each within about 0.25 s of its word.
- `bash scripts/contact_sheet.sh out/ad.mp4 2 12` plus a few full-size frames at the busy moments. Look at them.

## 2. Three-lens review with adversarial verification

`scripts/qa_workflow.js` is a Claude Code Workflow: three reviewers run in parallel, each with its own lens; each reviewer's findings go to a verifier told to refute them by re-measuring. Only confirmed findings come back, each with a timestamp, evidence and a concrete fix. Run it with the Workflow tool: `scriptPath` = the skill's `scripts/qa_workflow.js`, `args` = `{dir, video, registry, python, script, onscreen, builder}` (it stops if one is missing).

| Lens | What it checks |
|---|---|
| Sync and sound | subtitles/titles/pops on their words, cuts between lines, nothing lingering across a cut, clipped words, clicks, effects masking words (per-word band SNR, whisper A/B with and without each effect stem), jingle vs CTA, loudness |
| Visual | text over faces, safe zones, legibility on a phone, overlapping elements, AI glitches (hands, drift, garbled text), freeze and stills quality |
| Compliance | every spoken and on-screen word against the registry's Section 5 checklist, company name, game names/logos, weapons/police/crime, platform-UI lookalikes (a bare row of stars reads as a rating: keep the STRESS label), testimonial framing, Meta housing-ad risks |

Typical confirmed findings: an effect with a long silent lead-in landing late; a jingle over the punchline; a zero-length subtitle; a banner carried a few frames into the next shot; the minimap on a face; the company admission playing over a face-on close-up.

Fix, re-render, re-run the automated checks, and look at the frames that changed.

## 3. Launch gate (say it at every delivery)

- Landing page works (registry Section 6: `propertyabundanceusa.com` returned 403; no ad sends traffic until fixed).
- Every claim is in registry Section 1; unconfirmed ones (bonus cash, speed, "any condition") wait for the owner.
- The owner has seen any made-up homeowner character.
- Written consent for any cloned voice and a licence for any third-party sound effects are filed next to the ad (`PERMISSIONS.md`).
- Music added at upload from the platform's commercial library.

Deliver: final mp4 in the ads folder with a plain name, plus 3-6 short lines on what changed and what still blocks launch.
