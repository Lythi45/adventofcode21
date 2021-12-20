lines=open("input20.txt","r").readlines()

lp=0
algo=""
dots=set()

while lines[lp]!="\n":
    algo+=lines[lp].strip()
    lp+=1

print(len(algo))

for row in range(lp+1,len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col]=="#":
            dots.add((col,row-lp-1))

startx=0
starty=0
endx=len(lines[lp+1].strip())+2
endy=len(lines)-lp-1+2

print(lp,startx,starty,endx,endy)

flip=False

print(len(dots))
for i in range(50):
    ndots=set()
    for y in range(starty,endy):
        line=""
        for x in range(startx,endx):
            ind=0
            for yy in range(3):
                for xx in range(3):
                    ind=ind*2
                    if (flip and ((x+xx-2) not in range(0,endx-2) or (y+yy-2) not in range(0,endy-2))) or (x+xx-2,y+yy-2) in dots:
                        ind+=1
            #print(x,y,ind,algo[ind])
            if algo[ind]=="#":
                ndots.add((x,y))
                line+="#"
            else:
                line+="."
        print(line)
    dots=ndots

    if algo[0]=="#":
        flip=not flip

    endx+=2
    endy+=2
    print(len(dots))


