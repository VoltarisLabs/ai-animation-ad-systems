#!/usr/bin/env bash
# Timestamped contact sheet of a clip or a finished ad, to see what happens when.
# Usage: bash contact_sheet.sh <video> [fps=4] [cols=8] [out.jpg]
#   bash contact_sheet.sh src/c1_splash.mp4          -> 4 frames a second, 8 across (a Flow clip)
#   bash contact_sheet.sh out/ad.mp4 2 12            -> 2 frames a second, 12 across (a finished ad)
# Font for the timestamps: FONT, else $FONTS_DIR/Anton-Regular.ttf, else ./fonts/, else a system font.
# (A missing font can crash ffmpeg's drawtext without a message, so the script checks first.)
set -euo pipefail
V="$1"; FPS="${2:-4}"; COLS="${3:-8}"; OUT="${4:-${V%.*}_sheet.jpg}"
FONT="${FONT:-${FONTS_DIR:-fonts}/Anton-Regular.ttf}"
if [ ! -f "$FONT" ]; then
  for f in C:/Windows/Fonts/arial.ttf /System/Library/Fonts/Supplemental/Arial.ttf /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf; do
    [ -f "$f" ] && FONT="$f" && break
  done
fi
[ -f "$FONT" ] || { echo "no font found: set FONT=/path/to/font.ttf" >&2; exit 1; }
FONT_ESC=$(printf '%s' "$FONT" | sed 's#\\#/#g; s#:#\\:#g')      # drive colon must be escaped in filters
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
N=$(awk -v d="$DUR" -v f="$FPS" 'BEGIN{printf "%d", d*f + 0.999}')
ROWS=$(( (N + COLS - 1) / COLS ))
ffmpeg -v error -y -i "$V" -vf "fps=${FPS},scale=240:-1,drawtext=fontfile='${FONT_ESC}':text='%{pts\:flt}':x=5:y=5:fontsize=24:fontcolor=yellow:box=1:boxcolor=black,tile=${COLS}x${ROWS}" -frames:v 1 "$OUT"
echo "$OUT ($N frames, ${COLS}x${ROWS})"
