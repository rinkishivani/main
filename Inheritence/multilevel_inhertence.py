class Person:
    def __init__(self, name):
        self.name = name

    def is_person(self):
        return f'{self.name} is a person'


class Child(Person):
    def is_child(self):
        return f'{self.name} is child'


class Adult(Child):
    def is_adult(self):
        return f'{self.name} is an adult'


a = Adult('rinki')

print(a.is_person())
print(a.is_child())
print(a.is_adult())
