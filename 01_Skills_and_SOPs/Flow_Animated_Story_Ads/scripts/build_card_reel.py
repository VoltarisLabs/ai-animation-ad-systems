"""Card-reel story ad builder (reference implementation; it made the claymation "Put the hammer down" ad).

NOT CLEARED FOR LAUNCH as configured: "Bonus cash" / "cash bonus" is not in the claims registry and
"Get an offer." implies an offer for every submission (registry Section 3). Replace both before any real use.

Look: the clip sits in a white rounded card (936x1248 at 72,592) on alternating cream / black backgrounds
(make them once with make_card_assets.py); small lead words and one big red keyword above the card; offer
stamps; an orange progress bar; light grain. Full-frame beats are allowed ("full" mode).

Timing: every voice pause over MAX_GAP is cut down to KEEP_GAP (a 57 s cut of a 55 s read became 43 s); every
beat, text, stamp and sound time is written in ORIGINAL voice time and mapped through the cut list; cuts snap
to the 24 fps grid so text and pictures change on the same frame. Lead words show the instant a shot starts.

Optional new hook (USE_INTRO = True): swaps the first beat and the first voice line (its first INTRO_WORDS
words) for a new clip (a wall smash cut into two shots, punch-in + shake + 2-frame flash on impact) and a
separately recorded, more excited read of that line (src/vo_intro.mp3); everything after it shifts by the
new intro length. Without it: USE_INTRO = False, a first BEAT that starts at 0.00, and SMASH / VO_INTRO taken
out of INPUT_FILES (and the index names).

Put this file, render_card_reel.sh and make_card_assets.py INTO the ad folder (beside src/ and work/),
keeping their names. Edit the CONFIG part (INPUT_FILES, CLIP_LEN, BEATS, STAMPS, SFX, INTRO_*), then run
render_card_reel.sh. Needs work/vo_words.json (python words.py src/vo.mp3 work/vo_words.json), fonts
Montserrat, Archivo Black and Anton in FONTS_DIR (default ./fonts), ffmpeg 7+ with libass.
"""
import json
import math
import os
from pathlib import Path

HERE = Path(__file__).parent
FONTS_DIR = Path(os.environ.get("FONTS_DIR", HERE / "fonts"))
# libass silently falls back to another typeface when a font is missing, so fail loudly instead
assert FONTS_DIR.is_dir() and any(FONTS_DIR.glob("*.ttf")), f"no fonts in {FONTS_DIR}; set FONTS_DIR"


def ff_path(p):
    """A path for an ffmpeg filter argument: forward slashes, and the drive colon escaped on Windows."""
    return Path(p).resolve().as_posix().replace(":", "\\:")


# ================================================================ CONFIG (edit per ad)
W, H, FPS = 1080, 1920, 24
INK, WHITE, RED = "&H001A1A1A", "&H00FFFFFF", "&H001F4BFF"
CARD_X, CARD_Y, CARD_W, CARD_H = 72, 592, 936, 1248
KEEP_GAP, MAX_GAP = 0.30, 0.40
END_HOLD = 1.40
HOUSE_ZOOM = "crop=810:1440:135:480"   # house shots: zoom 1.33x on the bottom-centre house

INPUT_FILES = ["src/n0_smash.mp4", "src/leak1.mp4", "src/leak2.mp4", "src/leak3.mp4", "src/leak4.mp4",
               "src/n6_holdhammer.mp4", "src/n3_garage.mp4", "src/n4_lean.mp4", "src/reel_09_glow.mp4",
               "src/reel_10_hand.mp4", "src/n7_thumbs.mp4",
               "work/card_bg_cream.png", "work/card_bg_black.png", "work/card_mask.png",
               "src/vo_intro.mp3", "src/vo.mp3", "work/mix.wav"]
SMASH, L1, L2, L3, L4, N6, N3, N4, GLOW, HAND, N7, BG_CREAM, BG_BLACK, MASK, VO_INTRO, VO, MIX = range(17)
assert INPUT_FILES[-1] == "work/mix.wav"         # the render script maps the last input as the audio
LOOPED = {BG_CREAM, BG_BLACK, MASK}
# real clip lengths (Flow returns 8 or 10 s)
CLIP_LEN = {SMASH: 8.0, L1: 8.0, L2: 8.0, L3: 8.0, L4: 8.0, N6: 8.0, N3: 8.0, N4: 8.0, GLOW: 8.0, HAND: 8.0, N7: 8.0}

# --- new hook, in AD time (not the original voice timeline)
USE_INTRO = True
INTRO_WORDS = 8            # words in the old first line that the new read replaces ("Bonus cash ... down.")
INTRO_AT = 0.40           # where vo_intro.mp3 starts; its speech begins 0.105 s in ("Bonus" ~0.51)
INTRO_SPEECH_END = 2.157   # end of speech inside vo_intro.mp3
INTRO_GAIN = 0.42          # the new read is ~10 LU hotter than vo2; this leaves it ~2 LU above the rest
OLD_INTRO_END = 2.85       # original-timeline end of the old intro beat
INTRO_CUT = 1.45           # swing + blast -> hammer lowering, just before "if you put..."
IMPACT = 0.27              # hammer hits the wall (source 1.12)
# 1.1x punch-in, a shake that dies out after the impact, and a two-frame flash on the hit
SHAKE = (f"scale=1188:2112,crop=1080:1920:x='54+30*sin(t*95)*exp(-7*max(t-{IMPACT},0))*gte(t,{IMPACT})'"
         f":y='96+24*cos(t*80)*exp(-7*max(t-{IMPACT},0))*gte(t,{IMPACT})',"
         f"eq=brightness=0.18:enable='between(t,{IMPACT},{IMPACT + 0.08})'")
# smash clip's own sound (grunt, crash, cash, floor thud): loud on the hit, ducked under the voice
INTRO_SFX = [(SMASH, 0.85, INTRO_CUT, 0.0, "0.15+0.4*max(0,min(1,(0.55-t)/0.15))"),
             (SMASH, 4.875, 1.35, INTRO_CUT, 0.5)]
# the two intro shots, in ad time; an end of None means "the end of the intro", worked out in build()
# unconfirmed claim: replace "Bonus cash!" before reuse
INTRO_BEATS = [
    (0.0, INTRO_CUT, SMASH, 0.85, "full", "black", 0, SHAKE, [("KO", "Bonus cash!", INTRO_AT + 0.08, 345, None)]),
    (INTRO_CUT, None, SMASH, 4.875, "full", "black", 0, "", [("SO", "if you put the hammer down.", INTRO_AT + 1.06, 488)]),
]

# Times below are in the ORIGINAL voice timeline; they are mapped through the pause cuts.
# (start, end, input, source start, mode, background, crop top, extra filter, text items)
# text item: (style, text, time, y)  L = lead words (shown at shot start), K = red keyword, S = small line
LY, KY, SY = 300, 445, 548
BEATS = [   # the intro (original 0.00-2.85) is built in build() from the smash clip
    (2.85, 5.00, L1, 0.00, "card", "cream", 240, "", [("L", "It started with one little", 0, LY), ("K", "leak.", 4.06, KY)]),
    (5.00, 6.45, L2, 1.72, "card", "black", 200, "", [("L", "Then the", 0, LY), ("K", "ceiling.", 5.38, KY)]),
    (6.45, 7.95, L2, 4.20, "card", "cream", 400, "", [("L", "Then the", 0, LY), ("K", "floor.", 6.80, KY)]),
    (7.95, 11.75, L3, 0.00, "card", "black", 480, "", [("L", "Now", 0, LY), ("K", "every weekend", 8.76, KY), ("S", "belongs to this house.", 9.64, SY)]),
    (11.75, 14.85, N6, 0.00, "card", "cream", 250, "", [("L", "In the back of your mind:", 0, LY), ("K", "sell it like this?", 14.24, KY)]),
    (14.85, 17.60, L1, 4.60, "card", "black", 150, "", [("L", "will I get", 0, LY), ("K", "ripped off?", 16.46, KY)]),
    (17.60, 20.40, L2, 5.00, "card", "cream", 450, "", [("L", "The repair quotes keep getting", 0, LY), ("K", "longer.", 19.38, KY)]),
    (20.40, 23.20, N3, 1.50, "card", "black", 300, "", [("L", "And the garage still isn't", 0, LY), ("K", "cleaned out.", 21.96, KY)]),
    (23.20, 26.65, N4, 1.60, "card", "cream", 100, "", [("L", "Here's the part", 0, LY), ("K", "nobody tells you", 23.84, KY), ("S", "about selling a house like this.", 24.58, SY)]),
    (26.65, 29.90, L3, 3.80, "card", "black", 480, "", [("L", "You can sell it", 0, LY), ("K", "the way it is.", 28.18, KY)]),
    (29.90, 31.25, GLOW, 6.50, "full", "cream", 0, HOUSE_ZOOM, []),
    (31.25, 33.15, N3, 5.00, "card", "black", 450, "", [("L", "Leave what you", 0, LY), ("K", "don't want.", 31.96, KY)]),
    (33.15, 35.55, L4, 0.00, "card", "cream", 200, "", [("L", "And you pick the", 0, LY), ("K", "closing date.", 34.04, KY)]),
    # two pops instead of one long hold: "nobody tells you." then "You never had to / fix it first."
    (35.55, 40.55, N6, 3.00, "card", "black", 250, "", [("L", "That's the part", 0, LY, 38.26), ("K", "nobody tells you.", 36.62, KY, 38.26),
                                                        ("L", "You never had to", 38.32, LY), ("K", "fix it first.", 39.12, KY)]),
    (40.55, 43.25, HAND, 1.40, "full", "black", 0, "", [("L", "That's why the choice", 0, 360), ("K", "stays yours.", 41.70, 520)]),
    (43.25, 49.30, GLOW, 0.00, "full", "cream", 0, HOUSE_ZOOM, []),
    # unconfirmed claims on the next two beats ("cash bonus", "Get an offer."): replace before reuse
    (49.30, 53.85, N7, 0.50, "card", "black", 250, "", [("L", "So put the", 0, LY), ("K", "hammer down,", 50.00, KY), ("S", "and ask about your cash bonus.", 51.00, SY)]),
    (53.85, None, N7, 5.60, "card", "cream", 250, "", [("L", "Get an", 0, LY), ("K", "offer.", 54.14, KY), ("S", "No obligation.", 54.60, SY)]),
]
STAMPS = [("NO REPAIRS", 30.02, 520, -3, 31.25),
          ("NO COMMISSION", 43.32, 380, -4, 49.30), ("NO CLOSING COSTS", 44.80, 540, 3, 49.30),
          ("NO OBLIGATION", 46.88, 700, -3, 49.30)]
# (input, source start, duration, original timeline start, volume)
SFX = [(L1, 0.0, 1.85, 2.85, 0.35), (L2, 1.93, 1.29, 5.21, 0.35), (N3, 1.5, 2.8, 20.40, 0.25),
       (N7, 2.6, 2.4, 51.40, 0.30)]
# ================================================================ end CONFIG


def load_words():
    return json.loads((HERE / "work" / "vo_words.json").read_text(encoding="utf-8"))


def pause_cuts(words):
    """(start, end) stretches of the original voice to remove: the middle of every pause > MAX_GAP."""
    cuts = []
    for a, b in zip(words, words[1:]):
        gap = b["s"] - a["e"]
        if gap > MAX_GAP:
            half = KEEP_GAP / 2
            cuts.append((a["e"] + half, b["s"] - half))
    return cuts


def make_map(cuts):
    def f(t):
        shift = 0.0
        for s, e in cuts:
            if t >= e:
                shift += e - s
            elif t > s:
                return s - shift
        return t - shift
    return f


def tc(t):
    # floor to centiseconds: an event ending on a cut never spills one frame into the next shot
    t = math.floor(max(t, 0.0) * 100 + 1e-6) / 100
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def key_size(text):
    return int(min(190, 960 / (max(len(text), 4) * 0.52)))


def build():
    words = load_words()
    cuts = pause_cuts(words)
    f = make_map(cuts)
    # every cut sits on the 24 fps frame grid, so video segments and caption events change together
    # (unsnapped cuts round up a frame each and drift the pictures behind the words)
    q = lambda t: round(t * FPS) / FPS
    ident = lambda t: t
    beats = []
    if USE_INTRO:
        # the new intro line replaces the old one (words 0..INTRO_WORDS-1); the first pause cut sits between
        # the old line's last word and the next word, so everything from its end on is shifted as one block
        first_cut = cuts[0]
        last_old, first_new = words[INTRO_WORDS - 1], words[INTRO_WORDS]
        assert last_old["e"] < first_cut[0] < first_cut[1] < first_new["s"], "first pause cut moved"
        shift = INTRO_AT + INTRO_SPEECH_END + KEEP_GAP - f(first_new["s"])
        g = lambda t: f(t) + shift
        intro_end = q(g(OLD_INTRO_END))
        for (t0, t1, inp, ss, mode, bg, y0, extra, items) in INTRO_BEATS:
            items = [it[:4] + (intro_end,) if len(it) > 4 and it[4] is None else it for it in items]
            beats.append((q(t0), intro_end if t1 is None else q(t1), inp, ss, mode, bg, y0, extra, items, ident))
    else:
        g, intro_end = f, 0.0
    total = q(g(words[-1]["e"]) + END_HOLD)
    for (t0, t1, *rest) in BEATS:
        beats.append((q(g(t0)), total if t1 is None else q(g(t1)), *rest, g))

    # --- captions (lead words at shot start, keyword and small line when spoken)
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: L,Montserrat,88,{INK},{INK},&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,30,30,0,1
Style: K,Archivo Black,190,{RED},{RED},&H00000000,&H00000000,0,0,0,0,100,100,-2,0,1,0,0,5,30,30,0,1
Style: S,Montserrat,56,{INK},{INK},&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,30,30,0,1
Style: Stamp,Anton,132,{WHITE},{WHITE},{RED},&H00000000,0,0,0,0,100,100,2,0,3,20,0,5,0,0,0,1
Style: KO,Archivo Black,190,{RED},{RED},{WHITE},&H80000000,0,0,0,0,100,100,-2,0,1,9,6,5,30,30,0,1
Style: SO,Montserrat,70,{WHITE},{WHITE},&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,7,4,5,30,30,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    # KO / SO: outlined keyword and line for text laid straight over full-screen footage (the intro)
    ev = []
    for (t0, t1, _inp, _ss, mode, bg, _y0, _x, items, m) in beats:
        col = WHITE if bg == "black" else INK
        for item in items:
            style, text, t, y = item[:4]
            end = q(m(item[4])) if len(item) > 4 else t1   # optional early/late end, e.g. two pops in one shot
            if style in ("K", "KO"):
                ev.append(f"Dialogue: 2,{tc(m(t))},{tc(end)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{key_size(text)}"
                          f"\\fscx135\\fscy135\\frz-5\\t(0,140,\\fscx100\\fscy100\\frz0)\\fad(50,0)}}{text}")
            else:
                # a lead given time 0 shows the instant the shot starts; a timed one waits for its words
                start = t0 + 0.02 if (style == "L" and t == 0) else max(t0 + 0.02, m(t))
                size = "" if style in ("S", "SO") else ("\\fs78" if len(text) > 26 else "")
                ev.append(f"Dialogue: 1,{tc(start)},{tc(end)},{style},,0,0,0,,"
                          f"{{\\c{col}&{size}\\move(540,{y + 26},540,{y},0,140)\\fad(70,0)}}{text}")
    for text, t, y, rot, end in STAMPS:
        ev.append(f"Dialogue: 3,{tc(g(t))},{tc(g(end))},Stamp,,0,0,0,,{{\\pos(540,{y})\\frz{rot}\\fscx165\\fscy165"
                  f"\\alpha&HFF&\\t(0,110,\\fscx100\\fscy100\\alpha&H00&)}}{text}")
    (HERE / "work" / "caps.ass").write_text(head + "\n".join(ev) + "\n", encoding="utf-8")

    # --- voice with pauses cut: keep the complement of the cut list, 8 ms fades at each join
    keeps, last = [], 0.0
    for s, e in cuts:
        keeps.append((last, s))
        last = e
    keeps.append((last, words[-1]["e"] + 0.35))
    if USE_INTRO:
        keeps = keeps[1:]                  # drop the old intro line; the new one is mixed in below
    rest_ms = int(round(g(keeps[0][0]) * 1000))
    ap = []
    for k, (s, e) in enumerate(keeps):
        ap.append(f"[{VO}:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
                  f"afade=t=in:st=0:d=0.008,afade=t=out:st={max(e - s - 0.008, 0):.3f}:d=0.008[k{k}]")
    ap.append("".join(f"[k{k}]" for k in range(len(keeps))) + f"concat=n={len(keeps)}:v=0:a=1,"
              f"adelay={rest_ms}|{rest_ms},apad=whole_dur={total:.3f}[vo]")
    mix = ["[vo]"]
    if USE_INTRO:
        in_ms, in_len = int(round(INTRO_AT * 1000)), INTRO_SPEECH_END + 0.12
        ap.append(f"[{VO_INTRO}:a]atrim=end={in_len:.3f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
                  f"volume={INTRO_GAIN},afade=t=out:st={in_len - 0.06:.3f}:d=0.06,adelay={in_ms}|{in_ms}[voi]")
        mix.append("[voi]")
    sfx = (INTRO_SFX if USE_INTRO else []) + [(inp, ss, d, g(at), vol) for (inp, ss, d, at, vol) in SFX]
    for k, (inp, ss, d, at, vol) in enumerate(sfx):
        ms = int(round(at * 1000))
        gain = f"volume='{vol}':eval=frame" if isinstance(vol, str) else f"volume={vol}"
        ap.append(f"[{inp}:a]atrim=start={ss:.3f}:end={ss + d:.3f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
                  f"{gain},afade=t=in:st=0:d=0.02,afade=t=out:st={d - 0.12:.3f}:d=0.12,adelay={ms}|{ms}[sfx{k}]")
        mix.append(f"[sfx{k}]")
    pop = "aevalsrc='0.55*sin(2*PI*(380+950*exp(-t*38))*t)*exp(-t*34)|0.55*sin(2*PI*(380+950*exp(-t*38))*t)*exp(-t*34)':s=48000:d=0.18"
    for k, (_t, t, *_r) in enumerate(STAMPS):
        ms = int(round(g(t) * 1000))
        ap.append(f"{pop},volume=0.45,adelay={ms}|{ms}[pop{k}]")
        mix.append(f"[pop{k}]")
    ap.append("".join(mix) + f"amix=inputs={len(mix)}:duration=first:normalize=0,atrim=end={total:.3f}[aout]")
    (HERE / "work" / "audio_graph.txt").write_text(";\n".join(ap), encoding="utf-8")

    # --- video
    vp, labels = [], []
    cards = [i for i, b in enumerate(beats) if b[4] == "card"]
    for name, src in (("cream", BG_CREAM), ("black", BG_BLACK)):
        idx = [i for i in cards if beats[i][5] == name]
        vp.append(f"[{src}:v]split={len(idx)}" + "".join(f"[bgs{i}]" for i in idx))
    vp.append(f"[{MASK}:v]format=gray,split={len(cards)}" + "".join(f"[ms{i}]" for i in cards))
    for i, (t0, t1, inp, ss, mode, bg, y0, extra, _items, _m) in enumerate(beats):
        d = t1 - t0
        n = int(round(d * FPS))           # exact frame count for this segment
        assert ss + 0.1 < CLIP_LEN[inp], (inp, ss)
        src_d = min(d, CLIP_LEN[inp] - ss)
        base = f"[{inp}:v]trim=start={ss:.3f}:end={ss + src_d:.3f},setpts=PTS-STARTPTS,fps={FPS}"
        if extra:
            base += f",{extra}"
        # pad with the last frame (covers a short source), then cut to exactly n frames
        base += (f",scale={W}:{H}:flags=lanczos,setsar=1,tpad=stop_mode=clone:stop_duration=2,"
                 f"trim=end_frame={n},setpts=PTS-STARTPTS")
        if mode == "full":
            vp.append(base + f",format=yuv420p[b{i}]")
        else:
            vp.append(f"[bgs{i}]fps={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,format=yuv420p[bg{i}]")
            vp.append(f"[ms{i}]fps={FPS},trim=end_frame={n},setpts=PTS-STARTPTS[m{i}]")
            vp.append(base + f",crop={W}:{W * 4 // 3}:0:{y0},scale={CARD_W}:{CARD_H},format=rgba[cc{i}]")
            vp.append(f"[cc{i}][m{i}]alphamerge[ca{i}]")
            vp.append(f"[bg{i}][ca{i}]overlay=x={CARD_X}:y={CARD_Y}:shortest=1,setsar=1,format=yuv420p[b{i}]")
        labels.append(f"[b{i}]")
    vp.append("".join(labels) + f"concat=n={len(beats)}:v=1:a=0,noise=alls=5:allf=t+u,"
              f"ass='{ff_path(HERE / 'work/caps.ass')}':fontsdir='{ff_path(FONTS_DIR)}',"
              f"drawbox=x=0:y=0:w=iw:h=10:color=black@0.35:t=fill,format=yuv420p[vt]")
    vp.append(f"color=c=0xFF4B1F:s={W}x10:r={FPS}:d={total:.3f}[bar]")
    vp.append(f"[vt][bar]overlay=x='-w+w*t/{total:.3f}':y=0:eof_action=pass,format=yuv420p[vout]")
    (HERE / "work" / "video_graph.txt").write_text(";\n".join(vp), encoding="utf-8")

    args = []
    for k, fn in enumerate(INPUT_FILES):
        if k in LOOPED:
            args += ["-loop", "1", "-framerate", str(FPS)]
        args += ["-i", fn]
    (HERE / "work" / "inputs.txt").write_text("\n".join(args), encoding="utf-8", newline="\n")
    (HERE / "work" / "total.txt").write_text(f"{total:.3f}", encoding="utf-8", newline="\n")
    removed = sum(e - s for s, e in cuts)
    print(f"{len(cuts)} pauses cut, {removed:.1f}s removed, intro {intro_end:.3f}s, new length {total:.3f}s")


if __name__ == "__main__":
    build()
