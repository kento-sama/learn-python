# no duplicates
print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

# intersection function gets the common of 2 sets
print(a.intersection(b))
print(b.intersection(a))

# symmetric_difference function merges the set except for the common
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# difference function gets the set without the common
print(a.difference(b))
print(b.difference(a))

# union function merges the sets
print(a.union(b))
print(b.union(a))

#