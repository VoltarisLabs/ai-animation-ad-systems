#!/usr/bin/env bash
# Automated checks on a finished ad. Run after every render, before anyone watches it.
# Usage: bash qa_checks.sh out/ad.mp4 [work/script.txt | "script text"]
#   The voice-over script (a file, or the text itself) is compared with the transcript word by word.
# env: PYTHON (default python3) with faster-whisper; words.py next to this script.
set -euo pipefail
V="$1"; SCRIPT="${2:-}"
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="${PYTHON:-python3}"

echo "== frames and duration (frames should equal duration x 24)"
ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames,duration,r_frame_rate -of compact "$V"

echo "== black and frozen stretches (a held freeze-frame shot is expected; anything else is a bug)"
ffmpeg -hide_banner -i "$V" -vf "blackdetect=d=0.1:pix_th=0.05,freezedetect=n=0.001:d=1.3" -an -f null - 2>&1 \
  | grep -E "black_start|freeze_start|freeze_duration" || echo "none"

echo "== loudness (target about -14 LUFS integrated, peak under about -1.5)"
ffmpeg -hide_banner -i "$V" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|LRA|Peak):" | tail -3

echo "== transcript"
T=$("$PY" "$HERE/words.py" "$V") || { echo "words.py failed: set PYTHON to a Python with faster-whisper (now: $PY)" >&2; exit 1; }
echo "$T"
if [ -n "$SCRIPT" ]; then
  echo "== word-by-word difference against the script (empty = match)"
  norm() { tr '[:upper:]' '[:lower:]' | tr -c "[:alnum:]'\n" ' ' | tr -s ' ' '\n' | sed '/^$/d'; }
  TMP="${TMPDIR:-/tmp}/qa_script_$$.txt"
  if [ -f "$SCRIPT" ]; then norm < "$SCRIPT"; else printf '%s\n' "$SCRIPT" | norm; fi > "$TMP"
  diff "$TMP" <(printf '%s\n' "$T" | norm) || true
  rm -f "$TMP"
fi
