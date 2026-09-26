# Claymation — Voice Section

**Source:** Ad Creators Lab lesson
**Saved:** 2026-08-29
**Covers:** voiceover for claymation ads (ElevenLabs voice design)

---

## The 6 steps

### 1. Go to a voice generator
ElevenLabs → **voice design**

### 2. Create a voice
- Describe the voice: **age, tone, style**
- Keep it **calm, simple, not over-the-top**

### 3. Test the voice
- Generate a sample
- **Listen before adding enhancements**

### 4. Improve it
- Add enhancement if needed
- Make it sound **more natural, less robotic**

### 5. Add your script
- Paste the script
- Generate the full voiceover

### 6. Download
Save the audio, use it in the video.

---

## 🚨 The key rule

> **Don't make it too energetic.**
> **Best ads = calm, slightly serious, storytelling tone.**

- 👉 Sounds like a **YouTuber shouting** → **it's wrong**
- 👉 Sounds like a **documentary** → **you're close**

This is the single clearest voice direction across all four courses. It also matches the ElevenLabs lesson in the skeleton section (*"avoid a voice that sounds too polished"*) — both are pushing away from ad-read energy, just from different directions: skeleton wants casual-real, claymation wants calm-documentary.

---

## The 10 voice prompts (paste into ElevenLabs voice design)

| # | Style | Prompt |
|---|---|---|
| 1 | **Classic documentary** | *"Soft British male, mid-40s, calm and authoritative, documentary narration style, slow and measured delivery"* |
| 2 | **Older trusted expert** | *"Older British male, 60s, warm, calm, slightly gravelly voice, reassuring and knowledgeable tone"* |
| 3 | **Calm female narrator** | *"Soft British female, 30s, calm and clear, neutral tone, gentle and informative delivery"* |
| 4 | **Subtle luxury tone** | *"Refined British male, 40s, smooth and polished, understated confidence, premium brand feel"* |
| 5 | **Scientific explainer** | *"Neutral British voice, 30s, precise and clear, slightly analytical tone, calm and factual delivery"* |
| 6 | **Storytelling narrator** | *"Warm British male, 40s, relaxed pacing, slightly emotional but controlled, storytelling tone"* |
| 7 | **Modern minimal ad voice** | *"Young British male, late 20s, calm, slightly monotone, minimal expression, clean ad style"* |
| 8 | **Soft persuasive female** | *"British female, 30s, soft and reassuring, slightly warm tone, persuasive but subtle delivery"* |
| 9 | **Serious problem-solution** | *"British male, 40s, serious and grounded, calm but slightly concerned tone, clear emphasis on key words"* |
| 10 | **High-end brand voice** | *"Deep British male, 40s, slow, confident, luxurious tone, very controlled delivery, premium feel"* |

**Pattern to notice:** every one is British, and every one is calm. The formula is consistent:
```
[nationality/gender] [age] [2-3 tone adjectives] [delivery pacing]
```

---

## Picking for Altura

Our ICP is US business owners who have usually been burned by MCAs and are wary of funding pitches. Our research doc puts them at **Level 4-5 market sophistication** — they have heard every aggressive funding ad already.

**Best fits from the list:**

| # | Why |
|---|---|
| **9 — Serious problem-solution** | *"calm but slightly concerned tone, clear emphasis on key words"* — this is the closest match to our 8-stage objection stack. Concerned, not hyped. |
| **2 — Older trusted expert** | Funding is a trust purchase. A 60s reassuring voice reads as an advisor, not a salesperson. |
| **1 — Classic documentary** | Safe default, matches the "if it sounds like a documentary you're close" rule exactly. |

**One adjustment to consider:** all 10 prompts specify **British**. For a US business-funding audience a British narrator may read as premium/documentary — or as foreign and off-key for a domestic financial services pitch. Worth generating one British and one American version of the same prompt and comparing before committing.

**Pronunciation checks still apply:** Altura (*al-TOO-rah*), APR, 0%, pre-qualification, hard inquiry. Same as noted in the skeleton and singing lessons.

---

## Audio-first ordering

This is the third format that generates audio **before** video:

| Format | Audio timing | Why |
|---|---|---|
| Skeleton | VO first, parallel with images | clip length = VO line length |
| Singing | Suno track first | music sets cut points |
| **Claymation** | **VO first** | **audio section length decides clip count (3-5s → 1 clip, 6-9s → 2 clips)** |
| Seedance UGC | speech generated inside the video | native lipsync, no separate VO |

**Practical consequence:** generate the voiceover before spending any video credits. It costs almost nothing, it catches pronunciation problems early, and in claymation it is literally the input that determines how many clips you need to buy.

---

## Our path

KIE's ElevenLabs wrapper is broken (500s, tested 2026-08-25). Use the **direct ElevenLabs API**:
```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
header: xi-api-key: <key>
```
Key in memory `elevenlabs-api-key.md`.

**Note:** these 10 prompts are for **voice design** (creating a custom voice), which is a different ElevenLabs feature than picking a stock voice. Voice design may need to be done in the ElevenLabs web UI rather than via the TTS endpoint — the API call above generates speech from an existing voice_id, it does not create one.

🚨 **No API call without Rafiul's explicit typed approval.**
