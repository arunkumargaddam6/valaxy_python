def myfunc():

    print ("hello user")
myfunc()
######################

def myfunc():

    print ("hello user")
print ("top")
myfunc()
print("bottom")
###################
def myfunc(name):

    print ("hello user "+ name)
myfunc("arun")
myfunc("radha")

###########

def myfunc(name, age):

    print ("hello user "+ name + "you are "+ age)
myfunc("arun", "35")
myfunc("radha", "34")

def myfunc(*name):
    print(name)
myfunc(10,20,30,40)

def myfunc(*name):
    print(name[2])
myfunc(10,20,30,40)