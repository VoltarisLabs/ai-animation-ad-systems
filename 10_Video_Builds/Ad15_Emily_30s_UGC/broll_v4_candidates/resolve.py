import sys, json
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
out={}
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True, args=["--disable-blink-features=AutomationControlled"])
    ctx=br.new_context(user_agent=UA)
    for i in sys.argv[1:]:
        try:
            r=ctx.request.get(f"https://www.pexels.com/download/video/{i}/", max_redirects=0, timeout=60000)
            out[i]=r.headers.get("location",""); print(i, r.status, out[i][:110])
        except Exception as e: print(i,"ERR",str(e)[:100])
    br.close()
json.dump(out, open("urls.json","w"), indent=1)
