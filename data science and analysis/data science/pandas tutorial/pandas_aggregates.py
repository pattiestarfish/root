# Calculating column statistics                         General syntax:
mean: Average of all values in column                   df.column_name.command()
std: Standard deviation                                 df.groupby('column1').column2.measurement()
median: Median
max: Maximum value in column
min: Minimum value in column
count: Number of values in column
nunique: Number of unique values in column
unique: List of unique values in column
#--------------------------------------------------------
orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max()

num_colors = orders.shoe_color.nunique()

# output Series
pricey_shoes = orders.groupby('shoe_type').price.max()
# groupby almost always linked with reset_index(); reverts output to DataFrame
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

# np.percentile calculates percentile over an array of values
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()

# Grouping by multiple columns
df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Returns total quantity of shoes sold based on type and color
shoe_counts = orders.groupby(['shoe_type','shoe_color'])['id'].count().reset_index()

# Reorganizing tables -- Pivot Syntax
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')

shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id').reset_index()


click_source = user_visits.groupby('utm_source')['id'].count().reset_index()
# alternatively
click_source = user_visits.groupby('utm_source').id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(
  columns ='month',
  index = 'utm_source',
  values = 'id').reset_index()