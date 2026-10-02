"""Word timestamps and a plain transcript from any audio or video file (faster-whisper, runs on CPU).

Usage:
  python words.py src/vo.mp3 work/vo_words.json     # voice file -> word list the builders read
  python words.py out/ad.mp4                        # just print the transcript (check it against the script)
  python words.py src/c3_beam.mp4 --start 28        # transcript from 28 s on (e.g. to check a last word)

Output JSON: [{"t": "ceiling's", "s": 0.18, "e": 0.56, "p": 0.97}, ...] with times in seconds.
Notes: whisper can drop a quiet first word and it hallucinates "Thank you for watching!" on breeze or room
noise; phrase starts from ffmpeg silencedetect are more reliable than whisper's first-word times.
Set HF_HUB_OFFLINE=1 once the small.en model is cached.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from faster_whisper import WhisperModel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("media")
    ap.add_argument("out_json", nargs="?")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--model", default="small.en")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "a.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a.start), "-i", a.media, "-vn", "-ar", "16000",
                        "-ac", "1", str(wav)], check=True)
        model = WhisperModel(a.model, device="cpu", compute_type="int8")
        segs, _ = model.transcribe(str(wav), word_timestamps=True, vad_filter=False)
        words = [{"t": w.word.strip(), "s": round(w.start + a.start, 2), "e": round(w.end + a.start, 2),
                  "p": round(w.probability, 3)} for s in segs for w in s.words]
    print(" ".join(w["t"] for w in words))
    if a.out_json:
        Path(a.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out_json).write_text(json.dumps(words, indent=1), encoding="utf-8")
        print(f"{len(words)} words -> {a.out_json}", file=sys.stderr)


if __name__ == "__main__":
    main()
