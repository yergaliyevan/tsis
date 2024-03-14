string=input()
def str(s):
    s2=s[::-1]
    if s==s2:
        print("palindrome")
    else:
        print("not  palindrome")
str(string)