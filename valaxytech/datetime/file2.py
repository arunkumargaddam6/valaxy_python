# identify the older file and remove
import os
import sys
import datetime
age=3
req_path=input("enter your path: ")

if not os.path.exists(req_path):
    print("please provide valid path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("please provide the directory path")
    sys.exit(2)
today=datetime.datetime.now()

for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days=(today-file_cre_date).days
        if diff_days > age:
            print(each_file_path,diff_days)