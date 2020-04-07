# What is Pandas module?
# Performs actions on tabular data (table with rows and columns)

# Creating a Dataframe: stores data as rows and columns (similar to spreadsheet or SQL table)
# Dataframes contain columns (string name) and rows (int index); can contain any data types


# Adding data with dictionaries: pass dictionary with equal length column
# (key = column name, value = column values)
df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})
# Dictionaries passed in have their columns alphabetized by default

import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue','green','red','black']
})
print(df1)

# Adding data with lists: can pass list of lists [[]] as values, and use keyword argument columns to assign headers
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns = [
    'Store ID',
    'Location',
    'Number of Employees'
  ])
print(df2)