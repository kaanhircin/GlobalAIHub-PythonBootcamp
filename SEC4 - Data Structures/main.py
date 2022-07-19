# LISTS - Mutable

shopping_list = ['Apple', 'Ball', 'Book', 'Juice']

shopping_list.append('Water')
print(shopping_list)
print(shopping_list[0])

shopping_list.insert(2, 'Banana')
print(shopping_list)

shopping_list.remove('Apple')
print(shopping_list)

shopping_list[3] = 'Strawberry'
print(shopping_list)

number_list = [1, 2, 3, 4, 5]
square_list = []
for num in number_list:
    square_list.append(num**2)
    
print(square_list)

square_list2 = [num**2 for num in number_list]
print(square_list2)



# TUPLES - Immutable

cars = tuple(['BMW', 'Ford', 'Opel', 'Citroen', 'Fiat'])

item1, item2, item3, item4, item5 = cars

print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

print(cars[1])

print(cars[1:4])

# cars[1] = "Volkswagen" # ERROR

print(cars)



# DICTIONARIES

school_numbers = {'Kaan Hırçın': '160202032', 'Özkan Kayış': '160218110'}

print(school_numbers)

print(school_numbers['Kaan Hırçın'])
print(school_numbers['Özkan Kayış'])


inventory = dict()
inventory['Bananas'] = 25
inventory['Apples'] = 16
inventory['Orange'] = 37

print(inventory)
print(inventory['Apples'])

print(inventory.keys())
print(inventory.values())
print(inventory.items())

for element in inventory:
    print(element)
    
for key in inventory:
    inventory[key] += 100

print(inventory)

for key, value in inventory.items():
    if value > 100:
        print('Too many', key)
    else:
        print('Enough', key)