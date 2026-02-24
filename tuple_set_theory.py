#tuple

a = (1,2,3,4,5)
b= (6,7,8)
c= a + b
print(c)
print(b*2)
print(list(c))
print(tuple("python"))
print(c.index(7))

data = ("Id1","priya","100")
i_d , name , mark = data
print(i_d,name,mark)

s1 = {1,2,3,4}
s2 = {2,4,6,8}
s = {3,1,4,2}
s.add(5)
print(s)
s.update([1,3,5,7])
print(s)
s.remove(7)
print(s)
s.discard(5)
print(s)
s.pop()
print(s)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s2.difference(s1))
s1.intersection_update(s2)
print(s1)
s2.difference_update(s1)
print(s2)

x = {1,2}
y = {3,4}
print(x.isdisjoint(y))
u = {1,2,3,4,5}
v = {2,3}
print(u.issuperset(v))
print(v.issubset(u))
