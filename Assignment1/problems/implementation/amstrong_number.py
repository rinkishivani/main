from Assignment1.base import AbstractClass


class ArmstrongNumber(AbstractClass):

    def __init__(self, num):
        self.num = num

    def run(self):
        """To determine whether number is an Armstrong number """
        digits = len(str(self.num))
        # print(type(digits))

        armstrong_num = 0

        for num in str(self.num):
            # print(num)
            armstrong_num += int(num) ** digits
            print(armstrong_num)
        if self.num == armstrong_num:
            return True
        return False


armstrong_obj = ArmstrongNumber()
armstrong_obj.run()
