field=[list(map(int,line.strip())) for line in open("input15.txt","r").readlines()]

dirs=[(0,1),(1,0),(-1,0),(0,-1)]
xs=len(field[0])
ys=len(field)
dists=[[999999]*xs for _ in range(ys)]
dists[0][0]=0
active=True
while active:
    active=False
    for x in range(xs):
        for y in range(ys):
            for xd,yd in dirs:
                px=x+xd
                py=y+yd
                if px in range(xs) and py in range(ys):
                    if dists[py][px]>dists[y][x]+field[py][px]:
                        active=True
                        dists[py][px]=dists[y][x]+field[py][px]

print(dists[-1][-1])

def shift(v,n):
    return ((v-1)+n)%9+1

field5=[]
for y in range(ys*5):
    field5.append([ shift(field[y%ys][x%xs],x//xs+y//ys) for x in range(xs*5)])
   
xs*=5
ys*=5
dists=[[999999]*xs for _ in range(ys)]
dists[0][0]=0
active=True
while active:
    active=False
    for x in range(xs):
        for y in range(ys):
            for xd,yd in dirs:
                px=x+xd
                py=y+yd
                if px in range(xs) and py in range(ys):
                    if dists[py][px]>dists[y][x]+field5[py][px]:
                        active=True
                        dists[py][px]=dists[y][x]+field5[py][px]

print(dists[-1][-1])