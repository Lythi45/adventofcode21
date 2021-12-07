crabs=sorted(map(int,open("input07.txt","r").read().split(",")))

print(sum([abs(crab-crabs[len(crabs)//2]) for crab in crabs]))

def fuel(dist):
    return dist*(dist+1)//2

mid=int(sum(crabs)/len(crabs))

print(min([sum([fuel(abs(crab-mid)) for crab in crabs]),  
           sum([fuel(abs(crab-mid-1)) for crab in crabs])] ))

