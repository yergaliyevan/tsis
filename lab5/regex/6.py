import re
p=r"[,. ]+"
r=":"
str=input()
new_s=re.sub(p, r, str)
print(new_s)