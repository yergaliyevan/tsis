def a(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def b(f):
    with open(f, "r") as file:
        print(file.read())


filename="/Users/mwtl2rua/workspace/1lab/lab6/dirandfile/t.txt"

a(filename)

b(filename)