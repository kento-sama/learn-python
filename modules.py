# PYTHONPATH=/folder_name python file_to_import.py

# import a file as an object
# import functions
# functions.my_function()

# print the objects, functions and variables that are imported from file
# print(dir(functions))

# import a file as an object with alias
# import functions as test
# test.my_function()

# import a function from a file. The imported functions will become a part of this file
# from functions import my_function, sum_two_numbers


# my_function()
#
# x = sum_two_numbers(3, 8)
# print(x)

import re

find_members = []
for x in dir(re):
    if "find" in x:
        find_members.append(x)

print(find_members)
