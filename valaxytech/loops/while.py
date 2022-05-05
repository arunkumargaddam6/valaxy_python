# while 1>10:
#     print("hello")
# import time
# while True:
#     print("hello")
#     time.sleep(1)

# value=1
# while value<5:
#     print("hello")
#     value=value+1

value=1
while value<5:
    print("hello")
    break
    value=value+1

for eacg in ['/usr/bin','/usr/bin/httpd','/usr/bin/kk']:
    if 'httpd' in eacg:
        print(eacg)
        break