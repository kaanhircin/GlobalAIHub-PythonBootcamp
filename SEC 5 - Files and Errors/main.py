# FILES

# message_file = open("message_file.txt", "r") # to read the file
# message_file = open("message_file.txt", "w") # to write the file
message_file = open("message_file.txt", "r+") # to read & write the file

content = message_file.read()
print(content)
message_file.write(" " + "I'm currently learning Python.")
new_content = message_file.read()
print(new_content)
message_file.close()



# Example
import random

# numbers_file = open("numbers_file.txt", "w")

with open("numbers_file.txt", "w") as numbers_file:

    while True:
        random_number = random.randrange(1000)
        print(random_number)
        numbers_file.write(str(random_number))
        numbers_file.write("\n")
        
        if random_number == 444:
            print("Found!")
            numbers_file.write("Found!")
            numbers_file.close()
            break



# EXCEPTIONS
def divide(number1, number2):
    try:
        number1_integer = int(number1)
        number2_integer = int(number2)
        return number1_integer / number2_integer
    
    except ValueError:
        return "Only integers are allowed! Try again please."
    
    except ZeroDivisionError:
        return "You cannot divide any number by zero!"

number1 = input("First number: ")
number2 = input("Second number: ")

print(divide(number1, number2))