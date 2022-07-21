names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

import numpy as np

data = np.array([], dtype = int) # default => float

def append_names (names_list):
    global data
    for i in names_list:
        data = np.append(data, names.index(i))
        
def append_performance_measures(feature_list):
    global data
    data = np.append(data, feature_list)

append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

print()
print(data)
print("\nData shape: ", data.shape)

data = data.reshape(4, 11)

print()
print(data)
print("\nReshaped data shape: ", data.shape)

# Accessing values
print()
print(data[0])
print()
print(data[1])
print()
print(data[2])
print()
print(data[3])

# Print spesific value for ex. => Ellen's revenue
print()
print(data[3,7])

# Analyzing the data
# FORMULA =>    Performance = (Average deal size * Revenue) / Number of calls

def calculate_performance(employee_name):
    idx = names.index(employee_name)
    number_of_calls = data[1, idx]
    average_deal_size = data[2, idx]
    revenue = data[3, idx]
    
    score = (average_deal_size * revenue) / number_of_calls
    return score

print()
print(calculate_performance("Ellen"))

performance_scores = []
for name in names:
    score = int(calculate_performance(name))
    performance_scores.append(score)


data = np.concatenate((data, [performance_scores]), axis = 0) # axis = 0 => vertically adding / axis = 1 => horizontally adding

print()
print(data)

# Determine the worst and best performing employee
idx_worst_employee = np.argmin(data[4])
idx_best_employee = np.argmax(data[4])

print()
print(f"Worst Performing Employee: {names[idx_worst_employee]}")
print(f"Best Performing Employee: {names[idx_best_employee]}")