---
name: claymation
description: Make a claymation (clay stop-motion look) story video ad for the cash home buying business, built shot by shot in Google Flow (Veo 3.1 clips, Nano Banana Pro images) with an ElevenLabs narrator and a local ffmpeg edit in the "ClayReel" card look. Use when someone types /claymation or asks for a claymation, clay or stop-motion ad, script options for one, its Flow prompts, its edit, a remade hook or a fix to a cut.
argument-hint: "[idea, team brief or finished script (optional)]"
---

# /claymation: claymation story ad

Request typed after the command: $ARGUMENTS

If nothing was typed, ask for the idea in one line, or offer three script options.

This command is the claymation front door to the shared pipeline skill in `${CLAUDE_PROJECT_DIR}/01_Skills_and_SOPs/Flow_Animated_Story_Ads/` (repo path `01_Skills_and_SOPs/Flow_Animated_Story_Ads/`). Read its `SKILL.md` first and follow it, making the claymation choices below at each stage. The look and edit choices here win over the shared defaults; the claims rules in the shared skill always win over everything.

## How to work with the person

Short, plain answers, one step at a time. Give one paste-ready prompt, wait for "done" / "clip added", check the clip, then give the next. The person runs Flow and ElevenLabs; you write every prompt and do the edit and QA locally. Never spend generation credits yourself.

## The claymation choices

| Stage | What to do | Read |
|---|---|---|
| 1. Script | Re-read `11_Psychological_Hooks/claims-registry.md` today. Nested loop (Open A, B, C, Main, Close C, B, A, Ask), 95-115 spoken words: a clay ad reads slower and runs 40-45 s. A finished team script is kept word for word in the script file, with every unconfirmed line marked NOT CLEARED and a safe swap beside it. The registry blocks production of a script that holds an unconfirmed claim, so voice, clips and on-screen text use the swaps until the owner clears each line; if the team still wants its own wording recorded, label that cut a draft that cannot launch. Options: a judge panel, top 3 as a table (Part / Narrator says / What we see). | `references/script-and-claims.md` |
| 2. Look | Make the clay character before any clip: a clean reference from the best frame of an approved clip (face crop and full body side by side), or a Nano Banana Pro sheet. Attach it to every clip. Style words: "Claymation stop-motion... handmade clay, visible fingerprints, choppy stop-motion movement, warm lamp light". Never mix in game-look words (no cel shading, ink outlines or HUD). | `references/flow-prompting.md` sections 1 and 5 |
| 3. Clips | One action per clip, starting mid-action, "single shot, no cuts", "He does not speak. No dialogue, no voice, no music", no text or numbers. Death or grief words get prompts blocked: imply them (an inherited house, a keepsake box). Money on screen only for an offer the owner has confirmed. For the prompt layout use the section 2 template with the clay style line from section 5 as the style words, and leave out "2D animated illustration, not 3D, not photoreal" (that line is for the game look only). | `references/flow-prompting.md` sections 2, 3 and 6 |
| 4. Voice | ElevenLabs "Brian" (library voice), Multilingual v2: speed 0.92, stability 44, similarity 46, style 27. An excited hook re-read: same voice, stability 25, style 60, speed 1.05, three takes, levelled to about 2 LU above the rest. Generate on a paid ElevenLabs plan (the free plan has no commercial licence) and write the voice, the plan and any sound-effect sources in `PERMISSIONS.md` next to the ad. | `references/voice-and-audio-rights.md` |
| 5. Edit | The card-reel builder: copy `scripts/build_card_reel.py`, `scripts/render_card_reel.sh` and `scripts/make_card_assets.py` into `10_Video_Builds/<Ad_Name>/` beside `src/` and `work/`. Make word times with `scripts/words.py`, then edit only the CONFIG block: INPUT_FILES and the index names, CLIP_LEN, BEATS (each card's lead words and red keyword), STAMPS, SFX and INTRO_*. All card text lives in CONFIG, not in `build()`. The shipped copy has `USE_INTRO = True`, set up for the hammer ad's smash clip and its unconfirmed "Bonus cash!" hook: for an ad without a remade hook set it to False, start the first BEAT at 0.00 and take SMASH / VO_INTRO out of INPUT_FILES and the index names. Replace the reference ad's "Bonus cash!", "cash bonus" and "Get an offer." lines. Render with `bash render_card_reel.sh`. It cuts every pause over 0.4 s to 0.3 s, puts small lead words and a big red keyword above the footage card, stamps and a progress bar; `USE_INTRO` splices a new hook. | `references/edit-pipeline.md`, `references/layout-and-style.md` |
| 6. QA | `scripts/qa_checks.sh`, then the three-lens Workflow `scripts/qa_workflow.js` (sync and sound, visuals, compliance) with adversarial verification. Fix what survives, re-render, re-check. | `references/qa-and-launch.md` |
| 7. Deliver | Final mp4 to `13_Generated/videos/` with a plain name; working files stay in `10_Video_Builds/<Ad_Name>/`. Say in a few lines what changed and what still blocks launch. | `references/qa-and-launch.md` section 3 |

All paths in this file (the table and the worked example) are inside `${CLAUDE_PROJECT_DIR}/01_Skills_and_SOPs/Flow_Animated_Story_Ads/` unless they start with a repo folder (`10_`, `11_`, `13_`).

## Rules that are easy to break

- No company name in voice, on screen or on the end card. End on "Ask for a cash offer. No obligation."
- Neutral verbs only: "the house sells as-is", never "we buy". Never numbers or $, "best price" or "top dollar", fake urgency or competitor names (registry Section 4: no confirmation unlocks them). No speed, "any condition", "guaranteed" offers or offer-for-everyone wording unless the registry lists it in Section 1.
- The clay homeowner is a story character, never a customer or a seller testimonial, and never the one saying company lines.
- Flag a team idea that fights the story the moment you see it (the hammer ad's money burst versus "put the hammer down").
- Nothing launches while the landing page is broken, a claim waits for the owner, or a voice or sound licence is missing.

Worked example: `references/examples/claymation-hammer.md` (its bonus-cash hook is not reusable as written; the example says why).
