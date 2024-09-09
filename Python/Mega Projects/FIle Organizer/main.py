import os
import shutil

path = input("Enter the Path: ")
files = os.listdir(path)

for file in files:
    filename, extention = os.path.splitext(file)
    extention = extention[1:]
    
    if os.path.exists(path+"/"+extention):
        shutil.move(path+"/"+file, path+"/"+extention+"/"+file)
    
    else:
        os.makedirs(path+"/"+extention)
        shutil.move(path+"/"+file, path+"/"+extention+"/"+file)
