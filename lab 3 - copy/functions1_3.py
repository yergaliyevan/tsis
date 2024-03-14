heads=int(input())
legs=int(input())
def solve():
    rabbit=int((legs-2*heads)/2)
    chicken=int(heads-rabbit)
    print("rabbits number is:", rabbit, "and chickens are:" , chicken)
    
solve()
    