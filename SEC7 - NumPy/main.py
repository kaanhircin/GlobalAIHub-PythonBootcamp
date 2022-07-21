# pip install numpy

import numpy as np

import time

array = np.array([1, 2, 3, 4, 5])

print(type(array))

revenues = [12000, 2560, 15600, 22000, 4500, 1980]

"""
initial_time = time.time()

sum = 0

for i in revenues:
    sum += i
    
print(sum)

termination_time = time.time()

print("Execution time: ", termination_time - initial_time)
"""

revenues_array = np.array(revenues)

initial_time_array = time.time()

sum_array = revenues_array.sum()

print(sum_array)

termination_time_array = time.time()

print("Execution time: ", termination_time_array - initial_time_array)



x = ["Ben", 5000, "Liz", "Jack", 6000]

for i in x:
    print(type(i))
    
arrayx = np.array(x)

for i in arrayx:
    print(type(i))



two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6]])

print(two_dimensional_array)

# Basic Array Attributes
""" 
.ndim
.shape
.size
"""

print(two_dimensional_array.ndim)
print(two_dimensional_array.shape)
print(two_dimensional_array.size)