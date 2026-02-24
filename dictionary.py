
#Dictionaries are key-value pairs, mutable and unordered

d = {"python":"60","java":"64","WD":"48"}
print(d)
print(d["python"])
print(d.get("python"))
d.pop("python")
print(d)
print(d.keys())
print(d.values())
print(d.items())
d.update({"python":"60"})
print(d)
d["WD"]="50"
print(d)
#del d
print(d)
for i in d:
   print(i,' : ',d[i])
m={
   "st1":{"Name":"Prathika","Age":22,"Course":"Python"},
   "st2":{"Name":"Priya","Age":22,"Course":"Java"},
   "st3":{"Name":"Vino","Age":22,"Course":"Django"}}
print(m)
print(m["st1"])
print(m["st1"]["Name"])
m.clear()
