def transmit_to_space(message):
    """This is the enclosing function"""
    def data_transmitter():
        """The nested function"""
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


def print_msg(number):
    def printer():
        """Here we are using the nonlocal keyword"""
        nonlocal number
        number = 3
    printer()
    print(number)


print_msg(9)


def transmit_to_space(message):
    """This is the enclosing function"""
    def data_transmitter():
        """The nested function"""
        print(message)

    # return as unexecuted function by returning function name without the parenthesis
    return data_transmitter


fun2 = transmit_to_space("Hello")
# fun2 function is the inner function that's returned by transmit_to_space function
fun2()


def multiplier_of(number):
    def multiplier(n):
        return n * number
    return multiplier


multiplywith5 = multiplier_of(5)
# multiplywith5 function is the inner function that's returned by multiplier_of function
print(multiplywith5(9))
