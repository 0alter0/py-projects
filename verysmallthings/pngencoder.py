import tkinter as t,zlib,struct
f=open(input("PNG: "),"rb").read();p=8;d=b''
while p<len(f):
 n=struct.unpack(">I",f[p:p+4])[0];typ=f[p+4:p+8];x=f[p+8:p+8+n];p+=12+n
 if typ==b'IHDR': w,h=struct.unpack(">II",x[:8])
 if typ==b'IDAT': d+=x
raw=zlib.decompress(d);s=w*4+1;im=[];i=0;prev=[0]*(w*4)
for y in range(h):
 f=raw[i];i+=1;row=list(raw[i:i+w*4]);i+=w*4
 for x in range(len(row)):
  a=row[x-4] if x>=4 else 0;b=prev[x];c=prev[x-4] if x>=4 else 0
  row[x]=(row[x]+([a,b,c,(a+b+c)//3][f] if f else 0))&255
 im+=row;prev=row
r=t.Tk();c=t.Canvas(r,width=w,height=h);c.pack()
for y in range(h):
 for x in range(w): c.create_rectangle(x,y,x+1,y+1,fill="#%02x%02x%02x"%tuple(im[(y*w+x)*4:(y*w+x)*4+3]),outline="")
r.mainloop()
