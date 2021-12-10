su=0
pu_li=[]
p_br={")":1,"]":2,"}":3,">":4}
openb={"(":")","[":"]","{":"}","<":">"}
closeb={")":3,"]":57,"}":1197,">":25137}
for line in open("input10.txt","r").readlines():
    stack=[]
    for c in line.strip():
        if c in openb:
            stack.append(openb[c])
        else:
            p=stack.pop()
            if p!=c:
                su+=closeb[c]
                stack=[]
                break
    p=0
    while len(stack)>0:
        p=p*5+p_br[stack.pop()]
    if p>0:
        pu_li.append(p)

print(su)
print(sorted(pu_li)[len(pu_li)//2])