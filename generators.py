import random
import types


def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)


print(lottery())

for random_number in lottery():
    print("And the next number is... %d!" % random_number)


def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
