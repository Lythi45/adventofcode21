import numpy as np

lines=open("input04.txt","r").readlines()
numbers=map(int,lines[0].split(","))
posis={}
fields=[]
fields_s=[]
win_boards=[]
win_msum=[]

def check_win(n):
    return np.prod([sum(row) for row in fields_s[n]])==0 or\
           np.prod([sum(column) for column in np.transpose(fields_s[n])])==0

def unmarked_sum(n):
    return sum([sum(np.multiply(row,row_s)) for row,row_s in zip(fields[n],fields_s[n])])

for i in range(len(lines)//6):
    field=[]
    field_s=[]
    for y in range(5):
        row=list(map(int,lines[2+i*6+y].split()))
        for x,n in enumerate(row):
            if n not in posis:
                posis[n]=[]
            posis[n].append((i,x,y))
        field.append(row)
        field_s.append([1]*5)
    fields.append(field)
    fields_s.append(field_s)


for n in numbers:
    for po in posis[n]:
        fields_s[po[0]][po[2]][po[1]]=0
        if po[0] not in win_boards and check_win(po[0]):
            win_boards.append(po[0])
            win_msum.append(n*unmarked_sum(po[0]))

print(win_msum[0])
print(win_msum[-1])

