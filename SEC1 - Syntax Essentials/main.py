# help()

"""

Comment

"""

print("Hello World")

fav_number = 12
if fav_number < 15:
    print("My favourite number is smaller than 15.")


# STRINGS
name = 'Kaan'
print(name)


# NUMBERS
age = 24
print(age)

print(type(name))
print(type(age))


#LISTS
store_items = ['Apple', 1.49, 'Banana', 1, 'Milk', 2.99, 'Cheese', 4.49]
print(store_items, type(store_items))

print(store_items[1])
print(store_items[0:4])
print(store_items[2:])
print(store_items[:2])

store_items[2] = 'Chocolate'
print(store_items)


# TYPE CONVERSATION
new_age = '25'
print(new_age, type(new_age))

new_age = int(new_age)
print(new_age, type(new_age))


# INPUT FUNCTION
print("Hi, this is Python.")

new_name = 'Ahmet'
print('Hello', new_name)


# OUTPUT FUNCTION
user_name = input('User name: ')
print('Hello', user_name)

"""
number = input('Number: ')
number = int(number)
print("Square of number is", number * number)
"""
number = int(input('Number: '))
print("Square of number is", number * number)


# IMPORT
import math

floor_number = (math.floor(3.9))
print(floor_number)


import datetime

print(datetime.datetime.now())


import random

print("Random number from 1 to 6:", random.randint(1,6))


# ARITMETIC OPERATORS
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2) # Float Division
print("5 / 2 =", 5 / 2)
print("5 ** 2 =", 5 ** 2)   # Exponential
print("5 // 2 =", 5 // 2)   # Normal Division - Int
print("5 % 2 =", 5 % 2)


# ASSIGNMENT OPERATORS
x = 5   # x = 5
x += 5  # x = x + 5
x -= 5  # x = x - 5
x *= 5  # x = x * 5
x /= 5  # x = x / 5


# COMPARISON OPERATORS
num1 = 10
num2 = 5

print(num1, '>', num2, '=', num1 > num2)
print(num1, '>=', num2, '=', num1 >= num2)
print(num1, '<', num2, '=', num1 < num2)
print(num1, '<=', num2, '=', num1 <= num2)
print(num1, '==', num2, '=', num1 == num2)
print(num1, '!=', num2, '=', num1 != num2)


# LOGICAL OPERATORS
# AND OPERATOR
print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)

# OR OPERATOR
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)

# NOT OPERATOR
print("not True =", not True)
print("not False =", not False)