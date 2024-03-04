import string
def files():
    for i in string.ascii_uppercase:
        name = f"{i}.txt" 
        with open(name, 'w') as file:
            file.write("text")

files()