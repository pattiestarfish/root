# Modifying DataFrames: Adding additional columns, using lambda functions, renaming columns

# Adding columns: input list of same length as existing df
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df["Quantity"] = [100, 150, 50, 35]
df["Sold in Bulk?"] = ['Yes','Yes','No','No']
# Fill in entire column with 1 value
df['Is taxed?'] = 'Yes'

df['Margin'] = df.Price - df['Cost to Manufacture']

# Apply function performs calculations on each row in given column
# Apply keyword axis: 1 applies function to each row, 0 to each column
df['Lowercase Name'] = df.Name.apply(lower)

mylambda = lambda x: x[0] + x[-1]
print(mylambda('Hello'))
# output 'Ho'

mylambda = lambda x: "Welcome to BattleCity!" if x >= 13 else "You must be over 13"

# Obtaining last names from name column (first last)
# split() does not work on Series, only dfs!
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

# Finding email providers- 1 liner
df['Email Provider'] = df.Email.apply(lambda x: x.split('@')[-1])

# Overtime calculator
df = pd.read_csv('employees.csv')
total_earned = lambda row: ((((row.hours_worked - 40) * 1.5 * row.hourly_wage) + (40 * row.hourly_wage)) if row.hours_worked > 40 else row.hours_worked * row.hourly_wage)
df['total_earned'] = df.apply(total_earned, axis=1)

# Alternative:
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked


# Renaming columns
df.columns = ['ID','Title','Category','Year Released','Rating']
# Method 2: allows us to rename individual columns, without inplace creates new df
df.rename(columns={'name':'movie_title'}, inplace=True)

# Cumulative practice
# axis=1 allows input of lambda function to be entire row
shoe_source = lambda row: 'animal' if row.shoe_material == 'leather' else 'vegan'
orders['shoe_source'] = orders.apply(shoe_source,axis=1)

greeting = lambda x: "Dear Mr. " + x.last_name if x.gender == 'male' else "Dear Ms. " + x.last_name
orders['salutation'] = orders.apply(greeting, axis=1)