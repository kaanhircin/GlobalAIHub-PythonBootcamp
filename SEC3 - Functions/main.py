# Define a function

# Example 1
def hello(name):
    print("Hello", name)

hello('Kaan')



# Example 2
def sum(number1, number2):
    print(number1 + number2)

number1 = int(input("Please enter number 1: "))
number2 = int(input("Please enter number 2: "))

sum(number1, number2)



# Example 3
def greetings(first_name, last_name, auto_correction):
    if auto_correction == True:
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()
        print("Hello", capitalized_first_name, capitalized_last_name)
    
    else:
        print("Hello", first_name, last_name)

greetings('KaAn', 'HıRÇın', True)
greetings(first_name = 'KaAn', auto_correction = False, last_name = 'HıRÇın')



# Example 4 - Usage 'global'
number = 10

def change_number():
    global number
    number = 4

change_number()
print(number)



# MODULES '.py extension'
import random
from matplotlib.pyplot import plot # for ex. => random.py

# LIBRARIES are collection of MODULES
# pip install seaborn on Terminal
# import seaborn as sns

import seaborn as sns

data = [1, 2, 10, 6, 3, 5, 13]

sns.lineplot(range(7), data)
