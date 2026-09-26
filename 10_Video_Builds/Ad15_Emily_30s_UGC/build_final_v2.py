"""Ad 15, full ad, final v2: final v1 with the sound brought up. Picture, voice and captions are unchanged.

The user said v1 "doesn't have any sounds". Measured on v1 after the master: voice -14.9 dB RMS, music -32.8 dB
(18 dB under the voice) and the SFX 8-18 dB under the voice, mostly on top of speech, so only her voice came through.

The house rule from the earlier reels (Notes/reel-system/addmusic.py, the level the user approved):
  bed mean_volume sits 4.8 dB under the voice's mean_volume, solved per video, not a fixed multiplier
  duck threshold 0.06 / ratio 4 / 15 ms / 350 ms (music dips only while she talks)
  +5.5 dB intro lift decaying to 0 dB by 2.5 s, so the bed is audible on frame 0
SFX: 2-11 dB louder than in v1, about 5 dB under the voice where they land on speech.

Run: python3 build_final_v2.py   (needs final_v1_picture.mp4, final_v1_voice.wav and final_v1_words.srt from v1)
"""
import json, os, re, subprocess
import build_final_v1 as v1

BUILD, AUD, FPS, END = v1.BUILD, v1.AUD, v1.FPS, v1.END
PIC = f"{BUILD}/final_v1_picture.mp4"
VOICE = f"{BUILD}/final_v1_voice.wav"
SRT = f"{BUILD}/final_v1_words.srt"
BASE = f"{BUILD}/final_v2_base.mp4"
OUT = f"{v1.ROOT}/13_Generated/videos/Ad15_final_v2.mp4"
GAP = 4.8
DUCK = "sidechaincompress=threshold=0.06:ratio=4:attack=15:release=350:makeup=1"

# (file, start_s in output, trim_s, loudness target LUFS). Same hits as v1, 2-11 dB louder.
# At voice level the 11.88 s swoosh masked "Listing" (heard as "Lifting"), so the swooshes and creak sit ~5 dB under her.
SFX = [
    ("Sound Effects/Swooshes/swoosh.mp3", 58 / FPS - 0.20, 1.35, -28),
    ("Sound Effects/Swooshes/swoosh.mp3", 162 / FPS - 0.20, 1.35, -29),
    # only the swoosh's loud middle (0.35-0.75 s), inside the gap between "too." (ends 11.84) and "Listing" (12.22)
    ("Sound Effects/Swooshes/swoosh.mp3", 11.84, 0.40, -27, dict(ss=0.35, fin=0.03, fout=0.12)),
    ("Thick Liquid Pouring Sound Effect.mp3", 90 / FPS, 1.0, -26),
    ("Sound Effects/PAPER SFX/Cardboard Shuffle 01.wav", 326 / FPS, 0.46, -23),
    ("Sound Effects/Actions/Audiio_ManilaPaperCrinkling1.wav", 337 / FPS, 1.6, -27),
    ("Sound Effects/Swooshes/swoosh.mp3", 425 / FPS - 0.20, 1.35, -29),
    ("Sound Effects/ambient/misc/creak3.wav", 425 / FPS + 0.10, 1.85, -32),
]


def mean_db(path):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume:\s*(-?[\d.]+) dB", e).group(1))


def music_chain(vol):
    lift = f"{vol:.5f}*(1+0.884*max(0\\,(2.5-t)/2.5))"  # +5.5 dB at t=0, flat from 2.5 s
    return (f"[1:a]volume=volume='{lift}':eval=frame[mu];[0:a]asplit=2[vo][sc];[mu][sc]{DUCK}[md]")


def build_audio(path, music):
    voice_db = mean_db(VOICE)
    target = voice_db - GAP
    stem = f"{BUILD}/final_v2_music_ducked.wav"
    vol = 0.3
    for _ in range(5):  # solve the multiplier: the ducked bed's mean lands 4.8 dB under the voice
        v1.ff("-i", VOICE, "-i", music, "-filter_complex", music_chain(vol) + ";[vo]anullsink",
              "-map", "[md]", "-c:a", "pcm_s16le", stem)
        bed = mean_db(stem)
        print(f"  music vol {vol:.4f} -> bed {bed:.1f} dB (voice {voice_db:.1f}, target {target:.1f})")
        if abs(bed - target) < 0.1:
            break
        vol *= 10 ** ((target - bed) / 20)
    ins = ["-i", VOICE, "-i", music]
    g = [music_chain(vol)]
    labels = ["[vo]", "[md]"]
    for i, (f, st, ln, lufs, *opt) in enumerate(SFX):
        o = opt[0] if opt else {}
        ss, fout = o.get("ss", 0.0), o.get("fout", 0.25)
        fin = f",afade=t=in:d={o['fin']}" if o.get("fin") else ""
        ins += ["-i", f"{AUD}/{f}"]
        ms = int(round(st * 1000))
        g.append(f"[{i + 2}:a]atrim={ss}:{ss + ln},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                 f"loudnorm=I={lufs}:TP=-3{fin},afade=t=out:st={ln - fout}:d={fout},adelay={ms}|{ms}[s{i}]")
        labels.append(f"[s{i}]")
    g.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first:dropout_transition=0[mix]")
    mix = f"{BUILD}/final_v2_mix.wav"
    v1.ff(*ins, "-filter_complex", ";".join(g), "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s16le", mix)
    ln = "loudnorm=I=-14:TP=-2.0:LRA=11"
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", mix, "-af", ln + ":print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    v1.ff("-i", mix, "-af", f"{ln}:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true", "-ar", "48000", "-c:a",
          "pcm_s16le", path)
    return vol


def main():
    for p in (PIC, VOICE, SRT):
        assert os.path.exists(p), f"missing v1 file: {p}"
    music = f"{BUILD}/final_v2_music.wav"
    subprocess.run(["python3", f"{BUILD}/music_v3.py", f"{END / FPS:.6f}", music], check=True)
    audio = f"{BUILD}/final_v2_audio.wav"
    vol = build_audio(audio, music)
    v1.ff("-i", PIC, "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
          "-t", f"{END / FPS:.6f}", "-movflags", "+faststart", BASE)
    subprocess.run(["python3", v1.DYNCAP, BASE, "-o", OUT, "--srt-in", SRT, "--top", "0.68", "--bottom", "0.78"], check=True)
    print(f"music vol {vol:.4f}\n-> {OUT}")


if __name__ == "__main__":
    main()
