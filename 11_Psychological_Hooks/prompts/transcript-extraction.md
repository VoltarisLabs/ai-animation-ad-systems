# Transcript Extraction Prompt

Use this prompt on any YouTube or podcast transcript. Save the output to `transcripts/<creator>-<video-slug>.md`.

```
Extract the following from this YouTube transcript:
1. Core Copywriting Frameworks/Formulas (e.g., PAS, AIDA, BAB).
2. Direct Actionable Rules (e.g., "Always put the primary benefit in the first 5 words of the headline").
3. Psychological Triggers Mentioned (e.g., Scarcity, Anchoring).
4. Concrete Examples or Teardowns.
Discard intro/outro banter, self-promotions, and filler words.

Output format:
- Title the file: "<Creator>: <Video title>"
- Add a source line: video URL + date published
- Use the 4 numbered sections above as headings
- Paraphrase; quote at most one short line per section
- If a claim cites a study or statistic, note whether the video gave a source
- Tag each trigger with the matching row in triggers-index.md, or mark it NEW
```

## Transcript sources
- YouTube's built-in transcript (the "Show transcript" button under the video description)
- `yt-dlp --write-auto-subs --skip-download <url>` for bulk downloads
