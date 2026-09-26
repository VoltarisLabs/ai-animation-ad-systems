import sys, os
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
ids=sys.argv[1:]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True,
                         args=["--disable-blink-features=AutomationControlled"])
    ctx=br.new_context(user_agent=UA)
    for i in ids:
        out=f"raw/{i}.mp4"
        if os.path.exists(out) and os.path.getsize(out)>100000: continue
        try:
            r=ctx.request.get(f"https://www.pexels.com/download/video/{i}/", timeout=180000)
            b=r.body()
            if r.status==200 and len(b)>100000:
                open(out,"wb").write(b); print(i,"ok",len(b))
            else: print(i,"FAIL",r.status,len(b))
        except Exception as e: print(i,"ERR",str(e)[:80])
    br.close()
