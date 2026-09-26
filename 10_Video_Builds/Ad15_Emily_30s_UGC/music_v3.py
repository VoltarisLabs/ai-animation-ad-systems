# Original bed for Ad 15 v3. Felt-piano arpeggio, A minor -> F -> C -> G, 84 bpm. Seeded, no samples.
import sys, wave
import numpy as np

SR = 48000
DUR = float(sys.argv[1]) if len(sys.argv) > 1 else 15.75
OUT = sys.argv[2] if len(sys.argv) > 2 else "music_v3.wav"
N = int(SR * DUR)
buf = np.zeros(N)
rng = np.random.default_rng(20260926)


def pluck(f, st, ln, amp):
    i = int(st * SR); n = min(int(ln * SR), N - i)
    if n <= 0:
        return
    x = np.arange(n) / SR
    v = np.sin(2*np.pi*f*x) + 0.30*np.sin(2*np.pi*2*f*x)*np.exp(-x*3) + 0.12*np.sin(2*np.pi*3*f*x)*np.exp(-x*5)
    buf[i:i+n] += amp * v * (1 - np.exp(-x*220)) * np.exp(-x*1.9)


def pad(f, st, ln, amp):
    i = int(st * SR); n = min(int(ln * SR), N - i)
    if n <= 0:
        return
    x = np.arange(n) / SR
    v = np.sin(2*np.pi*f*x) + 0.5*np.sin(2*np.pi*f*1.003*x)
    a = min(int(0.9*SR), n//3); r = min(int(1.2*SR), n//3)
    e = np.ones(n); e[:a] = np.linspace(0, 1, a); e[-r:] = np.linspace(1, 0, r)
    buf[i:i+n] += amp * v * e


A2, F2, C3, G2 = 110.0, 87.31, 130.81, 98.0
A3, C4, E4, F3, G3, B3, D4, G4, A4 = 220.0, 261.63, 329.63, 174.61, 196.0, 246.94, 293.66, 392.0, 440.0
prog = [(A2, [A3, C4, E4, A4]), (F2, [F3, A3, C4, E4]), (C3, [G3, C4, E4, G4]), (G2, [G3, B3, D4, G4])]
beat = 60 / 84; bar = beat * 4; t = 0; k = 0
while t < DUR - 0.8:
    root, arp = prog[k % 4]
    pad(root, t, bar + 0.5, 0.05); pad(root*2, t, bar + 0.5, 0.022)
    for j in range(8):
        st = t + j * beat / 2
        if st > DUR - 1.0:
            break
        pluck(arp[j % 4] if j < 4 else arp[(7 - j) % 4], st, 1.8, 0.07 * (0.85 + 0.3 * rng.random()))
    t += bar; k += 1
for _ in range(2):
    buf = np.convolve(buf, np.ones(5) / 5, mode="same")
fi, fo = int(0.05 * SR), int(1.0 * SR)
buf[:fi] *= np.linspace(0, 1, fi); buf[-fo:] *= np.linspace(1, 0, fo)
buf /= np.max(np.abs(buf)) + 1e-9; buf *= 0.7
w = wave.open(OUT, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.stack([buf, buf], 1) * 32767).astype(np.int16).tobytes()); w.close()
print(OUT, DUR)
