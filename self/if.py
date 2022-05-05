is_male = False

if is_male:
    print ("you are a male")
else:
    print ("you are a female")

#############################
#boolean

is_male = True
is_tall = True

if is_male or is_tall: # if is_male or is_tall: (both conditions have to be true)
    print ("you are a male or tall or both")
else:
    print ("you are neither a male nor tall")

#################################

# ifelse statements comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print (max_num(300,4,5))
print (max_num(20,34,56))


