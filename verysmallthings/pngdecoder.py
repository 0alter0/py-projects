import tkinter as t,zlib,struct
b=open(input("PNG: "),"rb").read();p=8;d=b''
while p<len(b):
 n=int.from_bytes(b[p:p+4],"big");q=b[p+4:p+8];x=b[p+8:p+8+n];p+=n+12
 if q==b'IHDR':w,h,bd,ct=struct.unpack(">IIBB",x[:10])
 if q==b'IDAT':d+=x
r=zlib.decompress(d);c={2:3,6:4}[ct];a=[];i=0;pr=[0]*(w*c)
for y in range(h):
 f=r[i];i+=1;ro=list(r[i:i+w*c]);i+=w*c
 for x in range(len(ro)):
  A=ro[x-c] if x>=c else 0;B=pr[x];C=pr[x-c] if x>=c else 0
  ro[x]=(ro[x]+([0,A,B,(A+B)//2,A+max(0,min(255,B-A))][f]))&255
 a+=ro;pr=ro
q=t.Tk();z=t.PhotoImage(width=w,height=h)
for y in range(h):
 for x in range(w):
  j=(y*w+x)*c;v=a[j:j+3];z.put("#"+"".join(f"{x:02x}" for x in v),(x,y))
t.Label(q,image=z).pack();q.mainloop()
