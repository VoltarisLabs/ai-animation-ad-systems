#!/usr/bin/env python3
"""Download a social video (Instagram, X, TikTok, YouTube...) and break it down for a remake.

    watch.py URL_OR_FILE [-o OUTDIR] [--model MODEL] [--no-gemini] [--no-transcript]
                         [--cookies-from-browser chrome] [--force]

Writes into OUTDIR (default $REMAKE_DIR/<platform>-<id>/; without REMAKE_DIR it uses
~/Documents/Ad engine/references/remakes/ when that folder's parent exists, else ./remakes/):
  video.mp4        the source (reuse it as a motion-transfer reference)
  info.json        caption, author, stats
  hook.png         8 timestamped frames across the first 3 seconds
  sheet.png        one timestamped frame per shot (cuts from scene detection)
  frames/          720px frame at each shot's midpoint, named by timestamp
  transcript.json  Whisper segments with timestamps
  gemini.md        Gemini's timestamped watch-through (video + audio)
  breakdown.md     everything above in one file

A post with several videos (X multi-video, IG carousel) gets one part-N/ folder per video.
Homebrew ffmpeg on this Mac has broken dylibs, so this uses the imageio_ffmpeg binary.
"""

import argparse
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import requests

AD_ENGINE = Path.home() / "Documents" / "Ad engine"
DEFAULT_ROOT = Path(os.environ["REMAKE_DIR"]).expanduser() if os.environ.get("REMAKE_DIR") else (
    AD_ENGINE / "references" / "remakes" if (AD_ENGINE / "references").is_dir() else Path.cwd() / "remakes"
)
ENV_FILES = [Path.home() / ".env", Path.cwd() / ".env", AD_ENGINE / ".claude" / ".env"]
GEMINI_MODELS = ["gemini-3.1-pro-preview", "gemini-2.5-pro", "gemini-flash-latest"]
GEMINI_BASE = "https://generativelanguage.googleapis.com"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
VIDEO_EXTS = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}

GEMINI_PROMPT = """You are breaking down a short-form social video so a production team can remake it
shot for shot with AI image generation + image-to-video. Watch the whole video and listen to the audio.

Detected cut timestamps from scene detection (may miss soft transitions or add false cuts): {cuts}
Runtime: {duration:.1f}s

Return markdown with exactly these sections:

## Format
What kind of video this is (talking-head UGC, claymation story ad, crochet/yarn animation, 3D cartoon
skeleton progression, Pixar-style talking objects, music-video ad, screen recording, text slideshow,
cinematic b-roll montage, live-action skit, other). The render look in one line. Runtime, number of
shots, average shot length.

## Transcript
Every spoken word and sung lyric, one line per sentence: `[start-end] text`. Mark who speaks if more
than one voice. Write "No speech" if there is none.

## Hook (0-3s)
Second by second: what moves, what is said, what text appears. Why it stops the scroll.

## Shot list
One table row per shot (a new shot = a cut or a hard change of framing):
| # | Start-End (s) | What we see (subject, action, setting) | Camera (framing, angle, movement) | Audio / VO (verbatim) | On-screen text (verbatim) |

## Characters
Each recurring character: look, outfit, materials/texture, what keeps them consistent between shots.

## Audio
Voiceover (voice type, pace, tone), music (genre, tempo, where it changes), SFX. Original speech,
trending sound, or song?

## Edit and text style
Cut rhythm, transitions, caption style (look, position, color, word-by-word or full lines),
zooms/shakes added in the edit.

## Script structure
The narrative beats in order with timestamps (e.g. pain -> turn -> proof -> destination -> CTA).
The CTA verbatim.

## Why it works
3-5 bullets on the specific retention mechanics.

## Remake difficulty
What will be hard to reproduce with AI image-to-video (fast motion, hands, lip sync, legible text,
crowds, long takes) and how to work around each.

Rules: be literal and specific. Quote speech and on-screen text exactly. Timestamps in seconds with
one decimal. If you are unsure of something, say so instead of guessing.
"""


def log(msg):
    print(f"[remake] {msg}", flush=True)


def env(*names):
    for name in names:
        if os.environ.get(name):
            return os.environ[name]
    for f in ENV_FILES:
        if not f.exists():
            continue
        for line in f.read_text().splitlines():
            for name in names:
                if line.startswith(name + "="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
    return None


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        exe = shutil.which("ffmpeg")
        if not exe:
            sys.exit("No ffmpeg. Run: pip install imageio-ffmpeg")
        return exe


# --- source handling -------------------------------------------------------

def slug_for(src):
    if Path(src).expanduser().exists():
        return "file-" + re.sub(r"[^A-Za-z0-9_-]+", "-", Path(src).stem)[:60]
    patterns = [
        ("ig", r"instagram\.com/(?:[^/]+/)?(?:reel|reels|p|tv)/([A-Za-z0-9_-]+)"),
        ("x", r"(?:x|twitter)\.com/[^/]+/status/(\d+)"),
        ("tt", r"tiktok\.com/.*/video/(\d+)"),
        ("yt", r"(?:youtube\.com/(?:shorts/|watch\?v=)|youtu\.be/)([A-Za-z0-9_-]{6,})"),
    ]
    for prefix, pat in patterns:
        m = re.search(pat, src)
        if m:
            return f"{prefix}-{m.group(1)}"
    tail = re.sub(r"[^A-Za-z0-9_-]+", "-", src.rstrip("/").split("/")[-1])[:60]
    return f"web-{tail or 'video'}"


def existing_videos(outdir):
    found = list(outdir.glob("video*")) or list(outdir.glob("part-*/video.*"))
    return sorted(p for p in found if p.suffix.lower() in VIDEO_EXTS)


def download_ytdlp(url, outdir, cookies_browser=None):
    cmd = [
        "yt-dlp", "--ffmpeg-location", ffmpeg(),
        "-f", "bv*[ext=mp4]+ba[ext=m4a]/bv*+ba/b",
        "--merge-output-format", "mp4",
        "--write-info-json", "--no-write-playlist-metafiles",
        "--no-warnings", "--socket-timeout", "30",
        "-o", str(outdir / "video-%(playlist_index|1)s.%(ext)s"),
        "-o", "infojson:" + str(outdir / "info-%(playlist_index|1)s"),
        url,
    ]
    if cookies_browser:
        cmd[1:1] = ["--cookies-from-browser", cookies_browser]
    if re.search(r"/(?:video|photo)/\d+", url):  # link names one video in a multi-video post
        cmd[1:1] = ["--no-playlist"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        log(f"yt-dlp failed: {r.stderr.strip()[-400:]}")
    return existing_videos(outdir)


def download_apify(url, outdir):
    """Instagram fallback via Apify (same actor as IG2Claude/ig_dl.py)."""
    token = env("APIFY_API_TOKEN")
    if not token:
        log("no APIFY_API_TOKEN for the Instagram fallback")
        return []
    log("trying Apify instagram-scraper fallback...")
    endpoint = (
        "https://api.apify.com/v2/acts/apify~instagram-scraper"
        f"/run-sync-get-dataset-items?token={token}&timeout=300"
    )
    r = requests.post(endpoint, json={
        "directUrls": [url], "resultsType": "posts", "resultsLimit": 1, "addParentData": False,
    }, timeout=330)
    r.raise_for_status()
    items = r.json()
    if not items or items[0].get("error"):
        log(f"Apify returned nothing usable: {items[:1]}")
        return []
    post = items[0]
    media = post.get("videoUrl")
    if not media:
        log(f"post has no video (type={post.get('type')})")
        return []
    dest = outdir / "video-1.mp4"
    req = urllib.request.Request(media, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
        shutil.copyfileobj(resp, f)
    (outdir / "info-1.info.json").write_text(json.dumps({
        "uploader": post.get("ownerUsername"),
        "description": post.get("caption"),
        "view_count": post.get("videoViewCount") or post.get("videoPlayCount"),
        "like_count": post.get("likesCount"),
        "comment_count": post.get("commentsCount"),
        "upload_date": post.get("timestamp"),
        "webpage_url": url,
    }, indent=2))
    return [dest]


def fetch(src, outdir, cookies_browser=None, force=False):
    outdir.mkdir(parents=True, exist_ok=True)
    have = existing_videos(outdir)
    if have and not force:
        log(f"already downloaded: {', '.join(str(p.relative_to(outdir)) for p in have)}")
        return have
    for p in have:
        p.unlink()
    local = Path(src).expanduser()
    if local.exists():
        dest = outdir / ("video-1" + local.suffix.lower())
        shutil.copy2(local, dest)
        return [dest]
    log(f"downloading {src}")
    vids = download_ytdlp(src, outdir, cookies_browser)
    if not vids and "instagram.com" in src:
        vids = download_apify(src, outdir)
    if not vids:
        sys.exit(
            "Could not download the video. If the account is private or login-walled, retry with "
            "--cookies-from-browser chrome, or save the video and pass the file path instead."
        )
    return vids


# --- analysis --------------------------------------------------------------

def probe(path):
    err = subprocess.run([ffmpeg(), "-i", str(path)], capture_output=True, text=True).stderr
    info = {"duration": 0.0, "width": None, "height": None, "fps": None, "has_audio": " Audio:" in err}
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    if m:
        info["duration"] = int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])
    m = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    if m:
        info["width"], info["height"] = int(m[1]), int(m[2])
    m = re.search(r"([\d.]+) fps", err)
    if m:
        info["fps"] = float(m[1])
    return info


def detect_cuts(path, duration, threshold=0.3, min_gap=0.4):
    r = subprocess.run(
        [ffmpeg(), "-hide_banner", "-i", str(path), "-an",
         "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    cuts = []
    for t in (float(x) for x in re.findall(r"pts_time:([\d.]+)", r.stderr)):
        if t > min_gap and duration - t > min_gap and (not cuts or t - cuts[-1] >= min_gap):
            cuts.append(round(t, 2))
    return cuts


def frame_at(path, t, dest, width=720):
    subprocess.run(
        [ffmpeg(), "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(path),
         "-frames:v", "1", "-vf", f"scale={width}:-2", "-q:v", "3", str(dest)],
        check=True,
    )
    return dest


def contact_sheet(images, labels, dest, tile_w=240, cols=None):
    from PIL import Image, ImageDraw, ImageFont
    tiles = [Image.open(p).convert("RGB") for p in images]
    tile_h = round(tiles[0].height * tile_w / tiles[0].width)
    cols = cols or (6 if tile_h > tile_w else 4)
    cols = min(cols, len(tiles))
    rows = -(-len(tiles) // cols)
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), "black")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    for i, (tile, label) in enumerate(zip(tiles, labels)):
        x, y = (i % cols) * tile_w, (i // cols) * tile_h
        sheet.paste(tile.resize((tile_w, tile_h)), (x, y))
        box = draw.textbbox((x + 6, y + 6), label, font=font)
        draw.rectangle((box[0] - 4, box[1] - 3, box[2] + 4, box[3] + 3), fill="black")
        draw.text((x + 6, y + 6), label, fill="yellow", font=font)
    sheet.save(dest)
    return dest


def transcribe(path, workdir, has_audio):
    key = env("OPENAI_API_KEY")
    if not has_audio:
        return {"skipped": "no audio stream"}
    if not key:
        return {"skipped": "no OPENAI_API_KEY"}
    audio = workdir / "audio.mp3"
    subprocess.run([ffmpeg(), "-v", "error", "-y", "-i", str(path), "-vn", "-ac", "1",
                    "-ar", "16000", "-b:a", "64k", str(audio)], check=True)
    with open(audio, "rb") as f:
        r = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {key}"},
            files={"file": ("audio.mp3", f, "audio/mpeg")},
            data={"model": "whisper-1", "response_format": "verbose_json"},
            timeout=300,
        )
    audio.unlink(missing_ok=True)
    if r.status_code != 200:
        try:
            reason = r.json()["error"]["message"].split(". ")[0]
        except (ValueError, KeyError, TypeError):
            reason = r.text[:120]
        return {"skipped": f"Whisper unavailable ({r.status_code}: {reason}); use Gemini's transcript"}
    d = r.json()
    return {
        "language": d.get("language"),
        "text": d.get("text", "").strip(),
        "segments": [
            {"start": round(s["start"], 1), "end": round(s["end"], 1), "text": s["text"].strip()}
            for s in d.get("segments", [])
        ],
    }


def gemini_watch(path, prompt, models):
    key = env("GEMINI_API_KEY", "GOOGLE_API_KEY")
    if not key:
        return None, "no GEMINI_API_KEY / GOOGLE_API_KEY"
    hdr = {"x-goog-api-key": key}
    mime = mimetypes.guess_type(str(path))[0] or "video/mp4"
    size = path.stat().st_size
    start = requests.post(
        f"{GEMINI_BASE}/upload/v1beta/files",
        headers={**hdr, "X-Goog-Upload-Protocol": "resumable", "X-Goog-Upload-Command": "start",
                 "X-Goog-Upload-Header-Content-Length": str(size),
                 "X-Goog-Upload-Header-Content-Type": mime, "Content-Type": "application/json"},
        json={"file": {"display_name": path.name}}, timeout=60,
    )
    start.raise_for_status()
    with open(path, "rb") as f:
        up = requests.post(
            start.headers["X-Goog-Upload-URL"],
            headers={"X-Goog-Upload-Command": "upload, finalize", "X-Goog-Upload-Offset": "0",
                     "Content-Length": str(size)},
            data=f, timeout=600,
        )
    up.raise_for_status()
    file = up.json()["file"]
    try:
        for _ in range(60):
            if file.get("state") == "ACTIVE":
                break
            if file.get("state") == "FAILED":
                return None, "Gemini could not process the video"
            time.sleep(3)
            file = requests.get(f"{GEMINI_BASE}/v1beta/{file['name']}", headers=hdr, timeout=30).json()
        body = {"contents": [{"parts": [
            {"file_data": {"mime_type": mime, "file_uri": file["uri"]}},
            {"text": prompt},
        ]}]}
        errors = []
        for model in models:
            log(f"Gemini watching with {model}...")
            r = requests.post(f"{GEMINI_BASE}/v1beta/models/{model}:generateContent",
                              headers=hdr, json=body, timeout=600)
            if r.status_code == 200:
                parts = r.json().get("candidates", [{}])[0].get("content", {}).get("parts", [])
                text = "".join(p.get("text", "") for p in parts).strip()
                if text:
                    return text, model
            errors.append(f"{model}: {r.status_code} {r.text[:160]}")
        return None, "; ".join(errors)
    finally:
        requests.delete(f"{GEMINI_BASE}/v1beta/{file['name']}", headers=hdr, timeout=30)


# --- per-video pipeline ----------------------------------------------------

def fmt_t(t):
    return f"{t:05.1f}s"


def process(video, workdir, args):
    workdir.mkdir(parents=True, exist_ok=True)
    meta = probe(video)
    dur = meta["duration"]
    log(f"{video.name}: {dur:.1f}s {meta['width']}x{meta['height']} "
        f"{meta['fps'] or '?'}fps audio={'yes' if meta['has_audio'] else 'no'}")

    cuts = detect_cuts(video, dur)
    bounds = [0.0] + cuts + [dur]
    shots = [(a, b) for a, b in zip(bounds, bounds[1:]) if b - a > 0.05]
    sampled = len(shots) == 1 and dur > 4
    if sampled:  # one long take: sample every ~2s instead
        step = max(2.0, dur / 24)
        edges = [round(i * step, 2) for i in range(int(dur // step) + 1)] + [dur]
        shots = [(a, b) for a, b in zip(edges, edges[1:]) if b - a > 0.05]
    log(f"{len(cuts)} cuts detected" + (f", sampling {len(shots)} frames" if sampled else f", {len(shots)} shots"))

    frames_dir = workdir / "frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir()
    sheet_shots = shots if len(shots) <= 36 else [shots[round(i * (len(shots) - 1) / 35)] for i in range(36)]
    shot_frames, shot_labels = [], []
    for i, (a, b) in enumerate(sheet_shots, 1):
        mid = (a + b) / 2
        shot_frames.append(frame_at(video, mid, frames_dir / f"shot{i:02d}-{mid:06.2f}s.jpg"))
        shot_labels.append(f"#{i} {a:.1f}-{b:.1f}s")
    contact_sheet(shot_frames, shot_labels, workdir / "sheet.png")

    hook_end = min(3.0, dur - 0.05)
    hook_times = [round(hook_end * i / 7, 2) for i in range(8)]
    hook_frames = [frame_at(video, t, frames_dir / f"hook-{t:05.2f}s.jpg") for t in hook_times]
    contact_sheet(hook_frames, [f"{t:.1f}s" for t in hook_times], workdir / "hook.png",
                  cols=8 if meta["height"] and meta["height"] > (meta["width"] or 0) else 4)

    tpath = workdir / "transcript.json"
    cached = json.loads(tpath.read_text()) if tpath.exists() and not args.force else {}
    if "segments" in cached or cached.get("skipped") == "no audio stream":
        transcript = cached
    elif args.no_transcript:
        transcript = {"skipped": "--no-transcript"}
    else:
        if meta["has_audio"]:
            log("transcribing with Whisper...")
        transcript = transcribe(video, workdir, meta["has_audio"])
        tpath.write_text(json.dumps(transcript, indent=2))

    gpath = workdir / "gemini.md"
    if gpath.exists() and not args.force and not gpath.read_text().startswith("_Gemini failed"):
        gemini = gpath.read_text()
    elif args.no_gemini:
        gemini = "_skipped (--no-gemini)_"
    else:
        prompt = GEMINI_PROMPT.format(cuts=", ".join(f"{c:.1f}" for c in cuts) or "none", duration=dur)
        text, model_or_err = gemini_watch(video, prompt, [args.model] if args.model else GEMINI_MODELS)
        gemini = f"_Watched by {model_or_err}_\n\n{text}" if text else f"_Gemini failed: {model_or_err}_"
        gpath.write_text(gemini)

    ends = [float(b) for _, b in re.findall(r"\b(\d{1,4}\.\d)\s*-\s*(\d{1,4}\.\d)\b", gemini)]
    drift = max(ends, default=0) > dur + 2
    if drift:
        log(f"warning: Gemini timestamps run to {max(ends):.1f}s on a {dur:.1f}s video")

    return {"video": video, "meta": meta, "cuts": cuts, "shots": shots, "sampled": sampled,
            "drift": max(ends) if drift else None,
            "transcript": transcript, "gemini": gemini, "workdir": workdir}


def load_info(outdir, n):
    p = outdir / f"info-{n}.info.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text())
    keep = ["webpage_url", "uploader", "uploader_id", "channel", "title", "description",
            "upload_date", "duration", "view_count", "like_count", "comment_count",
            "repost_count", "track", "artist"]
    slim = {k: d[k] for k in keep if d.get(k) not in (None, "")}
    p.unlink()
    return slim


def write_breakdown(outdir, src, results, infos):
    lines = [f"# Remake breakdown: {outdir.name}", "", f"Source: {src}", ""]
    for n, res in enumerate(results, 1):
        info, meta, wd = infos[n - 1], res["meta"], res["workdir"]
        if len(results) > 1:
            lines += [f"---", f"# Part {n}", ""]
        if re.fullmatch(r"\d{8}", str(info.get("upload_date", ""))):
            d = info["upload_date"]
            info["upload_date"] = f"{d[:4]}-{d[4:6]}-{d[6:]}"
        lines += ["## Post"]
        for k, label in [("uploader", "Author"), ("upload_date", "Posted"), ("view_count", "Views"),
                         ("like_count", "Likes"), ("comment_count", "Comments"),
                         ("repost_count", "Reposts"), ("track", "Sound")]:
            if info.get(k) is not None:
                lines.append(f"- {label}: {info[k]:,}" if isinstance(info[k], int) else f"- {label}: {info[k]}")
        if info.get("description"):
            lines += ["- Caption:", "", "  > " + info["description"].replace("\n", "\n  > ")]
        lines += ["", "## Specs",
                  f"- {meta['duration']:.1f}s, {meta['width']}x{meta['height']}, {meta['fps'] or '?'} fps, "
                  f"audio: {'yes' if meta['has_audio'] else 'no'}",
                  (f"- one continuous take (no cuts detected); sheet samples {len(res['shots'])} frames"
                   if res["sampled"] else
                   f"- {len(res['shots'])} shots, cuts at: "
                   + (", ".join(f"{c:.1f}" for c in res["cuts"]) or "none detected")),
                  "", "## Transcript (Whisper)"]
        t = res["transcript"]
        if t.get("segments"):
            lines += [f"- [{fmt_t(s['start'])}-{fmt_t(s['end'])}] {s['text']}" for s in t["segments"]]
            lines.append("")
            lines.append("_Whisper invents words over music-only audio. Trust it only where Gemini hears speech too._")
        else:
            lines.append(f"_{t.get('skipped') or 'no speech'}_ (see Transcript in the Gemini section)")
        lines += ["", "## Gemini watch-through", ""]
        if res["drift"]:
            lines += [f"> **Timeline drift:** Gemini's timestamps run to {res['drift']:.1f}s on a "
                      f"{meta['duration']:.1f}s video. Its content is usable; take timing from the cut "
                      "list above and the frames.", ""]
        lines += [res["gemini"], "", "## Files",
                  f"- video: {res['video']}", f"- hook frames: {wd / 'hook.png'}",
                  f"- shot sheet: {wd / 'sheet.png'}", f"- per-shot frames: {wd / 'frames'}/", ""]
    out = outdir / "breakdown.md"
    out.write_text("\n".join(lines))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", help="Video URL (Instagram, X, TikTok, YouTube...) or local file")
    ap.add_argument("-o", "--outdir", help=f"Output folder (default: {DEFAULT_ROOT}/<id>)")
    ap.add_argument("--model", help=f"Gemini model (default tries {', '.join(GEMINI_MODELS)})")
    ap.add_argument("--no-gemini", action="store_true")
    ap.add_argument("--no-transcript", action="store_true")
    ap.add_argument("--cookies-from-browser", help="e.g. chrome, safari — for login-walled posts")
    ap.add_argument("-f", "--force", action="store_true", help="Re-download and re-analyze")
    args = ap.parse_args()

    outdir = Path(args.outdir).expanduser() if args.outdir else DEFAULT_ROOT / slug_for(args.src)
    videos = fetch(args.src, outdir, args.cookies_from_browser, args.force)
    multi = len(videos) > 1
    if multi:
        log(f"post has {len(videos)} videos — one part-N/ folder each")

    results, infos = [], []
    for n, v in enumerate(videos, 1):
        target = (outdir / f"part-{n}" if multi else outdir) / ("video" + v.suffix.lower())
        target.parent.mkdir(exist_ok=True)
        if v != target:
            v = Path(shutil.move(str(v), target))
        info = load_info(outdir, n) or (json.loads((v.parent / "info.json").read_text())
                                        if (v.parent / "info.json").exists() else {})
        (v.parent / "info.json").write_text(json.dumps(info, indent=2))
        infos.append(info)
        results.append(process(v, v.parent, args))

    out = write_breakdown(outdir, args.src, results, infos)
    print(f"\nBREAKDOWN: {out}")
    for r in results:
        print(f"HOOK:      {r['workdir'] / 'hook.png'}")
        print(f"SHEET:     {r['workdir'] / 'sheet.png'}")


if __name__ == "__main__":
    main()
