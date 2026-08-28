# AI Animation Ad Systems

Production frameworks for AI-generated animated video ads. Five formats, each with its skill/prompt, the course lessons, and notes on running it on our own stack (KIE.ai + ElevenLabs + ffmpeg).

**Private repo — contains verbatim Ad Creators Lab course material. Do not make public.**

---

## The five formats

| Folder | Format | Slash command | Status |
|---|---|---|---|
| [🔥NEW🔥 Skeleton Ads](./🔥NEW🔥%20Skeleton%20Ads) | 3D cartoon skeleton, narrated escalating journey | `/skeleton` | ✅ complete |
| [Crochet Style Ads](./Crochet%20Style%20Ads) | Knitted stop-motion diorama | `/crochet` | ✅ complete |
| [Singing Animation Ads](./Singing%20Animation%20Ads) | Song-style micro music video | `/singing` | ✅ complete |
| [Claymation Ads](./Claymation%20Ads) | Clay stop-motion | — | ⚠️ GPT-hosted, see below |
| [Talking Objects Ad Style](./Talking%20Objects%20Ad%20Style) | The failed solution confesses its flaws | — | ⚠️ GPT-hosted |

Each folder starts with a `00-README` digest. Read that first.

---

## Picking a format

| | Skeleton | Crochet | Singing | Claymation | Talking Objects |
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
4. **Paste character blocks verbatim.** Paraphrasing breaks consistency — identical wording is what makes the model re-render the same character.
5. **Formats don't mix.** Crochet's negative prompt explicitly bans `claymation, clay texture`; the style blocks are mutually exclusive.
6. **Verify pronunciation of brand and product names** in any generated speech, before committing to video.
7. **Cheap model to test timing, better model for the final.** Every course lesson repeats this.

---

## Stack notes

The course teaches Max Fusion / Higgs Field. We run KIE.ai instead. Substitutions:

| Course tool | Ours | Cost |
|---|---|---|
| Seedream 4.5 / NanoBanana 2 | Nano Banana Pro | ~$0.09/image |
| Seedance 1.5 Pro | ⚠️ unverified on KIE | — |
| Seedance 2.0 | ✅ working — workhorse | $0.205/sec |
| Kling 2.6 / 3.0 | 🔴 500 Internal Error (2026-08-27) | — |
| Veo 3 Fast | ✅ working | ~$0.30 flat |
| ElevenLabs (via KIE) | 🔴 broken → use ElevenLabs direct API | — |
| Suno | external subscription, not set up | — |
| Assembly | ffmpeg / Premiere | free |

### Open blockers
1. **Kling down on KIE.** Claymation's continuous-flow mechanic depends on Kling 3.0's start/end frame feature. Check whether Seedance 2.0 exposes an end-frame parameter — that single answer decides whether claymation is fully producible here.
2. **No cheap test tier.** Every SOP assumes "test on the cheap model first." Verify `seedream-4.5` and `seedance-1.5-pro` on KIE.
3. **Two GPT-hosted formats.** Claymation and Talking Objects live in OpenAI custom GPTs whose instructions aren't extractable. Talking Objects' lesson contains enough to work without it; claymation needs the source document.

---

## Installing the skills

Three formats ship as skill files. Drop each into `.claude/skills/<name>/SKILL.md`:

```
.claude/skills/skeleton/SKILL.md   ← 🔥NEW🔥 Skeleton Ads/skeleton-ads-SKILL.md
.claude/skills/crochet/SKILL.md    ← Crochet Style Ads/crochet-ad-visuals-SKILL.md
.claude/skills/singing/SKILL.md    ← Singing Animation Ads/song-style-ad-generator-PROMPT.txt
```

The singing prompt ships without frontmatter — add a `name:` and `description:` block at the top before installing. Skill bodies should stay verbatim.

---

## Credit safety

Every model call costs real money. Nothing in this repo should be run against a paid API without explicit approval from the account owner. Cost estimates in each folder's README are per-run and exclude retries; budget ~30% headroom.
