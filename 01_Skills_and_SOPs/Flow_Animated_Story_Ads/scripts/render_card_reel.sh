#!/usr/bin/env bash
# Render a card-reel story ad built by build_card_reel.py. Put this script, the builder and
# make_card_assets.py INTO the ad folder (beside src/ and work/), keeping their names.
# Needs: work/vo_words.json (python words.py src/vo.mp3 work/vo_words.json).
# Usage: bash render_card_reel.sh [out/ad.mp4]     env: PYTHON (default python3), FONTS_DIR (default ./fonts)
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
OUT="${1:-out/ad.mp4}"
mkdir -p out work
[ -f work/card_mask.png ] || "$PY" make_card_assets.py
"$PY" build_card_reel.py
IN=(); while IFS= read -r l || [ -n "$l" ]; do IN+=("${l%$'\r'}"); done < work/inputs.txt   # strip Windows CRLF
N=${#IN[@]}
MIX_INDEX=$(( $(printf '%s\n' "${IN[@]}" | grep -cx -- '-i') - 1 ))   # work/mix.wav is always the last input
AIN=("${IN[@]:0:$((N-2))}")                      # every input except the final mix
T=$(tr -d '\r' < work/total.txt)
ffmpeg -v error -y "${AIN[@]}" -/filter_complex work/audio_graph.txt -map "[aout]" -ar 48000 -ac 2 -t "$T" work/mix_raw.wav
I0=$(ffmpeg -hide_banner -i work/mix_raw.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
G=$(awk -v i="$I0" 'BEGIN{printf "%.2f", -14 - i + 1.5}')
ffmpeg -v error -y -i work/mix_raw.wav -af "volume=${G}dB,alimiter=limit=0.708:attack=3:release=50:level=false" -ar 48000 work/mix_pass1.wav
I1=$(ffmpeg -hide_banner -i work/mix_pass1.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
G2=$(awk -v i="$I1" 'BEGIN{printf "%.2f", -14 - i}')
ffmpeg -v error -y -i work/mix_pass1.wav -af "volume=${G2}dB,alimiter=limit=0.708:attack=3:release=50:level=false" -ar 48000 work/mix.wav
ffmpeg -v error -y "${IN[@]}" -/filter_complex work/video_graph.txt -map "[vout]" -map ${MIX_INDEX}:a \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -movflags +faststart -t "$T" "$OUT"
ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames,duration -of compact "$OUT"
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):" | tail -2
