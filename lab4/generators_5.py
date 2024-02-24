n=int(input("n:"))
def down(n):
    while n>=0:
       yield n
       n-=1
for num in down(n):
    print(num)
