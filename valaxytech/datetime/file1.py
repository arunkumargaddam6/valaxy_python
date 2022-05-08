import datetime

print(datetime.datetime.today())
#print(datetime.datetime.now('ist'))
print(datetime.datetime.now().year)

# string format time - strftime - strftime.org
print(datetime.datetime.now().strftime("%y-%m-%d"))

#fromtimestamp

print(datetime.datetime.fromtimestamp(15555555))