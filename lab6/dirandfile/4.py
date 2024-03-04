def count(files):
    with open(files, "r") as file:
        num=0
        for l in file:
            num+=1
    return num
name="/Users/mwtl2rua/workspace/1lab/lab6/dirandfile/t.txt"
print("number of lines:", count(name))