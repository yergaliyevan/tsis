import os
def list_specific(path):
    dir = [i for i in os.listdir(path) if os.path.isdir(i)]
    files = [i for i in os.listdir(path) if os.path.isfile(i)]
    return dir, files

def list_all(path):
    all_dir = []
    all_files = []
    a=os.walk(path)
    for ( dr, fl) in a:
        all_dir.extend(dr)
        all_files.extend(fl)
    return all_dir, all_files
path = '/Users/mwtl2rua/workspace/1lab/lab3'
dir, files = list_specific(path)
print("Directories in this path:", dir)
print("Files in this path:", files)

all_dir, all_files = list_all(path)
print("All Directories in this path:", all_dir)
print("All Files in this path:", all_files)