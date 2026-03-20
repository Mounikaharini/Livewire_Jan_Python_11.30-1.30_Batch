#Ex 1: Name error
try:
    a =10
    print(b)
except Exception as n:
    print(n)
finally:
    print('bye')

#Ex 2: Value error
try:
    a = int(input('Enter a number:'))
    print(a)
except Exception as b:
    print(b)

#Ex 3: Key Error
	a={'name':kio','Age':21}
	try:
    		print(a['Age'])
	except Exception as k:
    		print(k)

#Ex 4: Index Error
	a=[98,23,45]
	try:
   		 print(a[3])
	except Exception as e:
  		 print('Index Error:',e)

#Ex 5: Zero Division Error
try:
    print(5 / 10)
except Exception as a:
    print(a)

#finally
try:
    print(10/0)
except ZeroDivisionError as a:
    print(a)
finally:
    print("hi")

#assert
a=5
assert a==50
print(a)


a=5
assert a==50,'a is equal to 5'
print(a)

#raise

a=3
b=0
if b==0:
    raise ZeroDivisionError(‘This error is made by me   ’)
c=a+b
d=a-b
e=a/b
try:
    print(c,d,e)
except Exception as e:
    print(e)



