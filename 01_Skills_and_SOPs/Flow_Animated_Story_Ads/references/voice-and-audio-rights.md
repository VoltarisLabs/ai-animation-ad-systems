# Voice and audio rights

## ElevenLabs settings that worked

| Use | Voice / model | Settings |
|---|---|---|
| Warm narrator (claymation ads) | "Brian" (library voice), Multilingual v2 | Speed 0.92, Stability 44, Similarity 46, Style 27 |
| Excited hook line only | same voice and model so it matches | Stability 25, Style exaggeration 60, Speed 1.05, Similarity unchanged; make 3 takes |
| Punchier game-style read (the earlier 43 s version of the game-look ad) | same | Speed 1.0, Stability 40, Style 35 |

The file name ElevenLabs gives encodes the settings (`sp92_s44_sb46_se27` = speed 0.92, stability 44, similarity 46, style 27). Read it to check whether the person actually changed the settings.

Record the whole script in one file. Swapping just one line (like the excited intro) works if the same voice and model are used; match its loudness to the rest (the excited re-read came in about 10 LU hotter and was turned down to about 2 LU above the rest).

Always transcribe the file (`scripts/words.py`) and compare it with the script word for word. Whisper sometimes drops a quiet first word ("Ask for a cash offer" read as "For a cash offer"); check with word timestamps on the tail before asking for a re-record.

## Cloned voices and third-party audio

- Cloning a real person's voice for a paid ad needs that person's written consent. Soundalike voices in ads have lost in US courts (Midler v. Ford, Waits v. Frito-Lay), ElevenLabs requires the speaker's consent, and platforms and rights holders can take the ad down.
- The clean route with a consenting speaker: he records the script himself, or records at least 30 minutes of clean speech (ElevenLabs recommends 2-3 hours) for a Professional Voice Clone and completes its voice verification. An Instant Voice Clone needs only 1-3 minutes but has no speaker verification, so file his written consent either way. If he is known for a game or film character, his consent covers his voice, not the character: no character name, persona or catchphrases, and don't pair his voice with that game's look or sounds without the publisher's written licence. Recordings of a character ripped from a game or YouTube belong to the publisher, not the actor; the actor's signature does not cover them.
- An original designed voice is fine: ElevenLabs Voice Design ("a warm, relaxed male narrator, smooth low voice, unhurried, clean studio recording") or a Voice Library voice licensed for commercial use. Don't aim a designed voice at a specific real person or character: details that together point at one known voice (age + city + background + delivery) make it a soundalike.
- Game sound effects (mission jingles, notifications, pickups) belong to the publisher; soundboard download sites are not a licence source. Use them only with a written licence; otherwise use the synthesized set (`scripts/make_synth_sfx.sh`).
- When the team says it has permission, you may build a draft with those files, but mark it not for launch and write a `PERMISSIONS.md` next to the ad listing exactly which voice and sound files are used and what written consent or licence must be filed. Anything that will run uses synthesized effects or an original voice until that proof is filed. Downloading any file needs a clear yes after stating file name, source and size.

## Music

No licensed music is added in the edit. Tell the person to add a track from the Meta Sound Collection or the TikTok Commercial Music Library at upload (retro synth suits the game look).
