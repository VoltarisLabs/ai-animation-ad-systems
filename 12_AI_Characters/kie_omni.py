#!/usr/bin/env python3
"""Kie.ai Gemini Omni talking clip: upload refs -> createTask -> poll -> download.

Usage:
    python3 12_AI_Characters/kie_omni.py <prompt.txt> <out.mp4> <duration 4|6|8|10> <aspect 9:16|16:9> <res 720p|1080p|4k> <img1> [img2 ...]

Model `gemini-omni-video` (docs.kie.ai/market/gemini-omni-video.md, checked 2026-09-26).
Images are references for the character and scene, not a guaranteed first frame.
Output video has synced audio. PAID: run only after the user's typed go-ahead.
"""
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "JMSN"))
from kie_nbp import req, upload  # noqa: E402  (same Kie key, same upload host)


def download(url, out, tries=4):
    for i in range(tries):
        try:
            urllib.request.urlretrieve(url, out)
            return
        except Exception as e:  # ContentTooShortError and friends: task already paid, just refetch
            if i == tries - 1:
                raise
            print(f"download retry {i + 1}: {e!r}")
            time.sleep(5)


def upload_retry(path, tries=4):
    # A dropped connection on a big PNG (BrokenPipe / SSL bad record mac) costs nothing: no task exists yet.
    for i in range(tries):
        try:
            return upload(path)
        except SystemExit as e:
            if i == tries - 1:
                raise
            print(f"upload retry {i + 1}: {e}", flush=True)
            time.sleep(5 * (i + 1))


def main():
    prompt_file, out, duration, aspect, res, *imgs = sys.argv[1:]
    prompt = open(prompt_file).read().strip()
    urls = [upload_retry(p) for p in imgs]
    print("uploaded:", len(urls))
    body = json.dumps({"model": "gemini-omni-video", "input": {
        "prompt": prompt, "image_urls": urls, "duration": str(duration),
        "aspect_ratio": aspect, "resolution": res}}).encode()
    d = req("https://api.kie.ai/api/v1/jobs/createTask", body, {"Content-Type": "application/json"}, "POST")
    if d.get("code") != 200:
        raise SystemExit(f"createTask failed: {d}")
    tid = d["data"]["taskId"]
    print("taskId:", tid, flush=True)
    t0 = time.time()
    while True:
        time.sleep(10)
        info = req(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}")["data"]
        st = info.get("state")
        if st == "success":
            result = json.loads(info["resultJson"])["resultUrls"][0]
            download(result, out)
            print(json.dumps({"state": st, "creditsConsumed": info.get("creditsConsumed"),
                              "costTime_ms": info.get("costTime"), "resultUrl": result, "out": out}))
            return
        if st == "fail":
            raise SystemExit(f"task failed: {info.get('failCode')} {info.get('failMsg')}")
        if time.time() - t0 > 1500:
            raise SystemExit(f"timeout after 25 min, last state {st}, taskId {tid}")


if __name__ == "__main__":
    main()
