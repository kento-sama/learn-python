def my_function():
    print("Hello from my function")


# my_function()


def my_function_with_args(username, greetings):
    print("%s, %s!" % (greetings, username))


# my_function_with_args("Kent", "Hello")


def sum_two_numbers(num1, num2):
    return num1 + num2


x = sum_two_numbers(3, 5)
# print(x)


def list_benefits():
    return [
        'More organized code',
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]


def build_sentence(info):
    return info + " is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefits in list_of_benefits:
        pass
        # print(build_sentence(benefits))


# name_the_benefits_of_functions()
