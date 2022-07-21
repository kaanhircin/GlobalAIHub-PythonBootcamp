import pandas as pd
import numpy as np

last_year = pd.read_csv("employee_revenue_lastyear.csv")

print(last_year)
print()

print(last_year.head())
print()
print(last_year.head(8))
print()
print(last_year.tail())
print()
print(last_year.tail(6))
print()
print(last_year.shape)
print()
print(last_year.info())
print()

last_year["Year"] = 2021

print(last_year)
print()

names = np.array(['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude'])
call_numbers = np.array([300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
average_deal_sizes = np.array([8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12])
revenues = np.array([2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500])

dictionary = {"name": names,
              "calls": call_numbers,
              "avg_deal_size": average_deal_sizes,
              "revenue": revenues}

current_year = pd.DataFrame(dictionary)
print(current_year.head())
print()

current_year["Year"] = 2022
print(current_year.head())
print()

current_year.columns = last_year.columns

all_data = pd.concat([last_year, current_year], axis = 0)
print(all_data)
print()

all_data.reset_index(drop = True, inplace = True)
print(all_data)
print()

# Check the DataFrame for missing values
print(all_data.isna().any())
print()

# Replace the missing values with the mean of the respective column
all_data.fillna(value = np.mean(all_data), inplace = True)
print(all_data)
print()

# Drop the duplicates
all_data.drop_duplicates(inplace = True)
print(all_data)
print()

# Reset the indexes again
all_data.reset_index(drop = True, inplace = True)
print(all_data)
print()

print(all_data.describe().T)
print()

print(all_data[all_data["Year"] == 2021].describe().T)
print()
print(all_data[all_data["Year"] == 2022].describe().T)
print()

print(all_data.sort_values(by = "Revenue"))
print()

print(all_data[all_data["Year"] == 2022].sort_values(by = "Revenue"))
print()

print(all_data["Name"].value_counts())
print()