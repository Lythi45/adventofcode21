from numpy.core.overrides import verify_matching_signatures
for modus in range(2):
    vents={}
    for line in open("input05.txt","r").readlines():
        (x1,y1),(x2,y2)=list(map(lambda x:list(map(int,x.split(","))),line.split(" -> ")))
        if x1==x2:
            if y1>y2:
                y1,y2=y2,y1
            for y in range(y1,y2+1):
                if (x1,y) in vents:
                    vents[(x1,y)]+=1
                else:
                    vents[(x1,y)]=1
        elif y1==y2:
            if x1>x2:
                x1,x2=x2,x1
            for x in range(x1,x2+1):
                if (x,y1) in vents:
                    vents[(x,y1)]+=1
                else:
                    vents[(x,y1)]=1
        elif modus==1:
            rx=[1,-1][x1>x2]
            ry=[1,-1][y1>y2]
            for x in range(x1,x2+rx,rx):
                y=y1+((x-x1)*rx)*ry
                if (x,y) in vents:
                    vents[(x,y)]+=1
                else:
                    vents[(x,y)]=1

    print(sum(map(lambda x:x>1,vents.values())))