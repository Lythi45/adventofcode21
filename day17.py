from parse import parse

input=open("input17.txt","r").read().strip()
xa,xb,ya,yb=parse("target area: x={:d}..{:d}, y={:d}..{:d}",input)

xs=0
for i in range(20):
    if (i*(i+1))//2 in range(xa,xb+1):
        xss=i
yss=-ya-1

my=(yss*(yss+1))//2
print(my)

sum=0

for x in range(xss,xb+1):
    for y in range(ya,yss+1):
        xs=x
        ys=y
        xp=0
        yp=0
        while(yp>=ya):
            xp+=xs
            if xs>0:
                xs-=1
            yp+=ys
            ys-=1
            if xp>=xa and xp<=xb and yp>=ya and yp<=yb:
                sum+=1
                break

print(sum)