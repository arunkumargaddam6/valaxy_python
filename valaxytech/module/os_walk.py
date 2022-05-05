# os.walk() will give you all the files and directories as list in the given path
import os 

path="C:\\Users\\Radha\\Desktop\\resume"
# print(list(os.walk(path)))

for r,d,f in os.walk(path):
    print(r,f)
    for each_file in f:
        print(each_file)