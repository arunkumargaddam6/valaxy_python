#search will look in all the lines
#match will look only at the begining or 0th index

import re

text="thi is for python and there are two major vers python2 and python3 in future python4"

pat=r"\bpythonn\b"
match_job=re.search(pat,text)
# print(match_job.group())

if match_job:
    print("match for your pattern: ",match_job.group())
    print('starting index :', match_job.start())
else:
    print("no match found")

#goup
#start
#end