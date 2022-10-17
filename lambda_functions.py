def sum(a, b):
    return a + b


a = sum(3, 8)
print(a)

# function_name = lambda inputs: output

sum_of_two = lambda x, y: x + y

a = sum_of_two(1, 2)
print(a)

l = [2, 4, 7, 3, 14, 19]
for i in l:
    odd = lambda a : a % 2 == 1
    print(odd(i))
