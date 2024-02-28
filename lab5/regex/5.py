import re

p=r"a[a-zA-Z-_0-9]*b"

s=input()

if re.match(p, s):
    print("matched")
else:
    print("not matched")