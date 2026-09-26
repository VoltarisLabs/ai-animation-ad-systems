"""Ad 15, full ad, final v1: the v4 cut of clips 1 + 2, then clip 3, which closes loops C, B and A.

Clip 3 is the user's own generation (2026-09-26, another model, not Kie):
13_Generated/videos/Woman_recording_car_selfie_video_20260926041442.mp4, 8.000 s, 24 fps.
She says: "Lower isn't everything. We buy as is, no fees. Think it's a lowball? Just say no. Don't clean it out."

1. Merge: frames 0-378 of Ad15_clips1-2_merged.mov (exactly the v4 timeline) + clip 3 frames 7-186.
   Clip 3 opens with 0.365 s of silence. Starting at its frame 7 leaves a 0.477 s pause after
   "closing costs." (REEL-PROCESS cap after a sentence: 0.46 s). It ends 0.67 s after "out." on her smile.
2. Clip 3 opens with her glancing off-lens and blinking through "Lower isn't" (output frames 378-395).
   The contract shot runs on under those words; her face comes up on "everything." (frame 396, eyes back
   on the lens) and the gutted ceiling lands on "as-is". The voice is never cut; only the picture changes.
3. Same finish as v4: object-only B-roll, original music bed ducked under the voice, a few SFX,
   two-pass loudnorm to -14 LUFS, dynamic_captions_3click from a corrected word SRT, kept off the face.

Run: python3 build_final_v1.py
"""
import difflib, json, os, re, subprocess
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD = f"{ROOT}/10_Video_Builds/Ad15_Emily_30s_UGC"
STOCKV = f"{ROOT}/07_Assets/Stock_Video"
AUD = f"{ROOT}/07_Assets/Audio"
M12 = f"{BUILD}/Ad15_clips1-2_merged.mov"
CLIP3 = f"{ROOT}/13_Generated/videos/Woman_recording_car_selfie_video_20260926041442.mp4"
MERGED = f"{BUILD}/Ad15_full_merged.mov"
BASE = f"{BUILD}/final_v1_base.mp4"
OUT = f"{ROOT}/13_Generated/videos/Ad15_final_v1.mp4"
DYNCAP = os.path.expanduser("~/.claude/skills/dynamic_captions_3click/scripts/dyncap.py")
FPS, W, H = 24, 1080, 1920
V4_END = 378          # 15.750 s: end of the clips 1 + 2 part, as cut in v4
C3_IN, C3_OUT = 7, 186  # clip 3 frames used: 0.292 s to 7.750 s
END = V4_END + C3_OUT - C3_IN  # 557 frames = 23.208 s
FACE_C = (540, 830)

SCRIPT = ("Inherited a house? Don't clean it out yet. Closet's still full. Hours away. "
          "Scared a cash buyer will lowball you? Family can't agree. Truth? Cash offers usually come in "
          "lower than listing. Ours too. Listing usually means repairs, cleanout, commission, closing costs. "
          "Lower isn't everything. We buy as-is, no fees. Think it's a lowball? Just say no. Don't clean it out.")

# (start_frame, end_frame, picture). Frames are on the merged take, which is also the output timeline.
SCENES = [
    (0, 58, dict(kind="F", z=(1.00, 1.05))),                        # Inherited a house? Don't clean it out yet.
    (58, 90, dict(kind="V", src="closet_8844337", t=1.0)),          # Closet's still full.
    (90, 114, dict(kind="V", src="leak_4159571", t=3.0)),           # Hours away.
    (114, 162, dict(kind="F", z=(1.28, 1.30))),                     # Scared a cash buyer will lowball you?
    (162, 192, dict(kind="V", src="house_32116905", t=2.0)),        # Family can't agree.
    (192, 290, dict(kind="F", z=(1.12, 1.16))),                     # Truth? ... lower than listing. Ours too.
    (290, 312, dict(kind="V", src="forsale_7578271", t=8.5)),       # Listing usually means
    (312, 326, dict(kind="V", src="roof_11629980", t=2.5)),         # repairs,
    (326, 337, dict(kind="V", src="junk_35421432", t=3.0)),         # cleanout,
    (337, 396, dict(kind="V", src="contract_7841865", t=1.0)),      # commission, closing costs. Lower isn't
    (396, 425, dict(kind="F", z=(1.18, 1.22))),                     # everything. We buy
    (425, 470, dict(kind="V", src="ceiling_4882745", t=8.5)),       # as-is, no fees.                (gutted ceiling)
    (470, END, dict(kind="F", z=(1.05, 1.16))),                     # Think it's a lowball? Just say no. Don't clean it out.
]

# (file, start_s in output, trim_s, loudness target LUFS)
SFX = [
    ("Sound Effects/Swooshes/swoosh.mp3", 58 / FPS - 0.20, 1.35, -30),
    ("Sound Effects/Swooshes/swoosh.mp3", 162 / FPS - 0.20, 1.35, -31),
    ("Sound Effects/Swooshes/swoosh.mp3", 290 / FPS - 0.20, 1.35, -31),
    ("Thick Liquid Pouring Sound Effect.mp3", 90 / FPS, 1.0, -33),
    ("Sound Effects/PAPER SFX/Cardboard Shuffle 01.wav", 326 / FPS, 0.46, -32),
    ("Sound Effects/Actions/Audiio_ManilaPaperCrinkling1.wav", 337 / FPS, 1.6, -34),
    ("Sound Effects/Swooshes/swoosh.mp3", 425 / FPS - 0.20, 1.35, -31),
    ("Sound Effects/ambient/misc/creak3.wav", 425 / FPS + 0.10, 1.85, -34),
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


def merge():
    """v4's first 378 frames untouched, then clip 3 from frame 7. Audio joined as PCM with 20 ms fades."""
    a0 = V4_END / FPS
    c3a, c3b = C3_IN / FPS, C3_OUT / FPS
    ff("-i", M12, "-i", CLIP3, "-filter_complex",
       f"[0:v]trim=end_frame={V4_END},setpts=PTS-STARTPTS[v0];"
       f"[0:a]atrim=end={a0:.6f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
       f"afade=t=out:st={a0 - 0.02:.6f}:d=0.02[a0];"
       f"[1:v]trim=start_frame={C3_IN}:end_frame={C3_OUT},setpts=PTS-STARTPTS[v1];"
       f"[1:a]atrim=start={c3a:.6f}:end={c3b:.6f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
       f"afade=t=in:d=0.02[a1];"
       "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
       "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-pix_fmt", "yuv420p",
       "-c:a", "pcm_s16le", MERGED)
    # guard: the join must land exactly on v4's last frame and on clip 3's frame 7
    for src, t, k in ((M12, (V4_END - 1) / FPS, V4_END - 1), (CLIP3, C3_IN / FPS, V4_END), (CLIP3, (C3_OUT - 1) / FPS, END - 1)):
        ref = frames(["-ss", f"{t:.6f}", "-i", src, "-frames:v", "1", "-vf", "scale=in_color_matrix=bt709,format=rgb24"], 1)[0]
        got = frames(["-ss", f"{k / FPS:.6f}", "-i", MERGED, "-frames:v", "1", "-vf", "scale=in_color_matrix=bt709,format=rgb24"], 1)[0]
        d = np.abs(ref.astype(np.int16) - got.astype(np.int16)).mean()
        assert d < 2.0, f"merged frame {k} does not match {os.path.basename(src)} @ {t:.3f}s (diff {d:.2f})"
        print(f"  join check frame {k}: diff {d:.2f}")


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
    voice, music = f"{BUILD}/final_v1_voice.wav", f"{BUILD}/final_v1_music.wav"
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
    mix = f"{BUILD}/final_v1_mix.wav"
    ff(*ins, "-filter_complex", ";".join(g), "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s16le", mix)
    ln = "loudnorm=I=-14:TP=-2.0:LRA=11"
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
        elif op == "replace":  # e.g. "lowball" heard as "low" + "ball": spread the span
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
    assert SCENES[0][0] == 0 and SCENES[-1][1] == END
    assert all(SCENES[i][1] == SCENES[i + 1][0] for i in range(len(SCENES) - 1))
    print("merge:"); merge()
    pic = f"{BUILD}/final_v1_picture.mp4"
    print("picture:"); build_picture(pic)
    audio = f"{BUILD}/final_v1_audio.wav"
    voice = build_audio(audio)
    ff("-i", pic, "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-t", f"{END / FPS:.6f}", "-movflags", "+faststart", BASE)
    srt = f"{BUILD}/final_v1_words.srt"
    print("srt words / heard:", word_srt(voice, srt))
    subprocess.run(["python3", DYNCAP, BASE, "-o", OUT, "--srt-in", srt, "--top", "0.68", "--bottom", "0.78"], check=True)
    print("->", OUT)


if __name__ == "__main__":
    main()
