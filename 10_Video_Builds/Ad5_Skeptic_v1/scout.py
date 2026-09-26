import sys, re, json, time
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
QUERIES=sys.argv[1:] or ["suburban house"]
RX=re.compile(r'https://videos\.pexels\.com/video-files/(\d+)/([\d_]+)\.mp4')
out={}
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True,
                         args=["--disable-blink-features=AutomationControlled"])
    ctx=br.new_context(user_agent=UA, viewport={"width":1440,"height":1000},
                       locale="en-US")
    pg=ctx.new_page()
    for q in QUERIES:
        url=f"https://www.pexels.com/search/videos/{q.replace(' ','%20')}/?orientation=portrait"
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=45000)
        except Exception as e:
            print(f"[{q}] nav fail: {str(e)[:80]}"); continue
        pg.wait_for_timeout(2500)
        for _ in range(3):
            pg.mouse.wheel(0, 2400); pg.wait_for_timeout(1200)
        html=pg.content()
        hits=sorted(set(RX.findall(html)))
        out[q]=[f"https://videos.pexels.com/video-files/{a}/{b}.mp4" for a,b in hits]
        print(f"[{q}] {len(out[q])} mp4 urls   (page bytes {len(html)})")
    br.close()
json.dump(out, open("found.json","w"), indent=1)
