from numpy.core.overrides import verify_matching_signatures
for modus in range(2):
    vents={}
    for line in open("input05.txt","r").readlines():
        (x1,y1),(x2,y2)=list(map(lambda x:list(map(int,x.split(","))),line.split(" -> ")))
        if x1==x2:
            ry=[1,-1][y1>y2]
            for y in range(y1,y2+ry,ry):
                vents[(x1,y)]=vents.get((x1,y),0)+1
        elif y1==y2:
            rx=[1,-1][x1>x2]
            for x in range(x1,x2+rx,rx):
                vents[(x,y1)]=vents.get((x,y1),0)+1
        elif modus==1:
            rx=[1,-1][x1>x2]
            ry=[1,-1][y1>y2]
            for x in range(x1,x2+rx,rx):
                y=y1+((x-x1)*rx)*ry
                vents[(x,y)]=vents.get((x,y),0)+1

    print(sum(map(lambda x:x>1,vents.values())))