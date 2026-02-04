#jumping statements
for i in range(1,6,1):
    if i==3:
        break
    print(i)

for i in range(1,6,1):
    if i==3:
        continue
    print(i)

for i in range(1,6,1):
    if i == 3:
        pass
    print(i)

#strings    
a="hello world"
print(a[0:5])
print(a[6:11])
print(a[6])
print(a[0:])
print(a[:11])
print(a[:])
print(a[::-1])

s="eye"
if s == s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#case conversion
x="ThIs Is PyThOn ClAsS"
print(x.lower())
print(x.upper())
print(x.title())
print(x.capitalize())
print(x.swapcase())

#testing
print("1989".isdigit())
print("Mounika".isalpha())
print(" ".isspace())
print("mo1201".isalnum())
print("mounika".islower())
print("MOUNIKA".isupper())
print("Mounika".istitle())

#trimming whitespace

a="     hi      "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

#search and replace

y="programming language"
print(y.find('ln'))
print(y.rfind('g'))
print(y.count('g'))
print(len(y))
print(y.index('g'))











