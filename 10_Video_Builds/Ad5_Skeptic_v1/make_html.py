import json
W=json.load(open("words.json"))
FPS=30
# line start times, derived from measured speech ends + 0.30s gap
ends={k:(w[-1]["e"] if w else 0) for k,w in W.items()}
starts={}; t=0.0
for k in sorted(W):
    starts[k]=round(t,3); t=round(t+ends[k]+0.30,3)
TOTAL_S=round(t-0.30+1.15,3)
TOTAL=int(TOTAL_S*FPS)
# caption chunks: <=3 words, absolute times
chunks=[]
for k in sorted(W):
    ws=W[k]; off=starts[k]
    for i in range(0,len(ws),3):
        g=ws[i:i+3]
        chunks.append({"s":round(off+g[0]["s"],3),"e":round(off+g[-1]["e"],3),
                       "w":[{"t":x["w"],"s":round(off+x["s"],3),"e":round(off+x["e"],3)} for x in g]})
SC={"A":(0.0,starts["L01"]),"B":(starts["L01"],starts["L02"]),"C":(starts["L02"],starts["L03"]),
    "D":(starts["L03"],starts["L04"]),"E":(starts["L04"],starts["L05"]),"F":(starts["L05"],TOTAL_S)}
print("line starts:",starts); print("scenes:",{k:(round(a,2),round(b,2)) for k,(a,b) in SC.items()})
print("TOTAL_S",TOTAL_S,"frames",TOTAL,"chunks",len(chunks))
json.dump({"fps":FPS,"total":TOTAL,"total_s":TOTAL_S,"starts":starts,"scenes":SC,"chunks":chunks},
          open("timing.json","w"),indent=1)
