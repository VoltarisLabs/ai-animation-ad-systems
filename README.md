# AI Animation Ad Systems

The ad studio for AI-generated video and static ads: format SOPs, the copywriting playbook, ad scripts, audience research, characters and finished renders. The production stack is Kie.ai + ElevenLabs + ffmpeg.

> **Visibility check:** this repo is currently **public** on GitHub. An earlier version of this README said it holds verbatim Ad Creators Lab course material and must stay private. The owner should decide whether to make the repo private or remove that material.

---

## Start here

| If you want to... | Go to |
|---|---|
| **Get a great script in one shot** | [11_Psychological_Hooks/prompts/one-shot-script.md](./11_Psychological_Hooks/prompts/one-shot-script.md) + [research-cards.md](./11_Psychological_Hooks/research-cards.md) + [claims-registry.md](./11_Psychological_Hooks/claims-registry.md) |
| Write an ad that converts | [11_Psychological_Hooks/AD_COPY_CHECKLIST.md](./11_Psychological_Hooks/AD_COPY_CHECKLIST.md), then the [copywriting playbook](#copywriting-playbook) |
| Produce an animated ad | [01_Skills_and_SOPs/](./01_Skills_and_SOPs) (the `00-README` in each format folder) |
| Make a claymation or game-look ("GTA style") story ad | `/claymation` or `/gta-style` ([install them](#installing-the-skills)); the pipeline is in [Flow_Animated_Story_Ads](./01_Skills_and_SOPs/Flow_Animated_Story_Ads) |
| See scripts in progress | [03_Ad_Scripts_and_Briefs/](./03_Ad_Scripts_and_Briefs) |
| Understand the buyer | [04_Audience_Research/](./04_Audience_Research) |

## Repo map

| Folder | What lives here |
|---|---|
| [01_Skills_and_SOPs/](./01_Skills_and_SOPs) | One folder per ad format: skill or SOP, lessons and prompt files |
| [02_Prompt_Libraries/](./02_Prompt_Libraries) | Cross-format prompt banks |
| [03_Ad_Scripts_and_Briefs/](./03_Ad_Scripts_and_Briefs) | Finished and in-progress scripts, clip prompts, headline banks |
| [04_Audience_Research/](./04_Audience_Research) | Buyer avatars, hook map, market research |
| [05_Tutorials/](./05_Tutorials) | Hook psychology research report and cross-format tutorials |
| [06_Canva_Ad_Templates/](./06_Canva_Ad_Templates) | Numbered Canva template PDFs |
| [09_Characters/](./09_Characters) | Character sheet prompt template and the animated JMSN-3D character |
| [10_Video_Builds/](./10_Video_Builds) | Working files for each rendered ad |
| [11_Psychological_Hooks/](./11_Psychological_Hooks) | **The copywriting playbook** (see below) |
| [12_AI_Characters/](./12_AI_Characters) | Realistic UGC avatars: references, prompts, scripts |
| [13_Generated/](./13_Generated) | Every generated image and video |

`07_Assets/` and `08_Software/` stay local only (see `.gitignore`). Working rules for Claude live in [CLAUDE.md](./CLAUDE.md).

---

## The ad formats

| Folder | Format | Slash command | Status |
|---|---|---|---|
| [Skeleton_Ads](./01_Skills_and_SOPs/Skeleton_Ads) | 3D cartoon skeleton, narrated escalating journey | `/skeleton` | Complete |
| [Crochet_Ad_Visuals](./01_Skills_and_SOPs/Crochet_Ad_Visuals) | Knitted stop-motion diorama | `/crochet` | Complete |
| [Singing_Animation_Ads](./01_Skills_and_SOPs/Singing_Animation_Ads) | Song-style micro music video | `/singing` | Complete |
| [Claymation](./01_Skills_and_SOPs/Claymation) | Clay stop-motion | none (Flow route: `/claymation`) | GPT-hosted, see below |
| [Talking_Objects](./01_Skills_and_SOPs/Talking_Objects) | The failed solution confesses its flaws | none | GPT-hosted |
| [Seedance_UGC](./01_Skills_and_SOPs/Seedance_UGC) | Realistic AI UGC with Seedance 2.0 | skill file | Complete |
| [Flow_Animated_Story_Ads](./01_Skills_and_SOPs/Flow_Animated_Story_Ads) | Stylised story ads from Google Flow + a local ffmpeg edit: claymation (card-reel edit) or game look (HUD edit) | `/claymation`, `/gta-style` | Complete |

Most format folders start with a `00-README` digest; read that first. Two don't: Seedance_UGC (start with `Seedance_2_Skill_for_Poppy.txt`) and Flow_Animated_Story_Ads (start with its `SKILL.md`, or use `/claymation` / `/gta-style`).

---

## Picking a format

| | Skeleton | Crochet | Singing | Claymation (GPT SOP) | Talking Objects |
|---|---|---|---|---|---|
| **Core mechanic** | curiosity hook + escalating spine | phrase → 5 visual options | lyrics carry the angle | scene chaining | "I'm the failed solution" |
| **Consistency method** | Character Bible verbatim + hero ref | character ref + diorama framing | n/a | facial-consistency line + ref | one character, one take |
| **Frames per clip** | 1 | 1 or 2 (Type A/B/C) | n/a | 1 or 2 (chained) | 1 |
| **Clip length driver** | VO line length | phrase | music beat | audio section (3-5s→1, 6-9s→2) | script length |
| **Audio** | ElevenLabs VO | ElevenLabs VO | Suno track | ElevenLabs VO | native lipsync |
| **Relative cost** | medium | high (2-frame scenes) | high (+ Suno sub) | medium-high | **lowest** |
| **Best for** | viral reach | novelty pattern interrupt | scroll-stop + memorability | tactile charm | education + positioning |

**Audio-first rule:** four of the five generate audio *before* video, because audio determines clip count and length. Only talking objects generates speech inside the video.

---

## Rules that apply across every format

1. **Never invent style rules.** Each format's skill or SOP is the authority. Substituting your own model choices or prompt wording is what produces rejected work.
2. **No text in image or video prompts.** Captions are added in the editor, never baked into generated footage.
3. **Reference the hero image, never the previous image.** Referencing the previous shot compounds drift.
4. **Paste character blocks verbatim.** Paraphrasing breaks consistency: identical wording is what makes the model re-render the same character.
5. **Formats don't mix.** Crochet's negative prompt explicitly bans `claymation, clay texture`; the style blocks are mutually exclusive.
6. **Verify pronunciation of brand and product names** in any generated speech, before committing to video.
7. **Cheap model to test timing, better model for the final.** Every course lesson repeats this.

---

## Stack notes

The course teaches Max Fusion / Higgs Field. We run KIE.ai instead. Substitutions:

| Course tool | Ours | Cost |
|---|---|---|
| Seedream 4.5 / NanoBanana 2 | Nano Banana Pro | ~$0.09/image |
| Seedance 1.5 Pro | ⚠️ unverified on KIE | n/a |
| Seedance 2.0 | ✅ working, workhorse for its own formats (Seedance_UGC SOP, non-talking footage) | $0.205/sec |
| AI-UGC talking clips (no course tool) | working: `gemini-omni-video` (Kie Gemini Omni), the production route per CLAUDE.md; runner `12_AI_Characters/kie_omni.py` | 63-126 credits per 4-10 s clip at 720p/1080p (list) |
| Kling 2.6 / 3.0 | 🔴 500 Internal Error (2026-08-27) | n/a |
| Veo 3 Fast | ✅ working | ~$0.30 flat |
| ElevenLabs (via KIE) | 🔴 broken → use ElevenLabs direct API | n/a |
| Suno | external subscription, not set up | n/a |
| Assembly | ffmpeg / Premiere | free |

### Open blockers
1. **Kling down on KIE.** The GPT-hosted Claymation format's continuous-flow mechanic depends on Kling 3.0's start/end frame feature. Check whether Seedance 2.0 exposes an end-frame parameter: that single answer decides whether that format is fully producible here. (The Flow route, `/claymation`, does not need Kling.)
2. **No cheap test tier.** Every SOP assumes "test on the cheap model first." Verify `seedream-4.5` and `seedance-1.5-pro` on KIE.
3. **Two GPT-hosted formats.** Claymation and Talking Objects live in OpenAI custom GPTs whose instructions aren't extractable. Talking Objects' lesson contains enough to work without it; the GPT Claymation format needs the source document; the Flow route (`/claymation`) does not.

---

## Installing the skills

Five slash commands ship as skill files. Drop each into `.claude/skills/<name>/SKILL.md` (the folder name becomes the command):

```
.claude/skills/skeleton/SKILL.md    <- 01_Skills_and_SOPs/Skeleton_Ads/002-skeleton-ads.md
.claude/skills/crochet/SKILL.md     <- 01_Skills_and_SOPs/Crochet_Ad_Visuals/Skill.md
.claude/skills/singing/SKILL.md     <- 01_Skills_and_SOPs/Singing_Animation_Ads/song-style-ad-generator-PROMPT.txt
.claude/skills/claymation/SKILL.md  <- 01_Skills_and_SOPs/Flow_Animated_Story_Ads/slash_commands/claymation/SKILL.md
.claude/skills/gta-style/SKILL.md   <- 01_Skills_and_SOPs/Flow_Animated_Story_Ads/slash_commands/gta-style/SKILL.md
```

The singing prompt ships without frontmatter: add a `name:` and `description:` block at the top before installing. Skill bodies should stay verbatim.

`/claymation` and `/gta-style` are the two front doors to the Flow story-ad pipeline. Both read the shared skill in `01_Skills_and_SOPs/Flow_Animated_Story_Ads/` (its `SKILL.md`, `references/` and `scripts/`) straight from the repo, so copy only the two command folders, then start Claude Code from the repo root. From the repo root:

```bash
mkdir -p .claude/skills
cp -r 01_Skills_and_SOPs/Flow_Animated_Story_Ads/slash_commands/claymation .claude/skills/
cp -r 01_Skills_and_SOPs/Flow_Animated_Story_Ads/slash_commands/gta-style .claude/skills/
```

Then type `/claymation` or `/gta-style`, optionally followed by an idea, a team brief or a finished script (for example `/gta-style a homeowner stuck on a loading screen of repairs`). If Claude Code was already running when `.claude/skills/` was created, type `/reload-skills` (or restart Claude Code) and the commands will show in the `/` menu. `.claude/` is in `.gitignore`, so each person installs locally, and the copies don't update with the repo: after a `git pull` that changes `slash_commands/`, run the two `cp` lines again. The shared `SKILL.md`, `references/` and `scripts/` are read straight from the repo and need nothing.

---

## Credit safety

Every model call costs real money. Nothing in this repo should be run against a paid API without explicit approval from the account owner. Cost estimates in each folder's README are per-run and exclude retries; budget ~30% headroom.

---

## Copywriting Playbook

[11_Psychological_Hooks/](./11_Psychological_Hooks) is how we write ads that convert. It combines the classic direct-response canon (Ogilvy, Schwartz, Halbert, Sugarman, Hopkins, Caples), the psychology behind it (Cialdini, Kahneman and Tversky, Ariely, Fogg, Thaler), and full YouTube channel scans of **Stefan Georgi** and **Sabri Suby**: 671 videos read, with lessons paraphrased and sourced by video ID, plus Jeremy Haynes (single video, Meta 2027 rules).

**Use it in this order:**
1. [research-playbook.md](./11_Psychological_Hooks/research-playbook.md): get the market's exact words, their awareness level and the one desire to aim at.
2. [offer-and-mechanism.md](./11_Psychological_Hooks/offer-and-mechanism.md): why it works, an honest offer, the catch said first, the funnel shape.
3. [AD_COPY_CHECKLIST.md](./11_Psychological_Hooks/AD_COPY_CHECKLIST.md): the routine every script passes, using [hook-formulas.md](./11_Psychological_Hooks/hook-formulas.md) (70 hooks + 11 fascination types), [templates/](./11_Psychological_Hooks/templates) (13 video templates + statics) and [copy-banks.md](./11_Psychological_Hooks/copy-banks.md).
4. [testing-and-iteration.md](./11_Psychological_Hooks/testing-and-iteration.md): kill checks, test order, hook rate, funnel triage, the AI workflow.
5. [prompts/copy-prompts.md](./11_Psychological_Hooks/prompts/copy-prompts.md): ready-to-paste prompts for each step.

Only claims you can prove. No fake urgency or scarcity. The folder's [README](./11_Psychological_Hooks/README.md) has the full index.
