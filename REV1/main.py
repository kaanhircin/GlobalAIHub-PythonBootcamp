my_name = 'Kaan'
my_surname = 'Hırçın'
my_age = 24
ID_number = 123456789
where_i_live = 'Zonguldak'
# health_insurance = True
my_nationality = 'Turkish'

print(f"\nMy name is {my_name} {my_surname}. I'm {str(my_age)} years old. I live in {where_i_live}")

item_list = ['Laptop', 'Headset', 'Second monitor', 'Mouse', 'Mousepad', 'USB drive', 'External driver']

mandatory_item_list = item_list[0:3] # or item_list[:3]

optional_item_list = item_list[3:] # or item_list[3:7]

print(f"\nMy mandatory items are {mandatory_item_list} and optional items are {optional_item_list}\n")

# Function Example
limit = 5000

price_sheet = {
    'Laptop': 1500,
    'Headset': 100,
    'Second monitor': 200,
    'Mouse': 100,
    'Mousepad': 50,
    'USB drive': 70,
    'External driver': 250,
}

cart = []

def add_to_cart (item, quantity):
    cart.append((item, quantity))
    item_list.remove(item)
    
def create_invoice():
    total_amount_inc_tax = 0
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.18 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print('Item: ', item, '\t', 'Price: ', price, '\t', 'Quantity: ', quantity, '\t', 'Tax: ', tax, '\t', 'Total: ', total, '\n' )
    
    print("After the taxes are applied the total amount is: ", '\t', total_amount_inc_tax)
    return total_amount_inc_tax

def checkout():
    global limit
    total_amount = create_invoice()
    if limit == 0:
        print("\nYou don't have any budget.")
    elif total_amount > limit:
        print("\nThe amount you have to pay is above the spending limit. You have to drop some items.")
    else:
        limit -= total_amount
        print(f"\nThe total amount (incl. taxes) you've paid is {total_amount}. You have {limit} dollars left.")

add_to_cart('Laptop', 1)
add_to_cart('Headset', 8)
add_to_cart('Second monitor', 1)
add_to_cart('Mouse', 1)
add_to_cart('Mousepad', 1)
add_to_cart('USB drive', 2)
add_to_cart('External driver', 4)

checkout()
