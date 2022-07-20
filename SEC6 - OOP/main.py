# Defining a class
class Employee():
    employee_name = 'Ben'
    department = 'sales'
    starting_year = 2020
    salary = 5000

# Call the class' object
myObject = Employee()

print(myObject.employee_name)
print(myObject.department)
print(myObject.starting_year)
print(myObject.salary)

# Defining a class with '__init__' method and 'self' parameter
class Car():
    def __init__(self, brand, production_year, price):
        self.brand = brand
        self.production_year = production_year
        self.price = price

# Creating an instance (new class' object)
car_1 = Car('Volvo', 2022, 300000)

print(car_1.brand)
print(car_1.production_year)
print(car_1.price)