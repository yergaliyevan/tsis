import re
p=r"\w"
str=input()
x=re.findall(p, str)
newstr=""
for i in x:
    if i.isupper():
        newstr+=" "+i
    else:
        newstr+=i

print(newstr)