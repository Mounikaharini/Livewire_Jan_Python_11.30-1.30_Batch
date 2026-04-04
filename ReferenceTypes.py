#__doc__ string

"""This function is used for add three values."""
def add(a=0,b=0,c=0):
    """
    This function is used for add three values.
    If you miss any value from three of its , it will takes '0' as default
    """
    return a+b+c
"""If you miss any value from three of its,it will takes '0' as default"""
print(add(1,36,2))
print(add.__doc__)
print(__doc__)

#iterator
odd = [1,3,4,5,6,7,8,9,2]
o = iter(odd)

print(next(o))
print(next(o))
print(next(o))

n=len(odd)
for i in range(n):
    print(next(o))
    
#generator
def count(n):
    i=1
    while i<=n:
        if i%2!=0:
            yield i
        i+=1
x = list(count(5))
print(x)
y = count(10)
print(y)

#map
def str5(s):
    if len(s)==5:
        return s
def c(s):
    c=0
    for i in s:
        c+=1
    return s,c
st = ["python","filter","apple","map","vowel","catch"]
y=list(map(c,st))
print(y)

x=list(filter(c,st))
print(x)

#closure
def make_multiplier(x):
    
    def multiplier(n):
        return x * n
    
    return multiplier

times3 = make_multiplier(3)

print(times3(100))


#decorator
def f1(f2):
    f2()
@f1
def h1():
    print("hello")
@f1
def h2():
    print("bye")
