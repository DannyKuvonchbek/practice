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

# try avoid thse
people = "Andrew", "John"
animals = "dog",

print("========== Unpacking arguments ==========")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list

# *args > tuple


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("==========")
calculate(4, 5, 300)
print("====================")
calculate(5, 7)
