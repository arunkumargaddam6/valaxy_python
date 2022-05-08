#Sysntax

# re.research(Pattern,text)
# re.match(pattern,text)
# re.finditer(pattern,text)
# re.findall(pattern,text)
#\w  matches all the character except space
#\w\w match 2 characters toghther
#\W will give you spaces and special characters like @ # ! , 
#\d will give you decial 0-9 
# "." will give all the characters
#".." will give all the 2 characters
#.\ will give you only .
 #import re
# text= "this is a python and it is easy to learn"
# my_pat='is'
# print(re.findall(my_pat,text))

# text= "this is a python and it is easy to learn"
# my_pat='i[st]' # will search for is and it
# print(re.findall(my_pat,text))

# text= "this is a python and it is easy to learn"
# my_pat='[st]' # will search for s and t
# print(re.findall(my_pat,text))
import re
# my_pt="\w"
# text= "this is a python and it is easy to learn"
# print(re.findall(my_pt,text))

# my_pt="\w\w"
# text= "this is a python and it is easy to learn"
# print(re.findall(my_pt,text))

# my_pattern="python\d"
# text= "this is a python2 and it is easy to learn"
# print(re.findall(my_pattern,text))

text="this is my ip of a db server: 255.100.102.103"
pat="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(pat,text))