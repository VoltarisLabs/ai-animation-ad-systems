#!/bin/zsh
# usage: sheet.sh out.jpg id1 id2 ...  -> 3 frames per clip, one row each
out=$1; shift; mkdir -p sh; rm -f sh/*.jpg
for id in "$@"; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 raw/$id.mp4)
  for k in 1 2 3; do
    ts=$(python3 -c "print($d*$k/4)")
    ffmpeg -v error -y -ss $ts -i raw/$id.mp4 -frames:v 1 -vf "scale=-2:360,crop=min(iw\,203):360,drawtext=text='$id':x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black" sh/${id}_$k.jpg
  done
done
ffmpeg -v error -y -pattern_type glob -i 'sh/*.jpg' -vf "tile=12x$(( ($#*3+11)/12 ))" -frames:v 1 $out
