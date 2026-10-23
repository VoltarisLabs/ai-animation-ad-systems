---
name: remake
description: Watch a video from Instagram, X/Twitter, TikTok, YouTube (or a local file) and explain how to remake it — downloads it, pulls timestamped frames, has Gemini watch it with audio, then gives a shot-by-shot breakdown and a remake recipe in the Ad engine pipeline (image prompts, Seedance I2V prompts, voice, music, costs). Trigger on "/remake <url>", "remake this", "how do I recreate this", "break down this video", "watch this reel/tweet/tiktok", or when the user pastes an instagram.com/reel, x.com/.../status, tiktok.com or youtube.com/shorts link and wants to copy the style.
---

# Remake

The user gives a link (or a file path). You download it, actually look at it, and tell them how to make their own version.

## Step 1: Run the watcher

```bash
python3 "<this skill's base directory>/scripts/watch.py" "<url or file path>"
# installed per user: python3 ~/.claude/skills/remake/scripts/watch.py "<url>"
```

Needs `yt-dlp`, `pip install requests pillow imageio-ffmpeg`, and `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) in the environment, `~/.env` or `./.env`. Optional: `OPENAI_API_KEY` for a Whisper transcript, `APIFY_API_TOKEN` as the Instagram fallback.

Takes 30-90s. Costs about 3-10 cents of Gemini per video (analysis only, no generation), so just run it. It writes to `$REMAKE_DIR/<platform>-<id>/` (default `~/Documents/Ad engine/references/remakes/` when the Ad engine is on the machine, else `./remakes/`):

| File | What it is |
|---|---|
| `breakdown.md` | Caption, author, stats, specs, cut list, Gemini's timestamped watch-through (format, transcript, hook, shot list, characters, audio, edit style, script beats, why it works, remake difficulty) |
| `hook.png` | 8 timestamped frames across the first 3 seconds |
| `sheet.png` | One timestamped frame per shot (or evenly sampled if it is one continuous take) |
| `frames/` | 720px frame per shot and per hook moment, named by timestamp |
| `video.mp4` | The source. Reuse it as the motion-transfer reference |

Posts with several videos get one `part-N/` folder each. Re-running the same link reuses the download and the analysis for free. `--force` redoes everything.

If the download fails: private or login-walled posts → retry with `--cookies-from-browser chrome`; still failing → ask the user to save the video and give you the file path. Image-only carousels have no video to remake.

## Step 2: Look at it yourself

Gemini watches the motion and hears the audio, but it misses and invents details. The frames are ground truth.

1. Read `breakdown.md`.
2. Read `hook.png` and `sheet.png` with the Read tool. Open individual `frames/` files for any shot you will write a prompt for, or where Gemini's description looks off.
3. Where the frames and Gemini disagree, trust the frames and fix the breakdown in your answer. Small graphics, logos, flash frames and on-screen text are the usual misses.

Gemini's `## Transcript` section is the main transcript; Whisper is an optional extra. Gemini's content is usually right but its timestamps can drift on long videos. When `breakdown.md` shows a **Timeline drift** note, take all timing from the cut list and the frames.

## Step 3: Answer

Keep it tight. Don't paste the whole breakdown; the user can open it.

1. **What it is**: format, render look, runtime, number of shots, average shot length, post stats if any.
2. **Why it works**: the hook in the first second (what moves, what's said, what text shows), then 2-4 retention mechanics.
3. **Shot by shot**: table with time, what we see, camera, VO/dialogue, on-screen text.
4. **How to remake it**: pick the route below, then for each shot give:
   - the still: image prompt + model
   - the motion: I2V prompt in the Ad engine template (`[camera] [three events in the first second] [what stays still] [face to lens] [guards]`) + model + duration
   - what happens in the edit instead (captions, logos, UI, title cards, transitions, music)
   - voice and music plan

   Group repeated shot types (40 interview shots are one template with variations, not 40 prompts). Don't generate shots that stay on screen under ~1s: use the still with a push-in in the edit. Generated clips have a 4s minimum, so a 0.5s shot wastes 3.5s of paid video.
5. **Cost to rebuild**: stills × per-image price + clips × seconds × per-second price, using the Ad engine cost table. Say it's an estimate.
6. **The script for their offer**: if the user named a product, rewrite the script for it: open on the landscape with fear (`11_Psychological_Hooks/sell-fear.md`: 1-3 sourced facts with source cards, the fear on one third-person character), and tag each line PAIN / PLANE / PATH / DESTINATION (cold: PAIN 40-50%, PLANE ≤ 10%, PATH ≥ 20%, DESTINATION ≥ 25%). If they didn't, finish by asking what product or offer the remake should sell.

### Pick the route

| The source looks like | Remake with |
|---|---|
| Handmade clay / stop-motion | `/claymation` skill |
| Knitted, yarn, crochet characters | `/crochet` (`crochet-ad-visuals`) skill |
| 3D cartoon skeleton, "Day 1… Day 30…" progression | `/skeleton` (`skeleton-ads`) skill |
| Characters or objects singing, music-video ad | `/singing` skill |
| Real person talking to camera (UGC) | `/seedance-20-ugc-ad-director`; Veo 3.1 when they need native spoken dialogue |
| Documentary or interview format: experts, survivors, customers answering on camera | Film real people for every face that claims a title or tells their own outcome. AI covers b-roll, silent reaction beats and title-card backgrounds. Or move the structure to stylised characters (clay, crochet) who give opinions, not credentials |
| A person's exact moves or dance you want to copy | Motion transfer (Ad engine Workflow 4) with `video.mp4` as the reference |
| Cinematic b-roll, product shots, montage | Per-shot stills → Seedance 2.0 I2V, following the playbook |
| Screen recordings, UI, charts, text slides | Don't generate them. Record the real screen or build it in the edit; generate only the human or character parts |

When a route skill exists, give the breakdown and route, then offer to start that skill with this breakdown as its input.

## Rules

- Before writing any image or I2V prompt, read the Ad engine playbook when it's on the machine: `~/Documents/Ad engine/references/docs/seedance-i2v-playbook.md` and `prompt-best-practices.md`, camera moves in `camera-moves-for-ai-video.md`, script craft in `ad-script-structure.md`.
- Never put a synthetic person on screen as a credentialed expert (name + "MD", "PhD") or as someone telling their own result ("given 6 months, still here 27 years later"). That's a fabricated endorsement: it breaks the FTC endorsement rules and Meta/TikTok ad policy. Real people for those beats, always.
- Never call a generation endpoint (image, video, voice, music) from this skill without showing the exact cost and getting a yes. The Ad engine cost rule applies.
- AI can't render small legible text, real UI, or brand logos reliably. Put them in the edit, and say so.
- Don't copy someone else's footage, voice or likeness into a new ad. The remake keeps the structure, pacing and style, with new characters, a new script and the user's product. `video.mp4` is only for study and motion reference.
- The output folder is gitignored (`references/remakes/`). Leave the files there for later rounds.
