str=input()
def palindrome(str):
    newstr=str[::-1]
    if str==newstr:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome(str)