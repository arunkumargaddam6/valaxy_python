import os
import platform
import time

def myfunc(a,b):
    print ("please wait it clears the screen")
    time.sleep(2)
    os.system(a)
  
    print("please wait it prints all the directories")
    time.sleep(2)
    os.system(b)
if platform.system()=="windows":
     myfunc ('clear','dir')
else:
    myfunc('clear','ls')