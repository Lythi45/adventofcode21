from collections import Counter,defaultdict

lines=open("input14.txt","r").readlines()
poly=lines[0].strip()
repl=[list(map(lambda x:x.strip(),l.split(" -> "))) for l in lines[2:]]

#works for 10, but not for 40
for i in range(0):
    rlist=[]
    for fi,re in repl:
        p=-1
        while True:
            p=poly.find(fi,p+1)
            if p>=0:
                rlist.append((p+1,re))
            else:
                break
    shift=0
    for po,re in sorted(rlist,key=lambda x:x[0]):
        poly=poly[:po+shift]+re+poly[po+shift:]
        shift+=1
    counts=sorted(Counter(poly).values())
    print(counts[-1],counts[0])

polyparts=defaultdict(int,{poly[p:p+2]:1 for p in range(len(poly)-1)})

for i in range(41):
    new_pps=defaultdict(int)
    if i==10 or i==40:
        sums=defaultdict(int)
        for pp,v in polyparts.items():
            sums[pp[0]]+=v
            sums[pp[1]]+=v
        sumsort=sorted([(x+1)//2 for x in sums.values() if x>0])
        print(sumsort[-1]-sumsort[0])
    for fi,re in repl:
        if fi in polyparts and polyparts[fi]>0:
            v=polyparts[fi]
            polyparts[fi]-=v
            new_pps[fi[0]+re]+=v
            new_pps[re+fi[1]]+=v
    for p,v in new_pps.items():
        polyparts[p]+=v
    



    