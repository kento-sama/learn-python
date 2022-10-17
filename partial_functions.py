from functools import partial


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


dbl = partial(multiply, 2)

print(dbl(4))

# partial(function_to_call, for_first_argument)
partial_subtract = partial(subtract, 3)
print(partial_subtract(4))


def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

partial_func = partial(func, 5, 3, 15)

print(partial_func(1))
