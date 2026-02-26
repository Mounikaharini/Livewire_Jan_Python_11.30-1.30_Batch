
#default argument
def greet(name="guest"):
    print("Welcome ",name)
greet("Mounika")
greet()


#keyword argument
def employee(name,age,role,seating):
    print(f"Name : {name}\nAge   : {age}\nRole  : {role}\nseat  : {seating}")

employee(role="Developer",age=22,name="Pavi",seating=102)

#variable - length argument
#for values only
def evenPrint(*n):     #n=(1,2,3,4,5,6,7,8,9,10)
    for i in n:
        if i%2==0:
            print(i)
evenPrint(1,2,3,4,5,6,7,8,9,10)

#for key and value
def employeeList(**emp):
    for i in emp:
        print(i ,":",emp[i])
employeeList(Id1="Mounika",Id2="Prathika",Id3="Vino")

def hi():
    print("hi")
    hi()
hi()

def login():
    un = input("Enter the Username : ")
    pw = input("Enter the Password : ")
    if un=="admin" and pw=="1234":
        print("Login Successfull")
    else:
        print("Invalid Username or password")
        login()
login()

#counter based login
c=0 #1-2-3-4
def login(c):
    c+=1
    if c==4:
        return
    else:
        un = input("Enter the Username : ")
        pw = input("Enter the Password : ")
        if un=="admin" and pw=="1234":
            print("Login Successfull")
        else:
            print("Invalid Username or password")
            login(c)
login(c)

#lamba function

def square(x):
    return x*x
l = square(5)
print(l)

square = lambda x : x*x
print(square(5))

check = lambda y : y%2==0
print(check(9))

#map function

def count(s):
    c = 0
    for i in s:
        c+=1
    return s,c
s = ["welcome","to","python","class"]
output = list(map(count,s))
print(output)

#filter function

def is_alphabet(s):
    return s.isalpha()

s = ["welcome","123","to","123","python","20.6396854","class"]
output = list(filter(is_alphabet,s))
print(output)

