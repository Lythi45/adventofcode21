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
