
import math
# num = input()
def is_prime(num):
    '''Check if num is prime or not.'''
    # raise TypeError for invalid input type
    if type(num) != int:
        # breakpoint()
        # print('error')
        raise TypeError('num is of invalid type')

    # raise ValueError for invalid input value
    if num < 0:
        raise ValueError('Check the value of num; is num a non-negative integer?')
    # for valid input, proceed to check if num is prime
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
is_prime('dfghj')
# is_prime(num)
# def upper_lower(word):
#     # word = input('Change uppper to lower and vice versa: ')
#     nword = ''
#     for w in word:
#         if w.islower():
#             nword += w.upper()
#             # print(nword)
#
#         else:
#             nword += w.lower()
#             # print(nword)
#     return nword
# print(upper_lower('word'))