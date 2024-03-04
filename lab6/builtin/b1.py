def n(numb):
    res = 1
    for number in numb:
        res *= number
    return res

a= input()
numb = [int(number) for number in a.split()]
print(n(numb))
