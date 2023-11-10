class Person:
    def __init__(self, name):
        self.name = name

    def swimmer(self):
        return False

class Swimmer(Person):
    def swimmer(self):
        return True

p = Person('Rinki')
print(p.swimmer())
s = Swimmer('Yash')
print(s.swimmer())
