import sys, os, json, time
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T=json.load(open("timing.json")); TOTAL=T["total"]
mode=sys.argv[1] if len(sys.argv)>1 else "preview"
OUT="ov" if mode=="all" else "ovp"; os.makedirs(OUT,exist_ok=True)
fr=list(range(TOTAL)) if mode=="all" else [int(s*30) for s in [1.5,5.0,12.5,17.0,24.5,29.0,31.5,36.0,39.0,43.0]]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME,headless=True,args=["--force-color-profile=srgb"])
    pg=br.new_page(viewport={"width":1080,"height":1920},device_scale_factor=1)
    pg.goto("file://"+os.path.abspath("overlay.html")); pg.wait_for_timeout(400)
    t0=time.time()
    for f in fr:
        pg.evaluate("f=>window.renderFrame(f)",f)
        pg.screenshot(path=f"{OUT}/o{f:04d}.png",type="png",omit_background=True)
    print(mode,len(fr),"frames",round(time.time()-t0),"s")
    br.close()
