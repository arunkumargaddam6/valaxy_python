import os
import sys
path=input("please enter the file path: ")
if os.path.exists(path):
    my_list=os.listdir(path)
else:
    print("please provide the valid path")
    sys.exit()

# p1=os.path.join(path,my_list[0])
# if os.path.isfile(p1):
#     print(f"{p1} is a file")
# else:
#     print(f"{p1} is a directory")
for each_list in my_list:
    file_path=os.path.join(path,each_list)
    print(file_path)
