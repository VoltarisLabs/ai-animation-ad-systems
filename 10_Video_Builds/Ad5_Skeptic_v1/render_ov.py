import sys, os, json, time
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="/tmp/fx/ov"
mode=sys.argv[1] if len(sys.argv)>1 else "preview"
T=json.load(open("timing.json")); TOTAL=T["total"]
os.makedirs(OUT,exist_ok=True)
fr=list(range(TOTAL)) if mode=="all" else [int(s*30) for s in [1.0,6.9,8.2,10.5,15.9,17.0,18.2,19.8,22.0,23.5,25.8,28.0,30.5]]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME,headless=True,args=["--force-color-profile=srgb"])
    pg=br.new_page(viewport={"width":1080,"height":1920},device_scale_factor=1)
    pg.goto("file://"+os.path.abspath("overlay.html")); pg.wait_for_timeout(300)
    t0=time.time()
    for i,f in enumerate(fr):
        pg.evaluate("f=>window.renderFrame(f)",f)
        n=f"{OUT}/o{f:04d}.png" if mode=="all" else f"/tmp/fx/ovp/p{i:02d}_f{f}.png"
        os.makedirs(os.path.dirname(n),exist_ok=True)
        pg.screenshot(path=n,type="png",omit_background=True)
        if mode=="all" and f%150==0: print(f"  {f}/{TOTAL} {time.time()-t0:.0f}s",flush=True)
    print(f"{mode}: {len(fr)} frames {time.time()-t0:.0f}s")
    br.close()
