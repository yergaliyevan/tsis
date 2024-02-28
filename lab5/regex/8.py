import re
s=input()
x=re.split("[A-Z]", s)
new_str=""
for i in x:
    new_str=new_str+" "+i
print(new_str)