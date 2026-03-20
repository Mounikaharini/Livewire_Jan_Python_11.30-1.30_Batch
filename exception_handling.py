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




