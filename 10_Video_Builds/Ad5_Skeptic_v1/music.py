import numpy as np, wave
SR=48000; DUR=32.47; N=int(SR*DUR); t=np.arange(N)/SR
rng=np.random.default_rng(20260924)          # seeded: identical between rebuilds
def adsr(n,a,d,s,r,sus=0.7):
    e=np.zeros(n); ai,di,ri=int(a*SR),int(d*SR),int(r*SR)
    e[:ai]=np.linspace(0,1,ai); e[ai:ai+di]=np.linspace(1,sus,di)
    e[ai+di:n-ri]=sus; e[n-ri:]=np.linspace(sus,0,ri); return e
def note(f,st,ln,amp,detune=0.004,sub=True):
    n=int(ln*SR); i=int(st*SR)
    if i+n>N: n=N-i
    if n<=0: return
    x=np.arange(n)/SR
    v =np.sin(2*np.pi*f*x)
    v+=0.55*np.sin(2*np.pi*f*(1+detune)*x)
    v+=0.35*np.sin(2*np.pi*f*2*x)
    if sub: v+=0.7*np.sin(2*np.pi*f*0.5*x)
    buf[i:i+n]+=amp*v*adsr(n,0.35,0.5,0,0.9,0.62)
buf=np.zeros(N)
# A minor bed, 4 chords, one per 8.2s. Honest, calm, not hype.
A2,C3,E3,G3,D3,F3=110.00,130.81,164.81,196.00,146.83,174.61
prog=[(A2,C3,E3),(F3,A2*2,C3*2),(C3,E3,G3),(D3,F3,A2*2)]
for k,ch in enumerate(prog):
    st=k*8.2
    for f in ch: note(f,st,8.4,0.055)
# soft pulse, 84 bpm, quiet, stops under the CTA so the voice owns the end
bp=60/84
for k in range(int(DUR/bp)):
    st=k*bp
    if st>29.3: break
    n=int(0.10*SR); i=int(st*SR)
    if i+n>N: break
    x=np.arange(n)/SR
    kick=np.sin(2*np.pi*(52*np.exp(-x*16)+34)*x)*np.exp(-x*22)
    buf[i:i+n]+=0.085*kick
    if k%2==1:
        hn=int(0.045*SR)
        h=rng.standard_normal(hn)*np.exp(-np.arange(hn)/SR*90)
        buf[i:i+hn]+=0.012*h
# gentle high cut + fades
b=np.copy(buf)
for _ in range(3): b=np.convolve(b,np.ones(9)/9,mode='same')
buf=b
fi,fo=int(0.15*SR),int(1.6*SR)
buf[:fi]*=np.linspace(0,1,fi); buf[-fo:]*=np.linspace(1,0,fo)
buf/= (np.max(np.abs(buf))+1e-9); buf*=0.72
st=np.stack([buf,buf],1)
w=wave.open("music.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
print("music.wav", round(DUR,2),"s, peak", round(float(np.max(np.abs(buf))),3))
