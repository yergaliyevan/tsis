import re
s=input()
newstr=""

p=r"\w"
a=re.findall(p, s)

for i in a:
    if i.isupper() and i!=a[0]:
        newstr+="_"+i
    else:
        newstr+=i

print(newstr)