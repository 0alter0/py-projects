import tkinter as t,zlib,struct
b=open(input("PNG: "),"rb").read();p=8;d=b''
while p<len(b):n=int.from_bytes(b[p:p+4],"big");q=b[p+4:p+8];x=b[p+8:p+8+n];p+=n+12;w,h,_,c=struct.unpack(">IIBB",x[:10])if q==b'IHDR'else(w,h,0,c);d+=x if q==b'IDAT'else b''
r=zlib.decompress(d);c={2:3,6:4}[c];a=[];p=[0]*(w*c);i=0
for _ in range(h):f=r[i];i+=1;o=list(r[i:i+w*c]);i+=w*c;exec('for x in range(len(o)):\n A=o[x-c]if x>=c else 0;B=p[x];o[x]=(o[x]+[0,A,B,(A+B)//2,A+max(0,min(255,B-A))][f])&255');a+=o;p=o
q=t.Tk();z=t.PhotoImage(width=w,height=h)
for y in range(h):
 for x in range(w):j=(y*w+x)*c;z.put('#'+''.join(f'{v:02x}'for v in a[j:j+3]),(x,y))
t.Label(q,image=z).pack();q.mainloop()
