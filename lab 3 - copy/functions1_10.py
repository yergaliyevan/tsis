m=input().split()
def n(l):
    newL=[]
    for x in l:
        if l.count(x)>1:
            continue
        else:
            newL.append(x)
    print(newL)
n(m)