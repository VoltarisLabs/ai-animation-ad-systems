import sys, os, json, time
from playwright.sync_api import sync_playwright
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mode=sys.argv[1] if len(sys.argv)>1 else "preview"
T=json.load(open("timing.json")); TOTAL=T["total"]
if mode=="preview":
    # one frame per scene midpoint + a few extras
    fr=[]
    for k,(a,b) in T["scenes"].items():
        fr += [int((a+(b-a)*0.45)*30), int((a+(b-a)*0.85)*30)]
    fr=sorted(set(fr)); d="preview"
else:
    fr=list(range(TOTAL)); d="frames"
os.makedirs(d,exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path=CHROME, headless=True, args=["--force-color-profile=srgb"])
    pg=br.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
    pg.goto("file://"+os.path.abspath("reel.html")); pg.wait_for_timeout(350)
    t0=time.time()
    for i,f in enumerate(fr):
        pg.evaluate("f=>window.renderFrame(f)", f)
        n=f"{d}/f{f:04d}.jpg" if mode!="preview" else f"{d}/p{i:02d}_f{f}.jpg"
        pg.screenshot(path=n, type="jpeg", quality=92 if mode!="preview" else 88)
        if mode!="preview" and f%150==0: print(f"  {f}/{TOTAL}  {time.time()-t0:.0f}s", flush=True)
    print(f"{mode}: {len(fr)} frames in {time.time()-t0:.0f}s")
    br.close()
