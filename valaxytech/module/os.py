# os
# os.path
# os.system()
# os.walk()

#os
#=================

# os.getcwd() - current working directory
# os.chdir() - change dir
# os.listdir(path)
# os.mkdir(path)
# os.makedirs(path) - recursively
# os.rmdir(path)
# os.rename(src,dest)
# os.environ
# os.getuid() - userid
# os.getgid() - groupid
# os.getpid() - processid

# os.path
#===============================

#os.path.sep
#os.path.basename(path)
#os.path.dirname(path)
#os.path.join(path1,path2)
#os.path.split(path)
#os.path.getsize(path)
#os.path.exists(path)
#os.path.isfile(path)
#os.path.isdir(path)

#os.system()  is helpful to executie the operating system cmds with python
#===========================

#os.system("pwd")
#os.system("ls")

# if os command is successful it will return 0 as code 


import os

# file=input("enter file name: ")
# for r,d,f in os.walk('c\\:'):
#     for fi in f:
#         if file==fi:
#             print(os.path.join(r,f))

cmd="datee"
ls=os.system(cmd)
if ls == 0:
    print("you command is success")
else:
    print("unsuceessful")
