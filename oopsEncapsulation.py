'''
class Employee:
    def __init__(self, name, salary):
        self.name = name              # Public attribute
        self.__salary = salary        # Private attribute

    # Getter method
    def get_salary(self):
        return self.__salary
    
    # Setter method
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")
            
emp = Employee("Fedrick", 50000)
print(emp.name)
print(emp.get_salary())

emp.set_salary(20000)
print(emp.name)
print(emp.get_salary())

class Smartphone:
    
    def __init__(self, brand, model,storageCapacity):
        self.__brand = brand
        self.__model = model
        self.__storageCapacity = storageCapacity
        
    def getbrand(self):
        return self.__brand
    def getModel(self):
        return self.__model
    def getStorageCapacity(self):
        return  self.__storageCapacity

'''
class Smartphone:
    
    def __init__(self):
        pass
        '''
        self.__brand = brand 
        self.__model = model
        self.__storageCapacity = storageCapacity 
        '''
    def setter(self,brand,model,storageCapacity):
        self.__brand = brand 
        self.__model = model
        self.__storageCapacity = storageCapacity 
        
    def getbrand(self):
        return self.__brand
    def getModel(self):
        return self.__model
    def getStorageCapacity(self):
        return self.__storageCapacity
    
#s = Smartphone("VIVO","A 57","256GB")
s = Smartphone()
s.setter("VIVO","A 57","256GB")
print(s.getbrand())
print(s.getModel())
print(s.getStorageCapacity())


