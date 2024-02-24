n=int(input("n:"))
def numbers(n):
    for i in range(n+1):
        if n%3==0 and n%4==0:
            yield i
n=int(input("n:"))
print(numbers(n))