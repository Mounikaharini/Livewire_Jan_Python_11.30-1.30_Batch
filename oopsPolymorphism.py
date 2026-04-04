#operator overloading
'''
#example 1
print(10+20)
print("hi"+"hi") #concatenation

#example 2
print(2*3)
print("hi"*3) #repeatation
'''
#function overloading
class Calculator():
    
    def add(self,a=0,b=0,c=0,d=0):
        print(a+b+c+d)
        
    def mul(self,a=1,b=1,c=1,d=1):
        print(a*b*c*d)
        
c = Calculator()
c.add(1)       #a=1,b=0,c=0,d=0 -> a+b+c+d -> 1+0+0+0 = 1
c.add(1,2)     #a=1,b=2,c=0,d=0 -> a+b+c+d -> 1+2+0+0 = 3
c.add(1,2,3)   #a=1,b=2,c=3,d=0 -> a+b+c+d -> 1+2+3+0 = 6
c.add(1,2,3,4) #a=1,b=2,c=3,d=4 -> a+b+c+d -> 1+2+3+4 = 10

c = Calculator()
c.mul(1)       #a=1,b=0,c=0,d=0 -> a*b*c*d -> 1*1*1*1 = 1
c.mul(1,2)     #a=1,b=2,c=0,d=0 -> a*b*c*d -> 1*2*1*1 = 2
c.mul(1,2,3)   #a=1,b=2,c=3,d=0 -> a*b*c*d -> 1*2*3*1 = 6
c.mul(1,2,3,4) #a=1,b=2,c=3,d=4 -> a*b*c*d -> 1*2*3*4 = 24










