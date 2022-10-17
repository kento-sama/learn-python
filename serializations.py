import json
import pickle

# json dumps function converts the list to string
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# pickle dumps function converts the list into stream of bytes
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickled_string)


def add_employee(salaries_json, name, salary):
    loaded_salaries = json.loads(salaries_json)
    loaded_salaries[name] = salary
    salaries_json = json.dumps(loaded_salaries)
    return salaries_json


salaries = '{"Alfred" : 300, "Jane": 400}'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
