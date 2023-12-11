from Assignment1.base import AbstractClass
import math


class PrimeNumber(AbstractClass):

    def __init(self, num):
        self.num = num

    def run(self):
        """Check if num is prime or not."""

        for i in range(2, int(math.sqrt(self.num)) + 1):
            if self.num % i == 0:
                return False
        return True


prime_obj = PrimeNumber()
prime_obj.run()
