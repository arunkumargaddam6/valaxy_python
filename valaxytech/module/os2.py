# clear screen of any operating system with one python script
import os
import platform

if platform.system()=="windows":
    os.system("cls")
else:
    os.system("clear")