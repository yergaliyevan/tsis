def check(t):
    return all(t)
a = input()
tuple = tuple(int(item) for item in a.split())
print(check(tuple))
