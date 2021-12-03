lines=list(map(lambda x:x.strip(),open("input03.txt","r").readlines()))
nl=len(lines)
zl=len(lines[0])
z=0
for i in range(zl):
    z=z*2+(sum([int(line[i]) for line in lines])>=nl//2)

print(z*(2**zl-1-z))

mu=1
new_lines=lines.copy()
for bit in [True,False]:
    i=0
    lines=new_lines.copy()
    while len(lines)>1:
        choosen_bitstate=bit==(sum([int(line[i]) for line in lines])>=len(lines)/2)
        lines=list(filter(lambda x:int(x[i])==choosen_bitstate,lines))
        i+=1
    mu*=int(lines[0],2)
print(mu)
            
        



