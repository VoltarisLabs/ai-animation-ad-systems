---
name: gta-style
description: Make a game-look ("GTA style") story video ad for the cash home buying business, painted like an open-world game loading-screen poster, built shot by shot in Google Flow (Veo 3.1 clips, Nano Banana Pro images) with an ElevenLabs narrator and a local ffmpeg edit that adds a game HUD (minimap, meters, toasts, objectives, NEW MISSION, MISSION COMPLETE, end card). Use when someone types /gta-style or asks for a GTA-style or game-style ad, script options for one, its Flow prompts, its edit or a fix to a cut.
argument-hint: "[idea, team brief or finished script (optional)]"
---

# /gta-style: game-look story ad

Request typed after the command: $ARGUMENTS

If nothing was typed, ask for the idea in one line, or offer three script options.

This command is the game-look front door to the shared pipeline skill in `${CLAUDE_PROJECT_DIR}/01_Skills_and_SOPs/Flow_Animated_Story_Ads/` (repo path `01_Skills_and_SOPs/Flow_Animated_Story_Ads/`). Read its `SKILL.md` first and follow it, making the game-look choices below at each stage. The look and edit choices here win over the shared defaults; the claims rules in the shared skill always win over everything.

"GTA style" is the team's shorthand for the look. Never put a game name, logo, lookalike logo font, real game character, police, weapons or crime in a prompt or in the ad; describe the look in generic words.

## How to work with the person

Short, plain answers, one step at a time. Give one paste-ready prompt, wait for "done" / "clip added", check the clip, then give the next. The person runs Flow and ElevenLabs; you write every prompt and do the edit and QA locally. Never spend generation credits yourself.

## The game-look choices

| Stage | What to do | Read |
|---|---|---|
| 1. Script | Re-read `11_Psychological_Hooks/claims-registry.md` today. Nested loop (Open A, B, C, Main, Close C, B, A, Ask), 70-85 spoken words for 30-35 s (Stress Meter: 76 words, 34 s; Stop the Drain: 78 words, 33 s); the HUD builder stretches pauses, it does not cut them. Carry the terms with one game device (a meter that drains or maxes out, a mission, a pause, a fail-and-retry, map waypoints). A team brief or finished script is written or kept as asked in the script file, with every unconfirmed line marked NOT CLEARED and a safe swap beside it. The registry blocks production of a script that holds an unconfirmed claim, so voice, clips and HUD text use the swaps until the owner clears each line; if the team still wants its own wording recorded, label that cut a draft that cannot launch. Options: a judge panel, top 3 as a table (Part / Narrator says / What we see). Every script and option passes the sell-the-destination check (`11_Psychological_Hooks/sell-the-destination.md`): mechanism in one line, 1-3 path beats, life after as the payoff, next chapter as the last shot, tag split shown. | `references/script-and-claims.md` |
| 2. Look | Character sheet and house as Nano Banana Pro images first, then attach them to clips. Style words: "open-world video game loading-screen poster art style: semi-realistic digital painting, bold black ink outlines, cel-shaded color blocks, dramatic lighting, saturated colors. Not 3D, not photoreal." A rugged, confident character reads as a game character; a flat cartoon does not. Add "must not resemble any real person" when a face starts to look like someone famous. | `references/flow-prompting.md` section 1 |
| 3. Clips | One action per clip, starting mid-action, "single shot, no cuts", mouth closed and no dialogue, no text or numbers. When Ingredients to Video loses the face or the house, edit an approved frame in Nano Banana Pro ("keep everything else exactly the same, change only...") and animate it with Frames to Video. Check every clip's first second for a face that morphs, any silent mouthing, and objects that come back after vanishing. | `references/flow-prompting.md` sections 2, 3, 6 and 7 |
| 4. Voice | One narrator file for the whole script. An original voice, or a clone only with the speaker's written consent naming the ad. Game sound effects only with a written licence listing each cue (a mission jingle is music); otherwise the synthesized set from `scripts/make_synth_sfx.sh`. Write `PERMISSIONS.md` next to the ad. | `references/voice-and-audio-rights.md` |
| 5. Edit | The HUD builder: copy `scripts/build_hud_ad.py` and `scripts/render_hud_ad.sh` into `10_Video_Builds/<Ad_Name>/` beside `src/` and `work/`. Make word times with `scripts/words.py`, set the CONFIG block and shot plan, rewrite every HUD, text and sound event in `build()`, render. Use the techniques from the second game-look ad: sub-pixel push-ins, still-to-clip zoom groups, cross-faded joins, partial slow motion, minimap above the captions, a dip to black for time skips. | `references/edit-pipeline.md` sections 1-8, `references/layout-and-style.md` |
| 6. QA | `scripts/qa_checks.sh`, then the three-lens Workflow `scripts/qa_workflow.js` with adversarial verification, then a re-check of the fixed render (fixes can cause side effects). | `references/qa-and-launch.md` |
| 7. Deliver | Final mp4 to `13_Generated/videos/` with a plain name; working files stay in `10_Video_Builds/<Ad_Name>/`. Say in a few lines what changed and what still blocks launch. | `references/qa-and-launch.md` section 3 |

All paths in this file (the table and the worked examples) are inside `${CLAUDE_PROJECT_DIR}/01_Skills_and_SOPs/Flow_Animated_Story_Ads/` unless they start with a repo folder (`10_`, `11_`, `13_`).

## HUD that works, and HUD that doesn't

- Works: a round minimap top-left; one meter with a plain label that makes no money or value claim (STRESS stars, or a segmented bar; the HOME VALUE label in Stop the Drain was flagged and waits for the owner); toasts that slide in from the right; an objective line; NEW MISSION and MISSION COMPLETE banners in amber; a comic freeze frame with a name card (RAY / HOMEOWNER); a NEW OBJECTIVE end card; a PAUSED title over a dimmed, desaturated frame.
- Doesn't: menu options or buttons (RESUME / MAP / SETTINGS read as tappable features that do nothing, which Meta rejects); a bare row of stars (reads as a rating); digits, prices or counters; a meter label that implies a value or equity claim (HOME VALUE, EQUITY); WASTED, arrest or police screens; anything over a face.

## Rules that are easy to break

- No company name in voice, on screen or on the end card. End on "Ask for a cash offer. No obligation."
- Neutral verbs only: "the house sells as-is", never "we buy". Never numbers or $, "best price" or "top dollar", fake urgency or competitor names (registry Section 4: no confirmation unlocks them). No speed, "any condition", "guaranteed" offers, "best way" or offer-for-everyone wording unless the registry lists it in Section 1. News hooks (rates, inflation, wars) carry no figure ("Rates jumped"), need a dated source for what they say, and can send the ad to Meta's social-issue review: flag them.
- The homeowner is a story character, never a customer or a seller testimonial, and never the one saying company lines.
- Nothing launches while the landing page is broken, a claim waits for the owner, or a voice or sound licence is missing.

Worked examples: `references/examples/gta-stress-meter.md` and `references/examples/gta-stop-the-drain.md`.
