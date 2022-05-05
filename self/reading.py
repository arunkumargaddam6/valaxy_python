# a = append
# r = read
# w = write
# r+ = read and write
# write()
# read()


# empfile = open ("new.txt", "r")
# print (empfile.read())                # read out the text inside the file

# empfile = open ("new.txt", "r")
# print (empfile.readline())
# print (empfile.readline())

# empfile.close()

# empfile = open ("new.txt", "r")
# print (empfile.readlines()[2])

# empfile = open ("new.txt", "a")   # adding new line to the existing file
# empfile.write("\n bhoodevi")

empfile = open ("new1.txt", "w")
empfile.write("bhoodevi2")         #creating new file with text
empfile.close()

