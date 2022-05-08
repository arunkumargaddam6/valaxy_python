import re
my_str="This is about python. Python is easy to learn and we have two major versions: python2 and python3"

# my_pat=r'\bpython\b'
# print(re.findall(my_pat,my_str))

# my_pat=r'\b[Pp]ython\b'
# print(re.findall(my_pat,my_str))

my_pat=r'\bpython\b'
print(re.findall(my_pat,my_str,flags=re.I))

my_pat=r'\bpython[23]?\b'
print(re.findall(my_pat,my_str,flags=re.I))

