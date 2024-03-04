def files(f):
    with open(f, "r") as file:
        copy=file.read()
    newfile="newfile.txt"
    with open(newfile, "w") as file:
        file.write(copy)

files("/Users/mwtl2rua/workspace/1lab/lab6/dirandfile/t.txt")