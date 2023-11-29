from exceptions import InvalidInputException

class Calculator:

    def __init__(self):
        print('Calculator \n')
        # try:
        self.a = input('enter first number: ')
        self.b = input('enter second number: ')
        if not (self.a.isdigit() and self.b.isdigit()):
            raise InvalidInputException
        else:
            self.a = int(self.a)
            self.b = int(self.b)


    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

c = Calculator()
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())