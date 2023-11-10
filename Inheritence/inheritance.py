class Person:
    # def __init__(self, name):
    #     self.name = name

    def getName(self, name):
        print(name)

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

a = Person('Yash')
a.getName()
print(a.isEmployee())

b = Employee('Rinki')
b.getName()
print(b.isEmployee())