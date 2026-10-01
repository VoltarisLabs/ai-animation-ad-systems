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
| A `while read` loop dropped the last input (the list had no final newline), so ffmpeg read `-/filter_complex` as a file | `while IFS= read -r line \|\| [ -n "$line" ]; do ...` |

## Second game-look ad ("Stop the Drain")

| What happened | Fix that worked |
|---|---|
| Ingredients to Video gave a different, lighter-skinned man, opened the mailbox instead of closing it and dropped the house | Edit an approved frame in Nano Banana Pro ("Edit the attached image. Keep everything else exactly the same... Change only two things: ..."), then animate it with Frames to Video |
| A kitchen still looked like a famous actor | Change the face (round face, thick short beard) and add "must not resemble any real person or celebrity"; then attach the new image, not the old character sheet |
| Frames to Video vanished the stack, then brought it back at 1.9 s | Keep the clean part, export its last clean frame, make the next clip from that frame; the join is invisible |
| The person attached the wrong first frame | Copy the exact file into their downloads folder with an obvious name (`FIRST_FRAME_empty_table.png`) and give its full path; check the new clip's first frame against it (SSIM) |
| The hook's first 1.2 s showed a different-looking face that morphed into the character | Check face crops frame by frame in the first second of every clip. Stopgap: play those frames as a tight crop of the setting and cut wide after the morph |
| The character mouthed words in a silent beat after the line | Hold the last closed-mouth frame, chosen after his head turn settles (measure head-area frame difference); a hold mid-turn reads as a stall |
| A small stamp square on an envelope moved with the camera | Track it with multi-scale template matching from a frame where it is clear, fill it with the envelope's own colour sampled beside it (inpainting pulled in the dark edge line) |
| A PAUSE menu with RESUME / MAP / SETTINGS | Meta rejects images showing features that do nothing; keep only the PAUSED title, a dim and desaturation, placed above the face |
| Slowed clip juddered (`setpts` + `fps` repeats every 5th frame) and froze at the end | Real frames where motion is fast, `minterpolate` only in the calm stretch, 3% spare so the source outlasts the shot; slow its audio the same way |
| Slow push-ins twitched back and forth | `zoompan` rounds to whole pixels; use the `perspective` filter for a sub-pixel crop |
| Banners and the PAUSE dim greyed half of the minimap | Overlay the minimap after the ASS |
| Sharpness jumped where two Veo clips meet on a shared frame | Start the second clip after its static lead-in and cross-fade 6 frames (`xfade`) |
| A toast slid in silently and its sound came 1.5 s later; another ding ran under the next line | Fire a toast and its sound together in a stretched pause beside its line; measure each file's real attack (two third-party pings had a quiet pre-blip of 0.29 s and 0.20 s; the synthesized notify and phone from `make_synth_sfx.sh` start on their attack, SFX_ONSET 0) |
| A team brief asked for "guaranteed offer", "best way to sell" and a news hook (rates above 7%, inflation, oil, war) | Write it as asked, mark each unconfirmed line and give a safe swap; keep the figure out of voice and screen ("Rates jumped") and check the line against a dated source; economy and war topics can send the ad to Meta's social-issue review |
