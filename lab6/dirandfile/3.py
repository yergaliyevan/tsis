import os
def check(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print(f"The path does not exist: {path}")
path = '/Users/mwtl2rua/workspace/1lab/lab3'
check(path)
