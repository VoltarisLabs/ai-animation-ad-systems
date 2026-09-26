# Original bed for Ad6. Soft felt-piano arpeggio in F major, 70 bpm. Seeded, no samples.
import numpy as np, wave, json
SR=48000; DUR=json.load(open("timing.json"))["total_s"]; N=int(SR*DUR); buf=np.zeros(N)
rng=np.random.default_rng(20260925)
def pluck(f,st,ln,amp):
    i=int(st*SR); n=min(int(ln*SR),N-i)
    if n<=0: return
    x=np.arange(n)/SR
    v=np.sin(2*np.pi*f*x)+0.30*np.sin(2*np.pi*2*f*x)*np.exp(-x*3)+0.12*np.sin(2*np.pi*3*f*x)*np.exp(-x*5)
    env=(1-np.exp(-x*220))*np.exp(-x*1.7)
    buf[i:i+n]+=amp*v*env
def pad(f,st,ln,amp):
    i=int(st*SR); n=min(int(ln*SR),N-i)
    if n<=0: return
    x=np.arange(n)/SR
    v=np.sin(2*np.pi*f*x)+0.5*np.sin(2*np.pi*f*1.003*x)
    a=min(int(1.2*SR),n//3); r=min(int(1.5*SR),n//3); e=np.ones(n); e[:a]=np.linspace(0,1,a); e[-r:]=np.linspace(1,0,r)
    buf[i:i+n]+=amp*v*e
F3,A3,C4,E4,G3,B3,D4,D3,Bb2,Bb3,F4=174.61,220.0,261.63,329.63,196.0,246.94,293.66,146.83,116.54,233.08,349.23
C3,A2,F2=130.81,110.0,87.31
prog=[(F2,[F3,A3,C4,E4]),(C3,[G3,C4,E4,G3*2]),(D3,[A3,D4,F4,A3*2]),(Bb2,[Bb3,D4,F4,A3*2])]
beat=60/70; bar=beat*4; t=0; k=0
while t<DUR-1.0:
    root,arp=prog[k%4]
    pad(root,t,bar+0.6,0.05); pad(root*2,t,bar+0.6,0.025)
    for j in range(8):
        st=t+j*beat/2
        if st>DUR-1.2: break
        pluck(arp[j%4] if j<4 else arp[(7-j)%4],st,2.2,0.07*(0.85+0.3*rng.random()))
    t+=bar; k+=1
b=buf.copy()
for _ in range(2): b=np.convolve(b,np.ones(5)/5,mode='same')
buf=b; fi,fo=int(0.05*SR),int(2.2*SR)
buf[:fi]*=np.linspace(0,1,fi); buf[-fo:]*=np.linspace(1,0,fo)
buf/=np.max(np.abs(buf))+1e-9; buf*=0.7
w=wave.open("music.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.stack([buf,buf],1)*32767).astype(np.int16).tobytes()); w.close()
print("music.wav",DUR)
