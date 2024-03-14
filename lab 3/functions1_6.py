string=input()
def reverse(s):
    newStr=""  
    ind=len(s)-1  
    while ind>=0:
        endInd=ind 
        while ind>=0 and s[ind]!=" ":
            ind-=1  
        newStr+=s[ind+1:endInd+1]+" " 
        ind-=1  
    print(newStr)
reverse(string)