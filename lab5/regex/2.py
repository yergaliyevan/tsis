import re
with open('row.txt', 'r', encoding='utf-8') as file:
    data=file.read()
    list=[]
    dt=data.split()
    for i in dt:
        g=re.search(r'a.{2,3}b',i)
        if g:
            list.append(i)
            
print(list)