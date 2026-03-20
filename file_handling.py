f=open("file1.txt","w")
f.write("Welcome to python")
print("File Is Written")
f.close()

f=open("file2.txt","w")
f.write("Welcome to python")
print("File Is Written")
f.close()

f=open("file1.txt","a")
f.write("Text Append")
print("File Is Written")
f.close()

f=open("file1.txt","a")
a=input("Enter a text : ")
f.write(a)
print("File Is Written")
f.close()

print("Name of the file : ",f.name)
print("File is closed or not : ",f.closed)
print("Opening Mode of the File : "f.mode)

f=open("file1.txt","a")
a=input("Enter a text : ")
f.write(a)
print("File Is Written")
f.close()
f=open("file1.txt","r")
print(f.read())#read all characters
print(f.read(20)) #read only 20 characters
print(f.readline())#read the first line
print(f.readlines())#read the all line
print("Current position of the cursor : ",f.tell())
f.seek(0)#current function of the file cursor
f.close()

import os
os.getcwd()#get current directory
os.listdir()
os.rename('old name','new name')
os.remove('file name')
