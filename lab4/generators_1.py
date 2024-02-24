def sq(n):
    for i in range(1, n + 1):
        yield i**2
n= int(input(" n: "))
squares = sq(n)
for square in squares:
    print(square)
