#while syntax

'''initial value
while condition:
    code block
    increment / decrement
'''

# 1 2 3 4 5
for i in range(1,6,1):
    print(i,end=" ")

j = 1
while j<6:
    print(j,end=" ")
    j=j+1

# 5 4 3 2 1

for i in range(5,0,-1):
    print(i,end=" ")

i=5
while i>0:
    print(i,end=" ")
    i=i-1
    
'''25.A number is said to be Buzz Number if it ends with 7 or is divisible by 7.
Example: 1007 is a Buzz Number.Define a class Buzz number to read a number and check if it is a Buzz number or not   
'''
n=1007
if n%7==0 or n%10==7:
    print("Buzz Number")
else:
    print("Not Buzz Number")

#sum of digits
#12345 = 1+2+3+4+5=15
#452 = 4+5+2 = 11

n=12345
s=0
while n>0:
    m=n%10
    s=s+m
    n//=10
print(s)

#0 1 1 2 3 5 8 13 21 34 55 ........ n
#fibonacci series
n=50
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,n+1,1): 
    s=a+b
    if s>n:
        break
    print(s,end=" ")
    a,b=b,s

n=int(input("enter a number : "))
if n==0:
    print(1000)
else:
    c=0
    while n>0:
        n=n//10
        c+=1
    print(c)

# * * *
# * * *
# * * *

i=0
while i<3:
    j=0
    while j<3:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''
a
b b
c c c
d d d d
e e e e e'''

for i in range(1,6,1):
    for j in range(1,i+1,1):
         print(chr(96+i),end=" ")
    print()

for i in range(1,6,1):
    for j in range(1,i+1,1):
         print(chr(96+j),end=" ")
    print()
'''
a
a b
a b c
a b c d
a b c d e

* * * * *
*       *
*       *
*       *
* * * * *'''
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,6,1):
    for j in range(1,6,1):
        if i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j or i+j==6 or i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

