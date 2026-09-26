import sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont
out=sys.argv[1]; ids=sys.argv[2:]; W,H=180,320; cols=12
fnt=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf",18)
tiles=[]
for i in ids:
    d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"raw/{i}.mp4"]))
    for k in (1,2,3):
        p=f"/tmp/_s_{i}_{k}.jpg"
        subprocess.run(["ffmpeg","-v","error","-y","-ss",str(d*k/4),"-i",f"raw/{i}.mp4","-frames:v","1",
          "-vf",f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",p])
        im=Image.open(p); dr=ImageDraw.Draw(im); dr.rectangle([0,0,110,24],fill="black"); dr.text((4,2),f"{i}.{k}",fill="yellow",font=fnt); tiles.append(im)
rows=(len(tiles)+cols-1)//cols; S=Image.new("RGB",(cols*W,rows*H))
for n,t in enumerate(tiles): S.paste(t,((n%cols)*W,(n//cols)*H))
S.save(out,quality=85); print(out,len(tiles))
