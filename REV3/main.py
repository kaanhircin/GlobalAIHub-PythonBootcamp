salesperson_revenue = {
    'Ahmet': 0,
    'Mehmet': 0,
    'Caner': 0,
    'Zeynep': 0,
    'Seda': 0,
    'Ozan': 0,
    'Orhan': 0,
    'Mert': 0
}

def enter_revenue(name, revenue):
    global salesperson_revenue
    salesperson_revenue[name] += revenue
    
while True:
    name = input("\nEmployee name: ")
    
    if name == 'quit':
        break
    
    revenue = int(input("Enter revenue: "))
    
    enter_revenue(name, revenue)
    
    print(f"\n{name}'s revenue is {salesperson_revenue[name]}.")
    
print(salesperson_revenue)