---
name: flow-animated-story-ads
description: End-to-end pipeline for Property Abundance animated story video ads (claymation, GTA-style game look, or any stylised 9:16 story ad) made with Google Flow (Veo 3.1 clips, Nano Banana Pro images) and ElevenLabs voice, then edited locally with ffmpeg + ASS into a finished Reel/TikTok/Short. Covers the nested-loop script checked against the claims registry, reference images, paste-ready Flow prompts, clip review, voice settings, the Python edit builders (pause tightening, frame-exact cuts, game HUD, captions, sound effects, loudness), multi-agent QA and the launch gate. Use this whenever someone wants to make, script, prompt, edit, re-edit, fix or QA an animated/claymation/GTA-style/cartoon video ad for the cash home buying business, asks for Flow or Veo prompts for an ad, says a cut has "dead space", wants a hook remade, wants captions/HUD/stars/mission banners, or wants to turn downloaded Flow clips into a finished ad, even if they don't say "skill" or name the pipeline.
---

# Flow animated story ads

Turn an ad idea into a finished 30-45 s vertical ad: script, then reference images, then Flow clips, then voice, then a local edit, then QA. The person runs Flow and ElevenLabs themselves; Claude writes every prompt and does the whole edit and QA locally. The same pipeline made the claymation "Put the hammer down" ad and the GTA-style "Stress Meter" and "Stop the Drain" ads.

Two slash commands start it in a given look: `/claymation` (clay stop-motion, card-reel edit) and `/gta-style` (game loading-screen look, HUD edit). Their skill files are in `slash_commands/`; the repo README shows how to install them. Each one reads this file and these references.

Read the parts you need:

| Stage | Read |
|---|---|
| Script, hook, claims | `references/script-and-claims.md` |
| Reference images and Flow/Veo prompts | `references/flow-prompting.md` |
| Voice (ElevenLabs), cloning, licensed audio | `references/voice-and-audio-rights.md` |
| The edit: builders, timing, HUD, sound, loudness | `references/edit-pipeline.md` |
| Screen layout, fonts, colours, caption styles | `references/layout-and-style.md` |
| QA and launch gate | `references/qa-and-launch.md` |
| Things that went wrong and the fix | `references/lessons-learned.md` |
| Worked examples | `references/examples/gta-stress-meter.md`, `references/examples/gta-stop-the-drain.md`, `references/examples/claymation-hammer.md` |

## How to work with the person

- Short, plain answers, one step at a time. Give the next Flow prompt, wait for "done" / "clip added", check it, then give the next. People lose track when handed ten prompts at once.
- Every prompt is complete and paste-ready (no "same as above", no "edit your last prompt"). Say which images to attach as ingredients and which Flow mode (Ingredients to Video, Frames to Video, Nano Banana Pro image) and the aspect ratio.
- Never spend generation credits yourself (Kie, APIs) without the person saying "generate" in their own words. Flow and ElevenLabs are run by the person.
- New clips land in the person's downloads folder; copy each into the ad's `src/` folder with a short name (`c1_splash.mp4`, `s2_table.jpg`, `vo.mp3`) before using it.
- After each clip arrives, look at it (contact sheet + transcript, see `scripts/contact_sheet.sh`, `scripts/words.py`) and tell the person in one or two lines what works and which seconds you will use. Flag problems immediately, while a re-roll is cheap.
- When an idea from the team conflicts with the story or the claims rules, say so the moment you see it. In the hammer ad the team wanted "money bursting from the wall" while the line was "put the hammer down"; not flagging that early cost a round of clips.

## The pipeline

1. **Script.** Re-read `11_Psychological_Hooks/claims-registry.md` (it changes; never work from memory). Write the nested loop: Open A, Open B, Open C, Main, Close C, Close B, Close A, Ask. Hook = face + motion + surprise in the first second, one named situation, no hype. For options, run a judge panel (several angles, each checked against the registry, one judge picks the top 3) and present them as a table: Part | Narrator says | What we see. Then pass `11_Psychological_Hooks/AD_COPY_CHECKLIST.md`, including the sell-the-destination check (`11_Psychological_Hooks/sell-the-destination.md`: mechanism in one line, 1-3 path beats, life after as the payoff, next chapter as the last shot; show the PAIN / PLANE / PATH / DESTINATION split with every option). The registry wins on any conflict. Details: `references/script-and-claims.md`.
2. **Look.** Make the character sheet and the setting (house) as Nano Banana Pro images first, get the person's OK, save them to `refs/`. Every clip then takes them as ingredients so the character and house stay the same. A new ad in an existing look reuses that ad's approved refs (ask the person for their copies; they are not in this skill).
3. **Clips.** One Veo 3.1 prompt per shot, given one at a time. One action per clip, starting mid-action, "single shot, no cuts", "He does not speak. No dialogue, no voice, no music" plus the sounds wanted, "No text, letters, numbers, logos". Stills (Nano Banana) for held beats and the end card. Details and the hazard list: `references/flow-prompting.md`.
4. **Voice.** ElevenLabs, one file for the whole script. Record after the script is final. Check the transcript word for word. A cloned voice only with the speaker's own written consent; third-party sound effects only with a written licence, otherwise the synthesized ones (`scripts/make_synth_sfx.sh`). See `references/voice-and-audio-rights.md`.
5. **Edit.** Copy a builder and its `render_*.sh` (card reel: also `make_card_assets.py`) into the ad folder itself, beside `src/` and `work/`, keeping their names. Make word times first: `mkdir -p work && python <skill>/scripts/words.py src/vo.mp3 work/vo_words.json`. Set INPUT_FILES, PHRASES, the pause settings and the shot plan, then rewrite every text, HUD and sound event in `build()`: they are written for the reference ad's phrase numbers and wording. Render with `bash render_*.sh`. The builders do pause tightening (or stretching), frame-exact cuts anchored to the voice, stills push-ins, a comic freeze frame, all on-screen text and HUD in one ASS file, clip ambience, sound effects aligned to their attack, and loudness to -14 LUFS. Details: `references/edit-pipeline.md`.
6. **QA.** Automated checks (`bash scripts/qa_checks.sh out/ad.mp4 work/script.txt`), then a three-lens review with adversarial verification (`scripts/qa_workflow.js`): sync and audio masking, visuals and safe zones, compliance. Fix what survives verification, re-render, re-check. Details: `references/qa-and-launch.md`.
7. **Deliver.** Copy the final mp4 to `13_Generated/videos/` with a plain name (`GTA_StressMeter_34s.mp4`); working files stay in `10_Video_Builds/<Ad_Name>/`. Send it, and list in plain words what changed and what still blocks launch (claims needing owner OK, broken landing page, permissions, music).

## Rules that are easy to break

- **Claims registry first.** Only Section 1 claims, in approved or narrower wording, with neutral verbs ("the house sells as-is", never "we buy"). Nothing unconfirmed (bonus cash, speed, "any condition", "we show you the math", an offer for everyone). No numbers or $ on screen or in voice. No "best deal", "best price", "top dollar". No "you are / you have" + a personal attribute. Why: these are FTC and Meta housing-ad (Special Ad Category) risks and the owner has not confirmed them.
- **No company name** in voice, on screen or in end cards (the page name already shows above the ad). End on the offer: "Ask for a cash offer. No obligation."
- **Characters are stories, not testimonials.** A made-up homeowner never speaks as a customer, is never called a customer or "sold", and no handshake/deal-papers scene runs while the buyer-identity claim is frozen. The narrator is the company's voice, never the character's inner voice.
- **Styles, not brands.** Describe a look in generic words (open-world game loading-screen poster art, semi-realistic painting, bold ink outlines, cel shading). Don't name a game in prompts or in the ad, and never show a game name, logo, lookalike logo font, real characters, weapons, police or crime. The team may call the look "GTA style"; that is shorthand, not prompt text.
- **Launch gate.** Nothing launches while the landing page is broken (registry Section 6), while a claim waits for the owner, or while voice/SFX permissions are not on file. Say this at every delivery, briefly.
