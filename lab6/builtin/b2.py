str=input()
def countl(n):
    upper=sum(1 for i in n if i.isupper())
    lower=sum(1 for j in n if j.islower())
    return upper, lower

uppcount, lowcount=countl(str)
print("Upper case count:", uppcount, "\nLower case count :", lowcount)