class MyClass:
    variable = "variable"

    def __init__(self, number=0):
        self.number = number

    def return_number(self):
        return self.number

    def function(self):
        print("This is a message inside a class")


myobject = MyClass()


print(myobject.variable)
myobject.variable = "hello world"
print(myobject.variable)

myobject.function()

var = MyClass(20)
print(var.return_number())


class Vehicle:

    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        des_str = "%s is a %s %s worth $%.2f." %(self.name, self.color, self.kind, self.value)
        return des_str


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

print(car1.description())
print(car2.description())
