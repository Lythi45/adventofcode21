s_bacons=[]
s_dvalues=[]
scanner=[]
ln=1
lines=open("input19.txt","r").readlines()
#print(len(lines))
while ln<len(lines):
    #print(ln,len(lines))
    bacons=[]
    #print(ln,lines[ln])
    while lines[ln]!="\n":
        bacons.append(list(map(int,lines[ln].split(","))))
        ln+=1
    s_bacons.append(bacons)
    ln+=2

for bcns in s_bacons:
    dvalues=[]
    for d in range(3):
        dvalues.append(list(map(lambda x:x[d],bcns)))
    s_dvalues.append(dvalues)
    scanner.append([[0,0,0]])

print(scanner)

def transform_merge(a,b,matcha,matchb,d0,f0,d1,f1,d2,f2):
    #print(len(s_bacons[a]),len(s_bacons[b]))
    #print(s_bacons[a])
    #print(s_bacons[b])

    dm=[d0,d1,d2]
    #s_pos=[s_dvalues[a][i][matcha]-s_dvalues[b][dm[i]][matchb]  for i in range(3)]
    #print("Dims: ",d0,d1,d2,f0,f1,f2,matcha,matchb)
    
    for beacon in  s_bacons[b]:
        t_b=[0,0,0]
        t_b[0]=f0*(beacon[d0]-s_dvalues[b][d0][matchb])+s_dvalues[a][0][matcha]
        t_b[1]=f1*(beacon[d1]-s_dvalues[b][d1][matchb])+s_dvalues[a][1][matcha]
        t_b[2]=f2*(beacon[d2]-s_dvalues[b][d2][matchb])+s_dvalues[a][2][matcha]
        if t_b not in s_bacons[a]:
            #print("Not match: ",t_b)
            s_bacons[a].append(t_b)
            for i in range(3):
                s_dvalues[a][i].append(t_b[i])

    for beacon in  scanner[b]:
        t_b=[0,0,0]
        t_b[0]=f0*(beacon[d0]-s_dvalues[b][d0][matchb])+s_dvalues[a][0][matcha]
        t_b[1]=f1*(beacon[d1]-s_dvalues[b][d1][matchb])+s_dvalues[a][1][matcha]
        t_b[2]=f2*(beacon[d2]-s_dvalues[b][d2][matchb])+s_dvalues[a][2][matcha]
        scanner[a].append(t_b)
    
    #print(len(s_bacons[a]))


def check(b,matcha,matchb,bdim,matchl):
    rdims=set([0,1,2])-set([bdim]) 
    #print(rdims)
    for bdim1 in rdims:
        bdim2=(rdims-set([bdim1])).pop()
        for flip1 in range(-1,2,2):
            for flip2 in range(-1,2,2):
                match=0
                #print("Flipflip: ",bdim1,bdim2,flip1,flip2)
                for i in matchl:
                    if flip1*(s_dvalues[b][bdim1][i]-s_dvalues[b][bdim1][matchb])+s_dvalues[a][1][matcha] in s_dvalues[a][1] and \
                       flip2*(s_dvalues[b][bdim2][i]-s_dvalues[b][bdim2][matchb])+s_dvalues[a][2][matcha] in s_dvalues[a][2]:
                       match+=1
                if match>=12:
                    return True,bdim1,bdim2,flip1,flip2
    return False,0,0,0,0


not_matched=set(range(1,len(s_bacons)))

while(len(not_matched)>0):
    bset=set(not_matched)
    print("Neue Runde")
    for a in range(len(s_bacons)):
        bset-=set([a])
        for b in set(bset):
            #print("B: ",a,b)
            matched=False
            for bdim in range(3):
                for matcha in range(len(s_bacons[a])):
                    vala=s_dvalues[a][0][matcha]
                    for flip in range(-1,2,2):
                        for matchb in range(len(s_bacons[b])):
                            valb=s_dvalues[b][bdim][matchb]
                            if a==0 and b==2:
                                xx=flip*valb+vala
                            match=0
                            matchl=[]
                            for i in range(len(s_bacons[b])):
                                if flip*(s_dvalues[b][bdim][i]-valb)+vala in s_dvalues[a][0]:
                                    match+=1
                                    matchl.append(i)
                            if match>=12:
                                print("Match:",a,b,flip,bdim,matcha,matchb,vala,valb)
                                #for k in matchl:
                                #    print(k,flip*(s_bacons[b][k][bdim]-valb)+vala)
                                ch,d1,d2,f1,f2=check(b,matcha,matchb,bdim,matchl)
                                if ch:
                                    bset-=set([b])
                                    print("Final: ",a,b,d1,d2,f1,f2)
                                    matched=True
                                    transform_merge(a,b,matcha,matchb,bdim,flip,d1,f1,d2,f2)
                                    not_matched-=set([b])
                                    print(not_matched)
                                    break
                        if matched:
                            break
                    if matched:
                        break
                if matched:
                    break

print(len(s_bacons[0]))

print(scanner)

print(max([max([sum([abs(scanner[0][i][d]-scanner[0][j][d]) for d in range(3)]) for j in range(0,i)]) for i in range(1,len(scanner[0]))]))


        






                

                
                





                            

                    








