
nums=input().split()
myList=[int(x) for x in nums]
def filter_prime(i):
    primeList=[]
    for num in i:
        div=2
        while div<num:
            if num%div!=0:
                div+=1
            else:
                break
        if num==div and num>1:
            primeList.append(num)
            
    print(primeList)

filter_prime(myList)

