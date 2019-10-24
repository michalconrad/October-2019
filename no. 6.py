import os
import time

dir = input("Enter directory name: ")

if not os.path.isdir(dir):
    print(f"{dir} must be a directory")

else:
    file = input(f"Enter filename saved in directory {dir}: ")

    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print(f"{path} file does't exist!")

    else:
        print(f"displaying properties of file {path}")
        print("Last modify date is: ", time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))
        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))
