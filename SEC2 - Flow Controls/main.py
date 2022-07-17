# IF - ELIF - ELSE

# Example 1
celsius = int(input("What is the temperature? => "))

if  -273 <= celsius <= 10:
    print("Cold")
elif 10 < celsius <= 29:
    print("Good")
elif celsius >= 30:
    print("Hot")
else:
    print("Something went wrong!")

# Example 2
age = int(input("How old are you? => "))

if age >= 18:
    drivers_license = input("Please enter 'Y' or 'N' => ")
    if drivers_license == 'Y':
        print("Have a nice ride!")
    elif drivers_license == 'N':
        print("You must have a license to drive a car.")
    else:
        print("Something went wrong!")
else:
    print("You must be over the age of 18 to drive.")



# FOR LOOPS

# Example 1
name = input("Please enter your name: ")
for i in name:
    print(i)
print("Loop is completed")

# Example 2
for j in range(5,10):
    print(j)
print("Loop is completed")

# Example 3 - divisible by 5, from 1 to 100
counter = 0
for k in range(1,101):
    if k % 5 == 0:
        print(k)
        counter += 1
print("Counter = ", counter)
print("Loop is completed")



# WHILE LOOPS

# Example
import time

room_temperature = int(input("What is the room temperature? => "))
if room_temperature < 25:
    while room_temperature < 25:
        room_temperature += 1
        print("The current room temperature is", room_temperature)
        time.sleep(1)
    print("Room temperature set to", room_temperature, "degrees")
elif room_temperature == 25:
    print("Room temperature is already", room_temperature, "degrees")
elif room_temperature > 25:
    while room_temperature > 25:
        room_temperature -= 1
        print("The current room temperature is", room_temperature)
        time.sleep(1)
    print("Room temperature set to", room_temperature, "degrees")
else:
    print("Something went wrong!")



# BREAK INFINITE LOOPS

# Example 1
import random

while True:

    random_number = random.randrange(1000)
    print(random_number)

    if(random_number == 777):
        print("Found!")
        break


# Example 2
names = ["Ahmet", "Mehmet", "Ayberk", 25, "Zeynep"]

for l in names:
    if type(l) != str:
        print("Found", l)
        break
    else:
        print(l, "is a string.")