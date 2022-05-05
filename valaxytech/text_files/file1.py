#open file in write mode
fo=open('new.txt','w')
fo.write("this is first line\n")
fo.write("this is second line")
fo.close()

content=['firstline\n','secondline']
fo=open ('new1.txt','w')
fo.writelines(content)
fo.close()

content=['firstline','secondline','this is third line']
fo=open('new2.txt','w')
for c in content:
    fo.write(c+"\n")
fo.close()

#append text
content=['firstline','secondline','this is third line']
fo=open('new2.txt','a')
for c in content:
    fo.write(c+"\n")
fo.close()

fo=open('new2.txt','r')
data=fo.read()
fo.close()
print(data)

# to get the data as list
fo=open('new2.txt','r')
data=fo.readlines()
fo.close()

print(data)

fo=open('new2.txt','r')
data=fo.readlines()
fo.close()

for each in range(3):
    print(data[each])