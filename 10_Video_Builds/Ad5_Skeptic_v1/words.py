import json, glob
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
out = {}
for f in sorted(glob.glob("vo/L*.mp3")):
    segs, _ = m.transcribe(f, word_timestamps=True, beam_size=5)
    ws = []
    for s in segs:
        for w in s.words:
            ws.append({"w": w.word.strip(), "s": round(w.start,3), "e": round(w.end,3)})
    key = f.split("/")[-1].replace(".mp3","")
    out[key] = ws
    print(key, len(ws), "words,", ws[0]["s"] if ws else None, "->", ws[-1]["e"] if ws else None)
json.dump(out, open("words.json","w"), indent=1)
