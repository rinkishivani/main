from Assignment1.base import AbstractClass


class Fibonacci(AbstractClass):

    def __int__(self, num):
        self.num = num

    def run(self):  # write Fibonacci series up to n
        a, b = 0, 1
        while a < self.num:
            print(a, end=' ')
            a, b = b, a + b


fibo_obj = Fibonacci()
fibo_obj.run()
