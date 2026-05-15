''' Tuple
    (1) What is tuple: typle vs list
    (2) Unpacking arguments
    (3) zip
'''

print("========== What is tuple: tuple vs list ==========")
# Java/PHP/NodeJs array => Python list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("MIT")

fruits = ["apple", "banana", "orange", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple
animals = ("dog", "cat", "rabbit", "fish")
tuple_obj = ("MiT", 100, True, None)

print(animals[0])
# animals[0] = "bird"
