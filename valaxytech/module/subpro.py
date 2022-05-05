import subprocess
cmd="java -version"
#cmd="ls -la".split() #shell=False
my=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=my.wait()
out,err=my.communicate()
# if rc==0:
#     if bool(out)==True:
#        print(out)

#     if bool(out)==False and bool(err)==True:
#         print(err.splitlines())
# else:
#     print(err)