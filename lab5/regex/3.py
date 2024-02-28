import re
with open('row.txt','r', encoding='utf-8') as file:
    inf=file.read()
    matches=re.findall(r'[a-z]+_[a-z]+', inf)
    
    for match in matches:
        print(match)