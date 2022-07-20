file = open("employee_revenue.txt", "r")
data = file.read()

print("\n", data, "\n")

# DATA CLEANING

print("--- FOR THE FIRST LINE ---\n")

# Seperate the data into line
lines = data.splitlines()
print(lines)

# Cleaning the data line by line
string = lines[0]
print(string)

# Remove the whitespaces from the edges
string = string.strip(" ")
print(string)

# Convert to string to lowercase
string = string.lower()
print(string)

# Capitalize the first character
string = string.capitalize()

# Split the sentences into words
split_string = string.split(" ")
print(split_string)

# Use the index 0 to access the name element
name = split_string[0]
print(name)

# Use the index 2 to access the number of calls element
call_number = split_string[2]
print(call_number)

# Find the element with the "$" sign
for i in split_string:
    # Divide the number from it
    if "$" in i:
        average_deal_size = i.split("$")[0]
        
print(average_deal_size)

# Find the index of element 'dollars'
dollars_index = split_string.index("dollars")
print(dollars_index)

# Substract one from the index to identify index of the revenue element
revenue_index = dollars_index - 1
print(revenue_index)

# Extract the revenue
revenue = split_string[revenue_index]
print(revenue)

# Print out the extracted information
print("Name: ", name)
print("Number of calls: ", call_number)
print("Average deal size: ", average_deal_size)
print("Revenue: ", revenue)

# Check the data types
print("Name type: ", type(name))
print("Number of calls type: ", type(call_number))
print("Average deal size type: ", type(average_deal_size))
print("Revenue type: ", type(revenue))

# Convert to datatypes
average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)

# Check the data types again
print("Name type: ", type(name))
print("Number of calls type: ", type(call_number))
print("Average deal size type: ", type(average_deal_size))
print("Revenue type: ", type(revenue))


"""
# Create empty lists for these
names = []
call_numbers = []
average_deal_sizes = []
revenues = []

# --- FOR ALL LINES ---

# Loop over the whole data
for employee in lines:
    
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()
    
    split_employee = employee.split(" ")
    name = split_employee[0]
    call_number = split_employee[2]
    
    for i in split_employee:
        if "$" in i:
            average_deal_size = i.split("$")[0]
    
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]
    
    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)
    
    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)

print("Names: ", names)
print("Number of calls: ", call_numbers)
print("Average deal sizes: ", average_deal_sizes)
print("Revenues: ", revenues)

"""

# --- BUILD AGAIN WITH FUNCTION ---
print("\n--- FOR ALL LINES BUILD WITH FUNCTION ---\n")

names = []
call_numbers = []
average_deal_sizes = []
revenues = []

# Define a function to clean and extract the data 
def clean_extract(lines):

    for employee in lines:
    
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()
        
        split_employee = employee.split(" ")
        name = split_employee[0]
        call_number = split_employee[2]
        
        for i in split_employee:
            if "$" in i:
                average_deal_size = i.split("$")[0]
        
        dollars_index = split_employee.index("dollars")
        revenue_index = dollars_index - 1
        revenue = split_employee[revenue_index]
        
        average_deal_size = int(average_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)
        
        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)
    
    return names, call_numbers, average_deal_sizes, revenues


names, call_numbers, average_deal_sizes, revenues = clean_extract(lines)

print("Names: ", names)
print("Number of calls: ", call_numbers)
print("Average deal sizes: ", average_deal_sizes)
print("Revenues: ", revenues)

# print(len(names))

IDs = list(range(0,11))
# print(len(IDs))

dictionary1 = dict(zip(IDs, names))
print(dictionary1)

dictionary2 = dict(zip(revenues, names))
print(dictionary2)

print("\n")

# Find the lowest performing employees (ascending order)
sorted_dictionary = sorted(dictionary2)[0:3]
for i in sorted_dictionary:
    print(dictionary2[i])

print("\n")

# Find the best performing employees (descending order)
sorted_dictionary2 = sorted(dictionary2, reverse = True)[0:3]
for i in sorted_dictionary2:
    print(dictionary2[i])