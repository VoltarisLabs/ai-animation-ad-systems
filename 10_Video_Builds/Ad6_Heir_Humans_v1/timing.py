import json, subprocess
W=json.load(open("words.json")); GAP=0.35; FPS=30
starts={}; t=0.0; chunks=[]; allw=[]
for k in sorted(W):
    dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"vo/{k}.mp3"]))
    starts[k]=round(t,3)
    ws=[{"t":w["w"],"s":round(t+w["s"],3),"e":round(t+w["e"],3)} for w in W[k]]
    allw+=ws
    cur=[]
    for w in ws:
        cur.append(w)
        if len(cur)==3 or w["t"][-1] in ".,?:" or sum(len(x["t"])+1 for x in cur)>=15: chunks.append({"s":cur[0]["s"],"e":cur[-1]["e"],"w":cur}); cur=[]
    if cur: chunks.append({"s":cur[0]["s"],"e":cur[-1]["e"],"w":cur})
    last=W[k][-1]["e"]
    t+= max(dur, last+0.1) + GAP
total_s=round(t-GAP+0.9,2)
json.dump({"fps":FPS,"total":int(total_s*FPS),"total_s":total_s,"starts":starts,"chunks":chunks,"words":allw},open("timing.json","w"),indent=0)
print(starts,total_s,len(chunks),"chunks")
for w in allw: print(f'{w["s"]:6.2f} {w["t"]}', end=" | ")
