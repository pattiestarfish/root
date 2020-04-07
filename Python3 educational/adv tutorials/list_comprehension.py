temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_F = [(9.0/5.0)*temp + 32 for temp in temperatures]

#creating multiple lists of x-values for graphs
#matplotlib default bar width is 0.8; 1st bar = 0.0, 2nd = 0.8, 3rd = 2.0, 4th = 2.8
#x-values for groups of bar graphs
x_values_1 = [2*index for index in range(5)]
# [0.0, 2.0, 4.0, 6.0, 8.0]
x_values_2 = [2*index + 0.8 for index in range(5)]
# [0.8, 2.8, 4.8, 6.8, 8.8]

#finding labels for bar graphs @ midpoint
x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]
# [0.4, 2.4, 4.4, 6.4, 8.4]

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name=='Jerry' for name in names]

nums = [5, -10, 40, 20, 0]
greater_than_two = [nums[i]>2 for i in range(len(nums))]

a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [item1 > item2 for (item1, item2) in zip(a,b)]

nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [item1*item2 for (item1,item2) in nested_lists]

#True if 1st num in list > 2nd num
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [nested_list[0] > nested_list[1] for nested_list in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [nested_list[0] for nested_list in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [item1 + item2 for (item1, item2) in zip(a, b)]
#sums[0]=5

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [item2/item1 for item1, item2 in zip(a,b)]

###Tuples: similar to lists, but elements cannot be changed once assigned (can contain any number of items of varying types); tuples can be created with or without parentheses (need trailing comma to create single var tuple)
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

location = zip(capitals, countries)
print(location)
print(type(location))
#output: [('Santiago', 'Chile'), ('Paris', 'France'), ('Copenhagen', 'Denmark')]
#<type 'list'>

locations = [capital + ', ' + country for capital, country in zip(capitals,countries)]
print(locations)
print(type(locations))
#output: ['Santiago, Chile', 'Paris, France', 'Copenhagen, Denmark']
#<type 'list'>

test_tuple = (1,2,'hi')
print(type(test_tuple))
#<type 'tuple'>
test_list = [1, 'hi']
print(type(test_list))


names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]
users = ["Name: " + name + ', Age: ' + str(age) for (name, age) in zip(names,ages)]
