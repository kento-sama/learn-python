import numpy as np

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

# no comma ??
print(np_height)
print(np_weight)

# with comma ??
print(height)
print(weight)

print(type(np_height))
print(type(height))

# compute each element in the array
bmi = np_weight / np_height ** 2

print(bmi)
print(type(bmi))

# filter values to print
print(bmi[bmi > 27])


weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_kg = np.array(weight_kg)

np_weight_lbs = np_weight_kg * 2.2

print(np_weight_lbs)
