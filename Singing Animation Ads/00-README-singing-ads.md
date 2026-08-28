# AI Animation — Singing / Song-Style Ads

**Prompt:** `song-style-ad-generator-PROMPT.txt` (Ad Creators Lab, saved 2026-08-29)
**Slash command:** `/singing` (installed at `.claude/skills/singing/`)
**Lessons:**
- `01-sop-song-style-ad-scripts.md` — 10-step SOP for generating the script
- `02-suno-music-generation.md` — lyrics → finished track in Suno

> This is the **singing framework** referenced in the Crochet course — the Hall of Fame reference ad is **crochet + singing combined.** See "Pairing with crochet" below.

---

## What this format is

Short ads that **play like micro music videos.** Animated objects, Pixar-style visuals, or stylized characters deliver the product story through **original music**.

Output: **Suno-ready lyrics** + a **Suno style prompt** + **visual direction**.

---

## The 4-step flow (wait for a reply at each step)

| Step | What happens |
|---|---|
| **1 — Collect inputs** | Brand research (any format) + **website URL required minimum**. Confirms the brand in 1 sentence, notes 2-3 things pulled that will inform the song. |
| **2 — Song style** | Genre + duration (15s / 30s / 60s). Say "help me pick" → asks target market → suggests 2-3 genres from the built-in map. |
| **3 — Angle + awareness stage** | Proposes ONE angle + ONE awareness stage, asks to confirm. |
| **4 — Output** | 2-3 **distinct** song scripts: concept, lyrics, Suno style prompt, visual idea. |

**Hard rule:** if the user has no research, the website is required. Neither → stop and ask again.

---

## Built-in genre map (demographic → genre)

| Demographic | Genres |
|---|---|
| Moms (general) | Pop, indie pop, light acoustic |
| Moms (Gen X / 40+) | Country, soft pop, throwback pop |
| Gen Z women | Pop, hyperpop, R&B, indie pop |
| Gen Z men | Hip-hop, trap, EDM, indie rock |
| Millennial women | Pop, indie pop, R&B, alt-pop |
| Millennial men | Indie rock, hip-hop, alt-rock |
| Black men (general) | Hip-hop, R&B, trap, neo-soul |
| Black women (general) | R&B, hip-hop, neo-soul, pop |
| Latino/Latina market | Reggaeton, Latin pop, bachata, trap latino |
| **Tech / SaaS audience** | **EDM, lo-fi, indie rock, electro-pop** |
| Fitness enthusiasts | Hip-hop, EDM, hard rock, trap |
| Outdoor adventurers | Folk, indie folk, alt-rock, americana |
| **Luxury buyers** | **Ambient, modern jazz, cinematic pop** |
| Pet owners | Folk, indie pop, country |
| Skincare / beauty | Pop, R&B, indie pop, hyperpop |
| Gamers | EDM, synthwave, hyperpop, dubstep |
| Boomers (60+) | Country, classic rock, soft pop, throwback |
| Wellness / spiritual | Ambient, indie folk, soft acoustic |
| **Trades / blue-collar** | **Country, classic rock, southern rock** |
| Foodies / chefs | Indie pop, jazz-pop, acoustic |

No exact match → closest fit, and explain why.

---

## Awareness stages (pick ONE)

| Stage | Customer's relationship to the problem |
|---|---|
| Unaware | Doesn't know the problem exists |
| Problem-aware | Feels the pain, doesn't know solutions exist |
| Solution-aware | Knows solutions, doesn't know this product |
| Product-aware | Knows the product, hasn't bought |
| Most-aware | Already a fan / loyal |

---

## Angle formats (customer outcome, never a feature)

- **"Stops [pain point]"** → *"Stops you from snapping at your kids"*
- **"[Desired state] without [common objection]"** → *"Builds muscle without spending hours at the gym"*
- **"[Product] does what [alternative] can't"** → *"Filters water your Brita can't touch"*

---

## The 10 lyric + script rules

1. **Hook in the first 5 seconds** — whatever the duration
2. **Lyrics communicate the ANGLE, not the brand.** Don't chant the product name, tell the customer outcome
3. **Sound like a real song, not a jingle.** Real verses, choruses, rhyme schemes. Not "buy buy buy"
4. **Short singable lines — 4-8 syllables** for pop hooks. Longer feels forced when sung
5. **Match vocabulary + energy to genre + demo.** Hip-hop ≠ country ≠ pop. Stay genre-authentic
6. **Chorus repeats scale with duration:** 15s = hook + one chorus · 30s = verse-chorus-verse-chorus · 60s = full song
7. **Suno style prompt stays tight** — genre, vocal style, BPM, mood, production style. **Under 25 words.** Suno does better with concise style prompts
8. **Visual idea must be PRODUCIBLE** — animated objects, stylized characters, simple Pixar-feel. No "live action cinematic crane shots"
9. **Never use:** "cinematic," "professional voiceover," "stunning," "breathtaking," generic hype words
10. **The 2-3 options must be meaningfully different** — different POV, mood, or structural hook. No near-duplicates

---

## Output structure per option

```
OPTION [N]: "[Hook line / song title]"

THE CONCEPT          1-2 sentences — vibe + visual treatment
LYRICS               [Verse 1] [Chorus] [Verse 2 — 30s+] [Chorus] [Bridge — 60s only]
SUNO STYLE PROMPT    genre, vocal style, BPM, mood, production style — under 25 words
VISUAL IDEA          2-3 sentences, referencing specific lyric moments
```

---

## 🔗 Pairing with crochet (the Hall of Fame ad)

The reference ad runs **both frameworks together**. The division of labour:

| Framework | Owns |
|---|---|
| **`/singing`** | Script, lyrics, genre, angle, awareness stage, Suno music generation |
| **`/crochet`** | Every visual — diorama framing, character consistency, start/end frames, I2V prompts |

**Suggested combined workflow:**
1. `/singing` → lock genre + angle + awareness → get lyrics + Suno style prompt
2. Generate the track in **Suno** (external tool, not KIE)
3. Take the **lyrics as the script** into `/crochet` → phrase-by-phrase breakdown (the lyric lines ARE the phrases)
4. `/crochet` Step 2 → storyboard frames + I2V prompts
5. Generate images + clips, cut to the Suno track's beat

**The clean fit:** singing's "VISUAL IDEA" field explicitly suggests *"animated character, pixel object, claymation-style visuals"* — crochet's knitted stop-motion diorama is exactly that lane, just a more distinctive one.

**Watch out:** timing changes. In a song ad the **music sets the cut points**, not a voiceover line list. Clips must land on the beat, so lock the Suno track **before** generating any video — clip lengths come from the music.

---

## Tools

| Purpose | Tool | Status |
|---|---|---|
| Lyrics + style prompt | `/singing` | ✅ free |
| **Music generation** | **Suno Pro** | ⚠️ **external, not KIE — separate subscription, not yet set up.** Course strongly recommends Pro over free: best model + 2,500 credits vs ~50. See `02-suno-music-generation.md` |
| Images | Nano Banana Pro (KIE) | ✅ ~$0.09 |
| Video | Seedance 2.0 (KIE) | ✅ $0.205/sec |
| Assembly | Premiere / ffmpeg | ✅ free |

🚨 **No API call without Rafiul's explicit typed approval.**

---

## Altura fit

Per the genre map, Altura's audience (business owners seeking funding) sits closest to **Tech / SaaS** → EDM, lo-fi, indie rock, electro-pop. Or **Trades / blue-collar** → country, classic rock, if targeting contractors and service businesses specifically.

Awareness stage from our research doc: **Level 4-5 market sophistication**, and the ICP already knows funding options exist and has usually been burned by MCAs. That reads as **Solution-aware** — knows solutions, doesn't know Altura.

Candidate angle in the prompt's own format:
> *"Capital without the hard inquiry"* — `[Desired state] without [common objection]`

That maps directly onto the client's approved Script 04 mechanism and needs no new claims.

**Honest read on fit:** a song ad for B2B business funding is a bigger swing than for consumer products. It could be a strong pattern interrupt in a feed full of serious finance ads, or it could undercut the credibility a funding brokerage needs. Worth testing as a diversification creative, not as the primary.
