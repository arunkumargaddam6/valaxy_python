# copy content from source file to dest file

file1=input("enter the file name: ")
file2= input("enter the dest path: ")


fo=open(file1,'r')
content=fo.read()
fo.close()



fo=open(file2,'w')
fo.write(content)
fo.close()