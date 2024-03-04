
import os
def check(path):
    if not os.path.exists(path):
        print("not exist")
        return
    if not os.access(path, os.R_OK):
        print("not readable.")
    else:
        print("readable.")
    if not os.access(path, os.W_OK):
        print("not writable.")
    else:
        print("writable.")
    if not os.access(path, os.X_OK):
        print("not executable.")
    else:
        print("executable.")
path ="/Users/mwtl2rua/workspace/1lab/lab3"
check(path)