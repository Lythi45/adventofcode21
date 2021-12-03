lines=open("input02.txt","r").readlines()
dep=0
dep2=0
fo=0
for l in lines:
    c=l.split()
    co=c[0]
    nu=int(c[1])
    if co=="forward": 
        fo+=nu
        dep2+=dep*nu
    elif co=="down":
        dep+=nu
    else:
        dep-=nu
print(dep*fo)
print(dep2*fo)

