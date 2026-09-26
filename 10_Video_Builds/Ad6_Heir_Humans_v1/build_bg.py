import json, subprocess, os
T=json.load(open("timing.json")); FPS=30; TOT=T["total"]
S=json.load(open("shots.json")); os.makedirs("seg",exist_ok=True)
GRADE="colorbalance=rs=0.04:gs=0.01:bs=-0.05:rm=0.03:bm=-0.03,eq=contrast=1.06:saturation=1.06:brightness=0.02,vignette=PI/7"
for n,(st,cid,off,z,_) in enumerate(S):
    f0=round(st*FPS); f1=round(S[n+1][0]*FPS) if n+1<len(S) else TOT
    nf=f1-f0; dur=nf/FPS
    W=int(1080*z*1.06)//2*2; H=int(1920*z*1.06)//2*2
    # cover-scale, then a slow drift so every shot moves
    vf=(f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
        f"crop=1080:1920:x='(iw-1080)/2+(iw-1080)/2*0.8*(t/{dur:.3f}-0.5)':y='(ih-1920)/2',setsar=1,{GRADE}")
    subprocess.run(["ffmpeg","-v","error","-y","-ss",str(off),"-i",f"raw/{cid}.mp4","-an","-vf",vf,
        "-frames:v",str(nf),"-c:v","libx264","-crf","14","-preset","fast","-pix_fmt","yuv420p",f"seg/s{n:02d}.mp4"],check=True)
    got=int(subprocess.check_output(["ffprobe","-v","error","-count_frames","-select_streams","v","-show_entries","stream=nb_read_frames","-of","csv=p=0",f"seg/s{n:02d}.mp4"]))
    print(n,cid,nf,got,"" if got==nf else "SHORT")
open("seg/list.txt","w").write("".join(f"file 's{n:02d}.mp4'\n" for n in range(len(S))))
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i","seg/list.txt","-c","copy","bg.mp4"],check=True)
print("bg frames",subprocess.check_output(["ffprobe","-v","error","-count_frames","-select_streams","v","-show_entries","stream=nb_read_frames","-of","csv=p=0","bg.mp4"]).decode().strip(),"target",TOT)
