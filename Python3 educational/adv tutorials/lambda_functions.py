#functions: objects that can accept inputs, modify, and returns output
#lambda functions are 1 line shorthand functions, great for single use functions
is_substring = lambda my_string: my_string in "This is the master string"
print(is_substring('am'))
print(is_substring('the'))
#False, True

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

#practice functions:
contains_a =  lambda word: 'a' in word

#returns True if str > 12 characters
long_string = lambda str: len(str)>12

ends_in_a = lambda str: str[-1]=='a'

double_or_zero = lambda num: 2*num if num>10 else 0

even_or_odd = lambda num: "even" if num%2==0 else "odd"

multiple_of_three = lambda num: "multiple of three" if num%3==0 else "not a multiple"

rate_movie = lambda rating: "I liked this movie" if rating>8.5 else "This movie was not very good"

ones_place = lambda num: num%10

double_square = lambda num: 2 * num**2

add_random = lambda num: num + random.randint(1,10)