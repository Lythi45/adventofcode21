from collections import defaultdict
fishes=defaultdict(int)

for cycle in open("input06.txt","r").read().split(","):
    fishes[int(cycle)]+=1

for i in range(256):
    fishes[9]=fishes[0]
    fishes[7]+=fishes[0]
    for j in range(9):
        fishes[j]=fishes[j+1]
    fishes[9]=0
    if i==80:
        print(sum(fishes.values()))
print(sum(fishes.values()))

