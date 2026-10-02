#!/usr/bin/env bash
# Write a set of original, synthesized game-style sound effects into src/sfx/ (no licence needed).
# build_hud_ad.py uses these by default: menu (star slam), notify (toasts), pickup (star pop),
# phone (mission title / end card ping), mission (closing chord after the payoff word).
# Usage (inside the ad folder): bash make_synth_sfx.sh
set -euo pipefail
mkdir -p src/sfx
gen() {  # gen <name> <duration> <expression>
  ffmpeg -v error -y -f lavfi -i "aevalsrc='$3|$3':s=48000:d=$2" -c:a pcm_s16le "src/sfx/$1.wav"
}
THUMP="0.9*sin(2*PI*(80+220*exp(-t*28))*t)*exp(-t*13)"
BLIP="0.5*sin(2*PI*1320*t)*exp(-t*38)+0.3*sin(2*PI*1980*t)*exp(-t*45)"
RISE="0.55*sin(2*PI*(620+1500*t)*t)*exp(-t*16)"
CHORD="(0.17*sin(2*PI*523.25*t)+0.15*sin(2*PI*659.25*t)+0.15*sin(2*PI*783.99*t)+0.12*sin(2*PI*1046.5*t)+0.25*sin(2*PI*130.81*t))*(1-exp(-t*40))*exp(-t*3.2)"
gen menu 0.35 "$THUMP"
gen notify 0.18 "$BLIP"
gen phone 0.18 "$BLIP"
gen pickup 0.25 "$RISE"
gen mission 1.3 "$CHORD"
ls -l src/sfx/*.wav
