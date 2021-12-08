sum=0
total=0
uniques={2:1,3:7,4:4,7:8}
wires=[0]*10

for line in open("input08.txt","r").readlines():
    parts=line.split("|")
    seg=map(lambda x:x.strip(),parts[1].split())
    for s in seg:
        if len(s) in [2,3,4,7]:
            sum+=1

    digits=list(map(lambda x:set(x.strip()),parts[0].split()))
    for d in digits:
        if len(d) in uniques:
            wires[uniques[len(d)]]=d
    for d in digits:
        if len(d) not in uniques:
            if len(d)==5: 
                if wires[1] <= d:
                    wires[3]=d
                elif  (wires[4]-wires[1]) <= d:
                    wires[5]=d
                else:
                    wires[2]=d
            else:    #6
                if wires[4] <= d:
                    wires[9]=d
                elif wires[1] <= d:
                    wires[0]=d
                else:
                    wires[6]=d
    num=0
    for s in map(lambda x:set(x.strip()),parts[1].split()):
        num=num*10+wires.index(set(s))
    total+=num

print(sum)
print(total)

    


