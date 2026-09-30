# Lessons learned

| What happened | Fix that worked |
|---|---|
| Team idea (money bursting from the wall) contradicted the line ("put the hammer down") and nobody said so until clips were made | Flag story/claim conflicts the moment they appear; propose an order that makes both true (money pops, line, he lowers the hammer) |
| A clip came back with a different-looking character | Make a reference image first and attach it to every clip; drop the off-model clip rather than hiding it with a crop |
| Veo changed a spoken line / invented speech | "He does not speak. No dialogue, no voice, no music." Mute or duck clip audio; trim the bad bit |
| Flow blocked a prompt mentioning a death ("late mother") | Remove the death reference; imply it (an inherited house, belongings) |
| "Too much dead space" | Cut every pause over 0.4 s to 0.3 s through a time map; lead words at shot start; bigger card and type; zoom in on wide house shots (1.33x crop) |
| Text drifted behind the pictures | Snap cuts to the frame grid and trim to exact frame counts |
| Captions in the middle rejected; word pop at top rejected | Tape captions with zoom/shake, stamps, progress bar; or the card reel; or game subtitles + HUD |
| "Not a game character" (flat cartoon tired dad) | "open-world video game loading-screen poster art style, semi-realistic digital painting, bold ink outlines, cel-shaded colour blocks", rugged confident character, hero angle |
| Legs disappeared behind a tailgate | Seat him on the tailgate, "whole body visible from cap to boots" |
| Comic freeze made his face a black blob | Thin, light edges; halftone only in deep shadows; no heavy posterize |
| Hook title covered his mouth | Put the hook title low (over the bucket) |
| Objective line covered his cap | Move objectives to the bottom (game-style) |
| Sound effects buried key words ("Empty", "commission", "No need") | Effects after the word, shorter and quieter; duck clip sounds under words; trim effect lead-ins |
| `loudnorm` went dynamic and pumped the hook | Fixed gain + limiter, measure, trim again |
| "Maxed out." subtitle never showed | Look up a line's shot with a small offset; floor ASS times to centiseconds |
| Admission line over a face-on close-up read as the character saying it | Put company lines over wide or back-facing shots |
| The team found "Walk-Away Offer" unclear and wanted "best deal" | "Best deal/price" is banned; show everything they skip instead ("Listing means repairs, cleanup, commission and closing costs. This cash offer? None of that.") and let the stars pop |
| Request to clone a voice from third-party recordings (game audio, YouTube) | Decline; use the speaker's own consented recording (ElevenLabs Professional clone with his verification) or an original voice; file written consent in PERMISSIONS.md |
| Handshake + deal papers ending | Blocked while the buyer-identity claim is frozen and because it reads as a fake customer story; keep it written up as an on-hold alternate ending |
| Python on Windows wrote CRLF into the ffmpeg input list | `tr -d '\r'` before `mapfile` |
