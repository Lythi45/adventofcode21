field=[list(map(int,line.strip())) for line in open("input11.txt","r").readlines()]

dirs=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
xs=len(field[0])
ys=len(field)
p_flc=0
flc=0

for step in range(100000000):
    if step==100:
        print(flc)
    if flc==p_flc+xs*ys:
        print(step)
        break
    p_flc=flc
    field=[list(map(lambda x:x+1,row))for row in field]
    flashes=True
    while flashes:
        flashes=False
        for x in range(xs):
            for y in range(ys):
                if field[y][x]>9:
                    flashes=True
                    field[y][x]=0
                    flc+=1
                    for dx,dy in dirs:
                        if x+dx in range(xs) and y+dy in range(ys):
                            if field[y+dy][x+dx]>0:
                                field[y+dy][x+dx]+=1