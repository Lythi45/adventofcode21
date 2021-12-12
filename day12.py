from collections import defaultdict
links={}

for line in open("input12.txt","r").readlines():
    l1,l2=list(map(lambda x:x.strip(),line.split("-")))
    if l1 in links:
        links[l1].append(l2)
    else:
        links[l1]=[l2]
    if l2 in links:
        links[l2].append(l1)
    else:
        links[l2]=[l1]
    
num=0

def path_s(fr,visited):
    global num
    if fr[0]>="a":
        visited.add(fr)
    if fr=="end":
        num+=1
    else:
        for to in links[fr]:
            if to not in visited:
                path_s(to,visited)

    visited.discard(fr)

path_s("start",set())
print(num)

num=0

def path_s2(fr,visited,twice):
    global num
    if fr[0]>="a":
        if fr in visited:
            twice=fr
        else:
            visited.add(fr)
    if fr=="end":
        num+=1
    else:
        for to in links[fr]:
            if to!="start" and (to not in visited or twice==""):
                path_s2(to,visited,twice)

    if fr!=twice:
        visited.discard(fr)

path_s2("start",set(),"")
print(num)