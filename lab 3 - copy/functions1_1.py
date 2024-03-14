ounces=float(input())
def convert(grams,ounces):
    grams=ounces/28.3495231
    return grams
#ex2
f=int(input())
c=(5/9)*(f-32)
print(c)
#ex3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
numheads = 35
numlegs = 94
a=solve(numheads,numlegs)
if a:
    chickens,rabbits=a
    print("chickens:",chickens)
    print("rabbits:",rabbits)
    #


  