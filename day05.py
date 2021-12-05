from collections import defaultdict

for modus in range(2):
    vents=defaultdict(int)
    for line in open("input05.txt","r").readlines():
        (x1,y1),(x2,y2)=map(lambda x:map(int,x.split(",")),line.split(" -> "))
        if x1==x2:
            ry=[1,-1][y1>y2]
            for y in range(y1,y2+ry,ry):
                vents[(x1,y)]+=1
        elif y1==y2:
            rx=[1,-1][x1>x2]
            for x in range(x1,x2+rx,rx):
                vents[(x,y1)]+=1
        elif modus==1:
            rx=[1,-1][x1>x2]
            ry=[1,-1][y1>y2]
            for x in range(x1,x2+rx,rx):
                y=y1+((x-x1)*rx)*ry
                vents[(x,y)]+=1

    print(sum(map(lambda x:x>1,vents.values())))


#shorter using ideas from my son

for modus in range(2):
    vents=defaultdict(int)
    for line in open("input05.txt","r").readlines():
        (x1,y1),(x2,y2)=map(lambda x:map(int,x.split(",")),line.split(" -> "))
        rx=[0,-1,1][(x1>x2)+2*(x2>x1)]
        ry=[0,-1,1][(y1>y2)+2*(y2>y1)]
        if modus==1 or x1==x2 or y1==y2:
            for l in range(max(abs(x2-x1),abs(y2-y1))+1):
                vents[(x1+l*rx,y1+l*ry)]+=1

    print(sum(map(lambda x:x>1,vents.values())))

for modus in range(2):
    vents=defaultdict(int)
    for line in open("input05.txt","r").readlines():
        (x1,y1),(x2,y2)=map(lambda x:map(int,x.split(",")),line.split(" -> "))
        le=max(abs(x2-x1),abs(y2-y1))
        if modus==1 or x1==x2 or y1==y2:
            for l in range(le+1):
                vents[(x1+l*(x2-x1)//le,y1+l*(y2-y1)//le)]+=1

    print(sum(map(lambda x:x>1,vents.values())))