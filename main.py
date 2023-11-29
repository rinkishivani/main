# import math
# import time

# class Bird
# ==================================================================================================
# 07 Nov
# ==================================================================================================


# # class Stack:
#     print(' __________Enter number and push/pop (exit/out to exit)___ /
# _______')
#
#     def __new__(cls):
#         print("Creating instance")
#         return super(Stack, cls).__new__(cls)
#
#     def __init__(self):
#         print('init')
#         self.numbers = []
#         self.u_n = ''
#
#     def push(self, num):
#         self.numbers.append(num)
#
#     def pop(self, numbers, num):
#         numbers.remove(num)
#
#     def isempty(self, numbers):
#         if len(numbers) == 0:
#             return True
#         return False
#
#     def display(self):
#         print(self.numbers)
#
#     def operation(self):
#         while True:
#
#             print('stack - ', self.numbers)
#             u_n = list(input('enter: ').split())
#
#             if len(u_n) == 1:
#                 self.num, self.op = u_n
#
#             s = Stack()
#
#             if self.op == 'push':
#                 s.push(self.num)
#             elif self.num == 'display':
#                 s.display()
#             elif self.op == 'pop':
#                 if s.isempty():
#                     print('List is empty')
#                 else:
#                     s.pop(self.num)
#             elif self.num == 'exit' or self.num == 'out':
#                 break
#             elif self.num != '':
#                 print('Something went wrong!')
#
#
# operation_obj = Stack()
# operation_obj.operation()

# ==================================================================================================

# class Calculator:
#     ''' Simple Calculator'''
#
#     print(' \n Calculator')
#     print('Enter numbers for addtion, subtration, \
# multiplication and division respectivley \n')
#
#     def __init__(self):
#         # print('Calculator \n')
#         self.a = int(input('enter first number: '))
#         self.b = int(input('enter second number: '))
#
#     def add(self):
#         return f"Addtion {self.a + self.b}"
#
#     def sub(self):
#         return f'Subtraction {self.a - self.b}'
#
#     def mul(self):
#         return f' Multiplication {self.a * self.b}'
#
#     def div(self):
#         return f'Division {self.a / self.b}'
#
# add = Calculator()
# 'Addition'
# h = add.add()
#
# # print(type(h))
# print(add.add())
#
# sub = Calculator()
# print(sub.sub())
#
# mul = Calculator()
# print(mul.mul())
#
# div = Calculator()
# print(div.div())

# ==================================================================================================
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
# ==================================================================================================
# class Calculator:
#
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
# c = Calculator(10, 20)
# print(c.add())
# print(c.sub())
# print(c.mul())
# print(c.div())
# ==================================================================================================
#
# class Calculator:
#     def add(self, a, b):
#         return a+b
#
#     def sub(self, a, b):
#         return a-b
#
#     def mul(self, a, b):
#         return a*b
#
#     def div(self, a, b):
#         return a/b
# c = Calculator()
# print(c.add(1,2))
# print(c.sub(5,2))
# print(c.mul(1,3))
# print(c.div(9,3))
# ==================================================================================================

# class Employee:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.pie = 3.14
#
#     def names(self):
#         return self.name, self.age, self.pie
#
# e = Employee('Yash', 21)
# print(e.names())
# ==================================================================================================

# def hello_decorator(func):
#
#     def inner1(*args, **kwargs):
#
#         print("before Execution")
#
#         returned_value = func(*args, **kwargs)
#
#         print("after Execution")
#
#         return returned_value
#
#     return inner1
#
# @hello_decorator
#
# def sum_two_numbers(a, b):
#
#     print("Inside the function")
#
#     return a + b
#
# a, b = 1, 2
#
# print("Sum =", sum_two_numbers(a, b))

# ==================================================================================================

# def outter_one(fun):
#     print('pehle')
#     def inner_one():
#         print('inside')
#         fun()
#     return inner_one
#
#     def outter_two(a, b):
#         print("hello", a + b)
#
# variable1 = outter_one(outter_two)

# ==================================================================================================

# def create_adder(x):
#
#     def adder(y):
#         print(x)
#         print(y)
#         return x+y
#
#     return adder
#
# add_15 = create_adder(15)
#
# print(add_15(10))


# ==================================================================================================
# 03 Nov
# ==================================================================================================

# ==================================================================================================
# 02 Nov
# ==================================================================================================
# for i in range(1,65):
#     grains = 2**(i - 1)
#     print(grains)
# ==================================================================================================
# 01 Nov
# ==================================================================================================

# define the 'EXPECTED_BAKE_TIME' constant.
# EXPECTED_BAKE_TIME = 40
#
#
# Remove 'pass' and complete the 'bake_time_remaining()' \
# function below.
# def bake_time_remaining(elapsed_bake_time):
#     """Calculate the bake time remaining.
#
#     :param elapsed_bake_time: int - baking time already elapsed.
#     :return: int - remaining bake time (in minutes) derived from \
# 'EXPECTED_BAKE_TIME'.
#
#     Function that takes the actual minutes the lasagna has been in the oven \
# as
#     an argument and returns how many minutes the lasagna still needs to bake
#     based on the `EXPECTED_BAKE_TIME`.
#     """
#
#     return EXPECTED_BAKE_TIME - elapsed_bake_time
#
#
# Define the 'preparation_time_in_minutes()' function below.
# # You might also consider using 'PREPARATION_TIME' here, if you have \
# it defined.
# def preparation_time_in_minutes(number_of_layers):
#     PREPARATION_TIME = number_of_layers * 2
#     return PREPARATION_TIME
#
#
# define the 'elapsed_time_in_minutes()' function below.
# def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
#     '''Calculate the elapsed time in minutes'''
#     prep = elapsed_time_in_minutes(number_of_layers)
#     return prep + EXPECTED_BAKE_TIME
# ==================================================================================================
# from fibo import fib2
# print(fib2(1000))

# l1 = (1,2,3,4,5)
# even_list = filter(lambda x : x%2 == 0, l1 )
# print(even_list)
# a = even_list
# print(a)
# print(type(range(10)))
# def even_list(x):
#     if x%2 == 0:
#         return True0x7fc0bf463850


# ==================================================================================================
# importing built-in module math
# import math
#
# # using square root(sqrt) function contained
# # in math module
# print(math.sqrt(25))
#
# # using pi function contained in math module
# print(math.pi)
#
# # 2 radians = 114.59 degrees
# print(math.degrees(2))
#
# # 60 degrees = 1.04 radians
# print(math.radians(60))
#
# # Sine of 2 radians
# print(math.sin(2))
#
# # Cosine of 0.5 radians
# print(math.cos(0.5))
#
# # Tangent of 0.23 radians
# print(math.tan(0.23))
#
# # 1 * 2 * 3 * 4 = 24
# print(math.factorial(4))
#
# # importing built in module random
# import random
#
# # printing random integer between 0 and 5
# print(random.randint(0, 5))
#
# # print random floating point number between 0 and 1
# print(random.random())
#
# # random number between 0 and 100
# print(random.random() * 100)
#
# List = [1, 4, True, 800, "python", 27, "hello"]
#
# # using choice function in random module for choosing
# # a random element from a set such as a list
# print(random.choice(List))
#
# # importing built in module datetime
# import datetime
# from datetime import date
# import time
#
# # Returns the number of seconds since the
# # Unix Epoch, January 1st 1970
# print(time.time())
#
# # Converts a number of seconds to a date object
# print(date.fromtimestamp(999990))

# ==================================================================================================
# import time
# st = time.time()
# def count_letters(x):
#     print(list(x))
#     return len(x)
# map_obj = map(count_letters,['bacon','toast','egg'])
# et = time.time()
#
# slt=time.time()
# def count_letters(x):
#     print(x)
#     return len(x)
# map_obj = map(count_letters,['bacon','toast','egg'])
# elt = time.time()
# # map_obj = list(map(lambda x: len(x), ['bacon','toast','egg']))
# print(list(map_obj))
# print('list ',elt-slt)
# print('string ',et-st)

# ==================================================================================================
# 31 Oct
# ==================================================================================================
# Hacker Rank
# spChar = '[@!#$%^&*()<>?}{~:]'
# userinput = ['rink5678i','_shivani','hello%']
# for un in userinput:
#     for letter in un:
#         if letter in spChar:
#             print('invalid ',letter)
#             break
#         else:
#             continue
#     if un.isalnum():
#         alphaNum = True
#
# website for website in domain if


# userName = list(map(lambda u : u.isalnum() or spChar, userinput))
# print(' '.join(userName))


# ==================================================================================================
# Lamda funtion

# n = [0,1,2,3,4,5]
# fibo = list(map((lambda x: x), n))
# print(fibo)

# def cube(x): return x* x * x

# def word():
#     prit('hello')
# def fibonacci(n):
#     count = 0
#     a=1
#     b=0
#     fibonacciList = []
#     while count <= (n-1):
#         print(b)
#         count+=1
#         fibonacciList.append(b)
#         a,b=b,a+b
#
#     print("list ", fibonacciList)
#     return fibonacciList
#
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
# word()

# from functools import reduce
# li = [5, 8, 10, 20, 50]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# final_list = list(filter(lambda x: (x % 2 != 0),li))
# print(final_list)

# Python 3 code to people above 18 yrs
# ages = [13, 90, 17, 59, 21, 60, 5]
# adults =  list(filter(lambda age: age > 18, ages))
# print(adults)
# ==================================================================================================
# List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
#
# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)

# # Get the second largest element
# secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
# res = secondLargest(List, sortList)
# print(res)
# ==================================================================================================
# Max = lambda a, b : a if(a > b) else b
# print(Max(9,0))
# ==================================================================================================

# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#
# # iterate on each lambda function
# # and invoke the function to get the calculated value
# for item in is_even_list:
#     print(item())
# ==================================================================================================
# format_numeric = lambda num: f"{num:e}" if isinstance(num, int) \
# else f"{num:,.2f}"
#
# print("Int formatting:", format_numeric(1000000))
# print("float formatting:", format_numeric(999999.789541235))

# ==================================================================================================
# def personDetails(name, *hobbies, **edu):
#     print(name)
#     print(hobbies)
#     print(edu)
# # personDetails('rinki', 'Coding',' Painting', Bachlors = 'BCA',
# Masters = 'MScIT')
# # details = True
# while True:
#     n = input('Enter details: ')
#     if len(n.strip) == 0:
#         break
#
# personDetails(n)
# ==================================================================================================
# रींकि using unicode
# k =  chr(2352), chr(2368), chr(2306), chr(2325), chr(2367), chr(2358),
# chr(2348)
# print(''.join(k))
# print(type(k))
# ==================================================================================================
# import time
# defst=time.time()
# def cube(x): return x * x * x
# defet=time.time()
#
# lmbdst=time.time()
#
# cube_v2 = lambda x: x * x * x
# lmbdet=time.time()
#
# print(cube(7))
# print(cube_v2(7))
# print('def time ',defet-defst)
# print('lambda time ',lmbdet-lmbdst)
# ==================================================================================================

# *args for variable number of arguments
# def myFun(**kwargv):
#     for arg in kwargv.items():
#         print(arg)
# myFun(Hello= 'rinki', to='GeeksforGeeks')

# ==================================================================================================
# Print Diamond shape

# k = 5
# for row in range(5):
#     for col in range(k):
#         print(' ',end='')
#     k -=1
#     for col in range(row+1):
#         print('* ',end='')
#     print()
# k = 0
# for row in range(6,0,-1):
#     for col in range(k):
#         print(' ',end='')
#     k +=1
#     for col in range(row):
#         print('* ',end='')
#     print()

# 30 Oct
# ==================================================================================================
# Print 'Z'

# for row in range(6):
#     for col in reversed(range(6)):
#         # k = 0
#         if row == 0 or row == 5 or (col == row):
#             print('*',end='')
#             # k += 1
#             # print(k)
#         else:
#             print(' ',end='')
#     print('\r')

# ==================================================================================================

# 23. Write a Python program to print the alphabet pattern 'O'

# for row in range(6):
#     for col in range(9):
#         if ((col == 0 or col == 8) and (row <5 and row > 0))
# or ((row == 0 or row == 5)
# and (col < 7 and col > 1)):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('\r')


# ==================================================================================================
# 22. Write a Python program to print the alphabet pattern 'M'.

# for row in range(8):
#     for col in range(11):
#         if (col == 0 or col == 10) or (row == 2 and (col == 2 or col == 8))
# or (row == 3 and col == 5):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('\r')

# ==================================================================================================
# k = 5
# for i in range(8):
#     for j in range(i):
#         print('*',end='')
#     print()
# for i in range(6):
#     for j in range(k):
#         print('*',end='')
#     k -= 1
#     for j in range(k,0,-1):
#         print('*',end='')
#     print(" ")

# ==================================================================================================
# 20. Write a Python program to print the alphabet pattern 'G'.

# for row in range(8):
#     for col in range(6):
#         if (row == 3 and col > 2 and col < 6) or (col == 5 and
#           (row == 1 or row == 4 or row == 5))
#           or ((row == 0 or row == 6) and col > 1 and col < 5) or
#           (col == 0 and row > 0 and row < 6) :
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('\r')

# ==================================================================================================

# Write a Python program to print the alphabet pattern 'E'.

# for row in range(7):
#     for col in range(8):
#         if col == 0 or (row == 0 and col < 8) or (row == 3 and col < 6) or
#           (row == 6 and col < 8):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('\r')

# ==================================================================================================
# 18. Write a Python program to print the alphabet pattern 'D'.

# for row in range(10):
#     for col in range(10):
#         if (col == 0 or (col == 9 and row != 0 and row != 9) or
#           (row == 0 and col < 9)
#  or (row == 9 and col < 9)):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('\r')

# ==================================================================================================
# Print | |

# for row in range(6):
#     for col in range(10):
#         if col == 0 or col == 9:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print('\r')
# ==================================================================================================
# 21. Write a Python program to print the alphabet pattern 'L'.
# Expected Output:
# for row in range(7):
#     for col in range(5):
#         if col == 0 or row == 6:
#             print('*', end='')
#         else:
#             pass
#     print('\r')
# print(res)


# ==================================================================================================

# 17. Write a Python program to print the alphabet pattern 'A'.
# Expected Output:
#
#   ***
#  *   *
#  *   *
#  *****
#  *   *
#  *   *
#  *   *

# res = ''
# for row in range(7):
#     for col in range(7):
#         if((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3)
#  and (col > 1 and col < 5)):
#             res += '*'
#         else:
#             res += ' '
#     res += '\n'
# print(res)


# ==================================================================================================
# 15. Write a Python program to check the validity of passwords input by users.
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# input_password = input("Enetr password: ")
# specialchar = '[@_!#$%^&*()<>?}{~:]'
# def passwordValidity(pwd):
#     '''Funtion to check password is valid or not'''
#     if len(pwd) >= 6 and len(pwd) <= 16:
#         countalphalower = countalphaupper = countnum = countspcl = 0
#         for p in pwd:
#             if p.isalpha() and p.islower():
#                 countalphalower += 1
#                 # print(p)
#             elif p.isalpha() and p.isupper():
#                 countalphaupper += 1
#             elif p.isnumeric():
#                 countnum += 1
#             elif p in specialchar:
#                 countspcl += 1
#             else:
#                 pass
#     else:
#         print("password length should be between 6 and 16!")
#     if countnum > 0 and countalphalower > 0 and countalphaupper > 0
#       and countspcl > 0:
#         print("Valid Password!")
#     else:
#         print("invalid Password!")
#     print(countnum, countalphalower, countalphaupper, countspcl)
# passwordValidity(input_password)
# print(passwordValidity.__doc__)

# ==================================================================================================
# 14. Write a Python program that accepts a string and calculates the number
# of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

# user_input = input("Enter alphanumeric word to count digits and lettes:  ")
# def digitsAndLetters(word):
#     countAlpha = countNum = 0
#     for s in word:
#         if s.isalpha():
#             countAlpha += 1
#         elif s.isnumeric():
#             countNum += 1
#             print(s)
#     print("Letters ", countAlpha)
#     print("Digits ", countNum)
# digitsAndLetters(user_input)

# ==================================================================================================
# stud = 'Joshua'  # Global variable
# roll_no = 26  # Global variable
# roll_no = roll_no + 4
# print(roll_no)
# def display():
#     global roll_no
#     roll_no = roll_no + 4
#     # Updating 1 global variable in local function
#     print('Inside display() student roll_no value:', roll_no)
# display()
# print('Global variable roll_no value:', roll_no)

# ==================================================================================================
# count = 5
# def some_method():
#     global count
#     count = count + 1
#     print(count)
#     return count
# some_method()
# ==================================================================================================
#  Built-in Scope Example
# from math import pi
# def example():
#     def example_inner():
#         print(pi," pi")
#     print(pi)
#
#     example_inner()
#
# example()
# print(pi)
# ==================================================================================================
# Global Scope Example

# str = "global function"
# def example():
#     def example_inner():
#         print(str)
#     print(str)
#     example_inner()
# example()
# ==================================================================================================
# Enclosing (or nonlocal) Scope Example

#     x="outer function"
#
#     def example_inner():
#         y="inner function"
#         print(f"{x} // {y}")
#     print(x)
#     example_inner()
# example()

# ==================================================================================================
# Local (or Function) Scope Example
# def example():
#     x="LEGB rule"
#     print(x)
#
# example()
#
# print(x)

# 29 Oct
# ==================================================================================================

# 13. Write a Python program that accepts a sequence of comma separated 4 digit
# binary numbers as its input.
# The program will print the numbers that are divisible by 5 in a comma
# separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

# binList = input().split(',')
# # list(binList)
# for n in binList:
#     deciN = int(n,2)
#     if deciN % 5 == 0:
#         print(n)

# =================================================================================================

# 28 Oct 23
# ==================================================================================================

# 12. Write a Python program that accepts a sequence of lines (blank line to
# terminate) as input
#  and prints the lines as output (all characters in lower case).

# import time
# cs=time.time()
# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.lower())
#     else:
#         break;
# for l in lines:
#     print(l)
# ce=time.time()
#
# rs=time.time()
# inputList = []
# while True:
#     L = input()
#     if len(L.strip()) == 0:
#         break
#     inputList.append(L.lower())
# for w in inputList:
#     print(w)
# re=time.time()
#
# print(re-rs," rinki took")
# print(ce-cs," computer took")
# ==================================================================================================

# 11. Write a Python program that takes two digits m (row) and n (column) as
# input and generates a two-dimensional array.
#  The element value in the i-th row and j-th column of the array should be
# i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# m,n = map(int, input('Enter row and column with space: ').split())
# num = [[0 for j in range(n)] for i in range(m)]
# for i in range(m):
#     for j in range(n):
#         # print((i*j),end=',')
#         num[i][j] = i*j
# print(num)

# ==================================================================================================

# 10. Write a Python program that iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for multiples
# of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".

# for n in range(0,51):
#     if n%3==0 and n%5==0:
#         print("FizzBuzz")
#     elif n%5==0:
#         print("Buzz")
#     elif n%3==0:
#         print("Fizz")
#     else:
#         print(n)

# ==================================================================================================

# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# a,b = 0,1
# while b<50:
#     print(b)
#     a, b = b , a+b

# ==================================================================================================

# Write a Python program that prints all the numbers from 0 to 6 except
# 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# for num in range(0,7):
#     if num == 3 or num == 6:
#         continue
#     print(num)

# ==================================================================================================
# 7. Write a Python program that prints each item and its corresponding type
# from the following list
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
# [5, 12], {"class":'V', "section":'A'}]

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
# {"class":'V', "section":'A'}]
# out = [(data,(type(data))) for data in datalist]
# print(out)

# ==================================================================================================
# 6. Write a Python program to count the number of even and odd numbers in a
# series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = 0
# odd = 0
# for num in numbers:
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1
# print('Number of even numbers :',even, ' \nNumber of odd numbers :', odd)

# 27 Oct 2023
# ==================================================================================================
# 5. Write a Python program that accepts a word from the user and reverses it.

# userinput = input("Enter a string to reverse it: ")
# reversedstring = []
# for letter in reversed(userinput):
#     reversedstring.append(letter)
# print(''.join(reversedstring))

# s1 = 'yash'
# s2 = s1[::-1]
# print(s2)
# ==================================================================================================
# 4. Write a Python program to construct the following pattern, using a nested
# for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(6):
#     for j in range(i):
#         print('*', end=' ')
#     print()
# for i in range(5,1,-1):
#     for j in range(i,1,-1):
#         print('*', end=' ')
#     print()

# ==================================================================================================
# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until
# the guess is correct,
# on successful guess, user will get a "Well guessed!" message,
# and the program will exit.

# import random
# random_number = random.randint(1,10)
# guess = False
# while guess is False:
#     userInput = int(input('Guess an integer between 1 to 9: '))
#     if userInput != random_number:
#         guess = False
#     else:
#         guess = True
#         print("Well Guessed")

# ==================================================================================================
# 2. Write a Python program to convert temperatures to and from Celsius
# and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and
# f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# tempScale = input("Write C for Celsius and F for Fahrenheit: ").upper()
# if tempScale in ['C','F']:
#     temp = float(input("Enter temperature"))
#     if tempScale == 'C':
#         convertedTemp = (temp*(9/5))+32
#     elif tempScale == 'F':
#         convertedTemp = (temp-32)*(5/9)
#     print("Converted Temparature: ",convertedTemp)
# else:
#     print("Try again!")

# ==================================================================================================
# 1. Write a Python program to find those numbers which are divisible by 7 and
# multiples of 5, between  1500 and 2700 (both included).
# l1 = [1505,1540,1575,1610,1645,1680,1715,1750,1785,1820,1855,1890,1925,1960,
# 1995,2030,2065,2100,2135,2170,2205,2240, 2275,2310,2345,2380,2415,2450,2485,
# 2520,2555,2590,2625,2660,2695 ]
# print(len(l1))
# result = [number for number in range(1500,2701) if number%7 == 0 and
# number%5 == 0]
# print(len(result))

# ==================================================================================================

# Time comparision between list comprehension and for loop
# startCompre = time.time()
# comprehensionList = [[x,x**2] for x in range(6)]
# endCompre = time.time()
#
# startForloop = time.time()
# forloopList = []
# for x in range(6):
#     x = x**2
#     forloopList.append(x)
# endForloop = time.time()
#
# print(comprehensionList)
# print(endCompre-startCompre)
# print(forloopList)
# print(endForloop-startForloop)


# tuple1 = (1,2,3,4)
# list1 = [1,2,3,4]
# mixedCompre = [k:v for k,v in zip(tuple1,list1)]
# print(tuple1)


# a = {1: 'edureka' , 2: 'data science'}
# b = {1: 2, 2: 3, 3: 'python'}
# c = {1: 'edureka' , 2: 'data science'}
# res = a.fromkeys(b)
# print(res)
# this will get the dictionary with the specified keys and values.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data = [x & 1 for x in range(1,10)]
# print(data)
# 79
