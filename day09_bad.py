import numpy as np

cave=list(map(lambda x:list("X"+x.strip()+"X"),open("input09.txt","r").readlines()))
xl=len(cave[0])
cave=[["X"]*xl]+cave+[["X"]*xl]
yl=len(cave)
dirs=[(1,0),(0,1),(-1,0),(0,-1)]

lowlist=[]

def lowest(x,y):
    lowest=sum(map(lambda r:cave[y+r[0]][x+r[1]]>cave[y][x],dirs))==4
    if lowest:
        lowlist.append((x,y))
    return lowest

def fill(x,y):
    if cave[y][x]<"9":
        cave[y][x]="9"
        return 1+sum([fill(x+d[0],y+d[1]) for d in dirs])
    else:
        return 0

print(sum([ sum( int(cave[y][x])+1 for x in range (1,xl-1) if lowest(x,y))for y in range(1,yl-1)]))

print(np.prod(sorted([fill(p[0],p[1]) for p in lowlist])[-3:]))




fill={}
nfill=0
cfill=[]
lost={}
for y in range(1,yl-1):
    for x in range(1,xl-1):
        if cave[y][x]<"9":
            if (x-1,y) in fill:
                fn=fill[(x-1,y)]
                fill[(x,y)]=fn
                cfill[fn]+=1
                if (x,y-1) in fill and fn!=fill[(x,y-1)]:
                    fnl=fill[(x,y-1)]
                    while fnl in lost and lost[fnl]!=fn:
                        fnl=lost[fnl]
                    cfill[fn]+=cfill[fnl]
                    cfill[fnl]=0
                    lost[fnl]=fn
            elif (x,y-1) in fill:
                fn=fill[(x,y-1)]
                fill[(x,y)]=fn
                cfill[fn]+=1
            else:
                fill[(x,y)]=nfill
                cfill.append(1)
                nfill+=1

while len(lost)>0:
    i,v= lost.popitem()
    cfill[v]+=cfill[i]
    cfill[i]=0

print(np.prod(sorted(cfill)[-3:]))

from PIL import Image, ImageDraw
img = Image.new('RGB', (xl, yl), color = 'black')

def color():
    return (np.random.randint(256),np.random.randint(256) ,np.random.randint(256)) 
clist={}
for i in range(nfill):
    j=i
    while j in lost:
        j=lost[j]
    if j not in clist:
        clist[j]=color()
    if j in lost:
        clist[j]=(200,200,200)
    clist[i]=clist[j]

for p,v in fill.items():
    img.putpixel(p,clist[v])

img.save('day09.png')