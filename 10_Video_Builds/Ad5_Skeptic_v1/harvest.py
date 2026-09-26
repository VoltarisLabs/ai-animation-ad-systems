import sys, re, json
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
QUERIES=json.load(open("queries.json"))
res={}
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True,
                         args=["--disable-blink-features=AutomationControlled"])
    ctx=br.new_context(user_agent=UA, viewport={"width":1440,"height":1000})
    pg=ctx.new_page()
    for q in QUERIES:
        url=f"https://www.pexels.com/search/videos/{q.replace(' ','%20')}/?orientation=portrait"
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=45000)
        except Exception as e:
            print(f"[{q}] nav fail {str(e)[:60]}"); res[q]=[]; continue
        pg.wait_for_timeout(2200)
        pg.mouse.wheel(0,2200); pg.wait_for_timeout(1400)
        items=pg.evaluate("""() => {
          const out=[];
          document.querySelectorAll("a[href*='/video/']").forEach(a=>{
            const m=a.getAttribute('href').match(/\\/video\\/([a-z0-9-]+?)-(\\d+)\\/?$/);
            if(m) out.push({slug:m[1], id:m[2]});
          });
          return out;
        }""")
        seen=set(); clean=[]
        for it in items:
            if it["id"] in seen: continue
            seen.add(it["id"]); clean.append(it)
        res[q]=clean[:8]
        print(f"[{q}] {len(clean)}")
        for it in clean[:4]: print("    ", it["id"], it["slug"][:58])
    br.close()
json.dump(res, open("harvest.json","w"), indent=1)
