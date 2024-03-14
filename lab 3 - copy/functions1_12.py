num=input().split()
myList=[int(x) for x in num]
def histogram(l):
    for x in l:
        print("*"*x)
histogram(myList)