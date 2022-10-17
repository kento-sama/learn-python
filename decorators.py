def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper


@f1
def f(a):
    print(a)


# f1(f)()

# f = f1(f)
# f()
f("Hello")


def multiply(multiplier):
    def multiply_generator(func):
        def wrapper(*args, **kwargs):
            # print(multiplier) # 3
            # print(old_function(*args, **kwds)) # 5
            return multiplier * func(*args, **kwargs)
        return wrapper
    return multiply_generator # it returns the new generator


@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# return_num function calls multiply(3) then becomes the inner function
print(return_num(5))


print("--------------")


def type_check(correct_type):
    def type_check_decorator(func):
        def wrapper(*args, **kwargs):
            print(*args)
            if isinstance(*args, correct_type):
                return func(*args)
            else:
                print("Bad Type")
        return wrapper
    return type_check_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2("Not A Number")


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter("Hello World"))
first_letter(["Not", "A", "String"])