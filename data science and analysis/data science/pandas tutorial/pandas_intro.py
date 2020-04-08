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

# Working with CSVs
# first line contains column headings, subsequents are row values
name,cake_flavor,frosting_flavor,topping
Devil's Food,chocolate,chocolate,chocolate shavings
Birthday Cake,vanilla,vanilla,rainbow sprinkles
Carrot cake,carrot,cream cheese,almonds

# Loading and Writing(saving) csvs
df = pd.read_csv('my-csv-file.csv')
df.to_csv('new-csv-file.csv')

# Inspecting DataFrames
# small dfs can be examined using print(), use .head(n) to display 1st n rows
# df.info() displays column stats
df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())

# Select columns from dfs
# Can select similarly to keys from dict df['column_name'] or var = df.column_name
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df['clinic_north']
clinic_north = df.clinic_north
# Output is converted into a Series

# Selecting 2+ columns from dfs requires list of col names: [[]]
clinic_north_south = df[['clinic_north', 'clinic_south']]
# Output STAYS THE SAME (remains df)

# Selecting entire rows with .iloc[], (0 indexed, output Series)
march = df.iloc[2]
# Selecting multiple rows (does not include upper limit)
april_may_june = df.iloc[3:6]

# Selecting rows with logic
january = df[df.month == 'January']

# | = or, & = and; PARENTHESES REQUIRED
march_april = df[(df.month == 'March') | (df.month == 'April')]
january_february_march = df[df.month.isin(['January','February','March'])]

# Subsets of data and resetting indices
# Select subset from DataFrames using logic results in non-consecutive indices
# call method .reset_index() to 0 index new df
df2 = df.loc[[1, 3, 5]]
df3 = df2.reset_index()
# Alternatively can substitute in place:
df2.reset_index(inplace=True,drop=True)