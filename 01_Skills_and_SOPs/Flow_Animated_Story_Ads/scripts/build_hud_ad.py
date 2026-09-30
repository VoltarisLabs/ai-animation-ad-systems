"""Game-HUD story ad builder (reference implementation; it made the GTA-style "Stress Meter" ad).

Copy this file next to an ad folder (src/, refs/, work/, out/), edit the CONFIG block (input files, phrases,
pauses, shot plan) and the text/sound events inside build(), then run render_hud_ad.sh.
Writes work/inputs.txt, work/video_graph.txt, work/audio_graph.txt, work/caps.ass and work/total.txt.

What it does:
  - splits the voice into phrases on its silences (asserts the count matches PHRASES) and stretches chosen
    pauses (MIN_GAP); every time in the ad goes through the voice->ad time map f(t)
  - lays the Flow clips and stills under the lines: shots start 0.10 s before their first line, cuts snap to
    the 24 fps grid, a clip moment can be anchored to a word with (src_t, ad_t)
  - comic freeze frame with a name card after the hook; centred 4x-oversampled push-ins on stills
  - all on-screen text in one ASS file: subtitles, hook title, STRESS star meter (vector stars that slam on
    and pop off), toasts, objective line with strike-through, mission title, a red cost list struck on the
    payoff, MISSION COMPLETE banner, end card; a PIL minimap, hidden where it would cover the face
  - sound: voice, clip ambience, sound effects aligned to their attack (src/sfx/*.wav from make_synth_sfx.sh;
    a third-party file only with a written licence filed in PERMISSIONS.md, see the skill's
    references/voice-and-audio-rights.md), a closing jingle ducked under the call to action, master fade
No company name, no numbers or $ on screen, no game names or logos.

Needs: ffmpeg with libass, Pillow, work/vo_words.json from scripts/words.py (faster-whisper word times),
fonts Anton, Bebas Neue and Montserrat in FONTS_DIR (default ./fonts).
"""
import json
import math
import os
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

HERE = Path(__file__).parent
FONTS_DIR = Path(os.environ.get("FONTS_DIR", HERE / "fonts"))
# libass silently falls back to another typeface when a font is missing, so fail loudly instead
assert FONTS_DIR.is_dir() and any(FONTS_DIR.glob("*.ttf")), f"no fonts in {FONTS_DIR}; set FONTS_DIR"
W, H, FPS = 1080, 1920, 24
WHITE, BLACK, AMBER, RED = "&H00FFFFFF", "&H00000000", "&H0000B4FF", "&H002E2EE8"


def ff_path(p):
    """A path for an ffmpeg filter argument: forward slashes, and the drive colon escaped on Windows."""
    return Path(p).resolve().as_posix().replace(":", "\\:")


def tc(t):
    # floor to centiseconds: an event ending on a cut never spills one frame into the next shot
    t = math.floor(max(t, 0.0) * 100 + 1e-6) / 100
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def star_path(R=34, r=14.5):
    pts = []
    for k in range(10):
        a = math.radians(-90 + 36 * k)
        rad = R if k % 2 == 0 else r
        pts.append((R + rad * math.cos(a), R + rad * math.sin(a)))
    p = [f"{x:.1f} {y:.1f}" for x, y in pts]
    return "m " + p[0] + " l " + " ".join(p[1:])


# ---------------------------------------------------------------- still assets (PIL)
def make_minimap():
    S = 250
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((6, 6, S - 6, S - 6), fill=(18, 24, 30, 170))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse((10, 10, S - 10, S - 10), fill=255)
    roads = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    rd = ImageDraw.Draw(roads)
    for x in (40, 115, 190):
        rd.line((x, 0, x - 18, S), fill=(150, 160, 170, 200), width=9)
    for y in (60, 150):
        rd.line((0, y, S, y + 14), fill=(150, 160, 170, 200), width=9)
    rd.rectangle((128, 88, 176, 124), fill=(70, 120, 70, 200))          # a park block
    im.paste(roads, (0, 0), Image.composite(roads, Image.new("RGBA", (S, S)), mask))
    # house icon at the centre (amber), player arrow just below it
    cx, cy = S // 2, S // 2
    d.polygon([(cx - 20, cy - 2), (cx, cy - 22), (cx + 20, cy - 2)], fill=(255, 180, 0, 255), outline=(0, 0, 0, 255))
    d.rectangle((cx - 14, cy - 2, cx + 14, cy + 18), fill=(255, 180, 0, 255), outline=(0, 0, 0, 255))
    d.polygon([(cx, cy + 30), (cx - 11, cy + 52), (cx, cy + 45), (cx + 11, cy + 52)], fill=(255, 255, 255, 255),
              outline=(0, 0, 0, 255))
    d.ellipse((6, 6, S - 6, S - 6), outline=(255, 255, 255, 235), width=5)
    im.save(HERE / "work/minimap.png")


def make_freeze(src_clip, src_t):
    png = HERE / "work/freeze_raw.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{src_t:.3f}", "-i", str(HERE / src_clip),
                    "-frames:v", "1", str(png)], check=True)
    im = Image.open(png).convert("RGB").resize((W, H), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(1.30)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Brightness(im).enhance(1.06)
    edges = im.convert("L").filter(ImageFilter.FIND_EDGES).point(lambda v: 150 if v > 70 else 0)
    im.paste((15, 15, 15), (0, 0), edges)
    # halftone dots over the darker half, like a printed comic panel
    dots = Image.new("L", (W, H), 0)
    dd = ImageDraw.Draw(dots)
    lum = im.convert("L").resize((W // 14, H // 14))
    for gy in range(lum.height):
        for gx in range(lum.width):
            v = lum.getpixel((gx, gy))
            if v < 70:
                rr = 1.5 + (70 - v) / 70 * 2.5
                x, y = gx * 14 + 7 + (7 if gy % 2 else 0), gy * 14 + 7
                dd.ellipse((x - rr, y - rr, x + rr, y + rr), fill=60)
    im.paste((20, 10, 40), (0, 0), dots)
    # panel border: white frame with a black ink line, slightly inset
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W - 1, H - 1), outline=(250, 246, 235), width=26)
    d.rectangle((26, 26, W - 27, H - 27), outline=(10, 10, 10), width=7)
    im.save(HERE / "work/freeze.png")


# ================================================================ CONFIG (edit per ad)
# Input order matters: the index constants below and render_hud_ad.sh (-map <MIX>:a) follow it.
# Clips are Flow downloads renamed c<n>_<what>.mp4, stills s<n>_<what>.jpg; the freeze and minimap PNGs
# are generated by this script; mix.wav is written by the render script.
END_HOLD = 1.60
REDLIST = "&H003C3CFF"                          # ASS BGR: a hot red for the listing costs

INPUT_FILES = ["src/c1_splash.mp4", "src/c2_ladder.mp4", "src/c3_beam.mp4", "src/c4_orbit.mp4",
               "src/c5_porch.mp4", "src/c6_sweep.mp4", "src/c7_walk.mp4",
               "src/s2_table.jpg", "work/freeze.png", "src/s8_endcard.jpg", "work/minimap.png",
               "src/vo.mp3", "src/sfx/mission.wav", "src/sfx/notify.wav", "src/sfx/pickup.wav",
               "src/sfx/menu.wav", "src/sfx/phone.wav", "work/mix.wav"]
assert INPUT_FILES[-1] == "work/mix.wav"         # the render script maps the last input as the audio
(C1, C2, C3, C4, C5, C6, C7, S2, FRZ, S8, MAP, VO,
 SX_MISSION, SX_NOTIFY, SX_PICKUP, SX_MENU, SX_PHONE, MIX) = range(18)
STILLS = {S2, FRZ, S8, MAP}
CLIP_LEN = {C1: 10.0, C2: 10.0, C3: 10.0, C4: 8.0, C5: 10.0, C6: 8.0, C7: 8.0}
# Seconds from a sound file's start to its attack, and how much lead-in to trim off. The synthesized set starts
# on its attack (all 0). For any other file measure it: silencedetect=n=-40dB:d=0.005, the first silence_end.
# (One third-party "menu" hit had 0.6 s of near-silence first: SFX_ONSET 0.605 with SFX_START 0.575.)
SFX_ONSET = {SX_MISSION: 0.0, SX_NOTIFY: 0.0, SX_PICKUP: 0.0, SX_MENU: 0.0, SX_PHONE: 0.0}
SFX_START = {}

PHRASES = ["The ceiling's leaking,", "again.", "Stress meter?", "Maxed out.", "Repair quotes piling up,",
           "weekends on a ladder,", "and everyone says:", "fix it all,", "then list it.",
           "There's another way out.", "Listing means repairs,", "cleanup,", "commission and closing costs.",
           "This cash offer?", "None of that.", "Take what matters,", "leave the rest.", "Fix it all first?",
           "No need.", "The house sells as-is.", "You pick the closing date.", "And that stress meter?",
           "Empty.", "Ask for a cash offer.", "No obligation."]
# gap after phrase k -> at least this long (s); only these beats get stretched. For a slow read with long
# pauses, cut instead: keep the middle 0.3 s of every gap over 0.4 s (see build_card_reel.py pause_cuts).
MIN_GAP = {3: 0.45, 9: 0.45, 14: 0.55, 22: 0.75}
# ================================================================ end CONFIG (the shot plan, text and sound
# events are inside build(): look for `plan = [`, the HUD section and the gsfx(...) calls)


def speech_segments():
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(HERE / "src/vo.mp3"), "-af",
                          "silencedetect=n=-40dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()
    dur = int(h) * 3600 + int(m) * 60 + float(s)
    segs, t = [], 0.0
    for a, b in zip(starts, ends):
        if a - t > 0.05:
            segs.append((t, a))
        t = b
    if dur - t > 0.05:
        segs.append((t, dur))
    if len(segs) != len(PHRASES):
        # show where the pauses split the read, so PHRASES can be written from this, not from punctuation
        wj = json.loads((HERE / "work/vo_words.json").read_text(encoding="utf-8"))
        for i, (a, b) in enumerate(segs):
            print(i, f"{a:.2f}-{b:.2f}", " ".join(w["t"] for w in wj if a - 0.05 <= w["s"] < b))
    assert len(segs) == len(PHRASES), f"{len(segs)} speech segments, expected {len(PHRASES)}"
    return segs, dur


def build():
    # Everything below is written for the reference ad (the Stress Meter script). For a new ad, rewrite:
    #   - plan = [...]: which clip or still covers which phrase, and its source start or (src_t, ad_t) anchor;
    #     the freeze frame sits on P[3] (the hook payoff), after shots[0]
    #   - the hook title (CEILING LEAKING. / AGAIN.), the name card (RAY / HOMEOWNER) and the subtitle groups
    #   - pops / pop_text: which phrase ends pop a star and the toast for each (E[14], E[16], E[19], E[20], E[22])
    #   - the toasts on P[4] / P[5], the objectives on P[7] / P[17] (struck on P[18]), the mission title on P[9]
    #   - the cost list on P[10]-P[14], MISSION COMPLETE on P[22], the end card on P[23] / P[24]
    #   - the minimap hide (the C3 shot) and the per-clip ambience levels (amb)
    #   - the gsfx(...) calls at the end
    # The phrase-count assert is the only automatic check: a new script with the same number of phrases
    # would render this ad's text on the wrong words.
    segs, vo_dur = speech_segments()
    # stretch: insert silence at the middle of the chosen gaps; f maps voice time -> ad time
    inserts = []                                # (voice time of the gap middle, seconds added)
    for k, need in MIN_GAP.items():
        gap = segs[k + 1][0] - segs[k][1]
        if need > gap:
            inserts.append(((segs[k][1] + segs[k + 1][0]) / 2, need - gap))
    inserts.sort()
    f = lambda t: t + sum(d for m, d in inserts if m <= t)
    q = lambda t: round(t * FPS) / FPS
    P = [f(s) for s, _ in segs]
    E = [f(e) for _, e in segs]
    total = q(E[-1] + END_HOLD)
    words = json.loads((HERE / "work/vo_words.json").read_text(encoding="utf-8"))

    def word_start(prefix, after):
        return f(next(w_["s"] for w_ in words if w_["s"] >= after and w_["t"].lower().startswith(prefix)))

    def word_end(prefix, after):
        for w_ in words:
            if w_["s"] >= after and w_["t"].lower().startswith(prefix):
                return f(w_["e"])
        raise KeyError(prefix)

    bound = lambda k: q(P[k] - 0.10)
    plan = [
        (C1, 0, 0.30), (FRZ, 3, None), (S2, 4, None), (C2, 5, (5.0, P[7])),
        (C3, 9, 0.10), (C4, 13, 0.30), (C5, 15, 2.50), (C6, 17, (1.30, P[18])),
        (C7, 20, (5.25, P[22] - 0.55)), (S8, 23, None),
    ]
    shots = []
    for i, (inp, k, ss) in enumerate(plan):
        t0 = 0.0 if i == 0 else (q(P[3]) if inp == FRZ else bound(k))
        if i + 1 < len(plan):
            nxt = plan[i + 1]
            t1 = q(P[3]) if nxt[0] == FRZ else bound(nxt[1])
        else:
            t1 = total
        if isinstance(ss, tuple):
            src_t, ad_t = ss
            ss = max(0.0, src_t - (ad_t - t0))
        shots.append(dict(inp=inp, t0=t0, t1=t1, ss=ss))
    for s in shots:
        if s["inp"] in CLIP_LEN:
            assert s["ss"] + 0.1 < CLIP_LEN[s["inp"]], s

    make_freeze(INPUT_FILES[shots[0]["inp"]], shots[0]["ss"] + shots[1]["t0"])
    make_minimap()

    # ------------------------------------------------ captions + HUD
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Montserrat,60,{WHITE},{WHITE},{BLACK},&H96000000,-1,0,0,0,100,100,0,0,1,4.5,2,5,200,200,0,1
Style: Title,Anton,150,{WHITE},{WHITE},{BLACK},&H96000000,0,0,0,0,100,100,2,0,1,7,4,5,40,40,0,1
Style: Kicker,Anton,62,{AMBER},{AMBER},{BLACK},&H96000000,0,0,0,0,100,100,6,0,1,4,2,5,40,40,0,1
Style: Obj,Bebas Neue,62,{AMBER},{AMBER},{BLACK},&H96000000,0,0,0,0,100,100,2,0,1,4,2,5,0,0,0,1
Style: Toast,Bebas Neue,56,{WHITE},{WHITE},&HB4101010,&H00000000,0,0,0,0,100,100,2,0,3,10,0,9,0,0,0,1
Style: Meter,Anton,50,{AMBER},{AMBER},{BLACK},&H96000000,0,0,0,0,100,100,6,0,1,3,2,9,0,0,0,1
Style: Draw,Arial,20,{AMBER},{AMBER},{BLACK},&H00000000,0,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Name,Anton,140,{WHITE},{WHITE},{BLACK},&H96000000,0,0,0,0,100,100,4,0,1,7,4,4,0,0,0,1
Style: Role,Bebas Neue,58,{AMBER},{AMBER},{BLACK},&H96000000,0,0,0,0,100,100,6,0,1,4,2,4,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    add = lambda layer, a, b, style, text: ev.append(f"Dialogue: {layer},{tc(a)},{tc(b)},{style},,0,0,0,,{text}")
    SUB_Y, TITLE_Y = 1185, 1000
    shot_end = lambda t: next(s["t1"] for s in shots if s["t0"] <= t + 0.05 < s["t1"])

    # subtitles (off where a title, list or banner already shows the words)
    groups = [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (13, 14), (15, 16), (17, 17), (18, 18), (19, 19),
              (20, 20), (21, 21)]
    for a, b in groups:
        text = " ".join(PHRASES[a:b + 1])
        end = min(P[b + 1] - 0.03, shot_end(P[a]))
        add(1, P[a], end, "Sub", f"{{\\pos(540,{SUB_Y})\\fad(60,60)}}{text}")

    def band(a, b, y, h=250, alpha="60"):
        add(0, a, b, "Draw", f"{{\\an7\\pos(0,{y - h // 2})\\1c&H000000&\\1a&H{alpha}&\\bord0\\shad0\\fad(120,160)\\p1}}"
                             f"m 0 0 l {W} 0 {W} {h} 0 {h}{{\\p0}}")

    # hook title, low over the bucket
    tA = P[2] - 0.05
    band(0.25, tA, 1250, 300)
    add(3, 0.25, tA, "Title", f"{{\\pos(540,1200)\\fs118\\fscx130\\fscy130\\t(0,120,\\fscx100\\fscy100)}}CEILING LEAKING.")
    add(3, P[1], tA, "Title", f"{{\\pos(540,1330)\\1c{RED}&\\fs150\\fscx170\\fscy170\\frz-4\\t(0,110,\\fscx100\\fscy100)}}AGAIN.")
    fz0, fz1 = shots[1]["t0"], shots[1]["t1"]
    add(4, fz0, fz1, "Name", "{\\pos(70,760)\\move(-300,760,70,760,0,160)}RAY")
    add(4, fz0 + 0.12, fz1, "Role", "{\\pos(78,860)\\fad(120,0)}HOMEOWNER")

    # STRESS meter
    SXP, SY = [721, 792, 863, 934, 1005], 345      # kept inside the freeze panel's ink rule
    add(5, 0.0, total, "Meter", "{\\pos(1038,268)}STRESS")
    star = star_path()
    slam = [0.10, 0.36, 0.62, 0.88, P[3]]
    # stars pop as each point lands (at the end of its phrase, so the sound never sits on the word)
    pops = [E[14], E[16], E[19], E[20], E[22]]
    # the long toasts go on two smaller lines so they stay off Ray's cap in the close-ups
    pop_text = ["{\\fs50}NO COMMISSION.\\NNO CLOSING COSTS.", "{\\fs50}LEAVE WHAT\\NYOU DON'T WANT", "SELLS AS-IS",
                "YOU PICK THE CLOSING DATE", None]
    order = [4, 3, 2, 1, 0]
    # once the meter is empty: a darker plate and light slot outlines, so "Empty." reads on the end card
    add(4, P[22], total, "Draw", "{\\an7\\pos(674,258)\\1c&H000000&\\1a&H40&\\bord0\\shad0\\fad(120,0)\\p1}"
                                 "m 0 0 l 378 0 378 134 0 134{\\p0}")
    for x in SXP:
        add(5, 0.0, P[22], "Draw", f"{{\\an5\\pos({x},{SY})\\1a&HFF&\\3c&H202020&\\bord3\\p1}}{star}{{\\p0}}")
        add(5, P[22], total, "Draw", f"{{\\an5\\pos({x},{SY})\\1a&HFF&\\3c&HE6E6E6&\\bord3\\p1}}{star}{{\\p0}}")
    for n, i in enumerate(order):
        x, on, off = SXP[i], slam[n], pops[n]
        add(6, on, off, "Draw", f"{{\\an5\\pos({x},{SY})\\fscx170\\fscy170\\t(0,140,\\fscx100\\fscy100)\\p1}}{star}{{\\p0}}")
        add(7, off, off + 0.40, "Draw", f"{{\\an5\\pos({x},{SY})\\1c&HFFFFFF&\\t(0,400,\\fscx260\\fscy260\\alpha&HFF&)\\p1}}{star}{{\\p0}}")
    for t in (P[3], P[3] + 0.3, P[3] + 0.6, P[4], P[5]):
        for x in SXP:
            add(8, t, t + 0.16, "Draw", f"{{\\an5\\pos({x},{SY})\\1c&HFFFFFF&\\bord3\\fad(0,120)\\p1}}{star}{{\\p0}}")

    def toast(a, b, text, y=420):
        add(6, a, b, "Toast", f"{{\\an9\\pos(1045,{y})\\fad(80,150)\\move(1110,{y},1045,{y},0,140)}}{text}")
    toast(P[4], bound(9), "+ REPAIR QUOTES")
    toast(P[5], bound(9), "+ WEEKENDS LOST", 505)
    for n, txt in enumerate(pop_text):
        if txt:
            toast(pops[n], min(pops[n + 1], pops[n] + 1.9), txt)

    # objective line (bottom, game style)
    OX, OY = 540, 1305

    def obj(a, b, text, strike_at=None):
        if strike_at is None:
            add(5, a, b, "Obj", f"{{\\pos({OX},{OY})\\fad(100,120)}}{text}")
        else:
            add(5, a, strike_at, "Obj", f"{{\\pos({OX},{OY})\\fad(100,0)}}{text}")
            add(5, strike_at, b, "Obj", f"{{\\pos({OX},{OY})\\s1\\1c&H9A9A9A&\\fad(0,120)}}{text}")
    obj(P[7], bound(9), "OBJECTIVE: FIX IT ALL. THEN LIST IT.")
    obj(P[17], bound(20), "FIX IT ALL. THEN LIST IT.", strike_at=P[18])

    # "There's another way out." -> the mission title
    m0, m1 = P[9], P[10] - 0.05
    band(m0 - 0.05, m1, TITLE_Y + 20, 290)
    add(3, m0, m1, "Kicker", f"{{\\pos(540,{TITLE_Y - 70})\\fad(80,120)}}NEW MISSION")
    add(3, m0 + 0.15, m1, "Title", f"{{\\pos(540,{TITLE_Y + 40})\\fs128\\fscx140\\fscy140\\t(0,130,\\fscx100\\fscy100)\\fad(0,120)}}SELL IT AS-IS")

    # "Listing means repairs, cleanup, commission and closing costs." -> red cost list, struck on "None of that."
    L0, strike = P[10], P[14]
    list_end = E[14] + 0.35
    # the header gives way to the "This cash offer? None of that." subtitle on the same line
    add(4, L0, P[13] - 0.03, "Obj", f"{{\\pos(540,{SUB_Y})\\1c&HFFFFFF&\\fs76\\fad(80,0)}}LISTING MEANS:")
    items = [("- REPAIRS", P[10] + 0.55), ("- CLEANUP", P[11]), ("- COMMISSION", P[12]),
             ("- CLOSING COSTS", word_start("closing", segs[12][0]))]
    for n, (txt, t) in enumerate(items):
        y = 1292 + n * 70
        add(4, t, strike, "Obj", f"{{\\pos(540,{y})\\1c{REDLIST}&\\fs74\\fscx150\\fscy150\\t(0,110,\\fscx100\\fscy100)}}{txt}")
        add(4, strike, list_end, "Obj", f"{{\\pos(540,{y})\\1c&H9A9A9A&\\s1\\fs74\\fad(0,150)}}{txt}")

    # MISSION COMPLETE on "Empty.", then the end card on "Ask"
    e0 = shots[-1]["t0"]                        # end card text starts on the cut; the banner is gone by then
    mc0, mc1 = P[22], e0
    band(mc0, mc1, TITLE_Y, 260, "50")
    add(9, mc0, mc1, "Title", f"{{\\pos(540,{TITLE_Y})\\1c{AMBER}&\\fs140\\fscx160\\fscy160\\t(0,150,\\fscx100\\fscy100)\\fad(0,150)}}MISSION COMPLETE")
    band(e0, total, 1080, 420, "58")
    add(9, e0, total, "Kicker", "{\\pos(540,925)\\fad(120,0)}NEW OBJECTIVE")
    add(9, e0, total, "Title", "{\\pos(540,1030)\\fs104\\fad(120,0)}ASK FOR A")
    add(9, e0, total, "Title", f"{{\\pos(540,1140)\\fs104\\1c{AMBER}&\\fad(120,0)}}CASH OFFER")
    add(9, P[24], total, "Sub", "{\\pos(540,1250)\\fs58\\fad(100,0)}No obligation.")
    (HERE / "work/caps.ass").write_text(head + "\n".join(ev) + "\n", encoding="utf-8")

    # ------------------------------------------------ video graph
    vp, labels = [], []
    for i, s in enumerate(shots):
        d = s["t1"] - s["t0"]
        n = int(round(d * FPS))
        if s["inp"] == FRZ:
            vp.append(f"[{FRZ}:v]fps={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,scale={W}:{H},setsar=1,format=yuv420p[b{i}]")
        elif s["inp"] in STILLS:
            vp.append(f"[{s['inp']}:v]fps={FPS},trim=end_frame={n},setpts=PTS-STARTPTS,"
                      f"scale={4 * W}:-2:flags=lanczos,crop={4 * W}:{4 * H},"   # 4x so the push-in doesn't shimmer
                      f"zoompan=z='1+0.07*on/{n}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s={W}x{H}:fps={FPS},"
                      f"setsar=1,format=yuv420p[b{i}]")
        else:
            src_d = min(d, CLIP_LEN[s["inp"]] - s["ss"])
            vp.append(f"[{s['inp']}:v]trim=start={s['ss']:.3f}:end={s['ss'] + src_d:.3f},setpts=PTS-STARTPTS,fps={FPS},"
                      f"scale={W}:{H}:flags=lanczos,setsar=1,tpad=stop_mode=clone:stop_duration=3,"
                      f"trim=end_frame={n},setpts=PTS-STARTPTS,format=yuv420p[b{i}]")
        labels.append(f"[b{i}]")
    vp.append("".join(labels) + f"concat=n={len(shots)}:v=1:a=0[cat]")
    vp.append(f"[{MAP}:v]fps={FPS},format=rgba[mm]")
    # the minimap drops out for the porch push-in (C3), where it would sit on Ray's cap
    c3 = next(i for i, s in enumerate(shots) if s["inp"] == C3)
    vp.append(f"[cat][mm]overlay=x=34:y=262:shortest=0:eof_action=repeat:"
              f"enable='not(between(t,{shots[c3]['t0'] - 0.01:.3f},{shots[c3 + 1]['t0'] - 0.01:.3f}))',"
              f"ass='{ff_path(HERE / 'work/caps.ass')}':fontsdir='{ff_path(FONTS_DIR)}',"
              f"trim=end_frame={int(round(total * FPS))},format=yuv420p[vout]")
    (HERE / "work/video_graph.txt").write_text(";\n".join(vp), encoding="utf-8")

    # ------------------------------------------------ audio graph
    ap, mix = [], []
    # voice: split at the gap middles that get stretched, pad each piece with the added silence
    cuts = [0.0] + [m for m, _ in inserts] + [vo_dur]
    adds = [d for _, d in inserts] + [0.0]
    for k in range(len(cuts) - 1):
        a, b = cuts[k], cuts[k + 1]
        ap.append(f"[{VO}:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,"
                  f"aformat=sample_rates=48000:channel_layouts=stereo,apad=pad_dur={adds[k]:.3f}[v{k}]")
    ap.append("".join(f"[v{k}]" for k in range(len(cuts) - 1)) + f"concat=n={len(cuts) - 1}:v=0:a=1,"
              f"apad=whole_dur={total:.3f}[vo]")
    mix.append("[vo]")

    amb = {C1: "if(between(t,0.45,1.4),0.12,0.30)", C2: 0.0, C3: 0.20, C4: 0.16, C5: 0.16, C6: 0.20, C7: 0.16}
    for i, s in enumerate(shots):
        vol = amb.get(s["inp"], 0)
        if not vol:
            continue
        d = s["t1"] - s["t0"]
        src_d = min(d, CLIP_LEN[s["inp"]] - s["ss"])
        ms = int(round(s["t0"] * 1000))
        gain = f"volume='{vol}':eval=frame" if isinstance(vol, str) else f"volume={vol}"
        ap.append(f"[{s['inp']}:a]atrim=start={s['ss']:.3f}:end={s['ss'] + src_d:.3f},asetpts=PTS-STARTPTS,"
                  f"aformat=sample_rates=48000:channel_layouts=stereo,{gain},afade=t=in:d=0.03,"
                  f"afade=t=out:st={max(src_d - 0.06, 0):.3f}:d=0.06,adelay={ms}|{ms}[amb{i}]")
        mix.append(f"[amb{i}]")

    # sound effects: each one lined up so its attack (after any lead-in silence) hits the moment
    fx = []                                     # (input, filter chain, output tag)

    def gsfx(inp, t, vol, dur=None, env=None):
        st = SFX_START.get(inp, 0.0)            # skip a long lead-in so the hit lands on the moment
        ms = int(round(max(0.0, t - (SFX_ONSET[inp] - st)) * 1000))
        chain = f"atrim=start={st:.3f}:end={st + dur:.3f}," if dur else (f"atrim=start={st:.3f}," if st else "")
        chain += "asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
        chain += f"volume='{env}':eval=frame" if env else f"volume={vol}"
        if dur:
            chain += f",afade=t=out:st={max(dur - 0.12, 0):.3f}:d=0.12"
        tag = f"g{len(fx)}"
        fx.append((inp, chain + f",adelay={ms}|{ms}", tag))
        mix.append(f"[{tag}]")

    for n, t in enumerate(slam):
        gsfx(SX_MENU, t, 0.40 if n == 4 else 0.30, dur=0.35)
    for t in (P[4], P[5], P[7]):
        gsfx(SX_NOTIFY, t, 0.40)
    for n, t in enumerate(pops[:4]):
        gsfx(SX_PICKUP, t, 0.85, dur=0.9)
    gsfx(SX_PHONE, P[9], 0.45)                 # NEW MISSION
    # closing jingle after "Empty.": full level in the stretched gap, then ducked under the call to action
    lead = E[22] - SFX_ONSET[SX_MISSION]
    duck_at = P[23] - lead
    gsfx(SX_MISSION, E[22], None, env=f"if(lt(t,{duck_at - 0.15:.3f}),0.75,0.75-0.57*min(1,(t-{duck_at - 0.15:.3f})/0.25))")
    gsfx(SX_PHONE, e0 + 0.02, 0.35)            # NEW OBJECTIVE
    # an input used more than once goes through asplit, one branch per use
    for inp in sorted({i for i, _, _ in fx}):
        mine = [(c, t) for i, c, t in fx if i == inp]
        if len(mine) == 1:
            ap.append(f"[{inp}:a]{mine[0][0]}[{mine[0][1]}]")
        else:
            ap.append(f"[{inp}:a]asplit={len(mine)}" + "".join(f"[s{inp}_{j}]" for j in range(len(mine))))
            ap.extend(f"[s{inp}_{j}]{c}[{t}]" for j, (c, t) in enumerate(mine))
    ap.append("".join(mix) + f"amix=inputs={len(mix)}:duration=first:normalize=0,atrim=end={total:.3f},"
              f"afade=t=out:st={total - 0.5:.3f}:d=0.5[aout]")
    (HERE / "work/audio_graph.txt").write_text(";\n".join(ap), encoding="utf-8")

    args = []
    for k, fn in enumerate(INPUT_FILES):
        if k in STILLS:
            args += ["-loop", "1", "-framerate", str(FPS)]
        args += ["-i", fn]
    (HERE / "work/inputs.txt").write_text("\n".join(args), encoding="utf-8", newline="\n")
    (HERE / "work/total.txt").write_text(f"{total:.3f}", encoding="utf-8", newline="\n")
    print(f"voice {vo_dur:.2f}s + {sum(d for _, d in inserts):.2f}s of added pauses, total {total:.3f}s")
    for s in shots:
        print(f"  in{s['inp']:>2} {s['t0']:6.3f}-{s['t1']:6.3f} ({s['t1'] - s['t0']:.2f}s) src {s['ss']}")
    print("phrase starts:", " ".join(f"{p:.2f}" for p in P))
    print("pops:", " ".join(f"{p:.2f}" for p in pops))


if __name__ == "__main__":
    build()
