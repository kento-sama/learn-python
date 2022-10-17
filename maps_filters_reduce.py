my_pets = ['alfred', 'tabitha', 'william', 'arla']

# for pet in my_pets:
#     pet_ = pet.upper()
#     upper_pets.append(pet_)


# str.upper() has only one argument so there's one iterable
upper_pets = list(map(str.upper, my_pets))

print(upper_pets)


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

# round() has have two arguments so there's two iterables
result = list(map(round, circle_areas, range(1, 7)))

print(result)

# map function will only map stop on the number of items in which all iterables fit
result = list(map(round, circle_areas, range(1, 3)))

print(result)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

# zip function will pair the iterables into tuple
result = list(zip(my_strings, my_numbers))

print(result)

# result is like a zip function
result = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(result)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_a_student(grade):
    return grade > 75


a_studens = list(filter(is_a_student, scores))

print(a_studens)

words = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda x: x == x[::-1], words))

print(palindromes)

from functools import reduce


numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(num1, num2):
    return num1 + num2

# sum of all elements in numbers
result = reduce(custom_sum, numbers)
print(result)

# sum of all elements in numbers + 10
result = reduce(custom_sum, numbers, 10)
print(result)

# exercise
# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
