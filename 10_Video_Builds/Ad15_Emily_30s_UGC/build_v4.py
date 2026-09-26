"""Ad 15, clips 1 + 2, v4: v3 with object-only B-roll matched to each spoken item (no other people).

1. Merge clip1_v1 + clip2_v1 into one take (Ad15_clips1-2_merged.mov, PCM audio, 16.000 s).
2. Cut that take into 7 scenes at sentence boundaries. The voice runs untouched from 0 to 15.75 s:
   no pause is deleted, so the rhythm is the one she spoke (REEL-PROCESS: cap pauses, don't delete).
3. Face scenes alternate with real moving stock video. Punch-ins: wide, tight, mid.
4. Audio: voice + original synthesized bed ducked under it + a few sound effects, two-pass loudnorm.
5. Captions: dynamic_captions_3click (yellow-pop), fed a corrected word SRT, in the lower band.

v2 froze Emily after 4.33 s: trim=start_frame without setpts made ffmpeg pad the front of each
face scene with copies of its first frame. Every face scene is now checked against an independent seek.

Run: python3 build_v3.py
"""
import difflib, json, os, re, subprocess
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD = f"{ROOT}/10_Video_Builds/Ad15_Emily_30s_UGC"
STOCKV = f"{ROOT}/07_Assets/Stock_Video"
AUD = f"{ROOT}/07_Assets/Audio"
MERGED = f"{BUILD}/Ad15_clips1-2_merged.mov"
BASE = f"{BUILD}/v4_base.mp4"
OUT = f"{ROOT}/13_Generated/videos/Ad15_clips1-2_v4.mp4"
DYNCAP = os.path.expanduser("~/.claude/skills/dynamic_captions_3click/scripts/dyncap.py")
FPS, W, H = 24, 1080, 1920
END = 378  # 15.750 s: last word ends 15.346 s, then a short hold
FACE_C = (540, 830)

SCRIPT = ("Inherited a house? Don't clean it out yet. Closet's still full. Hours away. "
          "Scared a cash buyer will lowball you? Family can't agree. Truth? Cash offers usually come in "
          "lower than listing. Ours too. Listing usually means repairs, cleanout, commission, closing costs.")

# (start_frame, end_frame, picture). Frames are on the merged take, which is also the output timeline.
# Every boundary sits inside a measured silence (silencedetect -35 dB) or between two words.
SCENES = [
    (0, 58, dict(kind="F", z=(1.00, 1.05))),                        # Inherited a house? Don't clean it out yet.
    (58, 90, dict(kind="V", src="closet_8844337", t=1.0)),          # Closet's still full.   (clothes packed tight)
    (90, 114, dict(kind="V", src="leak_4159571", t=3.0)),           # Hours away.            (ceiling leaking, nobody home)
    (114, 162, dict(kind="F", z=(1.28, 1.30))),                     # Scared a cash buyer will lowball you?
    (162, 192, dict(kind="V", src="house_32116905", t=2.0)),        # Family can't agree.    (the house, sitting)
    (192, 290, dict(kind="F", z=(1.12, 1.16))),                     # Truth? ... lower than listing. Ours too.
    (290, 312, dict(kind="V", src="forsale_7578271", t=8.5)),       # Listing usually means  (FOR SALE sign)
    (312, 326, dict(kind="V", src="roof_11629980", t=2.5)),         # repairs,               (collapsed roof)
    (326, 337, dict(kind="V", src="junk_35421432", t=3.0)),         # cleanout,              (storeroom full of old stuff)
    (337, END, dict(kind="V", src="contract_7841865", t=1.0)),      # commission, closing costs. (contract + pens)
]

# (file, start_s in output, trim_s, loudness target LUFS)
SFX = [
    ("Sound Effects/Swooshes/swoosh.mp3", 58 / FPS - 0.20, 1.35, -30),
    ("Sound Effects/Swooshes/swoosh.mp3", 162 / FPS - 0.20, 1.35, -31),
    ("Sound Effects/Swooshes/swoosh.mp3", 290 / FPS - 0.20, 1.35, -31),
    ("Thick Liquid Pouring Sound Effect.mp3", 90 / FPS, 1.0, -33),
    ("Sound Effects/PAPER SFX/Cardboard Shuffle 01.wav", 326 / FPS, 0.46, -32),
    ("Sound Effects/Actions/Audiio_ManilaPaperCrinkling1.wav", 337 / FPS, 1.6, -34),
]


def ff(*a):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)


def frames(args, n):
    raw = subprocess.run(["ffmpeg", "-v", "error", *args, "-fps_mode", "passthrough",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    assert len(fr) >= n, (args, len(fr), n)
    return fr[:n]


def crop_zoom(arr, cx, cy, z):
    im = Image.fromarray(arr)
    cw, ch = W / z, H / z
    x0 = min(max(cx - cw / 2, 0), W - cw)
    y0 = min(max(cy - ch / 2, 0), H - ch)
    return im.transform((W, H), Image.EXTENT, (x0, y0, x0 + cw, y0 + ch), Image.BICUBIC)


def face_scene(a, b, p):
    fr = frames(["-i", MERGED, "-vf", f"trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,"
                 "scale=in_color_matrix=bt709,format=rgb24"], b - a)
    # guard: each checked frame must equal an independent seek to the same source frame
    for k in (0, (b - a) // 2, b - a - 1):
        ref = frames(["-ss", f"{(a + k) / FPS:.6f}", "-i", MERGED, "-frames:v", "1", "-vf",
                      "scale=in_color_matrix=bt709,format=rgb24"], 1)[0]
        d = np.abs(fr[k].astype(np.int16) - ref.astype(np.int16)).mean()
        assert d < 1.5, f"face frame {a + k} does not match its source (diff {d:.2f})"
    moving = np.abs(fr[0].astype(np.int16) - fr[-1].astype(np.int16)).mean()
    assert moving > 1.0, f"face scene {a}-{b} looks frozen ({moving:.2f})"
    n = b - a
    return [crop_zoom(f, *FACE_C, p["z"][0] + (p["z"][1] - p["z"][0]) * k / max(n - 1, 1)) for k, f in enumerate(fr)]


def video_scene(a, b, p):
    """Every source frame is kept (every 2nd at 50-60 fps) and re-timed to 24 fps.
    fps=24 on a 30 or 60 fps pan drops frames unevenly and judders (caught on v4's closet shot)."""
    n = b - a
    src = f"{STOCKV}/{p['src']}.mp4"
    num, den = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                               "stream=r_frame_rate", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split("/")
    step = max(1, round(int(num) / int(den) / 30))
    vf = (f"select='not(mod(n\\,{step}))',setpts=N/({FPS}*TB),scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos:in_color_matrix=bt709,"
          f"crop={W}:{H}" + (f",{p['grade']}" if p.get("grade") else "") + ",format=rgb24")
    fr = frames(["-ss", str(p["t"]), "-i", src, "-frames:v", str(n), "-vf", vf], n)
    return [crop_zoom(f, W / 2, H / 2, 1.0 + 0.04 * k / max(n - 1, 1)) for k, f in enumerate(fr)]


def build_picture(path):
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
                            "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high", "-level", "4.1",
                            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", path],
                           stdin=subprocess.PIPE)
    for a, b, p in SCENES:
        for im in (face_scene if p["kind"] == "F" else video_scene)(a, b, p):
            enc.stdin.write(im.tobytes())
        print(f"  {a / FPS:6.3f}-{b / FPS:6.3f}  {p.get('src', 'face')}")
    enc.stdin.close()
    assert enc.wait() == 0


def build_audio(path):
    voice, music = f"{BUILD}/v4_voice.wav", f"{BUILD}/v4_music.wav"
    ff("-i", MERGED, "-vn", "-af", f"atrim=0:{END / FPS:.6f}", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", voice)
    subprocess.run(["python3", f"{BUILD}/music_v3.py", f"{END / FPS:.6f}", music], check=True)
    ins = ["-i", voice, "-i", music]
    g = ["[0:a]asplit=2[vo][sc]",
         "[1:a]volume=-23dB[mu]",
         "[mu][sc]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=350[md]"]
    labels = ["[vo]", "[md]"]
    for i, (f, st, ln, lufs) in enumerate(SFX):
        ins += ["-i", f"{AUD}/{f}"]
        ms = int(round(st * 1000))
        g.append(f"[{i + 2}:a]atrim=0:{ln},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                 f"loudnorm=I={lufs}:TP=-6,afade=t=out:st={ln - 0.25}:d=0.25,adelay={ms}|{ms}[s{i}]")
        labels.append(f"[s{i}]")
    g.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first[mix]")
    mix = f"{BUILD}/v4_mix.wav"
    ff(*ins, "-filter_complex", ";".join(g), "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s16le", mix)
    ln = "loudnorm=I=-14:TP=-1.5:LRA=11"
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", mix, "-af", ln + ":print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    ff("-i", mix, "-af", f"{ln}:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
       f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true", "-ar", "48000", "-c:a",
       "pcm_s16le", path)
    return voice


def word_srt(voice, path):
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel("small", device="cpu", compute_type="int8").transcribe(
        voice, language="en", word_timestamps=True, vad_filter=False, condition_on_previous_text=False)
    heard = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    norm = lambda s: re.sub(r"[^a-z]", "", s.lower())
    script = SCRIPT.split()
    hs = [norm(h[0]) for h in heard]
    ss = [norm(w) for w in script]
    out = [None] * len(script)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ss, hs, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                out[i1 + k] = heard[j1 + k][1:]
        elif op == "replace":  # e.g. "cleanout" heard as "clean" + "out": spread the span
            t0, t1 = heard[j1][1], heard[j2 - 1][2]
            for k in range(i2 - i1):
                out[i1 + k] = (t0 + (t1 - t0) * k / (i2 - i1), t0 + (t1 - t0) * (k + 1) / (i2 - i1))
    for k in range(len(out)):  # any word whisper missed: interpolate between neighbours
        if out[k] is None:
            prev = next((out[i][1] for i in range(k - 1, -1, -1) if out[i]), 0.0)
            nxt = next((out[i][0] for i in range(k + 1, len(out)) if out[i]), prev + 0.3)
            out[k] = (prev, nxt)
    ts = lambda v: f"{int(v // 3600):02d}:{int(v % 3600 // 60):02d}:{int(v % 60):02d},{int(round(v % 1 * 1000)) % 1000:03d}"
    with open(path, "w") as fh:
        for i, (w, (a, b)) in enumerate(zip(script, out), 1):
            fh.write(f"{i}\n{ts(a)} --> {ts(b)}\n{w}\n\n")
    return len(script), len(heard)


def main():
    if not os.path.exists(MERGED):
        ff("-i", f"{BUILD}/clip1_v1.mp4", "-i", f"{BUILD}/clip2_v1.mp4", "-filter_complex",
           "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]",
           "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", MERGED)
    assert SCENES[0][0] == 0 and SCENES[-1][1] == END
    assert all(SCENES[i][1] == SCENES[i + 1][0] for i in range(len(SCENES) - 1))
    pic = f"{BUILD}/v4_picture.mp4"
    print("picture:"); build_picture(pic)
    audio = f"{BUILD}/v4_audio.wav"
    voice = build_audio(audio)
    ff("-i", pic, "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-t", f"{END / FPS:.6f}", "-movflags", "+faststart", BASE)
    srt = f"{BUILD}/v4_words.srt"
    print("srt words / heard:", word_srt(voice, srt))
    subprocess.run(["python3", DYNCAP, BASE, "-o", OUT, "--srt-in", srt, "--top", "0.68", "--bottom", "0.78"], check=True)
    print("->", OUT)


if __name__ == "__main__":
    main()
