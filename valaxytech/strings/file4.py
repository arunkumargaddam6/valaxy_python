import os
w=os.get_terminal_size().columns
x=(input("enter your title: "))
print(x.center(w).title())
print(x.rjust(w))
