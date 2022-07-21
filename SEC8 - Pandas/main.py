import pandas as pd

my_series = pd.Series([10, 27, 35, 67, 50])

print("\nmy_series size: ", my_series.size)
print("\nmy_series dimension: ", my_series.ndim)
print()
print(my_series.head(2))
print()
print(my_series.tail(2))
print()
print(my_series[2])
print()
print(my_series[0:3])
print()

numbers = [[10, 15, 20, 25, 30], [5, 19, 21, 76, 9]]

df = pd.DataFrame(numbers)
print(df)
print()

import numpy as np

arr = np.array([[1, 10, 19, 17, 15], [55, 105, 75, 90, 25], [23, 17, 31, 35, 67]])

df_arr = pd.DataFrame(arr)

print(df_arr)
print()
print(df_arr.describe())
print()
print(df_arr.describe().T)


"""
dataframe_csv = pd.read_csv("file.csv")
dataframe_txt = pd.read_csv("file.txt")
dataframe_xlsx = pd.read_excel("file.xlsx")
"""