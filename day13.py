points=set()
parts=open("input13.txt","r").read().split("\n\n")
for line in parts[0].split("\n"):
    x,y=map(int,line.split(","))
    points.add((x,y))

for line in parts[1].split("\n"):
    axis,number=line.split("=")
    number=int(number)
    np=set()
    for p in points:
        if axis[-1]=="x" and p[0]>number:
            np.add((2*number-p[0],p[1]))
        elif axis[-1]=="y" and p[1]>number:
            np.add((p[0],2*number-p[1]))
        else:
            np.add(p)
    points=np
    print(len(points))
for y in range(10):
    print("".join([[".","#"][(x,y) in points] for x in range(50)]))

