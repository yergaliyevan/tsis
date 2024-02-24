n = int(input("n: "))
even = (i for i in range(n + 1) if i % 2 == 0)
numb = ', '.join(map(str, even))
print(f"Even numbers: {numb}")
