# ordered extra arguments
# def foo(first, second, third, *the_rest):
#     print("First: %s" % first)
#     print("Second: %s" % second)
#     print("Third: %s" % third)
#     print("And all the rest . . . %s" % list(the_rest))
#
#
# foo(1, 2, 3, 4, 5)

# undordered extra arguments
# def bar(first, second, third, **the_rest):
#     if the_rest.get("action") == "sum":
#         print("The sum is: %d" % (first + second + third))
#     if the_rest.get("number") == "first":
#         return first
#
#
# result = bar(1, 2, 3, action="sum", number="first")
# print("Result: %d" % result)


def foo(a, b, c, *d):
    return len(d)


def bar(a, b, c, **d):
    return d.get("magicnumber") == 7


if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1,2,3, magicnumber=6) == False:
    print("Great.")
if bar(1,2,3, magicnumber=7) == True:
    print("Awesome!")
