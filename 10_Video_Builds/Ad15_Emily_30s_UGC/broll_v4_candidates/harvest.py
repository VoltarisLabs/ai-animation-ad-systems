import sys, json
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
Q=sys.argv[1:]; res={}
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True, args=["--disable-blink-features=AutomationControlled"])
    pg=br.new_context(user_agent=UA, viewport={"width":1440,"height":1000}).new_page()
    for q in Q:
        try: pg.goto(f"https://www.pexels.com/search/videos/{q.replace(' ','%20')}/?orientation=portrait", wait_until="domcontentloaded", timeout=45000)
        except Exception as e: print(q,"nav fail"); continue
        pg.wait_for_timeout(2500); pg.mouse.wheel(0,2000); pg.wait_for_timeout(1500)
        res[q]=pg.evaluate("""() => {const out=[],seen=new Set();
          document.querySelectorAll("a[href*='/video/']").forEach(a=>{const m=(a.getAttribute('href')||'').match(/\\/video\\/([a-z0-9-]+?)-(\\d+)\\/?$/);
          if(!m||seen.has(m[2]))return; seen.add(m[2]); const c=a.closest('article')||a.parentElement; const img=c?c.querySelector('img'):null;
          out.push({slug:m[1],id:m[2],poster:img?(img.currentSrc||img.src):''});}); return out.slice(0,10);}""")
        print(f"[{q}] "+" | ".join(i['id']+':'+i['slug'][:30] for i in res[q][:8]))
    br.close()
json.dump(res, open("harvest_floor.json","w"), indent=1)
