
try:
    value = 10/0
    number = int(input("please enter number: "))
    print (number)
except ZeroDivisionError:
    print("divided by zero")
except ValueError:
    print ("invalid input")
    
