"""Kie.ai Nano Banana Pro: upload refs -> createTask -> poll -> download.
Usage: python3 kie_nbp.py <prompt.txt> <out.png> <aspect> <res> <img1> [img2 ...]
"""
import json, os, sys, time, mimetypes, uuid, urllib.request

ENV = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env"))
KEY = next(l.split("=", 1)[1].strip() for l in open(ENV) if l.startswith("KIE_API_KEY="))
H = {"Authorization": f"Bearer {KEY}"}


def req(url, data=None, headers=None, method=None):
    r = urllib.request.Request(url, data=data, headers={**H, **(headers or {})}, method=method)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read())


def upload(path):
    b = "----kie" + uuid.uuid4().hex
    name = os.path.basename(path)
    ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
    parts = []
    for k, v in (("uploadPath", "ugc-characters"), ("fileName", name)):
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    parts.append(f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: {ctype}\r\n\r\n'.encode()
                 + open(path, "rb").read() + b"\r\n")
    parts.append(f"--{b}--\r\n".encode())
    body = b"".join(parts)
    last = None
    for host in ("https://kieai.redpandaai.co", "https://api.kie.ai"):
        try:
            d = req(f"{host}/api/file-stream-upload", body, {"Content-Type": f"multipart/form-data; boundary={b}"}, "POST")
            if d.get("code") == 200 or d.get("success"):
                return d["data"]["downloadUrl"]
            last = d
        except Exception as e:
            last = repr(e)
    raise SystemExit(f"upload failed for {path}: {last}")


def main():
    prompt_file, out, aspect, res, *imgs = sys.argv[1:]
    prompt = open(prompt_file).read().strip()
    urls = [upload(p) for p in imgs]
    print("uploaded:", len(urls))
    body = json.dumps({"model": "nano-banana-pro", "input": {
        "prompt": prompt, "image_input": urls, "aspect_ratio": aspect,
        "resolution": res, "output_format": "png"}}).encode()
    d = req("https://api.kie.ai/api/v1/jobs/createTask", body, {"Content-Type": "application/json"}, "POST")
    if d.get("code") != 200:
        raise SystemExit(f"createTask failed: {d}")
    tid = d["data"]["taskId"]
    print("taskId:", tid)
    t0 = time.time()
    while True:
        time.sleep(6)
        info = req(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}")["data"]
        st = info.get("state")
        if st == "success":
            result = json.loads(info["resultJson"])["resultUrls"][0]
            urllib.request.urlretrieve(result, out)
            print(json.dumps({"state": st, "creditsConsumed": info.get("creditsConsumed"),
                              "costTime_ms": info.get("costTime"), "out": out}))
            return
        if st == "fail":
            raise SystemExit(f"task failed: {info.get('failCode')} {info.get('failMsg')}")
        if time.time() - t0 > 600:
            raise SystemExit(f"timeout, last state {st}")


if __name__ == "__main__":
    main()
