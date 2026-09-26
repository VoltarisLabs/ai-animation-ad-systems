#!/usr/bin/env python3
"""Attach local files to a row in the Airtable review hub (table `Content`).

Usage:
    python3 12_AI_Characters/airtable_attach.py <recordId> <field> <file> [file ...]

Example:
    python3 12_AI_Characters/airtable_attach.py recf8ByD6pxQSMwp9 "Generated Image 1" 12_AI_Characters/Emily/Emily_car_v3.png

Uses Airtable's uploadAttachment endpoint (5 MB per file). The file is added to
whatever is already in the field. A PNG over 5 MB is converted to a JPEG copy with
`sips` first, and the original file is left untouched. The token comes from
AIRTABLE_API_KEY in the environment, or from the airtable server entry in
~/.claude.json. It is never printed.
"""
import base64
import json
import mimetypes
import os
import subprocess
import sys
import tempfile
import urllib.request

BASE_ID = "appJ28xFZNqaHmW4u"
LIMIT = 5 * 1024 * 1024


def token():
    if os.environ.get("AIRTABLE_API_KEY"):
        return os.environ["AIRTABLE_API_KEY"]
    cfg = json.load(open(os.path.expanduser("~/.claude.json")))
    return cfg["mcpServers"]["airtable"]["env"]["AIRTABLE_API_KEY"]


def shrink_png(path):
    out = os.path.join(tempfile.mkdtemp(), os.path.splitext(os.path.basename(path))[0] + ".jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "90", path, "--out", out],
                   check=True, capture_output=True)
    return out


def upload(record_id, field, path, tok):
    if os.path.getsize(path) > LIMIT and path.lower().endswith(".png"):
        path = shrink_png(path)
    size = os.path.getsize(path)
    if size > LIMIT:
        sys.exit(f"{path}: {size} bytes is over the 5 MB upload limit. Attach it by public URL instead.")
    ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
    body = json.dumps({"contentType": ctype, "filename": os.path.basename(path),
                       "file": base64.b64encode(open(path, "rb").read()).decode()}).encode()
    url = f"https://content.airtable.com/v0/{BASE_ID}/{record_id}/{urllib.parse.quote(field)}/uploadAttachment"
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    files = next(iter(data.get("fields", {}).values()), [])
    print(f"OK {os.path.basename(path)} ({size} bytes) -> {field}: field now holds {len(files)} file(s)")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    import urllib.parse
    rec, fld, paths = sys.argv[1], sys.argv[2], sys.argv[3:]
    t = token()
    for p in paths:
        upload(rec, fld, p, t)
