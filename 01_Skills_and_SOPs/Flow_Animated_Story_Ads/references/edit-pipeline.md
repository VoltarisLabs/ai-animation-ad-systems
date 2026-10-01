# The edit pipeline

Each ad is built by a small Python script that writes three ffmpeg inputs (an input list, a video `filter_complex` script, an audio `filter_complex` script) plus one ASS file for all on-screen text and HUD. A shell script renders. Two reference builders are in `scripts/`:

| Builder | Look | Voice handling |
|---|---|---|
| `build_hud_ad.py` + `render_hud_ad.sh` | full-frame clips, game HUD (minimap, star meter, toasts, objectives, mission banners), subtitles, comic freeze frame, cost list | keeps the read and stretches chosen pauses (`MIN_GAP`); to cut long pauses instead, port `pause_cuts()`, `make_map()`, `KEEP_GAP`/`MAX_GAP` and the voice `keeps` loop from `build_card_reel.py` |
| `build_card_reel.py` + `render_card_reel.sh` + `make_card_assets.py` | "ClayReel": footage in a white rounded card on cream/black backgrounds, small lead words + big red keyword above, stamps, progress bar; optional new-hook block | cuts every pause over 0.4 s down to 0.3 s |

Set up an ad folder like this, keeping the file names (the render scripts call the builders by name and the builders read `src/` and `work/` next to themselves):

```
10_Video_Builds/<Ad_Name>/
  build_hud_ad.py  render_hud_ad.sh          (or the card-reel trio)
  src/   c1_splash.mp4 ... s2_table.jpg ... vo.mp3  sfx/
  refs/  work/  out/
```

Then: `mkdir -p work && python <skill>/scripts/words.py src/vo.mp3 work/vo_words.json` (word times; both builders need them), edit the CONFIG block and the events in `build()`, and run `bash render_*.sh`.

Setup: FFmpeg 7.0 or newer with libass (older builds: replace `-/filter_complex FILE` with `-filter_complex_script FILE`; on Windows the Gyan build works), Python 3.10+ with Pillow and faster-whisper, fonts Anton, Archivo Black, Bebas Neue and Montserrat (Google Fonts, OFL) in a folder given by `FONTS_DIR` (default `./fonts`). No sound files needed: `scripts/make_synth_sfx.sh` writes a synthesized set.

## 1. Timeline from the voice

1. **Phrases.** `silencedetect=n=-40dB:d=0.12` (0.25 for a slow read) splits the voice into speech segments. `PHRASES` holds the script text of each segment and the builder asserts the counts match, so a changed recording fails loudly instead of drifting. On a mismatch it prints where the segments fell with their words: write `PHRASES` from that printout, not from the script's punctuation.
2. **Pause map.** Either cut long pauses (keep the middle 0.3 s of anything over 0.4 s; a 57 s cut of a 55 s read became 43 s with nothing lost) or stretch chosen ones (add silence after "maxed out", "none of that", "empty" so a freeze, a reveal or a jingle can land). A function `f(t)` maps voice time to ad time; every text, shot and sound time goes through it.
3. **Word times.** faster-whisper word timestamps (`scripts/words.py`) give keywords inside phrases (for example the "closing costs" list item). Star pops use phrase ends from silencedetect, which are more reliable than whisper's first-word times.

## 2. Shots

- A shot starts 0.10 s before its first line (`bound(k) = q(P[k] - 0.10)`), so the picture changes just before the words.
- Snap every cut to the 24 fps grid (`q(t) = round(t*24)/24`) and cut each segment to an exact frame count (`trim=end_frame=n`). Unsnapped cuts round up a frame each and the pictures drift behind the words (seen as the previous line lingering over the new shot).
- Pick the source window by anchoring a moment in the clip to a word: `(src_t, ad_t)` → `ss = src_t - (ad_t - t0)`. Examples: head drop at 5.0 s on "fix it all"; paper sweep at 1.3 s on "No need"; glance back at 5.25 s just before "Empty".
- `CLIP_LEN` holds each clip's real length (Flow returns 8 or 10 s); `tpad=stop_mode=clone` covers a clip that runs short and the frame count trims the rest.
- Stills: centred push-in 100→107%: prescale 4x with lanczos, `crop` to 4x frame, then `zoompan=z='1+0.07*on/N':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1`. 2x still shimmers on thick outlines; anchoring at the top-left drifts. `zoompan` rounds to whole pixels, so slow pushes still twitch on fine line art: the `perspective` filter in section 8 is smoother.
- Comic freeze frame (on the hook payoff): grab the frame, boost colour, thin ink edges from `FIND_EDGES`, light halftone dots only in deep shadows, white panel border with a black rule. Hold it static (a push-in crops the border unevenly). A heavy version turned his face black: keep the effect light.
- Punch-in with shake and a 2-frame flash on an impact: `scale` to 1.1x, `crop` with a decaying `sin` offset after the impact time, `eq=brightness=0.18:enable='between(t,T,T+0.08)'`.
- Keep the character facing away or wide while the narrator says a company line ("Ours too"): a face-on punch-in made him read as the speaker.

## 3. On-screen text: one ASS file

Put every text and HUD element in one ASS file, rendered once with `ass=...:fontsdir=...` after the concat. `build_hud_ad.py` overlays the minimap PNG first and puts the ASS on top; the second game-look ad puts the minimap after the ASS instead (section 8), so banners and the pause dim don't grey it. Useful patterns:

- Pop-in: `\fscx150\fscy150\t(0,120,\fscx100\fscy100)`; slam: add `\frz-4`.
- Vector stars: an ASS drawing (`\p1`) of a 10-point star path, positioned with `\an5\pos(x,y)` so scaling grows from the centre (with `\an7` the star slides diagonally). Unlit slot: `\1a&HFF&` with an outline. Pop-off: white, `\t(0,400,\fscx260\fscy260\alpha&HFF&)`.
- Dark band behind a banner: a drawn rectangle with `\1a&H60&`.
- Strike-through: `\s1` plus a grey colour on a second event starting at the strike time.
- Time codes: floor to centiseconds (`floor(t*100)/100`) so an event ending on a cut never spills one frame into the next shot. A subtitle whose start sits a hair before its shot's rounded start can end up zero-length; look up its shot with `P[a] + 0.05`.
- Subtitles off wherever a title, list or banner already shows the same words.
- The minimap is a PIL PNG overlaid with `enable='not(between(t,a,b))'` to hide it in shots where it covers the face.

## 4. Sound

- Voice: cut or pad pieces (`atrim` + `apad=pad_dur`), 8 ms fades at joins, concat, `apad=whole_dur=TOTAL`.
- Clip ambience under the voice at 0.16-0.30, muted for clips with invented speech; duck a loud clip moment under a key word with `volume='if(between(t,a,b),0.12,0.30)':eval=frame`.
- Effects line up on their attack, not their file start. Measure a file's lead-in (`silencedetect=n=-40dB:d=0.005`, the first `silence_end`) and trim it (`atrim=start=`) or subtract it from the delay. One effect file had 0.6 s of near-silence before its hit, so every thump landed half a second late until trimmed.
- An effect on the exact word masks it. Put star-pop sounds at the end of the phrase they mark, keep them short and 2-8 dB under the voice, and fire a jingle or sting after the payoff word, ducking it (envelope) before the call to action.
- Inputs used more than once go through `asplit`.
- Fade the master out over the last 0.5 s so a jingle tail doesn't stop dead on loop.
- Synthesized effects (no licence needed), written as files by `scripts/make_synth_sfx.sh`:

| File | Use | `aevalsrc` / source |
|---|---|---|
| menu.wav | star slam | thump `0.9*sin(2*PI*(80+220*exp(-t*28))*t)*exp(-t*13)`, 0.35 s |
| notify.wav, phone.wav | toasts, mission and end-card pings | blip `0.5*sin(2*PI*1320*t)*exp(-t*38)+0.3*sin(2*PI*1980*t)*exp(-t*45)`, 0.18 s |
| pickup.wav | star pop | rise `0.55*sin(2*PI*(620+1500*t)*t)*exp(-t*16)`, 0.25 s |
| mission.wav | closing sting | C-major chord `(0.17*sin(2*PI*523.25*t)+0.15*sin(2*PI*659.25*t)+0.15*sin(2*PI*783.99*t)+0.12*sin(2*PI*1046.5*t)+0.25*sin(2*PI*130.81*t))*(1-exp(-t*40))*exp(-t*3.2)`, 1.3 s |
| whoosh (inline) | titles | `anoisesrc=d=0.5:c=pink:a=0.7,highpass=f=700,lowpass=f=7000,afade=t=in:d=0.32,afade=t=out:st=0.32:d=0.18` |

## 5. Loudness

Target -14 LUFS integrated, peaks under about -1.5 dBTP. Two-pass `loudnorm` falls back to dynamic mode on these mixes (effects peaks), which pumps the hook. Instead: measure the raw mix, apply one fixed gain toward -14 (+1.5 LU for what the limiter shaves off) plus a brickwall `alimiter=limit=0.708`, measure again and trim the gain once more. Check the final mp4 with `ebur128=peak=true`.

## 6. Render

The render scripts read the input list without `mapfile` (bash 3 on macOS has none) and strip Windows CRLF, map the mix as the last input automatically, then:

```bash
ffmpeg -y "${AIN[@]}" -/filter_complex work/audio_graph.txt -map "[aout]" -ar 48000 -ac 2 -t "$T" work/mix_raw.wav
# ... loudness (above) -> work/mix.wav
ffmpeg -y "${IN[@]}" -/filter_complex work/video_graph.txt -map "[vout]" -map <MIX_INDEX>:a \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -movflags +faststart -t "$T" out/ad.mp4
```

Windows paths inside filter arguments need the drive colon escaped: `ass='E\:/path/caps.ass'`. The builders compute this from their own location (`ff_path`).

## 7. Only a finished mp4?

Rebuilding from the source project (voice file + clips) is the supported path; ask for it first. For captions or HUD on a finished file only: `python scripts/words.py in.mp4 work/vo_words.json`, write `work/caps.ass` from a builder's ASS header and event helpers, then `ffmpeg -i in.mp4 -vf "ass='work/caps.ass':fontsdir='fonts'" -c:v libx264 -crf 18 -c:a copy out.mp4`.

## 8. Techniques from the second game-look ad

These came out of "Stop the Drain" (`references/examples/gta-stop-the-drain.md`); port them into a copy of `build_hud_ad.py` as needed.

- **Sub-pixel push-in.** Instead of `zoompan`, crop with `perspective` (no pre-scale needed; `in` is the frame number counted from 1, `nf` the frame count, `cx`/`cy` the zoom centre as fractions):
  ```python
  Z = f"({z0}+({z1}-{z0})*(in-1)/{max(nf - 1, 1)})"
  L, T = f"((W-W/{Z})*{cx})", f"((H-H/{Z})*{cy})"
  f"perspective=x0='{L}':y0='{T}':x1='({L}+W/{Z})':y1='{T}':x2='{L}':y2='({T}+H/{Z})':x3='({L}+W/{Z})':y3='({T}+H/{Z})':interpolation=cubic:eval=frame"
  ```
- **Still-to-clip pairs share one push.** Concat the still and the clip it turns into, then apply one push to the pair, so the cut doesn't snap back to 100%. Use the clip's own first frame as the still (`select=eq(n\,0)`), not the Nano Banana original: Veo reframes slightly (SSIM 0.92 with a centre crop, 0.67-0.78 otherwise).
- **Cross-faded join.** Two clips that share a frame but differ in sharpness: run the second clip XF longer and use `xfade=transition=fade:duration=0.25:offset=<first clip length in seconds - 0.25>` (XF = 6 frames = 6/24 = 0.25 s; xfade takes seconds, not frames). Skip a static lead-in on the second clip.
- **Partial slow motion.** Split the clip into three trims by frame: real speed where the motion is fast, `setpts=k*PTS,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1` only on the calm stretch, real speed again; `k` gets 3% spare so the source outlasts the shot. Slow that stretch's audio the same amount with two `atempo` stages (each stage goes down to 0.5).
- **Minimap above the captions.** `ass=...` first, then `overlay` the minimap PNG, so banners and dims don't grey half of it.
- **Time skip.** A short dip to black as an ASS rectangle on layer 0 (under subtitles and HUD), `\fad(70,200)`, around the cut.
- **Pause look.** A full-frame black rectangle at `\1a&H70&` (ASS alpha is transparency: about 56% opaque) plus `hue=s=0.35:enable='between(t,a,b)'` on the video, one PAUSED title above the face, the HUD meter still moving on top.
- **Segmented meter.** Twelve drawn rectangles with one ASS event per segment state (green, a white 0.10 s flash, red, then cleared or gold), a red minus bar popping up off each drained segment (a drawing, never a digit), a red flash on the plate, and one white shine sweep for the gold lock.
- **Morphing face in a clip's first second.** Play those frames as a tight crop of the setting (`crop=640:1138:0:250` then scale back to 1080x1920) and cut to the full frame after the morph.
- **Choosing a hold frame.** Measure frame-to-frame difference in the head area; hold where the motion has settled and the mouth is closed, not mid-turn.
- **Measure sound attacks.** Some effect files have a quiet pre-blip before the real hit; align on the main attack.
