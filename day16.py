import numpy as np

bits=bin(int("F"+open("input16.txt","r").read().strip(),16))[6:]

c=0
vers=0

def packet():
    global c
    global vers
    version=int(bits[c:c+3],2)
    vers+=version
    c+=3
    typ=int(bits[c:c+3],2)
    c+=3
    val=0
    if typ==4:
        while True:
            val=val*16+int(bits[c+1:c+5],2)
            c+=5
            if bits[c-5]=="0":
                break
    else:
        lis=[]
        if bits[c]=="0":
            length=int(bits[c+1:c+16],2)
            c+=16
            p=c+length
            while c<p:
                lis.append(packet())
        else:
            pack_num=int(bits[c+1:c+12],2)
            c+=12
            for _ in range(pack_num):
                lis.append(packet())
        if typ==0:
            val=sum(lis)
        elif typ==1:
            val=np.prod(lis)
        elif typ==2:
            val=min(lis)
        elif typ==3:
            val=max(lis)
        elif typ==5:
            val=lis[0]>lis[1]
        elif typ==6:
            val=lis[0]<lis[1]
        else:
            val=lis[0]==lis[1]

    return val
 
print("Aufgabe 2: ",packet())

print("Aufgabe 1: ",vers)